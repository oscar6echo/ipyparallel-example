

import os
import json
import time
import gc

import numpy as np
import pandas as pd


from timeit import default_timer as timer


class Collect:
    """
    """

    def __init__(self,
                 list_id,
                 root_dir,
                 folder_out,
                 file_out,
                 verbose=True,
                 ):
        """
        """
        self.list_id = list_id
        self.root_dir = root_dir
        self.folder_out = folder_out
        self.file_out = file_out
        self.verbose = verbose

    def run(self):
        """
        """
        if self.verbose:
            print(f'collecting {len(self.list_id)} files')

        results = []
        for id in self.list_id:
            path = os.path.join(self.root_dir,
                                self.folder_out,
                                self.file_out.format(id))
            with open(path, 'r', encoding='utf-8') as f:
                dic = json.loads(f.read())
            results.append(dic['res'])

        avg = np.mean(results)
        return avg
