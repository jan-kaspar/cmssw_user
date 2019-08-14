string dir_base = "tb,round1-short/10328/0,1,2,3,4,5-excl1981939712/s,fin,3pl,1rotzIt=0,units=2,overlap=t,3potsInO=t,eMuMvRot=f";

string dirs[], d_labels[];
dirs.push(dir_base + "/iteration1"); d_labels.push("iteration 1");
//dirs.push(dir_base + "/iteration2"); d_labels.push("iteration 2");
//dirs.push(dir_base + "/iteration3"); d_labels.push("iteration 3");

string rpSets[];
pen rps_pens[];
rpSets.push("0, 4"); rps_pens.push(black);
rpSets.push("0, 2, 3, 4"); rps_pens.push(heavygreen);
rpSets.push("0, 2, 4"); rps_pens.push(magenta);
rpSets.push("0, 3, 4"); rps_pens.push(brown);

rpSets.push("2, 3"); rps_pens.push(yellow);

rpSets.push("1, 5"); rps_pens.push(blue);
rpSets.push("1, 2, 3, 5"); rps_pens.push(red);
rpSets.push("2, 3, 5"); rps_pens.push(cyan);

include diagnostics_per_rp_conf_base;
