include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(100); unit_names.push("R, 210, near");
units.push(101); unit_names.push("R, 210, far");

excludedRPs = new int[] { 100 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("shr"); quantity_labels.push("shift$\ung{\mu m}$");
quantities.push("rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

//string options = "s+sr-fin,3pl,1rotzIt=0,units=1,overlap=f,3potsInO=f,eMuMvRot=f/iteration4";
string options = "s+sr-fin,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration4";
inputs = new string[] {
	"tb,round1/10077/101,102,103,104,105/"+options,
	"tb,round1/10079/101,102,103,104,105/"+options,
	"tb,round1/10080/101,102,103,104,105/"+options,
	"tb,round1/10081/101,102,103,104,105/"+options,
//	"tb,round1/10082/101,102,103,104,105/"+options,
};

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerPlane();
