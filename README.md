# Telco Customer Churn Prediction

An end-to-end Data Science project focused on predicting customer churn using the IBM Telco Customer Churn dataset. The project covers the main stages of a machine learning workflow, including data understanding, preprocessing, exploratory data analysis, statistical analysis, feature selection, feature engineering, model comparison, hyperparameter tuning, threshold optimization, and final model evaluation. 

The final model is a Logistic Regression pipeline selected for its competitive predictive performance, simplicity, interpretability, and suitability for production deployment. The model is exposed through a FastAPI REST API, containerized with Docker, stored in Amazon ECR, and deployed as a running service on AWS ECS/Fargate.



## Business Problem

Customer churn is a major challenge in the telecommunications industry. Identifying customers who are likely to leave can help a company target retention activities more effectively. The objective of this project is to build a machine learning model capable of estimating customer churn risk based on demographic information, subscribed services, contract characteristics, payment information, and customer tenure.


## Objectives

### Primary Objective

Develop a classification model that predicts whether a customer is likely to churn.

### Secondary Objectives

- Identify customer characteristics associated with churn.
- Perform statistical and multivariate analysis of churn-related factors.
- Build a reproducible preprocessing and machine learning pipeline.
- Compare multiple classification algorithms.
- Evaluate different feature sets and feature engineering approaches.
- Optimize model hyperparameters.
- Analyze the precision-recall trade-off and classification threshold.
- Select a model suitable for production deployment.
- Build a reusable inference layer and REST API.
- Add input validation and automated API tests.
- Containerize the application with Docker.
- Deploy the model as a cloud service on AWS.


## Project Workflow

The project is organized into several stages:

1. Data understanding
2. Data preprocessing
3. Exploratory data analysis
4. Statistical and multivariate analysis
5. Baseline model development
6. Model comparison, feature selection, and hyperparameter tuning
7. Final model selection and evaluation
8. Model serialization and inference preparation
9. REST API development with FastAPI
10. Input validation and automated testing
11. Docker containerization
12. Deployment to AWS using Amazon ECR and ECS/Fargate

## Deployment

The final model is deployed as a containerized REST API. The deployment workflow is:

```text
Trained scikit-learn pipeline
        ↓
Serialized model artifact
        ↓
FastAPI inference service
        ↓
Pydantic input validation
        ↓
Automated API tests
        ↓
Docker image
        ↓
Amazon ECR
        ↓
Amazon ECS / Fargate
        ↓
Public HTTPS endpoint
```

The deployed API exposes:

- `GET /` — service health / basic API response
- `POST /predict` — churn probability and classification
- `/docs` — automatically generated Swagger/OpenAPI documentation

## Live API

The churn prediction API is deployed on AWS ECS/Fargate and is publicly accessible.

- [API root](https://ch-298d8238ea5e43188b4e00693b316a3c.ecs.eu-north-1.on.aws/)
- [Swagger documentation](https://ch-298d8238ea5e43188b4e00693b316a3c.ecs.eu-north-1.on.aws/docs)

## Next Steps
- Add CI/CD for automated testing, Docker image builds, and deployment
- Improve cloud monitoring and logging
- Add model and data drift monitoring
- Add model versioning
- Extend the project with business-oriented churn prioritization
- Evaluate retention decisions using both churn risk and customer value

## Models Evaluated

The following models were evaluated using stratified cross-validation:

- Logistic Regression
- Random Forest
- Gradient Boosting

Despite its lower complexity, Logistic Regression achieved performance comparable to the ensemble models and was selected as the final production candidate. Gradient Boosting achieved a slightly higher cross-validated PR-AUC, but the improvement was modest relative to the additional model complexity. Logistic Regression was therefore selected because it provides competitive performance while offering substantially better interpretability and simpler deployment.


## Feature Selection and Engineering

Several feature sets were evaluated:

- Original feature set
- Reduced feature set
- Reduced feature set with engineered features

Removing several weak predictors resulted in almost no loss in predictive performance. The reduced feature set was therefore selected for the final model because it provides similar performance with fewer input variables.

Additional engineered features did not produce a meaningful improvement, suggesting that most of their predictive information was already represented in the original variables.


## Model Evaluation

Because the dataset contains an imbalanced target variable, model evaluation was based on multiple metrics:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- PR-AUC

Cross-validation was used for model comparison and hyperparameter tuning.

The classification threshold was also analyzed because the default threshold of 0.50 produced relatively low recall. A threshold of 0.35 was selected as a more recall-oriented operating point.


## Final Model

The final model is a Logistic Regression classifier using a reduced feature set and an end-to-end scikit-learn preprocessing pipeline.

Final evaluation on the held-out test set at a classification threshold of 0.35:

| Metric | Score |
|---|---:|
| Accuracy | 0.776 |
| Precision | 0.560 |
| Recall | 0.719 |
| F1-score | 0.630 |
| ROC-AUC | 0.848 |
| PR-AUC | 0.651 |

The model correctly identifies approximately 72% of actual churn customers. The increased recall comes at the cost of additional false positives, reflecting the expected precision-recall trade-off.


## Technologies

- Python
- pandas
- NumPy
- SciPy
- scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook
- FastAPI
- Pydantic
- pytest
- Docker
- Amazon ECR
- Amazon ECS / AWS Fargate
- AWS CloudWatch
- Git
- VS Code
