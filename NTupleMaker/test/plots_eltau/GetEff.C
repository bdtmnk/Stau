#include <cmath>
#include <sstream>
#include <iomanip>
#include "TChain.h"
#include "TH1.h"
#include "TTree.h"
#include "TKey.h"
#include "Riostream.h"
#include "TCanvas.h"
#include "TFile.h"
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
#include "Riostream.h"
#include <iostream>
#include <fstream>
//#include "tdrstyle.C"


using namespace std;



void Impose( TDirectory *ttarget, TList *ssourcelist, string &np_legend , vector<string> titles_ );
void ModifyHist (TH1D* &h, int cl,vector <string> title);

TCanvas *modifyCanvas (TCanvas *c1);

// void MergeRootfile( TDirectory *target, TList *sourcelist );


void GetEff()
{
       
    gROOT->SetStyle ("Plain");
    gStyle->SetPalette (1);
    gStyle->SetTextFont(22) ;
    gStyle->SetTitleFont(22,"xyz") ;
    gStyle->SetLabelFont(22,"xyz") ;
 //   setTDRStyle();
 

  
  
    vector <string> titles;
    vector <float> mspart;
    vector <float> mlsp;
    // void MergeRootfile( TDirectory *target, TList *sourcelist );
    //TTrees
    TList *FileList;
    TFile *Target;
    titles.clear();
 
   Float_t value=0;

   ifstream ifs("ds");
   string line;
   while(std::getline(ifs, line)) // read one line from ifs
    {
    istringstream iss(line); // access line as a stream
    string dataname;
    float sparticle,lsp;
    iss >> dataname >> sparticle >> lsp ; // no need to read further
    //titles.push_back(dataname+".root");
    titles.push_back(dataname);
    mspart.push_back(sparticle);
    mlsp.push_back(lsp);
    }
    
 float step=50;
 float stopmin = 25;
 float stopmax = 600;
 float n1min = 0;
 float n1max = 600;
 float xNbins = (stopmax-stopmin)/step;
 float yNbins = (n1max-n1min)/step;
 float stop,n1;
  


    char histotitle[100];
    char ranktitle[100];
    char filetitle[100];

     TFile *fout,*f;

    string np_title = titles[0];
    for (unsigned int j=0;j<titles.size();j++)
    {

	   
    sprintf(filetitle,"eff_%s",titles[j].c_str());
    fout = TFile::Open(filetitle,"recreate");
	
     f = TFile::Open(titles[j].c_str(),"read");

	TH1D * histW = (TH1D*)f->Get("mutau/histWeightsH");
	TH1D * hxsecW = (TH1D*)f->Get("mutau/xsec");
	TH1D * CutFlow = (TH1D*)f->Get("mutau/CutFlowUnW");

	int TotalEvents = histW->GetSumOfWeights();

    int TotalBins = CutFlow->GetNbinsX();
    TH2D *h[TotalBins] ;//= new TH2F ("LastBin Sign","Last Bin Sign", xNbins, stopmin, stopmax, yNbins, n1min, n1max);
    //TH2D *hrank[TotalBins] ;//= new  TH2D ("ranking",histotitle, xNbins, stopmin, stopmax, yNbins, n1min, n1max);	   
   
   
    cout<<" The size is "<<TotalBins<<" for  "<<filetitle<<"  events "<<TotalEvents<<endl;


    for (unsigned int k=0;k<TotalBins;++k){

    if (j==0){
    sprintf(histotitle,"Efficiency_%s",CutFlow->GetXaxis()->GetBinLabel(k));
    h[k] = new TH2D (histotitle,histotitle, xNbins, stopmin, stopmax, yNbins, n1min, n1max);	   
    h[k]->Fill(1.,1.,-1.);
    h[k]->GetXaxis()->SetTitle("#tilde{#tau} mass (GeV)");
    h[k]->GetYaxis()->SetTitle("#chi_{1}^{0} mass (GeV)");
  
    }
  
  
    h[k]->Fill(mspart[j], mlsp[j],float(CutFlow->GetBinContent(k)/TotalEvents)); 

     fout->cd();
     h[k]->SetStats(0000000);
     h[k]->Draw("colz text hist");
     h[k]->Write();
  }


    for (unsigned int k=0;k<TotalBins;++k)    delete h[k];

   // fout.Close();

  cout<<" done with it for "<<mspart[j]<<"  "<<mlsp[j]<<endl;
  //delete t;
  f->Close();
  delete f;
   
    }

    fout->Close();
    delete fout;

}
