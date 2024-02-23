# storage.py

import json
import csv
import pandas as pd
from typing import List
import os

from src.product import Product


class StorageExporter:
    @staticmethod
    def export_json(data: List['Product'], filename: str, append: bool = False):
        # Export data to a JSON file.
        mode = 'a' if append else 'w'
        try:
            with open(filename, mode, encoding='utf-8') as file:
                if append and os.path.getsize(filename) > 0:
                    file.write(',')
                json.dump(data, file, ensure_ascii=False, indent=4, default=StorageExporter.serialize_product)
                file.write('\n')
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

    @staticmethod
    def export_csv(data: List['Product'], filename: str, append: bool = False):
        # Export data to a CSV file.
        mode = 'a' if append else 'w'
        keys = data[0].__dict__.keys() if data else []
        try:
            with open(filename, mode, newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                if not append:
                    writer.writeheader()
                for product in data:
                    writer.writerow(product.__dict__)
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

    @staticmethod
    def export_excel(data: List['Product'], filename: str, append: bool = False):
        # Export data to an Excel file using Pandas.
        mode = 'a' if append else 'w'
        try:
            if append and os.path.exists(filename):
                with pd.ExcelWriter(filename, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                    df = pd.DataFrame([product.__dict__ for product in data])
                    df.to_excel(writer, index=False, header=False)
            else:
                with pd.ExcelWriter(filename, engine='openpyxl', mode='w') as writer:
                    df = pd.DataFrame([product.__dict__ for product in data])
                    df.to_excel(writer, index=False)
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

    @staticmethod
    def serialize_product(obj):
        # Custom serialization method to convert Product objects to a dictionary.
        if isinstance(obj, Product):
            return obj.__dict__
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

# TODO output işlemlerini tarihine göre kayıt edip her işlem için uniq dosyalar oluştur
