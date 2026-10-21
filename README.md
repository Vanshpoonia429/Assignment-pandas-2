# Assignment-pandas-2

Topics Covered: Data Cleaning | Missing Values | GroupBy & Aggregations | Reshaping | Rolling & Cumulative Operations | Joins and Concatenation. 

Question 1: What is data cleaning and why is it performed before analysis? Explain how missing values are identified in Pandas using isna().sum() and isna().mean(), and describe the situations in which a column should be dropped instead of being imputed. 

Answer: 

Data cleaning is the process of identifying and correcting or removing inaccurate, incomplete, duplicate, or inconsistent data from a dataset before perform analysis. It is performed to improve data quality, ensure accurate results, and make the analysis more reliable. 

Identifying Missing Values in Pandas 
In Pandas, missing values can be identified using the isna() function along with sum() and mean(). 

1. isna().sum(): Counts the number of missing values in each column of a DataFrame. df.isna().sum() 
It helps identify which columns contain missing values and how many values are missing in Each column. 

2. isna().mean() : Calculate the proportion of missing values in each column. Since missing values are represented as True and non-missing value as False, the mean gives the fraction of missing values. 
df.isna().mean() 

For example, a result of 0.25 means that 25% of the values in that column are missing. Multiplying the result by 100 gives the percentage of missing values. 
When should a column Be Dropped Instead of Imputed? 

A column should be dropped rather than imputed in the following situations: 

1. A large number of missing values: If most values in a column are missing, filling them may introduce unreliable information. 
2. Low importance: if the column is not relevant to the analysis or does not contribute useful information, it can be removed.
3. No reliable imputation method: If missing values cannot be estimated accurately using the available data, imputation may introduce bias. 
4. Redundant information: If a column duplicates information already available in another column, it may be unnecessary. 
5. Poor data quality: If may be more appropriate than attempting to repair it. 

However, column should not be dropped solely because they contain missing values. If a column is important, methods such as filling missing values with the mean, median, or mode may be more suitable. 

Question 2: Explain median imputation and mode imputation with suitable examples. Why is the median preferred for numerical columns such as age, and why is the mode used for categorical columns such as embarked? 

Answer: 

1. Median Imputation 
Median imputation is a technique used to fill missing values in a numerical column with the median (middle value) of the available val;ues. First, the values are arranged in ascending order, and the middle value is selected. 

Example: Consider an age column containing the values: 

[ 20, 25, 30, NaN, 80 ] 
The median of the available values is 30. Therefore, the missing value is replaced with 30. Python code: 
Df [‘age’] = df[‘age’].filena(df[‘age’].median()) 

Why is median preferred for age? 
- It is less affected by extreme values (outliers). 
- It provides a more representative central value when the data is skewed. 
- It helps preserve the general distribution of numerical data better than the mean in many cases. 
For example, if ages are [20, 25, 30, 35, 100], the median is 30, whereas the mean is 42. The median is less influenced by the unusually high age of 100. 

2. Mode Imputation 
Mode imputation is a technique used to fill missing values in a column with the mode, or most frequently occurring value, It is commonly used for categorical data.

Example: Consider an Embarked column containing the values: 
[‘S’, ‘C’, ‘S’, NaN, ‘S’, ‘C’] 

Here ‘S’ occurs most frequently. Therefore, the missing value is replaced with ‘S’. Python code: 

df[‘Embarked’] = df[“Embarked”].fillna( 
df[‘Embarked’].mode()[0] 
) 

Why is the mode used for categorical columns such as Emberked? 

- Categorical values represent labels or groups rather than numerical measurements. - Calculating the mean or median of categories such as ‘S’, ‘C’, and ‘Q’ is not meaningful. - The mode file missing values with the most common category. 

Question 3: What is the difference between map() and apply()? Explain with examples where each one should be used, and describe what happens when a value is missing from the dictionary passed to map(). 

Answer: 

1. Difference Between map() and apply() 
In Pandas, both map() and apply() are used to transform or process data, but they differ in their usage and functionality. 
- map() Function: 
The map() Function is mainly used to substitute or transform values in a Pandas Series using a dictionary, a function, or another Series. It is commonly used for value mapping and simple replacements. 

Example: 

import pandas as pd 
df = pd.DataFrame({ 
'Gender': ['M', 'F', 'M', 'F'] 
}) 
df['Gender'] = df['Gender'].map({
'M': 'Male', 
'F': 'Female' 
}) 
print(df) 

Output: 

Gender 
0 Male 
1 Female 
2 Male 
3 Female 

- apply () Function: 
The apply() function is used to apply a function to each element of a Series or along a specified axis of a DataFrame. It is useful for more complex operations and calculations. 

Example: 

df = pd.DataFrame({ 
'Age': [20, 25, 30] 
}) 
df['Age_Group'] = df['Age'].apply( 
lambda x: 'Adult' if x >= 18 else 'Minor' 
) 
print(df) 

Output: 

Age Age_Group 
0 20 Adult 
1 25 Adult 
2 30 Adult 

2. Key Differences 

