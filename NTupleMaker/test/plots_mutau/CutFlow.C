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

void CutFlow()
{
	
	TFile * file1 = new TFile("Stau100_LSP1_left_Nominal_B.root");
	TFile * file2 = new TFile("Stau125_LSP1_left_Nominal_B.root");
	TFile * file3 = new TFile("Stau200_LSP1_left_Nominal_B.root");

	TH1D * histo1 = (TH1D*)file1->Get("mutau/CutFlowUnW");
		TH1D * histo2 = (TH1D*)file2->Get("mutau/CutFlowUnW");
	TH1D * histo3 = (TH1D*)file3->Get("mutau/CutFlowUnW");

	TH1D * Weights1 = (TH1D*)file1->Get("mutau/histWeightsH");
		TH1D * Weights2 = (TH1D*)file2->Get("mutau/histWeightsH");
	TH1D * Weights3 = (TH1D*)file3->Get("mutau/histWeightsH");
	
	TH1D * BDT1 = (TH1D*)file1->Get("mutau/BDTmutau_Stau100_16");
	TH1D * BDT2 = (TH1D*)file2->Get("mutau/BDTmutau_Stau100_16");
	TH1D * BDT3 = (TH1D*)file3->Get("mutau/BDTmutau_Stau200_16");


	float xsec1 = 0.27079 * 5;
	float lumi = 35864;
	float xsec2 = 0.13164;
	float xsec3 = 0.02181*5;	
	
	/*
	for (int j=1;j<20;j++) 
	{
	cout << histo1->GetBinContent(j) *(xsec1*lumi)/Weights->GetSumOfWeights() << endl;

	} 
	*/
	
		cout << "\\begin{table}[htbp] "<<endl;
		//cout << "\\centering "<<endl;
	cout << "\\begin{center} "<<endl;
		//cout << "\\begin{tiny} "<<endl;
		//cout << "\\vspace*{-3.5cm}\\Rotatebox{90}{"<<endl;
		cout << "\\begin{tabular}{|l|l|l|l|}"<<endl;
		cout << "\\hline"<<endl;

cout << "Selection"<< 
	" & " <<setprecision(1)<< fixed<<setprecision(1)<< fixed<< " Stau(100,1)"  << 
	" & " <<setprecision(1)<< fixed<<" Stau(125,1)" << 
	" & " <<setprecision(1)<< fixed<< " Stau(200,1)"  << 
	"\\\\" <<
	endl;
	
	cout << "\\sigma Br$(\\mu \\tau_h)$"<< 
	" & " <<setprecision(1)<< fixed<<setprecision(1)<< fixed<< xsec1*lumi*0.23/5  << 
	" & " <<setprecision(1)<< fixed<<xsec2*lumi*0.23 << 
	" & " <<setprecision(1)<< fixed<< xsec3*lumi*0.23/5  << 
	"\\\\" <<
	endl;

	cout << "oppositely charged $\\mu \\tau_h$"<< 
	" & " <<setprecision(1)<< fixed<<setprecision(1)<< fixed<< histo1->GetBinContent(2) *(xsec1*lumi)/Weights1->GetSumOfWeights()  << 
	" & " <<setprecision(1)<< fixed<<histo2->GetBinContent(2) *(xsec2*lumi)/Weights2->GetSumOfWeights() << 
	" & " <<setprecision(1)<< fixed<< histo3->GetBinContent(2) *(xsec3*lumi)/Weights3->GetSumOfWeights()  << 
	"\\\\" <<
	endl;
	
	cout << "lepton veto"<< 
	" & " <<setprecision(1)<< fixed<<setprecision(1)<< fixed<< histo1->GetBinContent(5) *(xsec1*lumi)/Weights1->GetSumOfWeights()  << 
	" & " <<setprecision(1)<< fixed<<histo2->GetBinContent(5) *(xsec2*lumi)/Weights2->GetSumOfWeights() << 
	" & " <<setprecision(1)<< fixed<< histo3->GetBinContent(5) *(xsec3*lumi)/Weights3->GetSumOfWeights()  << 
	"\\\\" <<
	endl;
	
	cout << "SF and corrections"<< 
	" & " <<setprecision(1)<< fixed<<setprecision(1)<< fixed<< histo1->GetBinContent(13) *(xsec1*lumi)/Weights1->GetSumOfWeights()  << 
	" & " <<setprecision(1)<< fixed<<histo2->GetBinContent(13) *(xsec2*lumi)/Weights2->GetSumOfWeights() << 
	" & " <<setprecision(1)<< fixed<< histo3->GetBinContent(13) *(xsec3*lumi)/Weights3->GetSumOfWeights()  << 
	"\\\\" <<
	endl;
	
	cout << "$N_{jets} < 2$ and Dilepton mass $> 50 GeV$"<< 
	" & " <<setprecision(1)<< fixed<<setprecision(1)<< fixed<< histo1->GetBinContent(14) *(xsec1*lumi)/Weights1->GetSumOfWeights()  << 
	" & " <<setprecision(1)<< fixed<<histo2->GetBinContent(14) *(xsec2*lumi)/Weights2->GetSumOfWeights() << 
	" & " <<setprecision(1)<< fixed<< histo3->GetBinContent(14) *(xsec3*lumi)/Weights3->GetSumOfWeights()  << 
	"\\\\" <<
	endl;
	
	cout <<"$N_{bjets} = 0$"<< 
	" & " <<setprecision(1)<< fixed<<setprecision(1)<< fixed<< histo1->GetBinContent(15) *(xsec1*lumi)/Weights1->GetSumOfWeights()  << 
	" & " <<setprecision(1)<< fixed<<histo2->GetBinContent(15) *(xsec2*lumi)/Weights2->GetSumOfWeights() << 
	" & " <<setprecision(1)<< fixed<< histo3->GetBinContent(15) *(xsec3*lumi)/Weights3->GetSumOfWeights()  << 
	"\\\\" <<
	endl;
	
	cout <<"$20 GeV < M_T < 60 GeV$ and $M_T > 120 GeV$"<< 
	" & " <<setprecision(1)<< fixed<<setprecision(1)<< fixed<< histo1->GetBinContent(16) *(xsec1*lumi)/Weights1->GetSumOfWeights()  << 
	" & " <<setprecision(1)<< fixed<<histo2->GetBinContent(16) *(xsec2*lumi)/Weights2->GetSumOfWeights() << 
	" & " <<setprecision(1)<< fixed<< histo3->GetBinContent(16) *(xsec3*lumi)/Weights3->GetSumOfWeights()  << 
	"\\\\" <<
	endl;
	
	cout << "$N_{jets} < 1$, $\\Delta R > 2.$ and $\\Delta \\phi > 1.5$"<< 
	" & " <<setprecision(1)<< fixed<<setprecision(1)<< fixed<< histo1->GetBinContent(17) *(xsec1*lumi)/Weights1->GetSumOfWeights()  << 
	" & " <<setprecision(1)<< fixed<<histo2->GetBinContent(17) *(xsec2*lumi)/Weights2->GetSumOfWeights() << 
	" & " <<setprecision(1)<< fixed<< histo3->GetBinContent(17) *(xsec3*lumi)/Weights3->GetSumOfWeights()  << 
	"\\\\" <<
	endl;
	
	cout << "The most sensitive BDT bin"<< 
	" & " <<setprecision(1)<< fixed<<setprecision(1)<< fixed<< BDT1->GetBinContent(27) *(xsec1*lumi)/Weights1->GetSumOfWeights()  << 
	" & " <<setprecision(1)<< fixed<<BDT2->GetBinContent(27) *(xsec2*lumi)/Weights2->GetSumOfWeights() << 
	" & " <<setprecision(1)<< fixed<< BDT3->GetBinContent(36) *(xsec3*lumi)/Weights3->GetSumOfWeights()  << 
	"\\\\" <<
	endl;
	
	    cout << "\\hline  "<<endl;
cout << "\\end{tabular} "<<endl;
cout << "\\caption{ Cutflow table for the left handed stau direct production signal model with LSP mass of 1 GeV and stau masses of 100, 125 and 200 GeV in $\\mu\\tau_h$ channel.  Numbers are normalized to an integrated luminosity of 35.9 $fb^{−1}$}"<<endl;
cout << "\\label{cutflow} "<<endl;
	cout << "\\end{center} "<<endl;

cout << "\\end{table} "<<endl;
}
