from org.csstudio.display.builder.runtime.script import PVUtil
import os
from os.path import expanduser


val = PVUtil.getString(pvs[0])

if val == '1':
    arg1 = PVUtil.getString(pvs[1])
    arg2 = PVUtil.getString(pvs[2])
    home = expanduser("~")
    os.chdir(home + '/e3/e3-sis8300llrf/m-epics-sis8300llrf/scripts')
    os.system('./sis8300llrf-importTableFromFile.py %s %s' % (arg1, arg2))
