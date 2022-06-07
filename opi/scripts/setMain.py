from org.csstudio.display.builder.runtime.script import PVUtil
import sys

pvMainPref = PVUtil.getString(pvs[0])
listSufixes = (PVUtil.getString(pvs[1])).split(" ")

for pv in listSufixes:
    pvStatus = PVUtil.createPV(pv, 5000)
    # all the channels should be on INIT state
    if PVUtil.getDouble(pvStatus) != 3:
        PVUtil.releasePV(pvStatus)
        sys.exit()
    PVUtil.releasePV(pvStatus)

for pv in listSufixes:
    if pv != pvMainPref:
        pvSec = PVUtil.createPV(pv + ":MAIN", 5000)
        pvSec.setValue(0)
        PVUtil.releasePV(pvSec)

if (pvMainPref != ""):
    pvMain = PVUtil.createPV(pvMainPref + ":MAIN", 5000)
    pvMain.setValue(1)
    PVUtil.releasePV(pvMain)


