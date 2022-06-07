from org.csstudio.display.builder.runtime.script import PVUtil
import os
from os.path import expanduser


val = PVUtil.getString(pvs[0])

if val == '1':
    arg1 = PVUtil.getString(pvs[1])
    arg2 = PVUtil.getString(pvs[2])
    arg3 = PVUtil.getString(pvs[3])
    arg4 = PVUtil.getDouble(pvs[4])
    arg5 = PVUtil.getDouble(pvs[5])
    arg6 = PVUtil.getString(pvs[6])
    home = expanduser("~")
    os.chdir(home + '/e3/e3-sis8300llrf/m-epics-sis8300llrf/scripts')
    os.system('./sis8300llrf-generateTable.py %s %s %s %f %f %s' % (arg1, arg2, arg3, arg4, arg5, arg6))
