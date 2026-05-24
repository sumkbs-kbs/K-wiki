---
type: Chat_Log
topic: Wiki_Tree_Architecture
participants: Byeong-seok, Gemini
date: 2026-05-14
status: To_be_Refined
---

# Wiki Tree Architecture

## 요약
[[안티그래피티-K]] 및 AI 개발 전반에 대한 방대한 논의를 체계화하기 위해 구상한 '거대 지식 집합소(Second Brain)'와 [[Karpathy]]의 LLM OS(지식 관리 시스템) 이론에 대한 종합 설계안입니다. 다중 에이전트(로컬 모델, 클로드 코드, 구글 안티그래피티 등)가 하나의 위키 트리로 연결되어 지식의 갱신(Update)과 누적(Accumulate)을 자동으로 수행하는 '자율 갱신형 지능 네트워크'를 구축하는 비전을 담고 있습니다.

## 핵심 정보 (Core Information)

### 1. LLM OS와 Wiki Tree (카파시의 이론)
- 지식 관리의 핵심은 단순한 '누적'이 아니라 '갱신'입니다. 유사한 데이터가 들어오면 기존 문서와 비교하여 오류를 수정하거나 최신 버전으로 업데이트해야 하며, 완전히 새로운 경우에만 누적해야 합니다.
- Raw → Processed → Wiki로 이어지는 데이터 증류(Distillation) 파이프라인 필요
- 이 구조를 구축하면 '단기기억 상실'로 인한 인지 부하(Cognitive Load) 해소

### 2. 대안: 증분 업데이트 (Incremental Update) 하네스
- 하나의 폴더에 모든 파일을 모아 하나의 프론트엔드 모델에게 '전량 검토'를 시키는 것은 매우 비효율적이고 토큰 낭비
- 각 에이전트별로 별도의 `Inbox` 폴더를 두고, 로컬 7B-8B급 모델이 파일 내용을 스캔하고 요약하여 프론트엔드 모델(클로드 코드 Max)에게 '차이점(Delta)'만 보고
- 클로드는 수백 개의 파일을 다시 읽지 않고, 로컬 비서가 골라준 8개 파일만 읽으면 됨

### 3. 다중 에이전트 위키 조건
- **표준화된 데이터 규격:** 모든 에이전트(헤르메스, 안티그래피티, 코덱스 등)가 기록할 때 동일한 마크다운 형식과 메타데이터(Author, Category, Last_Updated)를 따름
- **의미적 중복 체크:** 파일명뿐만 아니라 벡터 유사도로 기존 위키 문서와 비교하여 80% 이상 겹치면 업데이트 대상으로 분류

## 파인 튜닝 및 집단지성 전략 (Fine-tuning & Collective Intelligence)
[[파인 튜닝]] 시 가장 핵심은 데이터의 질입니다. 모델의 크기(9b, 12b, 32b)는 정보의 '그릇'이며, 데이터 양(Token)은 '내용물'입니다.
- **집단지성 구현:** 작은 모델(7b, 8b)을 여러 개 사용하여 릴레이(Relay) 또는 토론(Debate) 방식으로 집단지성 만드는 것이 프론트엔드 모델(70b급)에 대한 효율적인 대안
- 128GB RAM을 보유한 M5 Max에서는 다중 모델 로딩(`OLLAMA_MAX_LOADED_MODELS=3`)이 충분히 가능

## 기술 스택 및 도구 전략
- **중앙 저장소:** [[Obsidian]]. 모든 디바이스(MacBook, 갤럭시북, 모바일) 간에 iCloud 또는 Git을 통해 실시간 동기화
- **포맷:** 입력과 저장은 [[Markdown]]로 하되(토큰 효율성), 클로드의 Artifacts나 복잡한 데이터 시각화 결과물은 [[HTML]]로 저장하여 비주얼적 직관성 확보
- **AI 하이브리드:**
  - **Claude Code Max 플랜:** 핵심 로직, 설계, 전체적인 코드 리팩토링 담당
  - **로컬 Ollama (Qwen2.5, Llama):** 단위 테스트 생성, 코드 문법 체크, 로그 분석 등 반복적이고 가벼운 작업 담당
  - **구글 안티그래피티:** UI/UX 디자인, 대시보드 시각화, 이미지 생성 담당

## 실전 실행 계획 (Action Plan)
1. **동기화 폴더 설정:** 모든 기기에서 접근 가능한 Obsidian Vault에 `00_Inbox`, `10_Projects`, `90_Archive` 폴더 구조 생성
2. **에이전트별 Inbox:** 각 AI 에이전트들이 생성한 결과물을 전용 Inbox 폴더에던지는 스크립트 구축
3. **로컬 비서 구축:** 128GB RAM에서 `Qwen2.5-Coder:7b` 등을 상주시켜 로컬에서 새 파일의 분류, 요약 및 중복 체크 수행
4. **Delta Report 작성:** 클로드 코드 Max와 연동하여 '새로 들어온 파일'과 '기존 위키'를 비교해 변경 사항만 자동으로 병합하는 스크립트 작성

## 관련 문서
- [[FineTuning_Datasets]]
- [[AntiGraffiti-K]]
- [[Karpathy_LLM_OS]]
- [[Obsidian_Automation]]
- [[Claude_Code_Max]]
