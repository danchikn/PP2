import psycopg2
conn = psycopg2.connect(host = "localhost", database = "sla", user = "postgres", password = "/s8,cntrlN")
current = conn.cursor()

current.execute("""
CREATE TABLE PhoneBook (name varchar, 
number varchar);
""")
current.close()
conn.commit()
conn.close()