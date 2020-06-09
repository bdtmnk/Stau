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


int mycolor=TColor::GetColor("#ffcc66");
int mycolorvv=TColor::GetColor("#6F2D35");
//int mycolorvv=TColor::GetColor("#FF6633");
int mycolorqcd=TColor::GetColor("#ffccff");
int mycolortt=TColor::GetColor("#9999cc");
//int mycolorttx=TColor::GetColor("#bbccdd");
int mycolorttx=TColor::GetColor("#33CCFF");
int mycolorwjet=TColor::GetColor("#de5a6a");
//int mycolorwjet=TColor::GetColor("#66CC66");
int mycolordyj=TColor::GetColor("#ffcc66");

void Overlap()
{
/*
	gROOT->SetStyle ("Plain");
	gROOT->LoadMacro("CMS_lumi.C");
	gStyle->SetPalette (1);
	gStyle->SetTextFont(22) ;
	gStyle->SetTitleFont(22,"xyz") ;
	gStyle->SetLabelFont(22,"xyz") ;
*/
	setTDRStyle();


	writeExtraText = true;       // if extra text
	extraText  = "Preliminary";  // default extra text is "Preliminary"
	lumi_8TeV  = "19.1 fb^{-1}"; // default is "19.7 fb^{-1}"
	lumi_7TeV  = "4.9 fb^{-1}";  // default is "5.1 fb^{-1}"
	lumi_sqrtS = "13 TeV";       // used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

	int iPeriod = 3;    // 1=7TeV, 2=8TeV, 3=7+8TeV, 7=7+8+13TeV, 0=free form (uses lumi_sqrtS)

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
	ifstream ifs("datasets");
	//ifstream ifs("datasets2D_stau-stau");
	string line;
	while(std::getline(ifs, line)) // read one line from ifs
	{
		istringstream iss(line); // access line as a stream
		string dataname;
		float XSec;	
		float xs,fact,fact2,fact3;
		xs=0;fact=1;fact2=1;fact3=1;
		iss >> dataname >> xs >> fact >> fact2 >> fact3;
		titles.push_back(dataname+"_Nominal_B.root");
		XSec= xs*fact*fact2*fact3;
		cout<<" Found the correct cross section "<<xs<<" for Dataset "<<dataname<<" XSec "<<XSec<<"  "<<fact<<"  "<<fact2<<"  "<<fact<<endl;
		xsecs_.push_back(XSec);
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
	float Lumi=1.;


	Lumi = 35800.;
	bool norm_=false;
	bool SO_=true;
	bool QCDMC=false;
        int MaxEventsBin = 0;
	bool drawData=true;
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
			n_.erase(n_.length()-5);
			string nn_ = n_+"_out.root";
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
	//TH1D* eventCount = (TH1D*)first_source->Get("mutau/inputEventsH");
	//TH1D* hxsec = (TH1D*)first_source->Get("mutau/xsec");
	float nGen = eventCount->GetSumOfWeights();
	float xsec = 1;//hxsec->GetMean();
	float norm = xsec*Lumi/nGen;

	norm =1;
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
	TFile *NPfile = TFile::Open ("NP.root", "recreate");
	TFile *smFile = TFile::Open ("BkgTemplates_hDZeta.root", "recreate");
	int count=0;
	TCanvas *c1  ;//= new TCanvas ("c1",obj->GetName (),0,22,600,600);
	//c1  = new TCanvas ("c1","c1",0,22,600,600);
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
		//c1->SetName(obj->GetName());
		c1->SetTitle(obj->GetName());


		//TCanvas *c1 = example_plot(3, 0 , obj->GetName ());

		string nn = obj->GetName();
		bool flcont = true;
		bool NormTT = false;
		//if ( string::npos == nn.find("CutFlowUnW")) flcont=false;
		if (string::npos == nn.find("_15") ) flcont=false;
		if (!flcont) continue;

		NormTT=true;
		if (obj->IsA ()->InheritsFrom ("TTree") ) continue;
		if (obj->IsA ()->InheritsFrom ("TH2") ) continue;
		if (obj->IsA ()->InheritsFrom ("TH1D") ) {
			// descendant of TH1D-> prepare the histograms to be superimposed

			TH1D* hh[500];
			TH1D* hsignal[500];
			TH1D* h1 = (TH1D*) obj;
			if (h1->Integral() <0.0001) continue;
      		        //if ( string::npos == nn.find("Iso")) MaxEventsBin=0; 


			TLegend *legend_c1 ;

if (SO_) legend_c1    = new TLegend (0.35, 0.92, 0.95, 0.55);
if (!SO_) legend_c1    = new TLegend (0.65, 0.92, 0.9, 0.55);

			TLegend *legend_c2 = new TLegend (0.3, 0.92, 0.5, 0.8);
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
if (SO_)
			 legend_c1-> SetNColumns(2);
			ModifyHist (h1,1,Lumi,lumiweights[0],titles[0],false);
			//hh[1]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(MaxEventsBin));	


			//if (! h1->GetSumOfWeights() >0 ) continue;

			// loop over all source files and modify the correspondant
			// histogram to the one pointed to by "h1"
			TFile *nextsource = (TFile *) sourcelist->After (first_source);

			int cl, countsignal;
			h1->SetStats(000000);
			h1->SetLineWidth(2);
			cl=1;
			countsignal=1;

			hh[cl]=h1;
      		        if ( string::npos != nn.find("CutFlowUnW")) {

			for (int ib=12;ib<hh[1]->GetNbinsX();ib++) 
		
			hh[1]->SetBinContent(ib,0.001);

			}

			THStack *hs = new THStack(h1->GetName(),h1->GetTitle());


			string sn="stau";
			string sdata="Single";
			string sdata2="MuonEG";
			string cc1="C1";


			while (nextsource) {
	
			string fname= nextsource->GetName();


					bool flagg= false;

					if (std::string::npos != fname.find(sn) || std::string::npos != fname.find(cc1) || std::string::npos != fname.find(sdata)  || std::string::npos != fname.find(sdata2)  ) 	flagg=true;

					//if (flagg) cout<<"=============================================================== "<<fname<<endl;
					// make sure we are at the correct directory level by cd'ing to path
					nextsource->cd("mutau");
					TH1D* eventCountt ;

				  if  ( std::string::npos == fname.find("TT_TuneCUETP8M2T4_13TeV-powheg-pythia8") || !NormTT) eventCountt = (TH1D*)nextsource->Get("mutau/histWeightsH");
				  if ( NormTT && std::string::npos != fname.find("TT_TuneCUETP8M2T4_13TeV-powheg-pythia8") ) eventCountt = (TH1D*)nextsource->Get("mutau/histTopPt");

					//TH1D* eventCountt = (TH1D*)nextsource->Get("mutau/inputEventsH");


					//TH1D* hxsecc = (TH1D*)nextsource->Get("mutau/xsec");
					//float xsecc = hxsecc->GetMean();
					float xsecc = xsecs[cl];
//					cout<< " XSEC CHECK  "<<xsecc<<"  "<<fname<<"  "<<cl<<"  "<<xsecs.size()<<endl;

					float nGenn = eventCountt->GetSumOfWeights();


					float normm = float(xsecc*Lumi) / float(nGenn)  ;
					string qcd="QCD_DataDriven";
					if (std::string::npos != fname.find(qcd)) { normm =1.;}
				//	if (std::string::npos == fname.find(qcd) && nGenn<0.) { normm =0.;}
					//if (nGenn <0.) normm=0.;
					lumiweights.push_back(normm);

					TKey *key2 = (TKey *) gDirectory->GetListOfKeys ()->FindObject (h1->GetName ());

					if (key2) {
						cl++;
						countsignal++;
						TH1D *h2;

						h2 = (TH1D*) key2->ReadObj ();
			
                                        /*if (nGenn<0. &&  string::npos == nn.find("CutFlowUnW")) {
                                        h2->Scale(-1);
                                        for (int jk=1;jk<=h2->GetNbinsX(); ++jk){

                                        if (h2->GetBinContent(jk)<0)
                                                h2->SetBinContent(jk,0.);
                                                }
                                        cout<<" After correcting the weights .... ====================================== "<<nGenn<<"  "<<h2->GetSumOfWeights()<<"  "<<h2->GetSumOfWeights()<<"  "<<h2->GetName()<<endl;
                                        }///nGenn <0.*/

						h2->SetLineWidth(3);
      		        			if ( string::npos == nn.find("CutFlowUnW")) 
						h2->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(MaxEventsBin));	

						ModifyHist (h2, cl,Lumi,lumiweights[cl-1],titles[cl-1],false,xsecc);
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

						//				cout<< " for "<<fname<<"  "<<count<<" file, there xsec is "<<xsecc<<" SuOfWeights "<<nGenn<<" Lumi "<<Lumi<<" lumiweight "<<lumiweights[cl-1]<<" weight "<<float(xsecc*Lumi/nGenn)<<"  norm "<<normm<<" cl "<<cl<<"  "<<h2->GetSumOfWeights()<<endl;
						//cout<< " for "<<fname<<" file, there xsec is "<<xsecc<<" SuOfWeights "<<"  "<<h2->GetSumOfWeights()<<" Lumi "<<Lumi<<" lumiweight "<<lumiweights[cl-1]<<" weight "<<float(xsecc*Lumi/nGenn)<<endl;
						//if (std::string::npos == fname.find(sn) )

						if (std::string::npos != fname.find(sn) || std::string::npos != fname.find(cc1) || std::string::npos != fname.find(sdata) ||  std::string::npos != fname.find(sdata2)  )
							flagg=true;


						string  title_ = fname;
							cout<<"  "<<fname<<endl;


			if (std::string::npos != title_.find("wJets")|| std::string::npos != title_.find("WJetsToLNu") || std::string::npos != title_.find("W1JetsToLNu") || std::string::npos != title_.find("W2JetsToLNu") 
			|| std::string::npos != title_.find("W3JetsToLNu") || std::string::npos != title_.find("W4JetsToLNu"))  { col=mycolorwjet ; hwj->Add(h2); hwj->SetLineColor(col);}
			if (std::string::npos != title_.find("TT_TuneCUETP8M2T4_13TeV-powheg-pythia8") || std::string::npos != title_.find("TTPow")) { col= mycolortt;htt->Add(h2); htt->SetLineColor(col); cout <<"AAAAAAAAAAA!!!!!!!!!!!"<<endl;}
			if (std::string::npos != title_.find("QCD"))  {col= mycolorqcd; hqcd->Add(h2); hqcd->SetLineColor(col); }
			if (std::string::npos != title_.find("DYJets") || std::string::npos != title_.find("DY1Jets") || 
			std::string::npos != title_.find("DY2Jets") || std::string::npos != title_.find("DY3Jets") || std::string::npos != title_.find("DY4Jets"))  {col= mycolordyj;hdyj->Add(h2); hdyj->SetLineColor(col);}
			if (std::string::npos != title_.find("ST_") || std::string::npos != title_.find("channel") )  {col= mycolortt; hstop->Add(h2);hstop->SetLineColor(col);}

			//if ( std::string::npos != title_.find("WW") || std::string::npos != title_.find("ZZ") ||  std::string::npos != title_.find("WZ") || std::string::npos != title_.find("WG") || std::string::npos != title_.find("ZG") ) {col=mycolorvv; hdib->Add(h2); hdib->SetLineColor(col);}

			if ( std::string::npos != title_.find("WW")  ) {col=mycolorvv; hdib->Add(h2); hdib->SetLineColor(col);}
			if ( std::string::npos != title_.find("WG") ) {col=kBlack; hdib->Add(h2); hdib->SetLineColor(col);}
			if (  std::string::npos != title_.find("ZZ") ) {col=kRed; hdib->Add(h2); hdib->SetLineColor(col);}
			if (  std::string::npos != title_.find("ZG") ) {col=kBlue; hdib->Add(h2); hdib->SetLineColor(col);}

			if ( std::string::npos != title_.find("TTW") || std::string::npos != title_.find("TTZ") || std::string::npos != title_.find("tZq") || std::string::npos != title_.find("TG") || std::string::npos != title_.find("tG") || std::string::npos != title_.find("TTG") || std::string::npos != title_.find("ttW") || std::string::npos != title_.find("ttZ") || std::string::npos != title_.find("tZ") || std::string::npos != title_.find("TTT_") ) {col=mycolorttx ;httx->Add(h2);   httx->SetLineColor(col);}


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

			///////// TPie
			Float_t vals[]={hdib->GetSumOfWeights()+httx->GetSumOfWeights(),  hwj->GetSumOfWeights(), htt->GetSumOfWeights()+hstop->GetSumOfWeights(),  hdyj->GetSumOfWeights(), hqcd->GetSumOfWeights()};
			//Float_t vals[]={1,2,3,4,5};

			string nan_ = key->GetName ();
			int nvals = 5;
			//if (std::string::npos != nan_.find("MET_16") ){
			if ( nan_ =="nMu_18") {
			  cout<<" Found it here  "<<nan_<<"   "<<key->GetName()<<endl;
			//Int_t nvals = sizeof(counter)/sizeof(counter[0]);
			//cout<<"  vals ============== "<<vals[0]<<"  "<<vals[1]<<"  "<<vals[2]<<"  "<<vals[3]<<"  "<<vals[4]<<"   "<<endl;
			cout<<" VV + TTX  "<<hdib->GetSumOfWeights()+httx->GetSumOfWeights()<<" TT+ST "<<htt->GetSumOfWeights()+hstop->GetSumOfWeights()<<" WJ "<<hwj->GetSumOfWeights()<<" DY "<<hdyj->GetSumOfWeights()<<" TTX "<<httx->GetSumOfWeights()<<" QCD "<<hqcd->GetSumOfWeights()<<endl;

			Int_t colors[] = { hdib->GetLineColor(),hwj->GetLineColor(),htt->GetLineColor(),hdyj->GetLineColor(),hqcd->GetLineColor()};
			TPie *pie3 = new TPie("pie3","Pie with tangential labels",nvals,vals,colors);

			TCanvas *cpie = new TCanvas("cpie","TPie test",1200,1200);
			cpie->cd();
			pie3->SetRadius(.2);
			pie3->SetLabelsOffset(.015);
			pie3->SetLabelFormat("%txt - (%perc)");
			pie3->SetTextAngle(0.45);
			pie3->SetTextSize(0.04);
			pie3->SetFractionFormat(".0g");


		
			for (int j=0;j<nvals;j++) cout<<" VALUES         ======================================="<<  vals[j]<<endl;

			char lumitag[100];
			sprintf(lumitag,"Data #int L = %.3g fb^{-1}",Lumi/1000);
			//pie3->GetSlice(0)->SetTitle(lumitag);
                        pie3->SetLabelFormat("#splitline{%txt}{%perc}");
			pie3->GetSlice(0)->SetTitle("Rest");
			pie3->GetSlice(1)->SetTitle("WJets");
			pie3->GetSlice(2)->SetTitle("t#bar{t}+SingleT");
			pie3->GetSlice(3)->SetTitle("DYJets");
			//pie3->GetSlice(4)->SetTitle("sT");
			//pie3->GetSlice(4)->SetTitle("ttx");
			pie3->GetSlice(4)->SetTitle("QCD");
			//pie3->SetEntryRadiusOffset(2,-.05);
			//pie3->SetLabelsOffset(-0);
			//pie3->SetLabelsSize(0.05);
			pie3->Draw("nol <");
			pie3->Draw("rsc");
			//pie3->Draw("3d");
			cpie->SaveAs("Tau/APie.pdf");

			}
			//////////////////////////// Pie

			
			target->cd ();
			//legend_c1->SetNColumns(3);

			TPad *pad1 ;//= new TPad("pad1","pad1",0,0.2,1,1);//ratio
			TPad *pad1r = new TPad("pad1","pad1",0.5,0.25,1,1);

			TPad *pad2 = new TPad("pad2","pad2",0, 0, 1,0.2);
			TPad *pad2s = new TPad("pad2s","pad2s",0, 0.13, 1,0.249);

			if (!drawData) 
			pad1= new TPad("pad1","pad1",0,0,1,1);
			if (drawData)  
			pad1= new TPad("pad1","pad1",0,0.2,1,1);

			pad1->SetBottomMargin(0.0);
			if (!drawData) pad1->SetBottomMargin(0.1);
			pad1->SetRightMargin(0.05);
			//pad1->SetGridy();
			pad1r->SetBottomMargin(0.07);
			pad1r->SetRightMargin(0.05);
			//pad1r->SetGridy();

			pad2->SetTopMargin(0.01);
			pad2->SetBottomMargin(0.35);
			pad2->SetRightMargin(0.05);

			pad2s->SetTopMargin(0);
			pad2s->SetBottomMargin(5);
			pad2s->SetRightMargin(0.05);


			//hs->Draw("nostack");
			c1->cd();


			c1->Clear();

			pad1->SetLogy();
			//pad1->SetGridx();
			pad1->Draw();
			//pad1r->Draw();
		if (drawData)	pad2->Draw();

			pad2->SetGridy(1);
			pad2s->SetGridy(1);
			//pad2s->Draw();

			pad1->cd();
			pad1->Clear();


			TH1D *hsum = ((TH1D*)(hs->GetStack()->Last())); // the "SUM"
      		        if ( string::npos == nn.find("CutFlowUnW")) 
			hsum->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(MaxEventsBin));	
			OverFlow(hsum,hh[1]->FindLastBinAbove(MaxEventsBin));
			//hsum->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());	
			//cout<<" events................. "<<hsum->GetSumOfWeights()<<"  "<<hsum->GetName()<<"  "<<hsum->GetTitle()<<" bkg "<<allbkg->GetSumOfWeights()<<endl;

			char namee[100];
			sprintf(namee,"%s",key->GetName ());
			char nnn[100];

			string titlee= hsum->GetTitle();
			if (std::string::npos != titlee.find("Phi")) hsum->GetYaxis()->SetTitle("Events");
			if (std::string::npos != titlee.find("eta")) hsum->GetYaxis()->SetTitle("Events");
			if (std::string::npos != titlee.find("nJ") || std::string::npos != titlee.find("nB") ||  std::string::npos != titlee.find("nEl") || std::string::npos != titlee.find("nM") || std::string::npos != titlee.find("nT")) hsum->GetYaxis()->SetTitle("Events");
			hsum->GetYaxis()->SetTitleOffset(1);
			hsum->GetYaxis()->SetTitleSize(0.045);

			//hh[1]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[titles.size()-1]->FindLastBinAbove(MaxEventsBin));
      		        if ( string::npos == nn.find("CutFlowUnW")) 
			hh[1]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(MaxEventsBin));
			OverFlow(hh[1],hh[1]->FindLastBinAbove(MaxEventsBin));
			//hh[1]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());
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
				v1->SetLineColor(kBlack);
if (drawData)			legend_c1->AddEntry(hh[1], "Data", "LEP");
				char lab_[100];
if (SO_){
				legend_c1->AddEntry(hh[2], "#tilde{#tau}(100,10)", "LEP");
				//legend_c1->AddEntry(hh[3], "C1C1(100,25)", "LEP");
				//legend_c1->AddEntry(hh[4], "C1C1(300,200)", "LEP");
				//legend_c1->AddEntry(hh[3], "C1N2(100,75)", "LEP");
				//legend_c1->AddEntry(hh[4], "C1N2(200,100)", "LEP");
				//legend_c1->AddEntry(hh[5], "C1N2(300,100)", "LEP");
				//legend_c1->AddEntry(hh[6], "C1N2(400,125)", "LEP");

				legend_c1->AddEntry(hh[3], "#tilde{#tau}(100,50)", "LEP");
				legend_c1->AddEntry(hh[4], "#tilde{#tau}(150,1)", "LEP");
				legend_c1->AddEntry(hh[5], "#tilde{#tau}(150,70)", "LEP");
				legend_c1->AddEntry(hh[6], "#tilde{#tau}(200,1)", "LEP");
}

				v6->SetLineColor(mycolortt);legend_c1->AddEntry(v6, "TTJets/singleT", "l");
				v7->SetLineColor(mycolorttx);legend_c1->AddEntry(v7, "TTX/TG", "l");
				v5->SetLineColor(mycolorwjet);legend_c1->AddEntry(v5, "WJets", "l");
				//int cl = TColor::GetColor("#ffcc66");
				v2->SetLineColor(mycolorqcd);legend_c1->AddEntry(v2, "QCD", "l");
				v8->SetLineColor(mycolordyj);legend_c1->AddEntry(v8, "DYJets", "l");
//				v4->SetLineColor(kAzure+10);legend_c1->AddEntry(v4, "SingleTop", "l");
				v3->SetLineColor(mycolorvv);legend_c1->AddEntry(v3, "VV/VG/VVV", "l");


				sprintf(lab_,"bkg,(%.2f)",hsum->GetSumOfWeights());
				//v5->SetLineColor(kRed-5);legend_c2->AddEntry(hsum, lab_, "l");
				sprintf(lab_,"data,(%.2f)",hh[1]->GetSumOfWeights());
				v1->SetLineColor(kBlack);legend_c2->AddEntry(hh[1], lab_, "l");
			}
			//	cout<<"  Total event from bkg  "<<counter[0]<<"   "<<hh[1]->GetSumOfWeights()<<endl;
			hsum->SetMaximum(500*hs->GetMaximum());
			hsum->SetMinimum(0.05);
			sprintf(nnn,"Entries  / %d GeV",hh[1]->GetBinWidth(2));
			hsum->GetYaxis()->SetTitle(nnn);
			if (norm_) {hsum->Scale(1/hsum->Integral()); hsum->SetFillColor(0);hsum->SetLineColor(kRed);}
			hsum->Draw("hist");
			if (!norm_)
				hs->Draw("same hist");
if (drawData)		hh[1]->Draw("same ep hist");
			hh[1]->SetMarkerStyle(20);
			hh[1]->SetFillColor(0);
			if (norm_) hh[1]->Scale(1/hh[1]->Integral());
		//		     hh[1]->Draw("same e0p hist");
			//	    sign->Draw("same p hist");
if (SO_){
			for (int ij=2;ij<7;ij++){
				//hh[ij]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());
      		        	if ( string::npos == nn.find("CutFlowUnW")) 
				hh[ij]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(MaxEventsBin));
				OverFlow(hh[ij],hh[1]->FindLastBinAbove(MaxEventsBin));
				if (norm_) { hh[ij]->Scale(1/hh[ij]->Integral());hh[ij]->SetLineColor(kBlue+ij);}
				//hh[ij]->Scale(10);
				hh[ij]->SetFillColor(0);
				hh[ij]->Draw("same  e1p hist");
				//ij++;
			}
}
			string Title = hh[1]->GetName();

			//c1->cd();
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
			ratio->SetMarkerStyle(20);
			ratio->SetMaximum( 2.2 );
			ratio->SetMinimum(0.5);
			//ratio->SetMaximum( 1.15 );
			//ratio->SetMinimum(0.85);
			ratio->GetXaxis()->SetTitle(hh[1]->GetXaxis()->GetTitle());
			ratio->GetYaxis()->SetTitle("");
			ratio->SetTitleSize(0);
			ratio->SetMarkerSize(0.08);
			ratio->SetLineStyle(1);
                        ratio->SetMarkerSize(1.2);
			ratio->SetMarkerColor(kBlack);
			ratio->SetLineColor(kBlack);
			ratio->SetLineWidth(1);
			ratio->GetYaxis()->SetNdivisions(5);

			ratio->GetXaxis()->SetNdivisions(545);
			ratio->GetXaxis()->SetLabelSize(0.15);
			ratio->GetXaxis()->SetTitleOffset(0.8);
			ratio->GetXaxis()->SetTitleSize(0.17);

			ratio->GetYaxis()->SetLabelSize(0.1);
			ratio->GetYaxis()->SetLabelSize(0.15);
			ratio->GetYaxis()->SetTitleSize(0.15);
			ratio->GetYaxis()->SetTitleOffset(0.25);
			ratio->GetYaxis()->SetTitle("Obs / MC");


			ratio->SetTitleFont(62);
			//ratio->GetXaxis()->SetRange(ratio->FindFirstBinAbove(0),ratio->FindLastBinAbove(MaxEventsBin));
      		        if ( string::npos == nn.find("CutFlowUnW")) 
			ratio->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(MaxEventsBin));

			//ratio->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->GetNbinsX());

			ratio->GetXaxis()->SetNdivisions(510);
			ratio->SetTitle("");
			TAxis *axis = hh[1]->GetXaxis();
			float halfbin = axis->GetBinWidth(hh[1]->GetBin(1))*0.5;
			//cout<<" halfbin  "<<halfbin
			//  TLine *l=new TLine(axis->GetBinLowEdge(hh[1]->FindFirstBinAbove(0.)),1,axis->GetBinWidth(hh[1]->GetBin(1))*hh[1]->GetNbinsX() - halfbin,1);
      		        //if ( string::npos == nn.find("CutFlowUnW")) 
			TLine *l=new TLine(axis->GetBinLowEdge(hh[1]->FindFirstBinAbove(0.)),1,axis->GetBinLowEdge(hh[1]->FindLastBinAbove(MaxEventsBin)+1),1);

			//   cout<<"  ================= > "<< hh[1]->GetBinContent(hh[1]->FindLastBinAbove(0.0))<<"    "<<hh[1]->FindLastBinAbove(float(0.0))<<endl;
			l->SetLineColor(kRed);
			l->SetLineWidth(2);
			bkgRatioErrH  = (TH1D*) ratio->Clone();
			DataHErrP  = (TH1D*) hh[1]->Clone();
			DataHErrM  = (TH1D*) hh[1]->Clone();
			//bkgRatioErrH =(TH1D*) bkgRatioErrH->Clone("hh[1]");
			//bkgRatioErrH->Reset();
			bkgRatioErrH->SetLineColor(kBlack);
			bkgRatioErrH->SetFillStyle(3013);
			bkgRatioErrH->SetFillColor(1);
			bkgRatioErrH->SetMarkerStyle(20);
			bkgRatioErrH->SetMarkerSize(0);
			bkgRatioErrH->SetLineColor(1);
			bkgRatioErrH->SetLineWidth(2);

			//hh[1]->Sumw2();
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

                       if (drawData) ratio->Draw("ep ");
			bkgRatioErrH->Draw("e2 same");
			l->Draw("same");
