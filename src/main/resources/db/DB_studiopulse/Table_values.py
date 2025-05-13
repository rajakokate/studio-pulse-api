import sqlite3 as sql
con=sql.connect('studiopulse')
cur=con.cursor()

from get_query import load_queries
queries = load_queries('create-query.properties')

cur.execute(queries['Client_create_query'])
cur.execute(queries['Project_create_query'])
cur.execute(queries['Department_create_query'])
cur.execute(queries['User_create_query'])
cur.execute(queries['ProjectComment_create_query'])
cur.execute(queries['Shot_create_query'])
cur.execute(queries['ShotAssociation_create_query'])
cur.execute(queries['Comment_create_query'])

con.commit()
con.close()