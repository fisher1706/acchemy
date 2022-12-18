from sqlalchemy import create_engine


engine = create_engine('sqlite:///db_05_01.sqlite', echo=False)


def direct_connection_use():
    query = 'SELECT 1'
    connection = engine.connect()
    print(type(connection), dir(connection))

    res = connection.execute(query)
    print(type(res))

    fetched_row = res.fetchone()

    connection.close()

    return fetched_row