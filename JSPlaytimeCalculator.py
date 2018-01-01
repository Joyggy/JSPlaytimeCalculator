'''
JSPlaytimeCalculator by Joyggy
Version 1.0

This script is available under the Gnu General Public License v3.
I would appreciate a it if you could link to my Github Account (https://github.com/Joyggy) when using my code in your projects but the license doesn't forces you to do so.
'''

import json #The Steam API and the Steamspy API use JSON as there output format. This library is used to filter those outputs.
import requests #Get requests are used to connect to the Steam API and the Steamspy API.

#This function is used to make a list ("appIdList") which contains all appID's of the games which are in the users library.
def getLibrary(steamId, steamApiKey):
    Json = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + str(steamApiKey) + "&steamid=" + str(steamId) + "&format=json").json() #This line is used to make a get request to the Steam API with the users Steam API key and steamID. The output of the API is formated into a dictionary with the JSON module.
    #The next two lines create a list ("steamIdlist") with the appID's from all games of the users library.
    appIdList = [x['appid']
    for x in Json['response']['games']]
    return appIdList

#This function is using the appID's from the list "appIdList" to get the avarage total playtime of the games in the list (that data provided by the Steamspy API). Those values are summed up in the "avaragePlaytimeSum" variable.
def getAveragePlaytime(appIdList):
    averagePlaytimeSum = 0 #Base value for the calculations.
    for AppId in appIdList:
        Json = requests.get("https://steamspy.com/api.php?request=appdetails&appid=" + str(AppId)).json() #This line is used to make a get request to the Steamspy.com API with a appID from the "appIdList" list.
        averagePlaytimeSum = averagePlaytimeSum + Json['average_forever'] #This lines summes up the avarage total playtime provided by the Steamspy.com API.
    return averagePlaytimeSum

print("Wellcome to Joyggy's Python Steam Total Required Playtime Callculator", "/n",
      "This script uses the official Steam API and the Steamspy.com API.", "/n",
      "You need a Steam API key to use the API.")

steamApiKey = input("Please enter your Steam Api key: ") #Prompts for the users Steam API
steamId = input("Please enter the Steam ID of the user from which you want to scan the library: ") #Prompts for a Steam ID
print("The script can take some time depending on how big the users library is.")

appIdList = getLibrary(steamId, steamApiKey) #Calls the function with the users input
averagePlaytimeSum = getAveragePlaytime(appIdList)
averagePlaytimeSumOutput = round(averagePlaytimeSum / 60, 1) #Rounds the variable to one decimal point.

print("The playtime needed to finish every game in the users library is: ")
print(str(averagePlaytimeSumOutput) + " hours")

