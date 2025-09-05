# 🚀 Data Science Projects

This repository contains a series of **data science projects** completed using Python.  
They demonstrate skills in **data preprocessing, machine learning, model evaluation, visualization, and dashboarding**.

---

## 📂 Projects Included

### 📊 Term Deposit Subscription Prediction
- **Dataset:** Bank Marketing Dataset (UCI ML Repository)  
- **Objective:** Predict whether a customer will subscribe to a term deposit after a marketing campaign.  
- **Approach:**
  - Data preprocessing & encoding categorical features  
  - Built and compared Logistic Regression & Random Forest models  
  - Evaluated models with Confusion Matrix, F1-Score, ROC Curve  
  - Used **SHAP explainability** to interpret predictions  
- **Key Insight:** Random Forest achieved better performance; call duration & demographics strongly influenced predictions.  

---

### 📈 Global Superstore Business Dashboard
- **Dataset:** Global Superstore dataset  
- **Objective:** Build an interactive dashboard for sales & profit analysis.  
- **Tech:** Streamlit, Pandas, Matplotlib, Seaborn  
- **Features:**
  - Sidebar filters: Region, Category, Sub-Category  
  - KPIs: Total Sales, Total Profit, Top 5 Customers  
  - Visualizations: Category-wise sales/profit, regional breakdown, customer analysis  
- **Key Insight:** Dashboard provides real-time business intelligence, helping identify high-value customers and profitable categories.  

---

### ⚡ Energy Consumption Forecasting
- **Dataset:** Household Power Consumption dataset (UCI ML Repository)  
- **Objective:** Forecast short-term energy consumption using time series models.  
- **Models Implemented:**
  - ARIMA (manual order selection `(2,1,2)`)  
  - Prophet (trend + seasonality)  
  - XGBoost (lag feature-based regression)  
- **Evaluation Metrics:** MAE & RMSE  
- **Key Insight:** Machine learning and hybrid approaches like XGBoost capture complex dependencies better than traditional ARIMA.  

---

## 🛠️ Tech Stack
- **Python**  
- **Pandas, NumPy, Matplotlib, Seaborn**  
- **Scikit-learn, Statsmodels, XGBoost, Prophet, SHAP**  
- **Streamlit** (for dashboards)  

---

## 📦 Installation
Clone this repository and install dependencies:
```bash
git clone https://github.com/YOUR-USERNAME/data-science-projects.git
cd data-science-projects
pip install -r requirements.txt
