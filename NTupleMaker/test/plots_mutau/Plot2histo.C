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
#include "HttStylesNew.cc"
#include "TPad.h"
#include "TROOT.h"
#include "TColor.h"
#include "TEfficiency.h"
#include "TMath.h"

void Plot2histo()
{
    TFile * file1 = new TFile("Stau100_LSP1_left_Nominal_B.root");
    TFile * file2 = new TFile("Stau100_LSP1_LiveTime0.10_right_B_OS_Nominal_B.root");
//TFile * file3 = new TFile("/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/test/plots_mutau/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_Nominal_B.root");
//TFile * file4 = new TFile("/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/test/plots_mutau/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_Nominal_B.root");
//TFile * file5 = new TFile("/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/test/plots_mutau/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_Nominal_B.root");

//TString var = "CutFlowUnW";
TString var = "METFB_12";

    TH1D * histo1 = (TH1D*)file1->Get("mutau/"+var);
    TH1D * histo2 = (TH1D*)file2->Get("mutau/"+var);

  //  TH1D * histo3 = (TH1D*)file3->Get("mutau/METFB_15");
  //  TH1D * histo4 = (TH1D*)file4->Get("mutau/METFB_15");
  //  TH1D * histo5 = (TH1D*)file5->Get("mutau/METFB_15");


    //TH1D * histo2 = (TH1D*)file2->Get("mutau/BDTmutau_stau100_LSP1My_18");

   histo1->Sumw2();
      histo2->Sumw2();
   
  //    histo3->Sumw2();
  //    histo4->Sumw2();
  //    histo5->Sumw2();


    TH1D * histo1w = (TH1D*)file1->Get("mutau/histWeightsH");
    TH1D * histo2w = (TH1D*)file2->Get("mutau/histWeightsH");
   // TH1D * histo3w = (TH1D*)file3->Get("mutau/histWeightsH");
   // TH1D * histo4w = (TH1D*)file4->Get("mutau/histWeightsH");
   // TH1D * histo5w = (TH1D*)file5->Get("mutau/histWeightsH");
   


	histo1->Scale(1/histo1->GetSumOfWeights());
	histo2->Scale(1/histo2->GetSumOfWeights());
    //    histo3->Scale(332.8*36000/histo3w->GetSumOfWeights());
    //    histo4->Scale(101.8*36000/histo4w->GetSumOfWeights());
    //    histo5->Scale(54.8*36000/histo5w->GetSumOfWeights());

//histo2->Add(histo2,histo3);
//histo2->Add(histo2,histo4);

//histo2->Add(histo2,histo5);

  //      histo2->Scale(1/histo2->GetSumOfWeights());
cout <<"hist1w  "<<histo1w->GetSumOfWeights() <<endl;
cout <<"hist2w  "<<histo2w->GetSumOfWeights() <<endl;

cout <<"hist1  "<<histo1->GetSumOfWeights() <<endl;
cout <<"hist2  "<<histo2->GetSumOfWeights() <<endl;
//cout <<"hist3  "<<histo3->GetSumOfWeights() <<endl;
//cout <<"hist4  "<<histo4->GetSumOfWeights() <<endl;
//cout <<"hist5  "<<histo5->GetSumOfWeights() <<endl;


	gStyle->SetOptStat(0);

	TCanvas* canv1 = new TCanvas("c1", "c1");

    TLegend *legend = new TLegend(0.6,0.7,0.9,0.9);
    //TLegend *legend = new TLegend(0.5,0.7,0.9,0.9);
    
    legend->AddEntry(histo1, "Left", "l");
    legend->AddEntry(histo2, "longlived 0.1", "l");

    histo1->SetLineColor(1);
    histo2->SetLineColor(2);

	histo1->Draw("sameh");
	histo2->Draw("sameh");

        legend->Draw();

    canv1->Update();
    //canv1->Print("/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/plots_mutau/BDTcomparisonStau100.pdf");

    canv1->Print("/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/plots_mutau/llVSleft"+var+".pdf");



}
