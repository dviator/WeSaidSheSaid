import psycopg2

conn = psycopg2.connect("dbname=wsss user=wsss")

cur = conn.cursor()
#Have to figure out how to escape O'Malley
# ('Martin J. O'Malley', 'Martin', "O'Malley", 'J.','Democrat'),

cur.execute("""INSERT INTO Candidates (fullName, first, last, middle, party) VALUES
	('Marco Rubio', 'Marco', 'Rubio','','Republican'),
	('Carly Fiorina', 'Fiorina', 'Carly','','Republican'),
	('Ted Cruz', 'Cruz', 'Ted','','Republican'),
	('Scott Walker', 'Walker', 'Scott','','Republican'),
	('Bernie Sanders', 'Sanders', 'Bernie','','Democrat'),
	('Hillary Rodham Clinton', 'Clinton', 'Hillary', 'Rodham', 'Democrat'),
	('John R. Kasich', 'Kasich', 'John', 'R.', 'Republican'),
	('Chris Christie', 'Christie', 'Chris','','Republican'),
	('Ben Carson', 'Carson', 'Ben','','Republican'),
	('Jeb Bush', 'Bush', 'Jeb','','Republican'),
	('Jim Gilmore', 'Gilmore', 'Jim','','Republican'),
	('Lindsey Graham', 'Graham', 'Lindsey','','Republican'),
	('Mike Huckabee', 'Huckabee', 'Mike','','Republican'),
	('Bobby Jindal', 'Jindal', 'Bobby','','Republican'),
	('George Pataki', 'Pataki', 'George','','Republican'),
	('Rand Paul', 'Paul', 'Rand','','Republican'),
	('Rick Perry', 'Perry', 'Rick','','Republican'),
	('Rick Santorum', 'Santorum', 'Rick','','Republican'),
	('Joe Biden', 'Biden', 'Joe','','Democrat'),
	('Lincoln Chafee', 'Chafee', 'Lincoln','','Democrat'),
	('Bill de Blasio', 'de Blasio', 'Bill','','Democrat'),
	('Jim Webb', 'Webb', 'Jim','','Democrat'),
	('Donald Trump', 'Trump', 'Donald','','Weasel');"""
)


conn.commit()

cur.close()
conn.close()
