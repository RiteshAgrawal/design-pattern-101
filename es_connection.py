
class Elasticsearch(object):
    def __init__(self, config):
        self.config = config

class ESConnection(object):
    connection = None
    @classmethod
    def get_connection(cls):
        if not cls.connection:
            connection = Elasticsearch({})
            cls.connection = connection
        return cls.connection

if __name__ == '__main__':
    e = ESConnection().get_connection()
    print(id(e))
    f = ESConnection().get_connection()
    print(id(f))
    print(e is f)

