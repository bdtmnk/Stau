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

void Impose( TDirectory *ttarget, TList *ssourcelist, string &np_legend , vector<string> titles_ ,vector<float> xsecs);
void ModifyHist (TH1D* &h, int cl,vector <string> title);
void ModifyHist (TH1D* &h, int cl,vector <string> title, TLegend * & tleg);
void ModifyHist (TH1D* &h, int cl);
void OverFlow (TH1D* &h, int bin);
ReBin(TH1* &h);
ReBinn(TH1* &h);
ReBinAxis(TH1 *&h);
TCanvas *modifyCanvas (TCanvas *c1);
TCanvas *example_plot(int iPeriod, int iPos , TString name);

// void MergeRootfile( TDirectory *target, TList *sourcelist );


void OverlapZeroLSPC1()
{

	gROOT->SetStyle ("Plain");
	gROOT->LoadMacro("CMS_lumi.C");
	gStyle->SetPalette (1);
	gStyle->SetTextFont(22) ;
	gStyle->SetTitleFont(22,"xyz") ;
	gStyle->SetLabelFont(22,"xyz") ;
	setTDRStyle();


	writeExtraText = true;       // if extra text
	extraText  = "Preliminary";  // default extra text is "Preliminary"
	lumi_8TeV  = "19.1 fb^{-1}"; // default is "19.7 fb^{-1}"
	lumi_7TeV  = "4.9 fb^{-1}";  // default is "5.1 fb^{-1}"
	lumi_sqrtS = "13 TeV";       // used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

	int iPeriod = 0;    // 1=7TeV, 2=8TeV, 3=7+8TeV, 7=7+8+13TeV, 0=free form (uses lumi_sqrtS)

	// second parameter in example_plot is iPos, which drives the position of the CMS logo in the plot
	// iPos=11 : top-left, left-aligned
	// iPos=33 : top-right, right-aligned
	// iPos=22 : center, centered
	// mode generally :
	//   iPos = 10*(alignement 1/2/3) + position (1/2/3 = left/center/right)

	//example_plot( iPeriod, 0 );   // out of frame (in exceptional cases)
	//  example_plot( iPeriod, 11 );  // left-aligned
	//  example_plot( iPeriod, 33 );  // right-aligned

	//  writeExtraText = false;       // remove Preliminary

	//  example_plot( iPeriod, 0 );   // out of frame (in exceptional cases)

	//  example_plot( iPeriod, 11 );  // default: left-aligned
	//  example_plot( iPeriod, 22 );  // centered
	//  example_plot( iPeriod, 33 );  // right-aligned

	vector <string> titles;
	// void MergeRootfile( TDirectory *target, TList *sourcelist );
	//TTrees
	TList *FileList;
	TFile *Target;
	titles.clear();
	int np=1;

	Float_t value=0;
	vector<float> xsecs_;
	ifstream ifs("datasetsZeroLSPC1");
	string line;
	while(std::getline(ifs, line)) // read one line from ifs
	{
		istringstream iss(line); // access line as a stream
		string dataname;
		float XSec;	
		float xs,fact,fact2;
		xs=0;fact=1;fact2=1;
		iss >> dataname >> xs >> fact >> fact2;
		titles.push_back(dataname+"_B.root");
		XSec= xs*fact*fact2;
		cout<<" Found the correct cross section "<<xs<<" for Dataset "<<dataname<<" XSec "<<XSec<<"  "<<fact<<"  "<<fact2<<endl;
		xsecs_.push_back(XSec);
	}

	string fout = "mergedplotsTauZeroLSPC1.root";
			
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
	Impose (Target, FileList, np_title,titles,xsecs_);
	delete FileList;
	delete Target;
}


	void
