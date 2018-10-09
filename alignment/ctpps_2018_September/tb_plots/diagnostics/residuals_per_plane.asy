import root;
import pad_layout;

string topDir = "../../";

string planes[], plane_labels[];
pen plane_pens[];
real plane_scale[];

planes.push("2040004608"); plane_labels.push("56-220-fr-hr, plane 0"); plane_pens.push(heavygreen); plane_scale.push(1e-1);
//planes.push("2040070144"); plane_labels.push("56-220-fr-hr, plane 1"); plane_pens.push(blue); plane_scale.push(1e-1);
//planes.push("2040332288"); plane_labels.push("56-220-fr-hr, plane 5"); plane_pens.push(red); plane_scale.push(1e-1);
planes.push("2006974464"); plane_labels.push("56-220-fr-tp, plane 0"); plane_pens.push(cyan); plane_scale.push(1.);
planes.push("2007498752"); plane_labels.push("56-220-fr-bt, plane 0"); plane_pens.push(magenta); plane_scale.push(1.);

/*
planes.push("2040070144"); plane_labels.push("56-220-fr-hr, plane 1"); plane_pens.push(black); plane_scale.push(1.);
planes.push("2007007232"); plane_labels.push("56-220-fr-tp, plane 1"); plane_pens.push(red); plane_scale.push(1.);
planes.push("2007531520"); plane_labels.push("56-220-fr-bt, plane 1"); plane_pens.push(blue); plane_scale.push(1.);
*/


string iterations[], iteration_labels[];
iterations.push("1"); iteration_labels.push("iteration 1");
//iterations.push("2"); iteration_labels.push("iteration 2");
iterations.push("3"); iteration_labels.push("iteration 3");

string dir = "tb,round1-short/314247/103,104,105,123,124,125/s,std,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f";

//----------------------------------------------------------------------------------------------------

frame f_legend;

for (int iti : iterations.keys)
{
	NewPad("$\hbox{residual}\ung{mm}$");
	//scale(Linear, Log);

	string f = topDir + dir + "/iteration" + iterations[iti] + "/diagnostics.root";

	for (int pli : planes.keys)
	{
		//RootObject obj = RootGetObject(f, "Jan/"+planes[pli]+"/"+planes[pli]+": R distribution");
		RootObject obj = RootGetObject(f, "common/residuals/"+planes[pli]+"/"+planes[pli]+": total_selected");
		obj.vExec("Rebin", 2);

		draw(scale(1., plane_scale[pli]), 
			obj, "vl", plane_pens[pli], plane_labels[pli]);
	}

	if (iterations[iti] == "1")
	{
		xlimits(-1, +2, Crop);
		currentpad.xTicks = LeftTicks(0.5, 0.1);
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
