from txtgamelib.metagame.framework.gametemplate import GameTemplate
from txtgamelib.grammar import SimpleGrammar
from txtgamelib.utils.printme import printme


class BranchBasedTextGenerationTemplate(GameTemplate):
    START_KEY = '__init__'

    def __init__(self):
        self.game_data = {}
        self.current_narrative_chunk = {}

    @staticmethod
    def verify_template(game_data):
        return 'game_template' in game_data and game_data['game_template'] == 'branch_based_interactive_fiction' and \
               BranchBasedTextGenerationTemplate.START_KEY in game_data

    def load_game_data(self, game_data):
        printme('__init__:BranchBasedTextGenerationTemplate:load_game_data ' + str(game_data), debug=True)
        self.game_data = game_data
        self.current_narrative_chunk = self.game_data[self.START_KEY]

    def play_game(self):
        printme('__init__:BranchBasedTextGenerationTemplate:play_game', debug=True)
        self.play_current_story_chunk()

    def play_current_story_chunk(self):
        chunk_text_exists = True
        current_text_index = 0
        while chunk_text_exists:
            printme(SimpleGrammar.parse(self.current_narrative_chunk, target_tag='text' + str(current_text_index)))
            current_text_index += 1
            chunk_text_exists = ('text' + str(current_text_index)) in self.current_narrative_chunk
        chunk_options = self.current_narrative_chunk.get('options', None)

        printme("Options available: %s" % (chunk_options,), debug=True)

        # Condition to finish current IF game
        if chunk_options is None:
            exit()

        options_data = {}

        for option in chunk_options:
            printme(" %s: %s" % (option['key'], option['text']))
            options_data[option['key']] = option['next_chunk']

        user_option = self.get_command()
        user_option = user_option.strip()
        next_story_chunk_tag = options_data.get(user_option, None)

        if next_story_chunk_tag is None or next_story_chunk_tag not in self.game_data:
            exit()

        self.current_narrative_chunk = self.game_data[next_story_chunk_tag]
        self.play_current_story_chunk()

    def get_command(self):
        user_command = input(">> ")
        return user_command
