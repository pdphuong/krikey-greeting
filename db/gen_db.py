import csv

authors = [
    ('01', 'Alice', '1981-01-01'),
    ('02', 'Bob', '1982-02-02'),
    ('03', 'Charlie', '1983-03-03'),
    ('04', 'Donald', '1984-04-04'),
    ('05', 'Eugene', '1985-05-05'),
    ('06', 'Frank', '1986-06-06'),
    ('07', 'George', '1987-07-07'),
    ('08', 'Henry', '1988-08-08'),
    ('09', 'Irene', '1989-09-09'),
    ('10', 'Jack', '1990-10-10'),
    ('11', 'Kevin', '1991-11-11'),
    ('12', 'Lena', '1992-12-12'),
    ('13', 'Lorelai Gilmore', '1993-12-13')
    ]


def write_author_csv(file_name, authors):

    with open(file_name,'w') as f:

        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'date_of_birth'])

        writer.writerows(authors)

def generate_books(authors):

    books = []

    for author_id, author_name, dob in authors:

        num_books = int(author_id)

        books.extend([(len(books) + i, author_id, f'{author_id}-{i}',len(author_name) * 100 ) 
                        for i in range(num_books)]
                    )

    return books

def write_books_csv(file_name, books):

    with open(file_name, 'w') as f:

        writer = csv.writer(f)
        writer.writerow(['id', 'author_id', 'isbn', 'price'])
        writer.writerows(books)

def generate_sale_items(books):
    
    sale_items = []

    for book_id, author_id, isbn, price in books:

        number_sale = len(isbn) // 2

        sale_items.extend(
            [(len(sale_items) + i, book_id, f'Cust{i}', price, number_sale) for i in range(number_sale)]
        )

    return sale_items

def write_sale_items_csv(file_name, sale_items):

    with open(file_name, 'w') as f:

        writer = csv.writer(f)
        writer.writerow(['id','book_id', 'customer_name', 'item_price', 'quantity'])
        writer.writerows(sale_items)
    


if __name__ == '__main__':
    
    authors = authors
    books = generate_books(authors)
    sale_items = generate_sale_items(books)

    write_author_csv('authors.csv', authors)    
    write_books_csv('books.csv', books)
    write_sale_items_csv('sales.csv', sale_items)

