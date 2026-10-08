import random
import time


homegoal={}
awaygoal={}

teams={}
team_data={
    "goal":0,
    "shot":0,
    "corner":0,
    "foul":0,
    "yellow":0
}

home=""
away=""
events=['shot','goal','nothing','foul','corner','yellow','nothing','nothing']
team=[]
hometeam=[]
awayteam=[]


def team_entry():
    global home
    global away
    home=input("Enter the home team: ")
    teams[home]=team_data.copy()
    away=input("Enter the away team: ")
    team.append(home)
    team.append(away)
    teams[away]=team_data.copy()
    for i in range(1,6):
        player=input(f"{home} player {i}: ")
        hometeam.append(player)
    for i in range(1,6):
        player=input(f"{away} player {i}: ")
        awayteam.append(player)


def shot():
    ranteam=random.choice(team)
    if ranteam==home:
        hplayer=random.choice(hometeam)
        print(f"{home} takes a shot- {hplayer}")
        teams[home]['shot']+=1
    elif ranteam==away:
        aplayer=random.choice(awayteam)
        print(f"{away} takes a shot- {aplayer}")
        teams[away]['shot']+=1



def goal():
    ranteam=random.choice(team)
    if ranteam==home:
        hplayer=random.choice(hometeam)
        print(f"Goal! {home}- {hplayer}")
        if hplayer not in homegoal:
            homegoal[hplayer]=1
        else:
            homegoal[hplayer]+=1
        teams[home]['goal']+=1
        teams[home]['shot']+=1
    elif ranteam==away:
        aplayer=random.choice(awayteam)
        print(f"Goal! {away}- {aplayer}")
        if aplayer not in awaygoal:
            awaygoal[aplayer]=1
        else:
            awaygoal[aplayer]+=1
        teams[away]['goal']+=1
        teams[away]['shot']+=1

def corner():
    ranteam=random.choice(team)
    if ranteam==home:
        print(f"Corner for {home}")
        teams[home]['corner']+=1
    elif ranteam==away:
        print(f"Corner for {away}")
        teams[away]['corner']+=1



def foul():
    ranteam=random.choice(team)
    if ranteam==home:
        print(f"Foul by {home}")
        teams[home]['foul']+=1
    elif ranteam==away:
        print(f"Foul by {away}")
        teams[away]['foul']+=1


def yellow_card():
    ranteam=random.choice(team)
    if ranteam==home:
        hplayer=random.choice(hometeam)
        print(f"Yellow Card for {home}-{hplayer}")
        teams[home]['yellow']+=1
    elif ranteam==away:
        aplayer=random.choice(awayteam)
        print(f"Yellow Card for {away}-{aplayer}")
        teams[away]['yellow']+=1



def match_statistics():
    for team,data in teams.items():
        print(f"{team}")
        print(f"Goals: {data['goal']}")
        print(f"Shots: {data['shot']}")
        print(f"Corners: {data['corner']}")
        print(f"Fouls: {data['foul']}")
        print(f"Yellow Card: {data['yellow']}")


def match():
    team_entry()
    for i in range(1,46):
        time.sleep(1)
        event=random.choice(events)
        if event!='nothing':
            if event=='shot':
                print(f"{i}'",end=" ")
                shot()
            elif event=='goal':
                print(f"{i}'",end=" ")
                goal()
            elif event=='foul':
                print(f"{i}'",end=" ")
                foul()
            elif event=='corner':
                print(f"{i}'",end=" ")
                corner()
            elif event=='yellow':
                print(f"{i}'",end=" ")
                yellow_card()
    print("_____HALF TIME_____")
    print(f"{home} {teams[home]['goal']} - {teams[away]['goal']} {away}")
    time.sleep(5)
    for i in range(46,91):
        time.sleep(1)
        event=random.choice(events)
        if event!='nothing':
            if event=='shot':
                print(f"{i}'",end=" ")
                shot()
            elif event=='goal':
                print(f"{i}'",end=" ")
                goal()
            elif event=='foul':
                print(f"{i}'",end=" ")
                foul()
            elif event=='corner':
                print(f"{i}'",end=" ")
                corner()
            elif event=='yellow':
                print(f"{i}'",end=" ")
                yellow_card()
    print("_____FULL TIME_____")
    print(f"{home} {teams[home]['goal']} - {teams[away]['goal']} {away}")
    time.sleep(2)
    match_statistics()
    print(f"{home} -")
    for i in homegoal:
        print(f"{i} Goals Scored {homegoal[i]}")
    print(f"{away} -")
    for i in awaygoal:
        print(f"{i} Goals Scored {awaygoal[i]}")


match()