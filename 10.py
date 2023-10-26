import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target


threshold = 150
y_binary = (y > threshold).astype(int)


X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)


weak_learner = DecisionTreeClassifier(max_depth=1)


adaboost_classifier = AdaBoostClassifier(base_estimator=weak_learner, n_estimators=50, random_state=42)


adaboost_classifier.fit(X_train, y_train)


y_pred = adaboost_classifier.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


sample_size = 10
X_sample = X_test[:sample_size]
y_sample_actual = y_test[:sample_size]
y_sample_pred = y_pred[:sample_size]

plt.figure(figsize=(10, 6))
plt.title("Actual vs. Predicted Diabetes Classification")
plt.xlabel("Sample Index")
plt.ylabel("Diabetes Classification")
plt.scatter(range(sample_size), y_sample_actual, color="blue", label="Actual", marker="o")
plt.scatter(range(sample_size), y_sample_pred, color="red", label="Predicted", marker="x")
plt.legend()
plt.show()
