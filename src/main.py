# main.py

import asyncio
from src import crawler, parser

async def main():
    while True:
        # Kullanıcıdan URL'yi al
        url = input("Enter the URL: ")

        # Web sayfasını getir
        html_content = await crawler.fetch(url)

        if html_content:
            # URL'yi parse et ve ürün detaylarını al
            url_parser = parser.URLParser(url)
            product_list = url_parser.parse(html_content)

            # Elde edilen ürün detaylarını ekrana yazdır
            for product in product_list:
                print("\nProduct Details:")
                print(f"Title: {product.title}")
                print(f"Price: {product.price}")
                print(f"Discounted Price: {product.discounted_price}")
                print(f"Main Image URL: {product.main_image_url}")
                print(f"Image URLs: {', '.join(product.image_urls)}")
                print(f"Rating Score: {product.rating_score}")
                print(f"Review Count: {product.review_count}")

        # Programı devam ettirip etmeme kararını kullanıcıya bırak
        user_decision = input("Do you want to continue? (y/n): ")
        if user_decision.lower() != 'y':
            break

if __name__ == "__main__":
    asyncio.run(main())
