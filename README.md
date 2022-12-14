# Assignment 4: Normalization

  University Shortlisting : Normalization

## Group Members:

  Preksha Chandrashekhar Yadav - 002787954

  Shreyasi Wakankar - 002771284

  Somesh Ramakanth Ramisetty - 002776372

## Requirements:

  Requires Python and MySql to be downloaded and installed.

## Steps to be followed:

1.	Clone the DMDD_Assignment4 repository to local machine,
    git clone git@github.com:PrekshaYadav/DMDD_Assignment4.git
2.	Execute Connector.py: It connects python to MySQL and creates the schema for the required tables.
3.	Execute Importing_Dataset.py: The dataset is segregated, and the file checks the accuracy of the data using various audits and uses data visualization to make the       data more understandable. Leverages audit completeness to clean and verify the data, then stores the values in the appropriate tables.
4.	Refer to DMDD_Assignment4/Normalization.md file for 1NF, 2NF and 3NF checks.
5.	Refer to DMDD_Assignment4/Views.md file and DMDD_Assignment4/Assignment-4 Normalization.sql file for views we created for previous use cases and SQL queries for         those cases which can be implemented in Assignment-4.

## First normal form (1NF)

•	Each table has a primary key University_Id.

•	The values in each column of a table are atomic (No multi-value attributes).

•	There are no repeating groups: two columns do not store similar information in the same table.

## Second normal form (2NF)

•	All requirements in 1st NF have been met.

•	No partial dependencies.

•	No calculated data

## Third normal form (3NF)

•	All requirements in 2nd NF have been met.

•	Eliminated fields that do not directly depend on the primary key i.e no transitive dependencies.


