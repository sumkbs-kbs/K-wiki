---
id: be46dc1a
category: "[[Projects/index]]"
confidence_score: 0.5
tags: [projects, 배포, 운영, devops, scp]
last_reinforced: 2026-04-15
github_commit: "pending"
---

# [[Projects/Plantler 배포 워크플로우 — SCP 직접 전송 방식.md]]

## 📌 한 줄 통찰 (The Karpathy Summary)
> 리포지토리 크기가 **24GB 이상** (`.venv`, 로컬 캐시, AI 모델 포함). Git push로는 사실상 배포 불가능.

## 📖 구조화된 지식 (Synthesized Content)
- **추출된 패턴:**
  - **절대 원격 .env를 로컬 .env로 덮어쓰지 말 것** (서버 시크릿 유실 위험)
  - `systemd` 서비스명: `plantler`
  - 서버: `ssak-ai.asia` (Ubuntu)

- **세부 내용:**
  - 리포지토리 크기가 **24GB 이상** (`.venv`, 로컬 캐시, AI 모델 포함). Git push로는 사실상 배포 불가능.
  - 변경된 파일만 골라서 서버에 직접 복사하는 방식 채택.
  - ```bash
  - scp -i plantler-key.pem 변경된파일.py ubuntu@ssak-ai.asia:~/plantler_backend/app/
  - ```
  - ```bash
  - ssh -i plantler-key.pem ubuntu@ssak-ai.asia "cd ~/plantler_backend && source venv/bin/activate && pip install -r [[requirements.txt]]"
  - ```

## ⚠️ 모순 및 업데이트 (Contradictions & RL Update)
- **과거 데이터와의 충돌:** 현재까지 발견된 모순 없음.
- **정책 변화:** 이 문서를 통해 분류 정책에 변화 없음.

## 🔗 지식 연결 (Graph)
- **Parent:** [[Projects/index]]
- **Related:** [[Decisions/Plantler v2.0 프로젝트 회고.md]], [[Decisions/Plantler 아키텍처 의사결정 기록.md]], [[Decisions/Plantler 프로젝트 개요 — 식물 관리 AI 앱.md]]
- **Raw Source:** Projects/Plantler 배포 워크플로우 — SCP 직접 전송 방식
