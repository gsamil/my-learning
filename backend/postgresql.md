# PostgreSQL

### What is a Database?

- It's a place where we can store, manipulate and retrieve data.

### What is SQL and Relational Database?

- `SQL` (Structured Query Language) is a programming language that allows us to manage data in a relational database.
- It's easy to learn and very powerful.
- Data is stored in tables, which are formed by columns and rows.
- A `relational database` is when two or more tables have some kind of relationship between them.

### What is PostgreSQL AKA Postgres?

- The most advanced open source relational database. (So it's free!)
- It's an Object-Relational Database Management System.
- It's alternative to Oracle, MySQL, SQL Server, etc.

### PostgreSQL Installation (MacOS)

- Search for `Postgres app` and download it.

### GUI Clients vs Terminal/CMD Clients

- GUI Clients are easier to use, but they are slower and not available in remote servers.
- Terminal/CMD Clients are faster.
- DataGrip is a GUI Client for PostgreSQL. 

### Setup PSQL (MacOS)

- In `.zshrc` add:

    ```bash
    export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin
    ```

### Create Database

- In terminal, type `psql` to enter the psql shell.
- You can type `help` to see the available commands. 
- Type `\l` to list all databases.
- To create a database:

  ```sql
  CREATE DATABASE test;
  ```

### Connect to Database

- In terminal, type:

  ```bash
  psql -h localhost -p 5432 -U amigoscode test
  ```
- Alternatively, type `psql` to enter the psql shell and then to connect to the database, type:

  ```bash
  \c test
  ```

### Delete a Database

- In terminal, type:

  ```sql
  DROP DATABASE test;
  ```

### Create Table

- This is a generic way you can create a table (without constraints):

  ```sql
  CREATE TABLE table_name (
    column_name data_type
  )
  ```

- Example:

  ```sql
  CREATE TABLE person (
    id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(7),
    date_of_birth DATE,
  );
  ```

- You can see the data types available in the [PostgreSQL Documentation](https://www.postgresql.org/docs/13/datatype.html).
- Type `\d` (for describe) to see the tables in the database.
- Type `\d person` to see the columns of the person table.

### Create Tables With Constraints

- This is a generic way you can create a table with constraints:

  ```sql
  CREATE TABLE table_name (
    column_name data_type column_constraints,
  )
  ```

- Example:

  ```sql
  CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(7) NOT NULL,
    date_of_birth DATE NOT NULL,
  );
  ```

- **Note:** `BIGSERIAL` is a signed eight-byte integer. It auto increments automatically for you.

### Drop Table

- To drop a table, type:
    
  ```sql
  DROP TABLE person;
  ```

### Insert Data into Table

- Let's say we want to insert a new person into our table:

  ```sql
  INSERT INTO person (
    first_name,
    last_name,
    gender,
    date_of_birth
  )
  VALUES ('Anne', 'Smith', 'FEMALE', DATE '1988-01-09');
  ```

- Notice here we didn't specify the `id` column. This is because the `BIGSERIAL` data type auto increments for us.

- **Note:** To list only the tables, type `\dt`.

### Generate 1000 People with Mockaroo

- Go to [Mockaroo](https://www.mockaroo.com/).
- After you create the data (don't forget to add `id`), click on `Download Data`, Select SQL.
- Define the constraints in the `.sql` file.
- Go back to terminal and `cd` to the directory where the file is.
- Type `psql` to enter the psql shell.
- First drop the existing table with `DROP TABLE person;`.
- Type `\i person.sql` to execute the file.
- Type `SELECT * FROM person;` to see the data.

### Select From

```sql
SELECT * FROM person;
SELECT first_name, last_name FROM person;
```

### Order By

```sql
SELECT * FROM person ORDER BY first_name; -- it's ASC by default
SELECT * FROM person ORDER BY first_name DESC;
```

### Distinct

```sql
SELECT DISTINCT countr_of_birth FROM person ORDER BY countr_of_birth;
```

### `WHERE` Clause and `AND`

```sql
SELECT * FROM person WHERE gender = 'Female';
SELECT * FROM person WHERE gender = 'Female' AND country_of_birth = 'Poland';
```

### Comparison Operators

```sql
SELECT 1 = 1;  -- equals
SELECT 1 <> 1; -- not equals
SELECT 1 > 1;  -- greater than
SELECT 1 < 1;  -- less than
SELECT 1 >= 1; -- greater than or equal
SELECT 1 <= 1; -- less than or equal
```

### Limit, Offset, Fetch

```sql
SELECT * FROM person LIMIT 10;
SELECT * FROM person OFFSET 10 LIMIT 10;
SELECT * FROM person OFFSET 10 FETCH FIRST 10 ROW ONLY; -- this is original way of limiting in sql
```

### In

```sql
SELECT * FROM person WHERE country_of_birth IN ('Poland', 'Germany');
```

### Between

```sql
SELECT * FROM person WHERE date_of_birth BETWEEN DATE '1990-01-01' AND DATE '1999-12-31';
```

### Like and ILike

```sql
SELECT * FROM person WHERE email LIKE '%@bloomberg.com';
SELECT * FROM person WHERE email LIKE '_______@%'; -- 7 characters before @
SELECT * FROM person WHERE email ILIKE '%@bloomberg.com'; -- case insensitive
```

### Group By & Group By Having

```sql
SELECT country_of_birth, COUNT(*) FROM person GROUP BY country_of_birth;
SELECT country_of_birth, COUNT(*) FROM person GROUP BY country_of_birth HAVING COUNT(*) > 5;

-- ORDER BY must come after HAVING
SELECT country_of_birth, COUNT(*) FROM person GROUP BY country_of_birth HAVING COUNT(*) > 5 ORDER BY country_of_birth;
```

### Max, Min, Avg

```sql
SELECT MAX(price) FROM car;
SELECT MIN(price) FROM car;
SELECT AVG(price) FROM car;
SELECT ROUND(AVG(price)) FROM car;
SELECT make, model, MIN(price) FROM car GROUP BY make, model;
```

### Sum

```sql
SELECT SUM(price) FROM car;
SELECT make, SUM(price) FROM car GROUP BY make;
```

### Basic Arithmetic Operations

```sql
SELECT 1 + 1;  -- addition
SELECT 1 - 1;  -- subtraction
SELECT 1 * 1;  -- multiplication
SELECT 1 / 1;  -- division
SELECT 1 ^ 1;  -- power
SELECT 1!;     -- factorial
SELECT 1 % 1;  -- modulo
```

### Round

```sql
SELECT ROUND(1.5);         -- 2
SELECT ROUND(1.43465, 2);  -- 1.43
```

### Alias

```sql
SELECT first_name AS name FROM person;
```

### Coalesce

```sql
SELECT COALESCE(NULL, 'Amigoscode');        -- Amigoscode
SELECT COALESCE(NULL, NULL, 'Amigoscode');  -- Amigoscode
```

### NULLIF

- Returns the first argument if it is not equal to the second argument. 
- Returns null if the arguments are equal.

  ```sql
  SELECT NULLIF(1, 2);                    -- 1
  SELECT NULLIF(1, 1);                    -- NULL
  SELECT 10 / 0;                          -- ERROR
  SELECT 10 / NULL;                       -- NULL
  SELECT 10 / NULLIF(0, 0);               -- NULL
  SELECT COALESCE(10 / NULLIF(0, 0), 0);  -- 0
  ```

### Timestamps and Dates

```sql
SELECT NOW();        -- 2021-01-09 16:00:00.000000
SELECT NOW()::DATE;  -- 2021-01-09
SELECT NOW()::TIME;  -- 16:00:00.000000
```

### Adding and Subtracting Dates

```sql
SELECT NOW() - INTERVAL '1 YEAR';
SELECT NOW() - INTERVAL '10 YEARS';
SELECT NOW() - INTERVAL '1 MONTH';
SELECT NOW() - INTERVAL '1 DAY';
SELECT (NOW() - INTERVAL '1 DAY')::DATE;
```

### Extracting Fields from Timestamp

```sql
SELECT EXTRACT(YEAR FROM NOW());  -- 2021
SELECT EXTRACT(MONTH FROM NOW()); -- 1
SELECT EXTRACT(DAY FROM NOW());   -- 9
SELECT EXTRACT(DOW FROM NOW());   -- 6
```

### Age Function

```sql
SELECT AGE('1990-01-01');  -- 31 years 8 days
SELECT AGE(NOW(), date_of_birth) AS age FROM person;
```

### Primary Keys

- A primary key is a column or a group of columns used to identify a row uniquely in a table.
- A primary key cannot be null.
- A table can have only one primary key.
- A primary key can consist of one or more columns on a table.
- When multiple columns are used as a primary key, they are called a composite key.

### Drop Primary Key

```sql
ALTER TABLE person DROP CONSTRAINT person_pkey;
```

### Adding Primary Key

```sql
ALTER TABLE person ADD PRIMARY KEY (id);
```

### Unique Constraints

- A unique constraint is a single field or combination of fields that uniquely defines a record.

  ```sql
  -- Adding Unique Constraints
  ALTER TABLE person ADD CONSTRAINT person_email_key UNIQUE (email);
  ALTER TABLE person ADD UNIQUE (email);
  
  -- Dropping Unique Constraints
  ALTER TABLE person DROP CONSTRAINT person_email_key;
  ```

### Check Constraints

- A check constraint is used to limit the value range that can be placed in a column.

  ```sql
  -- Adding Check Constraints
  ALTER TABLE person ADD CONSTRAINT gender_constraint CHECK(gender = 'Female' OR gender = 'Male');
  ```

### Delete Records

```sql
DELETE FROM person WHERE id = 1;
```

### Update Records

```sql
UPDATE person SET first_name = 'Anne' WHERE id = 2;
```

### On Conflict Do Nothing

```sql
INSERT INTO person (id, first_name, last_name, gender, email, date_of_birth, country_of_birth)
VALUES (2017, 'Russ' "Ruddoch', 'Male', 'rruddoch7@hhs.gov', DATE 1952-09-25', 'Norway')
ON CONFLICT (id) DO NOTHING;
```

### Upsert

```sql
INSERT INTO person (id, first_name, last_name, gender, email, date_of_birth, country_of_birth)
VALUES (2017, 'Russ' "Ruddoch', 'Male', 'rruddoch7@hhs.gov', DATE 1952-09-25', 'Norway')
ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email, date_of_birth = EXCLUDED.date_of_birth;
```

### Foreign Keys, Joins, Relationships

- A foreign key is a column or a group of columns in a table that reference the primary key of another table.
- A relationship is a connection between two tables using foreign keys.

```sql
create table car (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    make VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    price NUMERIC(19, 2) NOT NULL
);

create table person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(7) NOT NULL,
    email VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    country_of_birth VARCHAR(50) NOT NULL,
    car_id BIGINT REFERENCES car(id),
    UNIQUE(car_id)
);

insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth) values ('Fernanda', 'Beardon', 'Female', 'fernandabais.gd', '1953-10-28', 'Finland');
insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth) values ('Omar', 'Colomore', 'Male', null, '1921-04-03', 'Finland');
insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth) values ('Adriana', 'Matuschek', 'Female', 'amatuschek2@feedburner.com', null, null);

insert into car (make, model, price) values ('Land Rover', 'Sterling', '87665.38');
insert into car (make, model, price) values ('GMC', 'Acadia', '17662.69');
```

### Update Foreign Key Columns

```sql
UPDATE person SET car_id = 1 WHERE id = 1;
```

### Inner Join

- It's an effective way of combining data from multiple tables.
- It returns rows that have matching values in both tables.

  ```sql
  SELECT * FROM person
  JOIN car ON person.car_id = car.id;
  ```

### Left Join

- It returns all rows from the left table and the matching rows from the right table.
- If there are no matches in the right table, it returns null values.

- Example:

  ```sql
  SELECT * FROM person
  LEFT JOIN car ON person.car_id = car.id;
  ```

- Return only the people who don't have a car:
  
  ```sql
  SELECT * FROM person
  LEFT JOIN car ON person.car_id = car.id
  WHERE car.* IS NULL;
  ```

### Delete Records with Foreign Keys

- You cannot directly delete a record that has a foreign key constraint.
- You must delete the child records first.

  ```sql
  -- first option is to delete the records from the person table
  DELETE FROM person WHERE id = 1;

  -- second option is to remove car_id from the person table for that specific record
  UPDATE person SET car_id = NULL WHERE id = 1;
  ```

### Exporting Query Results to CSV

- In psql terminal, type:

  ```sql
  \copy (SELECT * FROM person) LEFT JOIN car ON person.car_id = car.id TO 'person.csv' DELIMITER ',' CSV HEADER;    
  ```

### Extensions & UUID

```sql
SELECT * FROM pg_available_extensions;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
SELECT uuid_generate_v4();  --random uuid
```

### UUID as Primary Key

- Instead of `BIGSERIAL`, we can use `UUID`, don't forget to update foreign key types too.

  ```sql
  create table car (
      car_uuid UUID NOT NULL PRIMARY KEY,
      make VARCHAR(100) NOT NULL,
      model VARCHAR(100) NOT NULL,
      price NUMERIC(19, 2) NOT NULL CHECK (price > 0)
  );
  
  create table person (
      person_uuid UUID NOT NULL PRIMARY KEY,
      first_name VARCHAR(50) NOT NULL,
      last_name VARCHAR(50) NOT NULL,
      gender VARCHAR(7) NOT NULL,
      email VARCHAR(100),
      date_of_birth DATE NOT NULL,
      country_of_birth VARCHAR(50) NOT NULL,
      car_uuid UUID REFERENCES car(car_uuid),
      UNIQUE(car_uuid),
      UNIQUE(email)
  );
  
  -- INSERT INTO PERSON
  insert into person (person_uuid, first_name, last_name, gender, email, date_of_birth, country_of_birth) 
  values (uuid_generate_v4(), 'Fernanda', 'Beardon', 'Female', 'fernandab@is.gd', '1953-10-28', 'Comoros');
  
  insert into person (person_uuid, first_name, last_name, gender, email, date_of_birth, country_of_birth) 
  values (uuid_generate_v4(), 'Omar', 'Colomore', 'Male', null, '1921-04-03', 'Finland');
  
  insert into person (person_uuid, first_name, last_name, gender, email, date_of_birth, country_of_birth) 
  values (uuid_generate_v4(), 'Adriana', 'Matuschek', 'Female', 'amatuschek2@feedburner.com', '1965-02-28', 'Cameroon');
  
  -- INSERT INTO CAR
  insert into car (car_uuid, make, model, price) values (uuid_generate_v4(), 'Land Rover', 'Sterling', '87665.38');
  insert into car (car_uuid, make, model, price) values (uuid_generate_v4(), 'GMC', 'Acadia', '17662.69');
  ```

### Alternative way of Joining

```sql
SELECT * FROM person, 
JOIN car USING (car_uuid);
```

## References

- [Learn PostgreSQL Tutorial - Full Course for Beginners](https://youtu.be/qw--VYLpxG4)
