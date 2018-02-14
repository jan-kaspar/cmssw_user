include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(101); unit_names.push("56-210-fr");
units.push(121); unit_names.push("56-220-fr");

//excludedRPs = new int[] { 100 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("shx"); quantity_labels.push("shift in $x\ung{\mu m}$");
quantities.push("shy"); quantity_labels.push("shift in $y\ung{\mu m}$");
//quantities.push("rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string options = "s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration4";
inputs = new string[] {
	"tb,round1/303652/103,104,105,123,124,125/"+options,
	"tb,round1/303658/103,104,105,123,124,125/"+options,
	"tb,round1/303665/103,104,105,123,124,125/"+options,
};

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerPlane();
