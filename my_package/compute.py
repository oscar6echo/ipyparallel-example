

import os
import json
import time
import gc

import numpy as np
import pandas as pd


from timeit import default_timer as timer


class Compute:
    """
    """

    def __init__(self,
                 id,
                 root_dir,
                 folder_in,
                 folder_out,
                 file_in_common,
                 file_in,
                 file_out,
                 verbose=True,
                 ):
        """
        """
        self.root_dir = root_dir
        self.id = id
        self.folder_in = folder_in
        self.folder_out = folder_out
        self.file_in_common = file_in_common
        self.file_in = file_in.format(self.id)
        self.file_out = file_out.format(self.id)
        self.verbose = verbose

        self.duration = 1

    def setup(self):
        """
        """
        if self.verbose:
            print(f'start setup id={self.id}')
        path = os.path.join(self.root_dir,
                            self.folder_in,
                            self.file_in_common)
        with open(path, 'r', encoding='utf-8') as f:
            dic = json.loads(f.read())
        self.base = dic['base']

        path = os.path.join(self.root_dir,
                            self.folder_in,
                            self.file_in)
        with open(path, 'r', encoding='utf-8') as f:
            dic = json.loads(f.read())

        idx = dic['idx']
        assert idx == self.id, 'Wrong file'

        self.data = dic['data']

    def run(self):
        """
        """
        if self.verbose:
            print(f'start run id={self.id}')
        t0 = timer()
        df = pd.DataFrame(data=self.data)
        avg = df.mean().iloc[0]
        self.res = {
            'base': self.base,
            'avg': avg,
            'res': self.base + avg,
        }
        time.sleep(self.duration)
        t1 = timer()
        if self.verbose:
            print(f'end run id={self.id} - time={t1-t0:,.2f}')

        # clear memory
        del df
        gc.collect()

        return self.res

    def save(self):
        """
        """
        if not os.path.exists(os.path.join(self.root_dir,
                                           self.folder_out)):
            os.makedirs(os.path.join(self.root_dir,
                                     self.folder_out))

        if self.verbose:
            print(f'start save id={self.id}')
        path = os.path.join(self.root_dir,
                            self.folder_out,
                            self.file_out.format(self.id))
        with open(path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.res))

        # clear memory
        del self.res
        gc.collect()
