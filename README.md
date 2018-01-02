# JSteamPlaytimeCalculator
This Python Script is made with intention of calculating how much time is needed to finish every game in Steam library. 
The Python version which is used is Python 3.6. The JSON and Request modules are necessary.

The script utilizes the Steam API to get a list of all games in a users library. To do so you need a Steam API key, which you can acquire one on this site: https://steamcommunity.com/dev/apikey, and your Steam ID. By default your Steam ID is part of your Steam profile link (e.g. http://steamcommunity.com/profiles/"YOUR STEAM ID"). If you are using a custom url you can resolve your Steam ID on this site: https://www.steamidfinder.com/. 

After fetching the Steam appID's of the games in the users library API requests are made to the Steamspy.com API (steamspy.com/api.php). A API key is not required. The maximal allowed requests are 4 per second. My script isn't locked to 4 requests per second but I never had a problem with that and locking down the requests, locally, to 4 per second would make the script slower. Steamspy tracks the total avarage per player playtime of the game since 2009. I'm using that as an estimate for how long it would take to finish the game. There are other services that are superior to Steamspy for getting that data (for example https://howlongtobeat.com/ or https://www.igdb.com/) but they don't have an API or dont allow requests on an estimate for how long it would take to finish the game. Scraping directly from the website would be an alternative but both sites use AJAX so thats not ideal.

The time the script needs varies from a few seconds to a few minutes based on how many games you have in your library. 
