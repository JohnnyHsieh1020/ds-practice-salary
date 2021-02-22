import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')
# print(df)  # 預設顯示前5筆資料

# Salary Estimate: keep the numbers only.
df['hourly'] = df['Salary Estimate'].apply(
    lambda x: 1 if 'per hour' in x.lower() else 0)  # 增加一個欄位來註記欄位「Salary Estimate」中有 "Per hour" 的資料

df = df[df['Salary Estimate'] != '-1']  # 移除欄位「Salary Estimate」中，值為 -1

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])  # 移除 ”（“後方的文字

rm_KD = salary.apply(lambda x: x.replace(
    'K', '').replace('$', ''))  # 移除 “Ｋ” 及 “＄”

rm_HR = rm_KD.apply(lambda x: x.lower().replace(
    'per hour', ''))  # 移除 “Per hour”
# 簡單統計薪水（最小、最大、平均）
df['min_salary'] = rm_HR.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = rm_HR.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary) / 2

# Company name: keep text only.
df['Company'] = df.apply(lambda x: x['Company Name']
                         if x['Rating'] < 0 else x['Company Name'][:-4], axis=1)  # 取企業名稱

# Location: keep state.
df = df[df['Location'] != 'Remote']
df = df[df['Location'] != 'United States']
df = df[df['Location'] != 'Maryland']
df = df[df['Location'] != 'New Jersey']
df = df[df['Location'] != 'Virginia']

df['job_location'] = df['Location'].apply(
    lambda x: x.split(',')[1])  # 取欄位「Location」中後兩個字元

print(df.job_location.value_counts())  # 統計 location 個數

# Founded: age of company.
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2021 - x)  # 計算企業年齡

# Job Description: Excel, R, Tableau, SQL and Python, TensorFlow etc.
df['req_python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.req_python.value_counts()

df['req_excel']= df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.req_excel.value_counts()

df['req_R']= df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.req_R.value_counts()

df['req_tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df.req_tableau.value_counts()

df['req_sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df.req_sql.value_counts()

df['req_tensorflow'] = df['Job Description'].apply(lambda x: 1 if 'tensorflow' in x.lower() else 0)
df.req_tensorflow.value_counts()

# export to CSV
df.to_csv('salary_data_cleaned.csv', index = False)
