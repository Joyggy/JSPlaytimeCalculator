'''
This script is made by Joyggy and is available under the Gnu General Public License v3.
I would appreciate it if you could link to my Github Account (https://github.com/Joyggy) when using my code in your
projects but the license doesn't forces you to do so.
'''

import json # The Steam API and the Steamspy API use JSON as there output format. This library is used to filter those
            # outputs.
import requests #Get requests are used to connect to the Steam API and the Steamspy API.

'''This function is used to make a list ("appIdList") which contains all appID's of the games which are in the users 
library.
@param (the input) steamId : The Steam ID of the user whom you want to scan.
               steamApiKey : The authorisation key you need to use the steam api.
@return appIdList: A list of all app ids from the users library as a list.
'''
def getLibrary(steamId, steamApiKey):
    # This line is used to make a get request to the Steam API with the users Steam API key and steamID.
    # The output of the API is formated into a dictionary with the JSON module.
    Json = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + str(steamApiKey) +
                        "&steamid=" + str(steamId) + "&format=json").json()
    #The next two lines create a list ("steamIdlist") with the appID's from all games of the users library.
    appIdList = [x['appid']
    for x in Json['response']['games']]
    return appIdList

'''
@param appIdList: The appIDs from the users library saved in a list. 
@return avaragePlaytimeSum: The avarage playtime of every game from the users library summed up.
'''
def getAveragePlaytime(appIdList):
    averagePlaytimeSum = 0 #Base value for the calculations.
    for AppId in appIdList:
        # This line is used to make a get request to the Steamspy.com API with a appID from the "appIdList" list.
        Json = requests.get("https://steamspy.com/api.php?request=appdetails&appid=" + str(AppId)).json()
        # This lines summes up the avarage total playtime provided by the Steamspy.com API.
        averagePlaytimeSum = averagePlaytimeSum + Json['average_forever']
    return averagePlaytimeSum

print("Wellcome to Joyggy's Python Steam Total Required Playtime Callculator", "/n",
      "This script uses the official Steam API and the Steamspy.com API.", "/n",
      "You need a Steam API key to use the API.")

steamApiKey = input("Please enter your Steam Api key: ") #Prompts for the users Steam API
steamId = input("Please enter the Steam ID of the user from which you want to scan the library: ")#Prompts for a steamID
print("The script can take some time depending on how big the users library is.")

appIdList = getLibrary(steamId, steamApiKey) #Calls the function with the users input
averagePlaytimeSum = getAveragePlaytime(appIdList)
averagePlaytimeSumOutput = round(averagePlaytimeSum / 60, 1) #Rounds the variable to one decimal point.

print("The playtime needed to finish every game in the users library is: ")
print(str(averagePlaytimeSumOutput) + " hours")

