# Tinker-NemoGym 개요 및 시작하기

## 개요
**tinker-nemogym**은 NVIDIA의 **NeMo-Gym** 환경과 Thinking Machines의 **Tinker**(관리형 GPU 및 LoRA 훈련 플랫폼)를 이어주는 브릿지 역할을 하는 강화학습(RL) 트레이너입니다. 이 저장소는 실시간 핫스왑, GRPO 어드밴티지 정규화, 그리고 높은 수준의 진단 기능(Precision-gap)을 제공하여 효율적인 RL 파이프라인을 구축할 수 있게 해줍니다.

## 주요 개념
- **NeMo-Gym 연동**: 에이전트와 보상 모델(Resources Server)이 상호작용.
- **Tinker 클라이언트**: 훈련 도중 핫스왑 되는 샘플링 클라이언트를 통해 다운타임 없이 가중치 업데이트 반영.
- **FastAPI Shim**: 훈련 루프 내에 내장된 웹 서버가 모델인 척 위장(`SimpleResponsesAPIModel`)하여 트래픽을 가로채고 제어함.

## 빠른 시작 (Quickstart)

### 1. 설치 (설정 환경 준비)
이 프로젝트는 Python 3.12 환경과 의존성 관리 도구인 `poetry`를 사용합니다.

```bash
cd tinker-nemogym
poetry install
```

### 2. Tinker API 키 설정
실제 Tinker GPU 자원을 활용하여 훈련하기 위해서는 인증 키가 필요합니다.
```bash
export TINKER_API_KEY=tml-...
```

### 3. 테스트 스모크(Smoke) 실행
모든 구성요소가 정상 작동하는지 E2E 라이브 테스트를 실행해 봅니다.
```bash
bash scripts/smoke_json_format.sh
```

또는 파이썬 코드로 직접 실행할 수도 있습니다.
```python
import tinker_nemogym as tng
summary = tng.train("configs/smoke_mcqa.yaml")
```

## 참고사항
* 오프라인 더미 테스트 환경은 없으며, 모든 `smoke_*.sh` 스크립트는 **실제 Tinker GPU** 환경에 요청을 보냅니다.
* `nemo-gym` 레포지토리가 `../nemo-gym` (상위 디렉토리)에 병렬로 클론되어 있어야 하며, 독립된 `.venv`가 설정되어 있어야 스크립트 실행이 가능합니다.
