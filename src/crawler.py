# src/crawler.py
import aiohttp
import re

import os
import logging

# Check the 'logs' folder
log_folder = 'logs'
os.makedirs(log_folder, exist_ok=True)

# Configure the log file
log_file_path = os.path.join(log_folder, 'crawler.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Crawler:
    # Fetch the HTML content of the given URL.
    @staticmethod
    async def fetch(url):
        """
        Fetches the HTML content of the given URL using aiohttp.
        Parameters:
        - url (str): The URL to fetch.
        Returns:
        - str: The HTML content of the page.
        """
        while True:
            if not await Crawler.check_url(url):
                url = input("Enter a valid URL: ")
                continue

            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get(url) as response:
                        # Check the HTTP response; open a log entry if there is a timeout
                        response.raise_for_status()
                        logging.warning(f"The HTTP response timed out: {url}")

                        # Return the HTML content; open a log entry if successful
                        html_content = await response.text()
                        logging.info(f"Successfully fetched data from {url}")
                        print("Successfully fetched the data ")
                        return html_content

                except aiohttp.ClientError as e:
                    # Handle operations in case of an error related to the request
                    logging.error(f"Error fetching {url}: {e}")
                    print("An error occurred while fetching")

                    # Provide a warning and continue if it's a 403 error
                    if '403' in str(e):
                        logging.warning("Forbidden (403) error. Program will continue.")
                        print("The program did not work; error code: Forbidden (403) error.")
                        return None

                    # You can stop for other error situations or perform another action
                    logging.exception("An unexpected error occurred.")
                    print("An unexpected error occurred.")
                    raise

    # Check if the given URL is valid.
    @staticmethod
    async def check_url(url):
        """
        Checks if the URL is valid.

        Parameters:
        - url (str): The URL to check.

        Returns:
        - bool: True if the URL is valid, False otherwise.
        """
        # Check if the URL is empty
        if not url:
            logging.error("Invalid URL: URL cannot be empty.")
            print("Invalid URL: URL cannot be empty.")
            return False

        # Perform a simple check for an HTTP URL
        if not re.match(r'^https?://', url):
            logging.error(f"Invalid URL: Please enter a valid HTTP or HTTPS URL. Invalid URL: {url}")
            return False

        return True
