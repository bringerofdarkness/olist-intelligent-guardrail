# 🚀 Olist Intelligent Guardrail (E-commerce Logistics Intelligence)
> Turning logistics data into real-time risk intelligence for smarter delivery decisions.

<p align="center">
  <b>AI-Powered Delivery Risk Prediction</b><br>
  End-to-End Machine Learning Application<br><br>
  FastAPI · Streamlit · Scikit-learn · Plotly · Hugging Face Spaces
</p>

---

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Spaces-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)

---

## 🌍 Live Demo

👉 **[Launch App](https://huggingface.co/spaces/bringerofdarkness/olist-intelligent-guardrail)**  
*(Interactive AI dashboard with real-time prediction)*

---

## 📸 App Preview

<p align="center">
  <img src="assets/prediction.png" width="48%">
  <img src="assets/static_analysis.png" width="48%">
</p>

<p align="center">
  <img src="assets/sidebar.png" width="260">
</p>

---

## 📌 Project Overview

**Olist Intelligent Guardrail** is an end-to-end machine learning system built to predict **delivery delay risk** in e-commerce logistics.

The project combines:

* 🔍 Advanced feature engineering
* 🤖 Ensemble machine learning model
* ⚡ FastAPI backend for real-time inference
* 📊 Streamlit dashboard for business insights
* 🚀 Deployment-ready architecture for live product demonstration

This solution is designed to help e-commerce businesses proactively identify risky orders before delivery issues impact customers and operations.

---
## 💼 Business Impact

This system is designed to help e-commerce platforms:

- 🚚 **Reduce late deliveries** by identifying high-risk orders early  
- 📉 **Minimize operational losses** from delayed shipments  
- 📊 **Improve logistics planning** using risk-based decision making  
- 🤝 **Enhance customer satisfaction** with proactive intervention  
- ⚡ **Enable real-time decision support** for operations teams  

---

## 🧠 Problem Statement

Late deliveries can significantly harm:

* Customer satisfaction
* Seller reliability
* Marketplace trust
* Operational efficiency

This system predicts **whether an order is likely to be delayed**, enabling:

* proactive intervention
* smarter logistics planning
* risk-aware operational decisions
* faster response to high-risk shipments

---
## 🎯 Real-World Use Case

A logistics manager can:

1. Input order details (distance, weight, price, seller risk)
2. Instantly receive a **risk score**
3. Take action:
   - Low risk → proceed normally  
   - High risk → prioritize or reroute shipment  

This transforms raw data into **actionable business decisions in seconds**.

---

## ⚙️ System Architecture

```text
User Input → Streamlit UI → FastAPI API → ML Model → Prediction → Dashboard
```

---

## 🔑 Key Features

### ✅ Real-Time Prediction

* Instant delay risk scoring
* Confidence-based prediction output
* Low-risk vs high-risk classification

### 📊 Executive Analytics Dashboard

* Delivery performance indicators
* Risk factor visualization
* Regional risk correlation insights
* Interactive business-facing UI

### 🧠 ML Intelligence

* Feature-engineered inputs such as:

  * logistics stress
  * freight ratio
  * seller reliability
  * regional late-delivery patterns
* Ensemble model optimized for prediction performance

### 🎯 Business Impact

* Identify high-risk deliveries before failure
* Support logistics decision-making
* Improve customer delivery experience
* Reduce operational blind spots

---

## 📁 Project Structure

```text
olist-intelligent-guardrail/
│
├── api/                # FastAPI backend
├── frontend/           # Streamlit UI
├── models/             # Trained ML artifacts
├── data/               # Dataset files
├── notebooks/          # EDA & feature engineering
├── src/                # Core project modules
├── tests/              # Testing scripts
├── Dockerfile
└── README.md
```

---

## 🛠️ Tech Stack

| Layer         | Technology          |
| ------------- | ------------------- |
| ML Model      | Scikit-learn        |
| Backend       | FastAPI             |
| Frontend      | Streamlit           |
| Visualization | Plotly              |
| Deployment    | Hugging Face Spaces |

---

## 📊 Model Intelligence

The model predicts the **probability of delivery delay** based on:

- 📍 Distance & logistics complexity  
- 📦 Product weight & shipping load  
- 💰 Order value & freight ratio  
- 🏪 Seller reliability (historical performance)  
- 🌍 Regional delay patterns  

### Output

- 🎯 Delay Probability (0–100%)
- 🚦 Risk Classification (Low / High)

👉 Designed for **real-time decision-making in logistics operations**


---

## 📂 Dataset

This project uses the **Brazilian E-Commerce Public Dataset by Olist**.

👉 Dataset Link:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/code

The dataset provides rich transactional and logistics information that supports:

* delivery behavior analysis
* seller performance analysis
* customer order flow understanding
* feature engineering for delay prediction

---

## 🔗 Repository

👉 GitHub Repository:
https://github.com/bringerofdarkness/olist-intelligent-guardrail

---

## 🚀 How to Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/bringerofdarkness/olist-intelligent-guardrail.git
cd olist-intelligent-guardrail
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r api/requirements.txt
```

### 5. Run Backend

```bash
cd api
uvicorn main:app --reload
```

### 6. Run Frontend

Open a new terminal from the project root, then run:

```bash
cd frontend
streamlit run app.py
```

---

## 📈 Future Improvements

* 🔄 Automated model retraining pipeline
* 📦 Batch prediction support
* 📊 Enhanced analytics dashboard
* ☁️ Production-grade cloud deployment
* 📉 Model monitoring and drift detection

---

## 👨‍💻 Author

**Md Shahrul Zakaria**

📧 [md.shahrul.zakaria@gmail.com](mailto:md.shahrul.zakaria@gmail.com)
🔗 LinkedIn: https://www.linkedin.com/in/md-shahrul-zakaria-24a805230/
🔗 GitHub: https://github.com/bringerofdarkness

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---
