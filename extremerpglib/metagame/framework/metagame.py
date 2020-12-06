"""
"""
from extremerpglib.grammar import SimpleGrammar
from extremerpglib.utils.printme import printme

import json
import os


class MetaGame:
    def __init__(self):
        pass

    def load_game_data(self, game_file_data):
        with open(game_file_data, 'r') as json_file:
            game_data = json.load(json_file)

        if 'game_template' in game_data:
            if game_data['game_template'] == 'text-generation':
                printme(SimpleGrammar.parse(game_data))

    def load_game(self, game_files):
        printme("MetaGame:load_game - " + str(game_files), debug=True)
        if game_files.__class__ == list:
            for game_file in game_files:
                self.load_game(game_file)
        elif os.path.isdir(game_files):
            self.load_game(list(map(lambda x: os.path.join(game_files, x), sorted(os.listdir(game_files)))))
        else:
            self.load_game_data(game_files)
