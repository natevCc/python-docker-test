<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

Table of contents

- [Docker tutorial with simple Python script](#docker-tutorial-with-simple-python-script)
  - [Goal](#goal)
  - [Script](#script)
  - [Requirements.txt](#requirementstxt)
  - [Docker](#docker)
    - [Run](#run)
    - [Mount](#mount)

<!-- TOC end -->

<!-- TOC --><a name="docker-tutorial-with-simple-python-script"></a>

# Docker tutorial with simple Python script

<!-- TOC --><a name="goal"></a>

## Goal

To dockerize a simple python script that can run in a container.
The script can receive user input, and also take command line parameters.

<!-- TOC --><a name="script"></a>

## Script

The script uses a dummy web scraping site for testing and practicing:
https://books.toscrape.com/

The script has the following functionality:

1. Scrapes the books from the URL and selects randomly a book. Shows its title and rating
2. Can select a different one from user input
3. Generate a JSON file from the data and saves it to the system

<!-- TOC --><a name="requirementstxt"></a>

## Requirements.txt

Requirements file is auto generated via:

```bash
pip install pipreqs
pipreqs /path/to/project

# Or if you are in the current working directory
pipreqs .

```

<!-- TOC --><a name="docker"></a>

## Docker

<!-- TOC --><a name="run"></a>

### Run

Runs the specified image

**Arguments**

- `-i`, `--interactive` - Keep STDIN open even if not attached
- `-t`, `--tty` - Allocate a pseudo-TTY
- `--rm` - Remove container after exit
- `--name` - The name of the container
- `-v` - Mount path source:target

```bash
docker run -it --name books_app --rm -v "/$(pwd)/data":/home/app_user/app/data nate/python-books
```

<!-- TOC --><a name="mount"></a>

### Mount

As seen the mounting set to `-v "/$(pwd)/data":/home/app_user/app/data`. This when is used with git bash for Windows, otherwise it produces some errors.

For Linux, you can just use `-v $(pwd)/data:/home/app_user/app/data`
