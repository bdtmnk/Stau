#include "TString.h"
#include "TFile.h"
#include "TH1F.h"
#include <fstream>


int calc_mean_var_fit(){


	std::ifstream infile("thefile.txt");

	TFile *file2 =  new TFile("Var_BDTmutau_Stau100_16_35invfb_mt_SR.root");

	TH1D *hOriginal = (TH1D*)file2->Get("allbkg_BDTmutau_Stau100_16");

	std::string line;
	//std::string
	TString file_name;
	//std::string
	TString hist_name;

	while (std::getline(infile, line))
	{

		std::istringstream iss(line);
		//cout<<"Line:"<<line<<endl;
		iss >> file_name >> hist_name;	

	TFile *file =  new TFile(file_name);
	TH1D *histo = (TH1D*)file->Get(hist_name);
	int N_bins =  histo->GetNbinsX();
	float rel_dev=0;
	float mean = histo->GetMean();
	float MPE=0;
	double N_entries = histo->GetEntries();
//	for (int i=17; i<=N_bins; i++){
//		mean += histo->GetBinContent(i)/(N_bins-17);
//	}
	TH1F *h=new TH1F("h","h", N_bins,0, 1.0);
	TF1 *f = new TF1("f", "TMath::Gaus(x, 0.5, 0.5)", 0, 1.0);
	h->FillRandom("f", int(N_entries));



	
	for (int i=17; i<=N_bins; i++){

		float bin_value	= histo->GetBinContent(i);
		float normal_bin_value = hOriginal->GetBinContent(i);
		float _rel_dev = std::abs(bin_value - normal_bin_value)/normal_bin_value;
		rel_dev += _rel_dev;
	}

	MPE = rel_dev/(N_bins-17);
	cout<<"FILE: "<<file_name<<endl;
	cout<<"SYST: "<<MPE<<endl;
	}
	return 0;


}
