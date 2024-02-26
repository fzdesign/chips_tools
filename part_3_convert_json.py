import cc_classes
import cc_dat_utils
import json

parsed_json = json.load(open('data/fanxuanz_cc1.json'))
level_pack = cc_classes.CCLevelPack()
level=cc_classes.CCLevel()
level.level_number = 1 #replace with parsed json
level.time = level_time=60
level.level_pack = level_pack

level_pack.add_level(level)
cc_dat_utils.write_cc_level_pack_to_dat(level_pack, "my.dat")







