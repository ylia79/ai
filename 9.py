import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

data = {
    'Transaction_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Items': [
        'bread, milk, eggs',
        'bread, milk',
        'bread, butter',
        'milk, eggs',
        'bread, milk, butter',
        'milk, butter',
        'bread, eggs',
        'bread, milk, eggs',
        'bread, milk',
        'bread, milk, eggs, butter'
    ]
}

df = pd.DataFrame(data)
df['Items'] = df['Items'].str.split(', ')  
df_encoded = pd.get_dummies(df['Items'].apply(pd.Series).stack(), prefix='item').groupby(level=0).max().clip(0, 1)

min_support = 0.3  
frequent_itemsets = apriori(df_encoded, min_support=min_support, use_colnames=True)

min_confidence = 0.7  
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=min_confidence)

print(rules)
