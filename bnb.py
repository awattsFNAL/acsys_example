from logger_get import *
import numpy as np


nhours=72
T2 = int(time.time())
T1 = int(T2 - nhours*3600)

bnb_rate = {
    "desc": "BNB rate",
    "devicename": "E:MBRATE",
    "units": "protons/hour",
    "event": "e,00,e,2000",
    "color": black,
    "yMin": 0.0,
    "yMax": 1.0E17
}
bnb_tor = {
    "desc": "BNB intensity",
    "devicename": "E:TR875L",
    "units": "protons/pulse",
    "event": "e,1d,e,40",
    "color": gold,
    "yMin": 0.0,
    "yMax": 5
}
try:
	t, d = acsysLoggerGet(bnb_rate["devicename"], bnb_rate["event"], T1, T2)
	bnb_rate["t_data"] = t
	bnb_rate["data"] = d
	t, d = acsysLoggerGet(bnb_tor["devicename"], bnb_tor["event"], T1, T2)
	bnb_tor["t_data"] = t
	bnb_tor["data"] = d
	timePlot('bnb_overview', [bnb_rate, bnb_tor], T1, T2, dims=[12, 4])
except:
	pass
	
booster_turns = {
    "desc": "Booster $1D turns",
    "devicename": "G:TURN1D",
    "units": "turns",
    "event": "p,30000",
    "color": grey,
    "yMin": 0.0,
    "yMax": 20.0,
}
bnb_rep = {
    "desc": "Booster avg. rep. rate",
    "devicename": "E:MBPRTE",
    "units": "Hz",
    "event": "p,60000",
    "color": orange,
    "yMin": 0.0,
    "yMax": 10.0,
}
try:
	t, d = acsysLoggerGet(booster_turns["devicename"], booster_turns["event"], T1, T2)
	booster_turns["t_data"] = t
	booster_turns["data"] = d
	t, d = acsysLoggerGet(bnb_rep["devicename"], bnb_rep["event"], T1, T2)
	bnb_rep["t_data"] = t
	bnb_rep["data"] = d
	timePlot('BNB_rates', [booster_turns, bnb_rep], T1, T2, dims=[12, 4])
except:
	pass

linac_tor = {
    "desc": "Linac intensity",
    "devicename": "L:D7TOR",
    "units": "mA",
    "event": "p,15000",
    "color": green,
    "yMin": 0.0,
    "yMax": 35.0,
}
booster_loss = {
    "desc": "Booster avg. loss",
    "devicename": "B:BPL5MA",
    "units": "Watts",
    "event": "p,30000",
    "color": red,
    "yMin": 0.0,
    "yMax": 700.0,
}
try:
	t, d = acsysLoggerGet(linac_tor["devicename"], linac_tor["event"], T1, T2)
	linac_tor["t_data"] = t
	linac_tor["data"] = d
	t, d = acsysLoggerGet(booster_loss["devicename"], booster_loss["event"], T1, T2)
	booster_loss["t_data"] = t
	booster_loss["data"] = d
	timePlot('BNB_upstream1', [linac_tor, booster_loss], T1, T2, dims=[12, 4])
except:
	pass
	
booster_rate = {
    "desc": "Booster rate",
    "devicename": "E:BTRATE",
    "units": "Hz",
    "event": "p,30000",
    "color": orange,
    "yMin": 0.0,
    "yMax": 18.0,
}
booster_eff = {
    "desc": "Booster $1D efficiency",
    "devicename": "B:BEFF1D",
    "units": "%",
    "event": "p,15000",
    "color": blue,
    "yMin": 60.0,
    "yMax": 100.0,
}
try:
	t, d = acsysLoggerGet(booster_rate["devicename"], booster_rate["event"], T1, T2)
	booster_rate["t_data"] = t
	booster_rate["data"] = d
	t, d = acsysLoggerGet(booster_eff["devicename"], booster_eff["event"], T1, T2)
	booster_eff["t_data"] = t
	booster_eff["data"] = d
	timePlot('BNB_upstream2', [booster_rate, booster_eff], T1, T2, dims=[12, 4])
