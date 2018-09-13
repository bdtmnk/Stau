//#include "HttStylesNew.cc"
//#include "HtoH.h"
#include <iostream>
#include <string> 
#include <fstream> 
#include <vector> 

//Xmin - minimum Bin cintent
void HistoRebinLastBin(TString FileName = "TTPowHeg_B",
		TString HistoName = "met_pt",
		float Xmin = 100) 
{

	
	TString	FileName2= FileName+".root";
	cout << FileName2 << endl;
	
	
	TFile * File = new TFile(FileName2);
	File->cd("mutau");
	
	TTree *tree = (TTree *)File -> Get("mutau/T");			
	

	
	tree->Draw("met_pt","","goff");
	TH1 * Histo = tree->GetHistogram();
	TCanvas * c1 = new TCanvas("c1", "c1");
	Histo -> Draw();



	//find last bin
	int Nbins = Histo->GetXaxis()->GetLast();
	int LastBin =0;
	float LasrBinContent = 0;
	bool NextToLast = false;
	for ( int iN=1; iN<=Nbins; ++iN)
		{
		if (Histo-> GetBinContent(iN)>Xmin && NextToLast ==false)
			{LastBin = iN;
			LasrBinContent = Histo-> GetBinContent(iN);}
		else {NextToLast = true;}
		}


	// find bins dorders
	cout<<   "LastBin"<< LastBin     <<endl;
	NextToLast = false;
	float BinBorder[LastBin+1];	
	for ( int iN=1; iN<=Nbins; ++iN)
		{cout <<iN   << endl;
		if (Histo-> GetBinContent(iN)>Xmin && NextToLast ==false) 
			{BinBorder[iN-1]= Histo->GetXaxis()->GetBinLowEdge(iN);cout <<BinBorder[iN-1]  << endl;}
		else {LasrBinContent += Histo-> GetBinContent(iN); NextToLast = true;}
		}

	BinBorder[LastBin] = BinBorder[Nbins]= Histo->GetXaxis()->GetBinUpEdge(Nbins);
	cout <<BinBorder[LastBin]  << endl;
	

	//filling histo
	TH1D * HistoFinal = new TH1D(HistoName,HistoName, LastBin,BinBorder);
	for ( int iN=1; iN<LastBin; ++iN)
		{
		HistoFinal->SetBinContent(iN,Histo-> GetBinContent(iN));
		}

	HistoFinal->SetBinContent(LastBin,LasrBinContent);
	TCanvas * c2 = new TCanvas("c2", "c2");
	HistoFinal -> Draw();

}


