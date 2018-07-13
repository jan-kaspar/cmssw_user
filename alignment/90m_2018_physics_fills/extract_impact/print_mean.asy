import root;
import pad_layout;

string f = "output_319125.root";

string table[][];
table.push(new string[]{ "24", "4", "104", "124"});
table.push(new string[]{ "25", "5", "105", "125"});

	for (int row : table.keys)
	{
		for (int col : table[row].keys)
		{
			RootObject obj_x = RootGetObject(f, "RP " + table[row][col] + "/h_de_x");
			real mean_x = obj_x.rExec("GetMean");

			RootObject obj_y = RootGetObject(f, "RP " + table[row][col] + "/h_de_y");
			real mean_y = obj_y.rExec("GetMean");

			write("alignment_corrections[" + table[row][col] + "] = UnitHitData(false, " + format("%+#.3f", mean_x) + format(", %+#.3f);", mean_y));
		}
	}
