include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(1); unit_names.push("45-210-fr");
units.push(21); unit_names.push("45-220-fr");

//excludedRPs = new int[] { 100, 102 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("rp_shx"); quantity_labels.push("shift in $x\ung{\mu m}$");
quantities.push("rp_shy"); quantity_labels.push("shift in $y\ung{\mu m}$");
//quantities.push("rp_rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string prefix = "tb,round3/";
string postfix = "/3,4,5,23,24,25-excl1981939712,1982332928,1982365696,1982398464,1982431232/s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration3";

// xangle-160-beta-30
//inputs.push(prefix + "314247" + postfix); input_pens.push(red);
inputs.push(prefix + "314247.1-20" + postfix); input_pens.push(red);
inputs.push(prefix + "314247.21-40" + postfix); input_pens.push(red);
inputs.push(prefix + "314247.41-61" + postfix); input_pens.push(red);

// xangle-131-beta-30
inputs.push(prefix + "314250.1-60" + postfix); input_pens.push(blue);
inputs.push(prefix + "314250.61-121" + postfix); input_pens.push(blue);
inputs.push(prefix + "314255.1-131" + postfix); input_pens.push(blue);
inputs.push(prefix + "314255.132-262" + postfix); input_pens.push(blue);

// xangle-130-beta-30
inputs.push(prefix + "314269.1-86" + postfix); input_pens.push(heavygreen);
inputs.push(prefix + "314269.87-172" + postfix); input_pens.push(heavygreen);
inputs.push(prefix + "314272.1-18" + postfix); input_pens.push(heavygreen);
inputs.push(prefix + "314272.19-37" + postfix); input_pens.push(heavygreen);

// xangle-130-beta-25
//inputs.push(prefix + "314274" + postfix); input_pens.push(magenta);
//inputs.push(prefix + "314274.1-25" + postfix); input_pens.push(magenta);
inputs.push(prefix + "314274.26-55" + postfix); input_pens.push(magenta);
inputs.push(prefix + "314274.56-80" + postfix); input_pens.push(magenta);
//inputs.push(prefix + "314276" + postfix); input_pens.push(magenta);
inputs.push(prefix + "314276.1-80" + postfix); input_pens.push(magenta);
inputs.push(prefix + "314276.81-160" + postfix); input_pens.push(magenta);
inputs.push(prefix + "314276.161-230" + postfix); input_pens.push(magenta);

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerRP();
