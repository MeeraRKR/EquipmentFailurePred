# Equipment Predictive Maintenance

## Overview

---

Predictive maintenance can help companies minimize downtime, reduce repair costs, and improve operational efficiency. Developing a web application for predictive maintenance can provide users with real-time insights into equipment performance, enabling proactive maintenance, and reducing unplanned downtime.

The important business questions that are solved by employing data driven approach using machine learning models are:

- Predict whether an equipment will fail or not based.

- Identifies the type of equipment failure.

This web application is a demonstration of predictive maintenance using a synthetic dataset.  The dataset comprises of process parameters, ambient air and process temperatures, rotational speed, torque, and tool wear. 

---

## Performance metrics

---

To evaluate the performance of the ML models used in the project following metrics are used:

- Precsion, recall, and F1 score of the machine learning models.
- Responsiveness and ease of use of the web application.

---

The web application provides the following functionality:

- Users can provide the process parameters to the model and receive a prediction of whether the equipment will fail or not, and the type of failure.
- Users can view and infer the performance metrics of different machine learning models.
- Users can visualize the data and gain insights into the behavior of the equipment.
- The application should be built using Streamlit and deployed using Docker and Huggingface spaces.
- The cost of deployment should be minimal.

---

## Problem Statement

---

The problem is to develop a machine learning model that predicts equipment failures based on process parameters.

---
## Dataset
---

The dataset consists of more than 10,000 data points stored as rows with 14 features in columns. The features include process parameters such as air and process temperatures, rotational speed, torque, and tool wear. The target variable is a binary label indicating whether the equipment failed or not.

The dataset consists of 10 000 data points stored as rows with 14 features in columns

UID: unique identifier ranging from 1 to 10000

product ID: consisting of a letter L, M, or H for low (50% of all products), medium (30%) and high (20%) as

product quality variants and a variant-specific serial number

air temperature [K]: generated using a random walk process later normalized to a standard deviation of 2 K around 300 K

process temperature [K]: generated using a random walk process normalized to a standard deviation of 1 K, added to the air temperature plus 10 K.

rotational speed [rpm]: calculated from a power of 2860 W, overlaid with a normally distributed noise

torque [Nm]: torque values are normally distributed around 40 Nm

tool wear [min]: The quality variants H/M/L add 5/3/2 minutes of tool wear to the used tool in the process. and a 'machine failure' label that indicates, whether the machine has failed in this particular datapoint for any of the following failure modes are true.


---
## ML models
---
We will utilize both a binary classification model, and a multi-class classification model to predict equipment failures, and type of equipment failure respectively. 

### Machine failure consists of five unique modes
tool wear failure (TWF): the tool will be replaced of fail at a randomly selected tool wear time between 200 to 240 mins. At this point in time, the tool is replaced 69 times, and fails 51 times (randomly assigned).

heat dissipation failure (HDF): heat dissipation causes a process failure, if the difference between air- and process temperature is below 8.6 K and the tool's rotational speed is below 1380 rpm. This is the case for 115 data points.

power failure (PWF): the product of torque and rotational speed (in rad/s) equals the power required for the process. If this power is below 3500 W or above 9000 W, the process fails, which is the case 95 times in our dataset.

overstrain failure (OSF): if the product of tool wear and torque exceeds 11,000 minNm for the L product variant (12,000 M, 13,000 H), the process fails due to overstrain. This is true for 98 datapoints.

random failures (RNF): each process has a chance of 0,1 % to fail regardless of its process parameters. This is the case for only 5 datapoints, less than could be expected for 10,000 datapoints in our dataset.

If at least one of the above failure modes is true, the process fails and the 'machine failure' label is set to 1. It is therefore not transparent to the machine learning method, which of the failure modes has caused the process to fail

The following machine learning models will be used:

- Random Forest
- Decision Tree
- Logistic Regression
- Support Vector Machine (SVM)
---
## Generic steps
---
- Data preprocessing and cleaning
- Feature engineering and selection
- Model selection and training
- Hyperparameter tuning
- Model evaluation and testing
---
## Architecture
---
The web application architecture will consist of the following components:

- A frontend web application built using Streamlit
- A machine learning model for equipment failure prediction
- Docker containers to run the frontend, backend, and model
- Cloud infrastructure to host the application
- CI/CD pipeline using GitHub Actions for automated deployment

The frontend will interact with the backend server through API calls to request predictions, model training, and data storage. The backend server will manage user authentication, data storage, and model training. The machine learning model will be trained and deployed using Docker containers. The application will be hosted on Huggingface sppaces. The CI/CD pipeline will be used to automate the deployment process.

---

## Mlops practices

---

This project is designed to create an end-to-end workflow for developing and deploying a web application that performs data preprocessing, model training, model evaluation, and prediction. The pipeline leverages Docker containers for encapsulating code, artifacts, and both the frontend and backend components of the application. The application is deployed on a huggingface space to provide a cloud hosting solution.

---
