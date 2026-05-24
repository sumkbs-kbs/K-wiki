# Wiki 구조 정밀 분석 보고서 (2026-05-16)

> `~wiki` 전체를 분석하여 중복, 과밀, stale 데이터, 연결 결함 현황 파악.

## 1. 총체적 현황

| 지표 | 값 |
|------|------|
| Markdown 파일 총수 | **723개** |
| 총 용량 | **42.9 MB** |
| 최상위 폴더 수 | **9개** (git제외) |
| Wiki 인덱스 최신 | **2026-05-13** (3일전, stale) |

### 폴더별 분포

| 폴더 | 파일 수 | 용량 | 비율 |
|------|--------|------|------|
| entities/ | 313 | 37.8 MB | 43% |
| My_Wiki/ | 295 | 4.9 MB | 11.4% |
| _company/ | 84 | 85 KB | 0.2% |
| pages/ | 24 | 45 KB | 0.1% |
| tinker-nemogym/ | 4 | 12 KB | |
| notebooklm-llm-wiki-flow/ | 2 | 15 KB | |
| SystemData/ | 1 | | |
| scripts/ | | | |

---

## 2. 중복/과밀/부적합 항목 분석

### 2.1 entities/ 폴더 — 심각한 과밀 (313개/37.8MB)

**문제:** Wiki의 절반이 entities/ 폴더에 집중되어 있음. 대부분 NLW(Neural wiki) 시스템에서 자동 생성된 파일로 보임.

| 카테고리 | 개수 | 특징 |
|---------|------|------|
| tiny (<500B) | **95개** | 거의 공허한 단어 파일 (About, Advanced, Agent, Design 등) |
| small (1~10KB) | 94개 | 짧은 개념 정의 |
| medium (10~100KB) | 7개 | 중간 크기 |
| large (100~500KB) | 105개 | 대다수가 **360,000 bytes = 359.7 KB**로 동일 — 자동 생성의 의심 |
| huge (>500KB) | **3개** | `AI.md` (360KB), `GCD.md` (515KB), `Reasoning.md` (512KB), `LLLm.md` (720KB) |

**의심 점:** 105개가 정확히 359.7KB (360,000 bytes)로 동일 — 템플릿 기반 자동 생성 파일. 대부분 중복/진체 용량 확보용.

### 2.2 LLM-Wiki/GithubRepos/ 과밀 (220개/4.8MB)

**문제:** GitHub 레포지토리 분석 결과를 220개 markdown 파일로 저장. lock.yaml, package-lock.json 등 불필요 파일 포함.

**불필요 파일 (예시):**
- `claude_agent_teams_ui/bun.lock.md` (830KB)
- `claude_agent_teams_ui/pnpm-lock.yaml.md` (798KB)
- `claude-code-working/_Index.md` (194KB)
- lock 파일 총 11개

### 2.3 My_Wiki/index.md — stale (최신 안됨)

**현재 상태:**
- 마지막 업데이트: **2026-05-13** (3일전)
- 今日 2026-05-14 additions not reflected

**사실 vs 인덱스 차이:**

| 항목 | 인덱스宣称 | 실제 | 차이 |
|------|----------|------|------|
| Topics | 29개 | **30개** (+1) | +1 |
| Projects | 23개 | **17개** (-6) | -6 |
| Decisions | 13개 | **4개** (-9) | -9 |
| Skills | 8개 | **2개** (-6) | -6 |

→ index.md는 ** Projects/Decisions/Skills 세 폴더의 데이터가 모두 정확하지 않음**.

### 2.4 000-Inbox/ — 미분류 파일 6개

| 파일 | 크기 |
|------|------|
| Antigravity_Skills_Universe_MOC.md | 6KB |
| IEC_60092_Marine_Electrical_MOC.md | 2KB |
| NLW Getting Started.md | 410B |
| Plantler_Skills_MOC.md | 3KB |
| 이 사이트 안드로이드 보안 관련 핵심 내용 요약.md | 1KB |
| 지식연결_분석보고서.md | 3KB |

→ MOC 파일 3개는 Topics/로 이동해야함.

---

## 3. My_Wiki/ 구성 분석 (핵심 지식베이스)

### 3.1 Topics/ (30개 파일 / 주제별 분포)

| 분야 | 파일 수 | 대표 파일 |
|------|--------|----------|
| AI/LLM/Agent | **24개** | AI_Technology_Dashboard, YouTube_Analysis_24개 |
| 조선/marine | **9개** | IEC_60092-5개, 조선설계자동화, 조선해운, GTT, 금융 |
| Plantler/Ssak | **8개** | Plantler 4개, Ssak Image/Reader/Language 4개 |
| Wiki 자체 | **2개** | Wiki_Tree_Architecture, GraphPy |

**문제:** YouTube_Analysis 가 24개 파일로 과밀. 대부분 유사한 형식의 분석 기록 → MOC로 병합 가능.

### 3.2 Projects/ (17개 파일)

| 프로젝트 | 파일 수 |
|---------|--------|
| Antigravity-K | 2 (정밀분석, 개발계획) |
| Plantler | 4 |
| Ssak 파일류 | 7 |
| Ssak 이미지 | 2 |
| M5Max_Local_LLM_Strategy | 1 |
| AI_LLM_Agent_NewsDashboard | 1 |

### 3.3 Decisions/ (4개 파일)

→ 모두 **Plantler 프로젝트** 관련. 실제 프로젝트가 17개인데 Decisions는 4개뿐.
→ Ssak 파일류, Ssak 이미지, AI_LLM_Agent_News_Dashboard에 대한 의사결정 기록이 없음.

