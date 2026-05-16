---
type: Wiki
topic: Website_Analysis
source: website
url: https://maily.so/makersnote/posts/1do1dwqlox6
date: 2026-05-16
status: Refined
author: Product Makers Note
channel_url: https://maily.so/makersnote
tags: [superpowers, claude-code, AI코딩, 컨텍스트오염, AI에이전트, 워크플로우, 플러그인, 시각화]
related: [[Claude_Code_Max]], [[M5Max_Local_LLM_Strategy_and_Wiki]], [[AntiGraffiti-K]], [[AI_Technology_Dashboard_20260516]], [[GitHub_Repos_Superpowers_Analysis]]
---

# 웹사이트 분석: Product Makers Note - Superpowers 사용기

> **원문**: https://maily.so/makersnote/posts/1do1dwqlox6
> **저자**: Product Makers Note ("판교에서 여의도까지" — 프로덕트 메이커들의 기획·디자인·AI 노트)
> **작성일**: 2026.05.13 | **조회**: 1.21K

---

## 1. 핵심 요약

GitHub 19만 스타를 받은 Claude Code 플러그인 **Superpowers**의 실제 사용기. "AI한테 메모앱 만들어달라고 했더니, 먼저 같이 기획서부터 쓰자고 하던데요"라는 제목으로, Superpowers가 스펙-먼저-작동하는 AI 코딩 워크플로우를 어떻게 혁신하는지 상세히 분석.

---

## 2. 핵심 내용

### 2.1 문제 인식: AI 코딩의 근본 한계

- "클로드야, 우리 아까 분명히 약속했잖아..." — AI가 기획과 다른 기능 추가
- 코드가 비대해지며 버그 터지고, 수정 요청 시 저장 기능 작동 안 함
- AI가 자신의 코드를 객관적으로 평가할 수 없는 근본 문제
- **핵심 문제**: 0→1는 빠르지만, 1→100은 기획자에게 고문의 시간 소모

### 2.2 Superpowers 핵심 기능

#### 기능 1: 스펙 먼저 물어보고, 나중에 코드
- 일반 AI 코딩: "메모앱 만들어줘" → 바로 코드
- Superpowers 적용: `brainstorming 스킬` 발동 → 소크라테스식 질문으로 요구사항 캐내기 → 스펙서 작성 → 승인 → `writing-plans` → 개발 플랜 작성 → OK 후 코드
- **기획자 입장**: AI가 먼저 물어봐주는 경험을 기획자와 개발자의 소통 문제 자동 해결

#### 기능 2: 스펙이 "휘발되지 않는 문서"로 저장
- 파일로 저장 → 세션 리셋 후에도 스펙 유지
- 서브 에이전트들도 스펙서 참조 → 사람이 나중에 검증 가능

#### 기능 3: "스펙을 준수했는지" 별도 검증
- 작업마다 새로운 서브 에이전트 생성
- 리뷰어 서브에이전트가 2단계 검수: **스펙 준수 → 코드 품질**
- 일반 AI 코딩 도구에는 이런 검증 단계 아예 없음
- **셀링 포인트**: "AI가 두세 시간 자율적으로 일해도 계획에서 안 벗어난다"

### 2.3 Visual Companion 기능
- 브레인스토밍 중 AI가 "이건 보여드리는 게 낫겠다" 판단 시 → 로컬 HTTP 서버에 HTML 파일 작성
- 브라우저(`localhost:64816`) 또는 Launch Preview 패널에서 즉시 확인
- 텍스트 대신 **클릭으로 선택** 가능

---

## 3. 자동 발동 스킬 매핑

| 요청 | 자동 발동 |
|---|---|
| "이 버그 고쳐줘" | `systematic-debugging` |
| "코드 리뷰해줘" | `requesting-code-review` |
| "새 기능 만들어줘" | `brainstorming` → `writing-plans` → `executing-plans` |

---

## 4. 재태그/전략적 인사이트

- **GitHub 19만스타 = 검증된 도구**: 이미 실제 업계에서 검증된 AI 코딩 도구
- **컨텍스트 오염 해결**: 오늘 분석했던 GStack+GSD 영상과 같은 문제 (컨텍스트 오염) 에 대한 **구현적 답변**이 슈퍼파워스
- **M5 Max 연계성**: Superpowers + M5 Max 로컬 LLM은 **온-프레미스 AI 개발 파이프라인** 핵심 조합
- **Claude Code Desktop**: Max 플랜 이상 필요 (Pro는 Web만)

---

## 5. 관련 Wiki 문서

- [[Claude_Code_Max]] — Claude Code 활용 가이드
- [[M5Max_Local_LLM_Strategy_and_Wiki]] — M5 Max 전략적 활용
- [[AntiGraffiti-K]] — 에이전트 시스템 분석
- [[AI_Technology_Dashboard_20260516]] — AI/LLM 기술 동향 대시보드
- [[GitHub_Repos_Superpowers_Analysis]] — Superpowers GitHub 레포 분석
- [[GStack_GSD_Superpowers_Workflow]] — GStack+GSD+Superpowers 결합 워크플로우 (YouTube 분석)

---

*이 문서는 maily.so Product Makers Note 아티클을 분석하여 WikiTree 아키텍처의 증분 업데이트 패턴에 따라 작성되었습니다.*
