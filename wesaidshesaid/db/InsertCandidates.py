import psycopg2

conn = psycopg2.connect("dbname=wsss user=wsss")

cur = conn.cursor()
#Have to figure out how to escape O'Malley
# ('Martin J. O'Malley', 'Martin', "O'Malley", 'J.','Democrat'),

cur.execute("""INSERT INTO Candidates (fullName, validNames, first, last, middle, party) VALUES
	('Marco Rubio', ARRAY['Marco Rubio', 'Senator Marco Rubio'],'Marco', 'Rubio','','Republican'),
	('Carly Fiorina', ARRAY['Carly Fiorina', 'Mrs. Carly Fiorina'], 'Fiorina', 'Carly','','Republican'),
	('Ted Cruz', ARRAY['Ted Cruz', 'Senator Ted Cruz'], 'Cruz', 'Ted','','Republican'),
	('Scott Walker', ARRAY['Scott Walker', 'Gov. Scott Walker', 'Governor Scott Walker'], 'Walker', 'Scott','','Republican'),
	('Bernie Sanders', ARRAY['Bernie Sanders', 'Senator Bernie Sanders', 'Bernard Sanders'], 'Sanders', 'Bernie','','Democrat'),
	('Hillary Rodham Clinton', ARRAY['Hillary Rodham Clinton', 'Hillary Clinton'], 'Clinton', 'Hillary', 'Rodham', 'Democrat'),
	('John R. Kasich', ARRAY['John R. Kasich', 'Governor John R. Kasich', 'John Kasich', 'Governor John Kasich'], 'Kasich', 'John', 'R.', 'Republican'),
	('Chris Christie', ARRAY['Chris Christie', 'Governor Chris Christie'], 'Christie', 'Chris','','Republican'),
	('Ben Carson', ARRAY['Ben Carson', 'Benjamin Carson, Sr.', 'Dr. Ben Carson', 'Ben Carson, M.D.'], 'Carson', 'Ben','','Republican'),
	('Jeb Bush', ARRAY['Jeb Bush'], 'Bush', 'Jeb','','Republican'),
	('Jim Gilmore', ARRAY['Jim Gilmore'], 'Gilmore', 'Jim','','Republican'),
	('Lindsey Graham', ARRAY['Lindsey Graham'], 'Graham', 'Lindsey','','Republican'),
	('Mike Huckabee', ARRAY['Mike Huckabee'], 'Huckabee', 'Mike','','Republican'),
	('Bobby Jindal', ARRAY['Bobby Jindal'], 'Jindal', 'Bobby','','Republican'),
	('George Pataki', ARRAY['George Pataki'], 'Pataki', 'George','','Republican'),
	('Rand Paul', ARRAY['Rand Paul'], 'Paul', 'Rand','','Republican'),
	('Rick Perry', ARRAY['Rick Perry'], 'Perry', 'Rick','','Republican'),
	('Rick Santorum', ARRAY['Rick Santorum'], 'Santorum', 'Rick','','Republican'),
	('Joe Biden', ARRAY['Joe Biden'], 'Biden', 'Joe','','Democrat'),
	('Lincoln Chafee', ARRAY['Lincoln Chafee'], 'Chafee', 'Lincoln','','Democrat'),
	('Bill de Blasio', ARRAY['Bill de Blasio'], 'de Blasio', 'Bill','','Democrat'),
	('Jim Webb', ARRAY['Jim Webb'], 'Webb', 'Jim','','Democrat'),
	('Donald Trump', ARRAY['Donald Trump', 'The Don', 'Sir Trump', 'His Trumpness'], 'Trump', 'Donald','','Weasel');"""
)


conn.commit()

cur.close()
conn.close()
