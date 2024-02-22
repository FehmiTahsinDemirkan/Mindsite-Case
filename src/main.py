import asyncio
from src import parser
from src.storage import StorageExporter
from src.email_sender import EmailSender
from src.crawler import Crawler


async def main():
    all_products = []
    crawler_instance = Crawler()

    while True:
        urls = input("Enter the URLs separated by commas: ")
        url_list = [url.strip() for url in urls.split(',')]

        for url in url_list:
            html_content = await crawler_instance.fetch(url)
            print(f"\nProduct Details for URL: {url}\n")

            if html_content:
                if "trendyol.com" in url:
                    url_parser = parser.TrendyolURLParser(url)
                elif "n11.com" in url:
                    url_parser = parser.N11URLParser(url)
                else:
                    print("Error: Unsupported URL format.")
                    continue

                product_list = url_parser.parse(html_content)
                all_products.extend(product_list)

        user_decision = input("\nDo you want to continue? (y/n): ")
        if user_decision.lower() != 'y':
            user_email = input("Enter the recipient's email address: ")
            break

    StorageExporter.export_json(all_products, 'output.json', append=True)
    StorageExporter.export_csv(all_products, 'output.csv', append=True)
    StorageExporter.export_excel(all_products, 'output.xlsx', append=True)

    email_sender = EmailSender(sender_email="dfehmitahsin@gmail.com",
                               sender_password="flko lpqg kzdn tioq",
                               smtp_server="smtp.gmail.com",
                               smtp_port=587)

    # Crawl işlemi başarıyla tamamlandığında kullanıcıya bilgi veren mail gönderme
    await email_sender.send_crawl_success_email(receiver_email="fehmitahsindemirkan@gmail.com")

    # Export işlemi sonucunda kullanıcının girdiği mail adresine dosyaları gönderen mail gönderme
    await email_sender.send_exported_data_email(receiver_email=user_email, product_data=all_products,
                                                attachments=['output.json', 'output.csv', 'output.xlsx'])


if __name__ == "__main__":
    asyncio.run(main())
