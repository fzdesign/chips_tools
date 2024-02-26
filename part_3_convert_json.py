import cc_classes
import cc_dat_utils
import json

parsed_json = json.load(open('data/fanxuanz_cc1.json'))
level_pack = cc_classes.CCLevelPack()
level= cc_classes.CCLevel()
level.level_number = parsed_json['levels'][0]['level_number']
level.time = level_time= parsed_json['levels'][0]['time']
level.num_chips= parsed_json['levels'][0]['num_chips']
level.upper_layer= parsed_json['levels'][0]['upper_layer']
level.add_field(cc_classes.CCEncodedPasswordField(parsed_json['levels'][0]['password']))
level.add_field(cc_classes.CCMapHintField(parsed_json['levels'][0]['hint']))
level.add_field(cc_classes.CCMapTitleField(parsed_json['levels'][0]['title']))
#level.add_field(cc_classes.CCCoordinate(parsed_json['levels'][0]['monster']))
level_pack.add_level(level)
cc_dat_utils.write_cc_level_pack_to_dat(level_pack, "my.dat")







