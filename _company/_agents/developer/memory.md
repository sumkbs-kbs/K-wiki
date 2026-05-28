# 💻 코다리 (시니어 풀스택 엔지니어) 개인 메모리

_코다리 에이전트만 읽고 쓰는 개인 노트. 학습·교훈·자주 쓰는 패턴이 누적됩니다._

## 학습 기록

- [2026-05-28] business 에이전트가 제작한 ROI 템플릿을 구글 시트 API 연동형 웹 템플릿으로 구현: (1) 입력 폼(가격/가정 수치), (2) 자동 계산 로직(수익/비용/ROI), (3) 시나리오 저장/로드 기능. 기술 스택: HTML/CSS/JS + Firebase Realtime Database. 구현 후 테스트 및 docs/roi-template.md 작성. → 산출물 sessions/2026-05-28T04-44/developer.md
- [2026-05-28] roi_template_1person_business.csv 기반 Firebase Realtime Database 연동 웹 템플릿 구현 완료 확인 및 구글 시트와의 실시간 동기화 테스트 수행. 입력 폼(가격/고객수/전환율), 자동 계산 로직, 시나리오 저장/로드 기능 검증 후, docs/roi-template.md 업데이트 → 산출물 sessions/2026-05-28T05-29/developer.md
- [2026-05-28] docs/roi-usage-guide.md와 roi-data-validation-summary.md의 실제 전환율 분포(82.6~86.4%가 1~5% 구간, 평균 1.9~2.3%)를 반영해, Firebase 연동 ROI 웹 템플릿의 기본 전환율 입력값을 2.0%(±0.5% 분산)로 고정하고, 3가지 유형(학원/컨설팅/디지털 콘텐츠)에 대한 초기 시나리오 기본값(예: 학원형 2.1%, 컨설팅형 1.8%, 디지털 콘텐츠형 2.3%)을 구현. Firebase 스키마 업데이트 및 로컬 테스트 후, 구글 시트와의 동기화 검증. 산출물: do