#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

train_df = pd.read_csv(r"C:\Users\it\Downloads\train.csv")
test_df = pd.read_csv(r"C:\Users\it\Downloads\test.csv")

def eda(data):
    print("Data Overview:\n")
    print(data.info())
    print("\nData Summary Statistics:\n")
    print(data.describe())

    sns.countplot(x='Survived', data=data)
    plt.title('Survival Counts')
    plt.show()


    sns.countplot(x='Survived', hue='Sex', data=data)
    plt.title('Survival Counts by Gender')
    plt.show()

    sns.histplot(data['Age'].dropna(), kde=True, bins=30)
    plt.title('Age Distribution')
    plt.show()

eda(train_df)

print("Missing Values in Training Data:")
print(train_df.isnull().sum())
X = train_df.drop(columns=['Survived', 'PassengerId', 'Name', 'Ticket', 'Cabin'])
y = train_df['Survived']

numeric_features = ['Age', 'SibSp', 'Parch', 'Fare']
categorical_features = ['Sex', 'Embarked']

# Preprocessing pipeline for numeric and categorical features
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', LabelEncoder())
])

# Combine the preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Full pipeline with classifier (Random Forest)
rf_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)


rf_pipeline.fit(X_train, y_train)


y_pred = rf_pipeline.predict(X_val)

print(f"Validation Accuracy: {accuracy_score(y_val, y_pred) * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_val, y_pred))

conf_matrix = confusion_matrix(y_val, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

# Hyperparameter Tuning with GridSearchCV
param_grid = {
    'classifier__n_estimators': [100, 200, 300],
    'classifier__max_depth': [None, 10, 20, 30],
    'classifier__min_samples_split': [2, 5, 10],
    'classifier__min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(rf_pipeline, param_grid, cv=3, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

print("Best Parameters from GridSearchCV:")
print(grid_search.best_params_)

best_rf_pipeline = grid_search.best_estimator_
y_pred_tuned = best_rf_pipeline.predict(X_val)
print(f"Tuned Model Validation Accuracy: {accuracy_score(y_val, y_pred_tuned) * 100:.2f}%")

# Prepare the test dataset
X_test = test_df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])

test_predictions = best_rf_pipeline.predict(X_test)

output = pd.DataFrame({'PassengerId': test_df['PassengerId'], 'Survived': test_predictions})

output.to_csv('submission.csv', index=False)
print("Predictions saved to 'submission.csv'")


# In[ ]:




