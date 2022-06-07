from org.csstudio.display.builder.runtime.script import PVUtil

# run only if there is some valid channel
if len(PVUtil.getString(pvs[0]).split(" - ")) > 1 :
    channel = PVUtil.getString(pvs[0]).split(" - ")[1]

    # Adding the macros on the widget that will consume this script
    widget.getPropertyValue("macros").add("CHANNEL", channel)

    # if is a down-sampled or PIERR channel get DAQ format from PV
    if len(channel.split("DWN")) > 1 or ("PIERR" in channel and "PIERRILC" not in channel) :
        prefix = PVUtil.getString(pvs[1])
        pv_daq = PVUtil.createPV(prefix + ":" + channel + "-DAQFMT-RBV", 5000)
        daqfmt = PVUtil.getString(pv_daq)
        widget.getPropertyValue("macros").add("CMP0", daqfmt.split("/")[0])
        if len(daqfmt.split("/")) > 1:
            widget.getPropertyValue("macros").add("CMP1", daqfmt.split("/")[1])
        else:
            widget.getPropertyValue("macros").add("CMP1", "NONE")
    else: #otherwise the default format is IQ
        widget.getPropertyValue("macros").add("CMP0", "I")
        widget.getPropertyValue("macros").add("CMP1", "Q")

    widget.setPropertyValue("file", "")
    widget.setPropertyValue("file", "plot_ch.bob")
