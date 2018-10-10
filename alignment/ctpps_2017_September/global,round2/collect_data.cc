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
  vector<string> xangles = {
    "110",
    "130",
    "150",
  };

  struct RPInfo {
    string tag;
    string sector;
    double x_min, x_max;
  };

  vector<RPInfo> rpInfos = {
    { "L_2_F", "sector 45", 1.3, 4.0 },
    { "L_1_F", "sector 45", 2.5, 4.5 },
    { "R_1_F", "sector 56", 2.0, 5.0 },
    { "R_2_F", "sector 56", 2.6, 5.0 },
  };

  // prepare output
  TFile *f_out = TFile::Open("collect_data.root", "recreate"); 

  TF1 *ff = new TF1("ff", "[0] + [1]*x");

  // process all data
  for (const auto &xangle : xangles)
  {
    TDirectory *d_xangle = f_out->mkdir(xangle.c_str());

    for (const auto &rpInfo : rpInfos)
    {
      TDirectory *d_rp = d_xangle->mkdir(rpInfo.tag.c_str());

      printf("* %s, %s\n", xangle.c_str(), rpInfo.tag.c_str());

      // get input
      TFile *f_in_hor = TFile::Open(("/afs/cern.ch/work/j/jkaspar/analyses/elastic/6500GeV/ctpps-2017-september/master/DS-xangle-"
        + xangle + "/alignment.root").c_str());

      TProfile *p_in_hor = (TProfile *) f_in_hor->Get(("period 0/unit " + rpInfo.tag + "/horizontal/horizontal profile/p").c_str());

      TFile *f_in_vert = TFile::Open(("/afs/cern.ch/work/j/jkaspar/analyses/ctpps/alignment/2017_postTS2/data/alig/fill_6228/xangle_"
        + xangle + "/DS1/distributions.root").c_str());

      TProfile *p_in_vert = (TProfile *) f_in_vert->Get((rpInfo.sector + "/profiles/" + rpInfo.tag + "/h_mean").c_str());

      if (p_in_hor == NULL || p_in_vert == NULL)
      {
        printf("ERROR: cannot get input.\n");
        continue;
      }

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
