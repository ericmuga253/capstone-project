scraper = __import__('scraper')

job_database = __import__('job').Job_table

db = job_database(host = 'localhost', user = 'root', password = 'password', database_name = 'job_listing_db')

db.create_database()
db.check_database()

job_list = scraper.url_to_soup('https://www.brightermonday.co.ke/jobs/accounting-auditing-finance')

db.insert_into_database(job_list)
db.print_database()