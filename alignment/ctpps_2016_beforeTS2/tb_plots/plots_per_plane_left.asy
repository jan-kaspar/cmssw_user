include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(1); unit_names.push("L, 210, far");
units.push(0); unit_names.push("L, 210, near");

//excludedRPs = new int[] { 100, 102 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("shr"); quantity_labels.push("shift$\ung{\mu m}$");
quantities.push("rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string options = "s+sr-fin,3pl,1rotzIt=0,units=1,overlap=f,3potsInO=f,eMuMvRot=f/iteration3";
//string options = "s+sr-fin,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration3";
inputs = new string[] {
	"tb,round1/10077/0,1,2,3,4,5-excl44,50,51,52,53/"+options,
	"tb,round1/10079/0,1,2,3,4,5-excl44,50,51,52,53/"+options,
	"tb,round1/10080/0,1,2,3,4,5-excl44,50,51,52,53/"+options,
	"tb,round1/10081/0,1,2,3,4,5-excl44,50,51,52,53/"+options,
	"tb,round1/10082/0,1,2,3,4,5-excl44,50,51,52,53/"+options,
};

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerPlane();
