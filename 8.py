import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
education_data = pd.read_csv('education_data.csv')
X = education_data[['GPA', 'Study_Hours']]
y = education_data['Pass']
colors = {'Yes': 'blue', 'No': 'red'}
y_colors = [colors[label] for label in y]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train, y_train)
y_pred = svm_classifier.predict(X_test)
print("Predicted labels for the test data:")
print(y_pred)
plt.figure(figsize=(10, 6))
xx, yy = np.meshgrid(np.linspace(X['GPA'].min() - 1, X['GPA'].max() + 1, 100), np.linspace(X['Study_Hours'].min() - 1, X['Study_Hours'].max() + 1, 100))
Z = svm_classifier.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, levels=[-1, 0, 1], colors=['red', 'blue'], alpha=0.5)
scatter = plt.scatter(X['GPA'], X['Study_Hours'], c=y_colors)
legend_labels = [plt.Line2D([0], [0], marker='o', color='w', label='Yes', markerfacecolor='blue', markersize=10),plt.Line2D([0], [0], marker='o', color='w', label='No', markerfacecolor='red', markersize=10)]
plt.legend(handles=legend_labels, title="Classes")
plt.xlabel('GPA')
plt.ylabel('Study Hours')
plt.title('SVM Decision Boundary with Education Dataset')
plt.show()