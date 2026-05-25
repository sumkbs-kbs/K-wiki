# 📖 Paperclip 설치 및 연동 가이드

## 📋 개요

**Paperclip**: AI 에이전트 팀을 조직으로 운영하는 오케스트레이션 도구 (완전 무료, MIT License)

**핵심 기능**:
- ✅ AI 부서 구성 (CEO→엔지니어→디자이너)
- ✅ 작업 티켓 관리 (대시보드)
- ✅ 에이전트별 월 예산 제어
- ✅ Heartbeat 자동 실행
- ✅ 거버넌스 (승인, 정지, 종료)
- ✅ 다중 회사 분리 관리

**비용**: **월 $0** (완전 무료, self-hosted)  
**설치**: `npx paperclipai onboard --yes` (원클릭)  
**접속**: http://localhost:3100

---

## 🧩 우리 시스템과의 연동 구조

```
┌──────────────────────────────────────────────┐
│         Paperclip (대시보드:3100)            │
│         AI 회사 운영 OS                       │
│   부서구성 / 티켓 / 예산 / 거버넌스          │
└──────────────┬───────────────────────┬──────┘
               │ Heartbeat              │ Heartbeat
       ┌───────┴───────┐          ┌─────┴─────┐
       │  OpenClaw     │          │  AGK      │
       │  (예: 디자이너)│          │ (예: 개발자)│
       └───────────────┘          └───────────┘
```

### 연동 시나리오

| 업무 | Paperclip 역할 | 연결 에이전트 |
|------|----------------|---------------|
| 콘텐츠 제작 | 티켓 → 목표 설정 → 승인 | OpenClaw (디자이너) |
| 코드/기능 구현 | 티켓 → 목표 설정 → 승인 | AGK (개발자) |
| Wiki 관리 | 티켓 → 문서 생성/수정 | Herme (편집자) |
| 주간 리포트 생성 | 자동 Heartbeat 실행 | Herme |
| 주식/금융 분석 | 티켓 → 조사 → 보고 | Herme |

---

## 🚀 설치 방법 (Mac)

### 1. 원클릭 설치 (기존 완료)

```bash
npx paperclipai onboard --yes
```

### 2. 설치 완료 확인

```bash
paperclipai doctor  # 9개 체크 통과
```

### 3. 서버 실행

```bash
paperclipai run  # localhost:3100 시작
```

### 4. 대시보드 접속

**http://localhost:3100**

첫 실행 시 "Create your first company" 화면 → "Start Onboarding" 클릭

---

## ⚙️ 설정 파일 경로

| 항목 | 경로 |
|------|------|
| **설정** | `/Users/mr.k/.paperclip/instances/default/config.json` |
| **DB** | `/Users/mr.k/.paperclip/instances/default/db` (Embedded PG) |
| **시크릿** | `/Users/mr.k/.paperclip/instances/default/secrets/master.key` |
| **JWT** | `/Users/mr.k/.paperclip/instances/default/.env` |
| **로그** | `/Users/mr.k/.paperclip/instances/default/logs` |
| **백업** | `/Users/mr.k/.paperclip/instances/default/data/backups` |
| **저장** | `/Users/mr.k/.paperclip/instances/default/data/storage` |

---

## 🔗 Wiki 파이프라인 연동

### 1. "Company" 생성
- Company명: `ssak-ai-lab` (우리 회사)
- 목표: `AI 기반 개발 자동화 및 AI/IT 분석 지식베이스 구축`

### 2. Agent 배치 (예시)

| 역할 | 이름 | 연결 |
|------|------|------|
| **CEO** | Herme | 메인 허브 |
| **Developer** | AGK | Antigravity-K |
| **Designer** | OpenClaw | 부하 직원 |
| **Researcher** | External | 웹 검색 |
| **Writer** | Wiki | 파일시스템 |

### 3. Task 생성 예시

| 제목 | 담당 | 상태 |
|------|------|------|
| "AI 시장 동향 분석 리포트" | Herme + Researcher | 신규 |
| "Wiki 인덱스 업데이트" | Wiki | 진행중 |
| "신규 기능 구현" | Developer | 완료 |

---

## 💡 주요 기능

| 기능 | 설명 | 중요도 |
|------|------|--------|
| **Heartbeat** | 에이전트 자동 실행 (30초 간격 기본) | ⭐⭐⭐⭐⭐ |
| **비용 제어** | 에이전트별 월 예산, 초과 시 자동 정지 | ⭐⭐⭐⭐⭐ |
| **Task System** | 티켓 기반 관리, 작업 추적 | ⭐⭐⭐⭐ |
| **Governance** | 승인 게이트, 에이전트 정지/종료 | ⭐⭐⭐⭐ |
| **Multi-Company** | 단일 배포로 여러 회사 분리 | ⭐⭐⭐ |
| **Export/Import** | 회사 설정 저장/복원 | ⭐⭐⭐ |

---

## 📊 시스템 비교

| 기능 | 우리 기존 (Wiki 수동) | Paperclip 자동화 |
|------|---------------------|------------------|
| 작업 관리 | 파일 기반 (수동) | 티켓 기반 (자동) |
| 비용 추적 | 없음 | 에이전트별 월 예산 |
| Heartbeat | Cron (별도) | 내장 지원 |
| 대시보드 | 없음 | React UI (내장) |
| 예산 제어 | 없음 | hard stop |
| 감사 로그 | 없음 | 전체 추적 |

---

*작성: 2026-05-25 | 라이선스: MIT | 설치: npx paperclipai onboard --yes*
