import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.impute import SimpleImputer
from joblib import dump

# Load the dataset
data1 = pd.read_csv("GW_data.csv")
sm_data =pd.read_csv("sm_TN.csv")

# Convert class labels to integers
merged_data["Class"] = merged_data["Class"].map({"S": 1, "A": 0, "C": 2, "O": 3})

# Split the dataset into train, validation, and test sets
train, valid, test = np.split(data.sample(frac=1), [int(0.6 * len(data)), int(0.8 * len(data))])

# Scale data
scaler = StandardScaler()

# Select only the numeric columns for scaling
numeric_columns = train.select_dtypes(include=np.number).columns.drop(["Class"])
train_numeric = train[numeric_columns]
valid_numeric = valid[numeric_columns]
test_numeric = test[numeric_columns]

# Fit scaler on training data and transform training, validation, and test data
train_scaled = scaler.fit_transform(train_numeric)
valid_scaled = scaler.transform(valid_numeric)
test_scaled = scaler.transform(test_numeric)

# Handle missing values using an imputer
imputer = SimpleImputer(strategy="mean")
train_scaled_imputed = imputer.fit_transform(train_scaled)
valid_scaled_imputed = imputer.transform(valid_scaled)
test_scaled_imputed = imputer.transform(test_scaled)

# Oversample training data
ros = RandomOverSampler()
train_resampled, y_train_resampled = ros.fit_resample(train_scaled_imputed, train["Class"])

gnb = GaussianNB()
gnb.fit(train_resampled, y_train_resampled)

# Predict on test set
y_pred = gnb.predict(test_scaled)

# Print classification report
print(classification_report(test["Class"], y_pred))


dump(gnb, '1model.joblib')
dump(scaler,'scaler.joblib')
dump(imputer, 'imputer.joblib')
