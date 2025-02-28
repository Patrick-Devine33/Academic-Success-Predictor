import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import KFold, GridSearchCV, cross_val_score

# Read in and seperate data
prep_data = pd.read_csv('data/df_vif_cleaned.csv')
y = prep_data['result_pass'].astype(int)
X = prep_data.drop('result_pass', axis=1)
X.columns = X.columns.astype(str)

# Define our classifier
classifier = svm.SVC()

# Define hyperparameter grid
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'poly', 'rbf'],
    'degree': [3, 6, 9],
    'gamma': ['scale', 'auto']
}

# Set up KFold
kfold = KFold(5, shuffle=True, random_state=42)
for i, (train_index, test_index) in enumerate(kfold.split(X, y)):
    print(f"Fold {i}:")
    print(f"  Train: index={train_index}")
    print(f"  Test:  index={test_index}")


grid_search = GridSearchCV(classifier, param_grid, cv=kfold, scoring='accuracy', n_jobs=-1)

grid_search.fit(X, y)

best_params = grid_search.best_params_
print(f'best hyperparameters: {best_params}')

best_svm = grid_search.best_estimator_

# Calculate accuracy scores
scores = cross_val_score(best_svm, X, y, cv=kfold, scoring='accuracy')

average_acc = np.mean(scores)

print(f"Accuracy Score for each fold: {[round(score, 4) for score in scores]}")
print(f"Average accuracy across 5 folds: {average_acc:.2f}")
