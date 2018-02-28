#! /usr/bin/env python3

import os, sys


def make_dirs():
    root = os.getcwd()
    folders = {
        'experiment_code': [],
        'data': ['csv', 'dfs'],
        'exploration': [],
        'figures': ['plots', 'scripts'],
        'helpers': [],
        'statistics': [],
    }

    for parent, subs in folders.items():
        os.makedirs(os.path.join(root, parent), exist_ok=True)
        if len(subs) == 0:
            open(os.path.join(root, parent, 'README.md'), 'a').close()
        else:
            for sub in subs:
                os.makedirs(os.path.join(root, parent, sub), exist_ok=True)
                open(os.path.join(root, parent, sub, 'README.md'), 'a').close()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        make_dirs()
    elif len(sys.argv) == 2:
        os.makedirs(sys.argv[1], exist_ok=True)
        os.chdir(sys.argv[1])
        make_dirs()
    else:
        raise ValueError('expdir takes only 0 or 1 arguments.')

    print('Done.')
