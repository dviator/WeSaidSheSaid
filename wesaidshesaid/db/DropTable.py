import psycopg2

conn = psycopg2.connect("dbname=wsss user=wsss")

cur = conn.cursor()

cur.execute("""DROP TABLE Speeches;
	DROP TABLE Candidates;""")

conn.commit()

cur.close()
conn.close()