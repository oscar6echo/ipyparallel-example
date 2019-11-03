
import os
import json
import shutil

import numpy as np
import pandas as pd


class BuildData:
    """
    """

    def __init__(self,
                 data_dir,
                 N,
                 base=3):
        """
        """

        self.data_dir = data_dir
        self.N = N
        self.base = base

    def run(self):
        """
        """

        folder = os.path.join(self.data_dir,
                              'sample-data')
        data = np.random.randint(low=0,
                                 high=1000,
                                 size=int(1e5))
        chunks = np.split(data, 100)[:self.N]

        print(f'create {len(chunks)} files of integers between 0 and 1000')

        if os.path.exists(folder):
            print(f'delete existing folder {folder}')
            shutil.rmtree(folder)

        print(f'create folder {folder}')
        os.makedirs(folder)

        name = 'common.json'
        path = os.path.join(folder, name)
        print(f'create file {name} (with offset={self.base}) in folder {folder}')
        with open(path, 'w', encoding='utf-8') as f:
            dic = {
                'base': self.base,
            }
            f.write(json.dumps(dic))
        print(f'\t{os.path.basename(path)}')

        print(f'create {len(chunks)} files in folder {folder}')
        for k, v in enumerate(chunks):
            path = os.path.join(folder, f'data-{k}.json')
            with open(path, 'w', encoding='utf-8') as f:
                dic = {
                    'idx': k,
                    'data': [int(e) for e in v]
                }
                f.write(json.dumps(dic))
            print(f'\t{os.path.basename(path)}')
