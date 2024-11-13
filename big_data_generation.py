import pandas as pd
import numpy as np

# Define the number of patients and years
num_patients = 10000  # Adjust this number as needed
start_year = 1900
end_year = 2019
years = list(range(start_year, end_year + 1))

# Generate patient names
patient_names = [f'Patient_{i}' for i in range(1, num_patients + 1)]

# Create a DataFrame for patients
df = pd.DataFrame({'patient': patient_names})

# Generate random weights for each patient for each year
np.random.seed(42)  # For reproducibility

# Generate weights within a realistic range, e.g., 100 to 250 pounds
weights = np.random.uniform(100, 250, size=(num_patients, len(years)))

# Round weights to one decimal place
weights = np.round(weights, 1)

# Create a DataFrame for weights
weights_df = pd.DataFrame(weights, columns=[f'weight in year {year}' for year in years])

# Combine patient names with weights
df = pd.concat([df, weights_df], axis=1)

# Save the DataFrame to a Parquet file
df.to_parquet('large_dataset.parquet', engine='pyarrow', index=False)
