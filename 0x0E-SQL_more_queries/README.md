# MySQL Basics Readme

This readme provides a concise overview of fundamental concepts in MySQL, aimed at beginners.

## Creating a New MySQL User

To create a new MySQL user, follow these steps:

1. **Access MySQL**: Log in to your MySQL server using appropriate credentials.
2. **Create User**: Use the `CREATE USER` command followed by the username and host.
   ```
   CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
   ```
3. **Grant Privileges**: Grant necessary privileges using the `GRANT` command.
   ```
   GRANT SELECT, INSERT, UPDATE ON database_name.* TO 'new_user'@'localhost';
   ```
4. **Flush Privileges**: After granting privileges, execute `FLUSH PRIVILEGES;` for changes to take effect.

## Managing User Privileges

Use the `GRANT` command to manage user privileges. You can assign permissions to specific databases or tables.

## PRIMARY KEY

A PRIMARY KEY uniquely identifies records in a database table. It ensures the uniqueness and non-nullity of the key.

## FOREIGN KEY

A FOREIGN KEY establishes a link between two tables by referencing the primary key of another table. It enforces referential integrity, maintaining consistency across related tables.

## NOT NULL and UNIQUE Constraints

- The `NOT NULL` constraint ensures a column cannot contain null values.
- The `UNIQUE` constraint guarantees the uniqueness of values in a column.

## Retrieving Data from Multiple Tables

To retrieve data from multiple tables in one request:

- Use `JOIN` clauses to combine related tables based on specified conditions.
- Use `UNION` to merge the result sets of multiple `SELECT` statements.

## Subqueries

A subquery is a query nested within another query. It's used to retrieve data needed for the main query's conditions or calculations.

## JOIN and UNION

- **JOIN**: Joins combine rows from different tables based on common columns. Types include INNER, LEFT, RIGHT, and FULL OUTER JOINs.
- **UNION**: UNION combines the result sets of two or more `SELECT` statements into a single result set.
