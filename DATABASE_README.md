# BudgetPal Database Design

## Overview

This database design is for Budgetpal expenses manager application that helps users track and manage their expenses. The application includes user authentication, expense tracking, and predefined expense categories.

![App Preview](/budgetpal/static/images/amiresponsive.png)

[Live link](https://budgetpal-33d89df1b1a4.herokuapp.com)

## Table of Contents

* [BudgetPal Database Design](#budgetpal-database-design)
  * [Overview](#overview)
  * [Table of Contents](#table-of-contents)
  * [Database Schema](#database-schema)
    * [User](#user)
    * [Expense](#expense)
    * [Category](#category)
  * [ER Diagram](#er-diagram)
  * [Table Descriptions](#table-descriptions)
    * [User](#user-1)
    * [Expense](#expense-1)
    * [Category](#category-1)
  * [Sample Queries](#sample-queries)

## Database Schema

### User

- **Columns:**
  - `id`: Integer, primary key
  - `username`: String(50), unique, not nullable
  - `password_hash`: String(150), not nullable
  - `email`: String(150), unique, index
  - `balance`: Float, default 0.0, not nullable
  - `savings`: Float, default 0.0, not nullable
  - `expenses`: Relationship with Expense model
  - `joined_at`: DateTime, default datetime.utcnow, index

### Expense

- **Columns:**
  - `id`: Integer, primary key
  - `amount`: Float, not nullable
  - `description`: String(255)
  - `expense_date`: Date, not nullable
  - `user_id`: Integer, foreign key to User.id, not nullable
  - `category_id`: Integer, foreign key to Category.id, nullable
  - `category`: Relationship with Category model

### Category

- **Columns:**
  - `id`: Integer, primary key
  - `name`: String(50), unique, not nullable
  - `logo_url`: String(255), not nullable

## ER Diagram

Include an Entity-Relationship (ER) diagram to illustrate the relationships between entities in the database.

![ER Diagram](/budgetpal/static/images/er_diagram.png)

## Table Descriptions

### User

- **Columns:**
  - `id`: Integer, primary key
  - `username`: String(50), unique, not nullable - The username of the user.
  - `password_hash`: String(150), not nullable - The hashed password of the user.
  - `email`: String(150), unique, index - The email address of the user.
  - `balance`: Float, default 0.0, not nullable - The current balance of the user.
  - `savings`: Float, default 0.0, not nullable - The amount of savings for the user.
  - `expenses`: Relationship with Expense model - One-to-Many relationship with Expense table.
  - `joined_at`: DateTime, default datetime.utcnow, index - The date and time when the user joined.

### Expense

- **Columns:**
  - `id`: Integer, primary key
  - `amount`: Float, not nullable - The amount of the expense.
  - `description`: String(255) - A description or note for the expense.
  - `expense_date`: Date, not nullable - The date when the expense occurred.
  - `user_id`: Integer, foreign key to User.id, not nullable - The user associated with the expense.
  - `category_id`: Integer, foreign key to Category.id, nullable - The category associated with the expense.
  - `category`: Relationship with Category model - Many-to-One relationship with Category table.

### Category

- **Columns:**
  - `id`: Integer, primary key
  - `name`: String(50), unique, not nullable - The name of the category.
  - `logo_url`: String(255), not nullable - The URL to the logo/icon representing the category.

## Sample Queries

Include some sample SQL queries that demonstrate how to interact with the database.

```sql
-- Example Select Query
SELECT * FROM User WHERE username = 'example';

-- Example Insert Query
INSERT INTO Expense (amount, description, expense_date, user_id, category_id) VALUES (100.0, 'Groceries', '2023-01-01', 1, 1);

-- Example Update Query
UPDATE User SET balance = balance - 50.0 WHERE id = 1;

-- Example Delete Query
DELETE FROM Expense WHERE id = 1;
```