Impose (TDirectory * target, TList * sourcelist, string & np_title_, vector<string> titles,vector<float> xsecs)
{
	cout << "	" << "========================================================" << endl;
	cout << "	" << "This is a macro to superimpose plots of different root files." << endl;
	cout << "	" << "Only TH1Dobjects are superimposed." << endl;
	cout << "	" << "Target path: " << target->GetPath () << endl;
	TString path ((char *) strstr (target->GetPath (), ":"));
	path.Remove (0, 2);


	Float_t Lumi = 12000.;
	bool norm_=false;
	bool full = false;
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
		if (   std::string::npos != titles[k].find(sign_) || string::npos != titles[k].find("C1")){
			n_ = titles[k];
			n_.erase(n_.length()-5);
			string nn_ = n_+"_out.root";
			signal_names.push_back(n_.c_str());
		}
	}
	for (unsigned int k=0; k<signal_names.size();k++){
		cout<<" HERE ==========================  "<<signal_names[k]<<"  "<<signal_names.size()<<endl;
	}

	TH1D* allbkg, *htt,*hstop,*hwj,*hdyj,*hrare,*hdib,*hqcd,*httx;

	TFile *first_source = (TFile *) sourcelist->First ();
	first_source->cd ("mutau");

	TH1D* eventCount = (TH1D*)first_source->Get("mutau/histWeightsH");
	//TH1D* eventCount = (TH1D*)first_source->Get("mutau/inputEventsH");
	//TH1D* hxsec = (TH1D*)first_source->Get("mutau/xsec");
	float nGen = eventCount->GetSumOfWeights();
	float xsec = 1;//hxsec->GetMean();
	float norm = xsec*Lumi/nGen;

	norm =float(8000/2320);
	lumiweights.push_back(float(norm));


	//cout<< " for first source file, there where "<<nGen<<" events with xsec "<<xsec<<" weight "<<lumiweights[0]<<endl;//" weight "<<float(xsec*Lumi/nGen)<<"  norm "<<norm<<endl;

	TDirectory *current_sourcedir = gDirectory;
	//gain time, do not add the objects in the list in memory
	Bool_t status = TH1::AddDirectoryStatus ();
	TH1::AddDirectory (kFALSE);
	// loop over all keys in this directory
	TChain *globChain = 0;
	TIter nextkey (current_sourcedir->GetListOfKeys ());
	//TIter nextkey (((TDirectory *) current_sourcedir->Get ("ana"))->GetListOfKeys ());
	TKey *key, *oldkey = 0;
	cout<<" THE FINAL COUNTDOWN ======================================== "<<signal_names.size()<<endl;
	TFile *smFile = TFile::Open ("BkgTemplates_hDZeta.root", "recreate");
	TFile *NPfile = TFile::Open ("Signals.root", "recreate");
	int count=0;
	TCanvas *c1  ;//= new TCanvas ("c1",obj->GetName (),0,22,600,600);
	c1  = new TCanvas ("c1","c1",0,22,600,600);
	while ((key = (TKey *) nextkey ())) {
		count++;
		//if (count>20) break;
		//keep only the highest cycle number for each key
		//        if (oldkey && !strcmp (oldkey->GetName (), key->GetName ()))
		//            continue;

		// read object from first source file and create a canvas
		// first_source->cd (path);
		first_source->cd ("mutau");
		TObject *obj = key->ReadObj ();

		//string nn = obj->GetName();
		// if (std::string::npos == nn.find("Cut")) continue;
		//cout<<obj->GetName()<<endl;

		//c1  = new TCanvas ("c1",obj->GetName (),0,22,600,600);
		c1->SetName("c1");
		c1->SetTitle(obj->GetTitle());

	//	c1 = example_plot(3, 0 , obj->GetName ());

		string nn = obj->GetName();
		bool flcont = true;
		string variable = "_10";
		//if ( string::npos == nn.find("CutFlowUnW")) flcont=false;
		//if (string::npos == nn.find("hDZeta_19") ) flcont=false;
		if (string::npos == nn.find(variable) ) flcont=false;
		if (!flcont) continue;
		if (obj->IsA ()->InheritsFrom ("TTree") ) continue;
		if (obj->IsA ()->InheritsFrom ("TH2") ) continue;
		if (obj->IsA ()->InheritsFrom ("TH1D") ) {
			// descendant of TH1D-> prepare the histograms to be superimposed

			TH1D* hh[500];
			TH1D* hsignal[500];
			TH1D* h1 = (TH1D*) obj;
			if (h1->Integral() <0.000001) continue;
			TLegend *legend_c1 = new TLegend (0.3, 0.9, 0.9, 0.55);
			TLegend *legend_c2 = new TLegend (0.25, 0.95, 0.45, 0.8);
			legend_c1->SetFillColor(1);
			legend_c1->SetFillStyle(0);
			legend_c1->SetLineColor(0);
			legend_c1->SetTextFont (132);
			legend_c1->SetTextSize (0.035);
			legend_c2->SetFillColor(1);
			legend_c2->SetFillStyle(0);
			legend_c2->SetLineColor(0);
			legend_c2->SetTextFont (132);
			legend_c2->SetTextSize (0.035);
			legend_c1->SetNColumns(3);

			//if (!full)
			// h1->GetXaxis()->SetRange(h1->FindFirstBinAbove(0),h1->FindLastBinAbove(5));	
			//if (full) h1->GetXaxis()->SetRange(h1->FindFirstBinAbove(0),h1->GetNbinsX());	

			ModifyHist (h1,1,Lumi,lumiweights[0],titles[0],norm_);

			h1->Scale(12000/2320);

			//if (! h1->Integral() >0 ) continue;

			// loop over all source files and modify the correspondant
			// histogram to the one pointed to by "h1"
			TFile *nextsource = (TFile *) sourcelist->After (first_source);

			int cl, countsignal;
			h1->SetStats(000000);
			h1->SetLineWidth(5);
			cl=1;
			countsignal=1;

			hh[cl]=h1;

			THStack *hs = new THStack(h1->GetName(),h1->GetTitle());


			// QCD DY WJets TTJets
			string n1,n2,n3,n4,fname,sn,sdata,st1,st2,st3,st4,st5,st6,wj,wj1,dy1,dy2,tt,qcd, st_t, st_s, st_tw_t, st_tw_a,qcd1,qcd2,qcd3,qcd4,qcd5,qcd6,qcd7,qcd8,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,ttx1,ttx2,ttx3,ttx4,tx1,tx2,tx3,tx4;
			string st50,st60,st70,st80,st90,st100;
			string sdata = "Single";
			string sn = "stau";
			string cc1="C1";
			qcd="DataDriven";
			r1="WWTo2L2Nu" ;
			r2="WWZ";
			r3="WZJets";
			r4="WZZ";
			r5="ZZTo2L2Q";
			r6="TTWJetsToLept" ;
			r7="TTWJetsToQQ" ;
			r8="TTZToQQ"  ;
			r9="ZZTo2L2Nu"  ;
			r10="WWToLNuQQ";
			r11="WZTo1L1Nu2Q";
			r12="WZTo1L3Nu";
			r13="WZTo2L2Q";
			r14="WZTo3LNu";
			r15="ZZTo2L2Nu";
			r16="ZZTo2Q2Nu";
			r17="ZZTo4L";

			ttx1="tZqToLL";
			ttx2="tZqToNuNu";
			ttx3="tGJets";
			ttx4="TTGJets";


			wj="WJetsToLNu";
			wj1="wJetsToLNu";
			tt="TT_";
			dy1="DYJetsToLL_M-50";
			dy2="DYJetsToLL_M-10to50";
			st_t="ST_t-channel_4f_leptonDecays";
			st_s="ST_s-channel_4f_leptonDecays";
			st_tw_t="ST_tW_top";
			st_tw_a="ST_tW_antitop_5f";
			n1="QCD";n2="DY";n3="WJ",n4="TT", sn="stau";sdata="Single";st1="0.2/";st2="0.5";

			tx1="tGJets";
			tx2="TTGJets";
			tx3="tZqToLL";
			tx4="tZqToNuNu";


			qcd1="QCD_HT100to200" ;//275kMagenta+2000
			qcd2="QCD_HT200to300" ;//1735000
			qcd3="QCD_HT300to500" ;//367000
			qcd4="QCD_HT500to700" ;//29kMagenta+20
			qcd5="QCD_HT700to1000" ;//6524

			qcd6="QCD_HT1000to1500" ;//1064
			qcd7="QCD_HT1500to2000" ;//121.5
			qcd8="QCD_HT2000toInf" ;//25.kMagenta+2
			

			while (nextsource) {
	
			fname= nextsource->GetName();


					bool flagg= false;

					if (std::string::npos != fname.find(sn) || std::string::npos != fname.find(cc1) || std::string::npos != fname.find(sdata)    ) 	flagg=true;
				
					//if (flagg) cout<<"=============================================================== "<<fname<<endl;
					// make sure we are at the correct directory level by cd'ing to path
					nextsource->cd("mutau");
					TH1D* eventCountt = (TH1D*)nextsource->Get("mutau/histWeightsH");
					//TH1D* eventCountt = (TH1D*)nextsource->Get("mutau/inputEventsH");

					TH1D* hxsecc = (TH1D*)nextsource->Get("mutau/xsec");
					//float xsecc = hxsecc->GetMean();
					float xsecc = xsecs[cl];
					//cout<< " XSEC CHECK  "<<xsecc<<"  "<<fname<<"  "<<cl<<"  "<<xsecs.size()<<endl;

					float nGenn = eventCountt->GetSumOfWeights();

					float normm = float(xsecc*Lumi) / float(nGenn)  ;


					if (std::string::npos != fname.find(qcd)) { xsecc=1;normm =1.;}
				//	cout<<"  the weighting "<<xsecc<<"  "<<Lumi<< " "<<normm<<"  "<<fname<<"  "<<endl;

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
						if (!full) {
						h2->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(5));	
						}
						if (full) h2->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());	
						
						if (std::string::npos != fname.find(cc1) || std::string::npos != fname.find(sn)  )  hsignal[cl-2]= h2;
						else{ 
						hh[cl] = h2;}

						if (cl==2){
							allbkg  = (TH1D*) h2->Clone();
							allbkg->Reset();
							htt  = (TH1D*) h2->Clone();
							httx  = (TH1D*) h2->Clone();
							hstop  = (TH1D*) h2->Clone();
							hwj  = (TH1D*) h2->Clone();
							hdyj  = (TH1D*) h2->Clone();
							hrare  = (TH1D*) h2->Clone();
							hdib  = (TH1D*) h2->Clone();
							hqcd  = (TH1D*) h2->Clone();

							htt->Reset();
							httx->Reset();
							hstop->Reset();
							hdyj->Reset();
							hwj->Reset();
							hrare->Reset();
							hdib->Reset();
							hqcd->Reset();


						}

						//				cout<< " for "<<fname<<"  "<<count<<" file, there xsec is "<<xsecc<<" SuOfWeights "<<nGenn<<" Lumi "<<Lumi<<" lumiweight "<<lumiweights[cl-1]<<" weight "<<float(xsecc*Lumi/nGenn)<<"  norm "<<normm<<" cl "<<cl<<"  "<<h2->Integral()<<endl;
						//cout<< " for "<<fname<<" file, there xsec is "<<xsecc<<" SuOfWeights "<<"  "<<h2->Integral()<<" Lumi "<<Lumi<<" lumiweight "<<lumiweights[cl-1]<<" weight "<<float(xsecc*Lumi/nGenn)<<endl;
						//if (std::string::npos == fname.find(sn) )

						if (std::string::npos != fname.find(sn) || std::string::npos != fname.find(cc1) || std::string::npos != fname.find(sdata)    )
							flagg=true;

						//cout<<" will add histogram "<<h2->GetName()<< " for "<<titles[cl-1]<<"  "<<fname<<"  cl  "<<cl-1<<"  "<<countsignal-1<<endl;
						//}

						string  hn_ = obj->GetName();

						//if( string::npos != hn_.find("CutFlowUn"))
						//if( string::npos == hn_.compare("MET_14"))
						if(  hn_ == variable.c_str())
						{
							cout<<"  "<<fname<<endl;
							if (std::string::npos != fname.find(tt) ) { htt->Add(h2); htt->SetLineColor(h2->GetLineColor());};

							if (std::string::npos != fname.find(wj) || string::npos != fname.find(wj1) ) {hwj->Add(h2); hwj->SetLineColor(h2->GetLineColor());};

							if (std::string::npos != fname.find(dy1) || string::npos != fname.find(dy2)) {hdyj->Add(h2); hdyj->SetLineColor(h2->GetLineColor());};

							if ( string::npos != fname.find(st_t) || string::npos != fname.find(st_s) || string::npos != fname.find(st_tw_t) || string::npos != fname.find(st_tw_a)) 
							{hstop->Add(h2);hstop->SetLineColor(h2->GetLineColor());};

							if ( string::npos != fname.find(r1) || string::npos != fname.find(r2) || string::npos != fname.find(r3) || string::npos != fname.find(r4)  
									|| string::npos != fname.find(r5)  || string::npos != fname.find(r9)  || string::npos != fname.find(r10)  
									|| string::npos != fname.find(r11)  || string::npos != fname.find(r12)
									|| string::npos != fname.find(r13)  || string::npos != fname.find(r14)  || string::npos != fname.find(r15)  || string::npos != fname.find(r16)  || string::npos != fname.find(r17)) 
							{ hdib->Add(h2); hdib->SetLineColor(h2->GetLineColor());};

							if ( string::npos != fname.find(r6) || string::npos != fname.find(r7) || string::npos != fname.find(r8)  || string::npos != fname.find(ttx1)  
									|| string::npos != fname.find(ttx2) || string::npos != fname.find(ttx3)   || string::npos != fname.find(ttx4)) 
							{ httx->Add(h2);   httx->SetLineColor(h2->GetLineColor());};

							if (std::string::npos != fname.find(qcd) ) { hqcd->Add(h2); hqcd->SetLineColor(h2->GetLineColor());};

						}




						if (!flagg)
						{
							//cout<<" will add histogram "<<h2->GetName()<< " for "<<titles[cl-1]<<"  "<<fname<<"  cl  "<<cl<<endl;
							hs->Add(h2);
							allbkg->Add(h2);
						}

				}

				nextsource = (TFile *) sourcelist->After (nextsource);
			}				// while ( nextsource )
		}

		if (obj) {
			target->cd ();
			//legend_c1->SetNColumns(3);

			TPad *pad1 = new TPad("pad1","pad1",0,0.2,1,1);//ratio
			//TPad *pad1 = new TPad("pad1","pad1",0,0.0,1,1);
			TPad *pad1r = new TPad("pad1","pad1",0.5,0.25,1,1);

			TPad *pad2 = new TPad("pad2","pad2",0, 0,0.001,0.001);
			TPad *pad2s = new TPad("pad2s","pad2s",0, 0., 1,0.2);



			pad1->SetBottomMargin(0.00);
			pad1->SetRightMargin(0.05);
			//pad1->SetGridy();
			pad1r->SetBottomMargin(0.07);
			pad1r->SetRightMargin(0.05);
			pad1r->SetGridy();

			pad2->SetBottomMargin(0.05);
			pad2->SetTopMargin(0);
			pad2->SetBottomMargin(0.25);
			pad2->SetRightMargin(0.05);

			pad2s->SetBottomMargin(0.01);
			pad2s->SetTopMargin(0);
			pad2s->SetBottomMargin(0.25);
			pad2s->SetRightMargin(0.05);


			//hs->Draw("nostack");
			c1->cd();


			c1->Clear();
			pad1->SetGridx();
			pad1->Draw();
			//pad1r->Draw();
			//pad2->Draw();

			pad2->SetGridy(1);
			pad2s->SetGridy(1);
			pad2s->Draw();

			pad1->cd();
			pad1->Clear();


			TH1D *hsum = ((TH1D*)(hs->GetStack()->Last())); // the "SUM"
			//if (hsum->GetMinimum()>0)
			pad1->SetLogy();
			if (!full) {
			hsum->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(5));	
			OverFlow(hsum,hh[1]->FindLastBinAbove(5));
			}
			if (full) hsum->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());	

			char namee[100];
			sprintf(namee,"%s",key->GetName ());
			char nnn[100];
			sprintf(nnn,"Entries  / %d GeV",hh[1]->GetBinWidth(1));

			hsum->GetYaxis()->SetTitle("Events");
			cout<<" events................. "<<hsum->Integral()<<"  "<<hsum->GetName()<<"  "<<hsum->GetTitle()<<" bkg "<<allbkg->Integral()<<endl;

			//hh[1]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[titles.size()-1]->FindLastBinAbove(5));
			 if (!full) 
			 {
                         hh[1]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(5));
			 OverFlow(hh[1],hh[1]->FindLastBinAbove(5));
			 }
			 if (full) hh[1]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());
			
			if (cl=1){
				TH1F* v1 = new TH1F("", "", 1, 0, 1);v1->SetLineWidth(4);
				TH1F* v2 = new TH1F("", "", 1, 0, 1);v2->SetLineWidth(4);
				TH1F* v3 = new TH1F("", "", 1, 0, 1);v3->SetLineWidth(4);
				TH1F* v4 = new TH1F("", "", 1, 0, 1);v4->SetLineWidth(4);
				TH1F* v5 = new TH1F("", "", 1, 0, 1);v5->SetLineWidth(4);
				TH1F* v6 = new TH1F("", "", 1, 0, 1);v6->SetLineWidth(4);
				TH1F* v7 = new TH1F("", "", 1, 0, 1);v7->SetLineWidth(4);
				TH1F* v8 = new TH1F("", "", 1, 0, 1);v8->SetLineWidth(4);
				TH1F* v9 = new TH1F("", "", 1, 0, 1);v9->SetLineWidth(4);
				TH1F* v10 = new TH1F("", "", 1, 0, 1);v10->SetLineWidth(4);
				v9->SetMarkerSize(0.4);
				v9->SetMarkerColor(49);
				v1->SetMarkerSize(0.4);

				char lumitag[100];
				sprintf(lumitag,"Projected #int L = %.3g fb^{-1}",Lumi/1000);
				//v1->SetLineColor(kBlack);legend_c1->AddEntry(hh[1], lumitag, "LEP");
				char lab_[100];
				v5->SetLineColor(kBlack);legend_c1->AddEntry(v5, "Bkg", "f");
				legend_c1->AddEntry(hsignal[0], "C1C1(100,1)", "LEP");
				legend_c1->AddEntry(hsignal[1], "C1C1(150,1)", "LEP");
				legend_c1->AddEntry(hsignal[2], "C1C1(200,1)", "LEP");
				legend_c1->AddEntry(hsignal[3], "C1C1(250,1)", "LEP");
				legend_c1->AddEntry(hsignal[4], "C1C1(300,1)", "LEP");
				legend_c1->AddEntry(hsignal[5], "C1C1(350,1)", "LEP");
				legend_c1->AddEntry(hsignal[6], "C1C1(400,1)", "LEP");
				legend_c1->AddEntry(hsignal[7], "C1N2(100,1)", "LEP");
				legend_c1->AddEntry(hsignal[8], "C1N2(150,1)", "LEP");
				legend_c1->AddEntry(hsignal[9], "C1N2(200,1)", "LEP");
				legend_c1->AddEntry(hsignal[10], "C1N2(250,1)", "LEP");
				legend_c1->AddEntry(hsignal[11], "C1N2(300,1)", "LEP");
				legend_c1->AddEntry(hsignal[12], "C1N2(350,1)", "LEP");
				legend_c1->AddEntry(hsignal[13], "C1N2(400,1)", "LEP");

				//v5->SetLineColor(kPink);legend_c1->AddEntry(v5, "WJets", "l");

				//v6->SetLineColor(60);legend_c1->AddEntry(v6, "TTJets", "l");
				//v2->SetLineColor(kYellow-7);legend_c1->AddEntry(v2, "QCD", "l");
				//v8->SetLineColor(kTeal+9);legend_c1->AddEntry(v8, "DYJets", "l");
				//v4->SetLineColor(kAzure+10);legend_c1->AddEntry(v4, "SingleTop", "l");
				//v3->SetLineColor(kMagenta+2);legend_c1->AddEntry(v3, "VV/VVV", "l");
				//v7->SetLineColor(kOrange+2);legend_c1->AddEntry(v7, "TTX/TG", "l");


				sprintf(lab_,"bkg,(%.2f)",hsum->Integral());
				//v5->SetLineColor(kRed-5);legend_c2->AddEntry(hsum, lab_, "l");
				sprintf(lab_,"data,(%.2f)",hh[1]->Integral());
				v1->SetLineColor(kBlack);legend_c2->AddEntry(hh[1], lab_, "l");
			}
			//	cout<<"  Total event from bkg  "<<counter[0]<<"   "<<hh[1]->Integral()<<endl;
			hsum->SetMaximum(20*hs->GetMaximum());
			hsum->SetMinimum(0.1);
			if (norm_) {
			hsum->Scale(1/hsum->Integral()); hsum->SetFillColor(0);hsum->SetLineColor(kRed);
			}
			hsum->SetMaximum(50*hs->GetMaximum());
			hsum->SetMinimum(1);
			hsum->SetFillColor(0);
			hsum->SetLineColor(kBlack);
			//ReBinn(hsum);
			hsum->Draw("hist");

			//if (!norm_)

			//hs->Draw("same hist");

			//hh[1]->Draw("same ep hist");
			//hh[1]->SetMarkerStyle(20);
			//hh[1]->SetFillColor(0);
			//if (norm_) hh[1]->Scale(1/hh[1]->Integral());

			for (int ij=0;ij<14;ij++){
			if (!full) {
				hsignal[ij]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(5));
				OverFlow(hsignal[ij],hh[1]->FindLastBinAbove(5));
			}
			if (full)hsignal[ij]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());
				if (norm_) hh[ij]->Scale(1/hh[ij]->Integral());
				hsignal[ij]->SetFillColor(0);
				hsignal[ij]->SetMarkerSize(0.025);
				hsignal[ij]->Draw("same e1p hist");
				//ij++;
			}

			string Title = hh[1]->GetName();

			//c1->cd();
			legend_c1->Draw("sames");
			//legend_c2->Draw("sames");
			c1->SetFillColor(0);
			c1->SetBorderMode(0);
			c1->SetBorderSize(0);
			c1->SetFrameBorderMode(0);
			c1->SetBorderSize(0);
			pad1->SetFrameLineColor(0);;
			pad1r->SetFrameLineColor(0);;


			pad2s->cd();
			for (int ij=0;ij<14;ij++){
				//hh[ij]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());
				sig = (TH1D*) hsignal[ij]->Clone();
				htest = (TH1D*) hsum->Clone();
				htest ->Add(hsignal[ij],1);
				for (int nb = 0;nb < htest->GetNbinsX()+1;nb++) {
					//if (htest->GetBinContent(nb)>0);
					htest->SetBinContent(nb,sqrt(htest->GetBinContent(nb)));

					//if (htest->GetBinContent(nb)<0.000000001);
					//	htest->SetBinContent(nb,0.000000001);
				}
				//htest->Sumw2();
				sig->Divide(htest);
				sig->SetMarkerStyle(7);
				sig->Draw("same  hist lp");
				sig->SetMarkerStyle(7);
				sig->SetMaximum( 0.5 );
				sig->SetMinimum(0.01);
				sig->GetXaxis()->SetTitle(hh[1]->GetXaxis()->GetTitle());
				sig->GetYaxis()->SetTitle("");
				sig->SetTitleSize(0);
				sig->SetMarkerSize(0.08);
				//sig->SetMarkerColor(39);
				//sig->SetLineColor(39);
				sig->SetLineWidth(2);
				sig->GetYaxis()->SetNdivisions(5);

				sig->GetXaxis()->SetNdivisions(545);
				sig->GetXaxis()->SetLabelSize(0.15);
				sig->GetXaxis()->SetTitleSize(0.12);
				sig->GetXaxis()->SetTitleOffset(0.85);

				sig->GetYaxis()->SetLabelSize(0.1);
				sig->GetYaxis()->SetLabelSize(0.15);
				sig->GetYaxis()->SetTitleSize(0.12);
				sig->GetYaxis()->SetTitleOffset(0.25);
				sig->GetYaxis()->SetTitle("Significance");


				sig->SetTitleFont(62);
				//ratio->GetXaxis()->SetRange(ratio->FindFirstBinAbove(0),ratio->FindLastBinAbove(5));
				if (!full)sig->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(5));
				if (full) sig->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());
				//ratio->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());

				sig->GetXaxis()->SetNdivisions(510);
				sig->SetTitle("");
			}

			pad2->cd();
			ratio = (TH1D*) hh[1]->Clone();
			string nT = hh[1]->GetName();
			if (std::string::npos != nT.find("CutFlowUnW"))
				ratio->Sumw2();
			ratio->SetStats(000000);
			ratio->Divide(hsum);
			ratio->SetMarkerStyle(7);
			ratio->SetMaximum( 2.2 );
			ratio->SetMinimum(0.2);
			ratio->GetXaxis()->SetTitle(hh[1]->GetXaxis()->GetTitle());
			ratio->GetYaxis()->SetTitle("");
			ratio->SetTitleSize(0);
			ratio->SetMarkerSize(0.05);
			ratio->SetMarkerColor(39);
			ratio->SetLineColor(39);
			ratio->SetLineWidth(2);
			ratio->GetYaxis()->SetNdivisions(5);

			ratio->GetXaxis()->SetNdivisions(545);
			ratio->GetXaxis()->SetLabelSize(0.15);
			ratio->GetXaxis()->SetTitleSize(0.12);
			ratio->GetXaxis()->SetTitleOffset(0.85);

			ratio->GetYaxis()->SetLabelSize(0.1);
			ratio->GetYaxis()->SetLabelSize(0.15);
			ratio->GetYaxis()->SetTitleSize(0.12);
			ratio->GetYaxis()->SetTitleOffset(0.25);
			ratio->GetYaxis()->SetTitle("Data / MC");


			ratio->SetTitleFont(62);
			//ratio->GetXaxis()->SetRange(ratio->FindFirstBinAbove(0),ratio->FindLastBinAbove(5));
			ratio->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(5));

			//ratio->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());

			ratio->GetXaxis()->SetNdivisions(510);
			ratio->SetTitle("");
			TAxis *axis = hh[1]->GetXaxis();
			float halfbin = axis->GetBinWidth(hh[1]->GetBin(1))*0.5;
			//cout<<" halfbin  "<<halfbin
			//  TLine *l=new TLine(axis->GetBinLowEdge(hh[1]->FindFirstBinAbove(0.)),1,axis->GetBinWidth(hh[1]->GetBin(1))*hh[1]->GetNbinsX() - halfbin,1);
			TLine *l=new TLine(axis->GetBinLowEdge(hh[1]->FindFirstBinAbove(0.)),1,axis->GetBinLowEdge(hh[1]->FindLastBinAbove(5)+1),1);
			//   cout<<"  ================= > "<< hh[1]->GetBinContent(hh[1]->FindLastBinAbove(0.0))<<"    "<<hh[1]->FindLastBinAbove(float(0.0))<<endl;
			l->SetLineColor(kRed);
			l->SetLineWidth(2);
			ratio->SetLineColor(kBlack);
			ratio->SetFillColor(17);
			ratio->SetFillColor(kBlack);
			bkgRatioErrH  = (TH1D*) ratio->Clone();
			DataHErrP  = (TH1D*) hh[1]->Clone();
			DataHErrM  = (TH1D*) hh[1]->Clone();
			//bkgRatioErrH =(TH1D*) bkgRatioErrH->Clone("hh[1]");
			//bkgRatioErrH->Reset();
			bkgRatioErrH->SetLineColor(kBlack);
			bkgRatioErrH->SetFillStyle(3013);
			bkgRatioErrH->SetFillColor(1);
			bkgRatioErrH->SetMarkerStyle(21);
			bkgRatioErrH->SetMarkerSize(0);
			bkgRatioErrH->SetLineColor(1);
			bkgRatioErrH->SetLineWidth(2);

			//hh[1]->Sumw2();
			//allbkg->Sumw2();
			for (int iB=1; iB<=allbkg->GetNbinsX(); ++iB) {
				float datX = hh[1]->GetBinContent(iB);
				float datE = hh[1]->GetBinError(iB);
				float bkgX = allbkg->GetBinContent(iB);
				float bkgE = allbkg->GetBinError(iB);
				//if (bkgX>0)
				//    cout<<" bin  "<<iB<<" error "<<bkgE<<" Content  "<<bkgX<<" rel "<<float(bkgE/bkgX)<<" data content  "<<datX<<" data error "<<datE<<endl;
				float datRatioX = datX/bkgX;
				float datRatioE = datE/bkgX;
				float bkgErr = float(bkgE / bkgX);
				bkgRatioErrH->SetBinContent(iB,1);
				bkgRatioErrH->SetBinError(iB,bkgErr);
				ratio->SetBinError(iB,datE/bkgX);
				DataHErrP->SetBinContent(iB,datX);
				DataHErrP->SetBinError(iB,datE);
				DataHErrM->SetBinContent(iB,bkgX);
				DataHErrM->SetBinError(iB,bkgE);

			}

			ratio->Draw("ep ");
			bkgRatioErrH->Draw("e2 same");
			l->Draw("same");

			/*  pad1->cd();
			//pad1->Clear();
			DataHErrP->Sumw2();
			DataHErrP->SetFillColor(1);
			DataHErrP->SetLineColor(1);
			DataHErrP->SetFillStyle(2013);
			DataHErrP->SetMarkerStyle(21);
			DataHErrP->SetMarkerSize(0);

			DataHErrM->SetLineColor(2);
			DataHErrM->SetFillColor(2);
			DataHErrM->SetFillStyle(3013);
			DataHErrM->SetMarkerStyle(22);
			DataHErrM->SetMarkerSize(0);

			DataHErrP->Draw("e2 same");
			DataHErrM->Draw("e2 same");

			hh[1]->Draw("e1same");
			*/
			//c1->SetTitle(namee);
			gPad->RedrawAxis();
			gPad->Modified();
			gPad->Update();
			pad1->cd();
			char lat[100];
			string str_stripped = c1->GetTitle();
			str_stripped.resize (str_stripped.size () - 3);
			sprintf(lat,"%s",str_stripped);
			tex = new TLatex(0.45,0.96,lat);
			tex->SetLineWidth(2);
			tex->SetTextSize(0.035);
			c1->cd();
		        //tex->Draw();
 		        pad1->Modified();
        		c1->cd();
        		c1->Modified();

			c1->Write (namee);


			char f[100];char ff[100];
			if (!norm_)sprintf(f,"TauZeroLSPC1/%s.pdf",namee);
			else sprintf(f,"TauZeroLSPC1/%s_Norm.pdf",namee);

			if (!norm_)sprintf(ff,"TauZeroLSPC1/%s_Log.pdf",namee);
			else sprintf(ff,"TauZeroLSPC1/%s_Log_Norm.pdf",namee);

			//if (!norm_)sprintf(f,"TauZeroLSPC1/%s.pdf",namee);

			//TH1D* ht;
			// ht = (TH1D*)c1->GetPrimitive(namee);
			//c1->cd();
			//c1->Modified();
			//c1->cd();
			//c1->Update();
			c1->Print (f,"pdf");

			///////// TPie
			Float_t vals[]={hdib->Integral()+httx->Integral(),htt->Integral()+hstop->Integral(),hwj->Integral(),hdyj->Integral(),hqcd->Integral()};

			string nan_ = key->GetName ();
			int nvals = 5;
			//if (std::string::npos != nan_.find("CutFlowUnW") ){
			/*if (   nan_ == "_19") {
			  cout<<" Found it here  "<<nan_<<"   "<<key->GetName()<<endl;
			//Int_t nvals = sizeof(counter)/sizeof(counter[0]);
			//cout<<"  vals ============== "<<vals[0]<<"  "<<vals[1]<<"  "<<vals[2]<<"  "<<vals[3]<<"  "<<vals[4]<<"   "<<endl;
			cout<<" VV + TTX  "<<hdib->Integral()+httx->Integral()<<" TT+ST "<<htt->Integral()+hstop->Integral()<<" WJ "<<hwj->Integral()<<" DY "<<hdyj->Integral()<<" TTX "<<httx->Integral()<<" QCD "<<hqcd->Integral()<<endl;

			Int_t colors[] = {hdib->GetLineColor(),htt->GetLineColor(),hwj->GetLineColor(),hdyj->GetLineColor(),hqcd->GetLineColor()};
			TPie *pie3 = new TPie("pie3","Pie with tangential labels",nvals,vals,colors);

			TCanvas *cpie = new TCanvas("cpie","TPie test",1200,1200);
			cpie->cd();
			pie3->SetRadius(.2);
			pie3->SetLabelsOffset(.015);
			//pie3->SetLabelsSize(.005);
			//	for (int j=0;j<7;j++) cout<<" VALUES         ======================================="<<  vals[j]<<"   "<<counter[j]<<endl;
			pie3->SetLabelFormat("%txt - (%perc)");
			pie3->SetTextAngle(0.45);
			pie3->SetTextSize(0.04);
			//pie3->SetLabelFormat("#splitline{%val} {(%perc)}");
			//pie3->SetFractionFormat("2.1f");

			//pie3->Draw("pol <");
			//pie3->GetSlice(0)->SetTitle("Data");
			//pie3->GetSlice(1)->SetTitle("Bkg");


			char lumitag[100];
			sprintf(lumitag,"Data #int L = %.3g fb^{-1}",Lumi/1000);
			//pie3->GetSlice(0)->SetTitle(lumitag);
			pie3->GetSlice(0)->SetTitle("Rare");
			pie3->GetSlice(1)->SetTitle("t#bar{t}+SingleT");
			pie3->GetSlice(2)->SetTitle("WJets");
			pie3->GetSlice(3)->SetTitle("DYJets");
			//pie3->GetSlice(4)->SetTitle("sT");
			//pie3->GetSlice(4)->SetTitle("ttx");
			pie3->GetSlice(4)->SetTitle("QCD");
			//pie3->SetEntryRadiusOffset(2,.05);
			pie3->Draw("nol <");
			pie3->Draw("rsc");
			//pie3->Draw("3d");
			cpie->SaveAs("TauZeroLSPC1/APie.pdf");

			}
			*/
			string n = hh[1]->GetName();
			//const char *s1;
			string s1;
			float scale = 1;//float(Lumi/2320);
			if (std::string::npos != n.find(variable))
			{
			smFile->cd();
            
			

			//NPfile->Close();


				allbkg = hsum;
				//ReBinn(allbkg);
				allbkg->SetMinimum(1);
				allbkg->SetLineColor(kRed);
				allbkg->SetMarkerColor(kRed);
				allbkg->SetFillColor(kRed);
				allbkg->SetFillStyle(3011);
				s1 = "allbkg_" + variable;
				allbkg->SetName(s1.c_str());
				allbkg->Scale(scale);
				allbkg->Write();
				htt->Scale(scale);
				hwj->Scale(scale);
				hdyj->Scale(scale);
				hstop->Scale(scale);
				hdib->Scale(scale);
				hqcd->Scale(scale);
				httx->Scale(scale);
				if (!full){
				OverFlow(htt,hh[1]->FindLastBinAbove(5));
				OverFlow(hwj,hh[1]->FindLastBinAbove(5));
				OverFlow(hdyj,hh[1]->FindLastBinAbove(5));
				OverFlow(hstop,hh[1]->FindLastBinAbove(5));
				OverFlow(hdib,hh[1]->FindLastBinAbove(5));
				OverFlow(httx,hh[1]->FindLastBinAbove(5));
				OverFlow(hqcd,hh[1]->FindLastBinAbove(5));
				}

				htt->SetMinimum(1);
				hdyj->SetMinimum(1);
				hwj->SetMinimum(1);
				httx->SetMinimum(1);
				hstop->SetMinimum(1);
				hdib->SetMinimum(1);
				hqcd->SetMinimum(1);
				s1 = "tt_" + variable;
				htt->SetName(s1.c_str());
				htt->Write();

				s1 = "wj_" + variable;
				hwj->SetName(s1.c_str());
				hwj->Write();

				s1 = "dyj_" + variable;
				hdyj->SetName(s1.c_str());
				hdyj->Write();

				s1 = "sT_" + variable;
				hstop->SetName(s1.c_str());
				hstop->Write();

				s1 = "dib_" + variable;
				hdib->SetName(s1.c_str());
				hdib->Write();

				s1 = "ttx_" + variable;
				httx->SetName(s1.c_str());
				httx->Write();

				s1 = "qcd_" + variable;
				hqcd->SetName(s1.c_str());
				hqcd->Write();

				hh[1]->SetMinimum(1);
				hh[1]->SetLineColor(kBlack);
				hh[1]->SetFillColor(kBlack);
				hh[1]->SetMarkerColor(kBlack);
				//hh[1] = allbkg;
				s1 = "data_obs";
				hh[1]->SetName(s1.c_str());
				//hh[1]->Scale(scale);
				hh[1]->Write();
				//hh[2]->SetName("signal");
				//hh[2]->Write();

			for (unsigned int nm=0;nm<signal_names.size();++nm){
			//NPfile->cd();
			//ReBinAxis(hsignal[nm]);
			hsignal[nm]->SetMinimum(1);
			hsignal[nm]->SetLineColor(kBlue);
			hsignal[nm]->SetFillColor(0);
			//string str_stripped = signal_names[nn];
			//str_stripped.resize (str_stripped.size () - 9);
			//sprintf(signname,"%s_%s",signal_names[nm].c_str(),variable.c_str());
			string signname = signal_names[nm] + "_" + variable;
			hsignal[nm]->SetName(signname.c_str());
			//cout<<"  some xsecs "<<xsecs[nm+1]<<endl;
			//hsignal[nm]->Scale(1/xsecs[nm+1]);
			if (!full) OverFlow(hsignal[nm],hh[1]->FindLastBinAbove(5));
			hsignal[nm]->Write();
			
			}

			}

		}

		} 			// while ( ( TKey *key = (TKey*)nextkey() ) )
		delete c1;
		/*
		   char nnn[100];
		   for (unsigned int t=0;t<signal_names.size();t++){

		   TFile np (signal_names[t].c_str(), "RECREATE");
		   cout<<" will now write "<<signal_names[t].c_str()<<endl;
		   np.cd();
		//hsignal[1][t]->Write();
		}

*/
		// save modifications to target file
		target->SaveSelf (kTRUE);
		TH1::AddDirectory (status);
		cout << "	" << "========================================================" << endl;
		cout<< " Ended SuperImpose of files.... " <<endl;

		// for (int i=0;i<SValueVariables_.size();i++){
		//cout<<SValueVariables_[i].second<<endl;}



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

			if (h->GetNbinsX()>20 && nbins%2==0) nn=2;
			if (h->GetNbinsX()>20 && nbins%3==0) nn=3;
			//if (h->GetNbinsX()>40 && nbins%4==0) nn=4;
			//h->Rebin(nn);
			//h->Sumw2();







			h->SetMinimum(1);
			h->GetXaxis()->SetNdivisions(512);
			string titlee=h->GetName();
			int col=;//kOrange;
			string title1,title2;
			title1= h->GetTitle();
			//    if(title_.find("Data") == 0) col= kBlack;//TT
			//    if(title_.find("Stau") == 0) col= kBlack;//TT


			if (std::string::npos != title_.find("Data") || std::string::npos != title_.find("Single")  )  {
				//if ( std::string::npos != title_.find("StauA") ){

				col=kBlack ;
				h->SetLineStyle(1);
				h->SetMarkerStyle(20+cl_);
				h->SetMarkerSize(0.2);
				h->SetMarkerColor(col);
				h->SetLineColor(col);
			}


			if ( std::string::npos != title_.find("tau") || std::string::npos != title_.find("C1") ){

				//col=kBlue-10 + cl_;
				if (string::npos != title_.find("C1C1")) col = cl_;
				if (string::npos != title_.find("C1N2")) col = 31+cl_;
				//col=cl_;
				//if (cl_>9) col=20+cl_;
				h->SetLineStyle(1);
				h->SetMarkerStyle(32);
				h->SetMarkerSize(0.1);
				h->SetMarkerColor(col);
				h->SetLineColor(col);
				h->SetLineStyle(7);
			}


			//h->SetLineWidth(2);
			int nb = h->GetNbinsX();
			float over_ = h->GetBinContent(nb+1);
			float contlast = h->GetBinContent(nb);
			//h->SetBinContent(nb,contlast+over_);
			//if (weight != 1.)

			h->Scale(weight);
			//h->Scale (1/h->Integral());

			//cout<<" scaling to weight  "<<h->GetName()<<"  "<<h->Integral()<<endl;
			//int nbb = h->FindFirstBinBelow(10.);
			/*do
			  {
			  int nbb = h->GetFirstBinBelow(10.)
			  h->Rebin(2)
			  }*/

			//    if (std::string::npos != title_.find("TTV"))  col= 60;

			if (std::string::npos != title_.find("wJets")|| std::string::npos != title_.find("WJetsToLNu"))  { col= kPink;}// counter[0]  =h->Integral() }//cout << " ==============================  "<<h->Integral()<<endl;}
			if (std::string::npos != title_.find("TTJets") || std::string::npos != title_.find("TTPow")) { col= 60; }
			if (std::string::npos != title_.find("QCD"))  {col= kYellow-7; }
			if (std::string::npos != title_.find("DYJets"))  {col= kTeal+9;}
			if (std::string::npos != title_.find("ST_") || std::string::npos != title_.find("channel")  || std::string::npos != title_.find("ST_"))  {col= kAzure+10; }//counter[4] +=h->Integral();}
			if ( td::string::npos != title_.find("WWZ") || std::string::npos != title_.find("WWTo") || std::string::npos != title_.find("ZZ") || std::string::npos != title_.find("ZZTo")|| std::string::npos != title_.find("WZ") || std::string::npos != title_.find("WZZ")) {col=kMagenta+2;}// counter[5] +=h->Integral();}
			if ( std::string::npos != title_.find("TTW") || std::string::npos != title_.find("TTZ") || std::string::npos != title_.find("tZq") || std::string::npos != title_.find("TG") || std::string::npos != title_.find("tG")) {col=kOrange+2; }//counter[6] +=h->Integral();}


			float nm = 0.;nm = float(h->Integral());

			//if ( cl_>3) counter[0] += h->Integral() ;

			//cout<< "  "<<cl_<<"  "<<title_<<endl;

			if (std::string::npos != title1.find("MET"))  h->GetXaxis()->SetTitle("GeV/");
			if (std::string::npos != title1.find("mass"))  h->GetXaxis()->SetTitle("GeV");
			if (std::string::npos != title1.find("Inv"))  h->GetXaxis()->SetTitle("GeV");
			if (std::string::npos != title1.find("Mass"))  h->GetXaxis()->SetTitle("GeV");
			if (std::string::npos != title1.find("met"))  h->GetXaxis()->SetTitle("GeV");
			if (std::string::npos != title1.find("ST"))  h->GetXaxis()->SetTitle("GeV");
			if (std::string::npos != title1.find("HT"))  h->GetXaxis()->SetTitle("GeV");
			if (std::string::npos != title1.find("Jetp"))  h->GetXaxis()->SetTitle("GeV");
			if (std::string::npos != title1.find("Phi"))  h->GetXaxis()->SetTitle("rad");
			if (std::string::npos != title1.find("phi"))  h->GetXaxis()->SetTitle("rad");
			if (std::string::npos != title1.find("dPhi"))  h->GetXaxis()->SetTitle("");
			if (std::string::npos != title1.find("pT"))  h->GetXaxis()->SetTitle("GeV");
			if (std::string::npos != title1.find("nB"))  h->GetXaxis()->SetTitle("B-Jets");
			if (std::string::npos != title1.find("nJ"))  h->GetXaxis()->SetTitle("#Jets");
			if (std::string::npos != title1.find("nL"))  h->GetXaxis()->SetTitle("#Lept");
			if (std::string::npos != title1.find("nmu"))  h->GetXaxis()->SetTitle("#muons");
			if (std::string::npos != title1.find("nel"))  h->GetXaxis()->SetTitle("#el");
			if (std::string::npos != title1.find("eta"))  h->GetXaxis()->SetTitle("");

			h->GetXaxis()->SetTitleOffset(0.8);

			h->GetYaxis()->SetTitleOffset(1.5);

			//h->SetLineColor (col);

			//h->SetFillColor (col);
			h->SetMinimum(1);
			h->SetLineStyle (col);
			//    h->SetFillStyle (3000+cl_);
			// h->SetFillColorAlpha (col,0.9);


			//cout<<" for "<<title_.c_str()<<"  Weight to be applied " <<weight<<"  "<<title1<<"  "<<cl_<<endl;   
			//if (std::string::npos != title1.find("CutFlow")) 
			//if (std::string::npos == title_.find("Single")) 


			h->SetFillColor(col);
			h->SetLineColor(col);





			//cout<<"""""""""""""""""""""""""""""""""""""""""""""""""""""""""" <<h->GetName()<<"  "<<h->GetTitle()<<endl;
			ofstream tfile;
			string n_ = h->GetName();
			//float ev_ = 0;
			if (std::string::npos != n_.find("CutFlowUnW") ){

				//   cout<<" Counting from CutFlow 1 "<<h->Integral()<<endl;
				TString outname=title_;
				TString textfilename = "cutflow_"+outname +".txt";
				tfile.open(textfilename);

				tfile << "########################################" << endl;
				for (int b=0;b<20;b++){
					//ev_ += h->GetBinContent(b);
					//tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<" & "<<" & "<<endl;	
					if (h->GetBinContent(b) > 0. ) tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b) <<endl;	
					else tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<0<<endl;
					//if (b==15) cout<<"  "<<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<endl;
					//cout <<title1<<" & "<<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<" & "<<" & "<<endl;	
				}
				// cout<<" Counting from CutFlow  "<<ev_<<endl;
			}
