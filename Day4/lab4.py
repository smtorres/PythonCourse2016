#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page
	
from bs4 import BeautifulSoup
import urllib2
import csv 

web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)
soup = BeautifulSoup(web_page.read())

#Open a .csv file
f = open('test.csv', 'wb')
my_writer = csv.DictWriter(f, fieldnames=("Name", "Subfield","Title","E-mail","Web-page"))
my_writer.writeheader()


subfields=soup.find_all('h3') #Get a list of all subfields.


#Function to get personal page and email from the professor's page

def profinfo_frompage(prof_address):
	prof_page=urllib2.urlopen(prof_address)
	prof_soup=BeautifulSoup(prof_page.read())
	prof_personalpage, prof_email= 'NA', 'NA'
	div = prof_soup.find('div', {'class' : 'field field-name-field-person-website field-type-link-field field-label-inline clearfix'})
	if div:
		prof_personalpage = div.find('a')['href']
	for a_tag in prof_soup.find_all('a'):
		try:
			if 'mailto' in a_tag['href'] and a_tag.string!='polisci@wustl.edu':
				prof_email=a_tag.string
		except:
			pass
	return {'email':prof_email,'personalpage':prof_personalpage}


#Function to write professor's information to a .csv file
def process_profinfo(div_tag,subfield):
	name=div_tag.a.string 
	subfield=subfield.string
	title=div_tag.contents[-1]
	prof_address='https://polisci.wustl.edu/'+div_tag.a['href']
	otherinfo=profinfo_frompage(prof_address)
	my_writer.writerow({"Name":name, "Subfield":subfield,"Title":title,"E-mail":otherinfo['email'],"Web-page":otherinfo['personalpage']})


#Loop through the subfields and write the info for all professors using the previous function		
for subfield in subfields:
	for sibling in subfield.next_siblings: #iterate over the siblings of the current subfield
		if sibling in subfields: 
			break #if the sibling is one of the subfields, the inner loop is broken
		else:
			try:
				process_profinfo(sibling,subfield)
			except:
				pass
	
f.close()
			
				
				
				
