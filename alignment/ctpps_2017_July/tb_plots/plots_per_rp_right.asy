include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(101); unit_names.push("56-210-fr");
units.push(121); unit_names.push("56-220-fr");

//excludedRPs = new int[] { 100 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("rp_shx"); quantity_labels.push("shift in $x\ung{\mu m}$");
quantities.push("rp_shy"); quantity_labels.push("shift in $y\ung{\mu m}$");
//quantities.push("rp_rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string options = "s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration3";
inputs = new string[] {
	"tb,round1/298593/103,104,105,123,124,125-excl1998323712,1998356480/"+options,
	"tb,round1/298594/103,104,105,123,124,125-excl1998323712,1998356480/"+options,
	"tb,round1/298596/103,104,105,123,124,125-excl1998323712,1998356480/"+options,
	"tb,round1/298597/103,104,105,123,124,125-excl1998323712,1998356480/"+options,
};

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerRP();
