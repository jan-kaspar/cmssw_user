include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(1); unit_names.push("L, 210, far");
units.push(0); unit_names.push("L, 210, near");

//excludedRPs = new int[] { 100, 102 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("shr"); quantity_labels.push("shift$\ung{\mu m}$");
quantities.push("rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string options = "s+sr-fin,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration5";
inputs = new string[] {
	"tb,round1/10322/0,1,2,3,4,5-excl44/"+options,
	"tb,round1/10324/0,1,2,3,4,5-excl44/"+options,
	"tb,round1/10325/0,1,2,3,4,5-excl44/"+options,
	"tb,round1/10326/0,1,2,3,4,5-excl44/"+options,
	"tb,round1/10328/0,1,2,3,4,5-excl44/"+options,
//	"tb,round1/10329/0,1,2,3,4,5-excl44/"+options,
	"tb,round1/10331/0,1,2,3,4,5-excl44/"+options,
	"tb,round1/10332/0,1,2,3,4,5-excl44/"+options,
};

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerPlane();
