include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(1); unit_names.push("45-210-fr");
units.push(21); unit_names.push("45-220-fr");

//excludedRPs = new int[] { 100, 102 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("rp_shx"); quantity_labels.push("shift in $x\ung{\mu m}$");
quantities.push("rp_shy"); quantity_labels.push("shift in $y\ung{\mu m}$");
//quantities.push("rp_rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string prefix = "tb,round1/";
string postfix = "/3,4,5,23,24,25-excl1981939712,2023555072/s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration4";

inputs.push(prefix + "324579.1-45" + postfix); input_pens.push(blue);
inputs.push(prefix + "324579.46-99" + postfix); input_pens.push(red);

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerRP();
