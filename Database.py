import psycopg2

host = "localhost"
dbname = "PR"
user = "postgres"
password = ""
sslmode = "require"

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
    host, user, dbname, password, sslmode)

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

# cursor.execute("DROP TABLE IF EXISTS PR;")

cursor.execute(
    "CREATE TABLE IF NOT EXISTS PR (id serial PRIMARY KEY, service VARCHAR(30), password VARCHAR(255));")

class DB:
    @staticmethod
    def Create(Service, Password):
        cursor.execute(f"INSERT INTO PR (service, password) VALUES ('{Service}', '{Password}');")
        print(f'-- Password saved --\nService: {Service}, Password: {Password}')

        conn.commit()

    @staticmethod
    def Get(Service):
        cursor.execute(f"SELECT service, password FROM PR WHERE service = '{Service}';")
        rows = cursor.fetchall()
        for row in rows:
            print(f'--  Password found --\nService:{row[0]}, Password: {row[1]}')

    @staticmethod
    def Die():
        cursor.close()
        conn.close()