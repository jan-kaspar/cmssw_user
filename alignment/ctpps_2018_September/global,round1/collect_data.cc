#include "TFile.h"
#include "TProfile.h"
#include "TF1.h"
#include "TGraph.h"

#include <vector>
#include <string>

using namespace std;

int main()
{
  // configuration
  struct LHCSettings {
    string xangle;
    string beta;
  };

  vector<LHCSettings> lhcSettings = {
    { "130", "27" },
    { "130", "25" },
  };

  struct RPInfo {
    string tag;
    string sector;
    double x_min, x_max;
  };

  vector<RPInfo> rpInfos = {
    { "L_2_F", "sector 45", 2.0, 5.0 },
    { "L_1_F", "sector 45", 2.5, 5.0 },
    { "R_1_F", "sector 56", 2.5, 4.0 },
    { "R_2_F", "sector 56", 3.0, 4.0 },
  };

  // prepare output
  TFile *f_out = TFile::Open("collect_data.root", "recreate"); 

  TF1 *ff = new TF1("ff", "[0] + [1]*x");

  // process all data
  for (const auto &lhcSet : lhcSettings)
  {
    TDirectory *d_lhcSet = f_out->mkdir(("xangle-" + lhcSet.xangle + "-beta-" + lhcSet.beta).c_str());

    for (const auto &rpInfo : rpInfos)
    {
      TDirectory *d_rp = d_lhcSet->mkdir(rpInfo.tag.c_str());

      // get input
      string fn_in_hor = "/afs/cern.ch/work/j/jkaspar/analyses/elastic/6500GeV/ctpps-2018-september/alignment/"
        "DS-xangle-" + lhcSet.xangle + "-beta-" + lhcSet.beta + "/alignment.root";
      TFile *f_in_hor = TFile::Open(fn_in_hor.c_str());
      if (f_in_hor == NULL)
      {
        printf("ERROR: can't open file '%s'.\n", fn_in_hor.c_str());
        return 1;
      }

      TProfile *p_in_hor = (TProfile *) f_in_hor->Get(("period 0/unit " + rpInfo.tag + "/horizontal/horizontal profile/p").c_str());
      if (p_in_hor == NULL)
      {
        printf("ERROR: can't get p_in_hor from file '%s'.\n", fn_in_hor.c_str());
        return 2;
      }

      string fn_in_vert = "/afs/cern.ch/work/j/jkaspar/analyses/ctpps/alignment/2018/data/alig/fill_7206/"
        "xangle_" + lhcSet.xangle + "_beta_0." + lhcSet.beta + "/DS1/distributions.root";
      TFile *f_in_vert = TFile::Open(fn_in_vert.c_str());
      if (f_in_vert == NULL)
      {
        printf("ERROR: can't open file '%s'.\n", fn_in_vert.c_str());
        return 3;
      }

      TProfile *p_in_vert = (TProfile *) f_in_vert->Get((rpInfo.sector + "/profiles/" + rpInfo.tag + "/h_mean").c_str());
      if (p_in_vert == NULL)
      {
        printf("ERROR: can't get p_in_vert from file '%s'.\n", fn_in_vert.c_str());
        return 4;
      }

      // process input
      ff->SetParameters(0., 0.);
      ff->SetRange(rpInfo.x_min, rpInfo.x_max);

      p_in_vert->Fit(ff, "", "", rpInfo.x_min, rpInfo.x_max);

      // write output
      gDirectory = d_rp;

      p_in_hor->Write("p_hor");
      p_in_vert->Write("p_vert");

      delete f_in_hor;
      delete f_in_vert;
    }
  }

  // clean up
  delete f_out;

  return 1;
}