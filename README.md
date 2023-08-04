
## Description

A crawler that can start from a specified url and send requests to all urls it encounters.

Then store the file(html or text) locally, also store the relative path and url related information into the database

Due to the nature of **scrapy**, the whole process is asynchronous

## Config

1. The database
   - IN general.py and pipelines.py
2. The content you want
   - IN general.py

## Install and use

### make sure python3.10 or higher

### Install poetry

```shell
pip install poetry
```

### build

```shell
git clone
cd crawler
poetry install # automatic install dependencies
```

### use

```shell
cd GeneralCrawler
poetry shell
scrapy crawl general
```

