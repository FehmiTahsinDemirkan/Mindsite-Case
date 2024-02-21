# main.py

import asyncio
from src import parser
from src.storage import StorageExporter
from src.email_sender import EmailSender, mail_sender
from src.crawler import Crawler


async def main():


    all_products = []  # Her bir URL için çekilen ürün listelerini birleştirmek için kullanılacak liste
    crawler_instance = Crawler()

    while True:
        # Kullanıcıdan URL'yi al
        url = input("Enter the URL: ")

        # Web sayfasını getir
        html_content = await crawler_instance.fetch(url)

        if html_content:
            # URL'yi parse et ve ürün detaylarını al
            url_parser = parser.URLParser(url)
            product_list = url_parser.parse(html_content)

            # Elde edilen ürün detaylarını genel listeye ekle
            all_products.extend(product_list)

            # Elde edilen ürün detaylarını ekrana yazdır
            #for product in product_list:
            #    print("\nProduct Details:")
            #    print(f"Title: {product.title}")
            #    print(f"Price: {product.price}")
            #    print(f"Discounted Price: {product.discounted_price}")
            #   print(f"Main Image URL: {product.main_image_url}")
            #    print(f"Image URLs: {', '.join(product.image_urls)}")
            #    print(f"Rating Score: {product.rating_score}")
            #    print(f"Review Count: {product.review_count}")

        # Programı devam ettirip etmeme kararını kullanıcıya bırak
        user_decision = input("Do you want to continue? (y/n): ")
        if user_decision.lower() != 'y':
            break

    # Ürün bilgilerini ilgili formatta dosyaya kaydet
    StorageExporter.export_json(all_products, 'output.json', append=True)
    StorageExporter.export_csv(all_products, 'output.csv', append=True)
    StorageExporter.export_excel(all_products, 'output.xlsx', append=True)

    # E-posta gönder
    await mail_sender(sender_email="dfehmitahsin@gmail.com",
                      sender_password="flko lpqg kzdn tioq",
                      smtp_server="smtp.gmail.com",
                      smtp_port=587,
                      )


if __name__ == "__main__":
    asyncio.run(main())
