import warnings
warnings.simplefilter('ignore')

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import numpy as np
import pandas as pd
credit = pd.read_csv('"C:/Users/91939/Downloads/credit-approval_csv - pandas.csv"')
credit
credit.describe()
# Replace "?" with NaN
credit.replace('?', np.NaN, inplace = True)
# Convert Age to numeric
credit["Age"] = pd.to_numeric(credit["Age"])
# credit_copy = credit[:,:]
#credit_copy = credit.copy()
#replace missing values with mean values of numeric columns
credit.fillna(credit.mean(), inplace=True)
def imputeWithMode(df):
    """
    Going through each columns and checking the type is object
    if it is object, impute it with most frequent value
    """
    for col in df:
        if df[col].dtypes == 'object':
            df[col] = df[col].fillna(df[col].mode().iloc[0])
imputeWithMode(credit)
credit_drop=credit
credit_drop=credit.drop(["ZipCode"],axis=1)
credit_drop
credit_drop.describe
#LabelEncoder
from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
# # Looping for each object type column
#Using label encoder to convert into numeric types
for col in credit_drop:
    if credit_drop[col].dtypes=='object':
        credit_drop[col]=LE.fit_transform(credit_drop[col])
credit_drop.head()
#HOT ENCODER
#convert to categorical data to dummy data
credit_dummies = pd.get_dummies(credit_drop, columns=[ "Married","EducationLevel", "Citizen", "DriversLicense", "Ethnicity"])
credit_dummies.head()
credit_dummies.columns
credit_dummies.info()
credit_dummies.describe()
