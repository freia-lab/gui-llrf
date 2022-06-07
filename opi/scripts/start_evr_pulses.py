from org.csstudio.display.builder.runtime.script import PVUtil
import os
from jarray import array
from time import sleep

start = PVUtil.getInt(pvs[0])
n = PVUtil.getInt(pvs[4])

if start == 1 and n < 401 and n >= 0:
    rate = PVUtil.getDouble(pvs[1]) # Hz
    length = PVUtil.getDouble(pvs[2]) # us
    prefix = PVUtil.getString(pvs[3])
    base_pv_name = "TR-" + prefix


    pv_div = PVUtil.createPV(base_pv_name + ":PS0-Div-SP", 5000)
    pv_runmode = PVUtil.createPV(base_pv_name + ":SoftSeq0-RunMode-Sel", 5000)
    pv_trgsrc = PVUtil.createPV(base_pv_name + ":SoftSeq0-TrigSrc-2-Sel", 5000)
    pv_res = PVUtil.createPV(base_pv_name + ":SoftSeq0-TsResolution-Sel", 5000)
    pv_load = PVUtil.createPV(base_pv_name + ":SoftSeq0-Load-Cmd", 5000)
    pv_enbl = PVUtil.createPV(base_pv_name + ":SoftSeq0-Enable-Cmd", 5000)
    pv_cmt = PVUtil.createPV(base_pv_name + ":SoftSeq0-Commit-Cmd", 5000)
    pv_evt = PVUtil.createPV(base_pv_name + ":SoftSeq0-EvtCode-SP", 5000)
    pv_ts = PVUtil.createPV(base_pv_name + ":SoftSeq0-Timestamp-SP", 5000)

    pv_sfttrig = PVUtil.createPV(base_pv_name + ":SoftSeq0-SoftTrig-Cmd", 5000)

    div = int(88061948.02 / rate)
    pv_div.write(div)

    reprate_moment = 0
    pulsecoming_moment = reprate_moment + 210000
    pulsestart_moment = pulsecoming_moment + 300000
    finish_interval = 10000

    if n > 0:
        pv_runmode.write(1) # Single Mode
        pv_trgsrc.write(1) # trigger source is software
        pv_res.write(3) # ns

        P=int((1.0/rate)*1000000000) # pulse size in ns

        evtcode = []
        timestamp = []

        for i in range(n):
            newts = (i*P)
            evtcode += [14, 15, 16, 17]
            timestamp += [newts, newts + pulsecoming_moment, newts + pulsestart_moment,
                    newts+(length*1000) + pulsecoming_moment]

        evtcode.append(127)
        timestamp.append((timestamp[-1]) + finish_interval)


        pv_evt.write(array(evtcode, 'd'))
        pv_ts.write(array(timestamp, 'd'))
        sleep(1)

        pv_load.write(1)
        pv_enbl.write(1)
        pv_cmt.setValue(1)
        pv_sfttrig.setValue(1) # this start the trigger
    elif n == 0: # run without stop
        pv_runmode.write(0) # Normal mode
        pv_trgsrc.write(2) # trigger source is pre-scaler 0
        pv_res.write(3) # ns

        evtcode = [14, 15, 16, 17, 127]
        timestamp = [reprate_moment, pulsecoming_moment,
                    pulsestart_moment, (length*1000) + pulsecoming_moment,
                    (length*1000) + pulsecoming_moment + finish_interval]
        pv_evt.write(array(evtcode, 'd'))
        pv_ts.write(array(timestamp, 'd'))
        sleep(1)

        pv_load.write(1)
        pv_enbl.write(1)
        pv_cmt.setValue(1)

    PVUtil.releasePV(pv_div)
    PVUtil.releasePV(pv_runmode)
    PVUtil.releasePV(pv_trgsrc)
    PVUtil.releasePV(pv_res)
    PVUtil.releasePV(pv_load)
    PVUtil.releasePV(pv_enbl)
    PVUtil.releasePV(pv_cmt)
    PVUtil.releasePV(pv_evt)
    PVUtil.releasePV(pv_ts)
    PVUtil.releasePV(pv_sfttrig)

    # return to start_evr to 0
    pv_startevr = PVUtil.createPV("loc://start_evr", 5000)
    pv_startevr.write(0)
    PVUtil.releasePV(pv_startevr)
