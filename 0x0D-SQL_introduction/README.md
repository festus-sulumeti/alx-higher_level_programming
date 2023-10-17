## 0x0D. SQL - Introduction

## Task Descriptions

## Task 0: List Databases
List all databases on your MySQL server by running:

$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

## Task 1: Create a Database
Create the "hbtn_0c_0" database on your MySQL server with the following command:
$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p

## Task 2: Delete a Database
To delete the "hbtn_0c_0" database, run:
$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p

## Task 3: List Tables
List all the tables in a database. Replace mysql with your database name:
$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p your_database_name

## Task 4: First Table
Create the "first_table" with "id" and "name" columns:
$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p your_database_name

## Task 5: Full Table Description
Get the full description of the "first_table" with:
$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p your_database_name

## Task 6: List All in Table
List all rows of the "first_table" in your database:
$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p your_database_name

## Task 7: First Add
Insert a new row into the "first_table" with id=89 and name="Best School":
$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p your_database_name

## Task 8: Count 89
To count the number of records with id=89 in "first_table," run:
$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p your_database_name | tail -1

## Task 9: Full Creation
Create a table "second_table" with multiple rows:
$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p your_database_name

## Task 10: List by Best
List all records in "second_table" sorted by score:
$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p your_database_name

## Task 11: Select the Best
List records with a score >= 10 in "second_table":
$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p your_database_name

## Task 12: Cheating is Bad
Update the score of "Bob" to 10 in "second_table":
$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p your_database_name

## Task 13: Score Too Low
Remove records with a score <= 5 in "second_table":
$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p your_database_name

## Task 14: Average
Compute the average score of all records in "second_table":
$ cat 14-average.sql | mysql -hlocalhost -uroot -p your_database_name

## Task 15: Number by Score
List the number of records with the same score in "second_table":
$ cat 15-groups.sql | mysql -hlocalhost -uroot -p your_database_name

## Task 16: Say My Name
List all records with a name value in "second_table" ordered by descending score:
$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p your_database_name

## Repository
## GitHub repository: alx-higher_level_programming
Directory: 0x0D-SQL_introduction
