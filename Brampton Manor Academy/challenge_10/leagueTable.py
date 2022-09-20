import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

class formatData:
    def teamData(csvData):
        teamData = {}
    
        for game in csvData:
            home = game[1]
            away = game[2]
            
            homeGoals = int(game[3])
            awayGoals = int(game[4])
            
            winner = game[5]

            homeShots = int(game[7])
            awayShots = int(game[8])
            homeShotsOnTarget = int(game[9])
            awayShotsOnTarget = int(game[10])
            
            homeFouls = int(game[11])
            awayFouls = int(game[12])

            if home not in teamData:
                teamData[home] = {
                    "wins": 0,
                    "draws": 0,
                    "losses": 0,
                    "points": 0,
                    "shots": 0,
                    "shotsOnTarget": 0,
                    "accuracy": 0,
                    "goalDiff": 0,
                    "fouls": 0
                }
            if away not in teamData:
                teamData[away] = {
                    "wins": 0,
                    "draws": 0,
                    "losses": 0,
                    "points": 0,
                    "shots": 0,
                    "shotsOnTarget": 0,
                    "accuracy": 0,
                    "goalDiff": 0,
                    "fouls": 0
                }

            if winner == "D":
                teamData[home]["draws"] += 1
                teamData[away]["draws"] += 1

                teamData[home]["points"] += 1
                teamData[away]["points"] += 1          
            elif winner == "H":
                teamData[home]["wins"] += 1
                teamData[home]["points"] += 3

                teamData [away]["losses"] += 1
            elif winner == "A":
                teamData[away]["wins"] += 1
                teamData[away]["points"] += 3
            
                teamData[home]["losses"] += 1

            teamData[home]["shots"] = homeShots
            teamData[away]["shots"] = awayShots
            teamData[home]["shotsOnTarget"] = homeShotsOnTarget
            teamData[away]["shotsOnTarget"] = awayShotsOnTarget
            
            teamData[home]["goalDiff"] += homeGoals - awayGoals
            teamData[away]["goalDiff"] += awayGoals - homeGoals

            teamData[home]["fouls"] += homeFouls
            teamData[away]["fouls"] += awayFouls

            # teamData[home]["cards"] += (homeRed * 2) +  homeYellow
            # teamData[away]["cards"] += (awayRed * 2) + awayYellow
        
        for team in teamData:
            teamData[team]["accuracy"] = teamData[team]["shotsOnTarget"] / teamData[team]["shots"]
        
        return teamData
    
    def refereeData(csvData):
        refereeData = {}
        
        for game in csvData:            
            referee = game[6]
            homeYellow = int(game[15])
            awayYellow = int(game[16])
            homeRed = int(game[17])
            awayRed = int(game[18])

            if referee not in refereeData:
                refereeData[referee] = {
                    "yellow": 0,
                    "red": 0,
                    "cards": 0,
                    "cardAverage": 0,
                    "games": 0
                }
            
            refereeData[referee]["yellow"] += homeYellow + awayYellow
            refereeData[referee]["red"] += homeRed + awayRed
            refereeData[referee]["cards"] += (homeRed * 2) + homeYellow + (awayRed * 2) + awayYellow
            refereeData[referee]["games"] += 1

        for referee in refereeData:
            refereeData[referee]["cardAverage"] = refereeData[referee]["cards"] / refereeData[referee]["games"]

        return refereeData

class sort:
    def points(teamData):
        return sorted(teamData, key = lambda x: teamData[x]['points'], reverse = True)
    def accuracy(teamData):
        return sorted(teamData, key = lambda x: teamData[x]['accuracy'], reverse = True)
    def fouls(teamData):
        return sorted(teamData, key = lambda x: teamData[x]['fouls'], reverse = True)
    def cards(refereeData):
        return sorted(refereeData, key = lambda x: refereeData[x]['cardAverage'], reverse = True)

def table(teamData):
    sortedPoints = sort.points(teamData)
    
    headerValues = ["team", "points", "wins", "losses", "draws", "goal difference", "fouls"]
    print(f'{headerValues[0]:>9} {headerValues[1]:>12} {headerValues[2]:>5} {headerValues[3]:>7} {headerValues[4]:>6} {headerValues[5]:>17} {headerValues[6]:>7}')
    for team in sortedPoints:
        nameLength = len(team)        
        
        points = teamData[team]["points"]
        wins = teamData[team]["wins"]
        losses = teamData[team]["losses"]
        draws = teamData[team]["draws"]
        goalDiff = teamData[team]["goalDiff"]
        fouls = teamData[team]["fouls"]
        print(f"{team} {points:>{19 - nameLength}} {wins:>6} {losses:>6} {draws:>6} {goalDiff:>11} {fouls:>14}")

def singleData(teamData, refereeData):
    accuracy = sort.accuracy(teamData)
    fouls = sort.fouls(teamData)
    cards = sort.cards(refereeData)
    print(f"Most accurate team: {accuracy[0]}")
    print(f"Least accurate team: {accuracy[-1]}")
    print(f"Dirtiest team: {fouls[0]}")
    print(f"Cleanest team: {fouls[-1]}")
    print(f"Referee with highest card average per game: {cards[0]}")
    print(f"Referee with lowst card average per game: {cards[-1]}")
    

if __name__ == "__main__":
    csvData = read_csv(csv_file)
    teamData = formatData.teamData(csvData)
    refereeData = formatData.refereeData(csvData)
    table(teamData)
    singleData(teamData, refereeData)