---
type: Wiki
topic: YouTube_Analysis
source: youtube
video_id: OVilj8E2NnM
channel: 태오의 실행 비즈니스
upload_date: 2026-05-11
views: 10182
likes: 399
duration: 26:26
participants: 태오의 실행비즈니스
date: 2026-05-14
status: Refined
tags: [youtube, obsidian_claude_code, karpathy_llm_wiki, raw_wiki_prompt, slash_commands, ingest_query_lint, knowledge_density, karpathy_library_metaphor]
---

# 옵시디언에 클로드 코드 연결하면 이런 일이 가능합니다 | 정보 정리부터 사업 시스템까지

## 요약
태오의 실행비즈니스 채널에서 공개한 영상. Obsidian과 Claude Code를 결합하여 정보의 양은 줄이면서 밀도는 폭발적으로 높이는 방법을 다룹니다. "정보의 늪에서 빠져나오는 첫 단계"로 Raw→Wiki 파이프라인을 구축하고, Karpathy의 LLM Wiki 개념을 실무에 적용합니다.

## 핵심 내용

### Karpathy의 LLM Wiki + 도서관 비유
- 외부에서进来的 정보를 Raw(날것)로 받아들이지만, 즉시 Wiki(정제)로 분류
- 도서관의 비유: 모든 책을 다 읽지 않아도, 필요한 책(인덱스)만 빠르게 찾아볼 수 있어야 함
- Obsidian이 도서관, Claude Code가 사서 역할

### 3가지 핵심 개념

**1. Raw vs Wiki — 외부 정보 vs 내 사업 결정**
- Raw: YouTube 영상, 뉴스, 보고서 등 외부에서 들어오는 정보
- Wiki: 내가 읽고 해석하고 결정에 직접 활용하는 지식
- Claude Code가 Raw를 Wiki로 변환해주는 다리 역할

**2. Claude Code + Obsidian 연결 셋업**
- Claude Code로 Obsidian Vault 파일 읽고 쓰기
- 프롬프트 기반으로 자동 분류 및 요약 자동화
- 외부 도구와의 연결(MCP 기반) 가능

**3. raw-wiki 프롬프트 — 딱 2개 질문**
- 외부 정보를 Wiki로 변환하는 핵심 프롬프트 (간단한 질문 2개로 자동 정제)
- 👉 https://geekus.kr/actbusiness/classroom/351?lessonId=4370

### 슬래시 커맨드 3종
1. **/ingest** — 외부 자료 읽기 및 Obsidian 저장 (실시간 시연 포함)
2. **/query** — Wiki에서 정보 조회
3. **/lint** — Wiki 정리 및 중복 제거

### 외부 연결 (MCP 기반)
- YouTube, Email, Notion 등 외부 도구 연결

## 타임라인
00:00 - 도입부
00:44 - 옵시디언이란?
02:19 - Karpathy의 LLM Wiki + 도서관 비유
03:41 - Raw vs Wiki ― 외부 정보 vs 내 사업 결정
04:30 - Claude Code + 옵시디언 연결 셋업
07:00 - raw-wiki 프롬프트 (딱 2개 질문)
09:31 - 슬래시 커맨드 3종 (/ingest /query /lint)
13:35 - /ingest 라이브 시연
19:02 - 외부 연결 — YouTube/Email/Notion MCP
21:09 - AI 시대 본질
24:17 - 시스템이 굴러간다는 증거

## 핵심 인사이트
1. **정보 밀도 > 정보 양:** Raw에서 Wiki로 정제하여 정보 밀도를 폭발적으로 높임
2. **karpathy LLM Wiki의 한국적 실무 적용:** 미국 이론 → 한국 실전에 최적화된 워크플로우 정립
3. **슬래시 커맨드 자동화:** `/ingest`, `/query`, `/lint`로 일상 워크플로우 자동화
4. **MCP 기반 외부 연결:** YouTube, Email, Notion 등 외부 소스를 일관된 방식으로 통합
5. **단 한 사람의 사업 시스템:** 1인 사업을 위한 AI 기반 지식/업무 자동화 인프라 구축

## 참조 링크
- raw-wiki 프롬프트: https://geekus.kr/actbusiness/classroom/351?lessonId=4370
- Karpathy LLM Wiki Gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Obsidian: https://obsidian.md
- Claude Code: https://claude.com/claude-code

## 관련 문서
- [[Topics/Wiki_Tree_Architecture.md]]
- [[https://github.com/karpathy/llm-wiki]]
- [[Projects/M5Max_Local_LLM_Strategy_and_Wiki.md]]
- [[Topics/Website_Analysis_EZER_AI_Agent_University.md]]
- [[Projects/M5Max_Local_LLM_Strategy_and_Wiki.md]]
- [[Topics/YouTube_Analysis_Graphify_Token_Reduction.md]]
- [[Topics/YouTube_Analysis_Hermes_Obsidian_Omi_Memory.md]]
- [[Topics/YouTube_Analysis_Woorkpay0_AI_Company.md]]
- [[Topics/YouTube_Analysis_OpenClaw_5Agents_CodingFree.md]]
- [[Topics/Website_Analysis_EZER_AI_Agent_University.md]]

## 비교: Obsidian + AI 메모리 영상들 (종합)

| 영상 | 채널 | 조회수 | 주요 접근법 |
|-- ----|-- ----|-- ----|-----|
| Hermes + Obsidian + Omi | Julian Goldie | 4,787 | 백그라운드 녹화 → Vault → Hermes |
| Obsidian + Claude Code | 태오의 실행비즈니스 | 10,182 | Raw→Wiki, 슬래시 커맨드 |
| Graphify로 토큰 71.5배 절감 | 오늘코드 今天코드 | 29,030 | Graphify 분석, RAG 대안 |
| 월급 0원 AI직원 5명 | CONNECT AI LAB | 12,112 | 무료 AI회사, 안티그래비티 |
| 코딩없이 OpenClaw 5명 활용 | 패스트캠퍼스 | 13,000 | 바이브코딩, 코드 없는 에이전트 |

## Obsidian + Claude Code + Karpathy LLM Wiki 연계성
이 영상은 [[https://github.com/karpathy/llm-wiki]]에서 논의된 LLM Wiki 개념을 Karpathy 본인의 Gist를 직접 활용하여 가장 명확하게 실무 적용한 사례입니다. Raw(유튜브/뉴스 등 외부 Raw) → Wiki(내 사업 결정용 정제 지식) 파이프라인과 슬래시 커맨드 `/ingest /query /lint`는 [[Projects/M5Max_Local_LLM_Strategy_and_Wiki.md]]에서 제안한 RAG 기반 Wiki와 상호보완적입니다. 특히 Claude Code를 사서 역할로 활용하는 접근은 로컬 DeepSeek-V4-Flash와 비교 시 클라우드의 추론 품질 이점이 있으나, 보안 문제에서는 [[Projects/M5Max_Local_LLM_Strategy_and_Wiki.md]]의 로컬 전략이 우월합니다.
