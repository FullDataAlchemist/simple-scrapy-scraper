import json
import os
from newspaper import Article


def writer(domain: str, cat: str, name: str, out_data: str):
    try:
        os.mkdir('saved_data' + '/' + domain)
    except Exception as e:
        pass
    try:
        os.mkdir('saved_data' + '/' + domain + '/' + cat)
    except Exception as e:
        pass
    with open('saved_data' + '/' + domain + '/' + cat + '/' + name + '.txt', 'w') as out_file:
        out_file.write(out_data)


def json_writer(domain: str, cat: str, name: str, out_data: dict):
    try:
        os.mkdir('saved_data')
    except Exception as e:
        pass
    try:
        os.mkdir('saved_data' + '/' + domain)
    except Exception as e:
        pass
    try:
        os.mkdir('saved_data' + '/' + domain + '/' + cat)
    except Exception as e:
        pass
    with open('saved_data' + '/' + domain + '/' + cat + '/' + name + '.json', 'w') as out_file:
        json.dump(out_data, out_file)


def paring_html(url, html_body):
    article = Article(url=url, fetch_images=False, _language="fa",
                      browser_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
    article.set_html(html_body)
    article.parse()
    return article


def get_top_n_keywords(article: Article):
    try:
        article.nlp()
        keywords = article.keywords
        return keywords
    except Exception as e:
        print(e)
        return None


def load_links(fn, cat):
    try:
        saved_links = os.listdir('saved_data' + '/' + fn + '/' + cat)
        saved_links = [x[:-5] for x in saved_links]
    except FileNotFoundError as e:
        saved_links = list()
    return saved_links
