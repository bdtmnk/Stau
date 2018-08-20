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
void FOMtest(

//	  int nBins  =   50,//phi!!!!!
//	  float xmin =    0,
//	  float xmax =  3.14,
	  TString Input = "TMVA_Stau100LSP1_NewHope_NewSample_ANN_LessVar_MLP1",
	  float Nbackgr  =   180000,
	  float Nsignal  =   50
//	  float xmin =    -0.5,
//	  float xmax =  50.5,


//  	  bool NormalMetForData = false


          )
{
	//TString InputFile = "TMVA_"+Input+".root";
	TString InputFile = Input+".root";
	Input = Input + "";
	float testProc = 0.25;
	cout<<" "<<endl;
	cout<<" "<<endl;
	cout <<"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" <<endl;
	cout <<Input <<endl;

gStyle->SetOptStat(0);
    TFile * file = new TFile(InputFile);
    //TH1D * MVA_S = (TH1D*)file->Get("Method_BDT/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_S");
    //TH1D * MVA_B = (TH1D*)file->Get("Method_BDT/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_B");
    //TH1D * MVA_S = (TH1D*)file->Get("Method_Boost/MLP1/MLP_B0099/MVA_Train_S_0099");
    //TH1D * MVA_B = (TH1D*)file->Get("Method_Boost/MLP1/MLP_B0099/MVA_Train_B0099");

    TH1D * MVA_S = (TH1D*)file->Get("Method_MLP/MLP1/MVA_MLP1_S");
    TH1D * MVA_B = (TH1D*)file->Get("Method_MLP/MLP1/MVA_MLP1_B");
	bool deriveN = true;
	if (deriveN)
	{
        TTree * tree = (TTree*)file->Get("TestTree");
 	Float_t weight;
 	Int_t classID;
  	TBranch     *b_weight;
  	TBranch     *b_classID;
  	tree->SetBranchAddress("weight", &weight, &b_weight);
  	tree->SetBranchAddress("classID", &classID, &b_classID);
	
	Nbackgr =0;
	Nsignal = 0;
	Int_t iN = tree->GetEntriesFast();
	for ( Int_t i=0; i<iN; i++) 
		{
		tree->GetEvent(i);
		//cout <<classID <<endl;
		//cout <<weight <<endl;
		if (classID>0.5) {Nsignal += weight; /*cout<<"!!!!!!!!"<<endl;		cout <<Nsignal <<endl;*/}
		if (classID<0.5) Nbackgr+=weight;
		}
	Nsignal=Nsignal/testProc;
	Nbackgr=Nbackgr/testProc;
	cout <<"Nsignal "<<Nsignal <<endl;
	cout <<"Nbackgr "<<Nbackgr <<endl;

	}

	
/*
	cout << MVA_S->GetSumOfWeights()<<endl;
	cout << MVA_B->GetSumOfWeights()<<endl;
	cout << MVA_S->GetEntries()<<endl;
	cout << MVA_B->GetEntries()<<endl;
*/
	MVA_S->Scale(Nsignal/MVA_S->GetSumOfWeights());
	MVA_B->Scale(Nbackgr/MVA_B->GetSumOfWeights());

	TH1D * FOM = (TH1D*)MVA_S->Clone("FOM");
	TH1D * significance = (TH1D*)MVA_S->Clone("significance");
	TH1D * backgrRejection = (TH1D*)MVA_S->Clone("backgrRejection");
	TH1D * signalEfficiency = (TH1D*)MVA_S->Clone("signalEfficiency");

	FOM->Scale(0);
	significance->Scale(0);
	backgrRejection->Scale(0);
	signalEfficiency->Scale(0);

	float fFOM,fsignificance,fbackgrRejection,fsignalEfficiency;
	float sumBkg=0;
	float sumSignal=0;
	float RestSignal, RestBKG,UncBKG;

	int Nbins = MVA_S->GetNbinsX();
	cout <<Nbins <<endl;
	for (int i=0; i<(Nbins); ++i)
		{

		sumBkg += MVA_B->GetBinContent(i); 
		sumSignal += MVA_S->GetBinContent(i); 
		RestSignal = Nsignal-sumSignal;
		RestBKG = Nbackgr-sumBkg;
		UncBKG = 0.2*RestBKG;
		UncBKG = UncBKG*UncBKG;

		fsignificance = (RestSignal)/sqrt(RestSignal+RestBKG+UncBKG);
		fbackgrRejection = sumBkg/Nbackgr;
		fsignalEfficiency = RestSignal/Nsignal;
		fFOM = sqrt( 2*( (RestSignal+RestBKG)*log((RestSignal+RestBKG)*(UncBKG+RestBKG)/(RestBKG*RestBKG+(RestSignal+RestBKG)*UncBKG)) - (RestBKG*RestBKG/UncBKG)*log(1+UncBKG*RestSignal/(RestBKG*((UncBKG+RestBKG)))) ));
		if ((RestSignal+RestBKG)*log((RestSignal+RestBKG)*(UncBKG+RestBKG)/(RestBKG*RestBKG+(RestSignal+RestBKG)*UncBKG)) - (RestBKG*RestBKG/UncBKG)*log(1+UncBKG*RestSignal/(RestBKG*((UncBKG+RestBKG)))) < 0) fFOM = 0;
		if (fbackgrRejection>=1 ) fFOM=0;
		FOM->SetBinContent(i,fFOM);
		significance->SetBinContent(i,fsignificance);
		backgrRejection->SetBinContent(i,fbackgrRejection);
		signalEfficiency->SetBinContent(i,fsignalEfficiency);
		


//cout<< sumBkg << "  "<< sumSignal<< "  "<<fFOM << "  "<< fsignificance<< "  "<< fbackgrRejection<<"  "<< fsignalEfficiency<<"  "<< "  "<< "  "<< endl;
/*
cout  << sqrt( 2*((RestSignal+RestBKG)*log((RestSignal+RestBKG)*(UncBKG+RestBKG)/(RestBKG*RestBKG+(RestSignal+RestBKG)*UncBKG)) - (RestBKG*RestBKG/UncBKG)*log(1+UncBKG*RestSignal/(RestBKG*((UncBKG+RestBKG)))) ))<< endl;

cout  <<  (RestSignal+RestBKG)*log((RestSignal+RestBKG)*(UncBKG+RestBKG)/(RestBKG*RestBKG+(RestSignal+RestBKG)*UncBKG)) - (RestBKG*RestBKG/UncBKG)*log(1+UncBKG*RestSignal/(RestBKG*((UncBKG+RestBKG)))) << endl;

cout  <<  (RestBKG*RestBKG/UncBKG)*log(1+UncBKG*RestSignal/(RestBKG*((UncBKG+RestBKG)))) << endl;

cout  <<  (RestSignal+RestBKG)*log((RestSignal+RestBKG)*(UncBKG+RestBKG)/(RestBKG*RestBKG+(RestSignal+RestBKG)*UncBKG)) << endl;

cout  << log((RestSignal+RestBKG)*(UncBKG+RestBKG)/(RestBKG*RestBKG+(RestSignal+RestBKG)*UncBKG)) << endl;

cout  <<  log(1+UncBKG*RestSignal/(RestBKG*((UncBKG+RestBKG)))) << endl;
*/
		}



	TCanvas* canv1 = new TCanvas("c1", "c1");	
        FOM->SetMarkerColor(1);
        FOM->SetLineColor(1);
        FOM->SetFillColor(1);
        FOM->SetFillStyle(0);
        FOM->SetLineWidth(2);
        FOM->SetMarkerStyle(20);
        FOM->SetMarkerSize(1.1);

        significance->SetMarkerColor(2);
        significance->SetLineColor(2);
        significance->SetFillColor(2);
        significance->SetFillStyle(0);
        significance->SetLineWidth(2);
        significance->SetMarkerStyle(20);
        significance->SetMarkerSize(1.1);

        backgrRejection->SetMarkerColor(3);
        backgrRejection->SetLineColor(3);
        backgrRejection->SetFillColor(3);
        backgrRejection->SetFillStyle(0);
        backgrRejection->SetLineWidth(2);
        backgrRejection->SetMarkerStyle(20);
        backgrRejection->SetMarkerSize(1.1);

        signalEfficiency->SetMarkerColor(4);
        signalEfficiency->SetLineColor(4);
        signalEfficiency->SetFillColor(4);
        signalEfficiency->SetFillStyle(0);
        signalEfficiency->SetLineWidth(2);
        signalEfficiency->SetMarkerStyle(20);
        signalEfficiency->SetMarkerSize(1.1);

        TLegend *legend1 = new TLegend(0.1,0.7,0.48,0.9);
        legend1->SetTextFont(42);
        legend1->AddEntry(FOM, "FOM", "p");
        legend1->AddEntry(significance, "s/sqrt(s+b)", "p");
        legend1->AddEntry(backgrRejection, "backgr rejection", "l");
        legend1->AddEntry(signalEfficiency, "signal efficiency", "l");
	FOM->GetXaxis()->SetTitle("BDT Response");
	FOM->GetYaxis()->SetTitle("Events");
	FOM->GetYaxis()->SetRangeUser(0,1.5);

	FOM->Draw("psame");
	significance->Draw("psame");
	backgrRejection->Draw("csame");
	signalEfficiency->Draw("csame");
        legend1->Draw();
        canv1->Update();
        canv1->Print("Plots/Shape"+Input+"_.pdf");
	
	TCanvas* canv2 = new TCanvas("c2", "c2");//stolbikami
	canv2->SetLogy();
        MVA_B->SetLineColor(4);
        MVA_B->SetFillColor(4);
        MVA_S->SetLineColor(3);
	MVA_S->SetLineWidth(5);
	MVA_S->SetFillColorAlpha(kGreen, 0.76);
        TLegend *legend2 = new TLegend(0.6,0.7,0.9,0.9);
	legend2->SetTextFont(42);
	legend2->AddEntry(MVA_S, "MVA_S", "f");
	legend2->AddEntry(MVA_B, "MVA_B", "f");
	MVA_B->GetXaxis()->SetTitle("BDT Response");
	MVA_B->GetYaxis()->SetTitle("Events");
	MVA_B->SetMinimum(0.01);
	MVA_B->SetMaximum(100000);
	MVA_B->Draw("hist");
	MVA_S->Draw("samehist");
	legend2->Draw();
        canv2->Update();
        canv2->Print("Plots/FOM_"+Input+"_.pdf");
			
	cout <<"FOM->GetBinContent(34)  "<<FOM->GetBinContent(34) <<endl;
	cout <<"FOM->GetXaxis()->GetBinLowEdge(34)  "<<FOM->GetXaxis()->GetBinLowEdge(34) <<endl;
	cout <<"significance->GetBinContent(34)  "<<significance->GetBinContent(34) <<endl;
	cout <<"backgrRejection->GetBinContent(34)  "<<backgrRejection->GetBinContent(34) <<endl;
      	cout <<"signalEfficiency->GetBinContent(34)  "<<signalEfficiency->GetBinContent(34) <<endl;
	cout <<"Nsignal  "<<(Nsignal*signalEfficiency->GetBinContent(34)) <<endl;
	cout <<"Nbackgr  "<<(Nbackgr*(1-backgrRejection->GetBinContent(34))) <<endl;
	int iMax = significance->GetMaximumBin();
	cout << "maximum bin    " << iMax <<endl;
	cout <<"FOM->GetBinContent(iMax)  "<<FOM->GetBinContent(iMax) <<endl;
	cout <<"FOM->GetXaxis()->GetBinLowEdge(iMax)  "<<FOM->GetXaxis()->GetBinLowEdge(iMax) <<endl;
	cout <<"significance->GetBinContent(iMax)  "<<significance->GetBinContent(iMax) <<endl;
	cout <<"backgrRejection->GetBinContent(iMax)  "<<backgrRejection->GetBinContent(iMax) <<endl;
      	cout <<"signalEfficiency->GetBinContent(iMax)  "<<signalEfficiency->GetBinContent(iMax) <<endl;
	cout <<"Nsignal  "<<(Nsignal*signalEfficiency->GetBinContent(iMax)) <<endl;
	cout <<"Nbackgr  "<<(Nbackgr*(1-backgrRejection->GetBinContent(iMax))) <<endl;
		

}
