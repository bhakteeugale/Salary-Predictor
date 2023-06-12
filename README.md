# Salary-Predictor

## **Problem Statement**
&nbsp; &nbsp; Design salary predictor which predicts salary based on various parameters such as country, years of experience, etc.

## **Requirements**
- should be able to accept parameters such as country, years of experience, job title
- should be able to predict salary based on these parameters
- should be able to display various types of charts such as pie chart, line graph, histogram based on data used


## **Introduction**
- **Tittle**: Salary Prediction Model
- Used Linear Regressor and  Decision Tree Regressor To Predict The Salary

## **Theory**
- **Linear Regression**: Linear Regression is a machine learning algorithm based on supervised learning. It performs a regression task. Regression models a target prediction value based on independent variables 

- **Decision Tree Regressor**: It's used to solve regression problems.Decision tree builds regression  models in the form of a tree structure

- **Summary**: Dataset mentioned is used for predicting salary. First we created a regressor model and saved it in a pickle file. We used that pickle file to predict salary. We also visualized the data in the form of piechart, line graph and bar graph. For frontend we used streamlit which is used for machine learning.
 

## **Data Set Information** 
1. Data set used: StackOverflow survey 2021
2. Parameters considered while predicting salary: country, educational qualification, years of experience.

## **Technologies used**
1. Python libraries - `pickle`, `pandas`, `matplotlib`, `sklearn`
2. `streamlit` for front end

# Conclusion: 
1. Two types of regression models used for predicting salary out of which decision tree regressor gave minimum error so decision tree regressor is used.
2. Since linear regressor gave significantly larger error compared to Decision tree regressor, latter is implemented in machine learning project to predict salary using python.
