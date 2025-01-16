from csv import reader
import random


def read_csvfile():
    """
    Формирование двумерного массива из csv файла books.csv
    Первая строчка не обозначает книгу, поэтому от нее избавляемся
    """
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        bookreader = reader(csvfile, delimiter=';')
        books = []
        for book in bookreader:
            books.append(book)
        books = books[1::]
        return books

def task1(books):
    """
    Функция считает количество книг,
    имеющих название длиннее 30 символов
    """
    amount = 0
    for book in books:
        if len(book[1]) > 30:
            amount += 1
    print(amount)

def task2(books):
    """
    Функция осуществляет поиск книг не дороже 200 рублей
    по автору книги
    """
    print("Введите автора")
    name = str(input())
    answer = []
    for book in books:
        if book[3] == name or book[4] == name:
            if float(book[7]) <= 200:
                answer.append(book)
    for i in answer:
        print(*i, sep =', ')

def task3(books):
    """
    Функция генерирует 20 записей из csv файла;
    формат записей - <автор>. <название> - <год поступления>
    записи помещаем в файл result_csv.txt
    """
    output = open('result_csv.txt', 'w') 
    numbers = set()
    while len(numbers) < 20:
        x = random.randint(0, 9409)
        numbers.add(x)
    for i in numbers:
        # формат даты поступления - DD.MM.YYYY HH:MM
        year = books[i][6][6:10]
        string = f"{books[i][3]}. {books[i][1]} - {year}\n"
        #print(string)
        output.write(string)
    output.close()

def additional_task1(books):
    """
    Функция выводит все теги в алфавитном порядке
    Каждый тег выводится в своей строке
    """
    tags = set()
    for i in books:
        data = i[12].split('# ')
        # удалим хештег перед первым тегом
        data[0] = data[0][1::]
        for tag in data:
            tags.add(tag)
    tags_list = list(tags)
    tags_list.sort()
    for tag in tags_list:
        print(tag)

def additional_task2(books):
    """
    Функция выводит 20 самых популярных книг
    """
    books.sort(key = lambda x: int(x[8]))
    books = books[::-1]
    for i in range(20):
        print(books[i])

def main(n, books):
    """
    Функция определяет выполняемую задачу
    """
    if n == 1:
        task1(books)
    elif n == 2:
        task2(books)
    elif n == 3:
        task3(books)
    elif n == 4:
        additional_task1(books)
    elif n == 5:
        additional_task2(books)

if __name__ == "__main__":
    books = read_csvfile()
    print("Введите номер задачи")
    n = int(input())
    main(n, books)