string dir_base = "tb,round1-short/324579.1-25/103,104,105,123,124,125/ev=1E4,pl=3,units=2,ovlp=f,3rpsInO=t/s+sr,std,1rotzIt=0,eMuMvRot=t";

string dirs[], d_labels[];
dirs.push(dir_base + "/iteration1"); d_labels.push("iteration 1");
dirs.push(dir_base + "/iteration2"); d_labels.push("iteration 2");
dirs.push(dir_base + "/iteration3"); d_labels.push("iteration 3");

string rpSets[];
pen rps_pens[];
rpSets.push("104, 124"); rps_pens.push(black);
rpSets.push("103, 104, 123, 124"); rps_pens.push(heavygreen);
rpSets.push("103, 104, 124"); rps_pens.push(magenta);

rpSets.push("105, 125"); rps_pens.push(blue);
rpSets.push("103, 105, 123, 125"); rps_pens.push(red);
rpSets.push("103, 105, 123"); rps_pens.push(cyan);

include diagnostics_per_rp_conf_base;