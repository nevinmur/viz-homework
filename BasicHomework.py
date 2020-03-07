import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import pytest
from pandas.tests.test_downstream import df

data = pd.read_csv("/Users/nevinmurad/Desktop/PProject/heartdisease.csv")

data.columns = ['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke',
                        'prevalentHyp', 'diabetes',
                        'totalChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose', 'TenYearCHD']

# FIG 1

plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(10, 10))

axes.scatter(data['BMI'], data['totalChol'], label='BMI vs TotalChol')
axes.scatter(data['BMI'], data['heartRate'], label='BMI vs HR')
axes.scatter(data['BMI'], data['glucose'], label='BMI vs Glucose')

axes.set_xlabel('BMI')
axes.set_ylabel('TotalChol/HR/Glucose')
axes.set_title(f'BMI compare')
axes.legend()
plt.savefig(f'/Users/nevinmurad/Desktop/PProject/fig1.png', dpi=300)

plt.close()


#Fig 2

plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(10, 10))

axes.scatter(data['TenYearCHD'], data['totalChol'], label='CHD vs TotalChol', marker='v')
axes.scatter(data['TenYearCHD'], data['heartRate'], label='CHD vs HR', marker='x')
axes.scatter(data['TenYearCHD'], data['glucose'], label='CHD vs Glucose', marker='o')

axes.set_xlabel('TenYearCHD')
axes.set_ylabel('TotalChol/HR/Glucose')
axes.set_title(f'CHD compare')
axes.legend()
plt.savefig(f'/Users/nevinmurad/Desktop/PProject/fig2.png', dpi=300)

plt.close()

# Fig 3

plt.style.use("ggplot")

fig, axes = plt.subplots(1, 1, figsize=(10, 10))

axes.scatter(data['age'], data['BPMeds'], label='BMI vs BPMeds', color="yellow")
axes.scatter(data['age'], data['diabetes'], label='BMI vs Diabetes', color='blue')
axes.scatter(data['age'], data['prevalentStroke'], label='Age vs Stroke', color="red")
axes.scatter(data['age'], data['prevalentHyp'], label='Age vs Hyp', color='green')

axes.set_xlabel('age')
axes.set_ylabel('Outcomes')
axes.set_title(f'Age compare')
axes.legend()
plt.savefig(f'/Users/nevinmurad/Desktop/PProject/fig3.png', dpi=300)

plt.close()

# Fig 4 Histogram

fig, axes = plt.subplots(1, 1, figsize=(10, 10))
axes.hist(data['diabetes'], bins=10, color='blue', label='Diabetes')
axes.hist(data['prevalentStroke'], bins=10, color='red', label='Hyper')
axes.hist(data['BPMeds'], bins=10, color='yellow', label='BPMeds')
axes.set_title('Diabetes / Stroke / BPMeds')
axes.set_xlabel('Prevalence')
axes.set_ylabel('Frequency')
axes.legend()
plt.savefig(f'/Users/nevinmurad/Desktop/PProject/fig4.png', dpi=300)
plt.close()

#Fig 5

fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.bar(np.arange(0, len(data['cigsPerDay'])), data['cigsPerDay'], color='green', label='Cigarettes')
axes.set_title('Cigarettes')
axes.set_xlabel('Patient ID')
axes.set_ylabel('Nb Cigarettes per day')
axes.legend()
plt.savefig(f'/Users/nevinmurad/Desktop/PProject/fig5.png', dpi=300)
plt.close()

#Fig 6
data['TenYearCHD'] = data['TenYearCHD'].map(lambda x: int(x))
sns.countplot(data["TenYearCHD"])
plt.title("Labels")
plt.savefig(f'/Users/nevinmurad/Desktop/PProject/fig6.png', dpi=300)
plt.close()

#Fig 7
data.hist(figsize=(20, 20))
plt.savefig(f'/Users/nevinmurad/Desktop/PProject/fig7.png', dpi=300)
plt.close()

# Fig 8

fig, axes = plt.subplots(1, 1, figsize=(10, 10))
axes.pie(data['education'].value_counts(), labels=data['education'].value_counts().index.tolist(), autopct='%1.1f%%')
axes.set_title('Education')
axes.legend()
plt.savefig(f'/Users/nevinmurad/Desktop/PProject/fig8.png', dpi=300)
plt.close()

#Fig9

# male = data[data['male'] == 1]
# female = data[data['male'] == 0]
# fig = plt.figure()
# axes = fig.add_subplot(1, 1, 1, projection='3d')
# line1 = axes.scatter(male['mean smoothness'], male['mean symmetry'], male['mean concavity'])
# line2 = axes.scatter(female['mean smoothness'], female['mean symmetry'], female['mean concavity'])
# axes.legend((line1, line2), ('Male', 'Female'))
# axes.set_xlabel('mean smoothness')
# axes.set_ylabel('mean symmetry')
# axes.set_zlabel('mean concavity')
# plt.savefig(f'/Users/nevinmurad/Desktop/PProject/fig9.png', dpi=300)
# plt.close()

#Fig10

fig, axes = plt.subplots(2, 2, figsize=(10, 5))


axes[0][0].plot(data['age'], data['heartRate'], label = 'Age vs HR', color = 'red')
axes[0][1].plot(data['BMI'], data['heartRate'], label = ' BMI vs HR', color = 'blue')
axes[1][0].plot(data['BMI'], data['sysBP'], label = " BMI vs SysBP", color = 'green')
axes[1][1].plot(data['age'], data['sysBP'], label = 'Age vs SysBP', color = "orange")


plt.tight_layout()
plt.savefig(f'/Users/nevinmurad/Desktop/PProject/fig10.png', dpi=300)
plt.close()