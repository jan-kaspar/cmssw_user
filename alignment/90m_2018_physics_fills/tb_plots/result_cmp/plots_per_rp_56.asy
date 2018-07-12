include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(101); unit_names.push("56-210-fr");
units.push(121); unit_names.push("56-220-fr");

//excludedRPs = new int[] { 100 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("rp_shx"); quantity_labels.push("shift in $x\ung{\mu m}$");
quantities.push("rp_shy"); quantity_labels.push("shift in $y\ung{\mu m}$");
//quantities.push("rp_rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string prefix = "tb,round1/";
string postfix = "/103,104,105,123,124,125/s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration3";

// fill 6877
//inputs.push(prefix + "319097.37-136" + postfix); input_pens.push(black);
//inputs.push(prefix + "319104.1-21" + postfix); input_pens.push(black);

// fill 6879
inputs.push(prefix + "319124.125-135" + postfix); input_pens.push(red);
inputs.push(prefix + "319124.136-148" + postfix); input_pens.push(red);

// fill 6881
//inputs.push(prefix + "319159.1-3" + postfix); input_pens.push(blue);
inputs.push(prefix + "319159.164-201" + postfix); input_pens.push(blue);

// fill 6882
//inputs.push(prefix + "319174.1-22" + postfix); input_pens.push(heavygreen);
//inputs.push(prefix + "319177.1-10" + postfix); input_pens.push(heavygreen);

// fill 6884
inputs.push(prefix + "319190.18-28" + postfix); input_pens.push(magenta);
inputs.push(prefix + "319190.29-38" + postfix); input_pens.push(magenta);

// fill 6885
inputs.push(prefix + "319222.171-190" + postfix); input_pens.push(cyan);
//inputs.push(prefix + "319223.1-4" + postfix); input_pens.push(cyan);

// fill 6890
//inputs.push(prefix + "319254.154-164" + postfix); input_pens.push(green);
//inputs.push(prefix + "319254.165-167" + postfix); input_pens.push(green);

// fill 6891
inputs.push(prefix + "319300.26-47" + postfix); input_pens.push(orange);
//inputs.push(prefix + "319274.1-7" + postfix); input_pens.push(orange);

// fill 6892
//inputs.push(prefix + "319311.1-6" + postfix); input_pens.push(brown);
//inputs.push(prefix + "319311.27-49" + postfix); input_pens.push(brown);

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerRP();
