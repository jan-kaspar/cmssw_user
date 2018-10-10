import root;
import pad_layout;

string xangles[];
xangles.push("110");
xangles.push("130");
xangles.push("150");

string rps[], rp_labels[];
real x_min[];
rps.push("L_2_F"); rp_labels.push("45-220-fr"); x_min.push(1.3);
rps.push("L_1_F"); rp_labels.push("45-210-fr"); x_min.push(2.5);
rps.push("R_1_F"); rp_labels.push("56-210-fr"); x_min.push(2.0);
rps.push("R_2_F"); rp_labels.push("56-220-fr"); x_min.push(2.6);

transform xyswitch = (0, 0, 0, 1, 1, 0);

string f = "collect_data.root";

//----------------------------------------------------------------------------------------------------

NewPad(false);
for (int rpi : rps.keys)
{
	NewPad(false);
	label("{\SetFontSizesXX " + rp_labels[rpi] + "}");
}

for (int xai : xangles.keys)
{
	NewRow();

	NewPad(false);
	label("{\SetFontSizesXX xangle-" + xangles[xai] + "}");

	for (int rpi : rps.keys)
	{
		NewPad("$x_{\rm rel}\ung{mm}$", "$y_{\rm rel}\ung{mm}$");

		TH1_x_min = -10;
		TH1_x_max = +10;
		
		draw(xyswitch, RootGetObject(f, xangles[xai]+"/"+rps[rpi]+"/p_hor"), "d0,eb", black+1pt);

		TF1_x_min = -2;
		TF1_x_max = +7;
		RootObject o_fit_h = RootGetObject(f, xangles[xai]+"/"+rps[rpi]+"/p_hor|ff");
		draw(xyswitch, o_fit_h, "def", heavygreen+1pt);

		real h0 = o_fit_h.rExec("GetParameter", 0);
		real h1 = o_fit_h.rExec("GetParameter", 1);

		TH1_x_min = x_min[rpi];
		TH1_x_max = +5;

		draw(RootGetObject(f, xangles[xai]+"/"+rps[rpi]+"/p_vert"), "d0,eb", blue+1pt);

		RootObject o_fit_v = RootGetObject(f, xangles[xai]+"/"+rps[rpi]+"/p_vert|ff");

		TF1_x_min = -inf;
		draw(o_fit_v, "def", red+1pt);
		TF1_x_min = -1;
		draw(o_fit_v, "def", red+dashed);

		real v0 = o_fit_v.rExec("GetParameter", 0);
		real v1 = o_fit_v.rExec("GetParameter", 1);

		real x_cr = (h0 + h1*v0) / (1. - v1*h1);
		real y_cr = v0 + v1*x_cr;

		mark m = mCr+4pt+(magenta+1pt);
		draw((x_cr, y_cr), m);

		AddToLegend("beam position", m);
		AddToLegend(format("$x = %+#.3f\un{mm}$", x_cr));
		AddToLegend(format("$y = %+#.3f\un{mm}$", y_cr));

		limits((-1, -2), (5, 7), Crop);

		AttachLegend();
	}
}
