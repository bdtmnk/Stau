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

#include "TPad.h"
#include "TROOT.h"
#include "TColor.h"
#include "TEfficiency.h"
#include "TMath.h"
#include "TF1.h"

void N_FOM
(
	TString Input = "stau100_LSP1My",
	TString InputFile ="TMVA_stau-stau100_LSP1My_005.root",
//	TString InputFile ="TMVA_stau150_LSP1My.root",
	TString PlotDir="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_9_4_0_patch1/src/DesyTauAnalyses/NTupleMaker/test/MVA/recentPlots/",

	double Nbackgr = 180000,
	double Nsignal = 50
)
{
	double testProc = 0.3;
	cout << "  aaaa????" << endl;
	cout << Input <<"  aaaa????" << endl;

	gStyle->SetOptStat(0); 
	

        TFile *file = new TFile(InputFile);
              cout <<"dataset/Method_BDTmutau_"+Input+"/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_S_high" <<endl;

        //TH1D *MVA_B = (TH1D*)file->Get("dataset/Method_BDTmutau_stau-"+Input+"/BDTmutau_stau-"+Input+"/MVA_BDTmutau_stau-"+Input+"_B");
        //TH1D *MVA_S = (TH1D*)file->Get("dataset/Method_BDTmutau_stau-"+Input+"/BDTmutau_stau-"+Input+"/MVA_BDTmutau_stau-"+Input+"_S");
       /*TH1D *MVA_Train_B = (TH1D*)file->Get("dataset/Method_BDTmutau_"+Input+"/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_Train_B");
       TH1D *MVA_Train_S = (TH1D*)file->Get("dataset/Method_BDTmutau_"+Input+"/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_Train_S");
       TH1D *MVA_B = (TH1D*)file->Get("dataset/Method_BDTmutau_"+Input+"/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_B");
       TH1D *MVA_S = (TH1D*)file->Get("dataset/Method_BDTmutau_"+Input+"/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_S");
*/

TH1D *MVA_Train_B = (TH1D*)file->Get("dataset/Method_BDTmutau_"+Input+"/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_Train_B");
       TH1D *MVA_Train_S = (TH1D*)file->Get("dataset/Method_BDTmutau_"+Input+"/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_Train_S");
       TH1D *MVA_B = (TH1D*)file->Get("dataset/Method_BDTmutau_"+Input+"/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_B_high");
       TH1D *MVA_S = (TH1D*)file->Get("dataset/Method_BDTmutau_"+Input+"/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_S_high");



       //TH1D *MVA_B = (TH1D*)file->Get("dataset/Method_BDTmutau_"+Input+"/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_B");
       //TH1D *MVA_S = (TH1D*)file->Get("dataset/Method_BDTmutau_"+Input+"/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_S");       
       //TH1D *MVA_B = (TH1D*)file->Get("dataset/Method_BDTmutau/BDTmutau/MVA_BDTmutau_B");
       //TH1D *MVA_S = (TH1D*)file->Get("dataset/Method_BDTmutau/BDTmutau/MVA_BDTmutau_S"); 
       
	//TH1D *MVA_B = (TH1D*)file->Get("dataset/Method_BDTmutau/BDTmutau/MVA_BDTmutau_B");
	//TH1D *MVA_S = (TH1D*)file->Get("dataset/Method_BDTmutau/BDTmutau/MVA_BDTmutau_S");
      // 	TH1D *MVA_B = (TH1D*)file->Get("Method_BDT/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_B");
      // 	TH1D *MVA_S = (TH1D*)file->Get("Method_BDT/BDTmutau_"+Input+"/MVA_BDTmutau_"+Input+"_S");
      cout <<"!!!!!" <<endl;
	TH1D *MVA_B_NoScale = (TH1D*)MVA_B->Clone("MVA_B_NoScale");
	TH1D *MVA_S_NoScale = (TH1D*)MVA_S->Clone("MVA_S_NoScale");
	      cout <<"!!!!!" <<endl;
/*
// overtraining
	TCanvas* canv3 = new TCanvas("ca3", "ca3");//stolbikami
        MVA_B->SetLineColor(4);
        MVA_S->SetLineColor(3);
        MVA_Train_B->SetLineColor(kRed);
        MVA_Train_S->SetLineColor(kBlack);
        
        MVA_Train_B->SetLineWidth(2);
        MVA_Train_B->SetMarkerStyle(20);
        MVA_Train_B->SetMarkerColor(kRed);

        MVA_Train_S->SetMarkerColor(kBlack);
        MVA_Train_S->SetLineWidth(2);
        MVA_Train_S->SetMarkerStyle(20);
        TLegend *legend3 = new TLegend(0.6,0.7,0.9,0.9);
	legend3->SetTextFont(42);
	legend3->AddEntry(MVA_S, "MVA_Test_S", "f");
	legend3->AddEntry(MVA_B, "MVA_Test_B", "f");
	legend3->AddEntry(MVA_Train_S, "MVA_Train_S", "p");
	legend3->AddEntry(MVA_Train_B, "MVA_Train_B", "p");
    legend3->AddEntry((TObject*)0, Form("Mean Train_S = %.3f", MVA_Train_S->GetMean()), "" );
    legend3->AddEntry((TObject*)0, Form("Mean Test_S = %.3f", MVA_S->GetMean()), "" );
    legend3->AddEntry((TObject*)0, Form("chi2 test = %.3f", MVA_S->Chi2Test(MVA_Train_S,"WW")), "" );	
    
    
    
	MVA_B->GetXaxis()->SetTitle("BDT Response");
	MVA_B->GetYaxis()->SetTitle("Events");
	MVA_B->SetMinimum(0.0);
	//MVA_B->SetMaximum(100000);
	MVA_B->Draw("hist");
	MVA_S->Draw("samehist");
	MVA_Train_B->Draw("psame");
	MVA_Train_S->Draw("psame");
	
	legend3->Draw();
        canv3->Update();
        //canv2->Print(PlotDir+"N_MVA_SB_"+Input+"_mutau.pdf");
                canv3->Print(PlotDir+"N_Overtrain_SB_"+InputFile+"_mutau.pdf");*/

//MVA_Train_B->Sumw2();
//MVA_B->Sumw2();
//MVA_Train_S->Sumw2();
//MVA_S->Sumw2();

//MVA_B->Add(MVA_Train_B, 2.33);
//MVA_S->Add(MVA_Train_S, 3);


        if (1==1)
        {
                TTree *tree = (TTree*)file->Get("dataset/TestTree");
//		TTree *tree = (TTree*)file->Get("TestTree"); 
		Float_t weight;
 	        Int_t classID;
  	        TBranch     *b_weight;
  	        TBranch     *b_classID;
  	        tree->SetBranchAddress("weight", &weight, &b_weight);
  	        tree->SetBranchAddress("classID", &classID, &b_classID);
	
	        Nbackgr = 0;
        	Nsignal = 0;
	        Int_t iN = tree->GetEntriesFast();
	        for (Int_t i=0; i<iN; i++) 
		{
		        tree->GetEvent(i);
		        
		        if (classID>0.5) Nsignal += weight; 
		        if (classID<0.5) Nbackgr += weight; 
		}
cout<<"com1"<<endl;
	        Nsignal = Nsignal/0.2;
	        Nbackgr = Nbackgr/0.7;
	        //Nsignal = 42.69;
	        //Nbackgr = 124899;
	        cout <<"Nsignal "<<Nsignal <<endl;
	        cout <<"Nbackgr "<<Nbackgr <<endl;

	}
	MVA_B->Scale(Nbackgr/MVA_B->GetSumOfWeights());
	MVA_S->Scale(Nsignal/MVA_S->GetSumOfWeights());

	TH1D *FOM = (TH1D*)MVA_S->Clone("FOM");
	TH1D *significance = (TH1D*)MVA_S->Clone("significance");
	TH1D *backgrRejection = (TH1D*)MVA_S->Clone("backgrRejection");
	TH1D *signalEfficiency = (TH1D*)MVA_S->Clone("signalEfficiency");
	FOM->Scale(0);
	significance->Scale(0);
	backgrRejection->Scale(0);
	signalEfficiency->Scale(0);
	
	double fFOM,fsignificance,fbackgrRejection,fsignalEfficiency;
	double sumBackgr= 0;
	double sumSignal = 0;
	double RestSignal, RestBackgr, UncBackgr;

	int Nbins = MVA_S->GetNbinsX();
	cout << "Nbins" << Nbins <<endl;
	
	
	significance->SetBinContent(0,0);
	backgrRejection->SetBinContent(0,0);
	signalEfficiency->SetBinContent(0,1);
	FOM->SetBinContent(0,0);

	
	for (int i = 0; i<(Nbins-1); ++i)
	{
		sumBackgr += MVA_B->GetBinContent(i); 
		sumSignal += MVA_S->GetBinContent(i); 
		RestSignal = Nsignal-sumSignal;

		RestBackgr = Nbackgr-sumBackgr;
		UncBackgr = 0.2*RestBackgr;
		UncBackgr = UncBackgr*UncBackgr;
		fsignificance = (RestSignal)/sqrt(abs(RestSignal+RestBackgr+UncBackgr));
		fbackgrRejection = sumBackgr/Nbackgr;

		fsignalEfficiency = RestSignal/Nsignal;

		fFOM = sqrt( 2*( (RestSignal+RestBackgr)*log((RestSignal+RestBackgr)*(UncBackgr+RestBackgr)/(RestBackgr*RestBackgr+(RestSignal+RestBackgr)*UncBackgr)) - (RestBackgr*RestBackgr/UncBackgr)*log(1+UncBackgr*RestSignal/(RestBackgr*((UncBackgr+RestBackgr)))) ));

                if ((RestSignal+RestBackgr)*log((RestSignal+RestBackgr)*(UncBackgr+RestBackgr)/(RestBackgr*RestBackgr+(RestSignal+RestBackgr)*UncBackgr)) - (RestBackgr*RestBackgr/UncBackgr)*log(1+UncBackgr*RestSignal/(RestBackgr*((UncBackgr+RestBackgr)))) < 0) fFOM = 0;

		if (fbackgrRejection>=1) fFOM=0;
		if(fsignalEfficiency*Nsignal<0.5) {fFOM=0; fsignificance=0; }
		FOM->SetBinContent(i+1,fFOM);

		significance->SetBinContent(i+1,fsignificance);
		backgrRejection->SetBinContent(i+1,fbackgrRejection);
		signalEfficiency->SetBinContent(i+1,fsignalEfficiency);
        }
		
	Double_t x1end=-40,x3end=-40; int x1, x3;
	for(int i = 0; i < Nbins; ++i)
	{
		if(signalEfficiency->GetBinContent(i)*Nsignal>=1)
			{x1end=MVA_S->GetBinCenter(i); x1=i;}
		if(signalEfficiency->GetBinContent(i)*Nsignal>=3)
			{x3end=MVA_S->GetBinCenter(i); x3=i; }
	}
	TCanvas* canv1 = new TCanvas("ca1", "ca1");
	TLine* line1end = new TLine(x1end,0,x1end,1.5);
	TLine* line3end = new TLine(x3end,0,x3end,1.5);
	line1end->SetLineColor(1);
	line3end->SetLineColor(kOrange+7);	
		
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
        legend1->AddEntry(significance, "s/sqrt(s+b+(0.2b)^2)", "p");
        legend1->AddEntry(backgrRejection, "backgr rejection", "l");
        legend1->AddEntry(signalEfficiency, "signal efficiency", "l");
	legend1->AddEntry(line1end,"1 signal","l");
	legend1->AddEntry(line3end,"3 signal","l");
	
	cout << "bin number is " << FOM->GetXaxis()->FindBin(x3end) << endl;
	int maxbin = FOM->GetXaxis()->FindBin(x1end);
	double x1sig = MVA_S->GetXaxis()->GetBinLowEdge(maxbin);
	cout << "low edge is " << x1sig << endl;
	

	FOM->GetXaxis()->SetTitle("BDT Response");
	FOM->GetYaxis()->SetTitle("relative units");
	FOM->GetYaxis()->SetRangeUser(0,1.5);
	
	FOM->Draw("psame");
	if(x1end!=-40) line1end->Draw("same");
	if(x3end!=-40) line3end->Draw("same");
	significance->Draw("psame");
	backgrRejection->Draw("csame");
	signalEfficiency->Draw("csame");
        legend1->Draw();
	//canv1->Print(PlotDir+"N_FOM_SB_MaxSignificance_"+Input+"_mutau.pdf");

	canv1->Print(PlotDir+"N_FOM_SB_MaxSignificance_"+InputFile+"_mutau.pdf");


	TCanvas* canv2 = new TCanvas("ca2", "ca2");//stolbikami
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
        //canv2->Print(PlotDir+"N_MVA_SB_"+Input+"_mutau.pdf");
                canv2->Print(PlotDir+"N_MVA_SB_"+InputFile+"_mutau.pdf");


	//TCanvas* canv3 = new TCanvas("ca3", "ca3");
	cout <<"FOM->GetBinContent(34)  "<<FOM->GetBinContent(34) <<endl;
	cout <<"FOM->GetXaxis()->GetBinLowEdge(34)  "<<FOM->GetXaxis()->GetBinLowEdge(34) <<endl;
	cout <<"significance->GetBinContent(34)  "<<significance->GetBinContent(34) <<endl;
	cout <<"backgrRejection->GetBinContent(34)  "<<backgrRejection->GetBinContent(34) <<endl;
      	cout <<"signalEfficiency->GetBinContent(34)  "<<signalEfficiency->GetBinContent(34) <<endl;
	cout <<"Nsignal  "<<(Nsignal*signalEfficiency->GetBinContent(34)) <<endl;
	cout <<"Nbackgr  "<<(Nbackgr*(1-backgrRejection->GetBinContent(34))) <<endl;
	int iMax = significance->GetMaximumBin();
	cout <<"Max FOM is: " << FOM->GetBinContent(iMax) << endl;
	cout <<"Max FOM low edge is: " << FOM->GetXaxis()->GetBinLowEdge(iMax) << endl;
	cout <<"Nsignal Max FOM "<<(Nsignal*signalEfficiency->GetBinContent(iMax)) <<endl;
	cout <<"Nbackgr Max FOM "<<(Nbackgr*(1-backgrRejection->GetBinContent(iMax))) <<endl;

	cout <<"minimum value is: " << min(FOM->GetXaxis()->GetBinLowEdge(iMax),x1sig) <<endl;
	
	
	//Here we go
			std::list<double> listOfInts;
		int elm = 0;
	for(double i = 0.4; i < min(FOM->GetXaxis()->GetBinCenter(iMax),x1sig); i+=0.01)
	{	
		listOfInts.push_back(i);
		elm = elm + 1;
		}
		listOfInts.pop_back();
		
	for (double val : listOfInts){
		std::cout << setprecision(3) << val << ",";
	}
	std::cout << std::endl;
	//Here we go
	
	cout << "maximum bin    " << iMax <<endl;
	cout <<"FOM->GetBinContent(iMax)  "<<FOM->GetBinContent(iMax) <<endl;
	cout <<"FOM->GetXaxis()->GetBinLowEdge(iMax)  "<<FOM->GetXaxis()->GetBinLowEdge(iMax) <<endl;
	cout <<"significance->GetBinContent(iMax)  "<<significance->GetBinContent(iMax) <<endl;
	cout <<"backgrRejection->GetBinContent(iMax)  "<<backgrRejection->GetBinContent(iMax) <<endl;
    cout <<"signalEfficiency->GetBinContent(iMax)  "<<signalEfficiency->GetBinContent(iMax) <<endl;
	cout <<"Nsignal Max "<<(Nsignal*signalEfficiency->GetBinContent(iMax)) <<endl;
	cout <<"Nbackgr Max "<<(Nbackgr*(1-backgrRejection->GetBinContent(iMax))) <<endl;
	cout <<"Nsignal x1end "<<(Nsignal*signalEfficiency->GetBinContent(maxbin)) <<endl;
	cout <<"Nbackgr x1end "<<(Nbackgr*(1-backgrRejection->GetBinContent(maxbin))) <<endl;
	cout << "min(1,2)==" << min(FOM->GetXaxis()->GetBinLowEdge(iMax),x1sig) << '\n';
		cout <<"x1end is: " << x1sig <<endl;
		cout <<"FOM->GetXaxis()->GetBinLowEdge(iMax) is: " << FOM->GetXaxis()->GetBinLowEdge(iMax) <<endl;
	//cout << "min(1,2)==" << min(FOM->GetBinContent(iMax),x3end) << '\n';

	
	ofstream fout;
	fout.open("bincor.txt", ios_base::app);
/*	fout<<endl<<InputFile<<endl;
	fout<<"significance 3 signals:	"<<significance->GetBinContent(x3)<<endl;
	fout<<"significance 1 signal:	"<<significance->GetBinContent(x1)<<endl;
	fout<<"X axis 3 signals: "<<x3end<<endl;
	fout<<"X axis 1 signal: "<<x1end<<endl;
	fout<<"Nbackgr: "<<(Nbackgr*(1-backgrRejection->GetBinContent(iMax))) <<endl;
	fout<<"Nsignal: "<<(Nsignal*signalEfficiency->GetBinContent(iMax))<<endl;
	fout<<"X axis Max Significance: "<<significance->GetBinContent(iMax) <<endl;
	fout<<"X axis Max FOM: "<< FOM->GetBinContent(iMax)  <<endl; 
	fout<<"Table of binning is: " <<endl; */
	fout<<"int nbinsBDTmutau_"<< Input << "= "<< elm + 1 <<";" <<endl;
	fout<<" double binsBDTmutau_"<< Input <<"["<< elm + 2 << "]  = {0.0, ";
	for (double val : listOfInts){
		fout << setprecision(3) << val << ",";
	}
	fout << min(FOM->GetXaxis()->GetBinLowEdge(iMax),x1sig) << ",1.0};" <<endl;
	//fout << "hBDTmutau_" << Input << "[cj] = new TH1D (\"BDTmutau_" << Input << "_\"" << "+nCut + Nplots," <<  "\"BDTmutau_" << Input << " \"+cutName + Nplots,nbinsBDTmutau_" << Input <<",binsBDTmutau_" << Input << ");" << endl;
    //fout << "hBDTmutau_" << Input << "[cj]->Sumw2();" << endl;
	fout<<"	"<<endl;
	fout.close();
	cout<<"table ready"<<endl;
}
