# 📈 ROI 계산기 — Firebase 연동 웹 앱

## 개요
- **목적**: 1인 기업을 위한 가상 시나리오 기반 ROI 계산 템플릿
- **기능**: 입력 폼 → 자동 계산 → 시나리오 저장/로드 (Firebase Realtime Database)
- **기술 스택**: HTML/CSS/JS + Firebase SDK v10

## 구현 위치
- 📁 `/docs/roi-template/`
- 🌐 `index.html` (단일 파일 배포 가능)

## 주요 기능
| 기능 | 설명 |
|------|------|
| 입력 폼 | 가격(단일/구독), 전환율, 고객 수, 마케팅 비용 입력 |
| 자동 계산 | 수익/비용/순이익/ROI 실시간 계산 |
| 시나리오 저장 | Firebase에 `scenarios/{이름}` 형태 저장 |
| 시나리오 로드 | 저장된 시나리오 선택 → 결과 재계산 |

## Firebase 설정
- `firebase-config.js`에서 `firebaseConfig` 객체를 Firebase Console에서 복사해 대체 필요
- Realtime Database 규칙 예시:
```json
{
  "rules": {
    "scenarios": {
      ".read": true,
      ".write": true
    }
  }
}
```

## 계산 공식
- `고객 수 = 총 타겟 × (전환율 / 100)`
- `수익 = 가격 × 고객 수`
- `순이익 = (가격 - COGS) × 고객 수 - 마케팅 비용`
- `ROI = (순이익 / 총 비용) × 100`

## 사용 예시
1. `index.html` 열기
2. 전환율 2%, 고객 100명, 마케팅 0원 입력
3. **계산하기** → 결과 확인
4. **시나리오 저장** → 이름 `CR2%_Cust100` 등으로 저장
5. 나중에 **로드** → 이전 시나리오 재계산

## 확장 가능성
- 📤 CSV 내보내기 기능 추가
- 📊 차트 시각화 (Chart.js 연동)
- 🌍 다국어 지원
- 🔐 인증 연동 (Firebase Auth)

## 유지보수
- Firebase SDK 업데이트 시 `app.js` 내 `firebase.database()` 사용 방식 확인
- `calculateROI()` 함수를 `roi-calculator.js`로 분리해 모듈화 가능

---

**최종 수정**: 2026-05-28  
**작성 에이전트**: 코다리  
**실행 이력**: `docs/roi-template/` 생성 → `index.html`, `app.js`, `styles.css`, `firebase-config.js`, `docs/roi-template.md` 작성