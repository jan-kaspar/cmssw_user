include "common_plots.asy";

//----------------------------------------------------------------------------------------------------

units.push(101); unit_names.push("56-210-fr");
units.push(121); unit_names.push("56-220-fr");

//excludedRPs = new int[] { 100 };

groups = new string[] { "top", "hor", "bot" };

quantities.push("shx"); quantity_labels.push("shift in $x\ung{\mu m}$");
quantities.push("shy"); quantity_labels.push("shift in $y\ung{\mu m}$");
quantities.push("rotz"); quantity_labels.push("rotation about $z\ung{mrad}$");

string prefix = "tb,round1/";
string postfix = "/103,104,105,123,124,125/ev=1E5,pl=3,units=2,ovlp=f,3rpsInO=t/s+sr,std,1rotzIt=0,eMuMvRot=t/iteration4";

inputs.push(prefix + "324462.166-251" + postfix); input_pens.push(blue);
inputs.push(prefix + "324462.252-336" + postfix); input_pens.push(cyan);

inputs.push(prefix + "324532.399-459" + postfix); input_pens.push(red);
inputs.push(prefix + "324532.460-520" + postfix); input_pens.push(magenta);

inputs.push(prefix + "324536.360-434" + postfix); input_pens.push(heavygreen);
inputs.push(prefix + "324536.435-509" + postfix); input_pens.push(green);

//----------------------------------------------------------------------------------------------------

LoadAlignments();
MakePlotsPerPlane();
