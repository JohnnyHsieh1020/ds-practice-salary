# ds-practice-salary

## Code and Resources Used 
**Python Version :** Python 3.7.4  
**IDE :** Spyder  

**Github :**
1. https://github.com/arapfaik/scraping-glassdoor-selenium
2. https://github.com/PlayingNumbers/ds_salary_proj

**Packages :** pandas, selenium

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
*	Removed rows without salary 
*	Parsed rating out of company text 
*	Made a new column for company state 
*	Calculate the age of company 
*	Made columns for if different skills were listed in the job description:
    * Python  
    * Excel  
    * R  
    * Tableau  
    * SQL  
    * TensorFlow  

**Reference documents or videos :** 
1. https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  
2. https://towardsdatascience.com/how-to-identify-the-most-requested-skills-on-the-data-science-job-market-with-data-science-726845ca9638
3. https://towardsdatascience.com/top-10-skills-for-a-data-scientist-in-2020-2b8e6122a742  
4. https://365datascience.com/career-advice/career-guides/5-skills-data-science-job/  
