---
title: "Claude + Hermes Agent: NEW Agent OS is INSANE!"
type: youtube
tags:
  - agent-os
  - hermes
  - claude
  - openclaw
  - obsidian
  - mission-stack
source: "https://youtu.be/nhDYrVQxBg4"
video_id: "nhDYrVQxBg4"
channel: "Julian Goldie SEO"
date: "2026-05-22"
views: "8,126"
likes: "191"
duration: "35:21"
summary: "Claude·Hermes·OpenClaw 등을 하나의 로컬 대시보드에서 통합 관리하는 'Agent OS' 구축법과 Goldy Mission Stack 4계층 아키텍처 소개"
---

# YouTube Analysis: Claude + Hermes Agent — NEW Agent OS

## 핵심 요약

Julian Goldie SEO가 직접 구축한 **Agent OS**(에이전트 운영체제)를 상세히 소개합니다. Claude, Hermes, OpenClaw 등 독립적인 AI 에이전트들을 **단일 로컬 대시보드**에서 통합 관리하는 'Goldy Mission Stack' 아키텍처입니다. **4계층 모델**(지능/실행/연구/자기)로 구성되며, Obsidian Vault를 연결해 개인 컨텍스트(목표, 저널, 메모)를 모든 에이전트가 공유하도록 설계되었습니다.

## 핵심 특징

### 1. Agent OS 개요

- **정체**: 로컬에서 실행되는 개인용 AI 운영체제
- **목적**: 분리된 AI 도구들의 단절 문제 해결 → 단일 Mission Control 대시보드
- **기술 스택**: Next.js + Tailwind (Claude Desktop에서 AI 코딩으로 1시간에 구축)
- **주요 에이전트**: Claude (AI), Hermes Agent (실행), OpenClaw (게이트웨이), Obsidian (기억)

### 2. Goldy Mission Stack — 4계층 아키텍처

| 계층 | 이름 | 구성 요소 | 역할 |
|------|------|-----------|-----|
| 1 | 인텔리전스 레이어 | Claude AI + Claude Code | 추론·계획·전략·코드 실행 (MCP 연동) |
| 2 | 실행 레이어 | OpenClaw | 에이전트 간 작업 라우팅·마ulti-에이전트 조정 (라우터 역할) |
| 3 | 리서치 레이어 | Hermes Agent | 실시간 작업 실행 (Kanban, 스킬/플러그인, 스케줄러) |
| 4 |セルフ 레이어 | Obsidian Vault (Omi) | 개인 기억 시스템: 목표·저널·메모·아이디어 |

### 3. 핵심 구성 요소 상세

#### 미션 컨트롤 대시보드
- 모든 에이전트의 실시간 상태 표시
- 에이전트별 Control Room (API 키, 인증, 이전 세션, 스킬, 플러그인)
- 활동 분석: 30일 사용 패턴, 피크 시간, 활성 세션
- 목표/저널/메모 통합 관리

#### Obsidian 기억 시스템 ("Infinite Context Engine")
- **목표 추적**: 진행률 바 + 에이전트가 목표 인식
- **저널**: 매일의 활동 (음성/텍스트, 일일 파일)
- **기억**: 모든 대화 자동 로깅 → 1,261개 메모 이상 축적
- **Omi 도구**: 화면/마이크 실시간 녹화 → 개인 프로필 자동 구축
- 양방향: 에이전트가 노트 읽기 + 대화 내용을 노트에 쓰기

#### 기술적 특징
- **로컬 퍼스트**: 모든 데이터 로컬 머신에 저장 (보안·속도·프라이버시)
- **확장성**: 추가 에이전트 스택 가능 (OpenHuman, SEO 에이전트 등)
- **Claude 코드로 구축**: 비개발자도 "친구에게 채팅"하듯 구축 가능
- **무료 옵션**: Hermes Agent + Step 3.5 Flash (무료 API) 사용 시 완전 무료

### 4. Agent OS vs 기존 AI 사용 방식

| 구분 | 기존(단일 도구) | Agent OS |
|------|----------------|----------|
| 메모 | 없음 (세션마다 초기화) | Obsidian 연동, 무한 기억 |
| 조정 | 수동 (탭 전환/복사) | 자동 (미션 컨트롤 통합) |
| 컨텍스트 | 도구별 분리 | 개인 전역 컨텍스트 공유 |
| 확장성 | 수동 설정 | 스택 방식으로 손쉬운 추가 |
| 운영자 | '작업자' | '지휘자' |

