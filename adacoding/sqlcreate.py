import csv
import sqlite3
import uuid
import sys
def populate(inputData):
  read = csv.reader(open(inputData, 'rb'), delimiter = '|')
  disp_info = []

  conn = sqlite3.connect('/tmp/example')
  c = conn.cursor()
  c.execute('''create table cases (caseid text, background text, holding text, plaintiff boolean, ada boolean, type boolean, completed boolean)''')

  index=0
  for row in read:
	  if(index==0):
		  print row
	  index=1	
	  caseid = str(uuid.uuid4()).replace('-','')
	  print caseid
	  command =  "insert into cases values('"+caseid+"','"+row[7].replace("'","[ap]")+"','"+row[8].replace("'","[ap]")+"','FALSE','FALSE','FALSE','FALSE')"
	  c.execute(command)

  conn.commit()
  c.close()

  c = conn.cursor()
  c.execute('select * from cases order by plaintiff limit 2')
 
  print "\n\n"
  print c.fetchall()
def sqldump():
  f = open('results.csv','w')
  conn = sqlite3.connect('/tmp/example')
  c = conn.cursor()
  c.execute("select * from cases where completed='TRUE'")
  for row in c:
    f.write('| '.join(row))
if(sys.argv[1]=="populate"):
  populate(sys.argv[2])
if(sys.argv[1]=="dump"):
  sqldump()  
if(sys.argv[1]=="test"):
  print "test"