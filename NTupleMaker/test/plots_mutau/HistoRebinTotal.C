#include "HttStylesNew.cc"
#include "HtoH.h"
#include <iostream>
#include <string> 
#include <fstream> 
#include <vector> 

//Xmin - minimum Bin cintent
void HistoRebinTotal(TString FileName = "TTPowHeg",
		TString HistoName = "met_ez",
		float Xmin = 100) 
{

	
	TString	FileName2= "eltau/"+FileName+".root";
	cout << FileName2 << endl;
	
	
	TFile * File = new TFile(FileName2);
	File->cd("eltau");
	
	TTree *tree = (TTree *)File -> Get("eltau/T");			
	


	
	tree->Draw(HistoName,"","goff");
	TH1 * Histo = tree->GetHistogram();
	TCanvas * c1 = new TCanvas("c1", "c1");
	Histo -> Draw();



	//find last bin
	int Nbins = Histo->GetXaxis()->GetLast();
	int LastBin =0;
	vector<double> eventV;
	vector<float> BinBorderV;
	float SumBinContent = 0;

	BinBorderV.push_back(Histo->GetXaxis()->GetBinLowEdge(1));
	cout<< Histo->GetXaxis()->GetBinLowEdge(1)<< endl;


	for ( int iN=1; iN<=Nbins; ++iN)
		{
		if (Histo-> GetBinContent(iN)<Xmin)
			{
			if (SumBinContent<Xmin && iN<Nbins) {SumBinContent += Histo-> GetBinContent(iN);}
			else  {BinBorderV.push_back(Histo->GetXaxis()->GetBinUpEdge(iN));
				eventV.push_back(SumBinContent); 
				SumBinContent=0;}
			}

		else 
			{
			BinBorderV.push_back(Histo->GetXaxis()->GetBinUpEdge(iN));
			eventV.push_back(Histo-> GetBinContent(iN)); 
			}
		}
	
	float BinBorder[BinBorderV.size()];
	for ( int iN=0; iN<BinBorderV.size(); ++iN) {BinBorder[iN]=BinBorderV.at(iN);}
	
	//filling histo
	TH1D * HistoFinal = new TH1D(HistoName,HistoName,eventV.size() ,BinBorder);
	for ( int iN=1; iN<=eventV.size(); ++iN) {HistoFinal->SetBinContent(iN,eventV.at(iN-1));}
	
	TCanvas * c2 = new TCanvas("c2", "c2");
	HistoFinal -> Draw();

}

