from firebase import firebase

class Db(object):

    def __init__(self, url):
        self.firebase = firebase.FirebaseApplication(url, None)

    def post_data(self, rootRef, data):
        if type(data) == dict:
            return self.firebase.post(rootRef, data)
        return False

    def get_data(self, rootRef):
        return self.firebase.get(rootRef, None)

    def latest_data(self, rootRef):
        data = self.firebase.get(rootRef, None)
        keys = data.keys()
        return data[keys[len(keys) - 1]]

    def get_loc_data(self, rootRef, loc):
        return self.latest_data("{}/{}".format(rootRef, loc))

