# Database

**DBMS** database management system, not only having database structure, but also manage data security, concurrent access,
and data exchange with other database systems.

## SQL

Structured Query Language. Developed in 1970s by IBM.

## SQLite

Database management systems. Stored in only one file. No separate server process is required to communicate with the database.
No configuration.

## sqlite3

Standard Python library
Interface compliant with the DB-API 2.0 specification which defines a common standard for creating modules to work with
database in Python.

`sqlite3.connect(xxx.db)` creates a database only if it cannot find a database `xxx.db` in a location. If a database exists,
SQLite connects to it.