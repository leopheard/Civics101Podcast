import requests
import re
from bs4 import BeautifulSoup

url1 = "https://feeds.megaphone.fm/PPY1168790592"
def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
get_soup1("https://feeds.megaphone.fm/PPY1168790592")

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item', limit=9):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/63ccd1d6-34f5-11e7-b527-335db86cfd5e/image/uploads_2F1552483361586-5d5fhueod4e-9827e8631b5a37cd3ad727b3cf6bb26b_2FCivics101Logo_LGwithBG.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/63ccd1d6-34f5-11e7-b527-335db86cfd5e/image/uploads_2F1552483361586-5d5fhueod4e-9827e8631b5a37cd3ad727b3cf6bb26b_2FCivics101Logo_LGwithBG.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
