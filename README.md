# Job Listing Scraper and Database Storage
![Screenshot 2025-02-27 133651](https://github.com/user-attachments/assets/100a8ccb-b362-4fcc-92e9-f083eb9f59be)

## Project Overview
This project is designed to scrape job listings from **BrighterMonday Kenya** and store them in a **MySQL database**. It automates the process of extracting job-related information such as job titles, company names, locations, job types, and salary details. The data is then stored in a structured format within a MySQL database for easy retrieval and analysis.

## Features
- **Web Scraping:** Uses `BeautifulSoup` and `requests` to extract job details from the website.
- **MySQL Database Integration:** Stores job listings in a MySQL database for structured access.
- **Automated Data Insertion:** Parses and inserts job postings into the database dynamically.
- **Error Handling & Logging:** Implements exception handling to manage missing data and connection issues.
- **Data Retrieval & Display:** Fetches and prints stored job data for validation.

## Technologies Used
- **Python** (Primary scripting language)
- **BeautifulSoup** (For web scraping)
- **Requests** (For sending HTTP requests)
- **MySQLdb** (For database interaction)

## Installation & Setup

### 1. Install Required Libraries
Ensure you have Python installed, then install dependencies using:
```sh
pip install beautifulsoup4 requests mysqlclient
```

### 2. Set Up MySQL Database
Create a MySQL database and update the credentials in the script:
```sql
CREATE DATABASE job_listing_db;
```
Modify the script to include your MySQL host, user, password, and database name.

### 3. Run the Script
Execute the Python script to scrape and store job listings:
```sh
python job_scraper.py
```

## Code Structure
### `JobTable` Class
Handles database creation, insertion, and retrieval of job listings.
- `create_database()`: Initializes database and tables.
- `insert_into_database()`: Inserts scraped job data into the database.
- `print_database()`: Retrieves and displays stored jobs.

### `url_to_soup(url)` Function
- Sends a request to fetch job postings from BrighterMonday Kenya.
- Parses job details and structures them into a list of dictionaries.

### `Main Execution`
1. Initializes the database.
2. Scrapes job listings from the provided URL.
3. Inserts scraped data into the database.
4. Displays stored job postings.

## Expected Output
The script will print stored job details:
```sh
Tables found: [('job_listings',)]
(1, 'Accountant', 'ABC Ltd', 'Nairobi', 'Full-time', 'Ksh 100,000/month')
(2, 'Finance Analyst', 'XYZ Ltd', 'Mombasa', 'Part-time', 'Negotiable')
...
```

## Troubleshooting
- **No jobs found?** Ensure the website structure hasn’t changed and update selectors accordingly.
- **Database connection issues?** Check if MySQL is running and credentials are correct.

## Future Enhancements
- **Schedule Automated Scraping**: Run at set intervals to update job listings.
- **Add More Fields**: Include job descriptions and application deadlines.
- **Deploy as a Web API**: Serve job listings through a REST API.

## License
This project is licensed under the MIT License.

