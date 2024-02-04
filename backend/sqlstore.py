import psycopg2


#using alloydb
def connect():
    return psycopg2.connect(
        dbname='alloydb',
        user
        ='alloy',
        password='alloy',
        host='localhost'
    )

#using alloydb
def init():
    conn = connect()
    cur = conn.cursor()
    """Video  table
        videoid : string
        title : string
        description : string

    """
    cur.execute('''
        CREATE TABLE IF NOT EXISTS video (
            videoid TEXT PRIMARY KEY,
            title TEXT,
            description TEXT
        )
    ''')
    
    cur.close()
    conn.commit()
    conn.close()
