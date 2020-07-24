import requests
from bs4 import BeautifulSoup

URL ='https://www.glassdoor.com/Job/remote-software-developer-jobs-SRCH_IL.0,6_IS11047_KO7,25.htmpage = requests.get(URL)'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='MainColSummary')

job_elems = results.find_all('li', class_='jl react-job-listing grGrid')

for job_elem in job_elems:
    company = job_elem.find('div', class_='jobInfoItem jobEmpolyerName')
    position = job_elem.find('a', class_='jobInfoItem jobTitle jobLink')
    try:
        link = job_elem.find('a', class_='jobInfoItem jobTitle jobLink')['href']
    except:
        pass
    if None in (company, position, link):
        continue
    print(company.text.strip())
    print(position.text.strip())
    try:
        print(f"Apply here:{link}\n")
    except:
        print("no Link")

    print()
