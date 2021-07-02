# from player import Player
class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'
        if player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str):
        if player_name not in [x.name for x in self.players]:
            return f'Player {player_name} is not in the guild.'
        user = [x for x in self.players if x.name == player_name][0]
        self.players.remove(user)
        user.guild = 'Unaffiliated'
        return f'Player {player_name} has been removed from the guild.'


    def guild_info(self,):
        return f'Guild: {self.name}\n{"".join([x.player_info() for x in self.players])}'

       
