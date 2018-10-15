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
#include "tdrstyle.C"


using namespace std;

void Impose( TDirectory *ttarget, TList *ssourcelist, string &np_legend , vector<string> titles_ );
void ModifyHist (TH1D* &h, int cl,vector <string> title);
void ModifyHist (TH1D* &h, int cl,vector <string> title, TLegend * & tleg);
void ModifyHist (TH1D* &h, int cl);
TCanvas *modifyCanvas (TCanvas *c1);
TCanvas *example_plot(int iPeriod, int iPos , TString name);

// void MergeRootfile( TDirectory *target, TList *sourcelist );


void ExtractRanks()
{
       
    gROOT->SetStyle ("Plain");
    gStyle->SetPalette (1);
    gStyle->SetTextFont(22) ;
    gStyle->SetTitleFont(22,"xyz") ;
    gStyle->SetLabelFont(22,"xyz") ;
 //   setTDRStyle();
 

  
 vector <string> titles;
    // void MergeRootfile( TDirectory *target, TList *sourcelist );
    //TTrees
    TList *FileList;
    TFile *Target;
    titles.clear();
    int np=1;
 
   Float_t value=0;
   ifstream ifs("ranker");
   string line;
   while(std::getline(ifs, line)) // read one line from ifs
    {
    istringstream iss(line); // access line as a stream
    string dataname;
    iss >> dataname ; // no need to read further
    //titles.push_back(dataname+".root");
    titles.push_back(dataname);
    }
    
    string fout ;
    
    
    FileList = new TList ();
        
    
        
    
    string np_title = titles[0];
    for (int j=0;j<titles.size();j++)
    {
    FileList = new TList ();
    fout = titles[j];
    FileList->Add (TFile::Open (fout.c_str()));

    string nam_ = fout.c_str();
    nam_.erase(nam_.length()-5);
    fout = nam_+"_ranked_plots.root";
    Target = TFile::Open (fout.c_str (), "RECREATE");
    cout<<" loading dataset "<<titles[j]<<endl;
    Impose (Target, FileList, np_title,titles);

    }

    delete FileList;
    delete Target;
}


void
Impose (TDirectory * target, TList * sourcelist, string & np_title_, vector<string> titles)
{
    cout << "	" << "========================================================" << endl;
    cout << "	" << "This is a macro to superimpose plots of different root files." << endl;
    cout << "	" << "Only TH1Dobjects are superimposed." << endl;
    cout << "	" << "Target path: " << target->GetPath () << endl;
    TString path ((char *) strstr (target->GetPath (), ":"));
    path.Remove (0, 2);
     float Lumi=1;

     //////Lumi =  149.487714934 full v3 , not 25ns C first runs = 133.143136532
    ////// Lumi = 1.65fb  , not 25ns C = 1.633376938269 /fb

    //float Lumi= 7.301;
    //float Lumi= 5000;
    // Lumi=16.859; ///PRv1
    //Lumi = 832.31 ; /// PRv1 + 05Oct+ PRv4
    //Lumi = 1697.;
    Lumi = 2301.;
    //Lumi = 860.71;
    //float Lumi=40.;
    bool norm_=false;
    
    //not really useful if plots already weighted to lumi - usefull is plots are in a.u.
    vector <float > lumiweights;
    vector <string > signal_names;
    signal_names.clear();
    lumiweights.clear();
    string sign_="stau";
    string signn_="Stau";
    string n_;
    TFile *first_source = (TFile *) sourcelist->First ();
    first_source->cd ("");
    
    
  

    TDirectory *current_sourcedir = gDirectory;
    //gain time, do not add the objects in the list in memory
    Bool_t status = TH1::AddDirectoryStatus ();
    TH1::AddDirectory (kFALSE);
    // loop over all keys in this directory
    TChain *globChain = 0;
    TIter nextkey (current_sourcedir->GetListOfKeys ());
    //TIter nextkey (((TDirectory *) current_sourcedir->Get ("ana"))->GetListOfKeys ());
    TKey *key, *oldkey = 0;
    int count=0;
        TCanvas *c1  ;//= new TCanvas ("c1",obj->GetName (),0,22,600,600);
    while ((key = (TKey *) nextkey ())) {
        count++;
    //    if (count>20) break;
        //keep only the highest cycle number for each key
//        if (oldkey && !strcmp (oldkey->GetName (), key->GetName ()))
//            continue;
        
        // read object from first source file and create a canvas
       // first_source->cd (path);
        first_source->cd ("");
        TObject *obj = key->ReadObj ();
	     string nn = obj->GetName();
            if (std::string::npos != nn.find("_20") ) break;
        
      //  if (obj->GetName () != "CutFlow" ) continue;
	//string nn = obj->GetName();
      // if (std::string::npos == nn.find("Cut")) continue;
        //cout<<obj->GetName()<<endl;
       
        
        
 	 //TCanvas *c1 = example_plot(3, 0 , obj->GetName ());
        
         //if (obj->IsA ()->InheritsFrom ("TH2") ) continue;
         if (obj->IsA ()->InheritsFrom ("TTree") ) continue;

         if (obj->IsA ()->InheritsFrom ("TH2D") ) {
            // descendant of TH1D-> prepare the histograms to be superimposed
            
             c1  = new TCanvas ("c1",obj->GetName (),0,22,600,600);

           TH2D* h1 = (TH2D*) obj;
	   //if (h1->Integral()<1) continue;
            
           double counter[10];    
           //ModifyHist (h1,1,Lumi,lumiweights[0],titles[0],norm_,counter);
          
	   //delete c1;	
        }
        
            
        if (obj) {
	        
                 target->cd();
		 c1->cd();
		 h1->Draw("colz text");
		 c1->SetName(h1->GetName());
		 c1->SetTitle(h1->GetTitle());
		 c1->Write();
		char namee[100];
		sprintf(namee,"Rank/%s.png",c1->GetTitle());
		 c1->SaveAs(namee);
		 

            
            
    
        }

  	} 			// while ( ( TKey *key = (TKey*)nextkey() ) )



    TH1::AddDirectory (status);
    cout << "	" << "========================================================" << endl;
    cout<< " Ended SuperImpose of files.... " <<endl;
    
    // for (int i=0;i<SValueVariables_.size();i++){
    //cout<<SValueVariables_[i].second<<endl;}
    
    
    
}

