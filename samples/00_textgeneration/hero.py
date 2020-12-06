from txtgamelib.grammar import SimpleGrammar
from txtgamelib.utils.printme import printme


main_story_structure = {
    "text": ["Once upon a time, #brief_hero_description# #hero_action# a dragon"],
    "brief_hero_description": ["a powerful knight", "a misterious wizard", "a good and generous paladin"],
    "hero_action": ["was fighting throught the night with", "was dancing throught the night with"]
}

generated_story = SimpleGrammar.parse(main_story_structure)
printme(generated_story)
