import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/predict"

def run_stress_test(name, payload):
    print(f"--- Testing Scenario: {name} ---")
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            res = response.json()
            print(f"Result: {res['risk_status']} | Prob: {res['probability']:.4f}")
            return res
        else:
            print(f"FAILED: Status {response.status_code} | {response.text}")
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")

# 1. THE "IMPOSSIBLE" ORDER (Boundary Test)
# Testing if the model crashes with near-zero values
test_boundary = {
    "distance_km": 0.1, "price": 1.0, "freight_value": 0.1, "product_weight_g": 1.0,
    "product_photos_qty": 1, "purchase_hour": 12, "purchase_day_of_week": 1,
    "purchase_month": 1, "category_short": "other", "seller_reliability": 0.0, "state_late_avg": 0.0
}

# 2. THE "LOGISTICS NIGHTMARE" (Extreme Stress Test)
# Heavy, far, bad seller, peak month - Should be near 100%
test_nightmare = {
    "distance_km": 3500.0, "price": 1000.0, "freight_value": 200.0, "product_weight_g": 30000.0,
    "product_photos_qty": 1, "purchase_hour": 23, "purchase_day_of_week": 6,
    "purchase_month": 11, "category_short": "furniture", "seller_reliability": 0.80, "state_late_avg": 0.50
}

# 3. THE "SENSITIVITY" CHECK
# Small change in Seller Risk should significantly move the needle
low_seller_risk = test_boundary.copy()
low_seller_risk["seller_reliability"] = 0.05

high_seller_risk = test_boundary.copy()
high_seller_risk["seller_reliability"] = 0.60

# RUN TESTS
run_stress_test("Boundary (Zero-ish)", test_boundary)
run_stress_test("Logistics Nightmare", test_nightmare)
run_stress_test("Sensitivity - Low Seller Risk", low_seller_risk)
run_stress_test("Sensitivity - High Seller Risk", high_seller_risk)