---

## 4. 연결 결함 분석 (Broken Links)

### 4.1 MOC 파일들 (3개)
- `Antigravity_Skills_Universe_MOC.md` → 6KB — Skills/에 존재함에도 MOC 별도
- `IEC_60092_Marine_Electrical_MOC.md` → 2KB → topics/IEC_60092-*/5개 파일과 연결 필요
- `Plantler_Skills_MOC.md` → 3KB → Topics/Plantler 4개 파일과 연결 필요

### 4.2 root/index.md (핵심 인덱스)
- 위치: `/Users/mr.k/wiki/index.md` (9,095자)
- **가장 풍부한 인덱스**인데 `My_WikI/index.md` (847자)보다 상세.
- My_WikI/index.md는 거의 비어있어 root/index.md가 실제 유일한 인덱스 역할.

### 4.3 24개 YouTube_Analysis 파일들
- 동일한 형식의 분석 결과들이 Topics/에 과밀 저장.
- 각각 마크다운 테이블, 소스 URL, 분석 결론을 포함.
- 통합 MOC 파일 하나로 압축 가능.

---

## 5. 권장 정리 작업 (우선순위)

### Priority-1 (즉시 필요)
1. **root/index.md 업데이트** — 2026-05-16의 새로운 항목 반영 (금융시장 동향, YouTube 분석 1개 추가)
2. **000-Inbox/ 파일 분류** — 6개 파일 Topics/Projects/로 이동
3. **My_WikI/Decisions/ 확장** — Plantler 밖 프로젝트 의사결정 추가

### Priority-2 (다음 주기)
4. **entities/tiny/tiny 파일 정리** — 95개 tiny 파일 중 의미 있는 것만 선별, 나머지를 단일 개념 파일로 병합
5. **LLM-WIKI/GithubRepos/ lock 파일 정리** — 11개 lock 파일 삭제
6. **YouTube_Analysis/ MOC 통합** — 24개 파일을 1개의 인덱스 MOC + 핵심 3~4개로 병합

### Priority-3 (장기)
7. **_company/, notebooklm/, tinker-* 폴더 분리** — Wiki 루트에서 별도 저장소로 이동
8. **entities/ massive file cleanup** — 360KB identical files 병합

---

## 6. 파일 목록 상세

### Topics/ (30개)
```
# AI/LLM/Agent (24개)
- AI_Technology_Dashboard_20260516.md (10.0KB)
- Wiki_Analysis_Latest_AI_LLM_Agent_News_20260514.md (0.3KB)
- YouTube_Analysis_24건 (1.1KB~8.5KB each)

# 조선/marine (9개)
- IEC_60092-101_201_301_350_401_504_General.md 각각 1~2KB
- MarineElectrical/ (2 파일 + index)
- 조선설계자동화_원가절감_전략_회의록.md (3.1KB)
-조선해운_Cable전장_혁신_5%절감_전략.md (5.0KB)
- 금융_동향_2026-05-15_16.md (2.7KB, 4.7KB)

# Plantler/Ssak (8개)
- Plantler AI 식물 분석 시스템.md
- Plantler UIUX 디자인 진화 기록.md
- Plantler 백업복원 시스템 통합.md
- Ssak Image — 2개 (AI 백엔드, 중복탐지)
- Ssak Reader — 2개 (의미론적검색, 경고억제)
- Ssak Language — 4개

# Wiki 자체 (2개)
- WikiTree_Architecture.md (4.3KB)
- GraphPy-자동-지식-그래프생성도구-20260513.md (12.5KB)
```

### Decisions/ (4개 - 모두 Plantler)
```
- Plantler v2.0 프로젝트 회고.md
- Plantler 게이미피케이션 시스템.md
- Plantler 아키텍처 의사결정 기록.md
- Plantler 프로젝트 개요.md
```

### Projects/ (17개)
```
- Antigravity-K: AI_LLM_Agent_News, Antigravity-K-정밀분석, 개발계획-코드수정반영
- Plantler: 4개 (UI/AI고도화, 실전교훈, 배포, 인증)
- SsakFile: 1개 (1.0~1.1)
- SsakImage: 2개 (AI탐지, MSStore배포)
- SsakReader: 5개 (출시, AI관리, 호환성, 모델배포)
- M5Max_Local_LLM_Strategy_and_Wiki.md
```

---

## 7. 구조화 요약

```
wiki/
├── index.md              ← 핵심 인덱스 (9KB, 최신화 필요)
├── entities/             ← 313개/37.8MB [⚠️ 과밀]
│   └── tiny/tiny/tiny   ← 95개 의미 없음 파일 [⚠️ 삭제 대상]
├── My_Wiki/
│   ├── index.md          ← stale (5/13, 847B) [⚠️ 업데이트 필요]
│   ├── Topics/           ← 30개/156KB [✅ 정상]
│   ├── Projects/         ← 17개/67KB [⚠️ Decisions 없음]
│   ├── Decisions/        ← 4개 (모두 Plantler) [⚠️ 확대 필요]
│   ├── Skills/           ← 2개 [⚠️ 6개 부족]
│   └── 000-Inbox/        ← 6개/15KB [⚠️ 분류 필요]
├── pages/                ← 24개/45KB [✅ 정상]
├── _company/             ← 84개/85KB [⚠️ 분리 검토]
├── notebooklm-llm-wiki-flow/ [⚠️ 분리 검토]
└── tinker-nemogym/       ← 4개/12KB [⚠️ 분리 검토]
```
