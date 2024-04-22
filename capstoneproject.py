import MySQLdb
from bs4 import BeautifulSoup
import requests

class Job_table():

    def __init__(self, host = '', user = '', password = '', database_name = ''):
        if (host != '' and user != '' and password != '' and database_name != ''):
            self.host = host
            self.user = user
            self.password = password
            self.database_name = database_name

    def create_database(self):
        db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password)
        cursor = db.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(self.database_name))
        cursor.execute('USE {}'.format(self.database_name))
        cursor.execute('CREATE TABLE IF NOT EXISTS {} (id INT PRIMARY KEY AUTO_INCREMENT, title TEXT, company TEXT,location TEXT,job_type TEXT, salary TEXT)'.format(self.database_name))
        db.close()

    def check_database(self):
        db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.database_name)
        cursor = db.cursor()
        cursor.execute('SHOW TABLES')
        tables = cursor.fetchall()
        if len(tables) == 0:
            print('No tables found')
        else:
            print('Tables found')
        db.close()


    def insert_into_database(self, list):
        db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.database_name)
        cursor = db.cursor()
        for job in list:
            cursor.execute('INSERT INTO {} (title, company, location, job_type, salary) VALUES (%s, %s, %s, %s, %s)'.format(self.database_name), 
                        (job['job_title'], job['company'], job['location'], job['job_type'], job['salary']))
        db.commit()
        db.close()

    def print_database(self):
        db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.database_name)
        cursor = db.cursor()
        cursor.execute('SELECT * FROM {}'.format(self.database_name))
        results = cursor.fetchall()
        for row in results:
            print(row)
        db.close()


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


db = Job_table(host = 'localhost', user = 'root', password = 'password', database_name = 'job_listing_db')

db.create_database()
db.check_database()

job_list = url_to_soup('https://www.brightermonday.co.ke/jobs/accounting-auditing-finance')

db.insert_into_database(job_list)
db.print_database()
