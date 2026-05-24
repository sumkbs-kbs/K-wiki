---
type: Chat_Log
topic: Wiki_Tree_Architecture
participants: Byeong-seok, Gemini/AI
date: 2026-05-14
status: Refined
tags: [macOS, M5_Max, Local_LLM, DeepSeek_V4, vLLM, SGLang, Obsidian_RAG, Multimodal, 128GB_RAM]
---

# M5 Max 128GB 기반 로컬 LLM Wiki 구축 및 전략 (DeepSeek-V4 & Multimodal)

## 요약
맥북 프로 M5 Max (128GB RAM, 4TB SSD) 사양의 한계와 활용 전략에 대한 분석. 대역폭과 양자화에 의한 감성 차이를 극복하고, [[DeepSeek-V4-Flash]]를 중심으로 [[vLLM]] 및 [[SGLang]]과 같은 최첨단 추론 엔진을 활용하는 방법을 정리. Obsidian 기반의 사적 LLM Wiki(RAG)와 사진/오디오/유튜브를 아우르는 멀티모달 워크플로우를 결합한 '제2의 뇌' 구축 로드맵을 제시.

## 1. M5 Max 128GB의 진정한 가치와 한계 (현타의 해소)
- **메모리 대역폭의 오해:** M5 Max의 대역폭(H100 대비 낮은 수준)으로 인해 단문 답변 속도는 유료 클라우드 LLM(GPT-4, Claude 등)에 미치지 못할 수 있음. 하지만 128GB 통합 메모리는 '컨텍스트의 길이(Long Context)'와 '동시 다중 작업'에서 압도적 우위.
- **양자화(QoL)와 지능:** 100B 이상 파라미터는 4-bit 압축 불가피. 지능 손실이 존재하므로, 클라우드의 100% 성능을 기대하지 않고 '10GB RAM의 로컬 대안'으로 접근해야 함.
- **최적의 포지셔닝:** 단순히 '챗봇'으로 쓰기보다, 클라우드가 거부하는 '거대한 로컬 맥락(Huge Context)', '민감한 로컬 RAG', '다중 에이전트 동시 구동'에 집중.

## 2. DeepSeek-V4-Flash: 맥북의 중심 엔진
- **MoE 구조:** 총 284B 파라미터 중 활성화되는 파라미터는 13B 수준. 속도(60 tok/s 이상 가능)와 지능의 최적 조합.
- **DSA (Sparse Attention):** KV 캐시 메모리 부담을 기존 대비 90% 절감. 128GB RAM은 이를 여실히 활용 가능.
- **100만 토큰 컨텍스트:** 수백 페이지 문서, 전체 소스 코드 병렬 분석 가능. 
- **활용 전략:** 실시간 응답(SWE-bench 79%)에는 Flash 모델, 복잡한 논리/Deep Reasoning에는 `Think Max` 모드 활용.

## 3. 초고속 로컬 추론 엔진 (Server Tier)
- **vLLM (PagedAttention):** 메모리 효율성 극대화. 여러 에이전트의 동시 요청 병렬 처리에 최적.
    - `python -m vllm.entrypoints.openai.api_server --model deepseek-ai/DeepSeek-V4-Flash --dtype float16`
- **SGLang (RadixAttention):** 동일한 프롬프트(긴 문서)를 반복할 때 캐싱으로 비약적인 속도 향상.
    - `python -m sglang.launch_server --model-path deepseek-ai/DeepSeek-V4-Flash --mem-fraction-static 0.8`
- **M5 Max 환경:** `--mem-fraction-static 0.8` 설정으로 100GB 이상을 모델 및 캐시에 할당. 나머지 여유 RAM으로 Docker 컨테이너 또는 추가 인덱싱 처리.

## 4. Python 및 환경 구축 (128GB 격리)
- **언어 버전:** Python 3.12 계열. 안정성, MLX 최적화, 모든 라이브러리 호환성 정점.
- **패키지 관리:** `uv` (Rust 기반, pip 대비 100배 빠름).
- **격리 전략:**
    - `MLX_env` (Python 3.13): Apple Silicon 직접 접근용.
    - `vLLM_env` (Python 3.12): 복잡한 의존성 처리용.
    - 128GB 덕분에 환경 격리 시에도 병목 없이 쾌적함.

## 5. 회사-개인 데이터 분리 및 LLM Wiki 전략 (RAG)
- **보안 분리 원칙:** 회사 파일 직접 반출 금지. '사고의 틀(Logic)'이나 '추상화된 지식'만 개인 Wiki로 이동.
- **지식 통합:** Obsidian + [[AnythingLLM]] 또는 [[Verba]]. PDF, Markdown, 웹 URL 모두 인덱싱.
- **하이브리드 워크플로우:** 집에서 vLLM 구축 및 테스트(더미 데이터 활용) → 회사에서는 검증된 스크립트 및 프롬포트 적용.

## 6. Obsidian + 로컬 LLM (다중 에이전트 통합)
- **Smart Connections:** 노트 간 관계 자동 분석 및 사이드바 추천 (로컬 임베딩).
- **Copilot / Text Generator:** AI가Obsidian 내에서 코딩, 번역, 요약. (API: `http://localhost:8000/v1`)
- **다중 에이전트:**
    - **Backend:** DeepSeek-V4-Flash (Core Reasoning)
    - **Vision:** Llama-3.2-Vision (90B), Qwen2-VL (72B)
    - **Audio:** Whisper-v3 (Large)

## 7. 멀티모달 LLM Wiki 구축 로드맵 (이미지, 오디오, 유튜브)
| 데이터 유형 | 권장 로컬 모델 | 권장 처리 도구 | Wiki 통합 방법 |
| :--- | :--- | :--- | :--- |
| 사진 / 이미지 | Llama-3.2-Vision / Qwen2-VL | Obsidian Media Extended | VLM 분석 결과 Markdown화 |
| 오디오 / 녹음 | Whisper-v3 | MacWhisper / Whisper.cpp | 텍스트 전사(SRT)하여 Obsidian 링크 |
| 유튜브 / 링크 | DeepSeek-V4-Flash | AnythingLLM / yt-dlp | 스크립트 크롤링하여 1M 컨텍스트 저장 |
| 소스 코드 / RAG | DeepSeek-V4-Flash | vLLM + AnythingLLM | Ssakfile/Plantler 개발 로직 벡터화 |

## 결론 및 실행 방안
128GB RAM의 힘으로 단순한 노트 앱(Obsidian)을 '살아있는 개인 지식 엔진'으로 격상. M5 Max는 단순 랩탑이 아닌 '개인용 초저비용 AI 데이터센터'입니다. 현타는 하드웨어가 아닌 '도구와 생태계의 부족'에서 왔음을 인지하고 DeepSeek-V4와 Obsidian/RAG를 연계하여 사적 지식망(L2 Brain) 구축에 집중.

## 관련 문서
- [[Wiki_Tree_Architecture]]
- [[AntiGraffiti-K]]
- [[Karpathy_LLM_OS]]
- [[Claude_Code_Max]]
- [[Website_Analysis_EZER_AI_Agent_University]]
- [[YouTube_Analysis_Woorkpay0_AI_Company]]
- [[YouTube_Analysis_OpenClaw_5Agents_CodingFree]]
