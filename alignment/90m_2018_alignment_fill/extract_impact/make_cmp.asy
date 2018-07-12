import root;
import pad_layout;

string files[] = {
	//"output_318546.root",
	//"output_318547.root",
	//"output_318548.root",
	//"output_318549.root",
	"output_318550.root",
	"output_318551.root",
};

string table[][];
table.push(new string[]{ "24", "4", "104", "124"});
table.push(new string[]{ "25", "5", "105", "125"});

string quantities[] = {
	"x",
	"y",
};

for (int qi : quantities.keys)
{
	for (int row : table.keys)
	{
		NewRow();

		for (int col : table[row].keys)
		{
			NewPad("$\De " + quantities[qi] + "\ung{mm}$");

			for (int fi : files.keys)
			{
				RootObject obj = RootGetObject(files[fi], "RP " + table[row][col] + "/h_de_" + quantities[qi]);
				real mean = obj.rExec("GetMean");
				string l = format("mean = %+#.3f", mean);
				draw(obj, "vl", StdPen(fi)+1pt, l);
			}

			AttachLegend("RP " + table[row][col]);
		}
	}

	GShipout("make_cmp_" + quantities[qi]);
}
