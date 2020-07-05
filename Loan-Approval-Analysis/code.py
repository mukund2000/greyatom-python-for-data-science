# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
#check type of variables in our dataset
bank_data = pd.read_csv(path)
categorical_var=bank_data.select_dtypes(include = 'object')
numerical_var=bank_data.select_dtypes(include = 'number')
print(categorical_var.shape,numerical_var.shape)

# remove missing values
banks=bank_data.drop(['Loan_ID'],axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode()
# print(bank_mode)
banks.fillna(bank_mode.iloc[0],inplace=True)
print(banks.shape)
print(banks.isnull().sum().values.sum())

# avg loan amount of person
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount['LoanAmount'][1])

loan_approved_se=banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')]
loan_approved_nse=banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')]
percentage_se=(len(loan_approved_se)/614)*100
percentage_nse=(len(loan_approved_nse)/614)*100
print(percentage_nse,percentage_se)

loan_term=banks['Loan_Amount_Term'].apply(lambda x:int(x)/12)
big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)

loan_groupby=banks.groupby(['Loan_Status'])[['ApplicantIncome', 'Credit_History']]
mean_values=loan_groupby.agg([np.mean])
print(mean_values)
#Code starts here




