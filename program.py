Question 6: Use the following dataset: 

import pandas as pd 
df = pd.DataFrame({ 
'region': ['North','North','South','South','East','East','East'], 
'category': ['A','B','A','A','B','A','B'], 
'sales': [100, 150, 200, 250, 120, 90, 300], 
'discount': [5, 10, 0, 2, 3, 1, 4], 
'quantity': [10, 12, 15, 20, 8, 9, 14] 
}) 

Write a Python program to: 

1. Group the data by region and category and find the total sales of every group. 2. Find the number of records present in every group. 

3. Create a region-wise summary containing total_sales, avg_discount and max_qty using
named aggregation. 

4. Find the mean, min and max sales of every region–category pair. Answer: 

Import pandas as pd 
df = pd.DataFrame ( { 
‘region’ : [‘North’, ‘North’, ‘South’, ‘East’, ‘East’, ‘East’ ], ‘category’ : [‘A’, ‘B’, ‘A’, ‘A’, ‘B’, ‘A’, ‘B’ ], 
‘sales’ : [100, 150, 200, 250, 120, 90, 300], 
‘discount’ : [5, 10, 0, 2, 3, 1, 4], 
‘quantity’ : [10, 12, 15, 20, 8, 9, 14] 
} ) 

# 1. Total sales for every region-category group 
total_sales = df.groupby ( [‘region’, ‘category’] ) [‘sales’].sum() print(“1.Total Sales:”) 
print(total_sales) 

# 2. Number of records in every group 
record_count = df.groupby ( [ ‘region’, ‘category’] ).size() print(“\n2. Number of records :”) 
print(record_count) 

# 3. Region-wise summary using named aggregation 
summary = df.groupby(‘region’).agg( 
total_sales=(‘sales’, ‘sum’), 
avg_discount=(‘discount’, ‘mean’), 
max_qty=(‘quantity’, ‘max’) 
) 
print(“\n3. Region-wise summary:”) 
print(summary) 

# 4. Mean, minimum and maximum sales for each region-category pair 
sales_stats = df.groupby ( [‘region’, ‘category’] ) [‘sales’].agg( mean_sales=’mean’, 
min_sales=’min’, 
max_sales=’max’ 
)
print(“\n4. Sales statistics:”) 
print(sales_stats) 

Output: 

1. Total sales of every region-category group 
region category 
East A 90 
B 420 
North A 100 
B 150 
South A 450 
Name: sales, dtype: int64 

2. Number of records in every group 
region category 
East A 1 
B 2 
North A 1 
B 1 
South A 2 
dtype: int64 

3. Region-wise summary 
total_sales avg_discount max_qty 
region 
East 510 2.666667 14 
North 250 7.500000 12 
South 450 1.000000 20 

4. Mean, minimum and maximum sales of every region-category pair 
mean_sales min_sales max_sales 
region category 
East A 90.0 90 90 
B 210.0 120 300 
North A 100.0 100 100 
B 150.0 150 150 
South A 225.0 200 250

Question 7: Using the same dataset given in Question 6, write a Python program to: 1. Add a column region_avg_sales containing the average sales of the region of each row. 2. Add a column pct_contribution showing the share of each row in its region's total sales. 3. Add a column rank_region_sales that ranks the sales within each region in descending order. 
4. Keep only those regions that contain more than two records. 

Answer: 

import pandas as pd 
df = pd.DataFrame({ 
'region': ['North', 'North', 'South', 'South', 'East', 'East', 'East'], 
'category': ['A', 'B', 'A', 'A', 'B', 'A', 'B'], 
'sales': [100, 150, 200, 250, 120, 90, 300], 
'discount': [5, 10, 0, 2, 3, 1, 4], 
'quantity': [10, 12, 15, 20, 8, 9, 14] 
}) 

# 1. Add region-wise average sales 
df [‘region_avg_sales’] = df.groupby(‘region’) [‘sales’].transform(‘mean’) # 2. Add percentage contribution to regional sales 
df [‘pct_contribution’] = ( 
df [‘sales’] / df.groupby(‘region’) [‘sales’].transfrom(‘sum’) 
) * 100 

# 3. Rank sales within each region in descending order 
df [‘rank_region_sales’] = df.groupby(‘region’) [‘sales’].rank( 
ascending=False 
) 
print(“Updated DataFrame :”) 
print (df) 

#4. Keep only region containing more than two records 
result = df.groupby(‘region’).filter (lambda x: len(x) > 2) 
print(“\nRegions with more than two records :”) 
print (result)

Output: 

1-3. Updated DataFrame 
region category sales discount quantity region_avg_sales pct_contribution rank_region_sales 0 North A 100 5 10 125.0 40.000000 2.0 1 North B 150 10 12 125.0 60.000000 1.0 2 South A 200 0 15 225.0 44.444444 2.0 3 South A 250 2 20 225.0 55.555556 1.0 4 East B 120 3 8 170.0 23.529412 2.0 5 East A 90 1 9 170.0 17.647059 3.0 6 East B 300 4 14 170.0 58.823529 1.0 

