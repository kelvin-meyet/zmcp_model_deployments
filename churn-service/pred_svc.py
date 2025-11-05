import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Literal
from pydantic import BaseModel, Field
import pickle

# Load model
model_file = "pipeline_model_C=0.5.bin"
with open(model_file, "rb") as f_in:
    training_pipeline = pickle.load(f_in)

# FastAPI app with Swagger disabled
app = FastAPI(
    title="churn-prediction-apis", docs_url=None, redoc_url=None, openapi_url=None
)
templates = Jinja2Templates(directory="templates")


# Input schema
class Customer(BaseModel):
    gender: Literal["male", "female"]
    seniorcitizen: Literal[0, 1]
    partner: Literal["yes", "no"]
    dependents: Literal["yes", "no"]
    phoneservice: Literal["yes", "no"]
    multiplelines: Literal["no", "yes", "no_phone_service"]
    internetservice: Literal["dsl", "fiber_optic", "no"]
    onlinesecurity: Literal["no", "yes", "no_internet_service"]
    onlinebackup: Literal["no", "yes", "no_internet_service"]
    deviceprotection: Literal["no", "yes", "no_internet_service"]
    techsupport: Literal["no", "yes", "no_internet_service"]
    streamingtv: Literal["no", "yes", "no_internet_service"]
    streamingmovies: Literal["no", "yes", "no_internet_service"]
    contract: Literal["month-to-month", "one_year", "two_year"]
    paperlessbilling: Literal["yes", "no"]
    paymentmethod: Literal[
        "electronic_check",
        "mailed_check",
        "bank_transfer_(automatic)",
        "credit_card_(automatic)",
    ]
    tenure: int = Field(..., ge=0)
    monthlycharges: float = Field(..., ge=0.0)
    totalcharges: float = Field(..., ge=0.0)

    class Config:
        extra = "forbid"


# Output schema
class PredictResponse(BaseModel):
    churn_probability: float
    churn: bool


# Prediction logic
def predict_single(customer):
    result = training_pipeline.predict_proba(customer)[0, 1]
    return float(result)


# API endpoint
@app.post("/predict", response_model=PredictResponse)
def predict(customer: Customer) -> PredictResponse:
    churn_proba = predict_single(customer.dict())
    return PredictResponse(
        churn_probability=round(churn_proba, 3), churn=churn_proba >= 0.5
    )


# UI route
@app.get("/", response_class=HTMLResponse)
def form_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Form handler
@app.post("/form-predict", response_class=HTMLResponse)
def predict_ui(
    request: Request,
    gender: str = Form(...),
    seniorcitizen: int = Form(...),
    partner: str = Form(...),
    dependents: str = Form(...),
    phoneservice: str = Form(...),
    multiplelines: str = Form(...),
    internetservice: str = Form(...),
    onlinesecurity: str = Form(...),
    onlinebackup: str = Form(...),
    deviceprotection: str = Form(...),
    techsupport: str = Form(...),
    streamingtv: str = Form(...),
    streamingmovies: str = Form(...),
    contract: str = Form(...),
    paperlessbilling: str = Form(...),
    paymentmethod: str = Form(...),
    tenure: int = Form(...),
    monthlycharges: float = Form(...),
    totalcharges: float = Form(...),
):

    customer = {
        "gender": gender,
        "seniorcitizen": seniorcitizen,
        "partner": partner,
        "dependents": dependents,
        "phoneservice": phoneservice,
        "multiplelines": multiplelines,
        "internetservice": internetservice,
        "onlinesecurity": onlinesecurity,
        "onlinebackup": onlinebackup,
        "deviceprotection": deviceprotection,
        "techsupport": techsupport,
        "streamingtv": streamingtv,
        "streamingmovies": streamingmovies,
        "contract": contract,
        "paperlessbilling": paperlessbilling,
        "paymentmethod": paymentmethod,
        "tenure": tenure,
        "monthlycharges": monthlycharges,
        "totalcharges": totalcharges,
    }

    proba = predict_single(customer)
    churn = proba >= 0.5
    return templates.TemplateResponse(
        "index.html", {"request": request, "result": round(proba, 3), "churn": churn}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)


# Original FastAPI with docs
# ==================================


# import uvicorn
# from fastapi import FastAPI

# from typing import Dict, Any
# from pydantic import BaseModel

# from typing import Literal
# from pydantic import BaseModel, Field

# #load pipeline model
# import pickle

# model_file = 'pipeline_model_C=0.5.bin'
# with open(model_file, 'rb') as f_in:
#     training_pipeline = pickle.load(f_in)


# #Define input and output schema
# #request - pydantic class for request
# class Customer(BaseModel):
#     gender: Literal["male", "female"]
#     seniorcitizen: Literal[0, 1]
#     partner: Literal["yes", "no"]
#     dependents: Literal["yes", "no"]
#     phoneservice: Literal["yes", "no"]
#     multiplelines: Literal["no", "yes", "no_phone_service"]
#     internetservice: Literal["dsl", "fiber_optic", "no"]
#     onlinesecurity: Literal["no", "yes", "no_internet_service"]
#     onlinebackup: Literal["no", "yes", "no_internet_service"]
#     deviceprotection: Literal["no", "yes", "no_internet_service"]
#     techsupport: Literal["no", "yes", "no_internet_service"]
#     streamingtv: Literal["no", "yes", "no_internet_service"]
#     streamingmovies: Literal["no", "yes", "no_internet_service"]
#     contract: Literal["month-to-month", "one_year", "two_year"]
#     paperlessbilling: Literal["yes", "no"]
#     paymentmethod: Literal[
#         "electronic_check",
#         "mailed_check",
#         "bank_transfer_(automatic)",
#         "credit_card_(automatic)",
#     ]
#     tenure: int = Field(..., ge=0)
#     monthlycharges: float = Field(..., ge=0.0)
#     totalcharges: float = Field(..., ge=0.0)

#     class Config:
#         extra = "forbid"


# #response -> output
# class PredictResponse(BaseModel):
#     churn_probability: float
#     churn: bool


# #initiate fastapi
# app = FastAPI(title = "churn-prediction-apis")


# def predict_single(customer):
#     result = training_pipeline.predict_proba(customer)[0,1]
#     return float(result)


# @app.post("/predict", response_model=PredictResponse)
# def predict(customer: Customer) -> PredictResponse:
#     churn_proba = predict_single(customer.dict())
#     #churn_proba.round(2)

#     #action = "send email with promo" if churn_proba >= 0.5 else "Do not send email"

#     return PredictResponse(
#        churn_probability=churn_proba,
#        churn = bool(churn_proba >= 0.5),
#        #action = str(action)
#     )

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=9696)
