from project import Game, Player, Race, Prompt

p1 = Player("alecgc", "a@hotmail.com", "luckycharms2")
prompt1 = Prompt("The Fox", "The quick brown fox jumped over the lazy dog.")

race1 = Race(p1, prompt1)
race1.start_race()
