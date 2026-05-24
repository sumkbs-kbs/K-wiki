---
title: "SOLAS Chapter II-1: Electrical Installations (선박 전기 안전 규정)"
description: "SOLAS 조 II-1의 주요 전기 설계 요구사항: 비상 전원, 부전원 시스템, 화재 안전성, 절연 모니터링 등."
tags:
  - SOLAS
  - Safety
  - EmergencyPower
  - FireIntegrity
category: "Marine_Engineering"
date: "2026-05-11"
parent: "wiki/My_Wiki/Topics/MarineElectrical"
---

# SOLAS Chapter II-1: 전기 설비 요구사항 (상세 매핑)

`SOLAS` 제II장(IIM-1)은 선박의 전기 시스템이 안전 운항을 위해 만족해야 할 핵심 기준입니다. 시니어 엔지니어 및 라인 리더에게 요구되는 핵심 항목은 다음과 같습니다.

## 1. 긴급 전원 공급 (Emergency Source of Power)
*   **SOLAS II-1/42~46 조**: 긴급 상황(주 발전기 정지 시)에서 안전에 필수적인 부하(비상 조명, 통신, 화재 경보기, 펌프 등)에 전원을 공급해야 함.
*   **시간 기준**: 일반 선박은 36시간, LNG/COT 등 위험물 선박은 36시간 이상.
*   **부하 요구량 (Load Demand)**: $P_{emergency} \ge P_{life\_support} + P_{fire\_pump} + P_{comms} + P_{lighting}$.
*   **자동 시작 요구사항**: 주 전원의 정전(Blackout) 시 45초 이내 자동 기동 및 450V까지 전압 회복.

## 2. 부전원 시스템 (Division of Switchboards)
*   **고전압/저전압 분리**: 주 발전기 출력이 $6.6kV$일 경우, 발전기실과 분리된 제2주전원반(Main Switchboard) 설치 요구.
*   **복구성(Reconstitution)**: $6.6kV$ 발전기의 자동 재시동 로직을 통한 부하의 순차적 복구(Phase Sequencing).
*   **연결선 절연**: 주전원반과 제2전원반 간 배선은 $F60$급 방화덕트(Fire Duct)로 격리.

## 3. 화재 안전성 (Fire Integrity)
*   **케이블의 비연연성(Non-Flame Propagation)**: $IBC$ Code 및 $IGC$ Code에 따라 LNG/COT Cargo Area는 $IEC 60332-3C$ (Single vertical trunked cable fire propagation) 테스트 기준 준수.
*   **방화 격리 (Zonal Separation)**: 선박 선미(Aft) 및 선미(Mid)에 분전 시스템(Zoning)을 적용하여, 화물 구역에서의 화재로 인해 기선(Forward) 구역의 전력 공급도 마비되는 것 방지.
*   **덕트 격리**: $F60$ 격리벽을 가로지를 경우, 인화성 가스가 통과하지 못하도록 시일링(Sealing) 수행.

## 4. 절연 및 접지 (Insulation & Grounding)
*   **부식 환경 고려**: 해수 환경에서 부식으로 인한 절연 저항 저하 방지. $IR$ monitor는 $6.6kV$ 이상 시스템에 필수.
*   **접지 방식**: 선박 부식 방지를 위해 $IT$ System(저저항 접지, Low resistance grounded) 또는 $I$ System(분리 권선, Insulated Neutral) 권장. (DNV, KR Class의 경우 $IT$ System 강력 추천).

---

| 항목 | 일반 LNG선 (174k $m^3$ 기준) | FLNG (생산 설비 탑재 기준) |
|--- | --- | --- |
| **주전압 (Main Voltage)** | $440V$ (Low Voltage), $6.6kV$ (HV: 주펌프 전용) | $6.6kV / 11kV$ (생산 설비 모터 구동용) |
| **위험구역 (Hazardous Zone)** | Cargo Deck (Zone 1/2) | FLNG Deck (Zone 1/2/3: 고압 아크 발생 가능) |
| **특수 요구사항** | 인화성 가스로 인한 폭발 위험 | 화물 실화 및 생산 라인 전압 강하 허용 |
| **비상 발전기** | 디즐 엔진 기반 $440V$ 발전기 | 발전기 2대 또는 가스 터빈 기반 발전 |
