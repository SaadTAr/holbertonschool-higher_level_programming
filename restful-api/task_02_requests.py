#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from the API and print the status code
    followed by the title of each post.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetch all posts from the API and save selected
    fields to posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        with open("posts.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )

            writer.writeheader()

            for post in posts:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })
