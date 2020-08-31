CREATE TABLE IF NOT EXISTS authors (
    id serial PRIMARY KEY,
    name text,
    date_of_birth timestamp
);

CREATE TABLE books (
    id serial PRIMARY KEY,
    author_id integer REFERENCES authors (id),
    isbn text,
    price money
);

CREATE TABLE sale_items (
    id serial PRIMARY KEY,
    book_id integer REFERENCES books (id),
    customer_name text,
    item_price money,
    quantity integer
);

.mode csv 
.import authors.csv authors
.import books.csv books
.import sale_items.csv sale_items
