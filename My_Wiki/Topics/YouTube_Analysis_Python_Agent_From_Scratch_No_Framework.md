---
id: you_tube_analysis_00144
title: 파이썬으로 AI Agent 만들기 - 프레임워크 없이 직접 구현
created: 2026-05-19T21:15:00+09:00
updated: 2026-05-19T21:15:00+09:00
type: youtube
tags: [youtube, python-agent, framework-free, agent-design, hermes-paradigm]
source: https://youtu.be/3wk45Ow3m3M
source_channel: 다비드스튜디오 dabidstudio
duration: '43:03'
summary: 프레임워크 없이 Python으로 AI Agent 직접 만드는 법
---

# 파이썬으로 AI Agent 만들기 (프레임워크 X)

## 📌 핵심 정보

- **제목**: 파이썬으로 AI Agent 만들기 (프레임워크 X)
- **출처**: https://youtu.be/3wk45Ow3m3M
- **채널**: 다비드스튜디오 dabidstudio
- **길이**: 43분 3초
- **시청 수**: 1.3천+개
- **날짜**: 최근

## 🔑 핵심 요약

### 이 영상이 다루는 내용:
LangChain, CrewAI 등 **외부 프레임워크 없이** Python의 표준 라이브러리와 LLM API만으로 AI Agent를 직접 구현하는 방법을 소개. Agent의 핵심 원리: **인지 → 계획 → 도구 실행 → 피드백** 사이클을 직접 코딩.

### 주요 특징:
1. **프레임워크 불필요**: 외주 라이브러리 없이 순수 Python 기반 Agent 구현
2. **핵심 원리 파악**: Agent의 본질적인 동작 메커니즘 이해
3. **실전 코드**: loop 구조, prompt engineering, tool calling 직접 구현

## 💡 우리 Hermes Agent와 직접적인 연관성

### 핵심 연관성: 매우 높음

Hermes Agent의 핵심 구조:
```
user request → agent loop:
  1. prompt LLM (인지)
  2. decide action (계획)
  3. execute tool (실행)
  4. process result → decide next (피드백)
  5. respond when complete
```

이 영상에서 다룰 Agent 구조와 **정확히 동일한 패턴**을 구현:
- loop 기반 의사결정 (Hermes `agent_loop`)
- tool dispatch (Hermes `browser_*`, `skill_*`, `cronjob` 등)
- context management (Hermes `session_search`, `memory`)

### 핵심 인사이트:
 프레임워크에 의존하지 않은 Agent 구현 → our Hermes와 동일한 철학
- loop 기반 Agentic architecture가 프레임워크 vs 직접구현 모두 동일하게 작동
- **실제 코드 구조**를 통해 our Hermes의 설계 의도 검증 가능

## 📊 분석 메타데이터

- **실습 난이도**: ★★★★☆ (고급)
- **적용 가능성**: 높음 (Agent 핵심 원리 이해)
- **our 프로젝트 적합도**: 매우 높 (동일 아키텍처 철학)
