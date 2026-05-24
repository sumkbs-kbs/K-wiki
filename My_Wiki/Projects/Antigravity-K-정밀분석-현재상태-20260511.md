---
id: proj_antigravity_k_analysis_20260511
title: Antigravity-K 정밀 분석 — 현재 상태 보고서
type: project_analysis
tags: [antigravity-k, analysis, codebase, architecture, assessment, 2026-05]
source: code-inspection
date: 2026-05-11
reviewer: antigravity-k-analysis-agent
status: complete
project_root: /Users/mr.k/program/coding/ssak_comp/antigravity-k
---

# Antigravity-K 정밀 분석 — 현재 상태 보고서

**분석 일시**: 2026-05-11  
**분석 대상**: 전체 Python 코드베이스 (src/antigravity_k/)  
**분석 방법**: 정적 분석, 구조 파싱, 스텁 검출, 테스트 카운팅, 보안 감사

---

## 1. 코드베이스 개요 (정량 분석)

```
총 Python 파일     : 220개
총 LOC (lines)     : 58,689줄
Test 파일 수       : 57개
Test 총 LOC        : 8,302줄 (코드베이스 대비 14.1%)
```

### 디렉토리별 분포

| 디렉토리    | 파일 수 | LOC     | 클래스 수 |
|-------------|---------|---------|-----------|
| engine/     | 133     | 37,884  | 317       |
| tools/      | 41      | 11,088  | 95        |
| agents/     | 14      | 2,727   | 15        |
| api/routes/ | 12      | 3,691   | —         |
| api/ (기타) | 3       | —       | 32        |
| knowledge/  | 5       | 1,236   | 6         |
| security/   | 3       | 318     | 2         |
| finetune/   | 2       | 542     | 4         |
| integrations/| 2      | 142     | 2         |

### 파일 크기 TOP 10

| 파일                          | LOC   |
|-------------------------------|-------|
| api/routes/legacy.py          | 1,431 |
| engine/slash_commands.py      | 1,230 |
| engine/model_manager.py       | 1,137 |
| engine/harness.py             | 1,070 |
| tools/web_search.py           | 952   |
| engine/goal_runner.py         | 834   |
| engine/external_brain.py      | 710   |
| api/routes/chat.py            | 685   |
| engine/rag_indexer.py         | 679   |
| engine/quality_gate.py        | 669   |

### 키워드 분석

| 패턴          | 발생 횟수 | 비고              |
|---------------|-----------|-------------------|
| pass          | 87        | 빈 메소드/블록    |
| return {}     | 17        | 빈 딕셔너리 반환  |
| lambda: None  | 1         | stub              |
| async         | 226       | 비동기 사용       |
| await         | 315       | await 사용        |

### Engine 내 클래스 수 (상위)

engine/ 내에는 약 **317개 클래스**가 정의되어 있으며, 이는 전체 프로젝트 클래스의 약 **50%**를 차지합니다.

---

## 2. 핵심 아키텍처 (현재 동작 흐름)

```
사용자 입력
  │
  ▼
[CEO Analyzer] ─→ 태스크 유형 분류: simple_chat | coding | reasoning | complex
  │
  ▼
[OrchestratorAgent + StateGraph]
  ├── 역할별 모델 매핑 (main_model / code_model / vision_model / embedding_model)
  ├── ToolLoopEngine (ReAct 루프, max 15 step)
  ├── RSI Engine (7단계 자기개선 사이클)
  ├── AutonomousLearner (지식 갭 감지 + 웹 수집 학습)
  ├── CognitiveLoop (사고 · 검증 · 반성)
  ├── QualityGate (출력 품질 평가)
  ├── DecisionAnchor (의사결정 추적)
  ├── SkillAutoLearner (스킬 자동 학습)
  ├── TrajectoryCompressor (경로 압축)
  ├── PlanGuard + HarnessEnforcer
  └── ArtifactEngine (산출물 생성)
  │
  ▼
[Tool Registry] (39개 도구 + MCP 연동 + Declarative Decorator)
  │
  ▼
[VaultEngine] (Git-first + RAG sync)
  │
  ▼
[RSI Engine] → OBSERVE → DIAGNOSE → HYPOTHESIZE → MUTATE → EVALUATE → SELECT → INTEGRATE
  │
  ▼
[LLM Wiki] (SQLite + Markdown 영속화)
```

### 핵심 설계 특징

