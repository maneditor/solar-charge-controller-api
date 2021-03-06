from utils.mongo import MongoDB
from datetime import datetime
import pprint


def get_date ():
    today = datetime.now()
    return "{Y}-{M}-{D}".format(
        Y=today.year,
        M=today.month,
        D=today.day
    )

class Power:
    @staticmethod
    def save (power, time):
        MongoDB.get_db().power.insert_one({
            'power': power,
            'created_date': datetime.utcnow(),
            'date': get_date(),
            'time': time
        })

    @staticmethod
    def get ():
        power = MongoDB.get_db().power.find_one()
        if power:
            del power['_id']
        return power

    @staticmethod
    def get_by_date(date = get_date(), end=None):
        query = {
            'date': {
                '$gte': date,
                '$lt': end
            } if end else date
        }
        results = MongoDB.get_db().power.find(query)
        powerData = [{
            'power': result.get('power'),
            'time': result.get('time')
        } for result in results]
        print(powerData)
        return powerData
