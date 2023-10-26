from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

csv_file_path = 'restaurant_waiting_data.csv'
examples_df = pd.read_csv(csv_file_path)
columns_to_encode = ['Alt', 'Bar', 'Hun', 'Price', 'Rain', 'Res', 'Est']
examples_df_encoded = pd.get_dummies(examples_df, columns=columns_to_encode)
X = examples_df_encoded.drop('ans', axis=1)
y = examples_df_encoded['ans']

clf = DecisionTreeClassifier()
clf.fit(X, y)

feature_names = X.columns.tolist()
plt.figure(figsize=(14, 10))
plot_tree(clf,
          feature_names=feature_names,
          class_names=['Not Going', 'Going'],
          filled=False,
          rounded=False,
          fontsize=10,
          impurity=False,  # Add a comma here
          node_ids=False,
          proportion=False,
          precision=2,
          max_depth=None)

plt.title("Decision Tree Visualization")
plt.show()
