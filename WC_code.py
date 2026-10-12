

import easygui


# Dictionary.
groups = {
    "A":{"Mexico":3.5, "Korea_Republic":0.30, "France":14.26, 
         "South Africa":0.10},
    "B":{"Canada":0.40, "Switzerland":1.20, "Norway":3.50, "Argentina":10.40}, 
    "C":{"Brazil":6.60, "Marocco":1.10, "Scotland":0.20, "Portugal":7.00},
    "D":{"USA":1.20,"Australia":0.30,"Paraguay":0.30,"Colombia":0.60},
    "E":{"Germany":5.00, "England":11.2, "Ecuador":1.40, "Curacao":0.01},
    "F":{"Netherlands":6.00, "Japan":1.70, "Sweden":0.60, "Croatia":0.70},
    "G":{"Egypt":0.10, "IR Iran":0.10, "Belgium":2.40, "New Zealand":0.01},
    "H":{"Spain":9.80, "Uruguay":0.70, "Cabo Verde":0.02, "Saudi Arabia":0.10},
}

easygui.msgbox("""Hi. This program is based on a knockout system of countries 
participating in the FIFA 2026 World Cup, having five stages: Group Stage,
Round of 16, Quarterfinals, Semifinals, and Final.\n\n 

At the end of each stage,a list of the countries that you chose before will 
appear, meaning that those countries have advanced to the next stage. \n\n

What you need to do is simple in this program, will appear, informations like 
the Group, Match number, percentage of win in 2026 Wolrd Cup, and both teams 
that will face each other. You will click on one of the two boxes at the bottom 
in the middle of the program and choose who will win between those two 
countries. This process will continue until the Final that you will choose 
one of the two to be the FIFA 2026 World Cup winner.""")

def get_percentage(team):
    for group in groups.values():
        if team in group:
            return group[team]

# Code to play a Match
def play_match(team1, team2, title):

    percentage1 = get_percentage(team1)
    percentage2 = get_percentage(team2)

    winner = easygui.buttonbox(
        title="2026 FIFA Wolrd Cup",
        msg=f"""{title}

{team1}: {percentage1}%

VS 

{team2}: {percentage2}%""",
        choices=[team1, team2]
    )

    return winner
# code to play the group stage.
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
"""
)

        winners.append(winner)

        match_number += 1

    return winners

# List containing all countries who passed to the Knokkout stage.
def show_teams(team_list, title, message):
    teams_formatted_list = "\n".join(
        [f" - {team}" for team in team_list]
    )

    easygui.msgbox(
        msg=f"{message}\n\n{teams_formatted_list}",
        title=title
    )
    
qualified_teams = []

# Code to play Knockout.
def play_knockout(team_list):
    """this is a docstring and should explain what the function does"""
    winners = []

    match = 1
    # Code containing variables to create a loop.
    for i in range(0, len(team_list), 2):

        team1 = team_list[i]
        team2 = team_list[i+1]

        winner = play_match(
            team1,
            team2,
            f"""
Knockout

Match {match}
"""
)

        winners.append(winner)

        match += 1

    return winners

def main():

    while True:

        qualified_teams = []

        for group in groups:
            winners = play_group(group)
            qualified_teams.extend(winners)

# List for the countries who have qualified for the round of 16.

        teams_formatted_list = "\n".join(
        [f"- {team}" for team in qualified_teams]
        )

        easygui.msgbox(
            msg=f"""The following teams have qualified for the 
            Round of 16: \n\n{teams_formatted_list}
            """)

        current_round = play_knockout(qualified_teams)

# List for the countries who have qualified for the quarterfinals.

        teams_formatted_list = "\n".join(
            [f"-{team}" for team in current_round]
        )

        easygui.msgbox(
            msg=f"""The following teams have qualified for the 
            Quarterfinals:\n\n{teams_formatted_list}   
        """)

        current_round = play_knockout(current_round)

# List for the countries who have qualified for the Semifinals.

        teams_formatted_list = "\n".join(
            [f"- {team}" for team in current_round]
        )

        easygui.msgbox(
            msg=f"""The following teams have qualified for the 
            Semifinals:\n\n{teams_formatted_list}
        """)

        current_round = play_knockout(current_round)

# List for the countries who have qualified for the finals.

        teams_formatted_list = "\n".join(
            [f"- {team}" for team in current_round]
        )

        easygui.msgbox(
            msg=f"""The following teams have qualified for the 
            Final:\n\n{teams_formatted_list}
        """)

        current_round = play_knockout(current_round)

# will show what country is the World Cup Champion.
        easygui.msgbox(
        f"""

        WORLD CHAMPION

        {current_round[0]}

        """
        )

        choice = easygui.buttonbox(
            msg="Thank you for playing!\n\nWould you like to play again?",
            title="Wolrd Cup Knockout",
            choices=["Replay", "Exit"]
        )

        if choice == "Replay":
            continue

        else:
            break
        
main()
