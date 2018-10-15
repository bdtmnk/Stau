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
#include <string>
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
#include "TPie.h"
#include "Riostream.h"
#include <iostream>
#include <fstream>
#include "tdrstyle.C"


using namespace std;

void Impose( TDirectory *ttarget, TList *ssourcelist, string &np_legend , vector<string> titles_ );
void ModifyHist (TH1D* &h, int cl,vector <string> title);
void ModifyHist (TH1D* &h, int cl,vector <string> title, TLegend * & tleg);
void ModifyHist (TH1D* &h, int cl);
void OverFlow (TH1D* &h, int bin);
TCanvas *modifyCanvas (TCanvas *c1);
TCanvas *example_plot(int iPeriod, int iPos , TString name);

// void MergeRootfile( TDirectory *target, TList *sourcelist );


void OverlapSignal()
{

	gROOT->SetStyle ("Plain");
	gStyle->SetPalette (1);
	gStyle->SetTextFont(22) ;
	gStyle->SetTitleFont(22,"xyz") ;
	gStyle->SetLabelFont(22,"xyz") ;
	setTDRStyle();



	vector <string> titles;
	// void MergeRootfile( TDirectory *target, TList *sourcelist );
	//TTrees
	TList *FileList;
	TFile *Target;
	titles.clear();
	int np=1;

	Float_t value=0;
	ifstream ifs("signal");
	string line;
	while(std::getline(ifs, line)) // read one line from ifs
	{
		istringstream iss(line); // access line as a stream
		string dataname;
		iss >> dataname ; // no need to read further
		titles.push_back(dataname);
	}

	string fout = "mergedplotsTau.root";


	FileList = new TList ();


	for (unsigned int i=0; i <titles.size();++i){
		//string ext=".root";
		cout<<" loading dataset "<<titles[i]<<endl;
		//string file=titles[i]+".root";
		string file=titles[i];
		FileList->Add (TFile::Open (file.c_str()));
	}


	//return;
	Target = TFile::Open (fout.c_str (), "RECREATE");

	string np_title = titles[0];
	Impose (Target, FileList, np_title,titles);
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


	Lumi = 2301.;
	bool norm_=false;
	cout<<titles[0]<<"   "<<titles.size()<<endl;

	//not really useful if plots already weighted to lumi - usefull is plots are in a.u.
	vector <float > lumiweights;
	vector <string > signal_names;
	signal_names.clear();
	lumiweights.clear();
	string sign_="stau";
	string n_;
	for (unsigned int k=0; k<titles.size();k++)
	{
		if (   std::string::npos != titles[k].find(sign_)){
			n_ = titles[k];
			n_.erase(n_.length()-7);
			string nn_ = n_;//+"_out.root";
			signal_names.push_back(nn_.c_str());
		}
	}
	for (unsigned int k=0; k<signal_names.size();k++){
		cout<<" HERE ==========================  "<<signal_names[k]<<endl;
	}

	TFile *first_source = (TFile *) sourcelist->First ();
	first_source->cd ("mutau");

	TH1D* eventCount = (TH1D*)first_source->Get("mutau/histWeightsH");
	float nGen = eventCount->GetSumOfWeights();
	float xsec = 1;
	float norm = xsec*Lumi/nGen;

	norm =1;
	lumiweights.push_back(float(norm));



	TDirectory *current_sourcedir = gDirectory;
	Bool_t status = TH1::AddDirectoryStatus ();
	TH1::AddDirectory (kFALSE);
	TChain *globChain = 0;
	TIter nextkey (current_sourcedir->GetListOfKeys ());
	TKey *key, *oldkey = 0;
	TFile *smFile = TFile::Open ("sm.root", "recreate");
	while ((key = (TKey *) nextkey ())) {
		first_source->cd ("mutau");
		TObject *obj = key->ReadObj ();
		string nn = obj->GetName();
		if (string::npos == nn.find("hDZeta_19") ) continue;

		if (obj->IsA ()->InheritsFrom ("TTree") ) continue;
		if (obj->IsA ()->InheritsFrom ("TH2") ) continue;
		if (obj->IsA ()->InheritsFrom ("TH1D") ) {
			// descendant of TH1D-> prepare the histograms to be superimposed

			TH1D* hh[300];
			TH1D* h1 = (TH1D*) obj;
			if (h1->Integral() <0.000001) continue;

			ModifyHist (h1,1,Lumi,lumiweights[0],titles[0],norm_);


			TFile *nextsource = (TFile *) sourcelist->After (first_source);

			int cl, countsignal;
			h1->SetStats(000000);
			h1->SetLineWidth(5);
			cl=1;
			countsignal=1;

			hh[cl]=h1;

			while (nextsource) {


				nextsource->cd("mutau");
				TH1D* eventCountt = (TH1D*)nextsource->Get("mutau/histWeightsH");
				TH1D* hxsecc = (TH1D*)nextsource->Get("mutau/xsec");
				float xsecc = hxsecc->GetMean();
				float nGenn = eventCountt->GetSumOfWeights();
				float normm = float(xsecc*Lumi) / float(nGenn)  ;

				lumiweights.push_back(normm);

				TKey *key2 = (TKey *) gDirectory->GetListOfKeys ()->FindObject (h1->GetName ());

				if (key2) {
					cl++;
					countsignal++;
					TH1D *h2;

					h2 = (TH1D*) key2->ReadObj ();
					h2->SetLineWidth(4);
					ModifyHist (h2, cl,Lumi,lumiweights[cl-1],titles[cl-1],norm_);
					h2->SetStats(0);
					hh[cl] = h2;
				}

				nextsource = (TFile *) sourcelist->After (nextsource);
			}				// while ( nextsource )
		}

		if (obj) {
			target->cd ();

			hh[1]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(5));
			OverFlow(hh[1],hh[1]->FindLastBinAbove(5));
			

			for (unsigned int kk=0;	kk < signal_names.size() ; kk++){
			hh[kk+2]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());
			OverFlow(hh[kk+2],hh[1]->FindLastBinAbove(5));

			string nan_ = key->GetName ();
				if (   nan_ == "hDZeta_19") 
					{
					hh[kk+2]->SetMinimum(0.01);
					char ns[100];
					sprintf(ns,"%s",signal_names[k].c_str());
					//hh[kk+2]->SetName(ns);
				cout<<" ========================>   "<<signal_names[k].c_str()<<" name "<<nan_<<" size "<<signal_names.size()<<"  "<<hh[kk+2]->GetName()<<"  "<<hh[kk+2]->GetTitle()<<endl;
					smFile->cd();
					hh[kk+2]->Write();
					}
				}

			//smFile->Write();
			}//if obj


		cout<< " here "<<endl;
		} 			// while ( ( TKey *key = (TKey*)nextkey() ) )
		// save modifications to target file
		target->SaveSelf (kTRUE);
		TH1::AddDirectory (status);
		cout << "	" << "========================================================" << endl;
		cout<< " Ended SuperImpose of files.... " <<endl;




	}

	void
		//ModifyHist (TH1D* &h, int cl_ ,float & lumi,float & weight,string & title_, bool norm_=false,TLegend *& legend)
		ModifyHist (TH1D* &h, int cl_ ,float & lumi,float & weight,string & title_, bool norm_=false)
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


			if (std::string::npos != title_.find("Data") || std::string::npos != title_.find("Single") || std::string::npos != title_.find("StauA") || std::string::npos != title_.find("tau") ||  std::string::npos != title_.find("Sq") || std::string::npos != title_.find("Gl") || std::string::npos != title_.find("0.2")  )  {

				//if ( std::string::npos != title_.find("StauA") ){

				col=kBlack ;
				h->SetLineStyle(1);
				h->SetMarkerStyle(20+cl_);
				h->SetMarkerSize(0.4);
				h->SetMarkerColor(col);
				h->SetLineColor(col);
			}


			if ( std::string::npos != title_.find("tau") || std::string::npos != title_.find("0.5") ){

				col=5+ cl_;
				h->SetLineStyle(1);
				h->SetMarkerStyle(32);
				h->SetMarkerSize(0.4);
				h->SetMarkerColor(col);
				h->SetLineColor(col);
				h->SetLineStyle(6);
			}



			h->Scale(weight);

			if (std::string::npos != title_.find("wJets")|| std::string::npos != title_.find("WJetsToLNu"))  { col= kPink;}// counter[0]  =h->Integral() }//cout << " ==============================  "<<h->Integral()<<endl;}
			if (std::string::npos != title_.find("TTJets") || std::string::npos != title_.find("TTPow")) { col= 60; }
			if (std::string::npos != title_.find("QCD"))  {col= kYellow-7; }
			if (std::string::npos != title_.find("DYJets"))  {col= kTeal+9;}
			if (std::string::npos != title_.find("ST_") || std::string::npos != title_.find("channel")  || std::string::npos != title_.find("ST_"))  {col= kAzure+10; }//counter[4] +=h->Integral();}
			if ( td::string::npos != title_.find("WWZ") || std::string::npos != title_.find("WWTo") || std::string::npos != title_.find("ZZ") || std::string::npos != title_.find("ZZTo")|| std::string::npos != title_.find("WZ") || std::string::npos != title_.find("WZZ")) {col=kMagenta+2;}// counter[5] +=h->Integral();}
			if ( std::string::npos != title_.find("TTW") || std::string::npos != title_.find("TTZ") || std::string::npos != title_.find("tZq") || std::string::npos != title_.find("TG") || std::string::npos != title_.find("tG")) {col=kOrange-4; }//counter[6] +=h->Integral();}


			float nm = 0.;nm = float(h->Integral());

			h->GetXaxis()->SetTitleOffset(0.8);
			h->GetYaxis()->SetTitleOffset(1.5);

			h->SetMinimum(1);
			h->SetLineStyle (col);


			h->SetFillColor(col);
			h->SetLineColor(col);





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



