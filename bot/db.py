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
        self.session = Session()

    def latest_data(self):
        '''return the latest set of data saved in the database
        '''
        return self.row_to_dict(self.session.query(State).order_by(State.id.desc()).first())

    def row_to_dict(self, row):
        '''convert row result to a dictionary
        '''
        return {'id': row.id, 'humidity': row.humidity,
                'temperature': row.temperature, 'pressure': row.pressure,
                'altitude': row.altitude, 'location': row.location,
                'timestamp': row.timestamp}
