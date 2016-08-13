from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker


class State(object):
    pass


class Db(object):
    '''class with operations to be one on the db
    '''

    def __init__(self, db_path):
        '''connect to the db with given path and start the session
        '''

        engine = create_engine('sqlite:///{path}'.format(path=db_path))

        metadata = MetaData(engine)
        state = Table('state', metadata, autoload=True)
        mapper(State, state)

        Session = sessionmaker(bind=engine)
        self.make_session = Session

    def latest_data(self):
        '''return the latest set of data saved in the database
        '''
        session = self.make_session()
        res = self.row_to_dict(session.query(State).order_by(State.id.desc()).first())
        session.close()
        return res

    def get_loc_data(self, loc):
        session = self.make_session()
        res = session.query(State).filter(State.location == loc)\
            .order_by(State.id.desc()).first()
        session.close()
        if res:
            res = self.row_to_dict(res)
        return res

    def row_to_dict(self, row):
        '''convert row result to a dictionary
        '''
        return {'id': row.id, 'humidity': row.humidity,
                'temperature': row.temperature, 'pressure': row.pressure,
                'altitude': row.altitude, 'location': row.location,
                'timestamp': row.timestamp}