### 5. 핵심 메시지

> **"도구를 사용하는 것과 시스템을 운영하는 것의 차이는 해머와 건설회사의 차이"**

단일 AI 도구 → 운영 시스템으로의 전환이 핵심. 에이전트가 24시간 작업을 대신하고, 사용자는 미션 운영자(Mission Operator) 역할만 수행.

---

## 우리 프로젝트 연관성

### 1. Ssak-AI-Lab DataBridge에의 적용 가능성 ⭐⭐ (높음)

#### 현재 상태
- Hermes는 이미 OpenClaw subordinate agent로 구동 중
- Ssak-AI-Lab DataBridge(FastAPI 8002)가 모바일 인제스트 처리
- 각각 독립적으로 작동

#### Agent OS 방식 적용 시 기대효과
- **통합 대시보드**: DataBridge 상태 + Hermes 세션 + OpenClaw 세션을 한 화면에서 모니터링
- **기억 시스템 관통**: 각 서비스의 컨텍스트를 Obsidian/Memory에 중앙 집적
- **목표 기반 자동화**: DataBridge 업로드 → STT → Wiki 저장 워크플로우를 Agent OS의 '실행 레이어'로 통합

### 2. Antigravity-K 에이전트 아키텍처 참조

- **4계층 모델**은 Antigravity-K 설계에 직접 반영 가능
  - 인텔리전스: Claude/LLM 레이어
  - 실행: Hermes/OpenClaw 작업 라우팅
  - 리서치: 웹/데이터 수집 레이어
  -セルフ: 개인/프로젝트 기억 레이어
- **미션 컨트롤** 개념은 Antigravity-K의 중앙 제어부 설계 영감이 됨

### 3. Weekly AI Briefing 향상

- 현재: RSS → Gmail 발송 (단일 워크플로우)
- Agent OS: 리서치 계층이 최신 AI 뉴스를 수집 → 인텔리전스 계층이 선별 → 실행 계층이 발송, 모든 단계가 Obsidian에 기록

### 4. 금일 적용 가능 여부: **부분적 즉시 가능** ⭐⭐⭐

| 적용 항목 | 가능 여부 | 소요 예상 |
|-----------|----------|-----------|
| Skill Bundles (이전 분석) | ✅ 즉시 | 분 |
| Obsidian 연동 (기억 레이어) | ✅ 즉시 | 30분 |
| 미션 컨트롤 대시보드 | ⚠️ 선택적 | 1-2일 |
| 완전한 4계층 모델 | 🔄 단계적 | 1주일 |

---

## 시사점

1. **로컬 퍼스트 철학**: 개인 데이터의 보안/속도/프라이버시 측면에서 로컬 실행이 클라우드보다 우위
2. **에이전트 간 컨텍스트 공유**: 개별 도구가 아닌 "시스템"으로 접근할 때 시너지 급증
3. **기억 시스템의 중요성**: Obsidian 연동이 가장 강력한 차별화 요소 (대부분의 경쟁자가 이것을 간과)
4. **비개발자 접근성**: Claude Desktop에서 AI 코드로 구축 가능 → 진입 장벽 낮춤
5. **운영자의 역할 변화**: '작업자' → '지휘자'로 전환. 에이전트가 실행, 사람이 방향성 결정
6. **축적의 힘**: 시스템이 갈수록 스마트해짐 (사용일수록 컨텍스트 확대)

---

## 기술 스택 요약

| 기술 | 역할 | 비용 |
|------|------|-----|
| Claude AI/Code | 추론·계획 레이어 | 유료 (Anthropic API) |
| Hermes Agent | 실행·리서치 레이어 | **무료** (오픈소스) |
| OpenClaw | 게이트웨이·라우팅 | **무료** (오픈소스) |
| Obsidian | 개인 기억 시스템 | **무료** |
| Omi | 실시간 프로필 수집 | **무료** |
| Next.js + Tailwind | 대시보드 UI | **무료** |

---

*문서 생성일: 2026-05-22 | 원문 영상의 스크립트를 기반으로 재구성*
