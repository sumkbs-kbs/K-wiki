---
title: "Marine Electrical Rulebook (선박 전기 설계 마스터 룩북)"
description: "중요 선박(FLNG, COT, LNG) 전기 설계에 필요한 IEC, SOLAS, Class Rules의 종합 지침서. Senior Engineer 및 Line Leader를 위한 설계 체크리스트 포함."
tags:
  - MarineElectrical
  - IEC60092
  - SOLAS
  - ClassRules
  - ABS
  - DNV
  - KR
  - LR
  - BV
  - FLNG
  - LNG
  - COT
  - SHI
date: 2026-05-11
author: "Samsung R&D / Senior Engineer"
category: "Marine_Engineering"
---

# 🚢 Marine Electrical Design Rulebook (선박 전기 설계 마스터 룩북)

시니어 엔지니어 및 라인 리더를 위한 **선박 전기 설계 종합 마스터 가이드**입니다. 본 문서는 IEC 60092 시리즈, SOLAS 규정, 주요 선급 규칙(ABS, DNV, KR, LR, BV) 및 FLNG/LNG/COT 등 특수 선종의 고유 전기 설계 기준을 통합하여 관리합니다.

## 1. 핵심 설계 가이드라인 (Checklist for Line Leader)
*   **절연 감시 (Ground Fault Monitoring)**: 선박 부식 환경의 장기 운항 시, 절연 저항(IR, min $1\Omega \cdot kV$) 유지 및 접지 시스템(IT System)의 신뢰성 검증 필수.
*   **단락 용량 (Short Circuit Capacity)**: $440V$/ $6.6kV$ 시스템에서 MCC, PCB의 breaking capacity ($85kA$~ $100kA$급) 적합성 검토.
*   **위험 구역 (Hazardous Areas)**: $FLNG$ 및 $LNG/COT$의 Deck, Cargo Area는 **IEC 60092-601** (Zone 1/2)에 따라 $Ex d / Ex e / Ex i$ 등급의 적합성을 철저히 검증해야 함.
*   **화재 안전 (Fire Integrity)**: $FLNG$ 구조물 특성상 $F60$ 또는 $F30$ 등급의 방화 케이블 라우팅 및 덕트 격리 (Bulkhead Penetration Sealing).

---

## 2. 핵심 지식 구조 (Knowledge Tree)
`wiki/My_Wiki/Topics/MarineElectrical/` 폴더 아래 다음 문서들이 상세 매핑되어 있습니다:
1. **[IEC 60092 Standards]**: 조선 전기 설비를 다루는 핵심 국제 표준의 상세 해설 (케이블, 배전, 절연, 위험구역).
2. **[SOLAS Compliance]**: $SOLAS$ Chap II-1에서의 전기 안전 요구사항 (비상 발전기, 분전 시스템 등).
3. **[Class Rules & Special Ships]**: 각급(KR, DNV, LR, ABS, BV)의 설계 차이점 및 FLNG/LNG/COT의 특수 요구사항 (Deck Power, IG System 등).
