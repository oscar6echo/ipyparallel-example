
import os
import shutil

class SetupIpp:
    """
    """

    def __init__(self,
                 ipython_dir,
                 cluster_id,
                 nb_core=[4],
                 local_packages=None,
                 ):
        """
        """
        self.ipython_dir = ipython_dir
        self.cluster_id = cluster_id
        self.nb_core = nb_core
        self.local_packages = local_packages

    def run(self):
        """
        """
        print(f'create ipyparallel scripts in {self.ipython_dir}')
        if not os.path.exists(self.ipython_dir):
            os.makedirs(self.ipython_dir)

        filename = 'launch_controller.sh'
        cmd = 'ipcontroller --ip="*" --ipython-dir={} --cluster-id={}'.format(
            self.ipython_dir,
            self.cluster_id
        )
        self.create_script(filename, cmd)

        if isinstance(self.nb_core, int):
            self.nb_core = [self.nb_core]

        for e in self.nb_core:
            filename = f'launch_engine-{e}.sh'
            cmd = 'ipcluster engines -n {} --ipython-dir={} --cluster-id={}'.format(
                e,
                self.ipython_dir,
                self.cluster_id
            )
            self.create_script(filename, cmd)

        if self.local_packages:
            print(f'copy {len(self.local_packages)} local packages to {self.ipython_dir}')
            for local_package in self.local_packages:
                print(f'\t{local_package}')
                src = local_package
                dst = os.path.join(self.ipython_dir, local_package)
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)

    def create_script(self, filename, cmd):
        print(f'\t{filename}')
        path = os.path.join(self.ipython_dir, filename)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(cmd)
