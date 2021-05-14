import os
import json

config_dict = {'DLA34.json':
                  {'dataset':
                      {'11class': ['None'],
                       '2class' : ['None'],
                      }
                  },
               'HG52.json':
                   {'dataset':
                       {'11class': ['bilinear', 'bicubic'],
                        '2class' : ['bilinear'],
                       }
                   },
               'HG104.json':
                   {'dataset':
                        {'11class': ['bilinear', 'bicubic'],
                         '2class': ['bilinear'],
                         }
                    }
               }


class JSON_manipulator(object):
    def __init__(self, name):
        self.name = name
        self.path = os.path.join("config", name)

    def read_file(self):
        with open(self.path) as f:
            self.data = json.load(f)

    def write_file(self):
        with open(self.path, 'w') as json_file:
            json.dump(self.data, json_file)

    def main(self, dataset, interpolation):

        self.read_file()

        self.data['db']['categories'] = int(dataset.split("class")[0])
        self.data['db']['interpolation_mode'] = interpolation

        self.write_file()



def main():
    splits = ['validation', 'testing']

    for config_file in os.listdir("config"):
        if not config_file.endswith("-multi_scale.json"):

            current_config = config_dict[config_file]

            for dataset in current_config['dataset']:
                for interpolation in current_config['dataset'][dataset]:

                    # change config file to current settings
                    J = JSON_manipulator(config_file)
                    J.main(dataset, interpolation)
                    # run script
                    for split in splits:
                        strs = "python test.py --cfg_file {} --split {}".format(config_file.split(".json")[0],
                                                                                split
                                                                                )
                        os.system(strs)


if __name__ == '__main__':
    main()