| 패턴 | 설명 |
|------|------|
| **CEO 기반 다중 모델** | 태스크 유형에 따라 전용 모델을 자동 매핑 (Qwen3-72B / Qwen2.5-Coder-32B / Qwen2-VL-7B / bge-m3) |
| **State Graph 기반 상태 전이** | 레거시 선형 루프 대체 (orchestrator_handlers.py) |
| **Declarative Tool Registry** | `@antigravity_tool` 데코레이터 + RCU (Read-Copy-Update) |
| **RSI 7단계 진화** | Darwin-Godel Machine + ADAS 패턴 기반 |
| **Auto-learn** | 지식 갭 감지 → SearxNG 검색 → Browser 서핑 → LLM 요약 → KI 저장 |
| **Git-first Vault** | 모든 지식 변경은 Git 커밋 → VectorStore RAG 동기화 → LLM Wiki |
| **Computer Use** | 데스크탑 자동화 (HITL 승인 필수, Audit 로그) |

---

## 3. 테스트 현황

| 지표 | 값 |
|------|-----|
| 테스트 파일 | 57개 |
| 테스트 LOC | 8,302줄 |
| 코드:테스트 LOC 비율 | 7.1:1 (14.1% 테스트 포함) |

### 테스트 파일 목록 (57개)

- `test_agent_autograd.py`, `test_agent_program_creation.py`, `test_agent_tools_api.py`
- `test_agentic_tech_radar.py`, `test_ambient_harvester.py`, `test_api_server.py`
- `test_audit_logger.py`, `test_autonomous_capabilities.py`, `test_benchmark_harness.py`
- `test_branch_context.py`, `test_browser_surfing_agent.py`, `test_ceo_analyzer_optimized.py`
- `test_compaction_and_mcp.py`, `test_computer_use.py`, `test_context_engineering.py`
- `test_context_pack.py`, `test_context_tree.py`, `test_e2e_parity_simulation.py`
- `test_embeddings.py`, `test_goal_runner.py`, `test_google_skills_pattern.py`
- `test_harness_config.py`, `test_harness_engineering.py`, `test_harness_routing_regression.py`
- `test_integration_rag_cov.py`, `test_integration_upgrade.py`, `test_lintai_scanner.py`
- `test_mcp_capability.py`, `test_mcp_client.py`, `test_media_gen.py`
- `test_meta_evolution_agent.py`, `test_model_manager_generate.py`, `test_model_router.py`
- `test_multi_agent.py`, `test_output_quality.py`, `test_performance_paradigms.py`
- `test_planning_and_rendering_quality.py`, `test_protocol_translator.py`, `test_rag.py`
- `test_rtk_compressor.py`, `test_self_capability.py`, `test_server_stream.py`
- `test_skills_registry.py`, `test_stream_processor.py`, `test_tiptap_patterns.py`
- `test_tool_call_parser.py`, `test_upgrade_phases.py`, `test_upgrade_phases_randomized.py`
- `test_upgrade_v6_9.py`, `test_usage_tracker.py`, `test_vault.py`, `test_wiki_evolver.py`
- `test_youtube_tool.py`, `test_zx_executor.py`, `test_claw_integration.py`, `conftest.py`

### 테스트 간격 (Gaps)

```
테스트 있음: agent_autograd, branch_context, benchmark_harness, browser_surfing,
            ceo_analyzer, codex_transfer, embeddings, goal_runner, harness,
            linter_scanner, model_manager, model_router, multi_agent,
            skills_registry, state_graph, tool_call_parser, usage_tracker,
            vault, wiki_evolver, youtTube_tool, agent_tools_api,
            audit_logger, integration_rag_cov, integration_upgrade,
            rtk_compressor, self_capability, server_stream, stream_processor

테스트 없음 (중요): orchestrator_core, tool_loop_core,
                    rsi_engine_core, tool_guardrails,
                    autonomous_learner_core,
                    security_gate, secret_scanner,
                    cost_guard, crdt_sync,
                    prompt_evolver, context_compressor,
                    agent_context_vm, mission_manager
```

---

## 4. 코드 완성도 분석

### 4.1 Skeleton Module (주요 stubs)

```
[STUB] engine/tool_loop.py       — 6 pass lines (ReAct 루프 skeleton)
[STUB] engine/tool_guardrails.py — 2 pass lines (보안 판정 skeleton)
[STUB] engine/hook_event_bus.py  — 2 pass lines (이벤트 bus skeleton)
[STUB] engine/curriculum_generator.py — 2 pass lines
[STUB] engine/model_manager.py   — 2 pass lines
[STUB] engine/agent_autograd.py  — lambda: None stub
[STUB] tools/impact_analyzer.py  — pass exception handler
[STUB] tools/self_evolution_tool.py — 2 pass + 17 return {}
[STUB] tools/mcp_tool_loader.py  — 2 return {} stubs
```

### 4.2 중복 검출

