from functions import Player
from functions import BasketballPlayer
from functions import FootballPlayer

kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)
lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2, rebounds=7.4, assists=7.2)
messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)


print(kev_dur.last_name)
print(kev_dur.rebounds)
print(kev_dur.weight_to_lbs())



print(messi.first_name)
print(messi.goals)
print(messi.weight_to_lbs())

print("-------------------------------------")

print("This is a players game, let's add some infos on your bball heroes!")

first_name = input("Who is your favorite Basketball Player (first name)?: ")
last_name = input("Please add his second name: ")
height_cm = input("Do you know his height in cm?: ")
points = input("Can you tell me how many points he scored last season?: ")
rebounds = input("Can you tell me how many rebounds he did last season?: ")
weight_kg = input("Can you tell me how much he weighs?: ")
assists = input("Can you tell me how much assists he did last season?: ")

#create a new player object
new_player = BasketballPlayer(first_name=first_name, last_name=last_name, height_cm=float(height_cm), points=points, rebounds=rebounds, weight_kg=float(weight_kg), assists=int(assists))


#aufgenommene daten sollen in einer text-file gespeichert werden
with open ("bball_players_list.txt", "w") as player_dictionary:
    player_dictionary.write(str(new_player.__dict__))


print("Player data now uploaded!")

print("Player's data: {0}".format(new_player.__dict__))

