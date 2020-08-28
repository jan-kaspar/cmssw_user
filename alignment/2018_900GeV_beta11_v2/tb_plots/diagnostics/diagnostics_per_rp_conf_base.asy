import root;
import pad_layout;

//----------------------------------------------------------------------------------------------------

string topDir = "../../";

dotfactor = 2;

TGraph_nPointsLimit = 2000;

//----------------------------------------------------------------------------------------------------

for (int di = 0; di < dirs.length; ++di)
{
	string f = topDir + dirs[di] + "/diagnostics.root";

	NewRow();

	//--------------------

	NewPad(false);
	label("{\SetFontSizesXX " + d_labels[di] + "}");

	//--------------------
	
	NewPad("$a_x\ung{mrad}$", "$a_y\ung{mrad}$");
	currentpad.xTicks = LeftTicks(0.5, 0.1);
	currentpad.yTicks = RightTicks(0.5, 0.1);
	for (int rpsi : rpSets.keys)
	{
		RootObject obj = RootGetObject(f, "common/plots per RP set/" + rpSets[rpsi] + "/ax vs. ay, selected", error=true);
		if (obj.valid)
			draw(scale(1e3, 1e3), obj, "d", rps_pens[rpsi]);
	}
	limits((-0.5, -0.5), (+0.5, +0.5), Crop);

	//--------------------
	
	NewPad("$b_x\ung{mm}$", "$b_y\ung{mm}$");
	currentpad.xTicks = LeftTicks(5., 1.);
	currentpad.yTicks = RightTicks(5., 1.);
	for (int rpsi : rpSets.keys)
	{
		pen p = rps_pens[rpsi];

		RootObject obj = RootGetObject(f, "common/plots per RP set/" + rpSets[rpsi] + "/bx vs. by, selected", error=true);
		if (obj.valid)
			draw(obj, "d", p);

		AddToLegend(rpSets[rpsi], mCi+2pt+p);
	}

	limits((-20, -25), (+20, +25), Crop);

	//xaxis(YEquals(-3.5, false), black);
	
	//yaxis(XEquals(4, false), black);

	//--------------------

	frame f_legend = BuildLegend();

	NewPad(false);
	attach(f_legend);

	//--------------------

	NewPad("$\ch^2 / \hbox{ndf}$");
	scale(Linear, Log);
	for (int rpsi : rpSets.keys)
	{
		pen p = rps_pens[rpsi];

		RootObject obj = RootGetObject(f, "common/plots per RP set/" + rpSets[rpsi] + "/chi^2 norm, lin, selected", error=true);
		if (obj.valid)
			draw(obj, "vl", p);
	}

	xlimits(0, 10, Crop);
	
}
