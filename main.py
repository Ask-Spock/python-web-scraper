
###
# 1.run on all sitemap / website page
# 2.enter content to a file, the name should be the original file name maybe the title/
# 3.creat a function to remove scrip and other - the fucntion check how many script there are and running acordenly
# ##



import requests
from bs4 import BeautifulSoup

URL = 'http://www.ask-tal.co.il'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')


content = soup.find("div", {"class": "content"})


title = soup.title

#print(content)

file1 = open("myfile.html","w") 
fileText = str(content)
  
# \n is placed to indicate EOL (End of Line) 
file1.writelines(fileText) 
file1.close() #to change file access modes 


