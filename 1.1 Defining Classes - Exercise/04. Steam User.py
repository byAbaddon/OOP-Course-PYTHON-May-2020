class SteamUser:
    played_hours = 0

    def __init__(self, username : str , games : list):
        self.username = username
        self.games = games 

    def play(self, game, hours):
        if game in self.games:
            SteamUser.played_hours += hours
            return f'{self.username} is playing {game}'
        return f'{game} is not in library'

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f'{self.username} bought {game}'
        return f'{game} is already in your library'    

    def stats(self):
        return f'{self.username} has {len(self.games)} games. Total play time: {SteamUser.played_hours}'    

