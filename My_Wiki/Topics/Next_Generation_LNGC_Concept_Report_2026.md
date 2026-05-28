# 🚢 신개념 LNG Carrier (Next Generation LNGC) — 컨셉 보고서

> **분류:** 선박 컨셉/타사설계, 차세대 LNGC 핵심기술 트렌드
> **작성일:** 2026-05-26
> **연계 표준:** IEC_60092-201_System_Design, IEC_60092-350_Cables, 선박_Bus_Duct_부스덕트_설계_적용

---

## 📌 Executive Summary

글로벌 해적 환경 규제 (IMO 2030/2050 탄소중립), Methane Slip 제한, 대체연료(Methanol/Ammonia) 전환기, 그리고 AI/전동화 기술의 비약으로 인해 새로운 LNGC는 단순한 "가스 운반선"을 넘어 **에너지 허브 **(Energy Hub)로 진화하고 있습니다.

본 보고서는 2025~2026년 기준, 차세대 LNGC 컨셉에 영향을 미치는 **6대 핵심 기술 동향** (SMR, OCCS, WAPS, 전동화/하이브리드, 다연료 대응, 최적 hull form)을 분석하여, 향후 타사설계 Concept Report 작성 시 반영해야 할 사항들을 정리합니다.

---

## 1. ⚛️ SMR (Small Modular Reactor) — 꿈의 원전 추진선

### 1.1 배경 및 현황
- **원자력 재조명**: IMO의 탄소중립 목표에 도달하기 위한 가장 확실한 제로탄소 대안으로 부각.
- **모든 Stakeholder 참여**: 2025년 기준 ABB Marine, Mitsubishi, DNV 등이 상용화 로드맵을 발표하며 막대한 자금을 투입 중.
- **핵심 기술**: Molten Salt Reactor (MSR) 방식 적용 논의 (기존 PWR보다 소형·고온·고압 해수 냉각 가능)

### 1.2 LNGC 컨셉 적용 방안
| 구분 | 내용 |
|------|------|
| **추진동력** | SMR에서 생산된 전기를 이용하여 전기추진 (Pure Electric Propulsion) |
| **장점** | 연료 적재시간 단축 (중유 보충 불필요), CO₂/Methane Slip 제로 |
| **단점** | 선급 심사 난이도 극상승 (원자력 안전·방재 기준), 국제법적 리스크 (IAEA) |
| **적용 시기** | 단기(2027) 실험선, 중장기(2030+) 상용선로 예상 |

### 1.3 타사설계 반영 포인트
1. **원전 격실 설계 공간 확보**: 원자로 격납용기·냉각 시스템·방사선 차폐 공간 할당
2. **전력계통 아키텍처**: SMR 발전기 → Main Switchboard(MSB) → 추진전동기까지 고전압 직류 계통 또는 대용량 부스덕트 시스템 설계
3. **연료저장소**: LPG/LNG 연료 대신 Uranium·Thorium 연료집적체 저장고 공간 설계
4. **안전 시스템**: 선급 DNV Nuclear Class, IAEA Safety Standards 준수 검토

---

## 2. 🏭 OCCS (Onboard Carbon Capture System) — 선적 탄소포집 시스템

### 2.1 OCCS 개요
- **선적 CCS**: 선박의 배기가스에 포함된 CO₂를 선상에서 흡수·포집하여 하역시설에서 재활용하거나 저장하는 기술
- **필수화 추세**: IMO CII(Emission Index), EU ETS(배출권 거래제), FuelEU Maritime 의무화에 따라 **OCCS는 필수가 아닌 필수 사항**
- **기술 방식**: Post-combustion (아민 흡수제 사용), Pre-combustion (연료 전처리 수소화 방식)

### 2.2 LNGC 적용 타당성
| 구분 | 내용 |
|------|------|
| **흡수제** | 아민 기반(Amine-based) 또는 암모니아 기반 (Mitsubishi, DNV 개발 중) |
| **저장 형식** | 액상(Liquid CO2) 30atm 이상, 고압 저장탱크 사용 |
| **공간 소모** | 탱크 용량 대비 약 5~10% 추가 공간 필요 (BOG 발생 증가) |
| **에너지 효율** | 발전 효율 3~5%p 감소 (Power Take-Off 부하 증가) |
| **선급 승인** | DNV "Onboard carbon capture and storage" 가이드라인 준수 필요 |

