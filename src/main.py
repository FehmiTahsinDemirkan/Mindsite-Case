import asyncio
from src import crawler, parser
from src.storage import StorageExporter
from src.email_sender import EmailSender


async def main():
    all_products = []  # Her bir URL için çekilen ürün listelerini birleştirmek için kullanılacak liste

    while True:
        # Kullanıcıdan URL'yi al
        url = input("Enter the URL: ")

        # Web sayfasını getir
        html_content = await crawler.fetch(url)

        if html_content:
            # URL'yi parse et ve ürün detaylarını al
            url_parser = parser.URLParser(url)
            product_list = url_parser.parse(html_content)

            # Elde edilen ürün detaylarını genel listeye ekle
            all_products.extend(product_list)

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

    # Ürün bilgilerini ilgili formatta dosyaya kaydet
    StorageExporter.export_json(all_products, 'output.json', append=True)
    StorageExporter.export_csv(all_products, 'output.csv', append=True)
    StorageExporter.export_excel(all_products, 'output.xlsx', append=True)

    # Kullanıcıdan e-posta adresi al
    sender_email = "dfehmitahsin@gmail.com"
    sender_password = "flko lpqg kzdn tioq"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    receiver_email = input("Enter the recipient's email address: ")  # Kullanıcıdan alıcı e-posta adresini al

    subject = "Web Crawler Results"
    body = "Please find attached the results of the web crawler."

    # Attach files (provide the paths to your .csv, .json, .xlsx files)
    attachments = ["output.csv", "output.json", "output.xlsx"]

    email_sender = EmailSender(sender_email, sender_password, smtp_server, smtp_port)
    email_sender.send_email(receiver_email, subject, body, attachments)

    # E-posta gönder
    email_sender = EmailSender(sender_email, sender_password, smtp_server, smtp_port)
    email_sender.send_email(receiver_email, "Web Crawler Results",
                            "Please find attached the results of the web crawler.",
                            ["output.json", "output.csv", "output.xlsx"])


if __name__ == "__main__":
    asyncio.run(main())
