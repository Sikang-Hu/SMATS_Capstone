from __future__ import absolute_import
from __future__ import print_function

import os
import subprocess
import sys


def runner(file, stat):
    """
    file: the name of configuration file
    stat: output statistic result such as RouteLength, WaitingTime, etc.
    """
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
        com = ""
    retcode = subprocess.call(
        [sumoBinary, "-c", file, com], stdout=sys.stdout, stderr=sys.stderr)
    print(">> Simulation closed with status %s" % retcode)
    sys.stdout.flush()