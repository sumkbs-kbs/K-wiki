# 📋 통합 스케줄
_업데이트: 2026. 5. 28. 오후 3:02:06_

## 🤖 에이전트 최근 활동
### 💻 코다리
- [2026-05-28] business 에이전트가 제작한 ROI 템플릿을 구글 시트 API 연동형 웹 템플릿으로 구현: (1) 입력 폼(가격/가정 수치), (2) 자동 계산 로직(수익/비용/ROI), (3) 시나리오 저장/로드 기능. 기술 스택: HTML/CSS/JS + Firebase Realtime Database. 구현 후 테스트 및 docs/roi-template.md 작성. → 산출물 sessions/2026-05-28T04-44/developer.md
- [2026-05-28] roi_template_1person_business.csv 기반 Firebase Realtime Database 연동 웹 템플릿 구현 완료 확인 및 구글 시트와의 실시간 동기화 테스트 수행. 입력 폼(가격/고객수/전환율), 자동 계산 로직, 시나리오 저장/로드 기능 검증 후, docs/roi-template.md 업데이트 → 산출물 sessions/2026-05-28T05-29/developer.md
- [2026-05-28] docs/roi-usage-guide.md와 roi-data-validation-summary.md의 실제 전환율 분포(82.6~86.4%가 1~5% 구간, 평균 1.9~2.3%)를 반영해, Firebase 연동 ROI 웹 템플릿의 기본 전환율 입력값을 2.0%(±0.5% 분산)로 고정하고, 3가지 유형(학원/컨설팅/디지털 콘텐츠)에 대한 초기 시나리오 기본값(예: 학원형 2.1%, 컨설팅형 1.8%, 디지털 콘텐츠형 2.3%)을 구현. Firebase 스키마 업데이트 및 로컬 테스트 후, 구글 시트와의 동기화 검증. 산출물: do
### 💼 현빈
- [2026-05-28] generate_roi_template.py 스크립트를 실행해 ROI 템플릿 CSV 생성. 생성된 CSV를 구글 시트로 변환해 공유 링크 제공. 가격대(9,900/19,900/29,900원), 구독형(월 4,900/연 49,000원), 전환율 1~5%, 고객수 100~1,000명 기준 자동 계산 로직 반영. 산출물은 sessions/2026-05-28T13-59/ 에 저장. → 산출물 sessions/2026-05-28T04-59/business.md
- [2026-05-28] generate_roi_template.py 실행 결과 CSV(/Users/mr.k/wiki/_company/_agents/business/tools/roi_template_1person_business.csv)를 구글 시트로 변환하고, 공유 링크를 생성해 팀에 전달. 구글 시트는 Firebase Realtime Database 연동을 위한 구조 기반으로 사용됨 → 산출물 sessions/2026-05-28T05-14/business.md
- [2026-05-28] ROI 템플릿 웹 앱(Firebase 연동 완료)의 실제 운영 활용 가이드 초안 작성: (1) 1인 기업 유형별 입력 패턴 3가지(학원/컨설팅/디지털 콘텐츠), (2) 전환율 가정 근거 및 검증 방법, (3) 실시간 수정 시 ROI 변화 시각화 가이드. 산출물: docs/roi-usage-guide.md → 산출물 sessions/2026-05-28T05-44/business.md
### 🔍 Researcher
- [2026-05-28] 1인 창업자 100명 중 실제 ROI 전환율 분포(1~5% 구간)에 대한 데이터 리서치 및 ROI 템플릿 입력 가정의 타당성 검증. 자료 출처: 통계청, 카카오브레인, 크레딧카드 사용 데이터 등 공공·민간 통계 요약. 산출물: roi-data-validation-summary.md → 산출물 sessions/2026-05-28T05-44/researcher.md