void
//ModifyHist (TH1D* &h, int cl_ ,float & lumi,float & weight,string & title_, bool norm_=false,TLegend *& legend)
ModifyHist (TH1D* &h, int cl_ ,float & lumi,float & weight,string & title_, bool norm_=false,double counter_[10])
{

  
    int nbins=h->GetNbinsX();
    int nn=1;
    /*
    if (  nbins<=150)  nn=5;
    if (  nbins>150)  nn=5;
    if (  nbins>200)  nn=10;
    if (  nbins<=50)  nn=1;
    if (nbins%64 == 0) nn=2;
    if (nbins%38 == 0) nn=2;
*/
    if (h->GetNbinsX()>80 && nbins%3==0) nn=3;
    if (h->GetNbinsX()>80 && nbins%4==0) nn=4;
    if (h->GetNbinsX()>80 && nbins%5==0) nn=5;
     //h->Rebin(nn);
  	 //h->Sumw2();

    h->SetMinimum(1);
    h->GetXaxis()->SetNdivisions(512);
    string titlee=h->GetName();
    int col=;//kOrange;
    string title1,title2;
    title1= h->GetTitle();
   

   
   
    //h->SetLineWidth(2);
    int nb = h->GetNbinsX();
    float over_ = h->GetBinContent(nb+1);
    float contlast = h->GetBinContent(nb);
    h->SetBinContent(nb,contlast+over_);
    //if (weight != 1.) 
     h->Scale(weight);

   
    if (std::string::npos != title1.find("MET"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
    if (std::string::npos != title1.find("mass"))  h->GetXaxis()->SetTitle("GeV/c");
    if (std::string::npos != title1.find("Inv"))  h->GetXaxis()->SetTitle("GeV/c");
    if (std::string::npos != title1.find("Mass"))  h->GetXaxis()->SetTitle("GeV/c");
    if (std::string::npos != title1.find("met"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
    if (std::string::npos != title1.find("ST"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
    if (std::string::npos != title1.find("HT"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
    if (std::string::npos != title1.find("Jetp"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
    if (std::string::npos != title1.find("Phi"))  h->GetXaxis()->SetTitle("");
    if (std::string::npos != title1.find("dPhi"))  h->GetXaxis()->SetTitle("");
    if (std::string::npos != title1.find("pT"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
    if (std::string::npos != title1.find("nB"))  h->GetXaxis()->SetTitle("B-Jets");
    if (std::string::npos != title1.find("nJ"))  h->GetXaxis()->SetTitle("#Jets");
    if (std::string::npos != title1.find("nL"))  h->GetXaxis()->SetTitle("#Lept");
    if (std::string::npos != title1.find("nmu"))  h->GetXaxis()->SetTitle("#muons");
    if (std::string::npos != title1.find("nel"))  h->GetXaxis()->SetTitle("#el");
    
    h->GetXaxis()->SetTitleOffset(0.8);
    
    h->GetYaxis()->SetTitleOffset(1.5);
    
    //h->SetLineColor (col);
       
    //h->SetFillColor (col);
    h->SetMinimum(1);
    h->SetLineStyle (col);



  ofstream tfile;
    if (std::string::npos != title1.find("Cut Flow") ){
  TString outname=title_;
  TString textfilename = "cutflow_"+outname +".txt";
  tfile.open(textfilename);

   tfile << "########################################" << endl;
   for (int b=0;b<16;b++){
   //tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<" & "<<" & "<<endl;	
   if (h->GetBinContent(b) > 0 ) tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<endl;	
   else tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<0<<endl;	
   //cout <<title1<<" & "<<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<" & "<<" & "<<endl;	
	}}
    tfile.close();
    if (norm_)    
      h->Scale (1/h->Integral());
    
    
    //double dic=double(lumi)/double(weight);
    //double dic=0;
    //if (h->Integral()>0)
    //dic=double(lumi)/double(weight);
    //dic=1;
    string namet=h->GetName();
    
    // double q[5];
    // double probs[5] = {0.025, 0.16, 0.5, 1 - 0.16, 0.975 };
    //  h->GetQuantiles( 5, q, probs );
    
    //    cout<<" Median and Mean values for  process"<<title_<<" variable"<<h->GetName()<<" median "<<q[2]<<" mean "<<h->GetMean()<<endl;
    
    
}


