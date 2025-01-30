DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS OrderDetails;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Shippers;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS Employees;

-- Creating tables and inserting data for a sample database similar to W3Schools in PostgreSQL

-- Create Customers table
CREATE TABLE Customers (
    CustomerID serial PRIMARY KEY,
    CustomerName varchar(255) NOT NULL,
    ContactName varchar(255),
    Address varchar(255),
    City varchar(255),
    PostalCode varchar(255),
    Country varchar(255)
);

-- Create Products table
CREATE TABLE Products (
    ProductID serial PRIMARY KEY,
    ProductName varchar(255) NOT NULL,
    SupplierID int,
    CategoryID int,
    Unit varchar(255),
    Price decimal
);

-- Create Orders table
CREATE TABLE Orders (
    OrderID serial PRIMARY KEY,
    CustomerID int,
    EmployeeID int,
    OrderDate VARCHAR(30),
    ShipperID int
);

-- Create OrderDetails table
CREATE TABLE OrderDetails (
    OrderDetailID serial PRIMARY KEY,
    OrderID int,
    ProductID int,
    Quantity int
);

-- Create Categories table
CREATE TABLE Categories (
    CategoryID serial PRIMARY KEY,
    CategoryName varchar(255) NOT NULL,
    Description text
);

-- Create Shippers table
CREATE TABLE Shippers (
    ShipperID serial PRIMARY KEY,
    ShipperName varchar(255) NOT NULL
);

-- Create Suppliers table
CREATE TABLE Suppliers (
    SupplierID serial PRIMARY KEY,
    SupplierName varchar(255) NOT NULL,
    ContactName varchar(255),
    Address varchar(255),
    City varchar(255),
    PostalCode varchar(255),
    Country varchar(255),
    Phone varchar(255)
);

-- Create Employees table
CREATE TABLE Employees (
    EmployeeID serial PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    BirthDate date,
    Photo varchar(255),
    Notes text
);

-- Insert data into Customers
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES 
('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),
('Vaffeljernet', 'Palle Ibsen', 'Smagsloget 45', 'Århus', '8200', 'Denmark'),
('Around the Horn', 'Thomas Hardy', '120 Hanover Sq.', 'London', 'WA1 1DP', 'UK'),
('Bon app', 'Laurence Lebihan', '12, rue des Bouchers', 'Marseille', '13008', 'France'),
('Bottom-Dollar Markets', 'Elizabeth Lincoln', '23 Tsawassen Blvd.', 'Tsawassen', 'T2F 8M4', 'Canada');

-- Insert data into Products
INSERT INTO Products (ProductName, SupplierID, CategoryID, Unit, Price)
VALUES 
('Chais', 1, 1, '10 boxes x 20 bags', 18.00),
('Chang', 1, 1, '24 - 12 oz bottles', 19.00),
('Aniseed Syrup', 1, 2, '12 - 550 ml bottles', 10.00),
('Chef Anton''s Cajun Seasoning', 2, 2, '48 - 6 oz jars', 22.00),
('Chef Anton''s Gumbo Mix', 2, 3, '36 boxes', 21.35);

-- Insert data into Categories
INSERT INTO Categories (CategoryName, Description)
VALUES 
('Beverages', 'Soft drinks, coffees, teas, beers, and ales'),
('Condiments', 'Sweet and savory sauces, relishes, spreads, and seasonings'),
('Confections', 'Desserts, candies, and sweet breads');

-- Insert data into Orders
INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID)
VALUES 
(1, 5, '2023-09-05', 2),
(2, 6, '2023-09-06', 1),
(3, 7, '2023-09-07', 3);

-- Insert data into OrderDetails
INSERT INTO OrderDetails (OrderID, ProductID, Quantity)
VALUES 
(1, 1, 10),
(1, 3, 5),
(2, 2, 3),
(3, 2, 2),
(3, 3, 4);

-- Insert data into Shippers
INSERT INTO Shippers (ShipperName)
VALUES 
('Federal Shipping'),
('Speedy Express'),
('United Package');

-- Insert data into Suppliers
INSERT INTO Suppliers (SupplierName, ContactName, Address, City, PostalCode, Country, Phone)
VALUES 
('Exotic Liquid', 'Charlotte Cooper', '49 Gilbert St.', 'London', 'EC1 4SD', 'UK', '171-555-2222'),
('New Orleans Cajun Delights', 'Shelley Burke', 'P.O. Box 78934', 'New Orleans', '70117', 'USA', '504-555-9831');

-- Insert data into Employees
INSERT INTO Employees (LastName, FirstName, BirthDate, Photo, Notes)
VALUES 
('Davolio', 'Nancy', '1968-12-08', 'EmpID1.pic', 'Education includes a BA in psychology.'),
('Fuller', 'Andrew', '1952-02-19', 'EmpID2.pic', 'Andrew received his BTS commercial and a Ph.D. in international marketing.'),
('Leverling', 'Janet', '1963-08-30', 'EmpID3.pic', 'Janet has a BS degree in chemistry.');


-- Insert more data into Customers
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES 
('Alfreds Futterkiste', 'Maria Anders', 'Obere Str. 57', 'Berlin', '12209', 'Germany'),
('Berglunds snabbköp', 'Christina Berglund', 'Berguvsvägen 8', 'Luleå', 'S-958 22', 'Sweden'),
('Blauer See Delikatessen', 'Hanna Moos', 'Forsterstr. 57', 'Mannheim', '68306', 'Germany'),
('Blondel père et fils', 'Frédérique Citeaux', '24, place Kléber', 'Strasbourg', '67000', 'France'),
('Bólido Comidas preparadas', 'Martín Sommer', 'C/ Araquil, 67', 'Madrid', '28023', 'Spain');

-- Insert more data into Products
INSERT INTO Products (ProductName, SupplierID, CategoryID, Unit, Price)
VALUES 
('Northwoods Cranberry Sauce', 3, 2, '12 - 12 oz jars', 40.00),
('Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97.00),
('Ikura', 4, 8, '12 - 200 ml jars', 31.00),
('Queso Cabrales', 5, 4, '1 kg pkg.', 21.00),
('Konbu', 6, 7, '2 kg box', 6.00);

-- Insert more data into Employees
INSERT INTO Employees (LastName, FirstName, BirthDate, Photo, Notes)
VALUES 
('Peacock', 'Margaret', '1958-09-19', 'EmpID4.pic', 'Margaret has a BA in English literature.'),
('Buchanan', 'Steven', '1955-03-04', 'EmpID5.pic', 'Steven has a master in sales management.'),
('Suyama', 'Michael', '1963-07-02', 'EmpID6.pic', 'Michael has a diploma in marketing.'),
('King', 'Robert', '1960-05-29', 'EmpID7.pic', 'Robert has an MBA.'),
('Callahan', 'Laura', '1958-01-09', 'EmpID8.pic', 'Laura has a degree in accounting.');

-- Insert more data into Orders
INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, ShipperID)
VALUES 
(4, 3, '2023-09-12', 3),
(5, 4, '2023-09-13', 2),
(6, 2, '2023-09-14', 1),
(7, 1, '2023-09-15', 3),
(8, 3, '2023-09-16', 2);

-- Insert more data into OrderDetails
INSERT INTO OrderDetails (OrderID, ProductID, Quantity)
VALUES 
(4, 6, 12),
(5, 6, 10),
(6, 5, 7),
(7, 4, 5),
(8, 3, 2);
