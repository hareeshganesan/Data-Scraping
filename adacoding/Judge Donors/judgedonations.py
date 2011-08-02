from BeautifulSoup import BeautifulSoup


def printer(x):
	print x['name']
	print x['loc']
	print x['employer']
	print x['recip']
	for i in x['donations']:
		print i


def writer(f,x):
	row = x['name']+'|'+x['loc']+'|'+x['employer']+'|'+x['recip']
	for i in x['donations']:
		f.write(row+'|'+i['date']+'|'+i['amount']+'|'+i['id']+'\n')
		
data = []
for i in range(6):
	i+=1
	f = open('raw_files/FEC Individual Contribution Search Results'+str(i)+'.html', 'r')
	s = f.read()
	soup = BeautifulSoup(''.join(s))
	f.close()
	ind = 0
	

	while ind < len(soup.contents):
		r1 ={}
		r1['name'] = soup.contents[ind].string.strip()
		r1['loc'] = soup.contents[ind+2].string.strip()
		r1['employer'] = soup.contents[ind+4].string.strip()
		print r1['name']
		table = soup.contents[ind+8].contents[1]
		r1['recip'] = table.contents[0].contents[0].contents[1].string
		donations = []		
		for i in range(len(table.contents)-1):
			i+=1
			donation = {}	
			if(table.contents[i] != '\n'):
				donation['date'] = table.contents[i].contents[1].string
				print donation['date']
				donation['amount'] = table.contents[i].contents[3].string
				donation['id'] = table.contents[i].contents[5].contents[0].string
				donations.append(donation)
		r1['donations'] = donations
		data.append(r1)
	

		ind += 11

f = open('judgedonations_final.csv', 'w')
for i in data:
	printer(i)
	writer(f,i)




