import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=software-developer&where=remote&stpage=1&page=1'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# card sections are stored in this container
results = soup.find(id='ResultsContainer')

# each card section contains a job (or an ad)
job_elems = results.find_all('section', class_='card-content')

# defines total card sections (includes adds)
total = len(job_elems)

ads = 0
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    date_elem = job_elem.find('time')
    try:
        link = job_elem.find('a')['href']
    except:
        pass
    # if it doesn't have one of these sections it is an ad
    if None in (title_elem, company_elem, location_elem, date_elem, link):
        ads += 1
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print(date_elem.text.strip())
    try:
        print(f"Apply here:{link}\n")
    except:
        pass
    print()

print('%s jobs found' % (total-ads))
# print('{0} jobs found and {1} ads found'.format(total - ads, ads))