tfile.close();
//if (norm_)    

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


TCanvas *example_plot(int iPeriod, int iPos , TString name)
{ 
	//  if( iPos==0 ) relPosX = 0.12;

	int W = 800;
	int H = 600;
	// 
	// Simple example of macro: plot with CMS name and lumi text
	//  (this script does not pretend to work in all configurations)
	// iPeriod = 1*(0/1 7 TeV) + 2*(0/1 8 TeV)  + 4*(0/1 13 TeV) 
	// For instance: 
	//               iPeriod = 3 means: 7 TeV + 8 TeV
	//               iPeriod = 7 means: 7 TeV + 8 TeV + 13 TeV 
	// Initiated by: Gautier Hamel de Monchenault (Saclay)
	// Updated by:   Dinko Ferencek (Rutgers)
	//
	int H_ref = 600; 
	int W_ref = 800; 

	// references for T, B, L, R
	float T = 0.08*H_ref;
	float B = 0.12*H_ref; 
	float L = 0.12*W_ref;
	float R = 0.04*W_ref;

	//TString canvName = "FigExample_";
	TString canvName = name;
	canvName += W;
	canvName += "-";
	canvName += H;
	canvName += "_";  
	canvName += iPeriod;
        writeExtraText = true;
	if( writeExtraText ) canvName += "-prelim";
	if( iPos%10==0 ) canvName += "-out";
	else if( iPos%10==1 ) canvName += "-left";
	else if( iPos%10==2 )  canvName += "-center";
	else if( iPos%10==3 )  canvName += "-right";

	TCanvas* canv = new TCanvas(canvName,canvName,50,50,W,H);
	canv->SetFillColor(0);
	canv->SetBorderMode(0);
	canv->SetFrameFillStyle(0);
	canv->SetFrameBorderMode(0);
	canv->SetLeftMargin( L/W );
	canv->SetRightMargin( R/W );
	canv->SetTopMargin( T/H );
	canv->SetBottomMargin( B/H );
	canv->SetTickx(0);
	canv->SetTicky(0);

	TH1* h = new TH1F("h","h",40,70,110);
	h->GetXaxis()->SetNdivisions(6,5,0);
	h->GetXaxis()->SetTitle("m_{e^{+}e^{-}} (GeV)");  
	h->GetYaxis()->SetNdivisions(6,5,0);
	h->GetYaxis()->SetTitleOffset(1);
	h->GetYaxis()->SetTitle("Events / 0.5 GeV");  

	h->SetMaximum( 260 );
	if( iPos==1 ) h->SetMaximum( 300 );
	h->Draw();

	int histLineColor = kOrange+7;
	int histFillColor = kOrange-2;
	float markerSize  = 1.0;

	{
		TLatex latex;

		int n_ = 2;

		float x1_l = 0.92;
		float y1_l = 0.60;

		float dx_l = 0.30;
		float dy_l = 0.18;
		float x0_l = x1_l-dx_l;
		float y0_l = y1_l-dy_l;

		TPad* legend = new TPad("legend_0","legend_0",x0_l,y0_l,x1_l, y1_l );
		//    legend->SetFillColor( kGray );
		legend->Draw();
		legend->cd();

		float ar_l = dy_l/dx_l;

		float x_l[1];
		float ex_l[1];
		float y_l[1];
		float ey_l[1];

		//    float gap_ = 0.09/ar_l;
		float gap_ = 1./(n_+1);

		float bwx_ = 0.12;
		float bwy_ = gap_/1.5;

		x_l[0] = 1.2*bwx_;
		//    y_l[0] = 1-(1-0.10)/ar_l;
		y_l[0] = 1-gap_;
		ex_l[0] = 0;
		ey_l[0] = 0.04/ar_l;

		TGraph* gr_l = new TGraphErrors(1, x_l, y_l, ex_l, ey_l );

		gStyle->SetEndErrorSize(0);
		gr_l->SetMarkerSize(0.9);
		gr_l->Draw("0P");

		latex.SetTextFont(40);
		latex.SetTextAngle(0);
		latex.SetTextColor(kBlack);    
		latex.SetTextSize(0.25);    
		latex.SetTextAlign(12); 

		TLine line_;
		TBox  box_;
		float xx_ = x_l[0];
		float yy_ = y_l[0];
		latex.DrawLatex(xx_+1.*bwx_,yy_,"Data");

		yy_ -= gap_;
		box_.SetLineStyle( kSolid );
		box_.SetLineWidth( 1 );
		//		box_.SetLineColor( kBlack );
		box_.SetLineColor( histLineColor );
		box_.SetFillColor( histFillColor );
		box_.DrawBox( xx_-bwx_/2, yy_-bwy_/2, xx_+bwx_/2, yy_+bwy_/2 );
		box_.SetFillStyle(0);
		box_.DrawBox( xx_-bwx_/2, yy_-bwy_/2, xx_+bwx_/2, yy_+bwy_/2 );
		latex.DrawLatex(xx_+1.*bwx_,yy_,"Z #rightarrow e^{+}e^{-} (MC)");

		canv->cd();
	}
/*
	{
		// Observed data
		TFile file_("histo.root","READ");

		TH1F *data = static_cast<TH1F*>(file_.Get("data")->Clone());
		data->SetDirectory(0);
		data->SetMarkerStyle(20);
		data->SetMarkerSize(markerSize);

		TH1F *MC   = static_cast<TH1F*>(file_.Get("MC")->Clone());
		MC->SetDirectory(0);
		MC->SetLineColor(histLineColor);
		MC->SetFillColor(histFillColor);

		MC->Draw("histsame");
		data->Draw("esamex0");

		file_.Close();
	}
*/
	// writing the lumi information and the CMS "logo"
	CMS_lumi( canv, iPeriod, iPos );

	canv->Update();
	canv->RedrawAxis();
	canv->GetFrame()->Draw();

	canv->Print(canvName+".pdf",".pdf");
	canv->Print(canvName+".pdf",".pdf");

	return canv;
}


