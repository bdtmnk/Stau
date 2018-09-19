#include <cmath>
#include <sstream>
#include <iomanip>
#include "TChain.h"
#include "TH1.h"
#include "TH2.h"
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
#include "TColor.h"
#include "TPie.h"
#include "Riostream.h"
#include <iostream>
#include <fstream>
#include "THStack.h"
#include <sstream>
using namespace std;
void comp(){



	TString NominalFile="Templ_met_MT2lester_DZeta01J1D_17_35invfb_mt_C1N2_SR_CR1";

	TFile *nom = TFile::Open (NominalFile+".root", "read");

	vector <string> syst;
	syst.push_back("MET");
	

	for (int st=0;st<syst.size();st++){

	TString UpFile="Templ_met_MT2lester_DZeta01J1D_17_35invfb_mt_C1N2_SR_CR1_"+syst.at(st)+"Up.root";
	TString DownFile="Templ_met_MT2lester_DZeta01J1D_17_35invfb_mt_C1N2_SR_CR1_"+syst.at(st)+"Down.root";

	TFile *Up = TFile::Open (UpFile, "read");
	TFile *Down = TFile::Open (DownFile, "read");


	vector <string> samples;
	samples.push_back("tt");
	samples.push_back("wj");
	samples.push_back("dyj");
	samples.push_back("ztt");
	samples.push_back("ttx");
	samples.push_back("dib");
	samples.push_back("ww");
	samples.push_back("sT");

	ifstream ifs("C1N2");
	string line;
	while(std::getline(ifs, line)) // read one line from ifs
	{
		istringstream iss(line); // access line as a stream
		string dataname;
		iss >> dataname;


	samples.push_back(dataname+"_B");

	}
//	samples.push_back("C1N2_400_LSP1_B");
//	samples.push_back("C1N2_500_LSP300_B");

	for (int n=0;n<samples.size();n++){
		char hist[200];
		char histUp[200];
		char histDown[200];
		sprintf(hist,"%s_met_MT2lester_DZeta01J1D_17",samples[n].c_str());
		sprintf(histUp,"%s_met_MT2lester_DZeta01J1D_17_%sUp",samples[n].c_str(),syst[st].c_str());
		sprintf(histDown,"%s_met_MT2lester_DZeta01J1D_17_%sDown",samples[n].c_str(),syst[st].c_str());

        TH1D* hNom = (TH1D*)nom->Get(hist);
        TH1D* hUp = (TH1D*)Up->Get(histUp);
        TH1D* hDown = (TH1D*)Down->Get(histDown);
//        TH1D* hUp = (TH1D*)nom->Get(samples.at(n)+"_met_MT2lester_DZeta01J1D_17"+syst);
  //      TH1D* hDown = (TH1D*)nom->Get(samples.at(n)+"_met_MT2lester_DZeta01J1D_17"+syst);

	float nomSoW = hNom->GetSumOfWeights();
	float UpSoW = hUp->GetSumOfWeights();
	float DownSoW = hDown->GetSumOfWeights();
	float maxim = max(fabs(nomSoW-UpSoW), fabs(nomSoW-DownSoW));
	cout<<" for process  "<<samples[n].c_str()<<" Nominal  "<<hNom->GetSumOfWeights()<<" Up "<<hUp->GetSumOfWeights()<<" Down "<<hDown->GetSumOfWeights()<<" max "<<maxim/nomSoW<<endl;

	}
	}

}
