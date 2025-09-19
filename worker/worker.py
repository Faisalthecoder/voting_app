import time
import redis
import psycopg2

r = redis.Redis(host="redis", port=6379)
conn = psycopg2.connect("dbname=postgres user=postgres password=postgres host=db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS votes (vote TEXT);")
conn.commit()

while True:
    vote = r.lpop("votes")
    if vote:
        cur.execute("INSERT INTO votes (vote) VALUES (%s);", (vote.decode("utf-8"),))
        conn.commit()
    time.sleep(1)

