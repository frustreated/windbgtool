import sys
import os
import logging

import windbgtool.debugger

from optparse import OptionParser, Option

parser = OptionParser(usage = "usage: %prog [options] args")
parser.add_option("-b", "--breakpoint_db", dest = "breakpoint_db", type = "string", default = "", metavar = "BREAKPOINT_DB", 
                  help = "Breakpoint DB filename")
parser.add_option("-l", "--log", dest = "log", type = "string", default = "", metavar = "LOG", help = "Log filename")

(options, args) = parser.parse_args(sys.argv)

root_dir = os.path.dirname(sys.argv[-3])

if options.breakpoint_db == '':
    options.breakpoint_db = os.path.join(root_dir, 'bp.db')

if options.log == '':
    options.log = os.path.join(root_dir, time.strftime("Record-%Y%m%d-%H%M%S.db"))

logging.basicConfig(level = logging.DEBUG)
root = logging.getLogger()

windbgtool_run = windbgtool.run()
# windbgtool_run.set_symbol_path()

if options.breakpoint_db:
    windbgtool_run.load_breakpoints(options.breakpoint_db, options.log)
    windbgtool_run.go()
