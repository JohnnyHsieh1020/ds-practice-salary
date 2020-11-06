import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')
# print(df)  # 預設顯示前5筆資料

# Salary Estimate: keep the numbers only.
df['hourly'] = df['Salary Estimate'].apply(
    lambda x: 1 if 'per hour' in x.lower() else 0)

df['employer_provided'] = df['Salary Estimate'].apply(
    lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']  # 移除欄位「Salary Estimate」中，值為 -1

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])  # 移除 ”（“後方的文字

rm_KD = salary.apply(lambda x: x.replace(
    'K', '').replace('$', ''))  # 移除 “Ｋ” 及 “＄”
print(salary)
# Job Description: python etc.

# Company name: keep text only.

# Location: keep state.

# Founded: age of company.
