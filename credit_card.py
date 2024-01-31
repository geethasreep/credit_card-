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

def plotDistPlot(col):
    """Flexibly plot a univariate distribution of observation"""
    sns.distplot(col)
    plt.show()
plotDistPlot(credit_drop['Age'])
plotDistPlot(credit_drop['PriorDefault'])
plotDistPlot(credit_drop['Debt'])
plotDistPlot(credit_drop['CreditScore'])
plotDistPlot(credit_drop['BankCustomer'])
plotDistPlot(credit_drop['YearsEmployed'])
plotDistPlot(credit_drop['Income'])
plt.savefig('Distribution.jpeg')

#correlation matrix
corr = credit_drop.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
plt.savefig('corelation.jpg')

#scatterplot
sns.set()
cols = ['Age', 'Debt', 'BankCustomer','YearsEmployed','PriorDefault','CreditScore','Income']
sns.pairplot(credit_drop[cols], size = 2.5)
plt.show();
plt.savefig('scatterplot.jpg')

<html>
<body background="IMG1.jpg">
<head>
<title>Credit Card Application Form</title>
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='../static/style.css') }}">
</head>

<body style = "background: url(IMG1.jpg)">
<h3>CREDIT CARD APPLICATION FORM</h3>

<form action="{{ url_for('predict')}}" method="POST">
<table align="center" cellpadding = "10">

<!----- First Name ---------------------------------------------------------->
<tr>
<td>FIRST NAME</td>
<td><input type="text" name="First_Name" maxlength="30"/>
(max 30 characters a-z and A-Z)
</td>
</tr>

<!----- Last Name ---------------------------------------------------------->
<tr>
<td>LAST NAME</td>
<td><input type="text" name="Last_Name" maxlength="30"/>
(max 30 characters a-z and A-Z)
</td>
</tr>

<!----- Age---------------------------------------------------->
<tr>
<td>AGE</td>
<td><input type="text" name="Age" maxlength="100" /></td>
</tr>

<!----- Gender ----------------------------------------------------------->
<tr>
<td>GENDER</td>
<td>
Male <input type="radio" name="Gender" value="Male" />
Female <input type="radio" name="Gender" value="Female" />
</td>
</tr>

<!----- Total Debt ---------------------------------------------------------->
<tr>
<td>TOTAL DEBT</td>
<td>
<input type="text" name="Total_Debt" maxlength="10" />
</td>
</tr>

<!----- Existing Bank Customer ---------------------------------------------------------->
<tr>
<td>EXISTING BANK CUSTOMER</td>
<td>
<select name="Bank_Customer" id="Bank_Customer">
<option value="-1">Select</option>
<option value="1">g</option>
<option value="2">gg</option>
<option value="3">p</option>
</select>
</td>
</tr>

<!----- Employment Status ---------------------------------------------------------->
<tr>
<td>EMPLOYMENT STATUS</td>
<td>
<select name="E_Status" id="E_Status">
<option value="-1">Select</option>
<option value="1">t</option>
<option value="2">f</option>
</td>
</tr>

<!----- Income ---------------------------------------------------------->
<tr>
<td>INCOME</td>
<td><input type="text" name="Income" maxlength="30" />
</td>
</tr>

<!----- Total Experience ---------------------------------------------------------->
<tr>
<td>TOTAL EXPERIENCE <br /><br /><br /></td>
<td><input type="text" name="Tot_Experience" maxlength="10" /></td>
</tr>

<!----- Address ---------------------------------------------------------->
<tr>
<td>CREDIT SCORE<br /><br /><br /></td>
<td><input type="text" name="Credit_Score" maxlength="10" /></td>
</tr>

<!----- Education ---------------------------------------------------------->
<tr>
<td>EDUCATION LEVEL</td>
<td>
<select name="Edu_Level" id="Edu_Level">
<option value="-1">Select</option>
<option value="1">w</option>
<option value="2">q</option>
<option value="3">m</option>

<option value="4">r</option>
<option value="5">cc</option>
<option value="6">k</option>
<option value="7">c</option>
<option value="8">d</option>
<option value="9">x</option>
<option value="10">i</option>
<option value="11">e</option>
<option value="12">aa</option>
<option value="13">ff</option>
<option value="14">j</option>
</select>
</td>
</tr>

<tr>
<td>PRIOR DEFAULT</td>

<td>
<select name="Default" id="Default">
<option value="-1">Select:</option>
<option value="1">Yes</option>
<option value="2">No</option>
</select>
</td>
</tr>

<tr>
<td>MARITAL STATUS</td>
<td>
<select name="Mar_Status" id="Mar_Status">
<option value="-1">Select:</option>
<option value="1">Single</option>
<option value="2">Married</option>
<option value="3">Divorced</option>
</select>
</td>
</tr>

<tr>
<td>CANADIAN CITIZENSHIP</td>
<td>
<select name="Citizen" id="Citizen">
<option value="-1">Select:</option>
<option value="1">Yes</option>
<option value="2">No</option>
<option value="3">Cannot disclose</option>
</select>
</td>
</tr>


<tr>
<td>DRIVERS LICENCE</td>
<td>
<select name="D_Licence" id="D_Licence">
<option value="-1">Select:</option>
<option value="1">Yes</option>
<option value="2">No</option>
</select>
</td>
</tr>

<tr>
<td>ETHNICITY</td>

<td>
<select name="Ethnicity" id="Ethnicity">
<option value="-1">Select:</option>
<option value="1">v</option>
<option value="2">h</option>
<option value="3">bb</option>
<option value="4">ff</option>
<option value="5">j</option>
<option value="6">z</option>
<option value="7">o</option>
<option value="8">dd</option>
<option value="9">n</option>
</select>
</td>
</tr>

<!----- Submit and Reset ------------------------------------------------->
<tr>
<td colspan="2" align="center">
<input type="submit" value="Submit">
<input type="reset" value="Reset">
</td>
</tr>
</table>

</form>

</body>
</html>
