import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix,accuracy_score, mean_squared_error,r2_score
import time
from clearml import Task,Logger, Dataset

"""
RESOURCES
-------------------
- https://prog.world/clearml-tutorial/

"""

#Initialize clear ml
task = Task.init(project_name="diabetes-prediction",
                 task_name="logistic_regression_training_with_full_artifacts",
                 tags=['diabetes_pred_base'])

#read data
df = pd.read_csv("diabetes.csv")

X = df.drop("Outcome",axis=1)
y= df["Outcome"] #We will predict Outcome(diabetes)

# split test and train data
X_train = X.iloc[:600]
X_test = X.iloc[600:]
y_train = y[:600]
y_test = y[600:]

task.upload_artifact(name="data.train", artifact_object=X_train)
task.upload_artifact(name="data.test", artifact_object=X_test)

#create dataset in clearml
dataset = Dataset.create(
    dataset_name="diabetes_dataset",
    dataset_project="diabetes"
)
dataset.add_files(path="diabetes.csv")

#-----------------------------------------------------

#clearml
task.upload_artifact(name="diabetes_raw_data", artifact_object="diabetes.csv")

task.upload_artifact(
    name="eda.describe.number",
    artifact_object=df.describe(include=np.number))
#-----------------------------------------------------

#train model
solver = "liblinear"
random_state = 42
task.connect({'solver': solver, 'random_state': random_state})

log = Logger.current_logger()

logistic_regression = LogisticRegression(random_state=random_state,solver=solver).fit(X_train,y_train)

# evaluate model performance
y_pred = logistic_regression.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='micro')
recall = recall_score(y_test, y_pred, average='micro')
metrics = {'accuracy': round(accuracy, 2), 'precision': round(precision, 2), 'recall': round(recall, 2)}
task.upload_artifact(name="model_metrics", artifact_object=metrics)
log.report_single_value(name="recall", value=recall)

#  Get model weights
coefficients = logistic_regression.coef_
intercept = logistic_regression.intercept_
model_weights = {'coefficients': coefficients, 'intercept': intercept}
task.upload_artifact(name="model_weights", artifact_object=model_weights)

"""
#config file
config_file_yaml = task.connect_configuration(
    name="yaml file",
    configuration="config.yaml"
)
"""

# Visualizing model
#sns.scatterplot(x=df['BloodPressure'], y=df['DiabetesPedigreeFunction'], hue=y, palette="deep")
#plt.title('Scatterplot')
#plt.savefig('scatter.png')
#task.upload_artifact(name="scatter", artifact_object='scatter.png')

#save model
#logistic_regression.save_model('my_model.cbm')

task.close()