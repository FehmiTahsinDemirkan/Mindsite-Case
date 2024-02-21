# Product.py

class Product:
    """
    Represents a product with its details.
    """

    def __init__(self, title, price, discounted_price, main_image_url, image_urls, rating_score, review_count):
        self.title = title
        self.price = price
        self.discounted_price = discounted_price
        self.main_image_url = main_image_url
        self.image_urls = image_urls
        self.rating_score = rating_score
        self.review_count = review_count
