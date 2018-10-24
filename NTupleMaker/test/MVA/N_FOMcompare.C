#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <fstream>
#include "boost/lexical_cast.hpp"
#include "boost/algorithm/string.hpp"
#include "boost/format.hpp"
#include "boost/program_options.hpp"
#include "boost/range/algorithm.hpp"
#include "boost/range/algorithm_ext.hpp"


#include "/nfs/dust/cms/user/bobovnii/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/Plotting.h"
#include "/nfs/dust/cms/user/bobovnii/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/Plotting_Style.h"
#include "/nfs/dust/cms/user/bobovnii/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/HttStylesNew.cc"
#include "TPad.h"
#include "TROOT.h"
#include "TColor.h"
#include "TEfficiency.h"
#include "TMath.h"
#include "TF1.h"

void N_FOMcompare
(
	TString Input = "stau300_LSP1My",
	TString InputFile ="TMVA_stau-stau300_LSP1My_005.root",
//	TString InputFile ="TMVA_stau150_LSP1My.root",
	TString PlotDir="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_9_4_0_patch1/src/DesyTauAnalyses/NTupleMaker/test/MVA/recentPlots/",

	double Nbackgr = 180000,
	double Nsignal = 50
)
{
	double testProc = 0.5;


	gStyle->SetOptStat(0); 
	

        TFile *file1 = new TFile("TMVA_stau-stau300_LSP1My.root");
        TFile *file2 = new TFile("TMVA_stau-stau_left_300_LSP1_B_OS.root");


       TH1D *MVA_B1 = (TH1D*)file1->Get("dataset/Method_BDTmutau_stau-stau300_LSP1My/BDTmutau_stau-stau300_LSP1My/MVA_BDTmutau_stau-stau300_LSP1My_B");
       TH1D *MVA_S1 = (TH1D*)file1->Get("dataset/Method_BDTmutau_stau-stau300_LSP1My/BDTmutau_stau-stau300_LSP1My/MVA_BDTmutau_stau-stau300_LSP1My_S");

		TH1D *MVA_B2 = (TH1D*)file2->Get("dataset/Method_BDTmutau_stau-stau_left_300_LSP1_B_OS/BDTmutau_stau-stau_left_300_LSP1_B_OS/MVA_BDTmutau_stau-stau_left_300_LSP1_B_OS_B");
        TH1D *MVA_S2 = (TH1D*)file2->Get("dataset/Method_BDTmutau_stau-stau_left_300_LSP1_B_OS/BDTmutau_stau-stau_left_300_LSP1_B_OS/MVA_BDTmutau_stau-stau_left_300_LSP1_B_OS_S");


	TH1D * hist2 = (TH1D*)MVA_S1->Clone("hist2");
  	TH1D * hist1 = (TH1D*)MVA_S2->Clone("hist1");

	int nBins = hist1->GetNbinsX();
    TCanvas* canv1 = new TCanvas("c1", "c1");
    canv1->cd();
    std::vector<TPad*> pads = TwoPadSplit(0.29, 0.00, 0.00);
    //pads[0]->SetLogy(logY);
    
    std::vector<TH1*> h = CreateAxisHists(2, hist1, hist1->GetXaxis()->GetXmin(), hist1->GetXaxis()->GetXmax()-0.01);\
	//if (Variable.Contains("MT")) h = CreateAxisHists(2, hist1, 0, 120-0.01);
	//if(!logY && Variable.Contains("pt")) h = CreateAxisHists(2, hist1, 0, 100-0.01);
	//if(!logY && Variable.Contains("pt[0]")) h = CreateAxisHists(2, hist1, 25, 100-0.01);
	//if(!logY && Variable.Contains("Ut")) h = CreateAxisHists(2, hist1, 0, 200-0.01);
	//if(!logY && Variable.Contains("Utr")) h = CreateAxisHists(2, hist1, -100, 100-0.01);
	//if(!logY && Variable.Contains("Ucol")) h = CreateAxisHists(2, hist1, -150, 50-0.01);
    h[0]->Draw();
    
    std::string units="";
    std::string xtitle_ = "BDT";
    size_t pos = xtitle_.find("[");
    if(pos!=std::string::npos) {
        units = xtitle_.substr(pos+1, xtitle_.find("]") - pos -1 );
        xtitle_ = xtitle_.substr(0, pos);
    }
        
    pads[1]->cd();
    h[1]->Draw();    
    SetupTwoPadSplitAsRatio(pads, "official/private", true, 0.0, 2.0);
    StandardAxes(h[1]->GetXaxis(), h[0]->GetYaxis(),xtitle_ ,units);
    h[1]->GetYaxis()->SetNdivisions(4);
    h[1]->GetXaxis()->SetTitleOffset(1.2);
    h[1]->GetYaxis()->SetTitleOffset(2.0);
    pads[0]->cd();
    h[0]->GetYaxis()->SetTitleOffset(2.0);
    pads[1]->SetGrid(0,1);
    //it complains if the minimum is set to 0 and you try to set log y scale
    //if(logY) h[0]->SetMinimum(1);
    pads[0]->cd();

    hist1->Sumw2();
    hist2->Sumw2();
    
    //TH1D * hist1W= (TH1D*)file1->Get("mutau/histWeightsH");
    //TH1D * hist2W= (TH1D*)file2->Get("mutau/histWeightsH");

    
    //hist1->Scale(1/hist1W->GetSumOfWeights());
	//hist2->Scale(1/hist2W->GetSumOfWeights());
    
	hist1->Scale(1/hist1->GetSumOfWeights());
	hist2->Scale(1/hist2->GetSumOfWeights());


    canv1->Update();


	TH1D * ratioH = (TH1D*)hist1->Clone("ratioH");


    for (int iB=1; iB<=nBins; ++iB) {
        float x1 = hist1->GetBinContent(iB);
        float x2 = hist2->GetBinContent(iB);
       cout << x1<<endl;
       cout << x2<<endl;

        if (x1>0&&x2>0) {
            float e1 = hist1->GetBinError(iB);
            float ratio = x1/x2;
            float eratio = e1/x2;
            ratioH->SetBinContent(iB,ratio);
            ratioH->SetBinError(iB,eratio);
    //cout << x1<<endl;

	cout << ratio<<endl;
        }
        else {
            ratioH->SetBinContent(iB,1000);
        }
    }
 pads[1]->cd();
    //ratioErrH->GetYaxis()->SetRangeUser(0.4,1.6);
    //ratioErrH->GetXaxis()->SetRangeUser(50,120);
    //ratioErrH->Draw("e2same");
    ratioH->GetYaxis()->SetRangeUser(0.0,2.0);
    ratioH->SetMarkerSize(0.5);
    ratioH->Draw("pe0same");



    pads[0]->cd();


   TLegend *legend = PositionedLegend(0.25, 0.15, 3, 0.01);
    legend->SetTextFont(32);
    //legend-> SetNColumns(2);
    hist1->SetMarkerColor(1);
    hist1->SetLineColor(1);
    hist1->SetFillColor(1);
    hist1->SetFillStyle(0);
    hist1->SetLineWidth(2);
    hist1->SetMarkerStyle(20);
    hist1->SetMarkerSize(1.1);
    
    legend->AddEntry(hist1, "official", "ple");

    hist2->SetMarkerColor(kRed);
    hist2->SetLineColor(kRed);
    hist2->SetFillColor(1);
    hist2->SetFillStyle(0);
    hist2->SetLineWidth(2);
    hist2->SetMarkerStyle(20);
    hist2->SetMarkerSize(1.1);
    legend->AddEntry(hist2,"private", "ple");
    //hist2->SetMaximum(0.06);
    hist2->Draw();
    hist1->Draw("same");

	TFile *smFile = TFile::Open ("PUsignalReweighting.root", "recreate");
	
				smFile->cd();
				hist2->Write();		
				hist1->Write();
				smFile->Write();
				smFile->Close();
				delete smFile;

    legend->Draw();

    canv1->Print("/nfs/dust/cms/user/bobovnii//test.pdf");

       
       //TH1D *MVA_B = (TH1D*)file->Get("dataset/Method_BDTmutau/BDTmutau/MVA_BDTmutau_B");
       //TH1D *MVA_S = (TH1D*)file->Get("dataset/Method_BDTmutau/BDTmutau/MVA_BDTmutau_S"); 
       
	//TH1D *MVA_B = (TH1D*)file->Get("dataset/Method_BDTmutau/BDTmutau/MVA_BDTmutau_B");
	//TH1D *MVA_S = (TH1D*)file->Get("dataset/Method_BDTmutau/BDTmutau/MVA_BDTmutau_S");
      // 	TH1D *MVA_B = (TH1D*)file->Get("Method_BDT/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_B");
      // 	TH1D *MVA_S = (TH1D*)file->Get("Method_BDT/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_S");
    
}
