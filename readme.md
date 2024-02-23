


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

