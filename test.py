from abc import ABC, abstractmethod
import csv

class DocumentParser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> dict:
        with open(file_path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

par = DocumentParser.parse("hkpfkh", './files/data.csv')

print(par)