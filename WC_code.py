# football = {"NZ":6.9,"Belgium":81,"Egypt":33.9,"IR Iran":38.2}
# print(football)

# test = easygui.buttonbox("Who will win?", choices = ["NZ", "Belgium"])
# football.pop(test)
# print(football)

# new_team = easygui.enterbox("What country do you want to add?")
# new_percentage = float(easygui.enterbox("What is their percentage chances?"))
# football[new_team]=new_percentage
# print(football)

# def hello(name):
# print(f"good day to you {name}")
 # hello("gustavo")


import easygui

groups = {
    "A":{"Mexico":0, "Korea_Republic":0, "France":0, "South Africa":0},
    "B":{"Canada":0, "Switzerland":0, "Norway":0, "Argentina":0}, 
    "C":{"Brazil":0, "Marocco":0, "Scotland":0, "Portugal":0},
    "D":{"USA":0,"Australia":0,"Paraguay":0,"Colombia":0},
    "E":{"Germany":0, "England":0, "Ecuador":0, "Curacao":0},
    "F":{"Netherlands":0, "Japan":0, "Sweden":0, "Croatia":0},
    "G":{"Egypt":0, "IR Iran":0, "Belgium":0, "New Zealand":0},
    "H":{"Spain":0, "Uruguay":0, "Cabo Verde":0, "Saudi Arabia":0},
}


def play_match(team1, team2, title):

    winner = easygui.buttonbox(
        title="2026 FIFA Wolrd Cup",
        msg=title,
        choices=[team1, team2]
    )
    # add one to the dictionary value for that team here
    
   

    return winner

def play_group(group_name):

    teams = list(groups[group_name].keys())

    winners = []

    match_number = 1

    for i in range(0, len(teams), 2):

        team1 = teams[i]
        team2 = teams[i+1]

        winner = play_match(
            team1,
            team2,
            f"""
Group {group_name}

Match {match_number}

{team1}

VS

{team2}
"""
        )

        winners.append(winner)

        match_number += 1

    return winners

def show_teams(team_list, title, message):
    teams_formatted_list = "\n".join(
        [f" - {team}" for team in team_list]
    )

    easygui.msgbox(
        msg=f"{message}\n\n{teams_formatted_list}",
        title=title
    )
    
qualified_teams = []

def play_knockout(team_list):

    winners = []

    match = 1

    for i in range(0, len(team_list), 2):

        team1 = team_list[i]
        team2 = team_list[i+1]

        winner = play_match(
            team1,
            team2,
            f"""
Knockout

Match {match}

{team1}

VS

{team2}
""",
        )

        winners.append(winner)

        match += 1

    return winners

qualified_teams = []

for group in groups:
    winners = play_group(group)
    qualified_teams.extend(winners)

teams_formatted_list = "\n".join(
    [f"- {team}" for team in qualified_teams]
)

easygui.msgbox(
    msg=f"The following team have qualified for the Round of 16: \n\n{teams_formatted_list}",
    title="Round of 16"
)

current_round = play_knockout(qualified_teams)

teams_formatted_list = "\n".join(
    [f"-{team}" for team in current_round]
)

easygui.msgbox(
    msg=f"The following teams have qualified for the Quarterfinals:\n\n{teams_formatted_list}",   
)

current_round = play_knockout(current_round)

teams_formatted_list = "\n".join(
    [f"- {team}" for team in current_round]
)

easygui.msgbox(
    msg=f"The following teaams have qualified for the Semifinals:\n\n{teams_formatted_list}",
    title="Semifinals"
)

current_round = play_knockout(current_round)

teams_formatted_list = "\n".join(
    [f"- {team}" for team in current_round]
)

easygui.msgbox(
    msg=f"The following teams have qualified for the Final:\n\n{teams_formatted_list}",
    title="Final"
)

current_round = play_knockout(current_round)

easygui.msgbox(

    f"""

WOLRD CHAMPION

{current_round[0]}

"""
)



