# MINDSITE INTERVIEW TASK

The system will take a list of product URLs as input.
Subsequently, it will expedite the data types for early parsing as specified.
Following this, upon initiation of the scanning process, it will export the collected data in various file formats.
Lastly, it can notify users by sending emails, which may also include the gathered data, attached to the email or embedded in the body.



## Used Libraries

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/): A library used for scraping data from web pages.
- [Requests](https://docs.python-requests.org/en/master/): A library for making HTTP requests.
- [asyncio](https://docs.python.org/3/library/asyncio.html): The core library for asynchronous programming.
- [pandas](https://pandas.pydata.org/): A library for data analysis and manipulation.
- [tabulate](https://pypi.org/project/tabulate/): A library for creating tables.
- [smtplib](https://docs.python.org/3/library/smtplib.html): A built-in library for sending emails using the Simple Mail Transfer Protocol.
- [re](https://docs.python.org/3/library/re.html): A built-in library for regular expressions.
- [logging](https://docs.python.org/3/library/logging.html): A built-in library for flexible event logging.
- [openpyxl](https://pypi.org/project/openpyxl/): A library for reading and writing Excel files.


## Project Structure

The project includes the following main components:

- **src/crawler.py**: Contains the Crawler class for asynchronously fetching web pages.
- **src/parser.py**: Includes URLParser classes for extracting product details from web pages.
- **src/storage.py**: Contains the StorageExporter class for storing obtained product information.
- **src/email_sender.py**: Includes the EmailSender class for handling email sending operations.
- **product.py**: Contains the `Product` class representing a product with its details.
- **logs/crawler.log**:Log file containing information about the crawling process.
  
## Usage

How to run this project :


**Example Usage:**

```bash
# Clone the repository
git clone https://github.com/your-username/your-web-scraper.git

# Navigate to the project directory
cd your-web-scraper

# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Activate the virtual environment (Unix/MacOS)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python main.py
```
# Project Overview

## Basic Requirements:

### 1. Asynchronous Handling for Reduced Response Wait Time
The project implements a concurrent approach by creating a product list, storing URLs in an array, and performing multiple data retrieval operations simultaneously.

### 2. Failure Handling Mechanism for Unresponsive or Blocked Requests
Crawler.py effectively addresses erroneous URLs and various errors, providing a robust mechanism to overcome challenges.

### 3. Logging for Consistency
The project maintains a log file (crawler.log) to record regular and consistent log information throughout the code.

### 4. Comprehensive Error Handling for Uninterrupted Runtime
Errors are handled gracefully, displaying error messages while allowing the project to continue running.

### 5. Data Export in Specified Formats
Data can be exported in JSON, XLSX, and CSV formats to ensure flexibility in data sharing and analysis.

### 6. Support for Two Specified Retailers
Two distinct classes for N11 and Trendyol have been created, enabling data parsing according to the respective retailer's structure.

### 7. Support for Two Specified File Formats
Export operations support JSON, XLSX, and CSV, providing versatility in exporting data files.

## Bonus Requirements:

### 1. Email Notification Module upon Completion
The email_sender.py module sends a notification email to the embedded email address once the data retrieval process is completed.

### 2. Attach Exported Files to Notification Email
Exported files are attached to the notification email using the email_sender.py module.

### 3. Beautifully Formatted Table in Email Body
The `send_email` method in email_sender.py has been updated, and a new method `_create_html_table` has been added to present collected data in a well-formatted HTML table within the email body.

### 4. Support for More Than Two Specified Retailers
Support for N11 and Trendyol has been extended to accommodate more than two retailers by creating classes for each retailer and parsing data accordingly.

### 5. Support for More Than Two Specified File Formats
Data export operations support JSON, CSV, and XLSX, providing a wider range of choices for file formats.

<<<<<<< HEAD

=======
>>>>>>> fad05722f8cc3f0b3535cf1b6fbab1241630f138

---

## References

**Python Documentation:**
- [Python Official Documentation](https://docs.python.org/3/)

**OpenAI GPT-3.5:**
- OpenAI. "ChatGPT. Version 3.5." 2023. OpenAI. [https://openai.com/](https://openai.com/).

**Web Crawling and Scraping:**
- TechTarget. "Crawler." [https://www.techtarget.com/whatis/definition/crawler](https://www.techtarget.com/whatis/definition/crawler)
- Analytics Vidhya. "Web Scraping with Python - Beginner to Advanced." [https://medium.com/analytics-vidhya/web-scraping-with-python-beginner-to-advanced-10daaca021f3](https://medium.com/analytics-vidhya/web-scraping-with-python-beginner-to-advanced-10daaca021f3)
- DataCamp. "Web Scraping with Python." [https://www.datacamp.com/tutorial/web-scraping-python-nlp](https://www.datacamp.com/tutorial/web-scraping-python-nlp)

**Selenium with Python:**
- Barış Teksin. "Selenium Nedir? Python ile Selenium Kullanımı." [https://www.baristeksin.com.tr/selenium-nedir-python-ile-selenium-kullanimi/](https://www.baristeksin.com.tr/selenium-nedir-python-ile-selenium-kullanimi/)

---
