import root;
import pad_layout;

string xangles[];
xangles.push("xangle-def-beta-def");

string rps[], rp_labels[];
real x_min[];
rps.push("L_1_F"); rp_labels.push("45-210-fr"); x_min.push(2.0);
rps.push("L_1_N"); rp_labels.push("45-210-nr"); x_min.push(2.5);
rps.push("R_1_N"); rp_labels.push("56-210-nr"); x_min.push(2.5);
rps.push("R_1_F"); rp_labels.push("56-210-fr"); x_min.push(3.0);

transform xyswitch = (0, 0, 0, 1, 1, 0);

string f = "collect_data.root";

//----------------------------------------------------------------------------------------------------

//NewPad(false);
for (int rpi : rps.keys)
{
	NewPad(false);
	label("{\SetFontSizesXX " + rp_labels[rpi] + "}");
}

for (int xai : xangles.keys)
{
	NewRow();

	//NewPad(false);
	//label("{\SetFontSizesXX " + xangles[xai] + "}");

	for (int rpi : rps.keys)
	{
		NewPad("$x\ung{mm}$", "$y\ung{mm}$");

		TH1_x_min = -10;
		TH1_x_max = +10;
		
		draw(xyswitch, RootGetObject(f, xangles[xai]+"/"+rps[rpi]+"/p_hor"), "d0,eb", black+1pt);

		TF1_x_min = -5;
		TF1_x_max = +5;
		RootObject o_fit_h = RootGetObject(f, xangles[xai]+"/"+rps[rpi]+"/p_hor|ff");
		draw(xyswitch, o_fit_h, "def", heavygreen+1pt);

		real h0 = o_fit_h.rExec("GetParameter", 0);
		real h1 = o_fit_h.rExec("GetParameter", 1);

		TH1_x_min = x_min[rpi];
		TH1_x_max = +9;

		real v0 = 0., v1 = 0.;

		if (rps[rpi] != "R_1_N")
		{
			draw(RootGetObject(f, xangles[xai]+"/"+rps[rpi]+"/p_vert"), "d0,eb", blue+1pt);

			RootObject o_fit_v = RootGetObject(f, xangles[xai]+"/"+rps[rpi]+"/p_vert|ff");

			TF1_x_min = -inf;
			TF1_x_max = +inf;
			draw(o_fit_v, "def", red+1pt);
			TF1_x_min = -1;
			draw(o_fit_v, "def", red+dashed);

			v0 = o_fit_v.rExec("GetParameter", 0);
			v1 = o_fit_v.rExec("GetParameter", 1);
		}

		real x_cr = (h0 + h1*v0) / (1. - v1*h1);
		real y_cr = v0 + v1*x_cr;

		mark m = mCr+4pt+(magenta+1pt);
		draw((x_cr, y_cr), m);

		AddToLegend("beam position", m);
		AddToLegend(format("$x = %+#.3f\un{mm}$", x_cr));
		AddToLegend(format("$y = %+#.3f\un{mm}$", y_cr));

		write("x_" + rp_labels[rpi] + format(" = %+#.3f", x_cr));
		write("y_" + rp_labels[rpi] + format(" = %+#.3f", y_cr));
		write("");

		limits((-1, -5.5), (9, 5.5), Crop);

		AttachLegend();
	}
}