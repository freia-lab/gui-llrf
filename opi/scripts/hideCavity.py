from org.csstudio.display.builder.runtime.script import PVUtil

pv0 = PVUtil.getDouble(pvs[0])

## Script Body
if pv0==True:
    widget.setPropertyValue('visible', False)
elif pv0==False:
    widget.setPropertyValue('visible', True)
else:
    widget.setPropertyValue('visible', True)
