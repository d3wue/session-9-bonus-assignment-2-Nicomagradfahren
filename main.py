import requests
import bs4
userAgent = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

url ="https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1"

print("1: Show available teams")
print("2: Select team and show high level information on the team")
print("3: Select team and and show all players of the team")
print("4: Stop the program")

def player_names(urlwunsch):
    r = requests.get(urlwunsch, headers=userAgent)
    htmlText = r.text
    htmlDocument = bs4.BeautifulSoup(htmlText, "html.parser")
    search = {'class': 'inline-table'}
    players = htmlDocument.find_all('table', search)
    for player in players:
        nameofplayer = player.get_text()
        print(nameofplayer)

while True:
    choice = int(input())
    if choice == 1:
        r = requests.get(url, headers=userAgent)
        htmlText = r.text
        htmlDocument = bs4.BeautifulSoup(htmlText, "html.parser")
        table = htmlDocument.find('table', {'class': 'items'}).find('tbody')
        teams = table.find_all('tr')
        for i in range(len(teams)):
            team = teams[i]
            name = team.find('td', {'class': 'hauptlink no-border-links'}).text.strip()
            print(f"{i}: {name}")
    elif choice == 2:
        teamChoice = int(input("Give the index of the team you are interested in (note they start with 0)\n"))
        r = requests.get(url, headers=userAgent)
        htmlText = r.text
        htmlDocument = bs4.BeautifulSoup(htmlText, "html.parser")
        table = htmlDocument.find('table', {'class': 'items'}).find('tbody')
        teams = table.find_all('tr')
        team = teams[teamChoice]
        info = team.find_all("td", {"class": "zentriert"})
        marketValue = team.find_all("td", {"class": "rechts"})
        squad = info[1].text
        age = info[2].text
        foreigners = info[3].text
        averageMV = marketValue[0].text
        totalMV = marketValue [1].text
        print(f"For the team with index {teamChoice}:\nmembers: {squad} \naverage age: {age} \nNumber of Foreigners: {foreigners} \nAverage value: {averageMV} \nTotal value: {totalMV}")
    elif choice == 3:
        while True:
            choice2 = int(input("Give the index of the team you are interested in (note they start with 0)\n"))
            if choice2 == 0:
                urlwunsch = "https://www.transfermarkt.com/fc-bayern-munchen/startseite/verein/27/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 1:
                urlwunsch = "https://www.transfermarkt.com/bayer-04-leverkusen/startseite/verein/15/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 2:
                urlwunsch = "https://www.transfermarkt.com/rasenballsport-leipzig/startseite/verein/23826/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 3:
                urlwunsch = "https://www.transfermarkt.com/borussia-dortmund/startseite/verein/16/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 4:
                urlwunsch = "https://www.transfermarkt.com/vfl-wolfsburg/startseite/verein/82/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 5:
                urlwunsch = "https://www.transfermarkt.com/vfb-stuttgart/startseite/verein/79/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 6:
                urlwunsch = "https://www.transfermarkt.com/eintracht-frankfurt/startseite/verein/24/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 7:
                urlwunsch = "https://www.transfermarkt.com/borussia-monchengladbach/startseite/verein/18/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 8:
                urlwunsch = "https://www.transfermarkt.com/sc-freiburg/startseite/verein/60/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 9:
                urlwunsch = "https://www.transfermarkt.com/1-fc-union-berlin/startseite/verein/89/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 10:
                urlwunsch = "https://www.transfermarkt.com/tsg-1899-hoffenheim/startseite/verein/533/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 11:
                urlwunsch = "https://www.transfermarkt.com/fc-augsburg/startseite/verein/167/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 12:
                urlwunsch = "https://www.transfermarkt.com/1-fsv-mainz-05/startseite/verein/39/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 13:
                urlwunsch = "https://www.transfermarkt.com/sv-werder-bremen/startseite/verein/86/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 14:
                urlwunsch = "https://www.transfermarkt.com/1-fc-koln/startseite/verein/3/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 15:
                urlwunsch = "https://www.transfermarkt.com/vfl-bochum/startseite/verein/80/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 16:
                urlwunsch = "https://www.transfermarkt.com/1-fc-heidenheim-1846/startseite/verein/2036/saison_id/2023"
                player_names(urlwunsch)
                break
            if choice2 == 17:
                urlwunsch = "https://www.transfermarkt.com/sv-darmstadt-98/startseite/verein/105/saison_id/2023"
                player_names(urlwunsch)
                break

    elif choice == 4:
        break
    else:
        print("Invalid Option!")

#for i in range(len(teams)):
#    team = teams[i]
#    name = team.find('td', {'class': 'hauptlink no-border-links'}).text.strip()
#    info = team.find_all("td", {"class": "zentriert"})
#    squad = info[1].text
#    age = info[2].text
#    foreigners = info[3].text
#    marketValue = team.find_all("td", {"class": "rechts"})
#    averageMV = marketValue[0].text
#    totalMV = marketValue [1].text
#    print(f"{i}:{name} {squad} {age} {foreigners} {averageMV} {totalMV}")
        
# Lösung wo nur Manu Neuer angezeigt wird
#         elif choice == 3:
 #       r = requests.get(url2, headers=userAgent)
  #      htmlText = r.text
   #     htmlDocument = bs4.BeautifulSoup(htmlText, "html.parser")
#
 #       table2 = htmlDocument.find('table', {'class': 'items'}).find('tbody')
  #      
   #     players = table2.find_all('tr')
    #    for i in range(len(players)):
     #       player = players[i]
      #      playername = player.find('td', {'class': 'hauptlink'}).text.strip()
       #     print(f"{i}: {playername}")
        
  # lösung wo zu viel html gesraped wird       
 #r = requests.get(url2, headers=userAgent)
  #      htmlText = r.text
   #     htmlDocument = bs4.BeautifulSoup(htmlText, "html.parser")
    #    search = {'class': 'hauptlink'}
     #   players = htmlDocument.find_all('td', search)
      #  print(players)
