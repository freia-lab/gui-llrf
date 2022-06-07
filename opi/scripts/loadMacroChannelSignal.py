from org.csstudio.display.builder.runtime.script import PVUtil

channel = PVUtil.getString(pvs[0]).split("- ")[1]

# Adding the macros on the widget that will consume this script
widget.getPropertyValue("macros").add("CH", channel)

widget.setPropertyValue("file", "")
widget.setPropertyValue("file", "./embedded/signal_monitoring.bob")
