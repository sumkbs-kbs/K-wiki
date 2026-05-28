---
title: "LLM Wiki를 업그레이드하는 외부 지식 시스템 – Zotero × NotebookLM × Obsidian × Claude Code"
type: youtube
tags: [llm-wiki, zotero, notebooklm, obsidian, claude-code, pk-workflow, external-knowledge-layer]
date: 2026-05-24
source: "https://www.youtube.com/watch?v=ulhEyDIxj6Q"
channel: "Brian's Brain Trinity (구독자 15,300명)"
related: [[Karpathy LLM Wiki]], [[My_Wiki]], [[Zotero MCP]], [[https://www.notion.so/notebooklm-py]]
summary: "Zotero+NotebookLM을 LLM Wiki 외부 지식 레이어로 연결하는 AI 지식관리 워크플로우 — 원본 소스 수집 → LLM Wiki 컴파일 → NotebookLM 산출 생성 → Obsidian 저장"
---

# 📺 LLM Wiki 외부 지식 시스템: Zotero × NotebookLM × Obsidian × Claude Code

## 📋 영상 개요

**채널**: Brian's Brain Trinity (구독자 15,300명)
**길이**: 32분 32초
**업로드**: 2026-05-17
**좋아요**: 292개 | **조회수**: 7,261회
**태그**: #LLMWiki #Zotero #NotebookLM #Obsidian #ClaudeCode

---

## 🎯 핵심 메시지

> "LLM Wiki 하나만으로는 부족할 수 있습니다. **원본 소스(Zotero) + LLM Wiki(컴파일) + NotebookLM(질의응답/산출) + Obsidian(최종저장)**의 4층 구조가 최강의 개인 지식관리 워크플로우다."

---

## 📚 32개 타임스탬프 상세 분석

### Section 1: 문제 정의 (00:00 → 04:49)
| 타임스탬프 | 주제 | 핵심 내용 |
|------------|------|-----------|
| 00:00 | LLM Wiki, 이 2개로 업그레이드 | Zotero + NotebookLM이 LLM Wiki를 보완 |
| 00:55 | LLM Wiki가 담당하는 영역 | 정리·컴파일·구성 |
| 01:23 | 원본 파일은 어디에? | LLM Wiki는 원본 저장소가 아님 |
| 03:03 | AI 대화창만으로 부족한 이유 | 컨텍스트 손실, 세션 분리 문제 |
| 03:54 | 소스 추적의 중요성 | AI 답변 → 원본 소스 → 재검증 |
| 04:49 | 해결책: Zotero + NotebookLM | 각각 원본·질답 도메인 담당 |

### Section 2: 도구 소개 (05:02 → 09:52)
| 타임스탬프 | 주제 | 핵심 내용 |
|------------|------|-----------|
| 05:02 | Zotero: 원본 소스 도서관 | 논문·영상·보고서·웹페이지 수집 |
| 05:39 | NotebookLM: 소스와 대화 | 특정 소스 기반 질의·요약·산출물 생성 |
| 06:30 | 3도구 연결 방식 | Zotero → LLM Wiki → NotebookLM → Obsidian |

### Section 3: 실제 시연 (09:52 → 20:20)
| 타임스탬프 | 주제 | 핵심 내용 |
|------------|------|-----------|
| 09:52 | Zotero + Connector 설치 | 브라우저 확장 프로그램으로 한클릭 저장 |
| 10:54 | 논문/웹자료 저장 | Zotero 컬렉션 자동 분류 |
| 12:01 | 유튜브 영상도 소스화 | 유튜브 영상을 Zotero 소스로 추가 |
| 13:02 | Claude Code + Zotero 연동 | MCP 서버(Zotero MCP)로 자동화 |
| 13:25 | Zotero MCP 소개 | github.com/54yyyu/zotero-mcp |
| 14:29 | LLM Wiki용 Zotero 스킬 | Zotero 컬렉션 → LLM Wiki ingest |
| 15:43 | AI로 관련 논문 찾기 | Zotero + AI 기반 자동 문헌 검색 |
| 16:51 | Zotero 컬렉션 자동 생성 | AI가 주제별 컬렉션 생성 |
| 18:01 | 논문 기반 문헌 리뷰 | Zotero 컬렉션 → 문헌분석 결과 |
| 18:47 | Zotero → Obsidian | Zotero에서 Obsidian으로 데이터 이관 |

### Section 4: NotebookLM 활용 (20:20 → 32:32)
| 타임스탬프 | 주제 | 핵심 내용 |
|------------|------|-----------|
| 20:20 | LLM Wiki ingest | Zotero 정리본을 LLM Wiki에 적재 |
| 25:09 | NotebookLM을 Claude Code에서 | Claude Code → NotebookLM API 연동 |
| 25:54 | LLM Wiki로 Notebook 만들기 | Wiki 자료를 NotebookLM 소스로 사용 |
| 28:30 | 원본 PDF까지 연결 | 인사이트 → 원문 PDF 간 연결고리 |
| 29:01 | 인포그래픽 생성 요청 | NotebookLM으로 시각산출물 생성 |
| 30:05 | 결과물을 Obsidian 저장 | 최종 산출물을 Obsidian知识库에 저장 |
| 31:10 | 전체 워크플로우 정리 | 소스 수집 → 컴파일 → 질의 → 산출 → 저장 |
| 31:51 | LLM Wiki → AI 워크스페이스 확장 | Wiki를 중앙 허브로 한 확장 생태계 |

---

## 🔗 관련 리소스

- Zotero: https://www.zotero.org/
- Zotero Connector: https://www.zotero.org/download/connectors
- Zotero MCP: https://github.com/54yyyu/zotero-mcp
- notebooklm-py: https://github.com/teng-lin/notebooklm-py

---

## 🏗️ 아키텍처: 4층 지식관리 파이프라인

```
[Zotero]          [LLM Wiki]     [NotebookLM]    [Obsidian/Claude Code]
┌─────────┐      ┌──────────┐   ┌────────────┐  ┌──────────────────┐
│ 원본 소스 │ ──▶ │ 컴파일    │─▶ │ 질의·산출  │─▶│  최종 저장/활용  │
│ 논문/웹/영상│     │ AI가정리  │   │ 인포그래픽  │  │ 문서화/활용       │
│ 자동수집    │      │          │   │ 요약·분석  │  │                  │
└─────────┘      └──────────┘   └────────────┘  └──────────────────┘
   수집 layer        정제 layer       산출 layer          활용 layer
```

---

# 🔧 우리 Wiki 구조와 비교 — 벤치마킹 검토

## 현재 우리 Wiki 구조 (DOCS 폴더 모델)

```
DOCS (My_Wiki/)
├── 000-Inbox/      ← 1차 정리본 (원본 유사)
├── Topics/         ← 주제별 지식 (정제된 지식)
├── Projects/       ← 프로젝트 문서
├── Decisions/      ← 의사결정
├── Skills/         ← 스크립트/워크플로우
├── 100-Templates/
├── 900-System/
└── index.md        ← 리렉션 데스크
```

---

## ✅ 이미 유사한 부분 (강점)

| 영상 개념 | 우리 Wiki 대응 방식 | 비고 |
|-----------|-------------------|------|
| Zotero (원본 수집) | `raw/` 폴더 + `000-Inbox/` | 원본/1차정리 분리 — 유사 |
| LLM Wiki (정제/컴파일) | `Topics/`, `Projects/` 등 정제 저장소 | 완벽 일치 |
| NotebookLM (질의응답) | AI 분석 → 문서화 | AI 분석 관점에서는 유사 |
| Obsidian (최종저장) | Obsidian Vault 연동 | 이미 Obsidian과 연동 중 |
| Claude Code 연동 | Hermes Agent + Claude Code | 도구만 다름, 개념 일치 |
| 소스 추적 | `source` 필드 + 위키링크 | Front Matter에 `source` 명시 |

---

## 🔥 벤치마킹해야 할 부분 (강화 포인트)

### 1. Zotero 연결 (높은 우선순위)

**왜 중요한가?**
- 우리 Wiki는 문서·텍스트 위주. **논문·논문집합·보고서 원본** 관리가 없음
- Zotero MCP 연동으로 원본 자동 수집+구조화 가능

**구현 방안:**
```
Zotero MCP → Zotero 컬렉션 자동생성 → PDF 추출 → Wiki Topics/ 저장
```
- Zotero는 논문·웹아카이빙·보고서의 **유일한 원본 저장소**로
- wiki/LLM-Wiki/선급_등에 Zotero 컬렉션에서 추출한 원문을 연결

**추가 가치:**
- 문헌 리뷰 자동화 (논문 컬렉션 → 문헌분석 결과)
- 소스 출처 자동 추적 (Zotero ID → 원문 PDF)
- AI 기반 논문 자동 분류 (Zotero 컬렉션 자동생성)

### 2. NotebookLM 인사이트 생성 (중요)

**왜 필요한가?**
- 현재 우리는 AI 분석 → 문서화만 하고 있음
- NotebookLM은 **소스 기반 질의응답, 요약, 인포그래픽**을 한 번에 처리

**구현 방안:**
- notebooklm-py를 통해 Wiki 자료 기반 Notebook 생성
- 복잡한 주제(예: AI 기술 대시보드)에 NotebookLM 인포그래픽 자동 생성
- AI 분석 결과물의 시각적 향상

**추가 가치:**
- Wiki 분석 결과 → NotebookLM 인포그래픽 자동 변환
- AI 요약 → 시각적 인사이트로 전환

### 3. 소스 추적 및 문서 간 연결 (보완 필요)

**현재 문제점:**
- 소스 추적은 `source` 필드로 부분만 가능
- 원본 문서(논문, 유튜브 영상, 보고서) → Wiki 분석 문서 간 **양방향 연결** 강화 필요

**강화 방안:**
```yaml
---
related_sources:
  - [[Zotero:DOI123456]]
  - [[YouTube:DC4nSUX9pCc]]
- original: [[raw/논문원문.pdf]]
  wiki: [[My_Wiki/Topics/분석문서.md]]
  notebooklm: [[NotebookLM:AI분석Notebook]]
---
```

### 4. 5층 파이프라인 도입 (장기 목표)

현재 3층 → 5층으로 확장:

| 층 | 현재 | proposed |
|----|------|----------|
| 수집 | raw/ + 000-Inbox | +Zotero(논문/보고서), +YouTube transcript |
| 정제 | Topics/ | 그대로 |
| 인사이트 | AI 분석 | +NotebookLM(질의/요약/인포그래픽) |
| 저장 | Obsidian Vault | 그대로 |
| 활용 | Hermes Agent | +Claude Code 연동 강화 |

---

## 📊 벤치마킹 실행 계획

### Phase 1: Zotero MCP 연동 (즉시 가능)
1. Zotero 데스크톱 + Zotero MCP 설치
2. Zotero → Wiki Topics/ 자동 ingest 스크립트 작성
3. 선급 설계 Rule 문서에 Zotero 출처 연결

### Phase 2: NotebookLM 인포그래픽 (API 확인 후)
1. notebooklm-py API 확인
2. AI 기술 대시보드에 인포그래픽 생성 적용
3. 분석 문서의 시각적 품질 향상

### Phase 3: 소스 추적 강화 (문서 구조 변경)
1. Front Matter에 `related_sources` 필드 추가
2. Zotero ID, YouTube ID, NotebookLM ID 연결
3. Obsidian Graph View 활용

---

*분석 완료: 2026-05-24*
*출처: YouTube (Brain Trinity, https://youtu.be/ulhEyDIxj6Q)*
