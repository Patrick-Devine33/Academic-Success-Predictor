# Academic-Success-Predictor

A Machine-Learning project designed to predict whether a student will pass an academic year. Comparing three different ML models: Logistic Regression, Random Forest, SVM

[Working report](https://docs.google.com/document/d/1dCHXsUZiGRWKD_ebOYLK8V84iSXU700reJE-n22-hvw/edit?usp=sharing)

## Data Management

Problem Modeling

* We model this as a binary classification task. Given structured data with discrete categorical variables, we aim to predict a binary 'pass' or 'fail' outcome for each student based on a minimum grade requirement. 
* Classification is preferred over regression due to the discrete nature of both inputs and outputs. Supervised learning is appropriate as we have labeled data. This approach allows us to directly predict the required binary labels, unlike clustering which is more suited for pattern discovery in unlabelled data.

Data Cleaning

* Remove null values and ensure consistent formatting.
* Compute 'pass/fail' labels based on a minimum grade of 12.
* Drop outliers (age <13 or >21) and remove the imbalanced 'paid' column.

Correlation Evaluation

* to be continued

Encoding

* Convert binary categories (e.g., 'yes/no', 'pass/fail') to 1/0.
* Encode categorical columns as specified in Table 1.1.

Experimental Protocol

* Use 5-fold cross-validation to mitigate over-fitting.
* Shuffle and split data into 5 groups for iterative training/testing.
* Compute average model accuracy from the 5 validation folds.

## Model Training
This project predicts whether a student will pass an academic year using machine learning, comparing three models: SVM, Random Forest, and Logistic Regression.

Hyperparameter Protocol

* GridSearchCV with 5-fold cross-validation was used to optimize model performance. If an optimal value was on the edge of tested values, further refinement was conducted.

>SVM

* Best Hyperparameters:
Kernel: poly /
C: 10 / 
Gamma: 0.01 /
Degree: 2 

* Accuracy: 74.4%

* Polynomial kernels (degrees 2 and 3) performed best, indicating non-linear relationships.

>Random Forest

* Best Hyperparameters:
Estimators: 150 / 
Max depth: 3 / 
Min split samples: 20 / 
Min leaf samples: 15 / 
Max features: log2

* Accuracy: 74.1%

* Lower max depth reduced overfitting; log2 feature selection yielded better results.

>Logistic Regression

* Best Hyperparameters:
Penalty: l2 / 
C: 0.10 / 
Solver: saga / 

* Accuracy: 74.3%

* Stronger regularization improved generalization; saga solver performed best.

Model Comparison

* SVM: 74.4% / Random Forest: 74.1% / Logistic Regression: 74.3%

Final Choice: SVM, due to highest cross-validation accuracy.

## Evaluate Models

Results:
* The testing accuracy for our final model is 80.1%. The table below contains the classification report. 

* Confusion Matrix