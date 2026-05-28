#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROI 계산 템플릿 생성기 — 1인 기업 가상 시나리오 기반
가격대: 9,900 / 19,900 / 29,900 (단일 상품)
구독: 월 4,900 / 연 49,000 (번들)
전환율: 1% ~ 5%, 고객 수: 100 / 500 / 1,000명
"""

import csv
import os
from datetime import datetime

# === 설정 ===
SALES_PRICES = [9_900, 19_900, 29_900]
SUBSCRIPTION_MONTHLY = 4_900
SUBSCRIPTION_ANNUAL = 49_000

CONVERSION_RATES = [0.01, 0.02, 0.03, 0.04, 0.05]  # 1% ~ 5%
CUSTOMER_SCENARIOS = [100, 500, 1000]

MONTHLY_MAINTENANCE_COST = 0  # 1인 기업 가정 (자기 운영)
ANNUAL_MAINTENANCE_COST = MONTHLY_MAINTENANCE_COST * 12

# === 계산 로직 ===
def calc_revenue(price, customers, conv_rate):
    return price * int(customers * conv_rate)

def calc_roi(revenue, cost):
    return (revenue - cost) / cost * 100 if cost > 0 else float('inf')

def generate_template():
    rows = []
    header = [
        "시나리오명", "가격/요금제", "고객 수", "전환율(%)",
        "월 구매 고객수", "월 매출", "월 이익", "월 ROI(%)",
        "연 매출", "연 이익", "연 ROI(%)"
    ]
    rows.append(header)

    scenario_id = 1

    # 1. 단일 상품 시나리오
    for price in SALES_PRICES:
        for customers in CUSTOMER_SCENARIOS:
            for conv_rate in CONVERSION_RATES:
                monthly_customers = int(customers * conv_rate)
                monthly_revenue = calc_revenue(price, customers, conv_rate)
                monthly_profit = monthly_revenue - MONTHLY_MAINTENANCE_COST
                monthly_roi = calc_roi(monthly_revenue, MONTHLY_MAINTENANCE_COST) if MONTHLY_MAINTENANCE_COST > 0 else 1000.0
                annual_revenue = monthly_revenue * 12
                annual_profit = monthly_profit * 12
                annual_roi = calc_roi(annual_revenue, ANNUAL_MAINTENANCE_COST) if ANNUAL_MAINTENANCE_COST > 0 else 1000.0

                rows.append([
                    f"단일-{scenario_id:02d}",
                    f"{price:,}원",
                    f"{customers:,}",
                    f"{int(conv_rate*100)}%",
                    f"{monthly_customers:,}",
                    f"{monthly_revenue:,}",
                    f"{monthly_profit:,}",
                    f"{monthly_roi:.1f}%",
                    f"{annual_revenue:,}",
                    f"{annual_profit:,}",
                    f"{annual_roi:.1f}%"
                ])
                scenario_id += 1

    # 2. 구독형 시나리오
    for customers in CUSTOMER_SCENARIOS:
        for conv_rate in CONVERSION_RATES:
            monthly_customers = int(customers * conv_rate)
            monthly_revenue = SUBSCRIPTION_MONTHLY * monthly_customers
            monthly_profit = monthly_revenue - MONTHLY_MAINTENANCE_COST
            monthly_roi = calc_roi(monthly_revenue, MONTHLY_MAINTENANCE_COST) if MONTHLY_MAINTENANCE_COST > 0 else 1000.0
            annual_revenue = SUBSCRIPTION_ANNUAL * monthly_customers  # 연간 전환 기준 (번들 구매 미포함)
            annual_profit = annual_revenue - ANNUAL_MAINTENANCE_COST
            annual_roi = calc_roi(annual_revenue, ANNUAL_MAINTENANCE_COST) if ANNUAL_MAINTENANCE_COST > 0 else 1000.0

            rows.append([
                f"구독-{scenario_id:02d}",
                f"월 {SUBSCRIPTION_MONTHLY:,}원",
                f"{customers:,}",
                f"{int(conv_rate*100)}%",
                f"{monthly_customers:,}",
                f"{monthly_revenue:,}",
                f"{monthly_profit:,}",
                f"{monthly_roi:.1f}%",
                f"{annual_revenue:,}",
                f"{annual_profit:,}",
                f"{annual_roi:.1f}%"
            ])
            scenario_id += 1

    # 3. 번들형 시나리오 (연 49,000원 기준, 전환율 가정 동일)
    for customers in CUSTOMER_SCENARIOS:
        for conv_rate in CONVERSION_RATES:
            annual_customers = int(customers * conv_rate)
            annual_revenue = SUBSCRIPTION_ANNUAL * annual_customers
            annual_profit = annual_revenue - ANNUAL_MAINTENANCE_COST
            annual_roi = calc_roi(annual_revenue, ANNUAL_MAINTENANCE_COST) if ANNUAL_MAINTENANCE_COST > 0 else 1000.0
            monthly_avg_revenue = annual_revenue / 12
            monthly_avg_profit = annual_profit / 12
            monthly_avg_roi = calc_roi(monthly_avg_revenue, MONTHLY_MAINTENANCE_COST) if MONTHLY_MAINTENANCE_COST > 0 else 1000.0

            rows.append([
                f"번들-{scenario_id:02d}",
                f"연 {SUBSCRIPTION_ANNUAL:,}원 (번들)",
                f"{customers:,}",
                f"{int(conv_rate*100)}%",
                f"{annual_customers:,} (연간)",
                f"{monthly_avg_revenue:,.0f}",
                f"{monthly_avg_profit:,.0f}",
                f"{monthly_avg_roi:.1f}%",
                f"{annual_revenue:,}",
                f"{annual_profit:,}",
                f"{annual_roi:.1f}%"
            ])
            scenario_id += 1

    # === CSV 저장 ===
    output_path = "/Users/mr.k/wiki/_company/_agents/business/tools/roi_template_1person_business.csv"
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print(f"✅ ROI 템플릿 CSV 생성 완료: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_template()