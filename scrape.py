# Python3

from bs4 import BeautifulSoup
import requests
import re
import os
from os.path import exists

filename = "complete_list.txt"
brand = "google"
if (os.path.exists(filename)):
    os.remove(filename)

results = []

def collect_urls(page, f):
    url = f"https://www.examtopics.com/discussions/{brand}/{page}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    reqs = requests.get(url, headers=headers)
    print(f"Running for page: {page} (Status: {reqs.status_code})")
    
    if reqs.status_code != 200:
        return

    soup = BeautifulSoup(reqs.text, 'html.parser')

    for tag in soup.find_all("a", attrs={"class" : "discussion-link"}, href=True):
        link = "https://www.examtopics.com" + tag.get('href')
        f.write(link + '\n')
        results.append(link)


with open(filename, "a") as f:
    for page in range(0, 176):
        collect_urls(page, f)
        f.flush()


# results.sort()
# for i in range(0, len(results)):
#     print(results[i])