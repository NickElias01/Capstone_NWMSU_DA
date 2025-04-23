# Colorado Energy Consumption Analysis and Modeling

![A snowy outdoor scene with a solar panel farm and wind turbine](images/pexels-pixabay-433308.jpg)

## Table of Contents

- [Colorado Energy Consumption Analysis and Modeling](#colorado-energy-consumption-analysis-and-modeling)
  - [Table of Contents](#table-of-contents)
  - [💡 About the Author](#-about-the-author)
  - [📊 Project Overview](#-project-overview)
  - [⚙️ Features](#️-features)
  - [📈 Results and Interpretation](#-results-and-interpretation)
    - [🔍 Regression Models](#-regression-models)
    - [📉 Linear Regression](#-linear-regression)
    - [🌲 Random Forest Regressor](#-random-forest-regressor)
    - [🧩 Clustering (K-Means)](#-clustering-k-means)
  - [🚀 Getting Started](#-getting-started)
    - [🧰 Prerequisites](#-prerequisites)
    - [🛠 Installation](#-installation)
  - [🧭 Next Steps](#-next-steps)
    - [For Regression Models:](#for-regression-models)
    - [For K-Means Clustering:](#for-k-means-clustering)
  - [📄 License](#-license)
  - [💬 Support](#-support)



## 💡 About the Author
Hello! I'm Nick Elias M.S., a professional Data Analyst from Denver, CO with expertise in Python, SQL, visualization, and machine learning. I specialize in uncovering actionable insights from complex datasets. Please feel free to connect with me on LinkedIn:

- **LinkedIn:** https://www.linkedin.com/in/nick-elias-84b08174/
- **GitHub:** https://github.com/NickElias01/Capstone_NWMSU_DA 

## 📊 Project Overview
This project focuses on analyzing energy consumption data at the city and county levels, building predictive models, and clustering energy profiles to uncover insights. The analysis includes statistical summaries, energy consumption trends, and machine learning models for regression and clustering.

The project leverages Python and popular data science libraries to:
- Perform statistical analysis of energy consumption data.
- Visualize energy consumption trends by sector and climate zone.
- Build and evaluate regression models (Linear Regression and Random Forest) to predict industrial electricity consumption.
- Apply K-Means clustering to group cities based on energy consumption patterns.

## ⚙️ Features

- **Statistical Analysis**: Summarizes key metrics and identifies missing data.
- **Energy Consumption Trends**: Visualizes total and average energy consumption by sector and climate zone.
- **Regression Models**: Predicts industrial electricity consumption using features like population and residential/commercial energy usage.
- **Clustering**: Groups cities into clusters based on energy consumption patterns, with evaluation using the Silhouette Score.


## 📈 Results and Interpretation

### 🔍 Regression Models

### 📉 Linear Regression
- **Mean Absolute Error (MAE):** 17,274.51  
  This means that, on average, the model's predictions for industrial electricity consumption are off by 17,274.51 MWh.
- **Mean Squared Error (MSE):** 3,238,976,130.99  
  A large value indicating significant errors in predictions.
- **R² (Coefficient of Determination):** -1.17  
  A negative R² suggests that the model performs worse than simply predicting the average value of the target variable. This indicates that Linear Regression is not capturing the relationship between the input features and the target variable effectively.

**Interpretation:**  
The Linear Regression model is not suitable for this dataset. It struggles to explain the variance in industrial electricity consumption.

### 🌲 Random Forest Regressor
- **Mean Absolute Error (MAE):** 12,797.84  
  The predictions are closer to the actual values compared to Linear Regression.
- **Mean Squared Error (MSE):** 1,627,876,745.22  
  A significantly lower value than Linear Regression, indicating better performance.
- **R² (Coefficient of Determination):** -0.09  
  Still negative but much closer to 0, suggesting that Random Forest performs slightly better than Linear Regression but still struggles to explain the data.

**Interpretation:**  
Random Forest performs better than Linear Regression but still requires improvement. Techniques like hyperparameter tuning or feature engineering could enhance its performance.

---

### 🧩 Clustering (K-Means)

- **Silhouette Score:** 0.6187  
  This score measures how well the data points fit within their assigned clusters. A score closer to 1 indicates well-formed and distinct clusters, while values above 0.5 are generally considered good.

**Interpretation:**  
The K-Means clustering model successfully grouped cities into distinct clusters based on their energy consumption patterns. This can help identify cities with similar energy profiles for targeted interventions or policy-making.

---


## 🚀 Getting Started

### 🧰 Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- `pip` for managing Python packages

### 🛠 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/NickElias01/Capstone_NWMSU_DA.git
   cd energy-analysis
   ```
2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up the environment variables
   - Copy .env.example to .env:
   ```sh
    cp .env.example .env
   ```
   - Update PROJECT_ROOT= "Project location" to your file path
     - ex: PROJECT_ROOT = C:\Documents\Capstone_NWMSU_DA


## 🧭 Next Steps

### For Regression Models:
- Investigate feature importance (e.g., using `feature_importances_` for Random Forest) to identify which features contribute most to the predictions.
- Perform feature engineering (e.g., create new features, remove irrelevant ones).
- Tune hyperparameters for Random Forest (e.g., number of trees, max depth) using `GridSearchCV` or `RandomizedSearchCV`.
- Consider trying other regression models like Gradient Boosting or XGBoost.

### For K-Means Clustering:
- Visualize the clusters to understand their characteristics.
- If the dataset has many features, consider dimensionality reduction (e.g., PCA) to improve clustering interpretability.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💬 Support

For issues and questions, please open a GitHub issue.