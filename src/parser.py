from bs4 import BeautifulSoup
from src.product import Product


class URLParser:
    """
    Parses product details from a given URL.
    """

    def __init__(self, url):
        # URLParser sınıfının kurucu metodudur. Bir URL alır ve ilgili özelliklere erişim sağlar.
        self.url = url
        self.product_list = []  # Her bir ürünü depolamak için bir liste oluşturulur.

    def parse(self, html_content):
        """
        Parses product details from HTML content.

        Parameters:
        - html_content (str): HTML content of the page.

        Returns:
        - list: List of Product objects.
        """
        # HTML içeriğini BeautifulSoup kütüphanesi ile parse et
        soup = BeautifulSoup(html_content, 'html.parser')

        # Product Title
        title_tag = soup.select_one('h1[class="pr-new-br"] span')
        title = title_tag.text.strip() if title_tag else None
        print(f"Title: {title}")

        # Product Price
        price_tag = soup.select_one('span.prc-dsc')
        price = price_tag.text.strip() if price_tag else None
        print(f"Price: {price}")

        # Discounted Price
        discounted_price_tag = soup.select_one('span.prc-org')
        discounted_price = discounted_price_tag.text.strip() if discounted_price_tag else None
        print(f"Discounted Price: {discounted_price}")

        # Product's main Image URL
        main_image_tag = soup.select_one('img[loading="lazy"]')
        main_image_url = main_image_tag['src'] if main_image_tag else None
        print(f"Main Image URL: {main_image_url}")

        # Product Image URLs
        image_tags = soup.select('img[loading="lazy"]')
        image_urls = [img['src'] for img in image_tags]
        print(f"Image URLs: {image_urls}")

        # Product's Rating Count
        rating_score_tag = soup.find('div', class_='rating-line-count')
        rating_score = rating_score_tag.text.strip() if rating_score_tag else None
        print(f"Rating Score: {rating_score}")

        # Product's Review Count
        review_count_tag = soup.find('span', class_='total-review-count')
        review_count = review_count_tag.text.strip() if review_count_tag else None
        print(f"Review Count: {review_count}")

        # Yeni bir Product nesnesi oluşturup product_list'e ekleyin
        product = Product(title, price, discounted_price, main_image_url, image_urls, rating_score, review_count)
        self.product_list.append(product)

        return self.product_list
