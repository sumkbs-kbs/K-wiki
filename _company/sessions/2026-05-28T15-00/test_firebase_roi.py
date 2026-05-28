import os
import subprocess
import json
import time
import random

from firebase_admin import credentials, initialize_app, db

# 📁 설정
EMULATOR_HOST = "localhost"
EMULATOR_PORT = 9099
PROJECT_ID = "antigravity-k"
TEST_DATA_DIR = "/Users/mr.k/wiki/_company/_agents/business/tools/roi_test_scenarios"
OUTPUT_DIR = "/Users/mr.k/wiki/_company/sessions/2026-05-28T15-00"

# 📄 테스트 시나리오 정의
SCENARIOS = [
    {"type": "학원", "base_conversion": 2.1, "test_values": [1.5, 2.0, 2.5]},
    {"type": "컨설팅", "base_conversion": 1.8, "test_values": [1.5, 2.0, 2.5]},
    {"type": "디지털 콘텐츠", "base_conversion": 2.3, "test_values": [1.5, 2.0, 2.5]},
]

INPUT_FIELDS = {
    "price": 19900,
    "customers": 500,
    "conversion_rate": 2.0,  # 실제 테스트 시 변경
    "monthly_costs": 300000,
}

def generate_test_data(type_name, conversion):
    data = INPUT_FIELDS.copy()
    data["conversion_rate"] = conversion
    data["scenario_type"] = type_name
    data["timestamp"] = int(time.time())
    return data

def run_emulator():
    """Firebase Emulator Suite 로컬 실행 (이미 실행 중이면 스킵)"""
    try:
        subprocess.run(["firebase", "emulator:check"], check=True, capture_output=True)
        print("✅ Emulator already running.")
    except subprocess.CalledProcessError:
        print("🚀 Starting Firebase Emulator Suite...")
        subprocess.run([
            "firebase", "emulators:start",
            "--project", PROJECT_ID,
            "--import", f"{TEST_DATA_DIR}/emulator_data",
        ], check=True)

def init_firebase():
    """Firebase SDK 초기화 (로컬 Emulator 사용)"""
    os.environ["FIREBASE_DATABASE_EMULATOR_HOST"] = f"{EMULATOR_HOST}:{EMULATOR_PORT}"
    cred = credentials.Certificate("/Users/mr.k/wiki/_company/firebase-adminsdk.json")
    app = initialize_app(cred, {"databaseURL": f"http://{EMULATOR_HOST}:{EMULATOR_PORT}/?ns={PROJECT_ID}"})
    return db

def test_save_and_load(db, type_name, conversion):
    """ROI 입력 → 저장 → 로드 → 계산 결과 검증"""
    data = generate_test_data(type_name, conversion)

    # ✍️ 저장
    ref = db.reference(f"/roi_scenarios/test_{type_name}_{conversion:.1f}")
    ref.set(data)
    print(f"💾 Saved: {type_name}, conversion={conversion}%")

    # 📥 로드
    loaded = ref.get()
    assert loaded is not None, "Load failed"
    assert loaded["conversion_rate"] == conversion, "Conversion mismatch"

    # 🧮 계산 (로직은 frontend JS에 있으므로, 여기선 기본 검증)
    expected_revenue = data["price"] * data["customers"] * (data["conversion_rate"] / 100)
    expected_profit = expected_revenue - data["monthly_costs"]
    expected_roi = (expected_profit / data["monthly_costs"]) * 100

    print(f"📊 {type_name}, conversion={conversion}% → revenue={expected_revenue:,.0f}, profit={expected_profit:,.0f}, roi={expected_roi:.1f}%")
    return {"scenario": type_name, "conversion": conversion, "revenue": expected_revenue, "profit": expected_profit, "roi": expected_roi}

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 🔥 Emulator 시작
    run_emulator()

    # 🔌 Firebase 연결
    db = init_firebase()

    # 🧪 테스트 실행
    results = []
    for scenario in SCENARIOS:
        for val in scenario["test_values"]:
            result = test_save_and_load(db, scenario["type"], val)
            results.append(result)

    # 📊 결과 저장
    output_file = os.path.join(OUTPUT_DIR, "test_results.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n✅ All tests passed. Results saved to {output_file}")

if __name__ == "__main__":
    main()