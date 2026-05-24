---
title: "Alda (Personal LLM Wiki) Integration"
tags: [llm-wiki, alda, mcp, obsidian, rag, antigravity-k]
date: 2026-05-10
---

# Alda: 개인용 LLM Wiki 통합 및 기능 강화

본 문서는 유튜브 영상 [M5 프로맥스 128G로 구축한 나만의 LLM Wiki 전격 대공개!](https://youtu.be/YCirjfAurng)의 분석을 통해 도출된 아키텍처 및 기능 강화 지식을 정리한 것입니다.

## 1. 개요 및 아키텍처
* **목표:** 안드레이 카파시(Andrej Karpathy)가 제안한 LLM Wiki 개념을 실체화하여, 개인의 방대한 로컬 노트(Obsidian)를 AI 에이전트의 영구적인 기억 장치로 통합.
* **이름:** `알다(Alda)` - 개인 LLM Wiki 시스템.
* **하드웨어 환경:** M5 Pro Max 128G 메모리 환경을 적극 활용, 대규모 로컬 인덱싱 및 빠른 RAG 파이프라인 구동.

## 2. 주요 기능 강화 포인트

### 2.1. 로컬 옵시디언 노트의 선별적 RAG 인덱싱
* 9,700개의 전체 옵시디언 노트 중, 코딩 및 기술 지식과 직결되는 **1,228개의 핵심 노트를 선별**하여 로컬 LLM을 통해 벡터화 및 인덱싱.
* 이를 통해 단순 텍스트 매칭이 아닌 딥러닝 기반의 **의미론적 검색(Semantic Search)** 아키텍처 구축.

### 2.2. MCP(Model Context Protocol) 기반 인터페이스
* 구축된 LLM Wiki(Alda)를 단절된 시스템이 아닌 **MCP 서버** 형태로 캡슐화.
* **Claude Code, Codex, Antigravity-K** 등의 코딩 에이전트가 런타임에 MCP를 통해 알다(Alda) 서버에 질의를 보내고, 개인화된 지식을 컨텍스트로 바로 주입받을 수 있도록 연동.

### 2.3. 에이전트 자율 진화(Autonomous Evolution)에의 기여
* Antigravity-K의 코어 엔진(예: Context Compressor, RAG Utilities)과 결합하여, 에이전트가 문제 해결 과정에서 알다(Alda) 위키를 스스로 검색.
* 과거의 버그 해결 기록, 아키텍처 설계 문서(ADR), 특정 도메인의 코드 스니펫 등을 에이전트가 직접 참조함으로써 **Hallucination(환각) 방지 및 코딩 정확성 극대화**.

## 3. 폴더 및 지식 구조 맵핑
해당 지식 체계는 Antigravity-K의 장기 기억(Long-term Memory) 확장성을 보장하기 위해, `user/mr.k/wiki` 하위의 로컬 지식 기반 저장소와 MCP를 통해 지속적으로 동기화됩니다.

- **MCP 서버 위치:** (로컬 환경 구성에 따름)
- **에이전트 연결 모듈:** `src/antigravity_k/engine/` 내 메모리/컨텍스트 라우터 연동
- **위키 문서:** `/Users/mr.k/wiki/` (Obsidian Vault)

---
> **결론:** '알다(Alda)' 시스템의 통합은 Antigravity-K 에이전트가 단순한 '생성형 봇'을 넘어 사용자의 뇌(옵시디언)와 직접 연결된 '개인화된 페어 프로그래머'로 진화하는 핵심 기틀을 마련했습니다.
