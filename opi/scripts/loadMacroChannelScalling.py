from org.csstudio.display.builder.runtime.script import PVUtil
                                                  
channel = PVUtil.getString(pvs[0]).split(" ")[2]
                                    
# Adding the macros on the widget that will consume this script
widget.getPropertyValue("macros").add("CHANNEL", channel)

widget.setPropertyValue("file", "")
widget.setPropertyValue("file", "scaling.bob")
