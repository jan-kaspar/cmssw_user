import root;
import pad_layout;

string planes[], plane_labels[];
pen plane_pens[];
real plane_scale[];

planes.push("0"); plane_labels.push("45-210-nr-tp, plane 0"); plane_pens.push(black); plane_scale.push(1.);
planes.push("10"); plane_labels.push("45-210-nr-bt, plane 0"); plane_pens.push(red); plane_scale.push(1.);
planes.push("20"); plane_labels.push("45-210-nr-hr, plane 0"); plane_pens.push(blue); plane_scale.push(1e-2);

/*
planes.push("30"); plane_labels.push("30"); plane_pens.push(black); plane_scale.push(1e-2);
planes.push("40"); plane_labels.push("40"); plane_pens.push(red); plane_scale.push(1.);
planes.push("50"); plane_labels.push("50"); plane_pens.push(blue); plane_scale.push(1.);
*/

string iterations[], iteration_labels[];
iterations.push("1"); iteration_labels.push("iteration 1");
iterations.push("2"); iteration_labels.push("iteration 2");
iterations.push("4"); iteration_labels.push("iteration 4");

string dir = "tb,round1/10332/0,1,2,3,4,5-excl44/s+sr-fin,diag,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f";

//----------------------------------------------------------------------------------------------------

frame f_legend;

for (int iti : iterations.keys)
{
	NewPad("$\hbox{residual}\ung{mm}$");

	string f = "../" + dir + "/iteration" + iterations[iti] + "/diagnostics.root";

	for (int pli : planes.keys)
	{
		RootObject obj = RootGetObject(f, "Jan/"+planes[pli]+"/"+planes[pli]+": R distribution");
		obj.vExec("Rebin", 4);

		draw(scale(1., plane_scale[pli]), 
			obj, "vl", plane_pens[pli], plane_labels[pli]);
	}

	if (iterations[iti] == "1")
	{
		xlimits(-0.4, +0.4, Crop);
		currentpad.xTicks = LeftTicks(0.2, 0.1);
	} else {
		xlimits(-0.1, +0.1, Crop);
		currentpad.xTicks = LeftTicks(0.05, 0.01);
	}

	f_legend = BuildLegend();

	currentpicture.legend.delete();
	AttachLegend(iteration_labels[iti]);
}
	
NewPad(false);
attach(f_legend);
