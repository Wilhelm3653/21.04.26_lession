from .interface import  ParserFactory

# Получаем и используем парсер
prs = ParserFactory.create_parser('csv')
res = prs.parse('./files/data1.csv')
print(res)

# Получаем список доступных парсеров
print(ParserFactory.get_formats())

# Парсим указанный файл
print(ParserFactory.parse_file('./files/data.csv','csv'))