### 2.3 LNGC 컨셉 설계 반영 포인트
1. **OCCS 모듈 배치**:cargo space와 분리된 기계실 상부 또는 전용 층 배치
2. **BOG(BOG) 처리 시스템 통합**: LNG Vaporizer와 OCCS 흡수기 통합 설계 (BOG 압력 제어와 CO₂ 포집 연계)
3. **저고압 저장탱크 설계**: H-class 강재 또는 내식성 합금 탱크 (액상 CO₂ 저장용)
4. **하역 호스 연결부**: 육상 CO₂ 하역 설비와의 표준 호스 연결 인터페이스 설계
5. **안전 밸브 및 가스 경보기**: CO₂ 누출 방지 설계 (O₂ 농도 감지기 다수 설치)

---

## 3. 🌬️ WAPS (Wind Assisted Propulsion Systems) — 풍력 추진 보조 시스템

### 3.1 WAPS 개요
- **정의**: 선박의 돛(Rotor Sail)、Flettner Rotor、Kite(연) 등을 이용해 풍력을 추진력 보조
- **효율**: 최대 30%의 연료 절감 효과 (DNV, Wärtsilä 연구)
- **주요 기술**:
  - **Rotor Sail (로터 세일)**: rotating cylinder (Flettner rotor)의 마그누스 효과 이용
  - **Hard Sail (Hard Sail)**: 고정/가변형 세일
  - **Kite (Kite)**: 비행 키트를 사용하여 추력 확보

### 3.2 LNGC 적용 타당성
| 구분 | 내용 |
|------|------|
| **LNGC 적합성** | 대형 LNGC의 정속 항해 특성과 매우 적합 |
| **설치 가능 수** | 2~4 기의 Rotor Sail (로터 세일) 권장 |
| **공간 소모** | deck 상부 2~4개소 설치부 확보 (보통 cargo deck 중앙 부분) |
| **선급 승인** | DNV "Wind assisted propulsion" 가이드라인. IMO WAPS Guidelines 준수 |

### 3.3 LNGC 컨셉 설계 반영 포인트
1. **Rotor Sail 설치 위치**: Cargo tank deck 상부의 비활성화 공간 (4개소 권장: A, B, C, D 위치)
2. **전력 소모**: Rotor Sail 구동용 모터 전력 (약 100kW × 4) → MSB 연계 설계
3. **선체 형상 최적화**: Rotor Sail의 바람 유입각(Heading variation) 고려한 hull form 재설계
4. **안전 고려**: 극한 풍속(100kt 이상) 시 자동 세일 폴다운 시스템
5. **자동화 제어**: WAPS 전용 제어실 설치 및 AIS(자동감지)연동 설계

---

## 4. 🔋 선박 전동화 (Hybrid Electric Propulsion & BESS)

### 4.1 Hybrid Electric Propulsion (HEP)
- **LNGC 적용례**: Shell, Wärtsilä, HD HHI가 개발한 Hybrid Electric LNG Carrier (185,000 cbm급)
- **장점**:
  - 에너지 효율 향상 (BOG(Bring-Off Gas) 활용 발전)
  - **cargo space 6% 증가 **(Propulsion system이 차지하는 기존 기계실 공간 감소)
  - 진동·소음 감소 (Shipboard vibration/noise 개선)
  - 미래 연료 전환 용이 (Ammonia/Fuel Cell로의 전환 준비)

### 4.2 Battery Energy Storage System (BESS)
- **역할**: Peak shaving, Emergency power backup, Station keeping (DP) 보조
- **선박용 배터리**: 리튬이온전지(Li-ion), Flow battery, 연료전지(Fuel Cell) 혼합 적용
- **용량**: 선박 크기에 따라 500kWh ~ 10MWh 적용

### 4.3 LNGC 컨셉 설계 반영 포인트
1. **전기추진 동력계통**: LNG BOG 발전기 → Motor Generator → Shaft Line (전동 추진)
2. **Busduct(부스덕트) 설계**: 대용량 전력(50MW급) 전송 → 선박_Bus_Duct_부스덕트_설계_적용 참조
3. **BESS 배치**: 비활성화 공간(Engine Room 상부)에 BESS 컨테이너 배치
4. **충전 시스템**: Shore Power(육상전원) 연계 설계 (FuelEU Maritime 대응)
5. **고전압 직류 계통**: MVDC(Medium Voltage DC) 계통 도입 (전력 손실 최소화)

