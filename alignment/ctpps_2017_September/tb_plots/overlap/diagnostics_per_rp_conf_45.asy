string dir_base = "tb,round1-short/303652/3,4,5,23,24,25-excl1981939712,1982332928,1982365696,1982398464,1982431232/s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f";

string dirs[], d_labels[];
dirs.push(dir_base + "/iteration3"); d_labels.push("iteration 3");

string rpSets[];
pen rps_pens[];

rpSets.push("4, 24"); rps_pens.push(blue);
rpSets.push("3, 4, 24"); rps_pens.push(cyan);
rpSets.push("3, 23, 24"); rps_pens.push(green);
rpSets.push("3, 4, 23, 24"); rps_pens.push(red);

rpSets.push("5, 25"); rps_pens.push(blue);
rpSets.push("3, 5, 23"); rps_pens.push(cyan);
rpSets.push("3, 5, 23, 25"); rps_pens.push(red);

rpSets.push("3, 23"); rps_pens.push(gray);

real pixel_x_min = 2.5;
real pixel_y_cen = 1.1;

include diagnostics_per_rp_conf_base;
