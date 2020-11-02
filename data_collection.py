import glassdoor_scraper as gs
import pandas as pd

path = "/Users/kyounihsieh/Documents/GitHub/ds-practice-salary/chromedriver"

df = gs.get_jobs('data scientist', 500, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index=False)
