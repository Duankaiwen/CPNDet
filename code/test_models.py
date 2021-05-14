#python test.py --cfg_file DLA34 --testiter 20000 --split testing
#python test.py --cfg_file DLA34 --testiter 20000 --split validation
#python test.py --cfg_file HG52 --testiter 30000 --split testing
#python test.py --cfg_file HG52 --testiter 30000 --split validation
#python test.py --cfg_file HG104 --testiter 30000 --split testing
#python test.py --cfg_file HG104 --testiter 30000 --split validation

python test.py --cfg_file HG52 --split testing

import os


config_dict = {'DLA34':
                   {'dataset':
                             {'11class': ['None'],
                              '2class' : ['None'],
                              }
                    },
               'HG52':
                   {'dataset':
                             {'11class': ['bilinear', 'bicubic'],
                              '2class' : ['bilinear'],
                              }
                    },
               'HG104': []}



for config_file in os.listdir("config"):
    if not config_file.endswith("-multi_scale.json"):


        current_config = config_dict[config_file]






# strs = ('pip install mmcv==0.6.2')
# os.system(strs)
#
#
#
# def open_change_json(name):
#     pass