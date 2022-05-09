

# Question 1:

**Thoughts:**

Exploring the data I discovered two clear outliers that were the result of the higher than expected AOV.

The first is a handful bulk purchases of quantities of 2000 items each.  I would suggest filtering these out from the results as the average order value for individual customer purchases should probably be considered seperately from those of bulk purchases. 

The second is an extremely expensive sneaker at shop 78 for $25,725.00. I would also suggest filtering these from the results as they would appear to be a luxury or collector item in their own category.

Both of these outliers are each respectively unique to a single store, and it would also be worth while speaking with someone at these stores to ensure this data is accurate and not the result of an error.  I would also want to consult with someone in the buisness department before implementing any thresholds that determine whether a purchase is bulk or not, or if an item is of high enough value to be in it's own category.

**Final Answer:**

I would report an AOV with both of these outliers filtered out, as it gives the best impression of the orders being made at the typical sneaker store.  However I would also note the outliers that had been removed from that calculation and bring attention to the signifigance that they hold in their own right.

<br/><br/>

# Question 2:
**How many orders were shipped by Speedy Express in total?**
```
SELECT COUNT(*) FROM Orders
    JOIN Shippers ON Shippers.ShipperID = Orders.ShipperID
    WHERE Shippers.ShipperName is 'Speedy Express';
```

52 orders were shipped by speedy express

<br/><br/>

**What is the last name of the employee with the most orders?**
```
SELECT LastName from Employees
    JOIN Orders ON Employees.EmployeeID = Orders.EmployeeID
    GROUP BY Employees.EmployeeID
    ORDER BY COUNT(Orders.OrderID) DESC
    LIMIT 1;
```
Peacock is the last name of the employee with the most sales

<br/><br/>

**What product was ordered the most by customers in Germany?**
 ```
SELECT ProductName FROM Products
	JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID
    JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
    JOIN Customers ON Orders.CustomerID = Customers.CustomerID
    	WHERE Customers.Country IS 'Germany'
    GROUP BY ProductName
    ORDER BY COUNT(Orders.OrderID) DESC
    LIMIT 1;
```
Gorgonzola Telino is the product ordered most by customers in Germany