import json
from test_data import Game, GameLibrary

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( parsed ):
    #Initialize a new GameLibrary
    game_library = GameLibrary()
    for parsed_game in parsed["games"]:
        game = Game(title=parsed_game["title"], year=parsed_game["year"])
        game_library.add_game(game)
    return game_library


#Part 2
input_json_file = "data/test_data.json"
with open(input_json_file, 'r') as reader:
    library_json = json.load(reader)
    #print(libraryjson['games'][0]['title'])
    game_library = make_game_library_from_json(library_json)
    print(game_library)
### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
