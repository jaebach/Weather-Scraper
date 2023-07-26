import requests
from bs4 import BeautifulSoup

URL = "https://forecast.weather.gov/MapClick.php?lat=39.3327&lon=-76.6337"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="contentArea")
weather_element = results.find("div", id="current-conditions")

location = weather_element.find("h2", class_="panel-title").text

curr_temp = weather_element.find("p", class_="myforecast-current-lrg").text.strip()

table = weather_element.find_all("table")[0].find_all("tr")
table_arr = []
weather_info ={"Location" : location,
               "Temperature" : curr_temp
               }
for i in table:
    for child in i.children:
        if child.text != '\n':
            table_arr.append(child.text.strip())
for i in range(0, len(table_arr), 2):
    weather_info[table_arr[i]] = table_arr[i + 1]
print(weather_info)
