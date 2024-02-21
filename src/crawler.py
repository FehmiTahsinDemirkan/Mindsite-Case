# crawler.py

import aiohttp
import re  # regex kütüphanesini ekleyin

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
        print("Invalid URL: URL cannot be empty.")
        return False

    # Basit bir HTTP URL kontrolü yapalım
    if not re.match(r'^https?://', url):
        print(f"Invalid URL: Please enter a valid HTTP or HTTPS URL. Invalid URL: {url}")
        return False

    return True


async def fetch(url):
    """
    Fetches the HTML content of the given URL using aiohttp.
    Parameters:
    - url (str): The URL to fetch.
    Returns:
    - str: The HTML content of the page.
    """
    while True:
        if not await check_url(url):
            url = input("Enter a valid URL: ")
            continue

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    # HTTP yanıtını kontrol et
                    response.raise_for_status()

                    # HTML içeriğini döndür
                    return await response.text()

            except aiohttp.ClientError as e:
                # İstekle ilgili bir hata olması durumunda işlemleri burada ele alabilirsiniz
                print(f"Error fetching {url}: {e}")

                # 403 hatası durumunda programın devam etmesi için uyarı verebilirsiniz
                if '403' in str(e):
                    print("Forbidden (403) error. Program will continue.")
                    return None

                # Diğer hata durumlarını durdurabilir veya başka bir işlem yapabilirsiniz
                raise
