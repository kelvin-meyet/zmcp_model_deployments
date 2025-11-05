# 🧠 Customer Churn Prediction Service

A production-ready **FastAPI** microservice for predicting customer churn.  
This project packages a trained `scikit-learn` pipeline into a containerized REST API and web app, deployed on **Render** using **Docker** and **UV** dependency management.

- Actual deployment is found in churn-service folder
- Model training process can be found in churn-model-building folder

---

## 🚀 Live Demo

🔗 **App URL:** [https://zmcpchurnprediction.onrender.com](https://zmcpchurnprediction.onrender.com)

This web interface allows users to enter customer details and instantly get a churn probability(a custo) and decision whether a user will be retained or leave .

- Churn (also known as attrition rate, turnover, customer turnover, or customer defection) refers to the rate at which customers cancels or stop doing business with a company or a service provider. It is a key metric in industries that provides valuable services to customers.

💡 Heads-up: The app may take about 40 - 50 seconds to start the first time you open it — this is a normal cold-start delay on Render’s free tier. Subsequent requests are lightning-fast!.

---

## 🧩 Project Structure

```
├── marketsvc                          # notebook to test and communicate with fast api service


churn-service/
├── pred_svc.py                        # FastAPI prediction service
├── pipeline_model_C=0.5.bin           # Trained ML pipeline
├── templates/
│ └── index.html                       # Jinja2 template - Template engine for the frontend HTML input form
├── Dockerfile                         # Build & run container
├── pyproject.toml                     # Project dependencies
├── uv.lock                            # Locked dependency versions
└── README.md                          # Documentation

churn-model-building/
├── Telco data
├── churn modelling notebook
├── model prediction script
├── model training script

```
