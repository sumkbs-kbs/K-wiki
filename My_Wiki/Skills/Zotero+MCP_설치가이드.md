---
title: "Zotero + Zotero MCP 서버 설치 가이드"
type: skill
tags: [zotero, zotero-mcp, mcp-server, 설치가이드, 연구자료관리, pk-workflow]
date: 2026-05-25
source: "https://github.com/54yyyu/zotero-mcp"
related: [[Zotero]], [[LLM Wiki]], [[https://www.notion.so/notebooklm-py]]
summary: "Zotero 데스크톱 + Zotero MCP 서버 설치·설정 및 Hermes Agent 연동 가이드"
---

# 📖 Zotero + Zotero MCP 서버 설치 가이드

## 📋 개요

**Zotero**: 개인 연구library 관리 도구 (무료, 오픈소스)  
**Zotero MCP**: Zotero를 AI 도구(Claude, ChatGPT, Hermes 등)에 연결하는 MCP 서버 (免费版, MIT 라이선스)

**총 비용: 월 $0** (Zotero Pro 선택시 $3.33/월)

---

## Step 1: Zotero 데스크톱 설치

### macOS

1. 다운로드: https://www.zotero.org/download/client/dl?channel=release&platform=mac
2. DMG 마운트 → Applications 폴더에 Zotero.app 드래그
3. 첫 실행 시 Zotero 계정 생성 (무료 계정으로 충분, 30GB 저장소)

### Ubuntu/Debian

```bash
wget https://www.zotero.org/download/client/dl?channel=release&platform=linux-x86_64 -O zotero.tar.xz
tar -xf zotero.tar.xz -C /opt/
ln -s /opt/Zotero/zotero /usr/local/bin/zotero
```

## Step 2: Zotero MCP 서버 설치

### 설치 (Python 3.10+, Zotero 7+ 필요)

```bash
# 기본 설치 (핵심 기능のみ - 무료)
pip install zotero-mcp-server

# Semantic search 포함 (로컬 모델 사용 - 무료)
pip install "zotero-mcp-server[semantic]"

# 전체 기능 (PDF 추출, Scite 연결 등)
pip install "zotero-mcp-server[pdf,scite]"

# 완전 설치
pip install "zotero-mcp-server[all]"
```

### 설정

```bash
# 자동 설정 (Claude Desktop 자동 연동)
zotero-mcp setup

# 수동 설정
zotero-mcp setup --manual

# 설정 파일 생성
zotero-mcp init

# Semantic search DB 초기화
zotero-mcp update-db
```

### 설정 파일 위치

```json
// ~/.zotero-mcp/config.yaml (또는 설정 파일 위치 확인)
{
  "zotero_user_id": "xxxxxxxx",  // Zotero 계정에서 확인
  "library_type": "group",        // 개인("user") 또는 그룹("group")
  "library_id": "000000",         // 개인 library는 기본값 사용
  "sync_interval": 3600,
  "embedding_model": "all-MiniLM-L6-v2",  // 무료 로컬 모델
  "proxy": ""
}
```

## Step 3: Hermes Agent 연동

### Hermes config.yaml 수정

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  zotero:
    command: "zotero-mcp"
    transport: "stdio"
```

### Claude Code 연동

```bash
# Claude Desktop 에 자동 연동됨
# 또는 수동 추가:
claude mcp add --transport stdio 54yyyu-zotero-mcp uvx zotero-mcp
```

### CLI 직접 사용

```bash
# 라이브러리 검색
zotero-cli s "keyword"

# 컬렉션 목록 조회
zotero-cli coll

# 태그 조회
zotero-cli tags

# 아이템 정보 조회
zotero-cli g "item-key"

# PDF 주석 추출
zotero-cli ann "item-key"
```

## Step 4: 실제 활용 시나리오

### 4.1: 문서 수집 자동화

```bash
# 웹페이지 저장
zotero-cli add-url https://example.com

# DOI 기반 논문 저장
zotero-cli add-doi 10.1234/abc123

# 파일 저장
zotero-cli add-file /path/to/paper.pdf
```

### 4.2: Wiki 연동 (Zotero → Wiki Topics/)

```python
# 예시: Zotero → Wiki 자동 ingest 스크립트
import subprocess
import json

# Zotero에서 논문 목록 가져오기
result = subprocess.run(
    ["zotero-cli", "coll", "AI-Research"],
    capture_output=True, text=True
)

# Wiki Topics에 문서로 저장
for item in json.loads(result.stdout):
    # 문서 생성 로직
    pass
```

### 4.3: AI 기반 문헌 분석

```bash
# Zotero 컬렉션 기반 문헌 리뷰
zotero-cli coll "AI-Research" | xargs zotero-cli ann

# Scite 인용 분석
zotero-cli scite "item-key"
```

## Step 5: Zotero Connector 설치 (브라우저 확장)

1. https://www.zotero.org/download/connectors
2. Chrome/Edge/Safari 확장 프로그램에서 Zotero Connector 추가
3. 웹페이지 클릭 한 번으로 Zotero에 저장

## Step 6: 추가 구성

### Semantic search 모델 선택

| 모델 | 비용 | 필요 API 키 | 설명 |
|------|------|---------|------|
| all-MiniLM-L6-v2 | 무료 | ❌ | 기본 로컬 모델을 권장 |
| OpenAI | API 사용량 | ✅ | quality up |
| Gemini | API 사용량 | ✅ | quality up |

### Zotero 계정 업그레이드

| 플랜 | 비용 | 저장공간 |
|------|------|----------|
| Basic (무료) | $0 | 30GB |
| Plus | $3.33/월 | 50GB |
| Pro | $5/월 | 1TB+ |

## Troubleshooting

### 문제: Zotero가 열리지 않음
해결: Java 설치 확인 (`java -version`), Zotero 재설치

### 문제: MCP 서버가 연결 안됨
해결: Zotero 데스크톱 실행 중인지 확인 → `zotero-mcp status`

### 문제: Semantic search 에러
해결: `zotero-mcp update-db` 재실행 → embedding 모델 초기화

## 관련 리소스

- Zotero 공식: https://www.zotero.org/
- Zotero MCP GitHub: https://github.com/54yyyu/zotero-mcp
- Zotero Connector: https://www.zotero.org/download/connectors
- Zotero 문서: https://www.zotero.org/support/

---

*작성: 2026-05-25 | 비용: 100% 무료*
