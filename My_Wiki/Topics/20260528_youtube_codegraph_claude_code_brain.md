---
title: "CodeGraph: Claude Code에 '뇌'를 부여 — 30k Stars GitHub (Bitwise AI)"
type: youtube
category: AI Engineering
tags: [CodeGraph, RAG, 코드 그래프, GitHub, Agent, MCP, knowledge graph]
source: YouTube
channel: Bitwise AI
channel_id: @BitwiseAI
video_id: aA-piqGXKUI
url: https://youtu.be/aA-piqGXKUI
published: "2026-05"
views: N/A
date: 2026-05-28
summary: "CodeGraph — 코드베이스 지식그래프로 AI 에이전트 토큰 70% 절감"
related: [[Antigravity-K-정밀분석-현재상태-20260511.md]], [[GitHub]], [[YouTube_Analysis_Graphify_Token_Reduction.md]]
---

# 🧠 CodeGraph: Claude Code에 '뇌'를 부여 — 30k Stars

> 영상: [This Repo Gives Claude Code a Brain, 30k Stars on GitHub](https://youtu.be/aA-piqGXKUI) — Bitwise AI

## 핵심 요약

Claude Code, Cursor,_CODex 같은 AI 코딩 에이전트는 매 질문마다 레포지토리를 다시 읽으면서 토��을 낭비함. **CodeGraph**는 레포를 단 한 번 파싱하여 지식그래프를 만들고, 에이전트가 그 그래프를 쿼리하도록 함 — 도구 호출 **70% 절감**, 20k stars → 30k stars.

## 주요 내용 (자막 기반)

### 동작 원리 — 3단계

| 단계 | 방법 | 세부 |
|------|------|------|
| 1. 파싱 | Tree-sitter | 20개 이상 언어, 함수/클래스/타입/임포트 추출 |
| 2. 그래프 구성 | SQLite + 관계 23종 | symbol 간 12관계 추적, 호출자/피호출자/extend/impl 모두 |
| 3. MCP 제공 | 10개 도구 | context 조회, 호출자/피호출자 추적, 영향권 매핑, 파일워치 자동 재인덱싱 |

### 핵심 차별점: RAG 아님
- **Embeddings/벡터DB 없음** — 구조적 파싱이므로 관계 정확
- **로컬 SQLite** — API 키 없음, 데이터 밖으로 나가지 않음
- **파일워치** — 수정 시 자동 재색인

## 벤치마킹 (우리 시스템 1:1 비교)

| 항목 | CodeGraph | 우리 시스템 | 적용 가능성 |
|------|-----------|-------------|---|
| 코드베이스 그래프 | Tree-sitter + SQLite | Antigravity-K에 도입 가능 | 🔴 즉시 적용 |
| MCP 도구 제공 | 10개 도구 | Hermes MCP 서버와 연동 가능 | 🟢 가능 |
| 파일워치 | ✅ 자동 재인덱싱 | cronjob으로 시뮬레이션 | 🟡 가능 |
| 로컬 실행 | ✅ 완전 오프라인 | ✅ 로컬 LLM과 궁합 | ✅ |
| 비용 | 무료 (오픈소스) | 로컬 qwen3.6:latest | ✅ |

## 핵심 인사이트

1. **Antigravity-K의 핵심 과제를 바로 해결** — 코드베이스 읽기/파일 개방 반복 = 비싼 API 호출
2. **Antigravity-K + CodeGraph = 완성형** — 로컬에서 그래프 기반 컨텍스트 + 로컬 LLM 추론
3. **30k stars의 의미** — AI 코딩 에이전트의 컨텍스트 문제는 업계 공통痛点

## 실질적 작용점

1. **CodeGraph 설치 → Antigravity-K 코드베이스 적용** (내주 이내)
2. **MCP 연동** — 10개 도구 중 context tracing + caller/callee → Antigravity-K에 통합
3. **프로젝트 관련 분석에 적용** — Plantler, Ssaq 레포 모두 그래프화 가능


## 관련 분석

| 문서 | 요약 |
|------|------|
| [[YouTube_Analysis_Graphify_Token_Reduction.md]] | 그래프 기반 토큰 최적화 |
| [[Antigravity-K-정밀분석-현재상태-20260511.md]] | 우리 시스템과 직접 연계 |
| [[GitHub]] | 30k Stars 프로젝트 |
