
from bs4 import BeautifulSoup
import requests

def url_to_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    container = soup.find_all('div', class_='flex-1 flex items-center justify-between px-4 py-3 rounded-tr-md w-full pr-4 rounded-t1-md px-4')
    job_list = []

    for i in container:
        try:
            job_title = i.find('p', class_='text-lg font-medium break-words text-link-500').text.strip()
            company = i.find('a', class_='text-loading-animate text-loading-animate-link').text.strip()
            job_details_container =i.find('div', class_='flex flex-wrap mt-3 text-sm text-gray-500 md:py-0')
            location = job_details_container.find_all('span', class_='mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide')[0].text.strip()
            job_type = job_details_container.find_all('span', class_='mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide')[1].text.strip()
            salary = job_details_container.find_all('span', class_='mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide')[2].text.strip()

            # print("company:", company)
            # print("job title:", job_title)
            # print("location:", location)
            # print("job type:", job_type)
            # print("salary:", salary)
            # print("\n")

            job_info = {
                "job_title": job_title,
                "company": company,
                "location": location,
                "job_type": job_type,
                "salary": salary,
            }

            job_list.append(job_info)
        except:
            pass
    return job_list



result = url_to_soup("https://www.brightermonday.co.ke/jobs/accounting-auditing-finance")
# print(result)
print(len(result))