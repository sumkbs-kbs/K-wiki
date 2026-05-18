# RAW 폴더 — 원본 보관소 (Raw Content Repository)

## 📌 핵심 원칙: "원본은 원본 그대로"

이 폴더에 AI가 들어갈 때 반드시 먼저 읽고 준수해야 하는 규칙입니다.

## 🚫 절대 규칙

1. **원본 내용 절대 수정 금지** — 캡처된 HTML, JSON, 마크다운, 텍스트를任何形式的으로 변경하지 않음
2. **요약/재구성 금지** — 이 폴더는 보관만 하고, 분석은 DOCS(인제스트된 문서)에서만 진행
3. **파일 구조 변경 금지** — 원본 파일의 폴더 구조를 임의로 변경하지 않음
4. **Front Matter 추가 금지** — 원본 파일에 메타데이터를 추가하지 않음

## ✅ permitted 작업

- 파일 추가 (새 원본 captured 데이터)
- 파일 삭제 (중복/깨진 원본만)
- 파일명 변경 (파일명 규칙 준수 시)

## 📁 저장 대상

| 유형 | 예시 |
|-----|------|
| HTML captured | `*-html.md`, `*-html.json` |
| JSON captured | `*.json`, `*.jsonl` |
| Video transcripts | `*-transcript.md` |
| Screenshots | `*.png`, `*.jpg` (해당 파일명) |
| Raw exports | Google Takeout, Drive exports |

## 📝 File Name Convention (원본 기준)

```
[sourcename]-[date]-[type].[ext]
예: google-drive-20260518-html.md
```

## 🔄 Workflow

```
[원본 captured] → raw/ (이 폴더)
                ↓
           DOCS (My_Wiki/ — 정리된 문서)
                ↓
           index.md (리셉션 데스크 — 전체 인덱스)
```

> **AI 에이전트 메모**: 여기에 들어오는 모든 데이터는 "입력 데이터"일 뿐 "결과물"이 아님. 
> 결과물은 항상 DOCS 폴더에 생성.

#claude-md #raw-folder
