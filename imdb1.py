from bs4 import BeautifulSoup
import requests
import csv

r=requests.get("https://www.imdb.com/chart/top")
soup=BeautifulSoup(r.content,"lxml")
#print(soup.text)

csv_file=open("Movies2.csv","w")
csv_write=csv.writer(csv_file)
csv_write.writerow(["Movie"])

list=soup.find_all("td",class_="titleColumn")
for x in list:
    for y in x.find_all("a"):
        print(y.text)
        csv_write.writerow([y.text])
csv_file.close()