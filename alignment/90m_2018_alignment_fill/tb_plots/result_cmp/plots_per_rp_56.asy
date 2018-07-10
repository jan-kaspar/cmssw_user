include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(101); unit_names.push("56-210-fr");
units.push(121); unit_names.push("56-220-fr");

//excludedRPs = new int[] { 100 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("rp_shx"); quantity_labels.push("shift in $x\ung{\mu m}$");
quantities.push("rp_shy"); quantity_labels.push("shift in $y\ung{\mu m}$");
//quantities.push("rp_rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string prefix = "tb,round1-short/";
string postfix = "/103,104,105,123,124,125/s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration3";

inputs.push(prefix + "318546.1-80" + postfix); input_pens.push(red);
inputs.push(prefix + "318546.81-163" + postfix); input_pens.push(red);
inputs.push(prefix + "318547" + postfix); input_pens.push(red);
inputs.push(prefix + "318548" + postfix); input_pens.push(red);
inputs.push(prefix + "318549" + postfix); input_pens.push(red);

string postfix = "/103,104,105,123,124,125/s,std,3pl,1rotzIt=0,units=2,overlap=t,3potsInO=t,eMuMvRot=f/iteration3";
inputs.push(prefix + "318550.1-35" + postfix); input_pens.push(blue);
inputs.push(prefix + "318550.36-71" + postfix); input_pens.push(blue);
inputs.push(prefix + "318551" + postfix); input_pens.push(blue);

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerRP();
