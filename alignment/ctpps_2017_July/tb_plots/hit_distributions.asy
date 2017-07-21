import root;
import pad_layout;

/*
string dirs[] = {
	"tb,round1/10332/0,1,2,3,4,5-excl44/s+sr-fin,diag,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration2",
};

string rpSets[] = {
	"0, 4",
	"2, 3",
	"1, 5",
	"2, 3, 5",
	"0, 2, 3, 4",
	"1, 2, 3, 5",
};
*/

string dirs[] = {
	"tb,round1/10079/101,102,103,104,105/s+sr-fin,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration1",
	"tb,round1/10079/101,102,103,104,105/s+sr-fin,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration2",
	"tb,round1/10079/101,102,103,104,105/s+sr-fin,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration3",
	"tb,round1/10079/101,102,103,104,105/s+sr-fin,3pl,1rotzIt=0,units=2,overlap=f,3potsInO=t,eMuMvRot=f/iteration4",
};

string rpSets[] = {
	"101, 103, 105",
	"101, 105",
	"103, 104",
};

dotfactor = 2;

TGraph_nPointsLimit = 20000;

//----------------------------------------------------------------------------------------------------

for (int di = 0; di < dirs.length; ++di)
{
	string f = "../" + dirs[di] + "/diagnostics.root";

	NewRow();

	//--------------------
	
	NewPad("$a_x\ung{mrad}$", "$a_y\ung{mrad}$");
	currentpad.xTicks = LeftTicks(0.5, 0.1);
	currentpad.yTicks = RightTicks(0.5, 0.1);
	for (int rpsi : rpSets.keys)
	{
		RootObject obj = RootGetObject(f, "common/plots per RP set/" + rpSets[rpsi] + "/ax vs. ay, selected", error=true);
		if (obj.valid)
			draw(scale(1e3, 1e3), obj, "d", StdPen(rpsi + 1));
	}

	//--------------------
	
	NewPad("$b_x\ung{mm}$", "$b_y\ung{mm}$");
	currentpad.xTicks = LeftTicks(5., 1.);
	currentpad.yTicks = RightTicks(5., 1.);
	for (int rpsi : rpSets.keys)
	{
		pen p = StdPen(rpsi + 1);

		RootObject obj = RootGetObject(f, "common/plots per RP set/" + rpSets[rpsi] + "/bx vs. by, selected", error=true);
		if (obj.valid)
			draw(obj, "d", p);

		AddToLegend(rpSets[rpsi], mCi+2pt+p);
	}

	limits((-20, -25), (+20, +25), Crop);

	xaxis(YEquals(-3.5, false), black);
	
	yaxis(XEquals(4, false), black);

	//--------------------

	frame f_legend = BuildLegend();

	NewPad(false);
	attach(f_legend);

	//--------------------

	NewPad("$\ch^2 / \hbox{ndf}$");
	scale(Linear, Log);
	for (int rpsi : rpSets.keys)
	{
		pen p = StdPen(rpsi + 1);

		RootObject obj = RootGetObject(f, "common/plots per RP set/" + rpSets[rpsi] + "/chi^2 norm, lin, selected", error=true);
		if (obj.valid)
			draw(obj, "vl", p);
	}

	xlimits(0, 40, Crop);
	
}
