#create a categorical classification model using Decision Tree

# Import libraries
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Age': ['Young', 'Young', 'Middle', 'Old', 'Old', 'Old', 'Middle', 'Young'],
    'Income': ['High', 'High', 'High', 'Medium', 'Low', 'Low', 'Low', 'Medium'],
    'Student': ['No', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes'],
    'BuysCar': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No']
}

# Create DataFrame
df = pd.DataFrame(data)

# Encode categorical data into numbers
df_encoded = pd.get_dummies(df, drop_first=True)

# Split features and target
X = df_encoded.drop('BuysCar_Yes', axis=1)
y = df_encoded['BuysCar_Yes']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Build Decision Tree model
model = DecisionTreeClassifier(criterion='entropy', random_state=1)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Visualize tree
plt.figure(figsize=(10,6))
plot_tree(model, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.show()