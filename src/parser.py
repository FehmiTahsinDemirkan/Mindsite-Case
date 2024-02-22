from bs4 import BeautifulSoup
from src.product import Product
from lxml import html
import time

class TrendyolURLParser:
    """
    Parses product details specifically from Trendyol URLs.
    """

    def __init__(self, url):
        # TrendyolURLParser sınıfının kurucu metodudur. Bir Trendyol URL alır ve ilgili özelliklere erişim sağlar.
        self.url = url
        self.product_list = []  # Her bir ürünü depolamak için bir liste oluşturulur.

    def is_trendyol_url(self, url):
        # Trendyol URL kontrolü
        return "trendyol.com" in url

    def parse(self, html_content):

        print(html_content)
        # HTML içeriğini BeautifulSoup kütüphanesi ile parse et
        soup = BeautifulSoup(html_content, 'html.parser')
        parsed_html = html.fromstring(html_content)

        # Trendyol URL kontrolü
        if not self.is_trendyol_url(self.url):
            print("Error: This parser is only compatible with Trendyol URLs.")
            return self.product_list


        # Product Title
        title_tag = parsed_html.xpath('//h1[@class="pr-new-br"]/span/text()') #[0].strip()
        if not title_tag:
            title_tag = parsed_html.xpath('//h1[@class="zLHJIGKJ"]/span/text()') #[0].strip()
            if not title_tag:
                title_tag = "ikisi de değil"
        if title_tag is not str:
            title_tag = title_tag[0].strip()


        #title = title_tag.text.strip() if title_tag else None
        print(f"Title: {title_tag}")



        # Product Price
        price_tag = parsed_html.xpath('//span[@class="prc-dsc"]/text()')
        if price_tag is None:
            price_tag = parsed_html.xpath('//span[@class="FteoagkF"]/text()')
            if price_tag is None:
                price_tag = "ikisi de değil"
        if price_tag is not str:
            price_tag = price_tag[0].strip()

            #price = price_tag.text.strip() if price_tag else None
        print(f"Price: {price_tag}")

        # Discounted Price
        discounted_price_tag = soup.select_one('span.prc-org')
        discounted_price = discounted_price_tag.text.strip() if discounted_price_tag else None
        print(f"Discounted Price: {discounted_price}")

        # Product's main Image URL
        main_image_tag = soup.select_one('img[loading="eager"]')
        main_image_url = main_image_tag['src'] if main_image_tag and 'src' in main_image_tag.attrs else None
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
        product = Product(title_tag, price_tag, discounted_price, main_image_url, image_urls, rating_score, review_count)
        self.product_list.append(product)

        # Herhangi bir return ifadesine gerek yok, çünkü product_list instance variable'ında zaten tutuluyor.
        return self.product_list
class N11URLParser:
    """
    Parses product details specifically from N11 URLs.
    """

    def __init__(self, url):
        # N11URLParser sınıfının kurucu metodudur. Bir N11 URL alır ve ilgili özelliklere erişim sağlar.
        self.url = url
        self.product_list = []  # Her bir ürünü depolamak için bir liste oluşturulur.

    def is_n11_url(self, url):
        # N11 URL kontrolü
        return "n11.com" in url

    def parse(self, html_content):
        # HTML içeriğini BeautifulSoup kütüphanesi ile parse et
        soup = BeautifulSoup(html_content, 'html.parser')

        # N11 URL kontrolü
        if not self.is_n11_url(self.url):
            print("Error: This parser is only compatible with N11 URLs.")
            return self.product_list

        # Product Title
        title_tag = soup.select_one('h1[class="proName"]')
        title = title_tag.text.strip() if title_tag else None
        print(f"Title: {title}")

        # Product Price
        product_price_tag = soup.select_one('.newPrice ins')
        product_price = product_price_tag['content'] if product_price_tag else None
        print(f"Product Price: {product_price}")

        # Discounted Price
        discounted_price_tag = soup.select_one('.oldPrice')
        discounted_price = discounted_price_tag.text.strip() if discounted_price_tag else None
        print(f"Discounted Price: {discounted_price}")

        # Product's main Image URL
        main_image_tag = soup.select_one('img.lazy.unf-p-img')
        main_image_url = main_image_tag[
            'data-original'] if main_image_tag and 'data-original' in main_image_tag.attrs else None
        print(f"Main Image URL: {main_image_url}")

        # Product Image URLs
        image_tags = soup.select('img[data-original]')
        image_urls = [img['data-original'] for img in image_tags] if image_tags else []
        print(f"Image URLs: {image_urls}")

        # Product's Rating Count
        rating_score_tag = soup.find('strong', class_='ratingScore')
        rating_score = rating_score_tag.text.strip() if rating_score_tag else None
        print(f"Rating Score: {rating_score}")

        # Product's Review Count
        review_count_tag = soup.find('span', class_='reviewNum')
        review_count = review_count_tag.text.strip() if review_count_tag else None
        print(f"Review Count: {review_count}")

        # Yeni bir Product nesnesi oluşturup product_list'e ekleyin
        product = Product(title, product_price, discounted_price, main_image_url, image_urls, rating_score, review_count)
        self.product_list.append(product)

        # Herhangi bir return ifadesine gerek yok, çünkü product_list instance variable'ında zaten tutuluyor.
        return self.product_list