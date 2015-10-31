import psycopg2

conn = psycopg2.connect("dbname=wsss user=wsss")

cur = conn.cursor()

cur.execute("""DROP TABLE IF EXISTS Speeches;
	DROP TABLE IF EXISTS Candidates; DROP TABLE IF EXISTS RunStats;""")

conn.commit()

cur.close()
conn.close()