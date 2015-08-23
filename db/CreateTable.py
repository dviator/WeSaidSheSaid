import psycopg2

conn = psycopg2.connect("dbname=wsss user=wsss")

cur = conn.cursor()

cur.execute("""CREATE TABLE Speeches (
	url	varchar(100) primary key,
	title varchar(100),
	speaker varchar(50),
	collectionTime timestamp,
	speechTime timestamp,
	city varchar(30),
	state varchar(30));""")

conn.commit()

cur.close()
conn.close()