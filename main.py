import random
import requests
from bs4 import BeautifulSoup
import argparse
import os
import json

# Books to scrape
URL = 'https://books.toscrape.com/'

def saveBooks(books):
  root_dir = os.path.dirname(os.path.abspath(__file__))
  data_folder = os.path.join(root_dir, "data")

  if not os.path.exists(data_folder):
    os.mkdir(data_folder)

  file_path = os.path.join(data_folder, "books.json")
  with open(file_path, "w") as f:
    json.dump(books, f)

def showBook(books):
  n_books = len(books)

  while(True):
    idx = random.randrange(0, n_books)
    
    print(f'Found random book to read: {books[idx]}')

    # comment/uncomment the next line out to add/remove user input
    # break

    user_input = input('Do you want another movie (y/[n])? ')
    if user_input != 'y':
        break

def main(mode, products):
    books = []
    for product in products:
      title = product.h3.a["title"]
      rating = product.p["class"][1]

      book = {
        "title": title,
        "rating": rating
      }
      books.append(book)

    if mode == "show":
      showBook(books)
    elif mode == "save":
      saveBooks(books)
    
    return

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-m", "--mode", help="specify 'show' to display a random book or 'save' to save all books to a JSON file", choices=["show", "save"])
  args = parser.parse_args()

  # If website thinks you're a bot (in Fortnite), add some fake headers to bypass this
  # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
  response = requests.get(URL)
  soup = BeautifulSoup(response.text, 'html.parser')
  products = soup.select("article.product_pod")

  # print(soup.prettify())

  main(args.mode, products)