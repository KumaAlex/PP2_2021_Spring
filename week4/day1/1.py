import re
import csv

file = open("text.txt" , 'r' , encoding="utf-8")
t = file.read()

NameOfTheComPattern = r"\nФилиал.(?P<NameCom>.+)"
NameOfTheComText = re.search(NameOfTheComPattern, t).group("NameCom")

BINPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"
BINText = re.search(BINPattern, t).group("BIN")

DateAndAddressPatterns = r"\nВремя:.(?P<Date>.+)\n(?P<Address>.+)"
DateText = re.search(DateAndAddressPatterns, t).group("Date")
AddressText = re.search(DateAndAddressPatterns, t).group("Address")

ItemPattern = r"\n{1}(?P<Title>.+)\n{1}(?P<Count>.+)x(?P<UnitPrice>.+)\n{1}(?P<TotalPrice>.+)\n{1}Стоимость\n{1}.*"
ItemPat = re.compile(ItemPattern)

items = [["Название компании", "БИН", "Наименование товара", "Количество", "Цена за единицу", "Общая сумма", "Дата", "Адрес"]]

for i in re.finditer(ItemPat, t):
    items.append([NameOfTheComText, BINText, i.group("Title"), i.group("Count"), i.group("UnitPrice"), i.group("TotalPrice"), DateText, AddressText])

with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(items)

file.close()