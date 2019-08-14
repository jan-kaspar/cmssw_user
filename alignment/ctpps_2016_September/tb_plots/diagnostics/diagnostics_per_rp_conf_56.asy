string dir_base = "tb,round1/10328/101,103,104,105-excl1998356480/s,fin,3pl,1rotzIt=0,units=2,overlap=t,3potsInO=t,eMuMvRot=f";

string dirs[], d_labels[];
dirs.push(dir_base + "/iteration1"); d_labels.push("iteration 1");
dirs.push(dir_base + "/iteration2"); d_labels.push("iteration 2");
dirs.push(dir_base + "/iteration3"); d_labels.push("iteration 3");

string rpSets[];
pen rps_pens[];
rpSets.push("103, 104"); rps_pens.push(black);

rpSets.push("101, 105"); rps_pens.push(blue);
rpSets.push("101, 103, 105"); rps_pens.push(red);

include diagnostics_per_rp_conf_base;
