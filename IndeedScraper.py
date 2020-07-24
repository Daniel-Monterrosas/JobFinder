import requests
from bs4 import BeautifulSoup

URL = 'https://www.indeed.com/jobs?q=software+developer&l=remote'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="resultsCol")
job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')

for job_elem in job_elems:
    try:
        unwanted = job_elem.find('span', class_='new')
        unwanted.extract()
    except:
        print()
    title_elem = job_elem.find('h2', class_='title')
    comp_elem = job_elem.find('span', class_='company')
    remote_elem = job_elem.find('span', class_='remote')
    sal_elem = job_elem.find('div', class_='salarySnippet holisticSalary')

    print(title_elem.text.strip())
    print(comp_elem.text.strip())
    try:
        print(remote_elem.text.strip())
    except:
        print('NOT REMOTE')
    try:
        print(sal_elem.text.strip())
    except:
        print("NO SALARY INFO")
    print()
print("%s jobs found\n" %len(job_elems))