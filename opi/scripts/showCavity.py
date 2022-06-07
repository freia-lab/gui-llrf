from org.csstudio.display.builder.runtime.script import PVUtil

pv0 = PVUtil.getDouble(pvs[0])

## Script Body
if pv0==True:
    widget.setPropertyValue('visible', True)
elif pv0==False:
    widget.setPropertyValue('visible', False)
else:
    widget.setPropertyValue('visible', True)
