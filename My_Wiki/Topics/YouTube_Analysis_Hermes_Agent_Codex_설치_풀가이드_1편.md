---
title: "Hermes-Agent X Codex 설치부터 실행까지 — AI 코딩 에이전트 시작하기 #1"
topic: YouTube_Analysis_Hermes_Agent_Codex_설치_풀가이드_1편
type: topics
source: YouTube — Dante's Datalab
video_id: PqvaZaeuigk
channel: Dante's Datalab
channel_id: UCXKXULkq--aSgzScYeLYJog
upload_date: 2026-05-13
view_count: 7268
like_count: 244
duration: 49:55
date: 2026-05-15
tags: [youtube, hermes, codex, ai에이전트, AI자동화, 셀프호스팅, slack, 멀티에이전트, hostinger, vps]
related: [[AI_LLM_Agent_News_Dashboard_20260514]], [[https://github.com/trending]], [[AntiGraffiti-K]], [[https://github.com/karpathy/llm-wiki]], [[Website_Analysis_EZER_AI_Agent_University.md]], [[M5Max_Local_LLM_Strategy_and_Wiki]]
---

## 핵심 요약

단테랩스가 공개한 Hermes-Agent와 Codex CLI를 결합한 **완전한 설치·구동 가이드**. 오픈클로에서 Hermes로 마이그레이션하려는 사용자를 타겟으로, 로컬 설치 + Hostinger VPS 원클릭 설치 두 가지 방식을 모두 다룬다. Slack 연동, 대시보드 투어, 한글 패치 정보까지 포함하며, 1편은 설치에 집중하고 2편(프로필·칸반·회의실)으로 이어진다.

## 핵심 내용

### 주요 도구/기술

- **Hermes Agent** (NousResearch) — 자기학습형 AI 에이전트. 런칭 7주 만에 GitHub star 10만 돌파, 5월 기준 ~13만 star. 텔레그램/슬랙 연동 가능. 셀프 호스팅.
- **Codex CLI** (OpenAI) — 구독 플랜 기반의 AI 코딩 에이전트. GPT 모델 추가 토큰 사용량 부담 없이 Hermes와 결합 가능.
- **OpenClaw** — 기존 대안. Hermes 4/30 대규모 업데이트 이후 마이그레이션 비용이 거의 없어짐.
- **Hostinger VPS** — Hermes 원클릭 배포 지원. 10불/월대. H 패널 기반 KVM2 스펙으로 도커 매니저 연동.
- **Wave Terminal** — 오픈소스 터미널. 다중 패널, 파일 탐색, 마크다운 편집, 시스템 모니터링 통합.
- **Slack** — Hermes 메신저 채널 추천 대상. 텔레그램 대비 슬랙의 쓰레드·채널·UX 관리 우위.

### 배경/전제

- Hermes는 LM 파인튜닝계 저명 연구소 NousResearch에서 개발한 셀프호스팅 AI 에이전트
- 2026-04-30 대규모 반전 업데이트: 오픈클로에서 헤르메스로 전환 장벽 거의 제로
- 현재 버전: 0.13.0 (한글 패치 신청 완료, 영상 후 1-2일 내 업데이트 예정)

### 비교/분석

| 항목 | Hermes-Agent | OpenClaw | Codex CLI |
|------|-------------|----------|-----------|
| 개발사 | NousResearch | - | OpenAI |
| 호스팅 | 셀프호스팅/클라우드 | 셀프호스팅 | 클라우드/API |
| 모델 | 여러 프로바이더 | 여러 프로바이더 | GPT (구독제) |
| 스타 | ~13만 | - | - |
| 메신저 | TG/Slack/SMS/Matrix 등 | TG/Slack 등 | - |
| 프로필(페르소나) | ✅ 0.12.0+ | ✅ | - |
| 칸반/멀티에이전트 | ✅ | ✅ | - |
| 대시보드 | ✅ 웹 | ✅ 웹 | - |
| VPS 원클릭 | ✅ Hostinger | ✅ | - |

### 설치/구축 가이드 (요약)

**1) 로컬 설치 (CLI 마법사)**
```bash
npx @sourcegraph/hermes@latest
```
- WSL2 추천 (윈도우 네이티브 베타 준비 중)
- Full Setup 시 단계별 설정: 프로바이더, TTS, 백엔드, 이터레이션, 메신저
- Quick Setup 시 디폴트값으로 즉시 시작
- OpenClaw 마이그레이션 자동 탐지 (Y/N 선택)

**2) Hostinger VPS 원클릭 설치**
- `hostinger.com/dante-labs10` (쿠폰: DANTE-LABS, 10% 할인)
- compose → Hermes 검색 → 배포 (약 5분)
- H 패널에서 도커 매니저로 UI 관리
- SSH 터널링 → 대시보드 접근 (port 9119)
- Codaex CLI로 원격 API 호출 → 설정 자동화

