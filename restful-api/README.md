# Task 2 - Consuming and Processing Data from an API

## Description

This project demonstrates how to consume data from a REST API using the Python `requests` library. It retrieves posts from the JSONPlaceholder API, prints the titles of all posts, and saves selected data into a CSV file.

## Requirements

- Python 3.x
- requests library

Install requests:

```bash
pip3 install requests
```

## Files

- `task_02_requests.py`
- `posts.csv` (generated after running the script)

## Functions

### fetch_and_print_posts()

- Sends a GET request to:
  ```
  https://jsonplaceholder.typicode.com/posts
  ```
- Prints the HTTP status code.
- Prints the title of each post.

### fetch_and_save_posts()

- Retrieves all posts from the API.
- Saves the following fields into `posts.csv`:
  - id
  - title
  - body

## Example

Run:

```python
from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

fetch_and_print_posts()
fetch_and_save_posts()
```

Example output:

```
Status Code: 200
sunt aut facere repellat provident occaecati...
qui est esse
ea molestias quasi exercitationem...
...
```

Generated CSV:

```
id,title,body
1,sunt aut facere...,quia et suscipit...
2,qui est esse...,est rerum tempore...
```
