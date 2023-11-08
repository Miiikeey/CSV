def players(name, score):
    print(name, score)
    return

list_of_players = []
#open file to write

playing = 1
number_of_players = int(input("How many players: "))
while playing <= number_of_players:
    name = (input("Name: "))
    score = int(input("Score: "))
    playing += 1
    player_info = name, score
    list_of_players.append(player_info)


f = open("golf.txt", "w")
f.write(str(list_of_players))
f.close()


