---
type: Wiki
topic: YouTube_Analysis
source: youtube
video_id: Ma8e25AOtao
channel: 오늘코드todaycode
upload_date: 2026-04-17
views: 29030
likes: 998
duration: 61:43
participants: 오늘코드todaycode
date: 2026-05-14
status: Refined
tags: [youtube, graphify, karpathy_llm_wiki, deterministic_graph, RAG_alternative, tokenize_reduction, legalize_kr, inference_optimization]
---

# 71.5배 토큰 절감, Graphify가 LLM 토큰 비용은 낮추고 답변 정확도는 높이는 방법

## 요약
오늘코드todaycode에서 공개한 영상. Andrej Karpathy의 LLM Wiki 개념을 실무에 적용하기 위해 Graphify 스킬을 직접 분석하며, 기존 RAG의 벡터 임베딩 방식 대신 코드 기반 그래프 생성으로 71.5배 토큰을 절감하면서 정확도를 높이는 방법을 설명합니다.

## 핵심 내용

### Graphify의 혁신적 접근법
- **벡터 임베딩 NON-사용:** 기존 RAG의 표준인 벡터 임베딩을 전혀 사용하지 않음
- **파이썬 코드 기반 그래프 생성:** 파이썬 코드로 먼저 그래프 생성 → 결정론적으로 실행 → 결과물을 LLM과 함께 활용
- **임베딩 모델/벡터 DB 불필요:** 임베딩 모델 호출도, 벡터 데이터베이스도 필요 없음
- **코드 위주의 추론:** LLM이 모든 것을 추론하는 것이 아니라, 코드가 처리할 수 있는 부분을 코드에 위임

### 검증 케이스
1. **legalize-kr 저장소 분석:** 대한민국 법령 문서 가져와 분석
2. **Graphify 저장소 자체 분석:** Graphify의 전체 내용을 Graphify로 분석

### 주요 링크
- https://graphify.net/kr/
- https://x.com/karpathy/status/2039805659525644595
- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- https://github.com/legalize-kr/legalize-kr
- https://discuss.pytorch.kr/t/legalize-kr-git/9596

## 핵심 인사이트

1. **토큰 비용의 근본적 절감:** 결정론적 코드 실행으로 LLM 호출량 최소화 (71.5배)
2. **RAG의 대안 아키텍처:** 임베딩/VectorDB 없이 Graph 기반으로 지식 탐색
3. ** karpathy LLM Wiki의 실전 적용:** 이론에서 실무로 넘어가는 구체적인 도구 (Graphify 스킬)
4. **코드와 LLM의 역할 분담:** 반복/논리 작업은 코드, 추론 작업은 LLM - 효율적 하이브리드 추론
5. **법령/구조적 데이터 최적화:** 법적 문서처럼 구조가 명확한 데이터에 특히 효과적

## 비교: 동일 주제 YouTube 영상들

| 영상 | 채널 | 조회수 | 주요 주제 |
|------|------|-------|---------|
| Graphify로 토큰 71.5배 절감 | 오늘코드todaycode | 2.9만 | Graphify 분석, RAG 대안 |
| Kapathy의 LLM Wiki (Claude x Obsidian x Graphify) | 브레인 트리니티 | 4.6만 | Karpathy Wiki 구현 가이드 |
| 옵시디언 + LLM Wiki 업무 시스템 | 칼퇴연구소 | 8.2천 | Obsidian 기반 AI 업무 환경 |
| RAG의 동작 과정 쉽게 이해하기 | 테디노트 | 8.8만 | RAG 기본 원리 |
| LLM 바닥부터 만들기 (사전학습) | 홍정모 | 18만 | LLM 원리 학습 |
| MCP 영상 하나로 끝내세요 | 조코딩 | 35만 | MCP 프로토콜 가이드 |

## 관련 문서
- [[Wiki_Tree_Architecture]]
- [[https://github.com/karpathy/llm-wiki]]
- [[AntiGraffiti-K]]
- [[Website_Analysis_EZER_AI_Agent_University.md]]
- [[M5Max_Local_LLM_Strategy_and_Wiki]]
- [[Website_Analysis_EZER_AI_Agent_University]]
- [[YouTube_Analysis_Woorkpay0_AI_Company]]
- [[YouTube_Analysis_OpenClaw_5Agents_CodingFree]]

## Karpathy LLM Wiki 연계성
이 영상은 [[https://github.com/karpathy/llm-wiki]]에서 논의된 LLM Wiki 개념을 Graphify라는 구체적 도구로 구현한 사례입니다. 벡터 임베딩 없이 코드 기반 그래프로 지식을 탐색하는 접근법은, [[M5Max_Local_LLM_Strategy_and_Wiki]]에서 제안한 RAG 기반 Wiki와 대비되는 아키텍처입니다. 특히 128GB 맥북에서는 Graphify의 결정론적 그래프 traversal + DeepSeek-V4-Flash의 추론을 결합하면 하이브리드 지식 엔진 구축이 가능합니다.
