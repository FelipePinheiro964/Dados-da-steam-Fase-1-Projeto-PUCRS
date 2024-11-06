f = open("steam_games.csv", "r")


for line in f:
  linhas = line.strip().split(';')
  print(linhas[:2])


f.close()