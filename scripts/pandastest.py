import pandas  as pan
import numpy as num
import matplotlib.pyplot as plt

data = pan.read_csv('/Users/sammishra/Desktop/train.csv')

print(data.head(3))
print
print(data.describe())

'''
print()
print('Gender')
print(data['Gender'].value_counts())
print()
print('Loan Status')
print(data['Loan_Status'].value_counts())
'''
plt.figure(1)
data['ApplicantIncome'].hist(bins=50).plot()
plt.figure(2)
data.boxplot(column='ApplicantIncome').plot()
plt.show()