except:
	pass

TLI864 = {
    "desc": "Loss @ 864",
    "devicename": "E:TLI864",
    "units": "R/s",
    "event": "e,1D,e,50",
    "color": blue,
    "yMin": 0.0,
    "yMax": 12.0,
}
TLI873 = {
    "desc": "Loss @ 873",
    "devicename": "E:TLI873",
    "units": "R/s",
    "event": "e,1D,e,50",
    "color": green,
    "yMin": 0.0,
    "yMax": 12.0,
}
try:
	t, d = acsysLoggerGet(TLI864["devicename"], TLI864["event"], T1, T2)
	TLI864["t_data"] = t
	TLI864["data"] = d
	t, d = acsysLoggerGet(TLI873["devicename"], TLI873["event"], T1, T2)
	TLI873["t_data"] = t
	TLI873["data"] = d
	timePlot('BNB_TLI', [TLI864, TLI873], T1, T2, dims=[12, 4])
except:
	pass

horn_current = {
    "desc": "BNB horn current",
    "devicename": "E:LHCURR",
    "units": "KA",
    "event": "p,3000",
    "color": red,
    "yMin": 172.0,
    "yMax": 182.0,
}
try:
	t, d = acsysLoggerGet(horn_current["devicename"], horn_current["event"], T1, T2)
	horn_current["t_data"] = t
	horn_current["data"] = d
	timePlot('BNB_horn', [horn_current], T1, T2, dims=[12, 4])
except:
	pass

tgt_jtmp1 = {
    "desc": "Target temp. @ joint",
    "devicename": "E:BTJT1",
    "units": "DegC",
    "event": "p,30000",
    "color": black,
    "yMin": 10.0,
    "yMax": 110.0,
}
tgt_jtmp2 = {
    "desc": "Target temp. > joint",
    "devicename": "E:BTJT2",
    "units": "DegC",
    "event": "p,30000",
    "color": orange,
    "yMin": 10.0,
    "yMax": 110.0,
}
try:
	t, d = acsysLoggerGet(tgt_jtmp1["devicename"], tgt_jtmp1["event"], T1, T2)
	tgt_jtmp1["t_data"] = t
	tgt_jtmp1["data"] = d
	t, d = acsysLoggerGet(tgt_jtmp2["devicename"], tgt_jtmp2["event"], T1, T2)
	tgt_jtmp2["t_data"] = t
	tgt_jtmp2["data"] = d
	timePlot('BNB_tgtjtmps', [tgt_jtmp1, tgt_jtmp2], T1, T2, dims=[12, 4])
except:
	pass

tgt_btmp1 = {
    "desc": "Target temp. @ bend",
    "devicename": "E:BTBT1",
    "units": "DegC",
    "event": "p,30000",
    "color": grey,
    "yMin": 10.0,
    "yMax": 110.0,
}
tgt_btmp2 = {
    "desc": "Target temp. > bend",
    "devicename": "E:BTBT2",
    "units": "DegC",
    "event": "p,30000",
    "color": gold,
    "yMin": 10.0,
    "yMax": 110.0,
}
try:
	t, d = acsysLoggerGet(tgt_btmp1["devicename"], tgt_btmp1["event"], T1, T2)
	tgt_btmp1["t_data"] = t
	tgt_btmp1["data"] = d
	t, d = acsysLoggerGet(tgt_btmp2["devicename"], tgt_btmp2["event"], T1, T2)
	tgt_btmp2["t_data"] = t
	tgt_btmp2["data"] = d
	timePlot('BNB_tgtbtmps', [tgt_btmp1, tgt_btmp2], T1, T2, dims=[12, 4])
except:
	pass

