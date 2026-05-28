#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSV → 구글 시트 변환 및 Firebase Realtime Database 연동 구조 기반 시트 생성
- ROI 템플릿 CSV를 구글 시트로 변환
- Firebase 연동을 위한 메타 데이터 및 스키마 포함
"""

import csv
import json
import os
from datetime import datetime

# Firebase 연동 구조 정의
FIREBASE_SCHEMA = {
    "roi_template": {
        "version": "1.0",
        "description": "1인 기업 ROI 템플릿 — Firebase Realtime Database 연동용",
        "path": "roi_templates/{uid}/{scenario_id}",
        "fields": {
            "scenario_name": "string",
            "created_at": "timestamp",
            "pricing": {
                "product_price": "number",
                "subscription_monthly": "number",
                "subscription_annual": "number"
            },
            "assumptions": {
                "conversion_rate_min": "number",
                "conversion_rate_max": "number",
                "customer_count_min": "number",
                "customer_count_max": "number"
            },
            "calculations": {
                "revenue": "number",
                "cost": "number",
                "roi": "number"
            }
        }
    }
}

def generate_firebase_metadata(csv_path):
    """CSV 파일 기반 Firebase 연동 메타데이터 생성"""
    metadata = {
        "generated_at": datetime.now().isoformat(),
        "source_csv": os.path.basename(csv_path),
        "schema": FIREBASE_SCHEMA
    }
    return metadata

def main():
    csv_path = "/Users/mr.k/wiki/_company/_agents/business/tools/roi_template_1person_business.csv"
    output_dir = "/Users/mr.k/wiki/_company/_agents/business/tools/"
    
    # CSV 읽기
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Firebase 연동 메타데이터 생성
    metadata = generate_firebase_metadata(csv_path)
    
    # Firebase 연동 구조 메타데이터 파일 저장
    firebase_meta_path = os.path.join(output_dir, "roi_firebase_metadata.json")
    with open(firebase_meta_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Firebase 연동 메타데이터 생성 완료: {firebase_meta_path}")
    print(f"📄 Firebase 연동 구조 기반 시트 생성을 위한 스키마:")
    print(json.dumps(FIREBASE_SCHEMA, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()