import pad_layout;
import common_code;

//----------------------------------------------------------------------------------------------------

string topDir = "../../";

drawGridDef = true;

xSizeDef = 7cm;

//----------------------------------------------------------------------------------------------------

string quantities[];

int units[];
string unit_names[];

int excludedRPs[];

string groups[];

string quantities[];
string quantity_labels[];

string inputs[];
pen input_pens[];

//----------------------------------------------------------------------------------------------------

Alignment alignments[];

void LoadAlignments()
{
	alignments.delete();
	
	for (int ini : inputs.keys)
	{
		string f = topDir + inputs[ini] + "/results_cumulative_factored_Jan.xml";
	
		Alignment a;
		int r = ParseXML(f, a);
		if (r != 0)
		{
			write("ERROR: can't parse " + f + ".");
			continue;
		}
	
		alignments[ini] = a;
	}
}

//----------------------------------------------------------------------------------------------------

void MakePlotsPerRP()
{
	for (int qi : quantities.keys)
	{
		NewPage();

		string quantity = quantities[qi];
		write("* " + quantity);
	
		// plot header
		NewPad(false);
		label("{\SetFontSizesXX\it " + replace(quantities[qi], "_", "\_") + "}");
		
		for (int uniti : units.keys)
		{
			NewPad(false);
			label("{\SetFontSizesXX " + unit_names[uniti] + "}");
		}
		
		// plot results
		for (string group : groups)
		{
			NewRow();
		
			NewPad(false);
			label("{\SetFontSizesXX " + group + "}");
			
		
			for (int unit : units)
			{
				int st = quotient(unit, 10);
				int arm = quotient(st, 10);
				int uidx = unit % 10;
		
				int rp = st * 10;
				if (group == "top" && uidx == 0) rp += 0;
				if (group == "bot" && uidx == 0) rp += 1;
				if (group == "hor" && uidx == 0) rp += 2;
				if (group == "hor" && uidx == 1) rp += 3;
				if (group == "top" && uidx == 1) rp += 4;
				if (group == "bot" && uidx == 1) rp += 5;
		
				NewPad("", quantity_labels[qi]);
				scale(Linear, Linear(false));
	
				bool rpExcluded = false;
				for (int erp : excludedRPs)
				{
					if (erp == rp)
					{
						rpExcluded = true;
						break;
					}
				}

				if (rpExcluded)
					continue;

				real q_min = +1e100, q_max = -1e100;

				for (int ai : alignments.keys)
				{
					pen p = input_pens[ai];
					mark m = mCi;
	
					//if (!alignments[ai].rp_shx.initialized(rp))
					//	continue;
		
					real qv = GetQuantity(alignments[ai], quantity, rp);
					real qu = GetQuantity(alignments[ai], quantity+"_e", rp);
			
					draw((ai, qv-qu)--(ai, qv+qu), p);
					draw((ai, qv), m+3pt+(p+1.5pt));

					if (qv < q_min)
						q_min = qv;

					if (qv > q_max)
						q_max = qv;
				}
		
				xlimits(-0.5, inputs.length - 0.5, Crop);

				AttachLegend(format("max - min = %.3f", q_max - q_min), SE, NE);
			}
		}
	
		NewPad(false);
	
		for (int ini : inputs.keys)
		{
			AddToLegend(replace(inputs[ini], "_", "\_"), input_pens[ini]);
		}
	
		AttachLegend();
	}
}

//----------------------------------------------------------------------------------------------------

void MakePlotsPerPlane()
{
	for (int qi : quantities.keys)
	{
		NewPage();

		string quantity = quantities[qi];
		write("* " + quantity);
	
		// plot header
		NewPad(false);
		label("{\SetFontSizesXX\it " + replace(quantities[qi], "_", "\_") + "}");
		
		for (int uniti : units.keys)
		{
			NewPad(false);
			label("{\SetFontSizesXX " + unit_names[uniti] + "}");
		}
		
		// plot results
		for (string group : groups)
		{
			NewRow();
		
			NewPad(false);
			label("{\SetFontSizesXX " + group + "}");	
		
			for (int unit : units)
			{
				int st = quotient(unit, 10);
				int arm = quotient(st, 10);
				int uidx = unit % 10;
		
				int rp = st * 10;
				if (group == "top" && uidx == 0) rp += 0;
				if (group == "bot" && uidx == 0) rp += 1;
				if (group == "hor" && uidx == 0) rp += 2;
				if (group == "hor" && uidx == 1) rp += 3;
				if (group == "top" && uidx == 1) rp += 4;
				if (group == "bot" && uidx == 1) rp += 5;
		
				NewPad("", quantity_labels[qi]);
				scale(Linear, Linear(false));

				bool rpExcluded = false;
				for (int erp : excludedRPs)
				{
					if (erp == rp)
					{
						rpExcluded = true;
						break;
					}
				}

				if (rpExcluded)
					continue;
	
				for (int pl = 0; pl < 10; ++pl)
				{
					int det = 10*rp + pl;
				
					for (int ai : alignments.keys)
					{
						pen p = input_pens[ai];
			
						if (!alignments[ai].shr.initialized(det))
							continue;
			
						real qv = GetQuantity(alignments[ai], quantity, det);
						real qu = GetQuantity(alignments[ai], quantity+"_e", det);
				
						mark m;
						string st = alignments[ai].sensorType[det];
						if (st == "strips, V") m = mCr;
						if (st == "strips, U") m = mCi+false;
						if (st == "pixels") m = mSq;

						draw((pl, qv-qu)--(pl, qv+qu), p);
						draw((pl, qv), m+3pt+(p+1.5pt));
					}
				}
	
				/*
				if (quantity == "shr")
					limits((0, -200), (9, +200), Crop);
			
				// TODO
				if (quantity == "rotz")
					limits((0, -1.5), (9, +1.5), Crop);
				*/
			}
		}
	
		//--------------------
	
		NewPad(false);
	
		AddToLegend("strips, V plane", mCr+3pt+(black+1.5pt));
		AddToLegend("strips, U plane", mCi+false+3pt+(black+1.5pt));
		AddToLegend("pixels", mSq+3pt+(black+1.5pt));
	
		for (int ini : inputs.keys)
			AddToLegend(replace(inputs[ini], "_", "\_"), input_pens[ini]);
	
		AttachLegend();
	}
}