Feature map() apply() 
Main purpose Mapping or replacing values Applying functions or calculations
Common usage Usually on a Series On a Series or DataFrame Input Dictionary, Series, or function Function 
Best suited for Simple value transformations Complex logic and calculations 3. What Happens When a Value is Missing from the Dictionary Passed to map() 
If a value in a Series is not present as a key in the dictionary passed to map() , Pandas replaces that value with NaN (a missing value). 

Example: 

df = pd.DataFrame( { 
‘Grade’ : [‘A’, ‘B’, ‘C’] 
} ) 
df[‘Grade_point’] = df[‘Grade’].map( { 
‘A’ : 4, 
‘B’ : 3 
} ) 
print(df) 

Output: 

Grade Grade_Point 
0 A 4.0 
1 B 3.0 
2 C NaN 

Here, ‘c’ is not present in the dictionary, so its mapped value becomes NaN. To avoid this, you can use fillna() to assign a default value: 
df['Grade_Point'] = df['Grade'].map({ 
'A': 4, 
'B': 3 
}).fillna(0) 

Question 4: Explain binning in Pandas. Describe the difference between pd.cut() and pd.qcut() with suitable examples, and mention one real-world situation in which each one is useful.

Answer: 

1. What is Binning in Pandas?
   
Binning is a data preprocessing technique in which continuous numerical values are divided into groups or intervals called bins. It helps convert numerical data info categorical data, making it easier to understand, analyze, and visualize. 
For example, age can be divided into categorise such as child, Teenager, Adult, Senior.

3. Difference Between pd.cut() and pd.qcut() 

A. pd.cut() 
The pd.cut() function divides data into bins based on specified numerical boundaries. The intervals are defined by the user or generated using an equal-width division of the data range. 

Example: 

Import pandas as pd 
Ages = [12, 18, 25, 35, 60] 
bins = [0, 18, 35, 60] 
labels = [‘Child’, ‘young Adult’, ‘Adult’] 
result = pd.cut(ages, bins=bins, labels=labels) 
print(result) 

Here, the age values are classified into predefined intervals. The default behaviour uses right-inclusive intervals, so the bins are approximately (0, 18], (19, 35], and (35, 60]. 
Real-world use: In healthcare pd.cut() can classify patients into predefined age groups for reporting and analysis. 

B. pd.qcut() 
The pd.qcut() function divides data into bins based on quantities. It attempts to place approximately the same number of observations in each bin. 

Example: 

Import pandas as pd
marks = [10, 20, 30, 40, 50, 60, 70, 80] 
result = pd.qcut( 
marks, 
q=4, 
labels=[‘Low’, ‘Median’, ‘High’, ‘very High’] 
) 
print(result) 

HEre, q=4 divides the data into four quartile-based groups, with approximately equal numbers of observations in each group when the quantile boundaries are distinct. 
Real-world use: In business analytics, helping identify low-, medium-, and high- spending customers.

3. Key Differences 
Feature pd.cut() pd.qcut() 
Basic Numerical intervals or boundaries Quantities or rank 
Bin sizes Can have equal width or custom widths Attempts to have equal numbers of observations 
Boundaries Usually specified by the user Calculated from the data distribution Best suited for Fixed ranges and meaningful thresholds Ranking data into similarly sized groups
Example Age groups: 0-18, 18-35, 35-60 Customers divided into four spending group 

Question 5: Explain the difference between agg(), transform() and filter() in a groupby operation. Support your answer with one example of each. 

Answer: 

In Pandas, age(), transform(), and filter() are used with groupby() to perform different operations on grouped data. 

1. agg() - Aggregation 
The agg() function calculates summary statistics, such as sum, mean, count, or maximum, for each group. It usually returns one row per group.

Example: 

import pandas as pd 
df = pd.DataFrame ( { 
‘Department’ : [‘IT’, ‘IT’, ‘HR’, ‘HR’], 
‘Salary’ : [30000, 40000, 25000, 35000] 
} ) 
result = df.groupby (‘Department’) [‘Salary’].agg(‘mean’) 

Output: 

Department 
HR 30000.0 
IT 35000.0 
Name: Salary, dtype: float64 
Here, agg() calculate the average salary for each department. 

2. transform() - Transformation 
The transform() function perform as operation on each group and return a result with the same number of rows as the original data. It is useful when we want to add group-level information to every row. 

Example: 
df [‘Average_salary’] = ( 
df.groupby(‘Department’) [‘Salary’].transform(‘mean’) 
) 
print(df) 

Output: 

Department Salary Average_Salary 
0 IT 30000 35000.0 
1 IT 40000 35000.0 
2 HR 25000 30000.0 
3 HR 35000 30000.0 

Here, transform() calculate the average salary of each department and assign it to every employee in that department.

3. filter() - Filtering groups 
The filter() function select or remove entire groups based on a specified condition. It returns the rows belonging to groups that satisfy the condition. 

Example:

result = or.groupby(‘Department’).filter( 
lambda x: x[‘Salary’].mean() > 32000 
) 
print(result)

Output: 

Department Salary Average_Salary 
0 IT 30000 35000.0 
1 IT 40000 35000.0 
Here, filter() keeps only the IT department because its average salary is greater than 32000. The HR department is removed because its average salary is 32000.
