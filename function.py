from email.policy import default
import requests
import pandas as pd
import re
import string

from bs4 import BeautifulSoup

def get_contents(url, tags, delimeter = '.'):
    html = requests.get(url)
    document = BeautifulSoup(html.text, "html.parser")
    content = []
    for tag in list(tags):
        content.extend([i.text for i in document.find_all(tag)])
    final = []
    for text in content:
        final.extend(text.split(delimeter))
    return final

def get_links(url, tags):
    html = requests.get(url)
    doc = BeautifulSoup(html.text, "lxml")
    links = []
    for tag in tags:
        links.extend([link['href'] for link in doc.select(f'{tag} a[href]')])
    return links

def normalize_list_string(array):
    new_list = []
    array = [words.replace("\n", "").replace("\t", "").replace("-", "").replace('ʔ', '').replace('·', '').replace('）', '') for words in array]
    array = [words.replace('-', '').replace('–', '').replace('“', "").replace('”', '').replace('：', '') for words in array]
    array = [words.replace('’', '').replace('°', '').replace('‘', '').replace('\u200b', '').replace('（', '') for words in array]
    for words in array:
        words = re.sub(r'[0-9]', '', words)
        words = words.translate(str.maketrans('', '', string.punctuation))
        new_list.append(words)
    return new_list

def delete_whitespace(array):
    new_string = []
    for sen in array:
        sen.lstrip()
        s = ' '.join(sen.split())
        new_string.append(s)
    return new_string

def check_length_list_string(array, length=50):
    array = list(array)
    return [i for i in array if len(i) > length]

def length_for_lang(lang):
    match lang:
        case 'zh', 'ja', 'ko':
            return 35
        case _:
            return 50

def lang_translate(language):
    match language:
        case 'vi':
            return 'vietnamese'
        case 'en':
            return 'english'
        case 'fr':
            return 'french'
        case 'ar':
            return 'arabic'
        case 'ko':
            return 'korean'
        case 'zh':
            return 'chinese'
        case 'ja':
            return 'japanese'
        case 'de':
            return 'german'
        case 'ru':
            return 'russian'
        case 'it':
            return 'italian'
        case 'pt':
            return 'portuguese'
        case 'es':
            return 'spanish'
        case 'nl':
            return 'dutch'
        case 'pl':
            return 'polish'
        case 'ta':
            return 'tamil'
        case 'uk':
            return 'ukrainian'
        case 'sv':
            return 'swedish'
        case 'ms':
            return 'malay'
        case 'ro':
            return 'romanian'
        case 'tr':
            return 'turkish'