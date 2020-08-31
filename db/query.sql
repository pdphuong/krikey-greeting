-- Get 10 authors ordered by their DoB
SELECT 
    id, name, date_of_birth
FROM authors
ORDER BY date_of_birth
LIMIT 10;

-- Select total sale of author(s??) named Lorelai Gilmore"

SELECT 
    a.id as author_id, SUM(s.item_price * s.quantity) AS total_sale
FROM 
    authors AS a INNER JOIN books AS b ON a.id = b.author_id
    INNER JOIN sale_items AS s on b.id = s.book_id
GROUP BY a.id
HAVING a.name = "Lorelai Gilmore";


-- Select top 10 authors order by their sales revenue
SELECT 
    a.id as author_id, a.name, SUM(s.item_price * s.quantity) AS total_sale
FROM 
    authors AS a INNER JOIN books AS b ON a.id = b.author_id
    INNER JOIN sale_items AS s on b.id = s.book_id
GROUP BY a.id
ORDER BY  total_sale DESC 
LIMIT 10;

