import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix,accuracy_score, mean_squared_error,r2_score
import time
import mlflow
import mlflow.sklearn

#read data
df = pd.read_csv("diabetes.csv")

X = df.drop("Outcome",axis=1)
y= df["Outcome"] #We will predict Outcome(diabetes)

# split test and train data
X_train = X.iloc[:600]
X_test = X.iloc[600:]
y_train = y[:600]
y_test = y[600:]

#-----------------------------------------------------

#mlflow

#This line of code, when included is causing an error
#mlflow.set_tracking_uri("http://localhost:5000")

experiment_name = "diabetes_classifier"
run_name="diabetes_classifier_v0.1.0"
mlflow.set_experiment(experiment_name)

#-----------------------------------------------------

with mlflow.start_run(run_name=run_name):

    #train model
    solver = "liblinear"
    random_state = 42

    logistic_regression = LogisticRegression(random_state=random_state,solver=solver).fit(X_train,y_train)

    # Log parameters
    mlflow.log_param("solver", solver)
    mlflow.log_param("random_state", random_state)

    # evaluate model performance
    y_pred = logistic_regression.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='micro')
    recall = recall_score(y_test, y_pred, average='micro')
    metrics = {'accuracy': round(accuracy, 2), 'precision': round(precision, 2), 'recall': round(recall, 2)}

    #  Get model weights
    coefficients = logistic_regression.coef_
    intercept = logistic_regression.intercept_
    model_params = {'coefficients': coefficients, 'intercept': intercept}

    # Visualizing model
    sns.scatterplot(x=df['BloodPressure'], y=df['DiabetesPedigreeFunction'], hue=y, palette="deep")
    plt.savefig('scatter.png')
    mlflow.log_artifact('./scatter.png')

    # Log metrics
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)

    # Log model
    mlflow.sklearn.log_model(logistic_regression, "model")


"""
If we want to get all lists of experiments
experiments = mlflow.search_experiments()

If we want to get details of an experiments
mlflow.get_experiment_by_name("diabetes_classifier")

If we want to get runs of an experiments
mlflow.search_runs(experiment_names=["diabetes_classifier"])

If we want to get an artifact
download_path = "/Users/berkayalan/mlflow" #path of your computer
client.download_artifacts(run_id = run_id, path="scatter.png", dst_path = download_path)
"""