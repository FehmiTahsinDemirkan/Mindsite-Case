# Product.py

class Product:
    """
    Represents a product with its details.
    """

    def __init__(self, title, price, discounted_price, main_image_url, image_urls, rating_score, review_count):
        # Constructor method to initialize a Product instance with its details.
        # Parameters:
        #   - title: The title of the product.
        #   - price: The original price of the product.
        #   - discounted_price: The discounted price of the product.
        #   - main_image_url: The URL of the main image associated with the product.
        #   - image_urls: A list of URLs for additional images related to the product.
        #   - rating_score: The score representing the product's rating.
        #   - review_count: The count of reviews for the product.
        self.title = title
        self.price = price
        self.discounted_price = discounted_price
        self.main_image_url = main_image_url
        self.image_urls = image_urls
        self.rating_score = rating_score
        self.review_count = review_count
