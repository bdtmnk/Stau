#include <iostream>
#include <vector>
#include <map>
#include "boost/lexical_cast.hpp"
#include "boost/algorithm/string.hpp"
#include "boost/format.hpp"
#include "boost/program_options.hpp"
#include "boost/range/algorithm.hpp"
#include "boost/range/algorithm_ext.hpp"
#include "TPad.h"
#include "TROOT.h"
#include "TColor.h"
#include "TEfficiency.h"
#include "TMath.h"
//WithoutNPV/

/*
Float_t myFunc(vector <float> events, float x) 
	{
	float y=0;
	for (i=0;i<events.size();i++) (y=y+TMath::Gaus(x,0,sigma,kTRUE))
	return x+sin(x); 
	
	}
*/
void testEventSmearing()

{


	float xmin=-5;
	float xmax=20;
	int Nevent=1000;
	int Nbins=100;
	float Event=0;
	TString func = "0";
	//TF1 *f1 = new TF1("f1","abs(sin(x)/x)*sqrt(x)",xmin,xmax);
	TF1 *f1 = new TF1("f1","TMath::Landau(x,0.2,1.3,0)",xmin,xmax);
	TH1F *h1 = new TH1F("h1", "h1 title", Nbins, xmin, xmax); 	
	TH1F *hNEW = new TH1F("hNEW", "hNEW title", Nbins, xmin, xmax); 
	float Chi1=0;
	float ChiNew=0;

	vector <float> events;
	vector <float> eventsNEW;

	for (i=0;i<Nevent;i++) 
	{	
		Event = f1->GetRandom();
		events.push_back(Event);
		h1->Fill(Event);
		func=func+Form("+TMath::Gaus(x,%f,%f,kTRUE)",Event,(xmax-xmin)/ /*TMath::Sqrt*/(Nevent));
	}
	TF1 *fNEW = new TF1("fNEW",func,xmin,xmax);

	for (i=0;i<(100000*Nevent);i++) 
	{	
		Event = fNEW->GetRandom();
		hNEW->Fill(Event);
	}

	f1->SetNormalized(true);
	h1->Scale(1/(h1->GetSumOfWeights()*((xmax-xmin)/Nbins)));
	hNEW->Scale(1/(hNEW->GetSumOfWeights()*((xmax-xmin)/Nbins)));

	for (i=1;i<(Nbins+1);i++) 
	{	
		Chi1= Chi1+(h1->GetBinContent(i)-f1->Eval(h1->GetBinCenter(i)))*(h1->GetBinContent(i)-f1->Eval(h1->GetBinCenter(i)))/(f1->Eval(h1->GetBinCenter(i))+0.000000001);
		ChiNew= ChiNew+(hNEW->GetBinContent(i)-f1->Eval(hNEW->GetBinCenter(i)))*(hNEW->GetBinContent(i)-f1->Eval(hNEW->GetBinCenter(i)))/(f1->Eval(hNEW->GetBinCenter(i))+0.000000001);
/*
	cout << "Chi1=  "<<Chi1 << endl;
	cout << "ChiNew=  "<<ChiNew << endl;
	cout << h1->GetBinContent(i)<< endl;
	cout << hNEW->GetBinContent(i)<< endl;
	cout << f1->Eval(hNEW->GetBinCenter(i))<< endl;*/
	}

	TCanvas* canv1 = new TCanvas("c1", "c1");
	f1->Draw();
	h1->Draw("same");
	hNEW->SetLineColor(1);
	hNEW->Draw("same");
	canv1->Print("/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/test/MVA/EventSmearing.pdf");
	canv1->Print("/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/test/MVA/EventSmearing.png");
	//cout << func << endl;
	cout << "Chi1=  "<<Chi1 << endl;
	cout << "ChiNew=  "<<ChiNew << endl;



}
