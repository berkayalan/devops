import pandas as pd
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import joblib

df = pd.read_csv("https://raw.githubusercontent.com/berkayalan/datasets/main/diabetes.csv")

X = df.drop("Outcome",axis=1)
y= df["Outcome"] #We will predict Outcome(diabetes)

X_train = X.iloc[:600]
X_test = X.iloc[600:]
y_train = y[:600]
y_test = y[600:]

xgb_classifier = XGBClassifier().fit(X_train,y_train)

y_pred = xgb_classifier.predict(X_test)
print(accuracy_score(y_test,y_pred))

# Save Model
joblib.dump(xgb_classifier, "diabetes_xgboost.pkl")