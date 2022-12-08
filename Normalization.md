# DMDD_Assignment4

Our database contains 3 tables University, Requirements and Standards 

![Class Diagram](images/University.jpg)
![Class Diagram](images/Standards.jpg)
![Class Diagram](images/Requirements.jpg)

## First Normal Form (1NF) :
- All these tables have primary key.
    University : University_ID (PK)
    Standards and Requirements does not need a primary key, it had University_ID as a Foreign key.
- All the columns of all the tables are atomic.
    There are no multiple values stored in a single column of the table.
- All the columns store distinct information and contribute to the dataset in it's own unique way.

Hence the tables in the database are in 1NF.

## Second Normal Form (2NF) :
- The table qualifies to be in the first normal form.
- No columns in all the tables are dependent on each other and hence there is not partial dependency in the dataset.
    The columns in the tables are not retrived from any of the other column

Hence the tables in the database are in 2NF.

## Third Normal Form (3NF):
- The table qualifies to be in the second normal form.
- There are no transitive dependencies.

Hence the tables in the database are in 3NF.








