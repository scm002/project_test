#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-20 11:34:39
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

"""The script is going to get all dirs and files from the path you

provides for us

"""

import os

CUR_PATH = os.getcwd()


class GetFiles(object):
    """docstring for GetFiles"""
    def __init__(self, path):
        self.path = path

    def run_cmd(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                print root, file


def main():
    print "We are fetching all files in current directory:"
    files = GetFiles(CUR_PATH)
    files.run_cmd()

if __name__ == '__main__':
    main(

