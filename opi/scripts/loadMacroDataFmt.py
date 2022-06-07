from org.csstudio.display.builder.runtime.script import PVUtil

prefix = PVUtil.getString(pvs[0])


pv_daq = PVUtil.createPV(prefix + "-DAQFMT-RBV", 5000)
daqfmt = PVUtil.getString(pv_daq)
widget.getPropertyValue("macros").add("CMP0", daqfmt.split("/")[0])
if len(daqfmt.split("/")) > 1:
    widget.getPropertyValue("macros").add("CMP1", daqfmt.split("/")[1])
else:
    widget.getPropertyValue("macros").add("CMP1", "NONE")

widget.setPropertyValue("file", "full-plot-emb.bob")
