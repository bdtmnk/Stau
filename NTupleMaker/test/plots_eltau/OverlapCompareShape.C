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



void OverlapCompareShape()
{
	TString Channel = "mutau";
	TString MC = "all"; 
   // TFile * file1 = new TFile(MC+"ToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_B.root");
   // TFile * file2 = new TFile(MC+"ToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_A.root");

    TFile * fileB4 = new TFile("backNewWJetsMethod/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_C.root");
    TFile * fileA4 = new TFile("backNewWJetsMethod/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_D.root");
    TFile * fileB3 = new TFile("backNewWJetsMethod/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_C.root");
    TFile * fileA3 = new TFile("backNewWJetsMethod/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_D.root");
    TFile * fileB2 = new TFile("backNewWJetsMethod/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_C.root");
    TFile * fileA2 = new TFile("backNewWJetsMethod/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_D.root");
    TFile * fileB1 = new TFile("backNewWJetsMethod/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_C.root");
    TFile * fileA1 = new TFile("backNewWJetsMethod/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_D.root");
    TFile * fileB = new TFile("backNewWJetsMethod/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_C.root");
    TFile * fileA = new TFile("backNewWJetsMethod/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_B_OS_Nominal_D.root");



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


			TH1D* wA = (TH1D*)fileA->Get(Channel+"/histWeightsH");
			TH1D* wA1 = (TH1D*)fileA1->Get(Channel+"/histWeightsH");
			TH1D* wA2 = (TH1D*)fileA2->Get(Channel+"/histWeightsH");
			TH1D* wA3 = (TH1D*)fileA3->Get(Channel+"/histWeightsH");
			TH1D* wA4 = (TH1D*)fileA4->Get(Channel+"/histWeightsH");
			TH1D* wB1 = (TH1D*)fileB1->Get(Channel+"/histWeightsH");
			TH1D* wB2 = (TH1D*)fileB2->Get(Channel+"/histWeightsH");
			TH1D* wB3= (TH1D*)fileB3->Get(Channel+"/histWeightsH");
			TH1D* wB4 = (TH1D*)fileB4->Get(Channel+"/histWeightsH");
			TH1D* wB = (TH1D*)fileB->Get(Channel+"/histWeightsH");

			TH1D* hA = (TH1D*)fileA->Get(Channel+"/"+name);
			TH1D* hA1 = (TH1D*)fileA1->Get(Channel+"/"+name);
			TH1D* hA2 = (TH1D*)fileA2->Get(Channel+"/"+name);
			TH1D* hA3 = (TH1D*)fileA3->Get(Channel+"/"+name);
			TH1D* hA4 = (TH1D*)fileA4->Get(Channel+"/"+name);
			TH1D* hB1 = (TH1D*)fileB1->Get(Channel+"/"+name);
			TH1D* hB2 = (TH1D*)fileB2->Get(Channel+"/"+name);
			TH1D* hB3= (TH1D*)fileB3->Get(Channel+"/"+name);
			TH1D* hB4 = (TH1D*)fileB4->Get(Channel+"/"+name);


			float Lumi=1.;
			Lumi = 35864.;

			float normB1 = (1.221 *9644.5)*Lumi/wB1->GetSumOfWeights();
			float normB2 = (1.221 *3144.5)*Lumi/wB2->GetSumOfWeights();
			float normB3 = (1.221 *954.8)*Lumi/wB3->GetSumOfWeights();
			float normB4 = (1.221 *485.6)*Lumi/wB4->GetSumOfWeights();
			float normB = (61526.7)*Lumi/wB->GetSumOfWeights();
			float normA1 = (1.221 *9644.5)*Lumi/wA1->GetSumOfWeights();
			float normA2 = (1.221 *3144.5)*Lumi/wA2->GetSumOfWeights();
			float normA3 = (1.221 *954.8)*Lumi/wA3->GetSumOfWeights();
			float normA4 = (1.221 *485.6)*Lumi/wA4->GetSumOfWeights();
			float normA = (61526.7)*Lumi/wA->GetSumOfWeights();

			hA->Sumw2();
			hB->Sumw2();
			hA->Scale(1/normA);
			hB->Scale(1/normB);

			hA->Add(hA1,normA1);
			hA->Add(hA2,normA2);
			hA->Add(hA3,normA3);
			hA->Add(hA4,normA4);
			hB->Add(hB1,normB1);
			hB->Add(hB2,normB2);
			hB->Add(hB3,normB3);
			hB->Add(hB4,normB4);


			TLegend *legend = new TLegend(0.5,0.7,0.9,0.9);
    			hA->SetLineColor(1);
    			hB->SetLineColor(2);
			legend->AddEntry(hA, "RegionA", "l");
    			legend->AddEntry(hB, "RegionB", "l");

		cout <<"nn  "<<hB->GetSumOfWeights() << endl;
		cout <<"nn  "<<hA->GetSumOfWeights() << endl;
			hB->Scale(1/hB->GetSumOfWeights());
			hA->Scale(1/hA->GetSumOfWeights());

			hB->Draw("sameh");
			hA->Draw("sameh");
       			 legend->Draw();
  		 	 canv1->Update();
   			canv1->Print("/nfs/dust/cms/user/bobovnii/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/plots_mutau/ShapeCompare/"+MC+name+".pdf");

			

			}
 		}
}
