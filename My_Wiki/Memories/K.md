# K (강병석) — 장기 기억 프로필

> **주의:** 이 문서는 AI의 장기 기억 시스템입니다. 세션이 재시작되거나 메모리가 초기화되더라도 이 파일에서 정보를 불러와야 합니다. 김봉석, BS K, 과장 — 모두 틀린 호칭/이름입니다.

---

## 📌 핵심 정보 (절대 변경 금지)

| 항목 | 값 |
|------|---|
| **이름** | 강병석 |
| **닉네임** | K |
| **Email** | sumkbs@gmail.com (삼성: bs06.kang@samsung.com) |
| **Device** | Android phone (SKT 5G) + Tailscale bridge |
| **Domain** | 조선 설계 자동화 및 원가 절감 전략 |
| **필수 언어** | 한국어 |

---

## 🏢 전문 분야

- 조선 설계 자동화 (Plantler)
- AI 기반 사내 도구 (Ssak)
- 로컬 LLM 에이전트 (Antigravity-K)
- 금리/기술 트렌드 연계 분석 (주식 투자)

---

## 🧠 작업 원칙

1. **김봉석이라는 잘못된 정보는 절대 인용 금지** (과거 세션에서 잘못 기록됨)
2. BS K, 과장 호칭도 부정
3. 단순 확인 요청 금지 — 검증 가능한 근거와 함께 응답
4. Wiki는 외부 장기 기록으로 활용
5. 반복 작업은 cronjob으로 자동화 권장

---

## 📊 주식 포트폴리오 (요약)

- Kiwoom Securities 6계좌
- 방산/반도체 ETF/AI/고배당 중심
- 총 자산 약 27M 원 (변동 가능)
- 포트폴리오 편중 리스크 인지 필요 (삼성전자+SK하이닉스 시총 50% 이상)

---

## 🏗️ 주요 프로젝트

### Antigravity-K
- 위치: `/Users/mr.k/program/coding/ssak_comp/antigravity-k/`
- 목적: 로컬 LLM 기반 자율 에이전트 — Claude Code/Codex 추월 목표
- 현재: 개발 중, qwen3.6:latest 기반

### Plantler
- 위치: 삼성현수 (Samsung Town) 내
- 목적: 조선 설계 자동화 및 원가 절감
- 관련 Wiki: `My_Wiki/Projects/Plantler_*`

### Ssak
- 목적: AI 기반 사내 도구 모음 (Image Reader/Language/Knowledge)
- 관련 Wiki: `My_Wiki/Projects/Ssak_*`

---

## 🧩 시스템 환경

- **OS:** macOS (26.5)
- **Device:** M5 Max, 128GB RAM, 4TB
- **Python:** 3.9 (Xcode Command Line Tools)
- **Node.js:** 20.x (Miniforge)
- **Miniforge path:** `/Users/mr.k/miniforge3/`
- **Wiki:** `/Users/mr.k/wiki/`
- **Git remote:** `https://github.com/sumkbs-kbs/K-wiki.git`

---

## 🔧 API/키 현황

- **OpenRouter:** 설정 완료 (sk-or-...d84d), 결제 미완료 (무료 모델 사용 가능)
- **ngrok:** Auth token 완료 → Dynamic URL로 모바일 브리징
- **Tavily:**内置, API 키 불필요
- **Edge TTS:**内置, API 키 불필요

---

## 📅 Cronjob 현황 (2026-05-27 기준)

| Job | Schedule | Next Run |
|-----|----------|----------|
| 금융시장 매일 동향 | 07:00 매일 | 2026-05-28 07:00 |
| AI/LLM/Physical AI 주간 업데이트 | 09:00 화,목 | 2026-05-30 09:00 |
| ai-tech-briefing (주4/목) | 09:00 목 | 2026-05-28 09:00 |

---

## 💡 학습 기록 (시행착오)

### 2026-05-27: 이름 오류 교정
- **문제:** memory에 `김봉석`으로 잘못 기록
- **원인:** 초기 세션에서 잘못된 정보 삽입 → 자동 누적
- **해결:** memory tool로 전량 삭제 후 `강병석`으로 재설정
- **교훈:** 새로운 정보는 즉시 검증 후 memory에 기록해야 함
- **방안:** 주기적 memory 내용 검증 cronjob 필요

### 2026-05-26: 메모리 용량 초과 문제
- **문제:** MEMORY 97%, USER 98% → 새 정보 추가 시 가장 오래된 항목 삭제
- **해결:** 메모리 항목 정리 + Wiki 외부 저장소 활용
- **방안:** 10,000자 이상 확장 권장

---

## 🎯 다음 작업 우선순위

1. [ ] Wiki/Memories/ 폴더 구조화
2. [ ] Cronjob에 "기억 정리" 추가 (매일 07:00)
3. [ ] config.yaml memory provider 설정 검토
4. [ ] sessions/ 폴더 구조화 (세션별 핵심 기록)
5. [ ] Decisions/ 폴더 구조화 (의사결정 이력)

---

#claude-md #memory-system #long-term-knowledge
