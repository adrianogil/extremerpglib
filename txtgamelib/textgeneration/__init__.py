from extremerpglib.metagame.framework.gametemplate import GameTemplate
from extremerpglib.grammar import SimpleGrammar
from extremerpglib.utils.printme import printme


class TextGenerationTemplate(GameTemplate):
    def __init__(self):
        self.game_data = {}

    @staticmethod
    def verify_template(game_data):
        return 'game_template' in game_data and game_data['game_template'] == 'text_generation'

    def load_game_data(self, game_data):
        printme('__init__:TextGenerationTemplate:load_game_data ' + str(game_data), debug=True)
        self.game_data = game_data

    def play_game(self):
        printme('__init__:TextGenerationTemplate:play_game', debug=True)
        printme(SimpleGrammar.parse(self.game_data))
