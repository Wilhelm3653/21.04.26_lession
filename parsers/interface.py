from abc import ABC, abstractmethod
from . import registry
import csv, os, json

# === Декоратор-Регистратор парсеров ===
def register_parser(format_name: str):
    def decorator(cls):
        registry[format_name.lower()] = cls
        return cls
    return decorator

# === Абстрактный парсер ===
class DocumentParser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> dict:
       pass

# === Конкретные парсеры ===
@register_parser("csv")
class CSVParser(DocumentParser):
    def parse(self, file_path: str) -> dict:
        try:
            with open(file_path, newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    print(row)
                    rows = len(row)
                print(f"CSV-файл {file_path} обработан", "кол-во строк", rows)
        except FileNotFoundError:
            print("Ошибка: файл не найден!")
        #return {'row': f"CSV-файл {file_path} обработан", "строк": 100}
    
@register_parser("json")
class JSONParser(DocumentParser):
    def parse(self, file_path: str) -> dict:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    
# === Фабрика с доп. функционалом ===
class ParserFactory:
    @classmethod
    def create_parser(cls, format_name: str) -> DocumentParser:
        format_key = format_name.lower()
        if format_key not in registry: # Проверка наличия парсера
            available = ", ".join(registry.keys())
            raise ValueError(f"Неизвестный формат '{format_name}'. Доступно: {available}")
        return registry[format_key]()
    
    @classmethod
    def get_formats(cls) -> list:
        return list(registry.keys())
    
    @classmethod
    def parse_file(cls, file_path: str, format_name: str) -> dict:
        """Удобный метод: создает парсер и сразу парсит"""
        parser = cls.create_parser(format_name)
        return parser.parse(file_path)    