4. Regions containing more than two records 
region category sales discount quantity region_avg_sales pct_contribution rank_region_sales 4 East B 120 3 8 170.0 23.529412 2.0 5 East A 90 1 9 170.0 17.647059 3.0 6 East B 300 4 14 170.0 58.823529 1.0 

Question 8: Use the following dataset: 

df = pd.DataFrame({ 
'region': ['North','North','South','South','East','East'], 
'month': ['Jan','Feb','Jan','Feb','Jan','Feb'], 
'sales': [100, 120, 200, 220, 150, 180], 
'discount': [5, 7, 3, 4, 6, 8] 
}) 

Write a Python program to: 
1. Convert the data into a wide format using pivot(), with region as the index and the months as columns. 
2. Create a pivot table of total sales along with an overall Total row and column. 3. Create a pivot table of the average discount in which the missing combinations are filled with 0. 
4. Explain in which situation pivot() fails but pivot_table() works. 

Answer: 

import pandas as pd 
df = pd.DataFrame({
'region': ['North', 'North', 'South', 'South', 'East', 'East'], 'month': ['Jan', 'Feb', 'Jan', 'Feb', 'Jan', 'Feb'], 
'sales': [100, 120, 200, 220, 150, 180], 
'discount': [5, 7, 3, 4, 6, 8] 
}) 

#1. Convert data into wide format using pivot() 
wide_format = df.pivot( 
index=’region’, 
columns=’month’, 
values=’sales 
) 
print(“1. Wide format :”, wide_format) 

#2. Pivot table of sales with row and column totals 
sales_table = pd.pivot_table( 
df, 
index=’region’, 
columns=’month’, 
values=’sales’, 
aggfunc=’sum’, 
margins=True, 
margins_name=’Total’ 
) 
print(“\n2. Total Sales Pivot Table:”, sales_table) 

#3. Pivot table of average discount, filling missing values with 0 

discount_table = pd.pivot_table 
df, 
index=’region’, 
columns=’month’, 
values=’discount’, 
aggfunc=’mean’, 
fill_value=0 
) 
print(“\n3. Average Discount Pivot Table:”) 
print(discount_table) 

Output 

1.wide format using pivot()

month Feb Jan 
region 
East 180 150 
North 120 100 
South 220 200 

2. Total sales with overall row and column 

month Feb Jan Total 
region 
East 180 150 330 
North 120 100 220 
South 220 200 420 
Total 520 450 970 

3.Average discount with missing values filled with 0 

month Feb Jan 
region 
East 8 6 
North 7 5 
South 4 3 

4. Difference between pivot() and pivot_table() 
● pivot() fails when the combination of index and column values contains duplicate entries because it cannot decide which value to place in the resulting cell. 
● pivot_table() works with duplicate entries because it can aggregate them using functions such as sum, mean, or count. 

Question 9: Explain rolling, expanding and cumulative operations in Pandas. Using the sales data of Question 8, write a Python program to create the columns rolling_mean_3, expanding_avg, cum_sum and cum_max, and explain why the first two values of the rolling mean are NaN and how min_periods=1 changes the output. 

Answer: 

In Pandas, rolling expanding, and cumulative operations are used to analze data over time or across a sequence of values. 

1. Rolling operation
The rolling () function performs calculations over a fixed-size window of observations. For example, a rolling mean with a window of 3 calculates the average of the current value and previous two values. 

2. Expanding operation 
The expanding() function performs calculations using all observations from the beginning of dataset up to the current row. For example, expending().mean() calculates the average of all seles recorded so far. 

3. Cumulative operation 
Cumulative operations calculate a running result as data progresses. For example: 
- cumsum() calculates the running total. 
- cummax() calculates the maximum value encountered so far. 
Python program 

USing the sales data from Question8: 

Import pandas as pd 
pd = pd.DataFrame ( { 
‘region’ : [‘North’, ‘North’, ‘South’, ‘South’, ‘East’, ‘East’], 
'month': ['Jan', 'Feb', 'Jan', 'Feb', 'Jan', 'Feb'], 
'sales': [100, 120, 200, 220, 150, 180], 
'discount': [5, 7, 3, 4, 6, 8] 
}) 

# 1. Rolling mean with a window of 3 
df['rolling_mean_3'] = df['sales'].rolling(window=3).mean() 
# 2. Expanding average 
df['expanding_avg'] = df['sales'].expanding().mean() 
# 3. Cumulative sum 
df['cum_sum'] = df['sales'].cumsum() 
# 4. Cumulative maximum 
df['cum_max'] = df['sales'].cummax()

print(df) 

Output: 

