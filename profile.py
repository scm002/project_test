#!/usr/bin/env python
# -*-coding: utf-8 -*-

"""The script is going to get some information:

    about environment variants
    WORKSPACE/JENKINS_URL/JAVA_HOME

"""

import os
import shutil

RESULT = os.path.join(os.environ["WORKSPACE"], "result")


class GetEnvVar(object):

    def __init__(self):
        pass

    def run_var(self):
        for k, v in os.environ.items():
            with open(os.path.join(RESULT,  "profile.txt"), "a") as f:
                f.writelines((k, " ", v, "\n"))


def main():
    print "WORKSPACE: %s" % os.environ["WORKSPACE"]
    if os.path.exists(os.environ["WORKSPACE"]):
        print "Remove: %s" % os.environ["WORKSPACE"]
        shutil.rmtree(os.environ["WORKSPACE"])
    print "Creating Dir:%s" % RESULT
    os.makedirs(RESULT)
    os.chdir(RESULT)

    env_var = GetEnvVar()
    print "Writing ENV into .profile..."
    env_var.run_var()

if __name__ == '__main__':
    main()
