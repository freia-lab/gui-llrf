from org.csstudio.display.builder.runtime.script import PVUtil
                                                  
channel = PVUtil.getString(pvs[0]).split(" ")[0]
                                    
# Adding the macros on the widget that will consume this script
widget.getPropertyValue("macros").add("CHANNEL", channel)

widget.setPropertyValue("file", "")
widget.setPropertyValue("file", "embedded/aux_channels.bob")