region month sales discount rolling_mean_3 expanding_avg cum_sum cum_max 0 North Jan 100 5 NaN 100.0 100 100 
1 North Feb 120 7 NaN 110.0 220 120 
2 South Jan 200 3 140.000000 140.0 420 200 
3 South Feb 220 4 180.000000 160.0 640 220 
4 East Jan 150 6 190.000000 158.0 790 220 
5 East Feb 180 8 183.333333 161.666667 970 220 

Why are the first two rolling mean values NaN? 

The rolling window size is 3, so Pandas requires three observations to calculate the mean by default. 
- First row : Only 1 observation is available. 
- Second row : Only 2 observations are available. 
- Third row : 3 observations are available, so the mean is (100 + 120 + 200) / 3 = 140. Therefore, the first two val;ues are NaN because there are not enough observations to fill the window. If we use : 
df [‘rolling_mean_3’] = ( 
df[‘sales’].rolling(window=3, min_periods=1).mean() 
) 

Question 10: Use the following datasets: 

import pandas as pd 
import numpy as np 
sales = pd.DataFrame({ 
'order_id': [1, 2, 3, 4, 5, 6], 
'region': ['North','South','East','North','South','East'], 
'category': ['A','B','A','B','A','B'], 
'sales': [100, 250, np.nan, 160, 200, 300], 
'quantity': [10, 20, 12, 10, 15, 14], 
'rep_id': [101, 102, 103, 101, 102, 103] 
}) 
reps = pd.DataFrame({
'rep_id': [101, 102, 103], 
'rep_name': ['Aditi', 'Rahul', 'Sneha'], 
'experience': [5, 2, 7] 
}) 

Write a single Python program to: 
1. Display the number of missing values in every column and fill the missing sales with the median. 
2. Merge sales with reps on rep_id using a left join. 
3. Create a column revenue_per_unit as sales / quantity. 
4. Create a region-wise summary containing total_sales, avg_sales and orders. 5. Create a pivot table of total sales with region as the index and category as the columns. 6. Print the name of the representative who generated the highest total sales. 
Answer: 

import pandas as pd 
import numpy as np 

# Create sales dataset 
sales = pd.DataFrame({ 
'order_id': [1, 2, 3, 4, 5, 6], 
'region': ['North', 'South', 'East', 'North', 'South', 'East'], 
'category': ['A', 'B', 'A', 'B', 'A', 'B'], 
'sales': [100, 250, np.nan, 160, 200, 300], 
'quantity': [10, 20, 12, 10, 15, 14], 
'rep_id': [101, 102, 103, 101, 102, 103] 
}) 

# Create representatives dataset 
reps = pd.DataFrame({ 
'rep_id': [101, 102, 103], 
'rep_name': ['Aditi', 'Rahul', 'Sneha'], 
'experience': [5, 2, 7] 
}) 

1 #. Display missing values and fill missing sales with median 
print(“1. Missing values :”, sales.isnull().sum()) 
sales[‘sales’] = sales[‘sales’], fillna(sales[‘sales’].median())
print(“\nSales after filling missing values :”, sales) 

#2. Merge sales with reps using a left join 
merged = pd.merge(sales, reps, on=’rep_id’, how=’left’) print(“\n2. Merged Data:”, merged) 

#3. Calculate revenue per unit 
merged [‘revenue_per_unit’] = merged[‘sales’] / merged[‘quantity’] print(“\n3. Revenue per unit :”) 
print (merged [ [‘order_id’, ‘revenue_per_unit’ ] ] ) 

#4. Region-wise summary 
summary = merged.groupby (‘region’).agg( 
total_sales=(‘sales’, ‘sum’), 
avg_sales=(‘sales’, ‘mean’), 
orders=(‘order_id’, ‘count’) 
) 
print(“\n4. Region-wise summary :”, summary) 

#5. Pivot table of total sales by region and category 
pivot = pd.pivot_table ( 
merged, 
index=’region’, 
columns=’category’, 
values=’sales’, 
aggfunc=’sum’, 
fill_value=0 
) 
print(“\n5. Total Pales Pivot Table :”, pivot) 

# 6. Representative with the highest total sales 
rep_sales = merged.groupby(‘rep_name’) [‘sales’].sum() top_rep = rep_sales.idxman() 
print(“\n6. Representative with Highest Total Sales :”, top_rep) Output :

1. Missing value in each column 
order_id 0 
region 0 
category 0 
sales 1 
quantity 0 
rep_id 0 
dtype: int64 

The median of the available sales values is 200, so the missing sales value is replaced with 200. 2. Merged data 
The left join combines sales records with representative names and experience using rep_id. 3. Revenue per unit 
The revenue_per_unit column is calculated by dividing sales by quantity. 4. Region-wise summary 

Region Total sales 
Average sales Orders 

East 500 250.00 2 North 260 130.00 2 South 450 225.00 2 5. Pivot table of total sales
Region A B 
East 200 300 
North 100 160 
South 200 250 

6. Representative with the highest total sales 

Sneha 
Sneha generated total sales of 500, which is the highest among the three representatives.
