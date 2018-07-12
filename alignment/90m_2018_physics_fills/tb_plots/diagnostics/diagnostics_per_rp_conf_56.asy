string dir_base = "tb,round1-short/319104.1-21/103,104,105,123,124,125/s,std,3pl,1rotzIt=0,units=2,overlap=t,3potsInO=t,eMuMvRot=f";

string dirs[], d_labels[];
dirs.push(dir_base + "/iteration1"); d_labels.push("iteration 1");
//dirs.push(dir_base + "/iteration2"); d_labels.push("iteration 2");
//dirs.push(dir_base + "/iteration3"); d_labels.push("iteration 3");

string rpSets[];
pen rps_pens[];

rpSets.push("104, 124"); rps_pens.push(black);
rpSets.push("105, 125"); rps_pens.push(black);

rpSets.push("103, 123"); rps_pens.push(cyan+2pt);

rpSets.push("103, 104, 124"); rps_pens.push(magenta);
rpSets.push("103, 105, 125"); rps_pens.push(magenta);

rpSets.push("103, 105, 123"); rps_pens.push(yellow);

rpSets.push("103, 123, 124"); rps_pens.push(blue);
//rpSets.push("103, 123, 125"); rps_pens.push(blue);

rpSets.push("103, 104, 123, 124"); rps_pens.push(red);
rpSets.push("103, 105, 123, 125"); rps_pens.push(red);

rpSets.push("105, 123, 125"); rps_pens.push(heavygreen);

include diagnostics_per_rp_conf_base;
