# 🧠 Customer Churn Prediction Service

A production-ready **FastAPI** microservice for predicting customer churn.  
This project packages a trained `scikit-learn` pipeline into a containerized REST API and web app, deployed on **Render** using **Docker** and **UV** dependency management.

---

## 🚀 Live Demo

🔗 **App URL:** [https://zmcpchurnprediction.onrender.com](https://zmcpchurnprediction.onrender.com)

The web interface allows users to enter customer details and instantly get a churn probability and decision.

- Churn (also known as attrition rate, turnover, customer turnover, or customer defection) refers to the rate at which customers cancels or stop doing business with a company or a service provider. It is a key metric in industries that provides valuable services to customers.

---

## ⚙️ Tech Stack

| Component        | Purpose                                          |
| ---------------- | ------------------------------------------------ |
| **FastAPI**      | Web framework for serving predictions            |
| **scikit-learn** | Trained ML pipeline (Logistic Regression)        |
| **UV**           | Fast dependency installer and virtualenv manager |
| **Docker**       | Containerization for consistent deployment       |
| **Render**       | Cloud hosting for the live web app               |
| **Jinja2**       | Template engine for the frontend HTML form       |

---

## 📸 Screenshots

**Web UI Form**

<p align="center" style="margin: 1em 0;">
  <img src="assets/example-ui.png" style="max-width:90%; height:auto;" alt="Web UI form screenshot" />
</p>

---

## 🧩 Project Structure

```
churn-service/
├── pred_svc.py                        # FastAPI prediction service
├── pipeline_model_C=0.5.bin           # Trained ML pipeline
├── templates/
│ └── index.html                       # Web input form (Jinja2 template)
├── Dockerfile                         # Build & run container
├── pyproject.toml                     # Project dependencies
├── uv.lock                            # Locked dependency versions
└── README.md                          # Documentation
```

---

## 🧑‍💻 Author

**Kelvin Ofori-Minta, PhD**  
📍 Indianapolis, IN  
📧 [k.mintah28@gmail.com](mailto:k.mintah28@gmail.com)  
🔗 **LinkedIn:** [https://www.linkedin.com/in/kelvin-o-9a5692b8/](https://www.linkedin.com/in/kelvin-o-9a5692b8/)

---
