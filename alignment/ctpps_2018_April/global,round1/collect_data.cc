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
    { "160", "30" },
    { "131", "30" },
    { "130", "30" },
    { "130", "25" },
  };

  struct RPInfo {
    string tag;
    double x_min, x_max;
  };

  vector<RPInfo> rpInfos = {
    { "L_2_F", 2.0, 6.0 },
    { "L_1_F", 2.5, 6.0 },
    { "R_1_F", 2.5, 4.5 },
    { "R_2_F", 3.0, 4.5 },
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
      TFile *f_in_hor = TFile::Open(("/afs/cern.ch/work/j/jkaspar/analyses/elastic/6500GeV/ctpps-2018-april/alignment/"
        "DS-xangle-" + lhcSet.xangle + "-beta-" + lhcSet.beta + "/alignment.root").c_str());

      TProfile *p_in_hor = (TProfile *) f_in_hor->Get(("period 0/unit " + rpInfo.tag + "/horizontal/horizontal profile/p").c_str());

      TFile *f_in_vert = TFile::Open(("/afs/cern.ch/work/j/jkaspar/analyses/ctpps/alignment/2018_preTS2/data/alig/fill_6554/"
        "xangle_" + lhcSet.xangle + "_beta_" + lhcSet.beta + "/DS1/distributions.root").c_str());

      TProfile *p_in_vert = (TProfile *) f_in_vert->Get(("profiles/" + rpInfo.tag + "/h_mean").c_str());

      // process input
      ff->SetParameters(0., 0.);
      ff->SetRange(0., 5.);

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
