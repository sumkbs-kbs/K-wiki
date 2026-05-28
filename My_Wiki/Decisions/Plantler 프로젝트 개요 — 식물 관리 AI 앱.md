---
id: d3a596f8
category: "[[Decisions/index]]"
confidence_score: 0.5
tags: [decisions, 프로젝트, 아키텍처, 기술스택]
last_reinforced: 2026-04-15
github_commit: "pending"
---

# [[Decisions/Plantler 프로젝트 개요 — 식물 관리 AI 앱.md]]

## 📌 한 줄 통찰 (The Karpathy Summary)
> Plantler는 AI 기반 식물 관리 앱이다. 사용자가 식물 사진을 찍으면 AI가 건강 상태를 분석하고, 날씨 기반 관리 조언을 제공하며, 커뮤니티에서 다른 식물 집사들과 ...

## 📖 구조화된 지식 (Synthesized Content)
- **추출된 패턴:**
  - **프론트엔드:** Flutter (Dart) — Riverpod 상태관리, GoRouter 네비게이션, Dio 네트워킹
  - **백엔드:** FastAPI (Python) — SQLAlchemy ORM, Gemini AI, TFLite 로컬 분류
  - **백그라운드 워커:** Celery + Redis
  - **데이터베이스:** SQLite (로컬) + PostgreSQL (프로덕션)
  - **다국어 지원:** 한국어, 영어, 일본어, 중국어(번체)

- **세부 내용:**
  - Plantler는 AI 기반 식물 관리 앱이다. 사용자가 식물 사진을 찍으면 AI가 건강 상태를 분석하고, 날씨 기반 관리 조언을 제공하며, 커뮤니티에서 다른 식물 집사들과 교류할 수 있다.
  - Flutter + FastAPI 조합을 선택한 이유:

## ⚠️ 모순 및 업데이트 (Contradictions & RL Update)
- **과거 데이터와의 충돌:** 현재까지 발견된 모순 없음.
- **정책 변화:** 이 문서를 통해 분류 정책에 변화 없음.

## 🔗 지식 연결 (Graph)
- **Parent:** [[Decisions/index]]
- **Related:** [[Decisions/Plantler v2.0 프로젝트 회고.md]], [[Skills/나만의 생산성 워크플로우.md]]
- **Raw Source:** Projects/Plantler 프로젝트 개요 — 식물 관리 AI 앱