ReBin(TH1* &h)
{

	int count_new_bins=0;
	int last_big_bin=0;
	int merge_up_to_this_bin=0;
	float binContent[1000];
	binContent{1000}=0;

	vector <double> low_edges;
	low_edges.clear();
	int MINENTRIES=10;
	int histo_size=h->GetNbinsX();
	for  (unsigned int nb = 0;nb<int(h->GetNbinsX()+1);nb++){

		///////First find the first bin above x>0 which has more than 10 entries - merge_up_to_this_bin refers to this exact bin
		float  small_bins=0;	
		if ( h->GetBinContent(nb)>=MINENTRIES && h->GetBinContent(nb-1)<MINENTRIES && h->GetBinLowEdge(nb-1)<0){
			merge_up_to_this_bin=nb-1;
			// low_edges.push_back(float (h->GetBinLowEdge(nb)));
			//  cout<<" WILL MERGE NEGATIVE BINS with <MINENTRIES up to "<<nb<<"  "<<h->GetBinLowEdge(nb)<<endl;

			//   low_edges.push_back(float (h->GetBinLowEdge(nb)));
		}

		if ( h->GetBinContent(nb)>=MINENTRIES && h->GetBinLowEdge(nb)> h->GetBinLowEdge(merge_up_to_this_bin-1)  ) {


			//cout<<" found >  "<<MINENTRIES<< "  entries  for  "<<nb<<"  "<<h->GetBinLowEdge(nb)<<"   "<<h->GetBinContent(nb)<<endl;
			low_edges.push_back(float (h->GetBinLowEdge(nb)));
		}

		//////// the last_big_bin counts for the last bin with more than 10 entries      	
		if (h->GetBinContent(nb)<MINENTRIES && h->GetBinContent(nb-1)>=MINENTRIES && h->GetBinLowEdge(nb)>0){
			last_big_bin=nb-1;
			//    low_edges.push_back(float ( h->GetBinLowEdge(last_big_bin)));
			//  break;
			cout<<" we are here  "<<nb<<"  "<<h->GetNbinsX()<<endl;

			for (unsigned int b=nb;b<int(h->GetNbinsX()+1);b++){
				float sum_two_bins = h->GetBinContent(b);	

				cout<<" ===================  bin "<<b<<" info "<<h->GetBinContent(b)<<endl;

				sum_two_bins+=h->GetBinContent(b+1);

				if (sum_two_bins<MINENTRIES && sum_two_bins!=0) { 
					cout<<" did not find a value that is satisfying you...."<<sum_two_bins<<"  "<<h->GetBinContent(b)<<"  "<<h->GetBinContent(b+1)<<"  "<<b<<endl;


				}
				if (sum_two_bins>=MINENTRIES) { 
					low_edges.push_back(float (h->GetBinLowEdge(b+2))); 
					cout<<" now merged the "<<b<<" and  "<<b+1<<"  bins "<<"  "<<h->GetBinContent(b)<<"  "<<h->GetBinContent(b+1)<<endl;
					b++;break;
				}


			}

		}
	}


	sort (low_edges.begin (), low_edges.end ());

	double *valsContent = new double[(low_edges.size()+1)];

	for (unsigned int t=0;t<low_edges.size();t++){
		valsContent[t]=low_edges[t];
		//cout<<" SIZEEEEEEEEEEEEEE=========== > "<<low_edges[t]<<" i "<<t<<" size  "<<low_edges.size()<<" value "<<endl;//valsContent[t+1]<<endl;
	}

	//valsContent[low_edges.size()]=values_[values_.size()-1];
	valsContent[low_edges.size()]=h->GetBinContent(h->GetNbinsX()-1);
	//valsContent[0]=-0.5;



	//valsContent[low_edges.size()]<<"  "<<low_edges[low_edges.size()-1]<<endl;

	//cout<<valsContent[low_edges.size()]<<"  "<<low_edges[low_edges.size()-1]<<endl;
	TAxis * axiss= new TAxis(low_edges.size(), valsContent);

	cout<<" OK here with the myNewAxis....."<<endl;

	///////merge the bin contents of the x<0 area
	for (int k=0;k<merge_up_to_this_bin+1;k++){
		small_bins+=h->GetBinContent(k);
	}

	////////assign the new bin content
	for  (unsigned int n_big = merge_up_to_this_bin+1;n_big<last_big_bin+1;n_big++){

		count_new_bins++;
		binContent[count_new_bins] = float(h->GetBinContent(n_big));
	}

	binContent[0]+=small_bins;


	for  (unsigned int n_small = last_big_bin+1;n_small<int(h->GetNbinsX());n_small++){
		binContent[count_new_bins+1]+= float(h->GetBinContent(n_small));
	}


	///now make a new TH1 which will hold  the new "binned" distribution
	//TH1D *histo_binned;
	bool fixed_bins = false;
	//if (fixed_bins) histo_binned = new TH1F("","",NBINS,values_[0], values_[values_.size()-1]);
	//if (fixed_bins) histo_binned = new TH1F("","",NBINS,-1.5,2);
	if (!fixed_bins) histo_binned = new TH1F("","",axiss->GetNbins(), axiss->GetXbins ()->fArray );

	/////get the same name,title from the input TH1
	// histo_binned->SetName(h->GetName());
	// histo_binned->SetTitle(h->GetTitle());
	int newBins = axiss->GetNbins();
	h->SetBit(TH1::kCanRebin);
	//h->ReBinAxis(newBins,axiss->GetXbins ()->fArray);
	h->ReBinAxis(valsContent,axiss);
	//h->ReBinAxis(100,h->GetXaxis());
	//h->Rebin(2);
	//h->Rebin(newBins,"hnew",axiss->GetXbins ()->fArray);
	/*
	   int ls_bin = histo_binned->GetNbinsX();
	   float  ls_bin_cont = histo_binned->GetBinContent(ls_bin);
	   float  ls_bin_cont1 = histo_binned->GetBinContent(ls_bin+1);
	   */ 
	//histo_binned->SetBinContent(ls_bin, ls_bin_cont+ls_bin_cont1);
	//cout<<" was ls_bin "<<ls_bin<<" last bin "<<ls_bin_cont<<" last+1 "<<ls_bin_cont1<<endl;

	//histo_binned->Sumw2();
	//h=histo_binned;
	return h;
	/*TFile *target2 = new TFile("test.root","recreate" );
	  target2->cd();
	  h->Write();
	  target2->Write();
	  target2->Close();
	  delete target2;*/
	// for (unsigned int nbb=1;nbb<h->GetNbinsX()+1;nbb++){
	//cout<<" From the histo_binned "<<h->GetBinContent(nbb)<<"   "<<h->GetBinLowEdge(nbb)<<endl;
	// }

	/*
	   TFile *taxisFile;
	// TAxis *axiss;
	taxisFile = new TFile ("TT_axis/TT_axis_POINT_CLASS_nentriesEVNTS.root", "recreate");
	taxisFile->cd ();
	axiss = histo_binned->GetXaxis();
	axiss->Write();
	histo_binned->SetName("Binning_Template_POINT_nentriesEVNTS");
	histo_binned->Write();
	//taxisFile->Write ();
	taxisFile->Close ();
	*/ 
	cout<<" ============================================================== end of RebinTTbar ============================================="<<endl;
}


