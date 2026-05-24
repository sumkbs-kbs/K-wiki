# LLM Wiki Activity Log

모든 문서화(ingest), 질문/답변(query), 위키 점검(lint) 작업의 이력이 시간순으로 남는 로그 공간입니다.

## [2026-05-10] lint | 볼트 하이어라키 정리 및 Antigravity-K 연동 수정
- **경로 단절 수정**: `config.yaml`의 `wiki_dir`을 존재하지 않는 `/wiki/AI_Learnings` → 실제 `/wiki/pages`로 수정
- **WikiExportTool 경로 통일**: config.yaml 직접 파싱 → `config.paths.wiki_dir` 사용으로 변경
- **ingest_obsidian.py 하드코딩 제거**: 절대 경로 대신 `config.paths.wiki_dir.parent` 기반 + CLI/ENV 오버라이드
- **SCHEMA.md**: Windows 경로 잔재(`c:\Python\wiki`) → macOS 실제 경로 수정
- **index.md 재구성**: 4건만 인덱싱 → 전체 볼트 309건 반영 (Topics 28, Projects 23, Decisions 13, Skills 8, 선급 5, 전기 3, GithubRepos 15개 프로젝트)
- **식별된 추가 과제**: 중복 파일 35건(`_1.md`, `_2.md`), 빈 디렉토리 3건

## [2026-05-04] ingest | Antigravity-K 에이전트 파이프라인 안정화 세션 지식 구조화
- 2026-05-03~04 세션에서 수행한 전체 작업을 4개의 지식 문서로 구조화하여 `pages/`에 저장
- 생성된 문서:
  1. `antigravity-k-output-stabilization.md` — 출력 품질 안정화 (thinking-tag, CJK, 반복 루프)
  2. `antigravity-k-recursive-self-improvement.md` — 재귀적 자기개선 아키텍처 진단 및 피드백 루프 복원
  3. `antigravity-k-ollama-native-api.md` — Ollama OpenAI 호환 API vs Native API 비교 및 VRAM 최적화
  4. `antigravity-k-dashboard-realtime.md` — 대시보드 실시간 연동 (Kanban, Think Block UI, 빌드 파이프라인)
| `index.md` 카테고리별 인덱스 갱신

## [2026-05-17] ingest | AI회사 교육총괄이 말한 AI 활용법 (앤트로픽, 클로드)
- YouTube 영상 분석: https://youtu.be/UjwaAF9X0qg (돈되는 AI+SNS, 이든, 8분)
- Markdown 문서를 `raw/videos/AI회사_교육총괄_AI활용법_UjwaAF9X0qg.md`에 저장
- 분석 페이지를 `pages/AI회사-교육총괄-AI활용법-UjwaAF9X0qg.md`에 저장
- 핵심 내용: 2022년형 '비서' 방식의 한계, 맥락(Context) 공유, AI 에이전트 활용 전략
- 앤트로픽 교육 총괄 드류 벤트의 통찰 및 실전 활용 프롬프트 포함
- `index.md` YouTube Analysis 섹션 갱신

## [2026-05-17] ingest | Hermes를 실무 에이전트로 바꾸는 명령어들
- YouTube 영상 분석: https://youtu.be/vfhXPrMp15A (일하는 ai, 19분)
- Markdown 문서를 `raw/videos/hermes 실무 에이전트 명령어들-vfhXPrMp15A.md`에 저장
- 분석 페이지를 `pages/youtube-Hermes-실무-에이전트-명령어들.md`에 저장
- 핵심 내용: `/status`, `/branch`, `/debug`, `/update` 등 핵심 슬래시 커맨드
- `index.md` YouTube Analysis 섹션 갱신

## [2026-05-13] youtube-transcript | 그래피파이(GraphPy) 전체 분석 — 위키 + HTML
- YouTube 영상 분석: https://youtu.be/Ma8e25AOtao (≈61분 스크립트)
- Markdown 문서를 `My_Wiki/Topics/GraphPy-자동-지식-그래프-생성-도구-20260513.md`에 저장
- HTML 보고서를 `pages/graphpy-자동-지식-그래프-생성-도구.html`에 저장
- GraphPy 핵심 내용: 이중 경로 추출(AST+LLM), 9단계 파이프라인, 5~71.5배 토큰 절감
- 관련 개념: AST, NetworkX, Laydens 커뮤니티 감지, 트리티시터 파싱 엔진

## [2026-04-16]
- `raw/`, `pages/` 디렉토리 생성
- `SCHEMA.md` 작성 
- `index.md` 구조 마련