| 중복 유형 | 파일 1 | 파일 2 | 상태 |
|-----------|--------|--------|------|
| 브라우저 자동화 | tools/browser_subagent_tool.py (147 LOC) | tools/browser_tool.py (469 LOC) | **중복** |
| 브라우저 자동화 | tools/browser_tool.py (469 LOC) | tools/browser_tools.py (220 LOC) | **중복** |
| 스킬 학습 | engine/skill_auto_learner.py (ToolCall, LearnedPattern, SkillRecord, SkillAutoLearner) | tools/self_evolution_tool.py (SelfEvolutionTool, SelfRewardEvaluator, MetacognitiveTracker) | **부분 중복** — 패턴 탐지 vs 코드베이스 진화 |

### 4.3 Security Issue

```
[CRITICAL] engine/tool_guardrails.py → default allows_execution = True
  → 모든 도구가 기본적으로 승인됨. 보안 의미 없음.
  → fix: default False, whitelist based approach

[MODERATE] engine/vault.py → restore_snapshot()
  → real_path in dangerous_paths (정확 매칭만)
  → fix: any(real_path.startswith(d) for d in dangerous_paths)
```

### 4.4 asyncio Issue

```
[WARNING] tools/self_test.py:89 → report_dict = asyncio.run(self._run_async(scope))
           tools/mcp_tool_loader.py:118 → 동기 컨텍스트에서 asyncio.run()
           tools/web_search.py:951 → asyncio.run(main())
           integrations/slack_bot.py:57 → asyncio.run(self.run_async())
  → 메인 이벤트 루프 내에서 asyncio.run() 호출 시 RuntimeError 발생 가능
```

---

## 5. Dashboard UI

```
path: dashboard/
index.html (9,541 bytes)
src/ (Vite React UI)
package.json (Vite + React)
dist/ (빌드된 파일)
  - 2/2/1301/1  UI 컴포넌트
  - 0/0/0  0
node_modules/
package-lock.json (34,288 bytes)
vite.config.js
```

---

## 6. Config 시스템

| 섹션 | 클래스 | env_prefix | 주요 설정 |
|------|--------|------------|-----------|
| 모델 | ModelConfig | AGK_MODEL_ | main_model, code_model, embedding_model, vision_model, api_engine |
| 서버 | ServerConfig | AGK_SERVER_ | host, port, inference_port |
| 경로 | PathConfig | AGK_PATH_ |.project_root, models_dir, data_dir, wiki_dir, logs_dir |
| 보안 | SecurityConfig | AGK_SEC_ | sandbox, max_execution_time, max_tool_risk, lintai_strict, access_pin |
| 워크플로 | WorkflowConfig | AGK_WORKFLOW_ | autopilot, auto_commit, auto_artifacts |
| i18n | I18nConfig | AGK_I18N_ | locale, fallback_locale |
| 라우터 | RouterConfig | AGK_ROUTER_ | default_strategy, cooldown_base_sec, max_cooldown_sec |
| PC | PCConfig | AGK_PC_ | enabled, hitl_required, force_stub |

---

## 7. 완성도 평가 (최종 점수)

| 항목 | 점수 (10점 만점) | 비고 |
|------|-------------------|------|
| 아키텍처 설계 | 9/10 | CEO 기반 다중 에이전트, RSI, RAG 설계 완성도 높음 |
| 구현 완성도 | 5.5/10 | Skeleton module 다수, pass/empty return 많음 |
| 테스트 커버리지 | 6/10 | 57개 테스트 존재하나 핵심 module 테스트 누락 (orchestrator, tool_loop, guardrails) |
| 보안 | 4/10 | Guardrail 기본 허용, Git reset 안전성, tool risk分级 부족 |
| 유지보수성 | 6/10 | 중복 브라우저 tool, Config consistency 문제 |
| **전체 평가** | **6/10** | **거대한 설계와 파이프라인은 완성되나, 구현 완성도와 검증 부족** |

---

## 8. 개선 로드맵

### 1순위 (즉시)
- [ ] Guardrail defaults → Default Deny
- [ ] Git reset security fix (startswith 체크)
- [ ] orchestrator, tool_loop, guardrails 단위 테스트 추가
- [ ] browser_subagent_tool + browser_tool 통합

### 2순위 (1-2주)
- [ ] `asyncio.run()` nested call fix
- [ ] Skeleton modules 구현 완료 또는 제거
- [ ] Config env 변수명 일관성 체크 (config.py vs engine_context.py)
- [ ] AgentArchive 영속화 (SQLite/File)

### 3순위 (1-2개월)
- [ ] OrchestratorAgent → EngineContext 중심 리팩토링
- [ ] RSI benchmark 지표 명확화
- [ ] full test suite (70% coverage 목표)
- [ ] skill_auto_learner + self_evolution 통합
- [ ] config 예외 처리 강화 (silent 무시 제거)

---

*분석 완료. 자동 학습된 상태 저장.*

`analysis_timestamp: '2026-05-11T09:00:00+09:00'`
`analysis_type: codebase-inspection`
`confidence: high`
`analyzer: agent-analysis-pipeline-v2`
