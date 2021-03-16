# DS_salary_estimate_project   
*  By estimating data science salaries to help data scientist know how much income does this position give.
*  Collected 500 job descriptions from glassdoor using python and selenium.

## Code and Resources Used 
**Python Version :** Python 3.7.4  
**IDE :** Spyder, Jupyter Notebook

**Packages :** pandas, numpy, sklearn, matplotlib, seaborn, dataframe_image, selenium

**Github :**
1. https://github.com/arapfaik/scraping-glassdoor-selenium
2. https://github.com/PlayingNumbers/ds_salary_proj

**Reference documents or videos :** 
1. https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  
2. https://towardsdatascience.com/how-to-identify-the-most-requested-skills-on-the-data-science-job-market-with-data-science-726845ca9638
3. https://towardsdatascience.com/top-10-skills-for-a-data-scientist-in-2020-2b8e6122a742  
4. https://365datascience.com/career-advice/career-guides/5-skills-data-science-job/  
5. https://medium.com/analytics-vidhya/python-exploratory-data-analysis-eda-on-nyc-airbnb-cbeabd622e30  
6. https://medium.com/@PatHuang/%E5%88%9D%E5%AD%B8python%E6%89%8B%E8%A8%98-3-%E8%B3%87%E6%96%99%E5%89%8D%E8%99%95%E7%90%86-label-encoding-one-hot-encoding-85c983d63f87  

## Data Collection 
Collect 500 job postings from glassdoor.com. With each job, we got the following:
*	Job Title
*	Salary Estimate
*	Job Description
*	Rating
*	Company Name
*	Location
*	Headquarters 
*	Size
*	Founded
*	Type of Ownership 
*	Industry
*	Sector
*	Revenue
*	Competitors 

## Data Cleaning
Clean the data up so that it was usable for our model. I made the following changes and created the following variables:
*	Parsed numeric data out of "Salary Estimate" 
*	Made columns for hourly wages 
*	Removed rows without salary and remove rows with "Remote", "United States" in Location column
*	Parsed rating out of company text 
*	Made a new column for company's location 
*	Calculate the age of company 
*	Made columns for if different skills were listed in the job description:
    * Python  
    * Excel  
    * Git  
    * Tableau  
    * SQL  
    * TensorFlow  
    * Power BI  

## Exploratory Data Analysis (EDA)
Below are a few tables and graphs I made. Try to find out the connections and relations in this dataset. 

**Correlations :**      
![image](https://github.com/JohnnyHsieh1020/ds-practice-salary/blob/main/Correlations.png)

**Job by location :**      
![image](https://github.com/JohnnyHsieh1020/ds-practice-salary/blob/main/job_by_location.png)

**Salary by job position :**      
![image](https://github.com/JohnnyHsieh1020/ds-practice-salary/blob/main/salary_by_job_postion.png)

**DS salary by location :**      
![image](https://github.com/JohnnyHsieh1020/ds-practice-salary/blob/main/ds_salary_by_location.png)

**Word Cloud :**  
<img src="https://github.com/JohnnyHsieh1020/ds-practice-salary/blob/main/wordcloud.png" width="200">

## Model Building
1. By using LabelEncoder. It can transform data into a value between 0 and n_classes-1.
2. I split the data in a 80–20 ratio.
3. I used three different models and evaluated them using Mean Absolute Error(MAE).
    * Linear Regression  
    * Lasso Regression  
    * Random Forest
    
## Model performance
The Lasso Regression model has the best performance.   
*	Linear Regression: MAE = 27.03  
*	Lasso Regression: MAE = 26.11
*	Random Forest : MAE = 31.48