from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


brightStarsUrl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(brightStarsUrl)
print(page)

soup = bs(page.text, "html.parser")

starTable = soup.find("table")

tempList= []
tableRows = starTable.find_all("tr")
for tr in tableRows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    tempList.append(row)



StarNames = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(tempList)):
    StarNames.append(tempList[i][1])
    Distance.append(tempList[i][3])
    Mass.append(tempList[i][5])
    Radius.append(tempList[i][6])
    Lum.append(tempList[i][7])
    
df2 = pd.DataFrame(list(zip(StarNames, Distance, Mass, Radius, Lum)), columns=["StarName", "Distance", "Mass", "Radius", "Luminosity"])
print(df2)

df2.to_csv("brightStars.csv")