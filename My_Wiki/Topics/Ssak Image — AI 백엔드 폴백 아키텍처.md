---
id: 251c5206
category: "[[Topics/index]]"
confidence_score: 1.0
tags: [topics, ai백엔드, openvino, onnx, pytorch, 폴백시스템]
last_reinforced: 2026-04-15
github_commit: "pending"
---

# Ssak Image — AI 백엔드 폴백 아키텍처

## 📌 한 줄 통찰 (The Karpathy Summary)
> - 어떤 PC에는 OpenVINO가 있고, 어떤 PC에는 ONNX Runtime만 있다

## 📖 구조화된 지식 (Synthesized Content)
- **추출된 패턴:**
  - 어떤 PC에는 OpenVINO가 있고, 어떤 PC에는 ONNX Runtime만 있다
  - GPU가 있는 PC도, 없는 PC도 있다
  - PyInstaller로 패키징하면 DLL 로딩이 또 다르게 동작한다

- **세부 내용:**
  - ```python
  - class OpenVINOEmbedder:
  - def __init__(self, onnx_path):
  - core = ov.Core()
  - model = core.read_model(onnx_path)
  - try:
  - self.compiled = core.compile_model(model, "GPU")
  - except:

## ⚠️ 모순 및 업데이트 (Contradictions & RL Update)
- **과거 데이터와의 충돌:** 현재까지 발견된 모순 없음.
- **정책 변화:** 이 문서를 통해 분류 정책에 변화 없음.

## 🔗 지식 연결 (Graph)
- **Parent:** [[Topics/index]]
- **Related:** [[Projects/Ssak Image — AI 중복 이미지 탐지 프로그램.md]], [[Ssak_Reader_AI_의미론적_검색_아키텍처.md]], [[Ssak_Reader_오프라인_모델_배포_전략.md]]
- **Raw Source:** [[00_Raw/19_SsakImage_AI_백엔드_아키텍처.md]]
