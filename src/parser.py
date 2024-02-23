from bs4 import BeautifulSoup
from src.product import Product
from lxml import html

class TrendyolURLParser:
    """
    Parses product details specifically from Trendyol URLs.
    """

    def __init__(self, url):
        # Constructor method of the TrendyolURLParser class. Takes a Trendyol URL and provides access to relevant features.
        self.url = url
        self.product_list = []  # Create a list to store each product.

    def is_trendyol_url(self, url):
        # Check if the given URL is from Trendyol.
        return "trendyol.com" in url

    def parse(self, html_content):
        # Parse HTML content using the BeautifulSoup library.
        soup = BeautifulSoup(html_content, 'html.parser')
        parsed_html = html.fromstring(html_content)

        # Check if the URL is from Trendyol.
        if not self.is_trendyol_url(self.url):
            print("Error: This parser is only compatible with Trendyol URLs.")
            return self.product_list

        # Product Title For Trendyol
        title_tag_pr_new_br = parsed_html.xpath('//h1[@class="pr-new-br"]/span/text()')

        if title_tag_pr_new_br:
            title_tag = title_tag_pr_new_br[0].strip()
            print(f"Title: {title_tag}")
        else:
            title_tag = "Default Title"  # Set a default title
            print(f"Title: {title_tag}")

        # Product Price For Trendyol
        price_tag = parsed_html.xpath('//span[@class="FteoagkF"]/text()')
        if not price_tag:
            price_tag = parsed_html.xpath('//span[@class="prc-dsc"]/text()')
            price_tag = price_tag[0].strip()
            print(f"Price: {price_tag}")
        else:
            price_tag = price_tag[0].strip()
            print(f"Price: {price_tag}")

        # Discounted Price For Trendyol
        discounted_price_tag = soup.select_one('span.prc-org')
        discounted_price = discounted_price_tag.text.strip() if discounted_price_tag else None

        if discounted_price is not None:
            print(f"Discounted Price: {discounted_price}")

        # Product's main Image URL For Trendyol
        main_image_tag = soup.select_one('img[loading="lazy"]')
        main_image_url = main_image_tag['src'] if main_image_tag and 'src' in main_image_tag.attrs else None

        if main_image_url is not None:
            print(f"Main Image URL: {main_image_url}")

        # Product Image URLs For Trendyol
        image_tags = soup.select('img[loading="lazy"]')
        image_urls = list(set(img['src'] for img in image_tags)) if image_tags else None

        if image_urls is not None:
            print(f"Image URLs: {image_urls}")

        # Product's Rating Count For Trendyol(Not Working)
        rating_score_tag = soup.select_one('.pr-rnr-sm-p > span')
        rating_score = rating_score_tag.text.strip() if rating_score_tag else None

        if rating_score is not None:
            print(f"Rating Score: {rating_score}")

        # Product's Review Count For Trendyol(Not Working)
        review_count_tag = soup.find('span', class_='total-review-count')
        review_count = review_count_tag.text.strip() if review_count_tag else None

        if review_count is not None:
            print(f"Review Count: {review_count}")

        # Create a new Product object and add it to the product_list
        product = Product(title_tag, price_tag, discounted_price, main_image_url, image_urls, rating_score,
                          review_count)
        self.product_list.append(product)

        # No need for a return statement since the product_list is already stored in the instance variable.
        return self.product_list


class N11URLParser:
    """
    Parses product details specifically from N11 URLs.
    """

    def __init__(self, url):
        # Constructor method of the N11URLParser class. Takes an N11 URL and provides access to relevant features.
        self.url = url
        self.product_list = []  # Create a list to store each product.

    def is_n11_url(self, url):
        # Check if the given URL is from N11.
        return "n11.com" in url

    def parse(self, html_content):
        # Parse HTML content using the BeautifulSoup library.
        soup = BeautifulSoup(html_content, 'html.parser')

        # Check if the URL is from N11.
        if not self.is_n11_url(self.url):
            print("Error: This parser is only compatible with N11 URLs.")
            return self.product_list

        # Product Title For N11
        title_tag = soup.select_one('h1[class="proName"]')
        title = title_tag.text.strip() if title_tag else None
        print(f"Title: {title}")

        # Product Price using XPath For N11(Not Working)
        parsed_html = html.fromstring(html_content)
        product_price = parsed_html.xpath('//ins[@content]/text()')
        product_price = product_price[0].strip() if product_price else None

        if product_price is not None:
            print(f"Product Price: {product_price}")

        # Discounted Price For N11(Not Working)
        discounted_price_tag = soup.select_one('.priceContainer .oldPrice')
        if not discounted_price_tag:
            discounted_price_tag = soup.select_one('.oldPrice')

        discounted_price = discounted_price_tag.text.strip() if discounted_price_tag else None
        if discounted_price is not None:
            print(f"Discounted Price: {discounted_price}")

        # Product's main Image URL For N11
        main_image_tag = soup.select_one('img.lazy.unf-p-img')
        main_image_url = main_image_tag[
            'data-original'] if main_image_tag and 'data-original' in main_image_tag.attrs else None
        print(f"Main Image URL: {main_image_url}")

        # Product Image URLs For N11
        image_tags = soup.select('img[data-original]')
        image_urls = [img['data-original'] for img in image_tags] if image_tags else []
        print(f"Image URLs: {image_urls}")

        # Product's Rating Count For N11
        rating_score_tag = soup.find('strong', class_='ratingScore')
        rating_score = rating_score_tag.text.strip() if rating_score_tag else None
        print(f"Rating Score: {rating_score}")

        # Product's Review Count For N11
        review_count_tag = soup.find('span', class_='reviewNum')
        review_count = review_count_tag.text.strip() if review_count_tag else None
        print(f"Review Count: {review_count}")

        # Create a new Product object and add it to the product_list
        product = Product(title, product_price, discounted_price, main_image_url, image_urls, rating_score,
                          review_count)
        self.product_list.append(product)

        # No need for a return statement since the product_list is already stored in the instance variable.
        return self.product_list
