import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.impute import SimpleImputer

data = pd.read_csv("restaurant_waiting_data.csv")
data['Alt'] = data['Alt'].map({'Y': 1, 'N': 0})
data['Bar'] = data['Bar'].map({'Y': 1, 'N': 0})
data['Hun'] = data['Hun'].map({'Y': 1, 'N': 0})
data['Price'] = data['Price'].map({'$$$': 2, '$$': 1, '$': 0})
data['Rain'] = data['Rain'].map({'Y': 1, 'N': 0})
data['Res'] = data['Res'].map({'Y': 1, 'N': 0})
data['Est'] = data['Est'].map({'0-10': 0, '10-30': 1, '30-60': 2, '>60': 3})
data['ans'] = data['ans'].map({'Y': 1, 'N': 0})

imputer = SimpleImputer(strategy='mean')
data = imputer.fit_transform(data)

X = data[:, :-1]
y = data[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

y_pred = nb_classifier.predict(X_test)
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Confusion Matrix:")
print(conf_matrix)
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 score: {f1:.2f}")
print("Classification Report:")
print(classification_rep)
