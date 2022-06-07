PVUtil = org.csstudio.display.builder.runtime.script.PVUtil;


var cavAng = PVUtil.getDouble(pvs[0]);
var refAng = PVUtil.getDouble(pvs[1]);
var iqAng  = PVUtil.getDouble(pvs[2]);
var iqAngEn = PVUtil.getDouble(pvs[3]);
var fixedSPAng  = PVUtil.getDouble(pvs[4]);

var compensatedAng;
var delay;

if (iqAngEn == 0.0) {
	iqAng = 0.0;
}
compensatedAng = cavAng - refAng;
compensatedAng += (compensatedAng > Math.PI) ? (-2*Math.PI) : ( (compensatedAng < -Math.PI) ? 2*Math.PI : 0);
compensatedAng += iqAng;
pvs[5].setValue(compensatedAng);

delay = fixedSPAng - compensatedAng;
pvs[6].setValue(delay);
