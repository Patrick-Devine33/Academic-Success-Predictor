import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import KFold, GridSearchCV, cross_val_score
# from sklearn.metrics import accuracy_score

# Read in and seperate data
prep_data = pd.read_csv('data/df_vif_cleaned.csv')
y = prep_data['result_pass'].astype(int)
X = prep_data.drop(['result_pass', 'goout', 'paid', 'Pstatus_T',
                    'famsize_LE3', 'sex_M', 'romantic', 'traveltime',
                    'health', 'absences', 'schoolsup', 'famsup', 'activities',
                    'nursery', 'Dalc', 'Mjob_other', 'Fjob_other'], axis=1)
X.columns = X.columns.astype(str)

# Define our classifier
classifier = svm.SVC()

# Define hyperparameter grid
param_grid = [
    {'kernel': ['linear'], 'C': [0.1, 1, 10]},
    {'kernel': ['rbf'], 'C': [0.1, 1, 10], 'gamma': ['scale', 'auto']},
    {'kernel': ['poly'], 'C': [0.1, 1, 10], 'gamma': ['scale', 'auto'],
     'degree': [2, 3, 4]}
    ]

# Set up KFold and grid search
kfold = KFold(5, shuffle=True, random_state=42)

grid_search = GridSearchCV(classifier, param_grid, cv=kfold,
                           scoring='accuracy')

print('Starting grid search to optimise hyperparams')
grid_search.fit(X, y)

best_params = grid_search.best_params_
print(f'best hyperparameters: {best_params}')

best_svm = grid_search.best_estimator_

# Calculate accuracy scores
scores = cross_val_score(best_svm, X, y, cv=kfold, scoring='accuracy')

average_acc = np.mean(scores)

print(f"Accuracy Score for each fold: {[round(score, 4) for score in scores]}")
print(f"Average accuracy across 5 folds: {average_acc:.2f}")


'''
for i, (train_index, test_index) in enumerate(kfold.split(X, y)):
    print(f'fold {i}')
    X_test, y_test = X.iloc[test_index], y.iloc[test_index]
    X_train, y_train = X.iloc[train_index], y.iloc[train_index]

    best_svm.fit(X_train, y_train)
    y_test = np.asarray(y_test)
    y_pred = best_svm.predict(X_test)
    misclass = np.where(y_test != y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    print(accuracy)
    print(X_test.iloc[misclass])
    print(y_test[misclass])
'''

# studytime, failures, internet, Walc?, address?, guardian
