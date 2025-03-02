import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
file_path = r"/Users/allakhverdiagakishiev/Desktop/hw/project /prediction with ml/morg-2014-emp.csv"
initial_dataset = pd.read_csv(file_path, low_memory=False)

# Filter dataset based on occ2012
filtered_df = initial_dataset[((initial_dataset['occ2012'] >= 2600) & (initial_dataset['occ2012'] <= 2920)) | 
                              (initial_dataset['occ2012'].isin([500, 40]))]

# Remove rows with NaN values in key columns
filtered_df = filtered_df.dropna(subset=['earnwke', 'uhours'])

# Create a new variable 'earn/h' for earnings per hour
filtered_df = filtered_df.copy()
filtered_df['earn/h'] = filtered_df['earnwke'] / filtered_df['uhours']

# Binarize sex and unionmme variables
filtered_df['sex'] = (filtered_df['sex'] == 2).astype(int)  # 1 → 0 (male), 2 → 1 (female)
filtered_df['unionmme'] = (filtered_df['unionmme'] == "Yes").astype(int)  # "Yes" → 1, "No" → 0

# Dummy encode only the required categorical variables
dummy_vars = ['race', 'marital', 'class', 'prcitshp']
filtered_df = pd.get_dummies(filtered_df, columns=dummy_vars, drop_first=True)

# Convert boolean variables to int
filtered_df = filtered_df.astype({col: int for col in filtered_df.select_dtypes('bool').columns})

# Check if there are non-numeric variables after encoding
print("Data types after encoding:")
print(filtered_df.dtypes)

# Define target variable
y = filtered_df['earn/h']

# Define predictors for each model
predictors = {
    "Model 1": ['age'],
    "Model 2": ['age', 'sex', 'race_2', 'race_3', 'race_4'],
    "Model 3": ['age', 'sex', 'race_2', 'race_3', 'race_4', 'marital_2', 'marital_3', 'marital_4', 'unionmme'],
    "Model 4": ['age', 'sex', 'race_2', 'race_3', 'race_4', 'marital_2', 'marital_3', 'marital_4', 
                'unionmme', 'class_Government - Local', 'class_Government - State',
                'class_Private, For Profit', 'class_Private, Nonprofit', 
                'prcitshp_Foreign Born, US Cit By Naturalization', 'prcitshp_Native, Born Abroad Of US Parent(s)', 
                'prcitshp_Native, Born In US', 'prcitshp_Native, Born in PR or US Outlying Area']
}

# Dictionary to store results
model_results = {}

# Train models and calculate metrics
for model_name, predictor_vars in predictors.items():
    print(f"Creating {model_name}...")

    # Prepare X
    X = filtered_df[predictor_vars]
    
    # Count number of predictor variables (grouping dummies as one)
    num_predictors = len(set([var.split('_')[0] for var in predictor_vars]))

    # Print data types to ensure all are numeric
    print(f"Checking data types for {model_name}:")
    print(X.dtypes)

    # Keep only numeric columns
    X = X.select_dtypes(include=[np.number])

    # Ensure all data is numeric
    assert X.dtypes.nunique() == 1, f"Error: Non-numeric data in {model_name}"

    # Fit OLS model
    model = sm.OLS(y, X).fit()

    # Compute RMSE on full sample
    y_pred = model.predict(X)
    rmse_full_sample = np.sqrt(mean_squared_error(y, y_pred))

    # Compute R-squared
    r_squared = model.rsquared

    # Cross-validation (5-fold)
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    rmse_cv_list = []

    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        model_cv = sm.OLS(y_train, X_train).fit()
        y_pred_cv = model_cv.predict(X_test)
        rmse_cv_list.append(np.sqrt(mean_squared_error(y_test, y_pred_cv)))

    rmse_cv = np.mean(rmse_cv_list)

    # BIC
    bic = model.bic

    # Store results
    model_results[model_name] = {
        "rmse_full_sample": rmse_full_sample,
        "rmse_cv": rmse_cv,
        "bic": bic,
        "r_squared": r_squared,
        "num_predictors": num_predictors
    }

# Display results
df_results = pd.DataFrame(model_results).T
print(df_results)

# Plot RMSE and BIC for comparison
models = list(model_results.keys())
rmse_full_sample = df_results["rmse_full_sample"].tolist()
rmse_cv = df_results["rmse_cv"].tolist()
bic = df_results["bic"].tolist()

# RMSE Plot
plt.figure(figsize=(10, 5))
plt.plot(models, rmse_full_sample, marker='o', linestyle='-', label="RMSE (Full Sample)")
plt.plot(models, rmse_cv, marker='s', linestyle='--', label="RMSE (Cross-Validation)")
plt.xlabel("Models")
plt.ylabel("RMSE")
plt.title("Comparison of RMSE for Different Models")
plt.legend()
plt.grid(True)
plt.show()

# BIC Plot
plt.figure(figsize=(10, 5))
plt.plot(models, bic, marker='o', linestyle='-', color='red', label="BIC")
plt.xlabel("Models")
plt.ylabel("BIC")
plt.title("Comparison of BIC for Different Models")
plt.legend()
plt.grid(True)
plt.show()
