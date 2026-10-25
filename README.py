
import pandas as pd
import matplotlib.pyplot as plt
import io

# Synthetic dataset: Chronic Disease Risk Factors
data = """Patient_ID,Age,BMI,Blood_Pressure,Fasting_Sugar,Outcome
C001,45,28.5,120,95,Healthy
C002,62,32.1,145,126,Diabetic
C003,50,29.0,135,105,Pre-diabetic
C004,38,22.4,115,88,Healthy
C005,71,35.2,150,140,Diabetic
C006,55,30.5,128,110,Pre-diabetic"""

# Load the data into a DataFrame
df_chronic = pd.read_csv(io.StringIO(data))

print("Chronic Disease Dataset:")
print(df_chronic)
# Sort the patients into groups by 'Outcome', then calculate the mean for each group
group_averages = df_chronic.groupby('Outcome').mean(numeric_only=True)

print("\nAverage Clinical Markers by Patient Group:")
print(group_averages)
# Create a scatter plot comparing BMI and Blood Pressure
df_chronic.plot(kind='scatter', x='BMI', y='Blood_Pressure', color='blue', title='BMI vs. Blood Pressure')

# Command Colab to display the generated chart
plt.show()
# Calculate the correlation between all numeric columns
correlation_data = df_chronic.corr(numeric_only=True)

print("\nCorrelation Matrix:")
print(correlation_data)
# Filter the dataset for patients with Fasting_Sugar strictly greater than 125
high_sugar_patients = df_chronic[df_chronic['Fasting_Sugar'] > 125]

print("\nPatients with Fasting Sugar > 125:")
print(high_sugar_patients)
# Create a histogram to see the age distribution, split into 3 ranges (bins)
df_chronic['Age'].plot(kind='hist', bins=3, color='green', edgecolor='black', title='Patient Age Distribution')

# Display the chart
plt.show()
