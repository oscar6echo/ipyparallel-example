
import os
import shutil


def runtime(t0, t1, newline=True):
    """
    """
    if newline:
        print('')
    print(f'runtime = {t1-t0:,.2f} s')


def file_content(path, show_path=True):
    """
    """
    if show_path:
        print(path)

    with open(path, 'r') as f:
        content = f.read()
    print(content)


def clear_output(shared_dir, folder_out, verbose=True):
    """
    """
    path = os.path.join(shared_dir,
                        folder_out)
    if verbose:
        print(f'delete output folder {path}')

    shutil.rmtree(path)
