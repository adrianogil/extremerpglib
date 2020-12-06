"""
"""
from extremerpglib.textgeneration import TextGenerationTemplate

from extremerpglib.utils.printme import printme

import json
import os


class MetaGame:
    def __init__(self):
        self.game_templates = [
            TextGenerationTemplate
        ]
        self.current_game = None

    def load_game_data(self, game_file_data):
        with open(game_file_data, 'r') as json_file:
            game_data = json.load(json_file)

        if self.current_game is None:
            for template in self.game_templates:
                printme("MetaGame:load_game_data - " + str(template) + ": " + str(template.verify_template(game_data)), debug=True)
                if template.verify_template(game_data):
                    self.current_game = template()
                    break

        if self.current_game:
            self.current_game.load_game_data(game_data)

    def load_game(self, game_files):
        printme("MetaGame:load_game - " + str(game_files), debug=True)
        if game_files.__class__ == list:
            for game_file in game_files:
                self.load_game(game_file)
        elif os.path.isdir(game_files):
            self.load_game(list(map(lambda x: os.path.join(game_files, x), sorted(os.listdir(game_files)))))
        else:
            self.load_game_data(game_files)

    def play(self):
        if self.current_game:
            self.current_game.play_game()