void OverFlow(TH1D *& h, int &last_bin){

	int nb = h->GetNbinsX();
	float over_ = h->GetBinContent(last_bin);
	float contlast = 0.;//h->GetBinContent(last_bin);
	for (int b=last_bin; b <= nb+1; b++) {contlast +=h->GetBinContent(b);h->SetBinContent(b,0.);}

	h->SetBinContent(last_bin,0);
	h->SetBinContent(last_bin,contlast);
}


void ReBinn(TH1 *&h){
			 int Nbins = h->GetNbinsX();
		         int LastBin =0;
		         vector<double> eventV;
        		 vector<float> BinBorderV;
        		 float SumBinContent = 0;

        		 BinBorderV.push_back(h->GetXaxis()->GetBinLowEdge(1));
        		 cout<< h->GetXaxis()->GetBinLowEdge(1)<< endl;
			float Xmin=10;


		        for ( int iN=1; iN<=Nbins; ++iN)
                	{
                		if (h-> GetBinContent(iN)<Xmin)
                        {
                        if (SumBinContent<Xmin && iN<Nbins) {SumBinContent += h-> GetBinContent(iN);}
                        else  {BinBorderV.push_back(h->GetXaxis()->GetBinUpEdge(iN));
                                eventV.push_back(SumBinContent);
                                SumBinContent=0;}
                        }

                		else
                        	{
                        	BinBorderV.push_back(h->GetXaxis()->GetBinUpEdge(iN));
                        	eventV.push_back(h-> GetBinContent(iN));
                        	}
                	}
			const int ssize=BinBorderV.size();

		        float BinBorder[ssize];

		        for ( int iNn=0; iNn<BinBorderV.size(); ++iNn) {BinBorder[iNn]=BinBorderV.at(iNn);}

        //filling histo
		        TH1D * hFinal = new TH1D(h->GetName(),h->GetTitle(),eventV.size() ,BinBorder);
		        for ( int iNm=1; iNm<=eventV.size(); ++iNm) {hFinal->SetBinContent(iNm,eventV.at(iNm-1));}
			TFile *taxisFile;
  // TAxis *axiss;
	  		 h = hFinal;
/*			  taxisFile = new TFile ("axis.root", "recreate");
			  taxisFile->cd ();
			  axiss = hFinal->GetXaxis();
			  axiss->Write();
			  hFinal->Write();
			  hFinal->SetName("axis");
			  taxisFile->Close ();
*/
}





