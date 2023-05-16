#Initialize the typing prompt database to support CRUD opertaions, store user data for account creation, and create
#the leaderboard database

import time

class Game:

    def __init__(self):
        self.users = {}
        self.prompts = {}

    def get_players(self):
        return self.users

    def get_prompts(self):
        return self.prompts

    def add_player(self, player):
        self.users[player.get_username()] = player

    def delete_player(self, player):
        self.users.pop(player.username)

    def lookup_player(self, username):
        return self.users.get(username)

    def add_prompt(self, prompt):
        self.prompts[prompt.get_prompt_title()] = prompt


class Race:

    def __init__(self, player, prompt):
        self.ID = None
        self.username = player.get_username()
        self.player = player
        self.prompt = prompt
        self.time = None

    def start_race(self):
        print("Go! Type the following prompt: ")
        print(self.prompt.get_prompt())

        start = time.time()
        attempt = input()
        end = round(time.time() - start)

        wpm = ((len(self.prompt.get_prompt()) / 5) / (end / 60))
        print("Your time was: " + str(end) + " seconds or " + str(wpm) + " WPM.")
        self.time = end
        self.ID = 1


class Player:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.game_history = {}

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_game_history(self):
        return self.game_history

    def set_username(self, username):
        self.username = username

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def add_game(self, race):
        self.game_history[race.ID] = race


class Prompt:

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def get_prompt(self):
        return self.text

    def get_prompt_title(self):
        return self.title

