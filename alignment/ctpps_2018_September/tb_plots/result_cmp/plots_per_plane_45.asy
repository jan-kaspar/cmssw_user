include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(1); unit_names.push("45-210-fr");
units.push(21); unit_names.push("45-220-fr");

//excludedRPs = new int[] { 100, 102 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("shx"); quantity_labels.push("shift in $x\ung{\mu m}$");
quantities.push("shy"); quantity_labels.push("shift in $y\ung{\mu m}$");
//quantities.push("rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string prefix = "tb,round3/";
string postfix = "/3,4,5,23,24,25-excl1981939712,2023555072/s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration3";

// xangle=130, beta*=0.27
inputs.push(prefix + "323311.1-91" + postfix); input_pens.push(blue);
inputs.push(prefix + "323311.92-182" + postfix); input_pens.push(blue);
inputs.push(prefix + "323312.1-60" + postfix); input_pens.push(blue);
inputs.push(prefix + "323312.61-120" + postfix); input_pens.push(blue);

// xangle=130, beta*=0.25
inputs.push(prefix + "323316.1-100" + postfix); input_pens.push(red);
inputs.push(prefix + "323316.101-200" + postfix); input_pens.push(red);
inputs.push(prefix + "323316.201-317" + postfix); input_pens.push(red);

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerPlane();
