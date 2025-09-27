-- Question 1 : Write a query to display all columns from the products table.
SELECT * FROM products;

-- Question 2 : Select only the Product and Category columns from the products table.
SELECT Product, Category FROM products;

-- Question 3 : Show the Salesperson and Team from the people table.
SELECT Salesperson, Team FROM people;

-- Question 4 : Display all products where the Category is 'Bars'
SELECT * FROM products WHERE Category = 'Bars';

-- Question 5 : Find all sales where the number of Boxes is greater than 500.
SELECT * FROM sales WHERE Boxes > 500;

-- Question 6 : Show sales that happened in the GeoID = 'G1'.
SELECT * FROM sales WHERE GeoID = 'G1';

-- Question 7 : List all products ordered by Cost_per_box in ascending order.
SELECT * FROM products ORDER BY Cost_per_box ASC;

-- Question 8 : Display sales ordered by Amount in descending order.
SELECT * FROM sales ORDER BY Amount DESC;

-- Question 9 : Show salespeople ordered alphabetically by their Salesperson name.
SELECT * FROM people ORDER BY Salesperson ASC;

-- Question 10 : Write a query to display Product, and add a new column PriceLevel which says
--"High" if Cost_per_box > 5,
--"Medium" if between 2 and 5, and "Low" otherwise.
SELECT Product,
       CASE 
           WHEN Cost_per_box > 5 THEN 'High'
           WHEN Cost_per_box BETWEEN 2 AND 5 THEN 'Medium'
           ELSE 'Low'
       END AS PriceLevel
FROM products;

-- Question 11 :  For each sale, display Amount and a column SaleType that says "Big" if Amount > 10000 and "Small" otherwise.
SELECT Amount,
       CASE 
           WHEN Amount > 10000 THEN 'Big'
           ELSE 'Small'
       END AS SaleType
FROM sales;

-- Question 12 :  Find products where Category = 'Bars' AND Size = 'SMALL'
SELECT * FROM products WHERE Category = 'Bars' AND Size = 'SMALL';

-- Question 13 :  Find products where Category = Bars' OR Category = 'Bites' 
SELECT * FROM products WHERE Category = 'Bars' OR Category = 'Bites';

-- Question 14 : . List sales where Amount > 5000 AND Boxes < 100.
SELECT * FROM sales WHERE Amount > 5000 AND Boxes < 100;

-- Question 15 :  Display sales where the year of SaleDate is 2021.
SELECT * FROM sales WHERE YEAR(SaleDate) = 2021;

-- Question 16 :  Find all sales that happened in January 2021.
SELECT * FROM sales WHERE date(SaleDate) BETWEEN '2021-01-01' AND '2021-01-31';

-- Question 17 :  Show the number of sales that happened on 2021-01-01.
SELECT COUNT(*) AS NumberOfSales FROM sales WHERE date(SaleDate) = '2021-01-01';

-- Question 18 : Display all salespeople whose names start with 'B'
SELECT * FROM people WHERE Salesperson LIKE 'B%';

-- Question 19 : Find all products where the Product name contains 'Dark'
SELECT * FROM products WHERE Product LIKE '%Dark%';

-- Question 20 : Show all salespeople whose Location ends with 'land'
SELECT * FROM people WHERE Location LIKE '%land';

-- Question 21 : . Display the Salesperson name and Geo name for each sale.
SELECT p.Salesperson, g.GeoName
FROM sales s
JOIN people p ON s.SalespersonID = p.SalespersonID
JOIN geographies g ON s.GeoID = g.GeoID;    

-- Question 22 :  Show Product name, Category, and Amount for each sale.
SELECT pr.Product, pr.Category, s.Amount
FROM sales s
JOIN products pr ON s.ProductID = pr.ProductID; 

-- Question 23 :  Display Salesperson, Product, and Amount for each sale. 
SELECT p.Salesperson, pr.Product, s.Amount
FROM sales s
JOIN people p ON s.SalespersonID = p.SalespersonID      
JOIN products pr ON s.ProductID = pr.ProductID;

-- Question 24 : . Find the total sales Amount for each GeoID. 
SELECT GeoID, SUM(Amount) AS TotalSales
FROM sales
GROUP BY GeoID;

-- Question 25 :  Count how many products belong to each Category.
SELECT Category, COUNT(*) AS ProductCount
FROM products
GROUP BY Category;  

-- Question 26 : Find the average Cost_per_box for each Size.
SELECT Size, AVG(Cost_per_box) AS AverageCost
FROM products
GROUP BY Size;  

-- Question 27 : Show all distinct Team names from the people table.
SELECT DISTINCT Team FROM people;

-- Question 28 : Display all distinct Geo regions from the geo table.
SELECT DISTINCT GeoRegion FROM geographies; 

-- Question 29 : Write a query to display all Location values from people UNION all Geo values from geo.
SELECT Location AS Place FROM people
UNION ALL
SELECT GeoName AS Place FROM geographies;   

-- Question 30 :  Display the top 5 most expensive products using Cost_per_box 
SELECT * FROM products
ORDER BY Cost_per_box DESC
LIMIT 5;    