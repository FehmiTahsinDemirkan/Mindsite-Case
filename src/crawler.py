# src/crawler.py
import aiohttp
import re


import os
import logging

# logs klasörünü kontrol et
log_folder = 'logs'
os.makedirs(log_folder, exist_ok=True)

# Log dosyasını yapılandırma
log_file_path = os.path.join(log_folder, 'crawler.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



class Crawler:
    @staticmethod
    async def check_url(url):
        """
        Checks if the URL is valid.

        Parameters:
        - url (str): The URL to check.

        Returns:
        - bool: True if the URL is valid, False otherwise.
        """
        # URL'nin boş olup olmadığını kontrol et
        if not url:
            logging.error("Invalid URL: URL cannot be empty.")
            return False

        # Basit bir HTTP URL kontrolü yapalım
        if not re.match(r'^https?://', url):
            logging.error(f"Invalid URL: Please enter a valid HTTP or HTTPS URL. Invalid URL: {url}")
            return False

        return True

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
                        # HTTP yanıtını kontrol et
                        response.raise_for_status()

                        # HTML içeriğini döndür
                        html_content = await response.text()
                        logging.info(f"Successfully fetched data from {url}")
                        return html_content

                except aiohttp.ClientError as e:
                    # İstekle ilgili bir hata olması durumunda işlemleri burada ele alabilirsiniz
                    logging.error(f"Error fetching {url}: {e}")

                    # 403 hatası durumunda programın devam etmesi için uyarı verebilirsiniz
                    if '403' in str(e):
                        logging.warning("Forbidden (403) error. Program will continue.")
                        return None

                    # Diğer hata durumlarını durdurabilir veya başka bir işlem yapabilirsiniz
                    raise
