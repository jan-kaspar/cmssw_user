string dir_base = "tb,round1-short/323311.1-91/3,4,5,23,24,25-excl1981939712,2023555072/s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f";

string dirs[], d_labels[];
dirs.push(dir_base + "/iteration1"); d_labels.push("iteration 1");
dirs.push(dir_base + "/iteration2"); d_labels.push("iteration 2");
dirs.push(dir_base + "/iteration3"); d_labels.push("iteration 3");

string rpSets[];
pen rps_pens[];
rpSets.push("4, 24"); rps_pens.push(black);
//rpSets.push("3, 4, 23, 24"); rps_pens.push(heavygreen);
rpSets.push("3, 4, 24"); rps_pens.push(magenta);

rpSets.push("5, 25"); rps_pens.push(blue);
rpSets.push("3, 5, 23, 25"); rps_pens.push(red);
rpSets.push("3, 5, 23"); rps_pens.push(cyan);

include diagnostics_per_rp_conf_base;
