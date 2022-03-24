from bs4 import BeautifulSoup as BS
import requests as req

source = req.get("https://kamar.lbc.school.nz/index.php/attendance").text

soup = BS(source, "html.parser")

data = str(soup.find_all()).splitlines()

for line in data:

    if "max" in line.lower():

        print(line)
