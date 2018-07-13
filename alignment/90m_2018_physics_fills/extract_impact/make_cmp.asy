import root;
import pad_layout;

string runs[] = {
	"319097",
	"319125",
	"319266",
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

			for (int ri : runs.keys)
			{
				RootObject obj = RootGetObject("output_" + runs[ri] + ".root", "RP " + table[row][col] + "/h_de_" + quantities[qi]);
				real mean = obj.rExec("GetMean");
				string l = runs[ri] + format(": mean = %+#.3f", mean);
				draw(obj, "vl", StdPen(ri)+1pt, l);
			}

			AttachLegend("RP " + table[row][col]);
		}
	}

	GShipout("make_cmp_" + quantities[qi]);
}
