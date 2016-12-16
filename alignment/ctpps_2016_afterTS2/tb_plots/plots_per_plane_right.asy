include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(100); unit_names.push("R, 210, near");
units.push(101); unit_names.push("R, 210, far");

excludedRPs = new int[] { 100, 102 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("shr"); quantity_labels.push("shift$\ung{\mu m}$");
quantities.push("rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string options = "s+sr-fin,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=t/iteration5";
inputs = new string[] {
	"tb,round1/10322/101,103,104,105-excl1039/"+options,
//	"tb,round1/10324/101,103,104,105-excl1039/"+options,
	"tb,round1/10325/101,103,104,105-excl1039/"+options,
//	"tb,round1/10326/101,103,104,105-excl1039/"+options,
//	"tb,round1/10327/101,103,104,105-excl1039/"+options,
	"tb,round1/10328/101,103,104,105-excl1039/"+options,
	"tb,round1/10329/101,103,104,105-excl1039/"+options,
	"tb,round1/10331/101,103,104,105-excl1039/"+options,
	"tb,round1/10332/101,103,104,105-excl1039/"+options,
};

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerPlane();