/*
			 pad1->cd();
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
*/
			//hh[1]->Draw("e1same");
			
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
			if (SO_ && !QCDMC)sprintf(f,"Tau/%sSO.pdf",namee);
			//if (SO_ && !QCDMC)sprintf(f,"Tau/%sSO_A.pdf",namee);
			if (SO_ && QCDMC)sprintf(f,"Tau/%s_QCDMC_SO.pdf",namee);
			if(!SO_ && !QCDMC) sprintf(f,"Tau/%s.pdf",namee);
			if(!SO_ && QCDMC) sprintf(f,"Tau/%s_QCDMC.pdf",namee);
//			else sprintf(f,"Tau/%s_Norm.pdf",namee);

//			if (!norm_)sprintf(ff,"Tau/%s_Log.pdf",namee);
//			else sprintf(ff,"Tau/%s_Log_Norm.pdf",namee);

			//if (!norm_)sprintf(f,"Tau/%s.pdf",namee);

			//TH1D* ht;
			// ht = (TH1D*)c1->GetPrimitive(namee);
			//c1->cd();
			//c1->Modified();
			//c1->cd();
			//c1->Update();
			c1->Print (f,"pdf");


		}

		} 			// while ( ( TKey *key = (TKey*)nextkey() ) )
		delete c1;
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
		ModifyHist (TH1D* &h, int cl_ ,float & lumi,float & weight,string & title_, bool norm_=false,float XSec=1.)
		{


			int nbins=h->GetNbinsX();
			int nn=1;
			string title1,title2;
			title1= h->GetName();


			h->SetMinimum(0.001);
			h->GetXaxis()->SetNdivisions(512);
			string titlee=h->GetName();
			int col=;//kOrange;


			if (std::string::npos != title_.find("Data") || std::string::npos != title_.find("Single") || std::string::npos != title_.find("MuonEG")  )  {

				//if ( std::string::npos != title_.find("StauA") ){

				col=kBlack ;
				h->SetLineStyle(1);
				h->SetMarkerStyle(20);
				h->SetMarkerSize(1.2);
				h->SetMarkerColor(col);
				h->SetLineColor(col);
			}


			if ( std::string::npos != title_.find("tau") || std::string::npos != title_.find("C1") || std::string::npos != title_.find("SMS")){

				//col=kBlue-10 + cl_;
				if (cl_>9) col=30+cl_;
				col=cl_+1;
				h->SetLineStyle(1);
				h->SetMarkerStyle(32);
				h->SetMarkerSize(0.3);
				h->SetMarkerColor(col);
				h->SetLineColor(col);
				h->SetLineStyle(6);
				h->SetFillColor(0);
			}


			//h->SetLineWidth(2);
			int nb = h->GetNbinsX();
			float over_ = h->GetBinContent(nb+1);
			float contlast = h->GetBinContent(nb);
			//h->SetBinContent(nb,contlast+over_);
			//if (weight != 1.)

			h->Scale(weight);
			//h->Scale (1/h->GetSumOfWeights());

			//cout<<" scaling to weight  "<<h->GetName()<<"  "<<h->GetSumOfWeights()<<endl;
			//int nbb = h->FindFirstBinBelow(10.);
			/*do
			  {
			  int nbb = h->GetFirstBinBelow(10.)
			  h->Rebin(2)
			  }*/

			//    if (std::string::npos != title_.find("TTV"))  col= 60;
			if (std::string::npos != title1.find("Mt2mu")) h->Rebin(5);
			if (std::string::npos != title_.find("wJets")|| std::string::npos != title_.find("WJetsToLNu") || std::string::npos != title_.find("W1JetsToLNu") || std::string::npos != title_.find("W2JetsToLNu") 
			|| std::string::npos != title_.find("W3JetsToLNu") || std::string::npos != title_.find("W4JetsToLNu"))  { col=mycolorwjet ; }
	//		if (std::string::npos != title_.find("wJets")|| std::string::npos != title_.find("WJetsToLNu"))  { col= TColor::GetColor("#de5a6a");}
			if (std::string::npos != title_.find("TT_TuneCUETP8M2T4_13TeV-powheg-pythia8") || std::string::npos != title_.find("TTPow")) { col= mycolortt; }
	//		if (std::string::npos != title_.find("TT_") || std::string::npos != title_.find("TTPow")) { col= TColor::GetColor("#9999cc"); }

			if (std::string::npos != title_.find("QCD"))  {col= mycolorqcd; }
	//		if (std::string::npos != title_.find("QCD"))  {col= TColor::GetColor("#ffccff"); }

			if (std::string::npos != title_.find("DYJets") || std::string::npos != title_.find("DY1Jets") || 
			std::string::npos != title_.find("DY2Jets") || std::string::npos != title_.find("DY3Jets") || std::string::npos != title_.find("DY4Jets"))  {col= mycolordyj;}
	//		if (std::string::npos != title_.find("DYJets"))  {col= TColor::GetColor("#ffcc66");}

			if (std::string::npos != title_.find("ST_") || std::string::npos != title_.find("channel") )  {col= mycolortt; }//counter[4] +=h->GetSumOfWeights();}

			//if ( std::string::npos != title_.find("WW") || std::string::npos != title_.find("ZZ") ||  std::string::npos != title_.find("WZ") || std::string::npos != title_.find("WG") || std::string::npos != title_.find("ZG") ) {col=mycolorvv;}

			if ( std::string::npos != title_.find("WW")  ) {col=mycolorvv; }
			if ( std::string::npos != title_.find("WG") ) {col=kBlack; }
			if (  std::string::npos != title_.find("ZZ") ) {col=kRed; }
			if (  std::string::npos != title_.find("ZG") ) {col=kBlue; }
			if (  std::string::npos != title_.find("WWTo2L2Nu") ) {col=kGreen; }

			if ( std::string::npos != title_.find("TTW") || std::string::npos != title_.find("TTZ") || std::string::npos != title_.find("tZq") || std::string::npos != title_.find("TG") || std::string::npos != title_.find("tG") || std::string::npos != title_.find("TTG") || std::string::npos != title_.find("ttW") || std::string::npos != title_.find("ttZ") || std::string::npos != title_.find("tZ") || std::string::npos != title_.find("TTT_") ) {col=mycolorttx ;}//counter[6] +=h->GetSumOfWeights();}



			//cout<< "  "<<cl_<<"  "<<title_<<endl;
			char histotitle[100];
		//	string htitle;
		//	if (std::string::npos != title1.find("met"))  h->GetXaxis()->SetTitle("GeV");
		//	if (std::string::npos != title1.find("ST"))  h->GetXaxis()->SetTitle("GeV/c^{2}`");
		//	if (std::string::npos != title1.find("HT"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
		//	if (std::string::npos != title1.find("Jetp"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
		//	if (std::string::npos != title1.find("Phi"))  h->GetXaxis()->SetTitle("rad");
		//	if (std::string::npos != title1.find("phi"))  h->GetXaxis()->SetTitle("rad");
		//	if (std::string::npos != title1.find("pT"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
			if (std::string::npos != title1.find("nB"))  h->GetXaxis()->SetTitle("nBJets");
			if (std::string::npos != title1.find("nJ"))  h->GetXaxis()->SetTitle("nJets");
			if (std::string::npos != title1.find("nL"))  h->GetXaxis()->SetTitle("nLept");
			if (std::string::npos != title1.find("nmu"))  h->GetXaxis()->SetTitle("nMu");
			if (std::string::npos != title1.find("nEl"))  h->GetXaxis()->SetTitle("nEl");
			if (std::string::npos != title1.find("nMu"))  h->GetXaxis()->SetTitle("nMu");
			if (std::string::npos != title1.find("nTau"))  h->GetXaxis()->SetTitle("nTau");
			if (std::string::npos != title1.find("dz"))  h->GetXaxis()->SetTitle("|d_{z}| [cm]");
			if (std::string::npos != title1.find("dxy"))  h->GetXaxis()->SetTitle("|d_{xy}| [cm]");
			if (std::string::npos != title1.find("el_dxy"))  h->GetXaxis()->SetTitle("|d_{xy}|(e) [cm]");
			if (std::string::npos != title1.find("mu_dxy"))  h->GetXaxis()->SetTitle("|d_{xy}|(#mu) [cm]");
			if (std::string::npos != title1.find("tau_dxy"))  h->GetXaxis()->SetTitle("|d_{xy}|(#tau) [cm]");
			if (std::string::npos != title1.find("mu_dz"))  h->GetXaxis()->SetTitle("|d_{z}|(#mu) [cm]");
			if (std::string::npos != title1.find("el_dz"))  h->GetXaxis()->SetTitle("|d_{z}|(e) [cm]");
			if (std::string::npos != title1.find("tau_dz"))  h->GetXaxis()->SetTitle("|d_{z}|(#tau) [cm]");

			if (std::string::npos != title1.find("dEtaDil"))  h->GetXaxis()->SetTitle("#Delta#eta(Dil)");


			if (std::string::npos != title1.find("HT"))  h->GetXaxis()->SetTitle("H_{T} [GeV]");
			if (std::string::npos != title1.find("HText"))  h->GetXaxis()->SetTitle("H_{Text} [GeV]");
			if (std::string::npos != title1.find("MCT"))  h->GetXaxis()->SetTitle("M_{CT} [GeV]");
//			if (std::string::npos != title1.find("MCTb"))  h->GetXaxis()->SetTitle("M_{CTb} [GeV]");
			if (std::string::npos != title1.find("MCTx"))  h->GetXaxis()->SetTitle("M_{CTx} [GeV]");
			if (std::string::npos != title1.find("MCTy"))  h->GetXaxis()->SetTitle("M_{CTy} [GeV]");
			if (std::string::npos != title1.find("MET"))  h->GetXaxis()->SetTitle("#slash{E}_{T} [GeV]");
			if (std::string::npos != title1.find("MT"))  h->GetXaxis()->SetTitle("M_{T} [GeV]");
			if (std::string::npos != title1.find("MTmu"))  h->GetXaxis()->SetTitle("M_{T}(#mu) [GeV]");
			if (std::string::npos != title1.find("MTel"))  h->GetXaxis()->SetTitle("M_{T}(el) [GeV]");
			if (std::string::npos != title1.find("MTtau"))  h->GetXaxis()->SetTitle("M_{T}(#tau) [GeV]");

			if (std::string::npos != title1.find("MTmutau"))  h->GetXaxis()->SetTitle("M_{T}(#mu,#tau) [GeV]");
			if (std::string::npos != title1.find("MTeltau"))  h->GetXaxis()->SetTitle("M_{T}(e,#tau) [GeV]");
			if (std::string::npos != title1.find("MTmuel"))  h->GetXaxis()->SetTitle("M_{T}(#mu,e) [GeV]");


			if (std::string::npos != title1.find("MTtot"))  h->GetXaxis()->SetTitle("M_{Ttot} [GeV]");
			if (std::string::npos != title1.find("MTsum"))  h->GetXaxis()->SetTitle("M_{Tsum} [GeV]");
			if (std::string::npos != title1.find("Mt2lester"))  h->GetXaxis()->SetTitle("M_{T2lester} [GeV]");
			if (std::string::npos != title1.find("Mt2mu"))  h->GetXaxis()->SetTitle("M_{T2} [GeV]");
			if (std::string::npos != title1.find("Mt2el"))  h->GetXaxis()->SetTitle("M_{T2} [GeV]");

			if (std::string::npos != title1.find("MET_"))  h->GetXaxis()->SetTitle("#slash{E}_{T} [GeV]");
			if (std::string::npos != title1.find("dPhiMETLep"))  h->GetXaxis()->SetTitle("#Delta#Phi(#slash{E}_{T},lep) [rad]");
			if (std::string::npos != title1.find("dPhiMETMu"))  h->GetXaxis()->SetTitle("#Delta#Phi(#slash{E}_{T},#mu) [rad]");
			if (std::string::npos != title1.find("dPhiMETEl"))  h->GetXaxis()->SetTitle("#Delta#Phi(#slash{E}_{T},e) [rad]");
			if (std::string::npos != title1.find("dPhiMuMET"))  h->GetXaxis()->SetTitle("#Delta#Phi(#slash{E}_{T},#mu) [rad]");
			if (std::string::npos != title1.find("dPhiElMET"))  h->GetXaxis()->SetTitle("#Delta#Phi(#slash{E}_{T},e) [rad]");
			if (std::string::npos != title1.find("dPhiTauMET"))  h->GetXaxis()->SetTitle("#Delta#Phi(#slash{E}_{T},#tau) [rad]");
			if (std::string::npos != title1.find("dR_mutau"))  h->GetXaxis()->SetTitle("#Delta R(#mu,#tau)");
			if (std::string::npos != title1.find("dR_eltau"))  h->GetXaxis()->SetTitle("#Delta R(e,#tau)");
			if (std::string::npos != title1.find("dR_muel"))  h->GetXaxis()->SetTitle("#Delta R(#mu,e)");
			if (std::string::npos != title1.find("Centrality"))  h->GetXaxis()->SetTitle("Centrality");
			if (std::string::npos != title1.find("DZeta"))  h->GetXaxis()->SetTitle("D#zeta [GeV]");
			if (std::string::npos != title1.find("InvMassMuTau"))  h->GetXaxis()->SetTitle("M_{#mu,#tau} [GeV]");
			if (std::string::npos != title1.find("InvMassElTau"))  h->GetXaxis()->SetTitle("M_{e,#tau} [GeV]");
			if (std::string::npos != title1.find("InvMassMuEl"))  h->GetXaxis()->SetTitle("M_{#mu,e} [GeV]");


			if (std::string::npos != title1.find("MupT"))  h->GetXaxis()->SetTitle("P_{T}(#mu) [GeV]");
			if (std::string::npos != title1.find("mupT"))  h->GetXaxis()->SetTitle("P_{T}(#mu) [GeV]");
			if (std::string::npos != title1.find("ElpT"))  h->GetXaxis()->SetTitle("P_{T}(e) [GeV]");
			if (std::string::npos != title1.find("TaupT"))  h->GetXaxis()->SetTitle("P_{T}(#tau) [GeV]");
			if (std::string::npos != title1.find("LeppT"))  h->GetXaxis()->SetTitle("P_{T}(lepton) [GeV]");
			if (std::string::npos != title1.find("Mueta"))  h->GetXaxis()->SetTitle("|#eta|(#mu)");
			if (std::string::npos != title1.find("Eleta"))  h->GetXaxis()->SetTitle("|#eta|(e)");
			if (std::string::npos != title1.find("Taueta"))  h->GetXaxis()->SetTitle("|#eta|(#tau)");
			if (std::string::npos != title1.find("Lepeta"))  h->GetXaxis()->SetTitle("|#eta|(lepton)");
			if (std::string::npos != title1.find("METphi"))  h->GetXaxis()->SetTitle("#Phi(#slash{E}_{T}) [rad]");
			if (std::string::npos != title1.find("HTOsqrMET"))  h->GetXaxis()->SetTitle("H_{T}/#sqrt{#slash{E}_{T}}");
			if (std::string::npos != title1.find("MeffEl"))  h->GetXaxis()->SetTitle("M_{eff}(e,H_{T})");
			if (std::string::npos != title1.find("MeffMu"))  h->GetXaxis()->SetTitle("M_{eff}(#mu,H_{T})");
			if (std::string::npos != title1.find("MeffTau"))  h->GetXaxis()->SetTitle("M_{eff}(#tau,H_{T})");
			if (std::string::npos != title1.find("MeffElOsqrMET"))  h->GetXaxis()->SetTitle("M_{eff}(e,H_{T})/#sqrt{#slash{E}_{T}}");
			if (std::string::npos != title1.find("MeffMuonOsqrMET"))  h->GetXaxis()->SetTitle("M_{eff}(#mu,H_{T})/#sqrt{#slash{E}_{T}}");
			if (std::string::npos != title1.find("MeffTauOsqrMET"))  h->GetXaxis()->SetTitle("M_{eff}(#tau,H_{T})/#sqrt{#slash{E}_{T}}");
			if (std::string::npos != title1.find("npv"))  h->GetXaxis()->SetTitle("#PV");



//			sprintf(histotitle,"%s %s",title1,h->GetXaxis()->GetTitle());
//			 h->GetXaxis()->SetTitle(histotitle);
//			h->GetXaxis()->SetTitleOffset(0.8);
//			h->GetYaxis()->SetTitleOffset(1.3);
//			h->GetYaxis()->SetTitleSize(2);

			//h->SetLineColor (col);

			//h->SetFillColor (col);
			h->SetMinimum(0.001);
			h->SetLineStyle (col);


			h->SetFillColor(col);
			h->SetLineColor(col);




	//		cout<<"""""""""""""""""""""""""""""""""""""""""""""""""""""""""" <<h->GetName()<<"  "<<h->GetTitle()<<endl;
			ofstream tfile;
			string fname = h->GetName();
			string n_ = h->GetName();
			//float ev_ = 0;
			if (std::string::npos != n_.find("CutFlowUnW") ){

				//   cout<<" Counting from CutFlow 1 "<<h->GetSumOfWeights()<<endl;
				TString outname=title_;
				TString textfilename = "cutflow_"+outname +".txt";
				tfile.open(textfilename);

				tfile << "########################################" << endl;
				for (int b=0;b<25;b++){
					//ev_ += h->GetBinContent(b);
					//tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<" & "<<" & "<<endl;	
//					if (b>10 &&  std::string::npos != fname.find("TT_TuneCUETP8M2T4_13TeV-powheg-pythia8")) h->SetBinContent(b, h->GetBinContent(b) * h->GetBinContent(10) / h->GetBinContent(11));

					//if (h->GetBinContent(b) > 0. ) tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<endl;	
					//else tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<0<<endl;
					tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<fabs(h->GetBinContent(b))<<endl;

					//if (b==15) cout<<"  "<<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<endl;
					//cout <<title1<<" & "<<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<" & "<<" & "<<endl;	
				}
				// cout<<" Counting from CutFlow  "<<ev_<<endl;
			}
tfile.close();
string namet=h->GetName();



}





void OverFlow(TH1D *& h, int &last_bin){

	int nb = h->GetNbinsX();
	float over_ = h->GetBinContent(last_bin);
	float contlast = 0.;//h->GetBinContent(last_bin);
	for (int b=last_bin; b <= nb+1; b++) {contlast +=h->GetBinContent(b);h->SetBinContent(b,0.);}

	h->SetBinContent(last_bin,0);
	h->SetBinContent(last_bin,contlast);
}



