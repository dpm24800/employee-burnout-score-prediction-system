# Employee Burnout AI: Wellness Predictor
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python) ![Streamlit](https://img.shields.io/badge/Streamlit-1.23%2B-FF4B4B?logo=streamlit) ![Flask](https://img.shields.io/badge/Flask-2.x-000000?logo=flask) ![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end Machine Learning regression project designed to predict **Employee Burnout Scores** () based on remote work habits and lifestyle metrics. This system helps in identifying early signs of exhaustion using data-driven insights.

## Project Overview
In the modern "Work From Home" era, burnout has become a silent productivity killer. This project utilizes a dataset of employee activities to build a predictive model. By analyzing factors like screen time, sleep, and task completion, the AI provides a precise burnout score, allowing for proactive wellness interventions.

### Key Features

* **Precise Regression:** Predicts a continuous burnout score () rather than just a category.
* **Dual-Platform UI:** High-end **Flask** web application and a sleek **Streamlit** dashboard.
* **Glassmorphic Design:** A modern dark-themed interface with electric blue accents and interactive forms.
* **Modular Pipeline:** Includes dedicated scripts for Data Ingestion, Transformation, Model Training, and Prediction.

## Dataset & Features

The model is trained on the `WorkFromHomeBurnout.csv` dataset. For the final prediction engine, we exclude identifiers (`user_id`) and categorical risks (`burnout_risk`) to focus on the raw numerical and behavioral features.

### Features ():

| Feature | Description |
| --- | --- |
| **Day Type** | Whether the data point is from a Weekday or Weekend. |
| **Work Hours** | Total number of hours spent working. |
| **Screen Time** | Total hours spent looking at digital screens. |
| **Meetings Count** | Total number of meetings attended during the day. |
| **Breaks Taken** | Number of breaks taken during work hours. |
| **After-hours Work** | Hours spent working outside of standard schedule. |
| **Sleep Hours** | Total hours of rest/sleep. |
| **Task Rate** | Completion percentage of assigned tasks (). |


## Project Structure

```
ml-project/
├── artifacts/                # Serialized models & preprocessors
├── catboost_info/            # CatBoost training metadata
├── notebook/                 # Jupyter notebooks for EDA & modeling
├── src/
│   ├── __init__.py
│   ├── components/           # Data ingestion, transformation modules
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/             # Training & prediction pipelines
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── exception.py          # Custom exception handling
│   ├── logger.py             # Logging configuration
│   └── utils.py              # Utility functions
├── templates/                # Flask HTML templates
├── flask-app.py              # Flask web application (port 8000)
├── streamlit-app.py          # Streamlit interactive UI
├── requirements.txt          # Project dependencies
├── setup.py                  # Package configuration
├── train.py                  # Training script
└── README.md
```

## Project Workflow

The project follows a modular industry-standard pipeline:

1. **Data Ingestion:** Reads the CSV data and splits it into training and testing sets.
2. **Data Transformation:** Handles categorical encoding (Day Type) and scales numerical features using a `ColumnTransformer`.
3. **Model Training:** Evaluates multiple regression algorithms (Linear Regression, Lasso, Ridge, CatBoost, XGBoost) and selects the best-performing model based on  score.
4. **Prediction Pipeline:** A dedicated service that takes user input from the web interface, converts it to a DataFrame, and returns the predicted burnout score.

## Logging and Exception Handling

To ensure the application is production-ready, I have implemented custom logging and exception handling:

* **Custom Exceptions:** Any error occurring in the pipeline (from data loading to prediction) is caught by a custom exception class that provides the specific file name and line number for debugging.
* **Logging:** Every step of the execution is logged into a `.log` file, allowing us to track the model's behavior and performance over time.

## Installation & Usage

1. **Clone the Repo**
```bash
git clone https://github.com/dpm24800/employee-wellness-predictor.git
cd employee-wellness-predictor
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# OR
venv\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run Training Script**
```bash
python train.py
```

## Usage

### Option 1: Streamlit Interface (Recommended)
6. **Run Streamlit App**
```bash
streamlit run streamlit-app.py
```

→ Open http://localhost:8501 in your browser

### Option 2: Flask Application
5. **Run Flask App**
```bash
python flask-app.py
```

→ Open http://localhost:8000 in your browser


## Dependencies

Key libraries used:

- `pandas`, `numpy` – Data manipulation
- `matplotlib`, `seaborn`, `altair` – Visualization
- `scikit-learn` – Preprocessing & baseline models
- `catboost`, `xgboost` – Gradient boosting models
- `dill` – Model serialization
- `flask`, `streamlit` – Web interfaces

See [`requirements.txt`](requirements.txt) for full dependency list.

## Deployment

The application is containerized and ready for deployment on cloud platforms like **AWS**, **Azure**, or **Heroku**. The Streamlit version is currently hosted on **Streamlit Community Cloud**.

---

## License
Distributed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact
Dipak Pulami Magar – [@dpm24800](https://www.linkedin.com/in/dpm24800/)
**Developed by [Dipak Pulami Magar](https://www.google.com/search?q=https://github.com/dpm24800) . 2026**