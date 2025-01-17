"""
Программа создает словарь
числовой код валюты - буквенный код валюты
словарь выводится в виде списка кортежей
(ключ, значение)
"""
import xml.dom.minidom


xml_file = open('currency.xml')
xml_data = xml_file.read()

dom = xml.dom.minidom.parseString(xml_data)
dom.normalize()

currencies = dom.getElementsByTagName('Valute')
currency_dict = {}
for currency in currencies:
    name = ''
    number = ''
    for attribute in currency.childNodes:
        if attribute.tagName == "CharCode":
            name = attribute.firstChild.data
        if attribute.tagName == "NumCode":
            number = attribute.firstChild.data
    currency_dict[number] = name
currency_dict_list = []
for i in currency_dict:
    currency_dict_list.append((i, currency_dict[i]))
print(*currency_dict_list)
xml_file.close()