string dir_base = "tb,round1-short/314247/103,104,105,123,124,125/s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f";

string dirs[], d_labels[];
dirs.push(dir_base + "/iteration3"); d_labels.push("iteration 3");

string rpSets[];
pen rps_pens[];
rpSets.push("104, 124"); rps_pens.push(blue);
rpSets.push("103, 104, 124"); rps_pens.push(cyan);
rpSets.push("103, 123, 124"); rps_pens.push(green);
rpSets.push("103, 104, 123, 124"); rps_pens.push(red);

rpSets.push("105, 125"); rps_pens.push(blue);
rpSets.push("103, 105, 123"); rps_pens.push(cyan);
rpSets.push("103, 105, 123, 125"); rps_pens.push(red);

rpSets.push("103, 123"); rps_pens.push(gray);

real pixel_x_min = 1.5;
real pixel_y_cen = 0.5;

include diagnostics_per_rp_conf_base;
