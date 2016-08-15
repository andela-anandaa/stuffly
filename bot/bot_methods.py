from _firebase.db import Db
from _firebase.config import config


fb_url = config['firebase']
rootRef = '/sample/status/'

_db = Db(fb_url)


def temperature(loc='valhalla'):
    loc = loc.lower()
    if loc == 'valhalla' or loc == 'valhala':
        # loc = 'valhalla' # for misspelling
        return _db.latest_data("{}/{}".format(rootRef, loc))['temperature']
    return False

def humidity(loc='valhalla'):
    loc = loc.lower()
    if loc == 'valhalla' or loc == 'valhala':
        return _db.latest_data("{}/{}".format(rootRef, loc))['humidity']
    return False

def is_stuffy(loc):
    loc = loc.lower()
    if loc == 'valhalla' or loc == 'valhala':
        loc = 'valhalla' # for misspelling
        data = _db.get_loc_data(loc)
        if data:
            if data['humidity'] < 30 or data['humidity'] > 60:
                return True
            else:
                return False
    return None
