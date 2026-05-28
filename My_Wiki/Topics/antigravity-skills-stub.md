# Antigravity Skills (Hermes Agent 내장 스킬 매핑)

> **중요**: 이 폴더의 스킬 명칭은 모두 **Hermes Agent의 내장 스킬**(`.hermes/skills/` 또는 시스템 스킬)입니다.
> Wiki에서 `[[skill-name]]`로 참조할 때 실제 Wiki 파일이 아닌, 아래 매핑을 통해 정확한 스킬을 호출하세요.

## 📋 Wiki ↔ Hermes 스킬 매핑 테이블

| Wiki 참조명 (개념) | 실제 Hermes 스킬 | 설명 |
|---|---|---|
| **기획 및 제품 전략** |
| office-hours | `plan` (writing-plans 스킬) | 아이디어 스케치부터 기획 |
| plan-ceo-review | `writing-plans` 스킬 — CEO 관점 | 목표 상향, 스코프 조정 |
| plan-eng-review | `writing-plans` 스킬 — Eng 관점 | 기술 구조, 데이터 흐름 |
| plan-design-review | `design-md` 스킬 | UI/UX 사전 리뷰 |
| autoplan | `writing-plans` 파이프라인 | CEO/Design/Eng 연속 실행 |
| **디자인 및 프론트엔드** |
| design-consultation | `claude-design` 스킬 | 통합 디자인 시스템 제안 |
| design-shotgun | `sketch` 스킬 | 여러 디자인 시안 생성 |
| design-html | `popular-web-designs` 스킬 | 실제 프로덕션 HTML 구현 |
| design-review | `dogfood` 스킬 | 운영 사이트 시각적 스캔 |
| ui-expert-mcp | `native-mcp` 관련 | React/Vue UI 컴포넌트 |
| **개발, 배포 및 리뷰** |
| review | `github-code-review` 스킬 | PR 자동 리뷰 |
| ship | `github-pr-workflow` 스킬 | 테스트 + 버전 + PR |
| setup-deploy | `web` 관련 스킬 | 배포 세팅 자동 구성 |
| land-and-deploy | `github-pr-workflow` | 병합 + CI + 배포 |
| document-release | `github-repo-management` | README/CHANGELOG同步 |
| retro | `github-list_commits` | Git 커밋 분석 |
| **시스템 보호 및 보안** |
| cso | `github-code-review` 보안 부분 | 시크릿/의존성/LLM 보안 |
| careful | `terminal` + `browser` 경보 | 위험 명령어 경보 |
| freeze | `file` 관련 격리 | 디렉토리 수정 제한 |
| unfreeze | `file` 관련 해제 | 세션 내 Freeze 해제 |
| guard | careful + freeze 결합 | 완전 보안 모드 |
| **품질 보증 및 디버깅** |
| investigate | `systematic-debugging` 스킬 | 4단계 체계적 디버깅 |
| qa | `dogfood` 스킬 | 브라우저 통합 테스트 |
| qa-only | `dogfood` 스킬 — 리포트 전용 | 스크린샷만 생성 |
| benchmark | browser 성능 측정 | 렌더링 속도 추적 |
| canary | process + terminal | 라이브 서버 모니터링 |
| **브라우저 및 자동화** |
| gstack / browse | `browser` 스택 (browser_navigate/snapshot/click) | 헤드리스 브라우저 상호작용 |
| connect-chrome | browser_vision + screenshot | 사용자 화면 실시간 관전 |
| setup-browser-cookies | browser + cookies | 쿠키 이관 |
| **에이전트 지능 및 진화** |
| learn | `session_search` / `skill_manage` | 세션간 패턴 기억 |
| gbrain | `memory` + `wiki-storage` | 영구 기억 시스템 |
| evolver | `skill_manage` + `memory` | 에이전트 자가발전 |
| awesome-agent-evolution | `hermes-agent` 스킬 | AI 진화 기술 논문 |
| hermes-for-web | `web` + `browser` 풀스택 | 커스텀 UI 및 통신 |
| **핵심 연동 플러그인** |
| nanobanana-pro-obsidian | `obsidian` 스킬 | 옵시디언 플러그인 유지보수 |
| obsidian-code | `obsidian` + `terminal` | Obsidian Code 플러그인 |
| nlwflow-research | `notebooklm` 관련 스킬 | NotebookLM → Obsidian 파이프라인 |
| claude-code-source-code-full | `claude-code` 스킬 | 분석가 소스 분석 |
| **특화 도메인 스킬** |
| `[[Plantler_Skills_MOC]]` | [03_Plantler_Skills_MOC.md](03_Plantler_Skills_MOC.md) | Plantler 관련 스킬 |

---

## 🔗 관련 Wiki 문서

- [01_Antigravity_Skills_Universe_MOC.md (원본 MOC)](01_Antigravity_Skills_Universe_MOC.md)
- [Antigravity-K 현재상태](../Projects/Antigravity-K-정밀분석-현재상태-20260511.md)
- [M5Max Local LLM Strategy](../Projects/M5Max_Local_LLM_Strategy_and_Wiki.md)
- [Wiki Tree Architecture](Wiki_Tree_Architecture.md)

---

## 💡 사용 가이드

### Wiki에서 스킬 호출하는 방법

이 문서의 각 스킬명은 **개념 참조명**입니다. 실제 호출은 agent가 `skill_view(name='실제-스킬명')`로 실행합니다.

예: `office-hours` 개념을 실제 호출하려면 `skill_view(name='writing-plans')`

### broken links 처리 결과

- **38개 broken links** 모두 위 매핑 테이블로 정리 완료
- 각 링크는 이제 Wiki에서 실제 파일 대신 **개념 설명서**로 연결
- Wiki 내에서 `antigravity-skills-stub` 폴더를 별도로 만들지 않고, 이 단일 문서에서 모두 관리

---

> 이 문서는 Hermes Agent의 내장 스킬 명칭과 Wiki의 [[링크]] 사이의 간극을 메우는 교량입니다.
> 실제 스킬은 `.hermes/skills/` 또는 내장 스킬 시스템에 정의되어 있습니다.
