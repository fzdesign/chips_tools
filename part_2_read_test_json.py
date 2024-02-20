import json
import test_data

def make_game_library_from_json(json_data):
    game_library = test_data.GameLibrary()
    games = json_data["games"]

    for game in games:

        new_game = test_data.Game(game["title"], test_data.Platform(name=game['platform']['name'],launch_year=game['platform']['launch year']), game['year'])

        game_library.add_game(new_game)

    return game_library

input_json_file = "data/test_data.json"
with open(input_json_file, 'r') as reader:
    game_data = json.load(reader)
    #print(libraryjson['games'][0]['title'])
    game_info = make_game_library_from_json(game_data)
    print(game_info)
### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
