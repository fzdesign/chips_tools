import cc_classes
import cc_dat_utils
import json

parsed_json = json.load(open('data/fanxuanz_chipschallenge.json'))
level_pack = cc_classes.CCLevelPack()
for level_j in parsed_json['levels']:
    level= cc_classes.CCLevel()
    level.level_number = level_j['level_number']
    level.time = level_time= level_j['time']
    level.num_chips= level_j['numberOfChips']
    level.upper_layer= level_j['upperLayer']
    level.add_field(cc_classes.CCEncodedPasswordField(level_j['password']))
    level.add_field(cc_classes.CCMapHintField(level_j['hintText']))
    level.add_field(cc_classes.CCMapTitleField(level_j['title']))

#level.add_field(cc_classes.CCCoordinate(parsed_json['levels'][0]['monster']))
#monsters = [cc_classes.CCCoordinate(monster["x"], monster["y"]) for monster in field["monster"]]
#level.add_field(cc_classes.CCMonsterMovementField(parsed_json['levels'][1]['monster']))

    level_pack.add_level(level)
cc_dat_utils.write_cc_level_pack_to_dat(level_pack, "my.dat")







