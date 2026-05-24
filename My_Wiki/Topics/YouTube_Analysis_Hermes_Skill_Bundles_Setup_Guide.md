# YouTube_Analysis_Hermes_Skill_Bundles_Setup_Guide

## 핵심 요약

Hermes Agent에 새로 추가된 **Skill Bundles** 기능을 상세히 소개합니다. Skill Bundles는 여러 스킬을 한 번에 묶어서 `{/bundles}` 커맨드로 로드하는 방식으로, 프로세스 매뉴얼(시퀀셜)이 아닌 **에이전트 자율 판단(adaptive)**으로 실행됩니다. 복잡한 워크플로우에서 스킬을 번들로 묶으면 컨텍스트 효율성, 일관성, 생산성이 모두 향상됩니다.

[[Claude + Hermes Agent: NEW Agent OS — Goldy Mission Stack 4계층 아키텍처]]
[[Hermes/Obsidian/Omi Memory]]

## 핵심 특징

### 1. Skill Bundles 란?

여러 스킬을 이름 있는 모음(bundle)으로 정의해 한 번의 커맨드로 로드합니다.

- **YAML 파일로 저장**: `~/.hermes/skill_bundles/` 디렉토리에tiny YAML 파일로 저장
- **명령어**: `/bundles create <이름>`, `/bundles list`, `/bundles reload`
- **핵심 필드**: `name`(실행 커맨드가 됨), `skills`(리스트), `description`(선택), `instruction`(선택 — 하우스 룰/가이드라인)

### 2. 왜 필요한가?

기존 방식:
```
작업 → 서브태스크 5개 → 5번의 스킬 개별 호출 → 컨텍스트 소모
```

Skill Bundles 방식:
```
작업 → /research → 모든 스킬 자동 로드 → 컨텍스트 효율적
```

주요 문제점 해결:
- **프로바이리스트성**: 에이전트가 필요한 스킬을 모두 사용하지 않을 수 있음
- **시간 소모**: 여러 번의 커맨드 필요
- **결과 불일치**: 자연어로 작성 시 에이전트의 행동이 일관되지 않음

### 3. YAML 구조 예시

```yaml
name: research
description: "일반 연구 워크플로우"
skills:
  - web-search
  - web-extract
  - file-read
  - codebase-inspection
  - git
instruction: |
  연구를 진행할 때 다음 규칙을 지켜주세요:
  - 1차 자료는 공식 문서 우선
  - 한국어 자료도 적극 활용
  - 결론은 불릿 포인트로 정리
```

### 4. 핵심 설계 원칙

| 요소 | 설명 |
|------|-----|
| name | 워크플로우 이름 → `/` 커맨드로 실행 |
| skills | 해당 워크플로우에 필요한 스킬 리스트 |
| description | 선택 — 번들 설명 |
| instruction | 하우스 룰 = mini `.agents.md` — 컨텍스트 중복 제거 |

### 5. 주요 명령어

```
/bundles create <workflow-name>   # 새 번들 생성
/bundles list                     # 등록된 번들 목록
/bundles reload                   # YAML 재읽기
```

### 6. 효과적인 번들 작성 원칙

1. **의도적으로 선택**: 워크플로우에 꼭 필요한 스킬만 포함
2. **instruction 필드 활용**: 자신의 습관/규칙을 bake-in
3. **에이전트와 먼저 상담**: 스택 조합은 에이전트와 논의 후 결정
4. **팀 공유**: 번들 파일을 `.dotfiles` 또는 공유 레포에 커밋

### 7. adaptive 실행 모델 ⭐

**핵심!** Skill Bundles의 스킬은 시퀀셜이 아닙니다. 각 스킬이 독립적인 가이드라인으로 제공되며, 에이전트가 **자신의 판단으로 필요한 스킬을 순서대로 선택해 실행**합니다. 즉, 에이전트가 각 단계에서 적절한 스킬을 동적으로 선택하는 **adaptive** 패턴입니다.

---

## 우리 프로젝트 연관성

### 1. Ssak-AI-Lab 인프라 개선

현재 Hermes는 개별 스킬을 하나씩 호출하는 방식. Skill Bundles를 적용하면:
- `web-data-ingest` 번들: web-search + web-extract + file-write 묶음
- `wiki-knowledge` 번들: obsidian + search + file + git 묶음
- `daily-briefing` 번들: rss + gmail + translation 묶음
- `code-review` 번들: codebase-inspection + github-code-review + github-pr-workflow

### 2. Antigravity-K 개발 워크플로우

- `full-stack-dev` 번들: python-debugpy + github-pr-workflow + test-driven-development + writing-plans
- `research-deploy` 번들: web-data-collection + jupyter-live-kernel + serving-llms-vllm

### 3. Weekly AI Briefing 자동화

- `weekly-briefing` 번들: blogwatcher + gmail + translation → HTML/PPTX 생성

### 4. 금일 적용 가능 여부: **즉시 적용 가능** ✅

Skill Bundles는 기존 Hermes 설치에 이미 내장된 기능. YAML 파일만 생성하면 바로 사용 가능합니다.

---

## 시사점

1. **에이전트 간 컨텍스트 효율성**: 5개 스킬을 분리 호출할 때의 컨텍스트 오버헤드를 1회 로드만으로 해결
2. **일관성**: instruction 필드로 하우스 룰을 고정 → 결과의 일관성이 크게 향상
3. **확장성**: 번들 파일 Git 관리 → 팀 공유, 버전 추적, 재사용 용이
4. **적응형 실행**: 시퀀셜이 아닌 adaptive → 에이전트 자율 판단으로 워크플로우 유연성 확보
5. **실무 적용 가치**: 매우 높음. 특히 반복 워크플로우(데이터 인제스트, 위키 정리, PR 리뷰)에서는 즉각적인 효과

## 참조 정보

| 항목 | 내용 |
|------|-----|
| 영상 제목 | Hermes Agent NEW Skill Bundles (Setup Guide) |
| 채널 | Ron (Ron's AI channel) |
| 길이 | 10분 13초 |
| 업로드 | 2026년 5월 |
| 핵심 기술 | Skill Bundles, YAML config, adaptive skill loading |
| 관련 기술 | .agents.md, mini agents.md 패턴, Git-based 번들 관리 |

---

*문서 생성일: 2026-05-22 | 원문 영상의 스크립트를 기반으로 재구성*
