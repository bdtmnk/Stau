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
    TFile * file2 = new TFile("Stau100_LSP1_left_Nominal_B.root");
    TFile * file = new TFile("Stau100_LSP1_left_Nominal_B_old.root");

    TH1D * histo1 = (TH1D*)file->Get("mutau/BDTmutau_Stau100_16");
    TH1D * histo2 = (TH1D*)file2->Get("mutau/BDTmutau_Stau100_16");

cout << "AAAA"<<endl;   
	//histo1->Scale(1/histo1->GetSumOfWeights());
	//histo2->Scale(1/histo2->GetSumOfWeights());

	gStyle->SetOptStat(0);

	TCanvas* canv1 = new TCanvas("c1", "c1");
    cout << "AAAA"<<endl;   

    TLegend *legend = new TLegend(0.5,0.7,0.9,0.9);
    legend->AddEntry(histo1, "Normal", "l");
    legend->AddEntry(histo2, "with prefired jets", "l");
    cout << "AAAA"<<endl;   

    histo1->SetLineColor(1);
    histo2->SetLineColor(2);
    cout << "AAAA"<<endl;   

	histo1->Draw("sameh");
cout << "AAAA"<<endl;   

	histo2->Draw("sameh");
cout << "AAAA"<<endl;   

        legend->Draw();

    canv1->Update();
    canv1->Print("/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_9_4_0_patch1/src/DesyTauAnalyses/NTupleMaker/test/plots_mutau/PrefiringTest.pdf");




}
