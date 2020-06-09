#include <cmath>
#include <sstream>
#include <iomanip>
#include "TH1.h"
#include "TTree.h"
#include "TFile.h"
#include <string>
#include "TLegend.h"
#include "TROOT.h"
#include "TFrame.h"
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include "TObject.h"
#include <functional>
#include "TMath.h"
#include "Riostream.h"
#include <iostream>
#include <fstream>
#include "tdrstyle.C"


using namespace std;
void OverFlow (TH1D* &h, int bin);
//void ModifyHist (TH1D* &h, int cl,float &lumi_,float &weight_,bool norm_);

//void GetHisto(){
void GetHisto(const char *obj_name = "data_obs_hDZeta_19"){

  float Lumi = 10000.;
 
  TFile * f = new TFile("BkgTemplates_hDZeta.root","read");
  TList *list = (TList *)f->GetListOfKeys();
  f->cd();
  f->ls();
  
  TH1D * hObs = (TH1D*)f->Get(obj_name);

  OverFlow(hObs,hObs->FindLastBinAbove(5));
  
  TFile * file = new TFile("stau50_LSP1_B.root","read");
  file->cd("mutau");
  TH1D * h1 = (TH1D*)file->Get("mutau/hDZeta_19");
				
  TH1D* eventCount = (TH1D*)file->Get("mutau/histWeightsH");
  TH1D* hxsec = (TH1D*)file->Get("mutau/xsec");
  float xsec = hxsec->GetMean();
  xsec = 1.;
				
  float nGen = eventCount->GetSumOfWeights();
  float norm = float(xsec*Lumi) / float(nGen)  ;

  int cl = 1;
  ModifyHist (h1, cl,Lumi,norm,false);
			
  OverFlow(h1,hObs->FindLastBinAbove(5));

  TFile * file1 = new TFile("SignalTemplates_hDZeta.root","update");
  file1->cd();
  h1->SetName("stau50_LSP1_B_hDZeta");
  h1->SetMinimum(0.01);
  h1->SetLineColor(kBlack);
  h1->SetMarkerColor(kBlack);
  h1->Write();
  file1->Write();
  file1->Close();

}


void ModifyHist (TH1D* &h, int cl_ ,float & lumi,float & weight,bool norm_=false)
		{


			int nbins=h->GetNbinsX();
			int nn=1;

			if (  nbins<=150)  nn=5;
			if (  nbins>150)  nn=5;
			if (  nbins>200)  nn=10;
			if (  nbins<=50)  nn=1;
			if (nbins%64 == 0) nn=2;
			if (nbins%kTeal+9 == 0) nn=2;
			//if (h->GetNbinsX()>80 && nbins%5==0) nn=5;

			if (h->GetNbinsX()>40 && nbins%2==0) nn=2;
			if (h->GetNbinsX()>40 && nbins%3==0) nn=3;
			if (h->GetNbinsX()>40 && nbins%4==0) nn=4;
			h->Rebin(nn);
			//h->Sumw2();

			h->SetMinimum(1);
			h->GetXaxis()->SetNdivisions(512);
			string titlee=h->GetName();
			int col=;//kOrange;
			string title1,title2;
			title1= h->GetTitle();

				col=cl_;
				h->SetLineStyle(1);
				h->SetMarkerStyle(32);
				h->SetMarkerSize(0.4);
				h->SetMarkerColor(col);
				h->SetLineColor(col);
				h->SetLineStyle(6);



			h->Scale(weight);

if (norm_)    
	h->Scale (1/h->Integral());



	}



void OverFlow(TH1D *& h, int &last_bin){

			int nb = h->GetNbinsX();
                        float over_ = h->GetBinContent(last_bin);
                        float contlast = 0.;//h->GetBinContent(last_bin);
			for (int b=last_bin; b <= nb+1; b++) {contlast +=h->GetBinContent(b);h->SetBinContent(b,0.);}

                        h->SetBinContent(last_bin,0);
                        h->SetBinContent(last_bin,contlast);
}
