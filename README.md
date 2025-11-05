# 🧠 Customer Churn Prediction Service

A production-ready **FastAPI** microservice for predicting customer churn.  
This project packages a trained `scikit-learn` pipeline into a containerized REST API and web app, deployed on **Render** using **Docker** and **UV** dependency management.

- Actual deployment is found in churn-service folder
- Model training process can be found in churn-model-building folder

---

## 🧩 Project Structure

```

├── ReadMe


├── marketsvc                          #notebook to communicate with fast api service


churn-service/
├── pred_svc.py                        # FastAPI prediction service
├── pipeline_model_C=0.5.bin           # Trained ML pipeline
├── templates/
│ └── index.html                       # Web input form (Jinja2 template)
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
