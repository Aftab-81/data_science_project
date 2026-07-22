# 🍷 End-to-End Wine Quality Prediction Project

An end-to-end Machine Learning project that follows an industry-standard pipeline for building, training, and deploying a Wine Quality Prediction model. The project is designed with a modular architecture, making it scalable, maintainable, and production-ready.

---

## 📌 Project Overview

This project demonstrates how to build a complete Machine Learning pipeline from data ingestion to model evaluation using best software engineering practices.

The pipeline includes:

- Data Ingestion
- Data Validation
- Data Transformation
- Model Training
- Model Evaluation
- Configuration Management
- Logging & Exception Handling
- MLflow Experiment Tracking

---

## 📂 Project Structure

```
data_science_project/
│
├── artifacts/
│
├── config/
│   └── config.yaml
│
├── research/
│
├── src/
│   └── datascience/
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── pipeline/
│       ├── utils/
│       └── logging/
│
├── main.py
├── params.yaml
├── schema.yaml
├── requirements.txt
└── README.md
```

---

## 🚀 Workflow

```
Configuration Files
        │
        ▼
Configuration Manager
        │
        ▼
Configuration Entities
        │
        ▼
─────────────────────────────
Stage 1 → Data Ingestion
        │
        ▼
Download Dataset
        │
        ▼
artifacts/data_ingestion/
        │
        ▼
─────────────────────────────
Stage 2 → Data Validation
        │
        ▼
Validate Dataset
        │
        ▼
status.txt
        │
        ▼
─────────────────────────────
Stage 3 → Data Transformation
        │
        ▼
Data Cleaning
Feature Engineering
Train-Test Split
        │
        ▼
train.csv
test.csv
preprocessor.pkl
        │
        ▼
─────────────────────────────
Stage 4 → Model Training
        │
        ▼
Train Multiple Models
Select Best Model
        │
        ▼
model.pkl
metrics.json
        │
        ▼
─────────────────────────────
Stage 5 → Model Evaluation
        │
        ▼
MLflow Logging
```

---

## ⚙️ Technologies Used

- Python 3.11
- Pandas
- NumPy
- Scikit-learn
- MLflow
- Flask
- PyYAML
- python-box
- Joblib
- Logging
- Ensure
- ConfigBox

---

## 📁 Configuration Files

### config.yaml

Stores project paths and file locations.

Example:

```yaml
data_ingestion:
    source_URL:
    local_data_file:
```

---

### params.yaml

Stores machine learning model parameters.

Example:

```yaml
RandomForest:
    n_estimators: 200
    max_depth: 20
```

---

### schema.yaml

Stores dataset schema including column names and datatypes.

---

## 🔧 Features

- Modular project structure
- Configuration-driven pipeline
- Automatic directory creation
- YAML-based configuration
- Logging support
- Exception handling
- Reusable utility functions
- Type validation using `ensure_annotations`
- Binary model serialization using Joblib

---

## 📦 Utility Functions

The project includes reusable utility functions such as:

- `read_yaml()`
- `create_directories()`
- `save_json()`
- `load_json()`
- `save_bin()`
- `load_bin()`

---

## 📊 Pipeline Stages

### 1. Data Ingestion

Downloads the dataset from the source URL and stores it locally.

**Input**

- Source URL
- Local file path

**Output**

```
artifacts/data_ingestion/data.csv
```

---

### 2. Data Validation

Validates the downloaded dataset against the schema.

**Checks**

- Missing Columns
- Data Types
- Schema Validation

---

### 3. Data Transformation

Performs preprocessing and feature engineering.

Outputs:

- train.csv
- test.csv
- preprocessor.pkl

---

### 4. Model Training

- Trains multiple Machine Learning models
- Hyperparameter tuning
- Selects the best performing model

Outputs:

- model.pkl
- metrics.json

---

### 5. Model Evaluation

Evaluates the trained model and logs results using MLflow.

---

## ▶️ Installation

Clone the repository

```bash
git clone <repository_url>
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run the Project

```bash
python main.py
```

---

## 📈 Future Improvements

- Model Deployment using Flask
- CI/CD Pipeline using GitHub Actions
- Docker Containerization
- AWS S3 Integration
- Cloud Deployment
- Monitoring & Logging

---

## 👨‍💻 Author

**Aftabalam Makandar**

AI/ML Intern | Machine Learning & NLP Enthusiast

---

## ⭐ Acknowledgement

This project is inspired by the End-to-End Machine Learning project by **Krish Naik**, implemented as a learning exercise to understand production-ready ML pipelines and software engineering best practices.