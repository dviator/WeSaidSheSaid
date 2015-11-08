import psycopg2

conn = psycopg2.connect("dbname=wsss user=wsss")

cur = conn.cursor()
#Have to figure out how to escape O'Malley
# ('Martin J. O'Malley', 'Martin', "O'Malley", 'J.','Democrat'),

query = "INSERT INTO Candidates(fullName, validNames, first, last, middle, party) VALUES (%s, %s, %s, %s, %s, %s);"

# data = ('Marco Rubio', ['Marco Rubio', 'Senator Marco Rubio'],'Marco', 'Rubio','','Republican')
data = (
	('Marco Rubio', ['Marco Rubio', 'Senator Marco Rubio'],'Marco', 'Rubio','','Republican'),
	('Carly Fiorina', ['Carly Fiorina', 'Mrs. Carly Fiorina'], 'Fiorina', 'Carly','','Republican'),
	('Ted Cruz', ['Ted Cruz', 'Senator Ted Cruz'], 'Cruz', 'Ted','','Republican'),
	('Scott Walker', ['Scott Walker', 'Gov. Scott Walker', 'Governor Scott Walker'], 'Walker', 'Scott','','Republican'),
	('Bernie Sanders', ['Bernie Sanders', 'Senator Bernie Sanders', 'Bernard Sanders'], 'Sanders', 'Bernie','','Democrat'),
	('Hillary Rodham Clinton', ['Hillary Rodham Clinton', 'Hillary Clinton'], 'Clinton', 'Hillary', 'Rodham', 'Democrat'),
	('John R. Kasich', ['John R. Kasich', 'Governor John R. Kasich', 'John Kasich', 'Governor John Kasich'], 'Kasich', 'John', 'R.', 'Republican'),
	('Chris Christie', ['Chris Christie', 'Governor Chris Christie'], 'Christie', 'Chris','','Republican'),
	('Ben Carson', ['Ben Carson', 'Benjamin Carson, Sr.', 'Dr. Ben Carson', 'Ben Carson, M.D.'], 'Carson', 'Ben','','Republican'),
	('Jeb Bush', ['Jeb Bush'], 'Bush', 'Jeb','','Republican'),
	('Jim Gilmore', ['Jim Gilmore'], 'Gilmore', 'Jim','','Republican'),
	('Lindsey Graham', ['Lindsey Graham'], 'Graham', 'Lindsey','','Republican'),
	('Mike Huckabee', ['Mike Huckabee'], 'Huckabee', 'Mike','','Republican'),
	('Bobby Jindal', ['Bobby Jindal'], 'Jindal', 'Bobby','','Republican'),
	('George Pataki', ['George Pataki'], 'Pataki', 'George','','Republican'),
	('Rand Paul', ['Rand Paul'], 'Paul', 'Rand','','Republican'),
	('Rick Perry', ['Rick Perry'], 'Perry', 'Rick','','Republican'),
	('Rick Santorum', ['Rick Santorum'], 'Santorum', 'Rick','','Republican'),
	('Joe Biden', ['Joe Biden'], 'Biden', 'Joe','','Democrat'),
	('Lincoln Chafee', ['Lincoln Chafee'], 'Chafee', 'Lincoln','','Democrat'),
	('Donald Trump', ['Donald Trump', 'The Don', 'Sir Trump', 'His Trumpness', 'Donald J. Trump'], 'Trump', 'Donald','','Weasel'),
	("Martin J. O'Malley", ["Martin O'Malley", "Martin J. O'Malley"], "O'Malley", 'Martin','J.','Democrat'),
	('Jim Webb', ['Jim Webb'], 'Webb', 'Jim','','Democrat'),
	('Bill de Blasio', ['Bill de Blasio'], 'de Blasio', 'Bill','','Democrat')
	)
cur.executemany(query, data)

conn.commit()

cur.close()
conn.close()
