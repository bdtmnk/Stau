#include <iostream>
#include <vector>
#include <map>
#include "boost/lexical_cast.hpp"
#include "boost/algorithm/string.hpp"
#include "boost/format.hpp"
#include "boost/program_options.hpp"
#include "boost/range/algorithm.hpp"
#include "boost/range/algorithm_ext.hpp"
#include "Plotting.h"
#include "Plotting_Style.h"
#include "TPad.h"
#include "TROOT.h"
#include "TColor.h"
#include "TEfficiency.h"
#include "TMath.h"

void Plot2histo()
{
    TFile * file = new TFile("test_Nominal_C.root");

    TH1D * histo1 = (TH1D*)file->Get("mutau/TaupT_1");
    TH1D * histo2 = (TH1D*)file->Get("mutau/TaupT_4");

   
	histo1->Scale(1/histo1->GetSumOfWeights());
	histo2->Scale(1/histo2->GetSumOfWeights());

	gStyle->SetOptStat(0);

	TCanvas* canv1 = new TCanvas("c1", "c1");

    TLegend *legend = new TLegend(0.5,0.7,0.9,0.9);
    legend->AddEntry(histo1, "DPT tight Tau", "l");
    legend->AddEntry(histo2, "MVA loose && not DPT tight Tau", "l");

    histo1->SetLineColor(1);
    histo2->SetLineColor(2);
	histo2->Draw("sameh");

	histo1->Draw("sameh");

        legend->Draw();

    canv1->Update();
    canv1->Print("/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/test/MVA/fakesTest.pdf");




}
