#! /usr/bin/env python3

import os, sys


def make_dirs():
    root = os.getcwd()
    folders = {
        'data': ['csv', 'dfs'],
        'exploration': [],
        'figures': ['plots', 'scripts'],
        'helpers': [],
        'statistics': [],
    }

    for parent, subs in folders.items():
        os.mkdir(os.path.join(root, parent))
        for sub in subs:
            os.mkdir(os.path.join(root, parent, sub))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        make_dirs()
    elif len(sys.argv) == 2:
        os.mkdir(sys.argv[1])
        os.chdir(sys.argv[1])
        make_dirs()
    else:
        raise ValueError('expdir takes only 0 or 1 arguments.')

    print('Done.')
