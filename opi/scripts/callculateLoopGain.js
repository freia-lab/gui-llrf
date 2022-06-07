PVUtil = org.csstudio.display.builder.runtime.script.PVUtil;


var cavMag = PVUtil.getDouble(pvs[0]);
var spMag  = PVUtil.getDouble(pvs[1]);
var vmLimit  = PVUtil.getDouble(pvs[2]);
var vmEnabled = PVUtil.getDouble(pvs[3]);

var out = spMag;
if (vmLimit <= spMag && vmEnabled==1.0) {
	out = vmLimit;
}
var gain = cavMag/out;

pvs[4].setValue(out);
pvs[5].setValue(gain);