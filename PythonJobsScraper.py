import requests
from bs4 import BeautifulSoup

URL = 'https://www.python.org/jobs/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_="list-recent-jobs list-row-container menu")

##print(results.prettify())

job_elems = results.find_all('li')
print("%s jobs found\n" %len(job_elems))

for job_elem in job_elems:
    unwanted = job_elem.find('span', class_='listing-new')
    unwanted.extract()
    comp_elem = job_elem.find('span', class_='listing-company-name')
    date_elem = job_elem.find('span', class_='listing-posted')
    if None in (date_elem, comp_elem):
        continue
    print(comp_elem.text.strip())
    print(date_elem.text.strip())
    print()