---

## 5. ⛽ 다연료 대응 Multi-Fuel Cargo Containment (GTT 기술 연동)

### 5.1 다연료 화물탱크 (GTT Mark III Flex, NO96 Flex)
- **GTT의 Mark III Flex**: LNG, Methanol, Ammonia, Bio-LNG 등 **다연료 호환** membrane containment system
- **핵심 장점**:
  - Methanol/Ammonia-ready: 기존 LNG 탱크에 Membrane 코팅 변경만으로 대체연료 호환
  - 연료전환 용이성: 향후 수소(H2)까지 확장 가능
  - 경제성: 탱크 구조 유지 → 설계 변경 최소화

### 5.2 대체연료 호환성 연구
| 대체연료 | 필요 온도 | Tank 재질 | Membrane 코팅 |
|------|------|------|------|
| LNG | -162°C | INVAR 36 (스테인less) | GTT NO96 / Mark III |
| Green Methanol | -30°C | 스테인less 316L | 내산성 코팅 |
| Green Ammonia | -33°C | 스테인less 316L | 내알칼리 코팅 |
| Hydrogen (미래) | -253°C | 특수합금 | 신규 개발 필요 |

### 5.3 LNGC 컨셉 설계 반영 포인트
1. **GTT Mark III Flex 채택**: 다연료 호환 membrane tank 적용 (미래 연료 전환 보장)
2. **Membrane 코팅 설계**: Methanol/Ammonia용 내산성/내알칼리 코팅 두께 고려
3. **BOG 처리 시스템**: 각 연료별 BOG(기화가스) 특성 고려 (메탄 vs 메탄올 vs 암모니아)
4. **연료 처리 계통**: Separate fuel supply line 설계 (LNG, Methanol, Ammonia별 파이프라인 분리)
5. **선급 승인**: DNV LR, ABS "Ammonia/Methanol Ready Notation" 심사 대응

---

## 6. 🌊 선체 최적화 (X-BOW, Flettner, Advanced Hull Form)

### 6.1 Hull form 최적화 (HD HHI + ABS 공동 개발)
- **Compact 200K LNG Carrier**: 선체 형상 최적화 + Machinery/Electrical/Piping arrangement 통합 설계
- **X-BOW (전방 선미형)**: 파도 받음 면적 감소 → 연료 절감 5~10%
- **Air Lubrication System**: 선저 공기주입으로 마찰저항 감소 (3~5% 연료 절감)

### 6.2 Wind Challenger (Mitsubishi)
- **Folding Rotor Sail (접이식 로터 세일)**: 4기 설치 가능 (Deck 상부 2개, Side 2개)
- **자동 접이식 기능**: 극한 풍속 시 세일 폴다운 (선박 안정성 확보)

### 6.3 LNGC 컨셉 설계 반영 포인트
1. **X-BOW 형상 채택**: 파도 받음 면적 감소 → 연비 향상
2. **Air Lubrication System**: 선저 공기주입 노즐 배치 설계 (3~5% 연료 절감)
3. **Wind Challenger 4기 설비**: Rotor Sail + 자동 접이식 메커니즘
4. **Propeller 최적화**: AIP (Augmented Propulsion) + Mewis Duct (10~15% 연료 절감)
5. **Hull coating**: Anti-fouling hull coating (초소수성 코팅 → 마찰저항 감소)

---

## 7. 🧠 Concept Report 작성 시 타사설계 핵심 반영사항 (Checklist)

