import asyncio
from src import parser
from src.storage import StorageExporter
from src.email_sender import EmailSender
from src.crawler import Crawler


# Asynchronous main function
async def main():
    # List to store information about all products
    all_products = []

    # Create an instance of the Crawler class
    crawler_instance = Crawler()

    # Infinite loop to handle multiple URLs
    while True:
        # User input for multiple URLs separated by commas
        urls = input("Enter the URL(s) separated by commas:")
        url_list = [url.strip() for url in urls.split(',')]

        # Loop through each URL in the list
        for url in url_list:
            # Fetch HTML content for the current URL using the Crawler
            html_content = await crawler_instance.fetch(url)
            print(f"\nProduct Details for URL: {url}\n")

            # Check if HTML content is retrieved successfully
            if html_content:
                # Determine the parser based on the URL format (Trendyol or N11)
                if "trendyol.com" in url:
                    url_parser = parser.TrendyolURLParser(url)
                elif "n11.com" in url:
                    url_parser = parser.N11URLParser(url)
                else:
                    print("Error: Unsupported URL format.")
                    continue

                # Parse the HTML content and get product details
                product_list = url_parser.parse(html_content)
                all_products.extend(product_list)

        # Ask the user if they want to continue entering URLs
        user_decision = input("\nDo you want to continue? (y/n): ")
        if user_decision.lower() != 'y':
            # If user decides to stop, prompt for the recipient's email address
            user_email = input("Enter the recipient's email address: ")
            break

    # Export product information to different file formats (JSON, CSV, Excel)
    StorageExporter.export_json(all_products, 'output.json', append=True)
    StorageExporter.export_csv(all_products, 'output.csv', append=True)
    StorageExporter.export_excel(all_products, 'output.xlsx', append=True)

    # Create an instance of the EmailSender class with SMTP details
    email_sender = EmailSender(sender_email="dfehmitahsin@gmail.com",
                               sender_password="flko lpqg kzdn tioq",
                               smtp_server="smtp.gmail.com",
                               smtp_port=587)

    # Send an email to notify the user when the crawl process is successfully completed
    await email_sender.send_crawl_success_email(receiver_email="fehmitahsindemirkan@gmail.com")

    # Send an email with exported data to the user's provided email address
    await email_sender.send_exported_data_email(receiver_email=user_email, product_data=all_products,
                                                attachments=['output.json', 'output.csv', 'output.xlsx'])


# Run the asynchronous main function when the script is executed
if __name__ == "__main__":
    asyncio.run(main())
