
import MySQLdb

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