| 분야 | 반영 사항 | Wiki 연계 |
|------|------|------|
| **추진동력** | Hybrid Electric 또는 SMR 기반 전기추진 | 선박_Bus_Duct_부스덕트_설계_적용 |
| **탄소포집** | OCCS 모듈 1set + 액상 CO₂ 저장탱크 | 본 문서 2장 |
| **풍력보조** | Wind Challenger 4기 (Rotor Sail) | 본 문서 3장 |
| **배터리** | Hybrid BESS (Peak shaving / DP 보조) | 본 문서 4장 |
| **화물탱크** | GTT Mark III Flex (다연료 호환) | 본 문서 5장 |
| **선체형상** | X-BOW + Air Lubrication + Mewis Duct | 본 문서 6장 |
| **배전반** | Busduct 3상 5선 (대용량 전기추진 계통) | 선박_Bus_Duct_부스덕트_설계_적용 |
| **안전** | Methane Slip 감지 + CO₂ 누출 경보기 | 선급 ABS/DNV/KR 심사 |
| **연료 저장** | Green Methanol / Green Ammonia 탱크 | 본 문서 5장 |
| **선급** | DNV Nuclear Class (SMR 시), Ammonia/Methanol Ready Notation | 본 문서 1,5장 |

---

## 8. 📈 경제성 및 타당성 분석 (Cost-Benefit)

### 8.1 투자 비용 대비 기대 효과
| 기술 | 추가 투자 비용 | 기대 효과 (비용절감) | 투자회수년 |
|------|------|------|------|
| **SMR** | 매우 높음 (원자력 격실 설계) | 연료비 제로, 탄소배출권 구매 불필요 | 장기(2030+) |
| **OCCS** | 높음 (CO₂ 포집·저장 시스템) | 탄소배출권 비용 절감, CII 등급 향상 | 3~5년 |
| **WAPS** | 적당함 (Rotor Sail 설치비) | 연료비 10~30% 절감 | 2~4년 |
| **Hybrid Electric** | 중간 (전기추진 시스템) | BOG 활용 발전, Space 6% 확보 | 3~5년 |
| **GTT Mark III Flex** | 보통 (Membrane 코팅 추가) | 다연료 전환 비용 절감 | 장기 |
| **Air Lubrication** | 적당함 | 연료비 3~5% 절감 | 2~3년 |

### 8.2 총체적 경제성 평가
- **초기 투자**: OCCS + WAPS + Hybrid Electric + Air Lubrication → 총 **약 5~8% 추가 투자**
- **운항비용 절감**: 연료비 15~30% 절감, 탄소배출권 비용 대폭 절감
- **수익성**: LNG 운임 상승 시 추가 수익 (탄소중립 LNGC Premium)
- **선급 승인**: 추가 심사 비용 발생 (DNV/Nuclear/Ammonia 등)

---

## 9. ⏰ 도입 로드맵 (Roadmap)

| 단계 | 기간 | 목표 |
|------|------|------|
| **Concept Phase** | 2026Q3~Q4 | 다연료 호환형 (Mark III Flex) + OCCS + WAPS + Hybrid Electric 통합 컨셉 정의 |
| **Pre-FEED Phase** | 2027Q1~Q2 | SMR 적용 타당성 검토, 선급 Preliminary Review |
| **FEED Phase** | 2027Q3~2028Q2 | 상세 설계 (Hull form, Machinery, Electrical, OCCS, WAPS, BESS 통합 설계) |
| **Ship Construction** | 2028Q3~2030Q4 | 도크 시공, 선급 심사, 진수·선적 시험 |
| **Commercial Operation** | 2031~ | 탄소중립 LNGC 상용 운항 |

---

## 10. 📝 Conclusion / Recommendations

1. **다연료 호환 설계 우선**: GTT Mark III Flex 채택은 장기적인 연료 전환 전략의 핵심.
2. **OCCS는 필수가 아닌 필수**: IMO 2030 규제 이전에 적용해야 탄소배출권 비용 절감 효과 극대화.
3. **WAPS는 연료비 절감의 핵심**: 30%까지 연료 절감 가능. Rotor Sail 4기 설치를 컨셉에 포함.
4. **전기추진은 Future-ready**: Hybrid Electric Propulsion 채택은 연료 전환(Fuel Cell, SMR)의 기초 인프라.
5. **SMR은 장기 관전**: 2030년대 상용화 목표. 실험선(2027) 모니터링 필요.
6. **Busduct(부스덕트) 필수 적용**: 대용량 전기추진 계통에 부스덕트 채택 → 선박_Bus_Duct_부스덕트_설계_적용 참조.

---

*본 보고서는 2025~2026년 기준의 최신 기술 동향을 기반으로 작성된 것이며, 향후 규제 changes, 기술 성숙도, 경제성 변화에 따라 수정되어야 합니다.*
