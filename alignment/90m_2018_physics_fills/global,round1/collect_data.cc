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
  map<string, string> rps = {
    { "L_2_F", "45_220_fr" },
    { "L_1_F", "45_210_fr" },
    { "R_1_F", "56_210_fr" },
    { "R_2_F", "56_220_fr" },
  };

  // get input
  TFile *f_in = TFile::Open("/afs/cern.ch/work/j/jkaspar/analyses/elastic/6500GeV/beta90_2018/10sigma-alignment/alignment/global_fit.root");

  //topDir+datasets[di]+"/alignment_fit.root", ""+units[ui]+"/b_fit"
  //draw(swToHours, RootGetObject(topDir+datasets[di]+"/alignment_fit.root", ""+units[ui]+"/c_fit"), "l", red+1.5pt);

  for (const auto& rp : rps)
  {
    TGraph *g_b = (TGraph *) f_in->Get((rp.first + "/b_fit").c_str());
    TGraph *g_c = (TGraph *) f_in->Get((rp.first + "/c_fit").c_str());

    double b = g_b->GetY()[0];
    double c = g_c->GetY()[0];

    printf("x_%s = %+.3f\n", rp.second.c_str(), b*1E-3);
    printf("y_%s = %+.3f\n", rp.second.c_str(), c*1E-3);
    printf("\n");
  }

  // clean up
  delete f_in;

  return 1;
}