tgt_bth1t1 = {
    "desc": "Target HEX 1 in temp.",
    "devicename": "E:BTH1T1",
    "units": "DegC",
    "event": "p,30000",
    "color": blue,
    "yMin": 0.0,
    "yMax": 120.0,
}
tgt_bth1t2 = {
    "desc": "Target HEX 1 out temp.",
    "devicename": "E:BTH1T2",
    "units": "DegC",
    "event": "p,30000",
    "color": orange,
    "yMin": 0.0,
    "yMax": 120.0,
}
try:
	t, d = acsysLoggerGet(tgt_bth1t1["devicename"], tgt_bth1t1["event"], T1, T2)
	tgt_bth1t1["t_data"] = t
	tgt_bth1t1["data"] = d
	t, d = acsysLoggerGet(tgt_btmp2["devicename"], tgt_bth1t2["event"], T1, T2)
	tgt_bth1t2["t_data"] = t
	tgt_bth1t2["data"] = d
	timePlot('BNB_tgthtmps1', [tgt_bth1t1, tgt_bth1t2], T1, T2, dims=[12, 4])
except:
	pass

tgt_bth2t1 = {
    "desc": "Target HEX 2 in temp.",
    "devicename": "E:BTH2T1",
    "units": "DegC",
    "event": "p,30000",
    "color": red,
    "yMin": 0.0,
    "yMax": 120.0,
}
tgt_bth2t2 = {
    "desc": "Target HEX 2 out temp.",
    "devicename": "E:BTH2T2",
    "units": "DegC",
    "event": "p,30000",
    "color": black,
    "yMin": 0.0,
    "yMax": 120.0,
}
try:
	t, d = acsysLoggerGet(tgt_bth2t1["devicename"], tgt_bth2t1["event"], T1, T2)
	tgt_bth2t1["t_data"] = t
	tgt_bth2t1["data"] = d
	t, d = acsysLoggerGet(tgt_bth2t2["devicename"], tgt_bth2t2["event"], T1, T2)
	tgt_bth2t2["t_data"] = t
	tgt_bth2t2["data"] = d
	timePlot('BNB_tgthtmps2', [tgt_bth2t1, tgt_bth2t2], T1, T2, dims=[12, 4])
except:
	pass

tgt_hexv1 = {
    "desc": "Target HEX 1 air vel.",
    "devicename": "E:BTH1AV",
    "units": "ft./m",
    "event": "p,30000",
    "color": blue,
    "yMin": 0.0,
    "yMax": 2000.0,
}
tgt_hexv2 = {
    "desc": "Target HEX 2 air vel.",
    "devicename": "E:BTH2AV",
    "units": "ft./m",
    "event": "p,30000",
    "color": green,
    "yMin": 0.0,
    "yMax": 2000.0,
}
try:
	t, d = acsysLoggerGet(tgt_hexv1["devicename"], tgt_hexv1["event"], T1, T2)
	tgt_hexv1["t_data"] = t
	tgt_hexv1["data"] = d
	t, d = acsysLoggerGet(tgt_hexv2["devicename"], tgt_hexv2["event"], T1, T2)
	tgt_hexv2["t_data"] = t
	tgt_hexv2["data"] = d
	timePlot('BNB_tgtairvel', [tgt_hexv1, tgt_hexv2], T1, T2, dims=[12, 4])
except:
	pass

tgt_blp = {
    "desc": "Target blower pressure",
    "devicename": "E:BTBLAP",
    "units": "PSIG",
    "event": "p,30000",
    "color": red,
    "yMin": 0.0,
    "yMax": 10.0,
}
tgt_h1p = {
    "desc": "Target HEX1 pressure",
    "devicename": "E:BTH1AP",
    "units": "PSIG",
    "event": "p,30000",
    "color": black,
    "yMin": 0.0,
    "yMax": 10.0,
}
try:
	t, d = acsysLoggerGet(tgt_blp["devicename"], tgt_blp["event"], T1, T2)
	tgt_blp["t_data"] = t
	tgt_blp["data"] = d
	t, d = acsysLoggerGet(tgt_hexv2["devicename"], tgt_hexv2["event"], T1, T2)
	tgt_h1p["t_data"] = t
	tgt_h1p["data"] = d
	timePlot('BNB_tgtairp', [tgt_blp, tgt_h1p], T1, T2, dims=[12, 4])
except:
	pass
