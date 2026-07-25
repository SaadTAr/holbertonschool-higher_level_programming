# Python - Object Relational Mapping

This project is part of the Holberton School Higher Level Programming curriculum.

The objective of this project is to learn how to interact with MySQL databases using Python. It introduces the MySQLdb module, SQLAlchemy ORM, database connections, SQL queries, and object-relational mapping.

## Learning Objectives

At the end of this project, you should be able to explain:

- Why Python programming is awesome
- How to connect to a MySQL database from Python
- How to execute SQL queries using MySQLdb
- How to fetch and display query results
- How to protect SQL queries against SQL injection
- What an ORM is
- How to map Python classes to database tables
- How to use SQLAlchemy
- How to create, read, update and delete database records using Python

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- MySQL 8.0
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- pycodestyle 2.8.*

## Files

| File | Description |
|------|-------------|
| 0-select_states.py | Lists all states from the database |
| 1-filter_states.py | Lists states matching the provided name |
| 2-my_filter_states.py | Filters states safely using user input |
| 3-my_safe_filter_states.py | Prevents SQL injection |
| 4-cities_by_state.py | Lists all cities by state |
| 5-filter_cities.py | Lists cities of a given state |
| 6-model_state.py | Creates the State model using SQLAlchemy |
| 7-model_state_fetch_all.py | Lists all State objects |
| 8-model_state_fetch_first.py | Displays the first State object |
| 9-model_state_filter_a.py | Lists states containing the letter 'a' |
| 10-model_state_my_get.py | Gets a state by name |
| 11-model_state_insert.py | Adds a new State |
| 12-model_state_update_id_2.py | Updates State with id = 2 |
| 13-model_state_delete_a.py | Deletes states containing 'a' |
| 14-model_city_fetch_by_state.py | Lists all cities grouped by state |

## Usage

Run a script using:

```bash
./script_name.py mysql_username mysql_password database_name
```

Example:

```bash
./0-select_states.py root root hbtn_0e_0_usa
```

## Author

Saad
