import root;
import pad_layout;

//----------------------------------------------------------------------------------------------------

string topDir = "../../";

dotfactor = 2;

TGraph_nPointsLimit = 5000;

//----------------------------------------------------------------------------------------------------

for (int di = 0; di < dirs.length; ++di)
{
	string f = topDir + dirs[di] + "/diagnostics.root";

	NewRow();

	//--------------------

	NewPad(false);
	label("{\SetFontSizesXX " + d_labels[di] + "}");

	//--------------------
	
	/*
	NewPad("$a_x\ung{mrad}$", "$a_y\ung{mrad}$");
	currentpad.xTicks = LeftTicks(0.5, 0.1);
	currentpad.yTicks = RightTicks(0.5, 0.1);
	for (int rpsi : rpSets.keys)
	{
		RootObject obj = RootGetObject(f, "common/plots per RP set/" + rpSets[rpsi] + "/ax vs. ay, selected", error=true);
		if (obj.valid)
			draw(scale(1e3, 1e3), obj, "d", rps_pens[rpsi]);
	}
	*/

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

	real w = 24;
	real h = 16;

	draw(shift(pixel_x_min, pixel_y_cen) * ( (0, -h/2)--(w, -h/2)--(w, +h/2)--(0, +h/2)--cycle ), black);

	draw(shift(pixel_x_min, pixel_y_cen-h/4) * ( (0, -h/4)--(w/3, -h/4)--(w/3, +h/4)--(0, +h/4)--cycle ), black);

	limits((-20, -25), (+20, +25), Crop);

	//xaxis(YEquals(-3.5, false), black);
	
	//yaxis(XEquals(4, false), black);

	//--------------------

	frame f_legend = BuildLegend();

	NewPad(false);
	attach(f_legend);

	//--------------------

	/*
	NewPad("$\ch^2 / \hbox{ndf}$");
	scale(Linear, Log);
	for (int rpsi : rpSets.keys)
	{
		pen p = rps_pens[rpsi];

		RootObject obj = RootGetObject(f, "common/plots per RP set/" + rpSets[rpsi] + "/chi^2 norm, lin, selected", error=true);
		if (obj.valid)
			draw(obj, "vl", p);
	}

	xlimits(0, 40, Crop);
	*/
	
}
