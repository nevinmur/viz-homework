#!/usr/bin/env python3
import inline as inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import os



#Load the data as a dataframe

data = pd.read_csv("/Users/nevinmurad/Desktop/PProject/heartdisease.csv")
pd.set_option('display.width', None)

print(data.head(5))
print('Number of columns:',len(data.columns))


sns.pairplot(data, hue='currentSmoker', diag_kind='hist')
plt.savefig('/Users/nevinmurad/Desktop/PycharmProjects/viz-homework/pairplot_png', format = 'png')
plt.clf()


#Still using thee same DataFrame from the previous exercise insurance.csv
# plot the chart for charges and save it as charges_plot.png

# plt.plot(insurance["charges"])
# plt.title("Insurance Charges")
# plt.xlabel('Charges')
# plt.ylabel('$')
# plt.savefig("/Users/nevinmurad/PycharmProjects/visualization-homework/charges_plt.png", format="png")
#
# plt.clf()
#
#
# # plot the histogram for bmi and save it as bmi_hist.png and add labels
#
# plt.hist(insurance["bmi"],bins=10)
# plt.title("BMI Distribution")
# plt.xlabel('BMI')
# plt.savefig("/Users/nevinmurad/PycharmProjects/visualization-homework/bmi_hist.png", format="png")
#
# plt.clf()
#
# #plot the scatterplot for age vs charges and save it as age_charge_scatter.png and add labels
#
# plt.scatter(insurance["age"],insurance["charges"])
# plt.title("Age vs Charges")
# plt.xlabel('Age')
# plt.ylabel('Charges')
# plt.savefig("/Users/nevinmurad/PycharmProjects/visualization-homework/age_charge_scatter.png", format="png")
#
# plt.clf()
