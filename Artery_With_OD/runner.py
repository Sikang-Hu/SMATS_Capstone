from __future__ import absolute_import
from __future__ import print_function

import os
import subprocess
import sys
import shutil
import re


def newcfg(old_cfg, new_cfg):
    """
    Generate a new configuration file and set the input and output.
    :param old_cfg:
    :param new_cfg:
    :return:
    """
    new_cfg = new_cfg + ".sumocfg"
    old_cfg = old_cfg + ".sumocfg"
    try:
        shutil.copy(old_cfg, new_cfg)
    except:
        print("Missing", old_cfg)

    file = open(new_cfg, "r")
    cfg = file.read()
    file.close()




def runner(file, stat):
    """
    file: the name of configuration file
    stat: output statistic result such as RouteLength, WaitingTime, etc.
    """
    file = file + ".sumocfg"
    if not os.path.isfile(file):
        print("Can't find " + file)
        return
    try:
        sys.path.append(os.path.dirname(
            __file__))  # tutorial in tests
        sys.path.append(os.path.join(os.environ.get("SUMO_HOME"), "tools"))
        from sumolib import checkBinary
    except ImportError:
        sys.exit(
            "please declare environment variable 'SUMO_HOME' as the root directory of your sumo installation (it should contain folders 'bin', 'tools' and 'docs')")

    sumoBinary = checkBinary('sumo')

    if stat:
        com = "--duration-log.statistics"
    else:
        com = "-"
    retcode = subprocess.call(
        [sumoBinary, "-c", file, com], stdout=sys.stdout, stderr=sys.stderr)
    print(">> Simulation closed with status %s" % retcode)
    sys.stdout.flush()