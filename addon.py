from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.megaphone.fm/PPY1168790592"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/63ccd1d6-34f5-11e7-b527-335db86cfd5e/image/uploads_2F1552483361586-5d5fhueod4e-9827e8631b5a37cd3ad727b3cf6bb26b_2FCivics101Logo_LGwithBG.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/63ccd1d6-34f5-11e7-b527-335db86cfd5e/image/uploads_2F1552483361586-5d5fhueod4e-9827e8631b5a37cd3ad727b3cf6bb26b_2FCivics101Logo_LGwithBG.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
