---
title: YouTube Analysis - LLM Wiki 외부 지식 업그레이드: Zotero × NotebookLM × Obsidian × Claude Code
tags: [youtube-analysis, external-knowledge, zotero, notebooklm, obsidian, ai-workspace]
date: 2026-05-18
type: topics
source: YouTube - 브레인 트리니티 (32분 32초)
related:
  - [[LLM_Wiki]]
  - [[Zotero]]
  - [[NotebookLM]]
  - [[personal-wiki]]
  - [[https://www.notion.so/notebooklm-py]]
  - [[zotero-mcp]]
---

# YouTube 분석: LLM Wiki 외부 지식 업그레이드

## 요약

LLM Wiki를 **외부 지식 원천 2가지**로 증강하는 방법:
- **Zotero**: 원본 소스 관리 (논문, PDF, 동영상, 웹페이지)
- **NotebookLM**: 심화 분석 & 아웃풋 생성기 (Q&A, PPT, 인포그래픽)
- **Claude Code + MCP**: Zotero + NotebookLM 자동화 통합
- **3층 아키텍처**: Zotero(원본) → LLM Wiki(정제) → NotebookLM(심화/아웃풋)

## 핵심 인사이트

- LLM Wiki만으로는 원본 소스가 끊기면 추적 불가, 컨텍스트 윈도우 한계
- Zotero Connector 원클릭 저장 (메타데이터 자동 추출)
- `인제스트 시 왜 이 자료를 모았는지` 목적 설명이 소화 품질을 결정
- NotebookLM-Py로 Claude 토큰 절약 (Gemini 연산 → Claude 토큰 절약)

## 주요 개념

- Zotero: "나만의 도서관" - 원본 원문 수집
- LLM Wiki: 1차 정제车间 - 마크다운 카드 형태
- NotebookLM: 심화 분석 - PPT, 인포그래픽, 팟캐스트 생성
- Claude Code MCP: 통합 자동화

## 파이프라인

```
Browser → Zotero Desktop (원본 수집)
   ↓ Zotero MCP Server
LLM Wiki (마크다운 카드 정제)
   ↓ NotebookLM-py
인포그래픽/PPT/아웃풋
   ↓ Obsidian Output 자동 저장
```

## 설치 완료 현황

| 항목 | 상태 |
|------|------|
| Zotero Desktop | ⚡ 미설치 (설치 필요) |
| Zotero Connector | ⚡ 미설치 (설치 필요) |
| Zotero MCP | ⚡ 미설치 (설치 필요) |
| NotebookLM-py | ✅ 설치됨 |