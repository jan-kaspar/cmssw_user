include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(100); unit_names.push("56-210-nr");
units.push(101); unit_names.push("56-210-fr");

excludedRPs = new int[] { 100, 102 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("rp_shx"); quantity_labels.push("shift in $x\ung{\mu m}$");
quantities.push("rp_shy"); quantity_labels.push("shift in $y\ung{\mu m}$");
//quantities.push("rp_rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string prefix = "tb,round1/";
string postfix = "/101,103,104,105-excl1998356480/s,fin,3pl,1rotzIt=0,units=2,overlap=t,3potsInO=t,eMuMvRot=f/iteration3";

inputs.push(prefix + "10322" + postfix); input_pens.push(black);
inputs.push(prefix + "10324" + postfix); input_pens.push(blue);
inputs.push(prefix + "10325" + postfix); input_pens.push(red);
inputs.push(prefix + "10326" + postfix); input_pens.push(heavygreen);
inputs.push(prefix + "10327" + postfix); input_pens.push(cyan);
inputs.push(prefix + "10328" + postfix); input_pens.push(magenta);
inputs.push(prefix + "10329" + postfix); input_pens.push(green);
inputs.push(prefix + "10331" + postfix); input_pens.push(brown);
inputs.push(prefix + "10332" + postfix); input_pens.push(yellow);

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerRP();
