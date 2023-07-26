import requests
from bs4 import BeautifulSoup
#url we scrape
URL = "https://forecast.weather.gov/MapClick.php?lat=39.3327&lon=-76.6337"

#makes url readable i think
page = requests.get(URL)

#parses url
soup = BeautifulSoup(page.content, "html.parser")

#filters search area to contentArea
results = soup.find(class_="contentArea")

#filters further to current-conditions
weather_element = results.find("div", id="current-conditions")

#pulls name of location
location = weather_element.find("h2", class_="panel-title").text

#pulls current temp
curr_temp = weather_element.find("p", class_="myforecast-current-lrg").text.strip()

#pulls table of weather data
table = weather_element.find_all("table")[0].find_all("tr")

#create list to put items from table
table_list = []

#dictionary for results
weather_info ={"Location" : location,
               "Temperature" : curr_temp
               }

#goes through each point in data table? idk what they're called exactly
for i in table:

    #goes through each child of i
    for child in i.children:

        #only add content that is relevant to the list
        if child.text != '\n':
            table_list.append(child.text.strip())

#add items from the list to the dictionary, every other item is the key for the item to its right [1, "one", 2, "two"] -> {1 : "one", 2 : "two"}
#i can probably do this simpler but ¯\_(ツ)_/¯ i'll figure it out at some point
for i in range(0, len(table_list), 2):

    #add current item from list as key, with immediate next item as value
    weather_info[table_list[i]] = table_list[i + 1]

#prints weather_info pretty and formatted and stuff
for datatype, value in weather_info.items():
    print("{}: {}".format(datatype, value))