**3) Slack 연동**
- bots.dev → 앱 생성 → Socket Mode + Bot Token
- 슬랙 워크스페이스에 앱 설치 → Bot Token / App Token 입력
- Allowlist User ID + Home Channel 설정
- Gateway를 시스템 서비스로 등록(auto-restart)

**4) 주요 설정 항목**
- **백엔드**: Local / Docker / Serverless / SSH
- **최대 이터레이션**: 디폴트 60, 복잡한 작업은 90, 탐색적 150+
- **컴팩팅 임계치**: 디폴트 0.5, 0.75로 증가 권장
- **세션 리셋**: 인액티브 + 일일 리셋 조합 추천
- **로컬 브라우저**: Playwright 기반 headless Chromium (무료)
- **검색 API**: Firecrawl Cloud 권장 (무료 한도 있음)

## 타임라인

| 시간 | 섹션 |
|------|------|
| 00:00 | 인트로 — Hermes vs OpenClaw 전환 논점 |
| 02:09 | 1. Hermes 설치 준비 |
| 04:50 |Codex CLI · hermes-skill 추가 |
| 06:36 | Codex × Hermes 설치 마법사 |
|15:09 | 2. Hermes × Slack 연동 |
|26:58 | Hermes 대시보드 둘러보기 |
|28:30 | 3. Hostinger VPS 원클릭 설치 |
|41:13 | Telegram · Slack 메신저 채널 설정 |
|47:39 | Slack에서 Hermes 첫 대화 |
|49:14 | 아웃트로 — 2편 예고(프로필·칸반·회의실) |

## 핵심 인사이트

1. **OpenClaw → Hermes 마이그레이션이 실질적으로 비용·학습 곡선 면에서 유리함**. 4/30 업데이트 이후 Codex 구독 플랜과 공식 연동되어 추가 토큰 비용 부담 제로.
2. **Slack이 텔레그램보다 Hermes 관리에 더 적합**. 쓰레드 기반 주제 구분, 채널 기반 멀티에이전트, UX 측면 모두 우위.
3. **Codex CLI와 결합하면 설정이 거의 자동화됨**. 자연어로 "슬랙 연동해줘"라고 요청하면 CLI가 모든 인프라 설정을 처리.
4. **VPS 원클릭 설치가 초보자에게最优**. 10불/월, 5분 설치, H 패널에서 도커 매니저로 GUI 관리. 복잡한 ssh/포트포워딩 없이 대시보드 접근 가능.
5. **프로필(페르소나) 기능으로 멀티에이전트 워크스페이스 구현 가능**. 각 프로필에 다른 모델 지정 → 작은 가상 회사 운영 패턴 예고.

## 관련 링크

- **2편 보기** (AI 팀 구성편): https://youtu.be/DuTZEAQwyLc
- **Hermes Agent GitHub**: https://github.com/NousResearch/hermes-agent
- **hermes-skill**: https://github.com/dandacompany/hermes-skill
- **Codex CLI**: https://chatgpt.com/codex
- **Hostinger (쿠폰 DANTE-LABS)**: https://hostinger.com/dante-labs10
- **Wave Terminal**: https://www.waveterm.dev/
- **실전AI 카카오 채팅방**: https://open.kakao.com/o/gURfTmqh

## M5 Max 연계성

128GB MacBook Pro M5 Max에서 HermesAgent를 **로컬 셀프호스팅**하면:
- Docker 격리 없이 로컬 백엔드로 직접 운영 가능 (중요 데이터 로컬 보존)
- GPT-5.5 (Codex 구독) + 로컬 로딩 LLM 하이브리드 구성
- 슬랙 연동 → 언제 어디서나 메신저로 AI 에이전트 접근
- M5 Max의 128GB RAM으로 로컬 모델 로딩 + Codex 클라우드 모델 조합으로 최적의 비용/성능 밸런스 달성 가능

## 이전 YouTube 분석 항목 대비 비교

| 항목 | 본 영상 (#1) | 2편 (프로필·칸반) |
|------|-------------|------------------|
| 초점 | 설치·구동·인프라 | AI 팀구성·멀티에이전트 |
| 메신저 | Slack 설정 중심 | 슬랙에서 다룹니다 |
| 프로필 | 언급만 | 실제 페르소나 구성 |
| VPS | Hostinger 원클릭 상세 | - |
| 다음 단계 | 2편으로 연결 | 실전 활용 |

## M5 Max 연계성 (추가)

본 영상에서 언급된 **로컬 vs 클라우드 전략**은 사용자의 M5 Max 환경(128GB RAM)과 직접적으로 연결:
- 중/저용량 모델은 M5 Max 로컬 로딩 → 비용 제로
- 고성능이 필요한 작업은 Codex GPT 구독 플랜으로 오프로드
- 두 가지의 하이브리드 전략이 핵심

---
*저장일: 2026-05-15 | 분석: Hermes Agent 자동 처리*
