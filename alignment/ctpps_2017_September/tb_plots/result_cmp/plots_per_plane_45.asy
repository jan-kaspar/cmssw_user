include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(1); unit_names.push("45-210-fr");
units.push(21); unit_names.push("45-220-fr");

//excludedRPs = new int[] { 100, 102 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("shx"); quantity_labels.push("shift in $x\ung{\mu m}$");
quantities.push("shy"); quantity_labels.push("shift in $y\ung{\mu m}$");
//quantities.push("rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string options = "s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration4";
inputs = new string[] {
	"tb,round1/303652/3,4,5,23,24,25-excl1981939712,1982332928,1982365696,1982398464,1982431232/"+options,
	"tb,round1/303658/3,4,5,23,24,25-excl1981939712,1982332928,1982365696,1982398464,1982431232/"+options,
	"tb,round1/303665/3,4,5,23,24,25-excl1981939712,1982332928,1982365696,1982398464,1982431232/"+options,
};

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerPlane();
