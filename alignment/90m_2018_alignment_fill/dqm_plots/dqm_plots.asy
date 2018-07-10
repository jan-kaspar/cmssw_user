import root;
import pad_layout;

string files[], runs[];
files.push("DQM_V0001_CTPPS_R000318546.root"); runs.push("318546");
files.push("DQM_V0001_CTPPS_R000318551.root"); runs.push("318551");

string table[][];

table.push(new string[] {
	"TrackingStrip/sector 45/station 220/fr_tp/activity in planes (2D)",
	"TrackingStrip/sector 45/station 210/fr_tp/activity in planes (2D)",
	"TrackingStrip/sector 56/station 210/fr_tp/activity in planes (2D)",
	"TrackingStrip/sector 56/station 220/fr_tp/activity in planes (2D)",
});

table.push(new string[] {
	"TrackingPixel/sector 45/station 220/fr_hr/ROCs hits multiplicity per event",
	"TrackingPixel/sector 45/station 210/fr_hr/ROCs hits multiplicity per event",
	"TrackingPixel/sector 56/station 210/fr_hr/ROCs hits multiplicity per event",
	"TrackingPixel/sector 56/station 220/fr_hr/ROCs hits multiplicity per event",
});

table.push(new string[] {
	"TrackingStrip/sector 45/station 220/fr_bt/activity in planes (2D)",
	"TrackingStrip/sector 45/station 210/fr_bt/activity in planes (2D)",
	"TrackingStrip/sector 56/station 210/fr_bt/activity in planes (2D)",
	"TrackingStrip/sector 56/station 220/fr_bt/activity in planes (2D)",
});

//----------------------------------------------------------------------------------------------------

for (int fi : files.keys)
{
	string prefix = "DQMData/Run " + runs[fi] + "/CTPPS/Run summary/";

	for (int ri : table.keys)
	{
		NewRow();

		for (int ci : table[ri].keys)
		{
			NewPad();

			draw(RootGetObject(files[fi], prefix + table[ri][ci]));
		}
	}

	GShipout("dqm_plots_" + runs[fi]);
}
