---
title: "오펜디자인+코덱스로 평면도 3D 변환 앱 — 처음부터 만들기"
type: youtube
tags: [오pendesign, 코덱스, 평면도3d, 2d-3d, 하이퍼프레임스, 코드워즈워크, 컴퓨터유즈]
source: YouTube
channel: 바비랩스
channel_id: @바비랩스
video_id: 66BqddouzWA
url: https://youtu.be/66BqddouzWA
duration: "25:01"
published: "2026-05"
summary: "OpenDesign → 디자인 핸드오프 MD → Codex CLI 백엔드/2D 분석 → 3D 뷰어 → GLB 다운로드 → HyperFrames MP4 — 풀스택 파이프라인 실습"
related: [[하네스 설계 vs 프롬프트 설계]], [[SmallCode]], [[AgentMemory]]
---

# 오픈디자인+코덱스로 평면도 3D 변환 앱 — 처음부터 만들기 🏗️

> **영상:** [바비랩스 — 오픈디자인+코덱스로 평면도 3D 변환 앱](https://youtu.be/66BqddouzWA) (25분 1초)

## 핵심 요약

**OpenDesign (클라우드 디자인 오픈소스)**로 3화면 디자인 → **디자인 핸드오프 MD**로 규칙 전달 → **Codex CLI**로 풀스택 구현 → **HyperFrames**로 MP4 영상까지. **사람은 디자인 3화면 + 실패 지점 코멘트만 남기고 나머지는 코덱스가 전액 처리.**

---

## 주요 내용

### 파이프라인 (전체 흐름)

```
OpenDesign (디자인)
     ↓ [디자인 핸드오프 MD]
Codex CLI (프로젝트 부트스트랩)
     ↓
   백엔드: Rails + SQLite + Active Storage
     ↓
   2D 분석 모듈: GPT-5.5 (Codex CLI EXEC 호출)
     ↓
   3D 뷰어: Three.js + 2D → 3D 변환
     ↓
   GLB 다운로드
     ↓
HyperFrames (MP4 영상 렌더링)
```

### 핵심 기술 스택

| 레이어 | 기술 |
|--------|------|
| **디자인** | OpenDesign (클라우드 디자인 클론 오픈소스) |
| **핸드오프** | 디자인 명세서 MD (라우트·컴포넌트·상태·API 정의) |
| **백엔드** | Ruby on Rails + SQLite + Active Storage |
| **2D 분석** | Codex CLI EXEC 방식 (외부 API 개입 없이 GPT-5.5 호출) |
| **3D 렌더링** | Three.js (웹 브라우저 내) |
| **영상** | HyperFrames 플러그인 (HTML → MP4, 30초 내외) |
| **테스트** | Codex Computer Use (브라우저 내 자동 클릭/테스트) |
| **장기 실행** | `/goal` 스킬 (목표 달성 시까지 미정지) |

### 핵심 인사이트

1. **디자인의 가치는 화면 자체가 아니라 핸드오프 명세서**. 이미지 던지는 게 아니라, 라우트·컴포넌트·상태·API 연결을 **텍스트로 정리**해서 넘기는 것. Codex는 이미지보다 잘 작성된 문서를 잘 읽는다.
2. **CLI EXEC 방식**. 외부 API 비용 부담 → Codex CLI를 EXEC 호출로 내부에서 GPT 처리. API 키 누출·비용 문제 해결.
3. **Codex 앱 vs CLI**. `/goal` 스킬은 앱에서는 나타나지 않음, CLI에서만 사용 가능. CLI가 더 강력.
4. **Computer Use 자동 테스트**. 샌드박스 제약으로 GLB 다운로드 직접 불가 → 크롬 브라우저 실행 → 브라우저 내에서 테스트 → 코드 수정 피드백. 사람이 클릭할 것을 AI가 대신.
5. **역할 변화**. "코드를 설계·작성" → **"어떻게 Codex가 원하는 결과를 만들지 오케스트레이션"**. 판단력, 도구 배치, 성공 기준 설정이 중요해짐.

### 실습 중 발견한 문제점

- OpenDesign 브라우저 깨짐 현상 (화면 공유 버튼 작동 안함) → PDF/MD로 별도 내보내기 필요
- 분석 버튼 UI 부자연스러움 (업로드만 되고 반응 없음) → 프로그레스바로 진행 표시 필요
- 3D 생성 후 인스펙터에 에러 다수 (GLB 변환 실패) → 수정 후 재시도
- GLB 다운로드 샌드박스 제약 (외부 브라우저 → 프로젝트 폴더 이동 필요)
- 최종 MP4 퀄리티: 와이어프레임형 프레임만 있는 저퀄리티 → 내부를 돌아다니는 효과는 나왔으나 퀄리티 부족

## 연관성

- **[하네스 설계 vs 프롬프트 설계](20260523_youtube_harness-vs-prompt-codex-cards.md)** — Karpathy의 원칙이 여기 그대로 구현됨 (goal 모드, 서브에이전트, 검증 스테이커스)
- **SmallCode** — 코딩 에이전트 하네스의 실제 구현. 여기서는 Codex 대신 SmallCode로 동일 파이프라인 가능
- **AgentMemory** — 세션 간 기억 + 핸드오프 문서 자동 관리 가능. 디자인 → 코딩 간 정보 손실 방지
- **컴퓨터 사용** — Codex의 Computer Use 기능으로 외부 도구 자동 테스트 (HyperFrames GLB 다운로드 등)

## 관련 분석

| 링크 | 제목 | 채널 |
|------|------|------|
| [[하네스 설계 vs 프롬프트 설계]] | Karpathy 코딩 워크플로우 6원칙 | 바비랩스 |
| [[SmallCode]] | 소형 LLM(7B~20B) 전용 코딩 에이전트 | Doorman11991 |
| [[AgentMemory]] | AI 코딩 에이전트 영구 메모리 | Rohit G |
| [OpenDesign GitHub](https://github.com/calebeby/open-design) | OpenDesign (클라우드 디자인 클론) | calebeby |
