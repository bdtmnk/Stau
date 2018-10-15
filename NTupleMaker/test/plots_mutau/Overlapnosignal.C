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
#include "CMS_lumi.C"


using namespace std;

void Impose( TDirectory *ttarget, TList *ssourcelist, string &np_legend , vector<string> titles_ ,vector<float> xsecs);
void ModifyHist (TH1D* &h, int cl,vector <string> title);
void ModifyHist (TH1D* &h, int cl,vector <string> title, TLegend * & tleg);
void ModifyHist (TH1D* &h, int cl);
void OverFlow (TH1D* &h, int bin);
ReBin(TH1* &h);
TCanvas *modifyCanvas (TCanvas *c1);
TCanvas *example_plot(int iPeriod, int iPos , TString name);



void Overlap()
{

	setTDRStyle();


	writeExtraText = true;       // if extra text
	extraText  = "Preliminary";  // default extra text is "Preliminary"
	lumi_8TeV  = "19.1 fb^{-1}"; // default is "19.7 fb^{-1}"
	lumi_7TeV  = "4.9 fb^{-1}";  // default is "5.1 fb^{-1}"
	lumi_sqrtS = "13 TeV";       // used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)


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
	ifstream ifs("datasetsBkg");
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

	string fout = "mergedplotsTau.root";
			
	FileList = new TList ();


	for (unsigned int i=0; i <titles.size();++i){
		//string ext=".root";
		cout<<" loading dataset "<<titles[i]<<endl;
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
	float Lumi=1;

	Lumi = 2320;
	bool norm_=false;
	cout<<titles[0]<<"   "<<titles.size()<<endl;

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
	//		n_.erase(n_.length()-5);
	//		string nn_ = n_+"_out.root";
			signal_names.push_back(nn_.c_str());
		}
	}
	for (unsigned int k=0; k<signal_names.size();k++){
		cout<<" HERE ==========================  "<<signal_names[k]<<endl;
	}

	TH1D* allbkg, *htt,*hstop,*hwj,*hdyj,*hrare,*hdib,*hqcd,*httx;

	TFile *first_source = (TFile *) sourcelist->First ();
	first_source->cd ("mutau");

	TH1D* eventCount = (TH1D*)first_source->Get("mutau/histWeightsH");
	float nGen = eventCount->GetSumOfWeights();
	float xsec = 1;//assuming that first one is data
	float norm = xsec*Lumi/nGen;

	norm =1;
	lumiweights.push_back(float(norm));



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
	//c1  = new TCanvas ("c1","c1",0,22,600,600);
	while ((key = (TKey *) nextkey ())) {
		count++;
		//if (count>20) break;
		//keep only the highest cycle number for each key
		//        if (oldkey && !strcmp (oldkey->GetName (), key->GetName ()))
		//            continue;

		// read object from first source file and create a canvas
		first_source->cd ("mutau");
		TObject *obj = key->ReadObj ();

		c1  = new TCanvas ("c1",obj->GetName (),0,22,600,600);

		//TCanvas *c1 = example_plot(3, 0 , obj->GetName ());

		string nn = obj->GetName();
		bool flcont = true;
		//if ( string::npos == nn.find("CutFlowUnW")) flcont=false;
		//if (string::npos == nn.find("hDZeta_19") ) flcont=false;
		if (string::npos == nn.find("MET_11") ) flcont=false;
		if (!flcont) continue;
		if (obj->IsA ()->InheritsFrom ("TTree") ) continue;
		if (obj->IsA ()->InheritsFrom ("TH2") ) continue;
		if (obj->IsA ()->InheritsFrom ("TH1D") ) {
			// descendant of TH1D-> prepare the histograms to be superimposed

			TH1D* hh[500];
			TH1D* hsignal[500];
			TH1D* h1 = (TH1D*) obj;
			if (h1->Integral() <0.000001) continue;
			TLegend *legend_c1 = new TLegend (0.65, 0.9, 0.95, 0.55);
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

			ModifyHist (h1,1,Lumi,lumiweights[0],titles[0],norm_);
			//hh[1]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(5));	


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
			n1="QCD";n2="DY";n3="WJ",n4="TT", sn="stau";sdata="MuonEG";st1="0.2/";st2="0.5";

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
			qcd="DataDriven";
			qcd1="QCD_mc";
			st50="stau50_";
			st60="stau60_";
			st70="stau70_";
			st80="stau80_";
			st90="stau90_";
			st100="stau100_";
			string cc1="C1";
			//qcd="QCD";




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
//					cout<< " XSEC CHECK  "<<xsecc<<"  "<<fname<<"  "<<cl<<"  "<<xsecs.size()<<endl;

					float nGenn = eventCountt->GetSumOfWeights();


					float normm = float(xsecc*Lumi) / float(nGenn)  ;

					if (std::string::npos != fname.find(qcd)) { xsecc=1;normm =1.;}

					lumiweights.push_back(normm);

					TKey *key2 = (TKey *) gDirectory->GetListOfKeys ()->FindObject (h1->GetName ());

					if (key2) {
						cl++;
						countsignal++;
						TH1D *h2;

						h2 = (TH1D*) key2->ReadObj ();
						h2->SetLineWidth(4);
						h2->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(5));	
						ModifyHist (h2, cl,Lumi,lumiweights[cl-1],titles[cl-1],norm_);
						h2->SetStats(0);
						//if (std::string::npos == fname.find(signn))
						hh[cl] = h2;
						//if (std::string::npos != fname.find(signn))
						//	hsignal[cl] = h2;

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

						if (std::string::npos != fname.find(sn) || std::string::npos != fname.find(cc1) || std::string::npos != fname.find(sdata)    )
							flagg=true;


						string  hn_ = obj->GetName();
						//if(  hn_ == "MT_7")
						//{
							cout<<"  "<<fname<<endl;
							if (std::string::npos != fname.find(tt) ) { htt->Add(h2); htt->SetLineColor(h2->GetLineColor());
							cout<<" TT "<<htt->GetEntries()<<"  "<<htt->Integral()<<"  "<<htt->GetSumOfWeights()<<endl;
								};

							if (std::string::npos != fname.find(wj) || string::npos != fname.find(wj1) ) {hwj->Add(h2); hwj->SetLineColor(h2->GetLineColor());
							cout<<" WJ "<<hwj->GetEntries()<<"  "<<hwj->Integral()<<endl;
};

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

						//}




						if (!flagg)
						{
							hs->Add(h2);
							allbkg->Add(h2);
						}

				}

				nextsource = (TFile *) sourcelist->After (nextsource);
			}				// while ( nextsource )
		}

		if (obj) {
			target->cd ();

			TPad *pad1 = new TPad("pad1","pad1",0,0.2,1,1);//ratio

			TPad *pad2 = new TPad("pad2","pad2",0, 0, 1,0.19);



			pad1->SetBottomMargin(0.07);
			pad1->SetRightMargin(0.05);

			pad2->SetBottomMargin(0.05);
			pad2->SetTopMargin(0);
			pad2->SetBottomMargin(0.25);
			pad2->SetRightMargin(0.05);


			//hs->Draw("nostack");
			c1->cd();
  			c1->Update();
		        c1->RedrawAxis();
		        c1->GetFrame()->Draw();


			c1->Clear();

			pad1->SetLogy();
			pad1->SetGridx();
			pad1->Draw();
			pad2->Draw();

			pad2->SetGridy(1);

			pad1->cd();
			pad1->Clear();


			TH1D *hsum = ((TH1D*)(hs->GetStack()->Last())); // the "SUM"
			hsum->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(5));	
			//hsum->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());	
			//OverFlow(hsum,hh[1]->FindLastBinAbove(5));
			cout<<" events................. "<<hsum->GetSumOfWeights()<<"  "<<hsum->GetName()<<"  "<<hsum->GetTitle()<<" bkg "<<allbkg->Integral()<<endl;

			char namee[100];
			sprintf(namee,"%s",key->GetName ());
			char nnn[100];
			sprintf(nnn,"Entries  / %d GeV",hh[1]->GetBinWidth(1));

			hsum->GetYaxis()->SetTitle(nnn);


			//hh[1]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[titles.size()-1]->FindLastBinAbove(5));
			hh[1]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(5));
			//hh[1]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());
			//OverFlow(hh[1],hh[1]->FindLastBinAbove(5));
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
				sprintf(lumitag,"Data #int L = %.3g fb^{-1}",Lumi/1000);
				//v1->SetLineColor(kBlack);legend_c1->AddEntry(hh[1], lumitag, "LEP");
				v1->SetLineColor(kBlack);legend_c1->AddEntry(hh[1], "Data", "LEP");
				char lab_[100];
	/*			legend_c1->AddEntry(hh[2], "#tau(100,1)", "LEP");
				legend_c1->AddEntry(hh[3], "#tau(100,10)", "LEP");
				legend_c1->AddEntry(hh[4], "#tau(100,20)", "LEP");
				legend_c1->AddEntry(hh[5], "#tau(100,30)", "LEP");
				legend_c1->AddEntry(hh[6], "#tau(100,40)", "LEP");
				legend_c1->AddEntry(hh[7], "#tau(100,50)", "LEP");
				legend_c1->AddEntry(hh[8], "#tau(100,60)", "LEP");
				legend_c1->AddEntry(hh[9], "#tau(100,70)", "LEP");
				legend_c1->AddEntry(hh[10], "#tau(100,80)", "LEP");
				legend_c1->AddEntry(hh[11], "#tau(100,90)", "LEP");
	*/
				v5->SetLineColor(kPink);legend_c1->AddEntry(v5, "WJets", "l");

				v6->SetLineColor(60);legend_c1->AddEntry(v6, "TTJets", "l");
				//int cl = TColor::GetColor("#ffcc66");
				v2->SetLineColor(kYellow-7);legend_c1->AddEntry(v2, "QCD", "l");
				v8->SetLineColor(kTeal+9);legend_c1->AddEntry(v8, "DYJets", "l");
				v4->SetLineColor(kAzure+10);legend_c1->AddEntry(v4, "SingleTop", "l");
				v3->SetLineColor(kMagenta+2);legend_c1->AddEntry(v3, "VV/VVV", "l");
				v7->SetLineColor(kOrange+2);legend_c1->AddEntry(v7, "TTX/TG", "l");


				sprintf(lab_,"bkg,(%.2f)",hsum->Integral());
				//v5->SetLineColor(kRed-5);legend_c2->AddEntry(hsum, lab_, "l");
				sprintf(lab_,"data,(%.2f)",hh[1]->Integral());
				v1->SetLineColor(kBlack);legend_c2->AddEntry(hh[1], lab_, "l");
			}
			//	cout<<"  Total event from bkg  "<<counter[0]<<"   "<<hh[1]->Integral()<<endl;
			hsum->SetMaximum(5*hs->GetMaximum());
			hsum->SetMinimum(0.1);
			if (norm_) {hsum->Scale(1/hsum->Integral()); hsum->SetFillColor(0);hsum->SetLineColor(kRed);}
			hsum->Draw("hist");
			if (!norm_)
				hs->Draw("same hist");
			//hh[1]->Draw("same ep hist");
			hh[1]->SetMarkerStyle(20);
			hh[1]->SetFillColor(0);
			if (norm_) hh[1]->Scale(1/hh[1]->Integral());
			hh[1]->Draw("same e0p hist");
			//	    sign->Draw("same p hist");
