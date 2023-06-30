# Database

**DBMS** database management system, not only having database structure, but also manage data security, concurrent access,
and data exchange with other database systems.

## SQL

Structured Query Language. Developed in 1970s by IBM.

### UPDATE

If you forget about the `WHERE` caluse, all data in the table will be updated.

## SQLite

Database management systems. Stored in only one file. No separate server process is required to communicate with the database.
No configuration.

## sqlite3

Standard Python library
Interface compliant with the DB-API 2.0 specification which defines a common standard for creating modules to work with
database in Python.

`sqlite3.connect(xxx.db)` creates a database only if it cannot find a database `xxx.db` in a location. If a database exists,
SQLite connects to it.

`:memory:` is a special connection string to indicate that the database should be created and stored in memory rather 
than on disk. `conn = sqlite3.connect(":memory:")`

## Cursor object iterator vs fetchall()

`fetchall` method is less efficient than the iterator, because it reads all records into the memory and then returns a
list of tuples. If a table contains a huge number of records, this can cause memory issues.

