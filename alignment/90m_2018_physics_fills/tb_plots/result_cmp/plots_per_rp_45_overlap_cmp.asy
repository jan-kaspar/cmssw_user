include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(1); unit_names.push("45-210-fr");
units.push(21); unit_names.push("45-220-fr");

//excludedRPs = new int[] { 100, 102 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("rp_shx"); quantity_labels.push("shift in $x\ung{\mu m}$");
quantities.push("rp_shy"); quantity_labels.push("shift in $y\ung{\mu m}$");
//quantities.push("rp_rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string prefix = "tb,round1/";
string postfix_t = "/3,4,5,23,24,25-excl1981939712,2023555072/s,std,3pl,1rotzIt=0,units=2,overlap=t,3potsInO=t,eMuMvRot=f/iteration3";
string postfix_f = "/3,4,5,23,24,25-excl1981939712,2023555072/s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration3";

// fill 6877

// fill 6879
inputs.push(prefix + "319124.125-135" + postfix_t); input_pens.push(red);
inputs.push(prefix + "319124.125-135" + postfix_f); input_pens.push(red);
inputs.push(prefix + "319124.136-148" + postfix_t); input_pens.push(red);
inputs.push(prefix + "319124.136-148" + postfix_f); input_pens.push(red);

// fill 6881
inputs.push(prefix + "319159.164-201" + postfix_t); input_pens.push(blue);
inputs.push(prefix + "319159.164-201" + postfix_f); input_pens.push(blue);

// fill 6882
inputs.push(prefix + "319174.1-22" + postfix_t); input_pens.push(heavygreen);
inputs.push(prefix + "319174.1-22" + postfix_f); input_pens.push(heavygreen);

// fill 6884
inputs.push(prefix + "319190.18-28" + postfix_t); input_pens.push(magenta);
inputs.push(prefix + "319190.18-28" + postfix_f); input_pens.push(magenta);
inputs.push(prefix + "319190.29-38" + postfix_t); input_pens.push(magenta);
inputs.push(prefix + "319190.29-38" + postfix_f); input_pens.push(magenta);

// fill 6885
inputs.push(prefix + "319222.171-190" + postfix_t); input_pens.push(cyan);
inputs.push(prefix + "319222.171-190" + postfix_f); input_pens.push(cyan);

// fill 6890

// fill 6891

// fill 6892
inputs.push(prefix + "319311.27-49" + postfix_t); input_pens.push(brown);
inputs.push(prefix + "319311.27-49" + postfix_f); input_pens.push(brown);

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerRP();
