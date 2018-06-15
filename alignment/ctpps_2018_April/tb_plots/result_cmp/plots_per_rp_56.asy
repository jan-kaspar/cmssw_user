include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(101); unit_names.push("56-210-fr");
units.push(121); unit_names.push("56-220-fr");

//excludedRPs = new int[] { 100 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("rp_shx"); quantity_labels.push("shift in $x\ung{\mu m}$");
quantities.push("rp_shy"); quantity_labels.push("shift in $y\ung{\mu m}$");
//quantities.push("rp_rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string prefix = "tb,round1";
string postfix = "s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration4";
inputs = new string[] {
	prefix + "/314247/103,104,105,123,124,125/"+postfix,

	prefix + "/314250/103,104,105,123,124,125/"+postfix,
	prefix + "/314255/103,104,105,123,124,125/"+postfix,

	prefix + "/314269/103,104,105,123,124,125/"+postfix,
	prefix + "/314272/103,104,105,123,124,125/"+postfix,

	//prefix + "/314274/103,104,105,123,124,125/"+postfix,
	prefix + "/314276/103,104,105,123,124,125/"+postfix,
};

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerRP();
