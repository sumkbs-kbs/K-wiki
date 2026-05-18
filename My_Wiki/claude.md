# DOCS 폴더 — 인제스트된 문서 (Curated Knowledge Base)

## 📌 핵심 원칙: "재사용 가능한 지식은 내 언어로 재구성한다"

이 폴더에 AI가 들어갈 때 반드시 먼저 읽고 준수해야 하는 규칙입니다.

## 🏗️ 폴더 구조 (Three-Space 모델)

```
DOCS (My_Wiki/)
├── 000-Inbox/      → AI가 생성한 1차 정리본 (최대 24시간 후 분류)
├── Topics/         → 주제별 지식 (55개 — YouTube 분석, 기술 분석 등)
├── Projects/       → 프로젝트 문서 (16개 — Plantler, Ssak, Antigravity-K 등)
├── Decisions/      → 의사결정 기록
├── Skills/         → 프시저 워크플로우 스킬
├── 100-Templates/  → 문서 템플릿
├── 900-System/     → 시스템 설정/가이드
└── index.md        → 리셉션 데스크
```

## 📝 파일명 규칙 (정제된 문서)

```
[timestamp]_[source_type]_[short-description].md
예: 20260518_youtube_solar-evaporation-desalination.md
```

**형식 설명:**
- `timestamp`: YYYYMMDD 형식
- `source_type`: youtube, web, book, meeting, decision, skill 등
- `short-description`: kebab-case 영어 (키워드 중심)

## 📋 Front Matter 스키마 (모든 DOCS 파일 필수)

```yaml
---
title: "문서 제목"
type: topic|project|decision|skill
tags: [tag1, tag2, tag3]
date: YYYY-MM-DD
source: 원천 출처 URL 또는 제목
related: [[related-file-1]], [[related-file-2]]
summary: "한 줄 요약 (50자 내외)"
---
```

## 🔗 위키링크 규칙 (Obsidian 호환)

- 문서 간 연결은 Obsidian 위키링크 형식: `[[다른 문서명]]`
- 관련 문서가 없으면 `related` 필드만 작성하고 위키링크는 생략

## 🔄 Workflow (RAW → DOCS)

```
1. raw/ 에서 원본 인제스트
2. 내용 파악 → DOCS에 내 언어로 재구성
3. 원본 유지 (raw/는 원본 그대로)
4. index.md 에 문서 정보 등록
5. 관련 문서에 위키링크 연결
```

## 🚫 AI 작업 금지 사항

- 원본(raw/) 파일 직접 수정 금지
- 인덱스 업데이트 누락 금지
- 파일명 규칙 위반 금지
- Front Matter 생략 금지

> **AI 에이전트 메모**: DOCS는 "지식"이다. 매일 매일 쌓이는 raw는 "원료"일 뿐. 
> DOCS에 저장되는 모든 문서는 재사용 가능해야 한다.

#claude-md #docs-folder
