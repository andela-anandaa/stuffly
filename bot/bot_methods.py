from db import Db

_db = Db('../arduino/arduino.db3')

def temperature(loc='valhalla'):
    loc = loc.lower()
    if loc == 'valhalla' or loc == 'valhala':
        return _db.latest_data()['temperature']
    return False

def humidity(loc='valhalla'):
    loc = loc.lower()
    if loc == 'valhalla' or loc == 'valhala':
        return _db.latest_data()['humidity']
    return False

def is_stuffy(loc):
    loc = loc.lower()
    if loc == 'valhalla' or loc == 'valhala':
        loc = 'valhala' # hack until it's fixed
        data = _db.get_loc_data(loc)
        if data:
            if data['humidity'] < 30 or data['humidity'] > 60:
                return True
            else:
                return False
    return None