/*
			for (int ij=2;ij<12;ij++){
				//hh[ij]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());
				hh[ij]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(5));
				OverFlow(hh[ij],hh[1]->FindLastBinAbove(5));
				if (norm_) hh[ij]->Scale(1/hh[ij]->Integral());
				hh[ij]->Draw("same e1p hist");
			}
*/

			string Title = hh[1]->GetName();

			legend_c1->Draw("sames");
			c1->SetFillColor(0);
			c1->SetBorderMode(0);
			c1->SetBorderSize(0);
			c1->SetFrameBorderMode(0);
			c1->SetBorderSize(0);
			pad1->SetFrameLineColor(0);;
			pad1r->SetFrameLineColor(0);;

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
			TLine *l=new TLine(axis->GetBinLowEdge(hh[1]->FindFirstBinAbove(0.)),1,axis->GetBinLowEdge(hh[1]->FindLastBinAbove(5)+1),1);
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

			allbkg->Sumw2();
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

			c1->SetTitle(namee);
			gPad->RedrawAxis();
			gPad->Modified();
			gPad->Update();
			tex = new TLatex(6.471403,1.803921e+08,"Some title here");
			tex->SetLineWidth(2);
			tex->Draw();

			c1->cd();
                	CMS_lumi( c1, 4, 1 );
			c1->Modified();
			c1->cd();
			c1->Update();


			c1->Write (namee);


			char f[100];char ff[100];
			if (!norm_)sprintf(f,"Tau/%s.pdf",namee);
			else sprintf(f,"Tau/%s_Norm.pdf",namee);

			if (!norm_)sprintf(ff,"Tau/%s_Log.pdf",namee);
			else sprintf(ff,"Tau/%s_Log_Norm.pdf",namee);

			c1->Print (f,"pdf");

			///////// TPie
			Float_t vals[]={hdib->Integral()+httx->Integral(),htt->Integral()+hstop->Integral(),hwj->Integral(),hdyj->Integral(),hqcd->Integral()};

			string nan_ = key->GetName ();
			int nvals = 5;
			string n = hh[1]->GetName();
			const char *s1;


		}

		delete c1;
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
			//h->Rebin(nn);
			//h->Sumw2();

			h->SetMinimum(0.1);
			h->GetXaxis()->SetNdivisions(512);
			string titlee=h->GetName();
			int col=;//kOrange;
			string title1,title2;
			title1= h->GetTitle();


			if (std::string::npos != title_.find("MuonEG") || std::string::npos != title_.find("Single") || std::string::npos != title_.find("C1") || std::string::npos != title_.find("tau") ||  std::string::npos != title_.find("Sq") || std::string::npos != title_.find("Gl") || std::string::npos != title_.find("0.2")  )  {

				//if ( std::string::npos != title_.find("StauA") ){

				col=kBlack ;
				h->SetLineStyle(1);
				h->SetMarkerStyle(20+cl_);
				h->SetMarkerSize(0.4);
				h->SetMarkerColor(col);
				h->SetLineColor(col);
			}


			if ( std::string::npos != title_.find("tau") || std::string::npos != title_.find("C1") ){

				//col=kBlue-10 + cl_;
				if (cl_>9) col=30+cl_;
				col=cl_;
				h->SetLineStyle(1);
				h->SetMarkerStyle(32);
				h->SetMarkerSize(0.4);
				h->SetMarkerColor(col);
				h->SetLineColor(col);
				h->SetLineStyle(6);
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
			if (std::string::npos != title_.find("TT_") || std::string::npos != title_.find("TTPow")) { col= 60; }
			if (std::string::npos != title_.find("QCD"))  {col= kYellow-7; }
			if (std::string::npos != title_.find("DYJets"))  {col= kTeal+9;}
			if (std::string::npos != title_.find("ST_") || std::string::npos != title_.find("channel")  || std::string::npos != title_.find("ST_"))  {col= kAzure+10; }//counter[4] +=h->Integral();}
			if ( td::string::npos != title_.find("WWZ") || std::string::npos != title_.find("WWTo") || std::string::npos != title_.find("ZZ") || std::string::npos != title_.find("ZZTo")|| std::string::npos != title_.find("WZ") || std::string::npos != title_.find("WZZ")) {col=kMagenta+2;}// counter[5] +=h->Integral();}
			if ( std::string::npos != title_.find("TTW") || std::string::npos != title_.find("TTZ") || std::string::npos != title_.find("tZq") || std::string::npos != title_.find("TG") || std::string::npos != title_.find("tG")) {col=kOrange+2; }//counter[6] +=h->Integral();}


			float nm = 0.;nm = float(h->Integral());

			//if ( cl_>3) counter[0] += h->Integral() ;

			//cout<< "  "<<cl_<<"  "<<title_<<endl;

			if (std::string::npos != title1.find("MET"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
			if (std::string::npos != title1.find("mass"))  h->GetXaxis()->SetTitle("GeV/c");
			if (std::string::npos != title1.find("Inv"))  h->GetXaxis()->SetTitle("GeV/c");
			if (std::string::npos != title1.find("Mass"))  h->GetXaxis()->SetTitle("GeV/c");
			if (std::string::npos != title1.find("met"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
			if (std::string::npos != title1.find("ST"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
			if (std::string::npos != title1.find("HT"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
			if (std::string::npos != title1.find("Jetp"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
			if (std::string::npos != title1.find("Phi"))  h->GetXaxis()->SetTitle("");
			if (std::string::npos != title1.find("phi"))  h->GetXaxis()->SetTitle("");
			if (std::string::npos != title1.find("dPhi"))  h->GetXaxis()->SetTitle("");
			if (std::string::npos != title1.find("pT"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
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
				for (int b=0;b<28;b++){
					//ev_ += h->GetBinContent(b);
					//tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<" & "<<" & "<<endl;	
					if (h->GetBinContent(b) > 0. ) tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<endl;	
					else tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<0<<endl;
					//if (b==15) cout<<"  "<<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<endl;
					//cout <<title1<<" & "<<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<" & "<<" & "<<endl;	
				}
				// cout<<" Counting from CutFlow  "<<ev_<<endl;
			}
tfile.close();
//if (norm_)    
//	h->Scale (1/h->Integral());

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

	// writing the lumi information and the CMS "logo"
	int iPeriod = 3;    // 1=7TeV, 2=8TeV, 3=7+8TeV, 7=7+8+13TeV, 0=free form (uses lumi_sqrtS)
	CMS_lumi( canv, iPeriod, 33 );

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



