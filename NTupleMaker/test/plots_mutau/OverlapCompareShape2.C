#include <sstream>
#include <iomanip>
#include "TChain.h"
#include "TH1.h"
#include "TTree.h"
#include "TKey.h"
#include "Riostream.h"
#include "TCanvas.h"
#include "TFile.h"
#include <string>
#include "TLegend.h"
#include "TROOT.h"
#include "TFrame.h"
#include "TGaxis.h"
#include "TStyle.h"
#include <vector>
#include <iostream>
#include <algorithm>
#include "TList.h"
#include <string>
#include "TObject.h"
#include "TBranch.h"
#include <functional>
#include "TAxis.h"
#include "TChain.h"
#include "TMath.h"
#include "TPie.h"
#include "Riostream.h"
#include <iostream>
#include <fstream>


using namespace std;



void OverlapCompareShape2()
{
	TString Channel = "mutau";
	TString MC = ""; 
   // TFile * file1 = new TFile(MC+"ToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_B.root");
   // TFile * file2 = new TFile(MC+"ToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_A.root");

    TFile * fileB4 = new TFile("W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_B.root");
    TFile * fileB3 = new TFile("W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_B.root");
    TFile * fileB2 = new TFile("W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_B.root");
    TFile * fileB1 = new TFile("W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_B.root");
    TFile * fileB = new TFile("WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_B.root");

    TFile * fileDataDriven = new TFile("WJets_B_OS_Nominal_B.root");



	gStyle->SetOptStat(0);
    TObject *obj;
    TKey *key;
    fileB->cd(Channel);
    TDirectory *current_sourcedir = gDirectory;
    TIter next( current_sourcedir->GetListOfKeys());
  	 while ((key = (TKey *) next())) {

		obj = key->ReadObj ();
		string nn = obj->GetName();
		//cout <<"nn  "<<nn << endl;
		TString name = nn;
		bool flcont = true;
		if (string::npos == nn.find("_15")) flcont=false;
		if (string::npos != nn.find("DeltaMET")) flcont=false;
		if (string::npos != nn.find("BDTperBin")) flcont=false;
		//if (string::npos == nn.find("METFB_15")) flcont=false;
		if (!flcont) continue;
		cout <<"nn  "<<nn << endl;
		if (obj->IsA ()->InheritsFrom ("TTree") ) continue;
		if (obj->IsA ()->InheritsFrom ("TH2") ) continue;
		if (obj->IsA ()->InheritsFrom ("TH3") ) continue;
		if (obj->IsA ()->InheritsFrom ("TH1D") ) 
			{
			TCanvas* canv1 = new TCanvas("c1", "c1");
			TH1D* hB = (TH1D*) obj;
			if (hB->GetSumOfWeights()<1) continue;


			TH1D* wB1 = (TH1D*)fileB1->Get(Channel+"/histWeightsH");
			TH1D* wB2 = (TH1D*)fileB2->Get(Channel+"/histWeightsH");
			TH1D* wB3= (TH1D*)fileB3->Get(Channel+"/histWeightsH");
			TH1D* wB4 = (TH1D*)fileB4->Get(Channel+"/histWeightsH");
			TH1D* wB = (TH1D*)fileB->Get(Channel+"/histWeightsH");

			TH1D* hB1 = (TH1D*)fileB1->Get(Channel+"/"+name);
			TH1D* hB2 = (TH1D*)fileB2->Get(Channel+"/"+name);
			TH1D* hB3= (TH1D*)fileB3->Get(Channel+"/"+name);
			TH1D* hB4 = (TH1D*)fileB4->Get(Channel+"/"+name);

    			TH1D* hDataDriven =  (TH1D*)fileDataDriven->Get(Channel+"/"+name);

			float Lumi=1.;
			Lumi = 35864.;

			float normB1 = (1.221 *9644.5)*Lumi/wB1->GetSumOfWeights();
			float normB2 = (1.221 *3144.5)*Lumi/wB2->GetSumOfWeights();
			float normB3 = (1.221 *954.8)*Lumi/wB3->GetSumOfWeights();
			float normB4 = (1.221 *485.6)*Lumi/wB4->GetSumOfWeights();
			float normB = (61526.7)*Lumi/wB->GetSumOfWeights();

			hB->Sumw2();
			hB->Scale(1/normB);

			hB->Add(hB1,normB1);
			hB->Add(hB2,normB2);
			hB->Add(hB3,normB3);
			hB->Add(hB4,normB4);

    hDataDriven->SetMarkerColor(2);
    hDataDriven->SetLineColor(2);
    hDataDriven->SetFillColor(1);
    hDataDriven->SetFillStyle(0);
    hDataDriven->SetLineWidth(2);
    hDataDriven->SetLineStyle(1);
    hDataDriven->SetMarkerStyle(2);
    hDataDriven->SetMarkerSize(1.1);


			//hB->Scale(1/hB->GetSumOfWeights());
			//hDataDriven->Scale(1/hDataDriven->GetSumOfWeights());
			TLegend *legend = new TLegend(0.5,0.7,0.9,0.9);
    			//hDataDriven->SetLineColor(1);
    			hB->SetLineColor(1);
			legend->AddEntry(hDataDriven, "DataDriven", "ple");
    			legend->AddEntry(hB, "MC", "l");

		cout <<"nn  hB "<<hB->GetSumOfWeights() << endl;
		cout <<"nn  hDataDriven  "<<hDataDriven->GetSumOfWeights() << endl;
			//hB->Scale(1/hB->GetSumOfWeights());
			canv1->SetLogy();
			hB->SetMinimum(1);
			hB->Draw("sameh");
			hDataDriven->Draw("pesame");
       			 legend->Draw();
  		 	 canv1->Update();
   			canv1->Print("/nfs/dust/cms/user/bobovnii/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/plots_mutau/WJetsDataDriven/"+MC+name+".pdf");

			

			}
 		}
}
