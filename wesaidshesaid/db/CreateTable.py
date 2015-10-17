import psycopg2

conn = psycopg2.connect("dbname=wsss user=wsss")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Speeches (
	url	varchar(100) primary key,
	title varchar(100),
	speaker varchar(50),
	transcription text,
	collectionTime timestamp(0),
	speechTime Date,
	city varchar(30),
	state varchar(30));""")

cur.execute("""CREATE TABLE IF NOT EXISTS Candidates (
	fullName varchar(50) primary key,
	validNames text[],
	first varchar(50),
	last varchar(50),
	middle varchar(50),
	party varchar(25));"""
	)


conn.commit()

cur.close()
conn.close()