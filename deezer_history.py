import requests
from datetime import datetime
import pytz

USER_AGENT = "Mozilla/5.0 (X11; Linux i686; rv:135.0) Gecko/20100101 Firefox/135.0"
HISTORY_SIZE = '100'
TZ = 'Europe/Zurich' #Timezone
ARL = ''
session = None

def init_deezer_session() -> None:
    global session
    header = {
        'Pragma': 'no-cache',
        'Origin': 'https://www.deezer.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': USER_AGENT,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://www.deezer.com/login',
        'DNT': '1',
    }
    session = requests.session()
    session.headers.update(header)
    session.cookies.update({'arl': ARL, 'comeback': '1'})

def get_history() -> None:
    global session
    url_get_csrf_token = "https://www.deezer.com/ajax/gw-light.php?method=deezer.getUserData&input=3&api_version=1.0&api_token="
    req = session.post(url_get_csrf_token)
    csrf_token = req.json()['results']['checkForm']
    history = session.post('https://www.deezer.com/ajax/gw-light.php?method=user.getSongsHistory&input=3&api_version=1.0&api_token={}'.format(csrf_token), json={'nb': HISTORY_SIZE, 'start': '0'})
    history_json = history.json()['results']
    for song in history_json['data']:
        date = datetime.fromtimestamp(song['TS'], pytz.timezone(TZ)).strftime('%d-%m-%Y %H:%M:%S')
        print(song['SNG_TITLE'] + ' - ' + song['ALB_TITLE'] + ' from ' + song['ART_NAME'] + ' | Started at ' + date  + ' and listened ' + song['DURATION'] + 's.')

if __name__ == '__main__':
    init_deezer_session()
    get_history()