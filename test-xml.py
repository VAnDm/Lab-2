import xml.dom.minidom as minidom


xml_file = open('books.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('book')
books_dict = {}
title = ''
price = 0

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'title':
                if child.firstChild.nodeType == 3:
                    title = child.firstChild.data
            if child.tagName == 'price':
                if child.firstChild.nodeType == 3:
                    price = float(child.firstChild.data)
    books_dict[title] = price

    if node.getAttribute('id') == 'bk104':
        print(node.getElementsByTagName('title')[0].firstChild.data)

# for key in books_dict.keys():
    # print(key, books_dict[key])

#print(title)

xml_file.close()