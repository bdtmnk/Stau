#include <cmath>
#include <sstream>
#include <iomanip>
#include "TChain.h"
#include "TH1.h"
#include "TH1D.h"
#include "THStack.h"
#include "TTree.h"
#include "TKey.h"
#include "Riostream.h"
#include "TCanvas.h"
#include "TFile.h"
#include "TH2.h"
#include "TH3.h"
#include "TLegend.h"
#include "TROOT.h"
#include "TFrame.h"
#include "TGaxis.h"
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


using namespace std;

void Impose( TDirectory *ttarget, TList *ssourcelist, string &np_legend , vector<string> titles_ ,vector<float> xsecs, string syst);
void ModifyHist (TH2D* &h, int cl_,float &w, float &lumi, string &title,bool norm=false);
void CheckHistZero (TH1D* &h1);			

void ModifyHist (TH2D* &h, int cl_ ,float & lumi,float & weight,string & title_,bool norm_){



			//h->SetMinimum(1);
			//h->GetXaxis()->SetNdivisions(512);
			string titlee=h->GetName();
			int col=1;//kOrange;
			string title1,title2;
			title1= h->GetTitle();

			//int nb = h->GetNbinsX();
			//float over_ = h->GetBinContent(nb+1);
			//float contlast = h->GetBinContent(nb);
			//h->SetBinContent(nb,contlast+over_);

			h->Scale(weight);


}

TH1D* WInclw,*W1Jw,*W2Jw,*W3Jw,*W4Jw;
TH1D* DYInclw,*DY1Jw,*DY2Jw,*DY3Jw,*DY4Jw;

void OverlapTF(string syst="Nominal")
{

	gROOT->SetStyle ("Plain");
	gStyle->SetPalette (1);
	gStyle->SetTextFont(22) ;
	gStyle->SetTitleFont(22,"xyz") ;
	gStyle->SetLabelFont(22,"xyz") ;

	vector <string> titles;
	TList *FileList;
	TFile *Target;
	titles.clear();
	int np=1;

	Float_t value=0;
	vector<float> xsecs_;
	ifstream ifs("TFsamples");
	string line;

	while(std::getline(ifs, line)) // read one line from ifs
	{
		istringstream iss(line); // access line as a stream
		string dataname;
		float XSec;	
		float xs,fact,fact2,fact3;
		xs=0;fact=1;fact2=1;fact3=1;
		iss >> dataname >> xs >> fact >> fact2 >> fact3;
		//titles.push_back(dataname+".root");
		if (std::string::npos == dataname.find("Single")) titles.push_back(dataname+"_"+syst+"_C.root");
		if (std::string::npos != dataname.find("Single") && (syst=="Nominal" || syst=="JetEnUp" || syst=="JetEnDown"  || syst=="ElEnUp" || syst=="ElEnDown" || syst=="MuEnUp" || syst=="MuEnDown" || syst=="UnclEnUp" || syst=="UnclEnDown" )) titles.push_back(dataname+"_"+syst+"_C.root");
		if (std::string::npos != dataname.find("Single") && !(syst=="Nominal" || syst=="JetEnUp" || syst=="JetEnDown" || syst=="ElEnUp" || syst=="ElEnDown" || syst=="MuEnUp" || syst=="MuEnDown" || syst=="UnclEnUp" || syst=="UnclEnDown" )) titles.push_back(dataname+"_Nominal_C.root");

		if (std::string::npos == dataname.find("Single")) titles.push_back(dataname+"_"+syst+"_D.root");
		if (std::string::npos != dataname.find("Single") && (syst=="Nominal" || syst=="JetEnUp" || syst=="JetEnDown"  || syst=="ElEnUp" || syst=="ElEnDown" || syst=="MuEnUp" || syst=="MuEnDown" || syst=="UnclEnUp" || syst=="UnclEnDown" )) titles.push_back(dataname+"_"+syst+"_D.root");
		if (std::string::npos != dataname.find("Single") && !(syst=="Nominal" || syst=="JetEnUp" || syst=="JetEnDown" || syst=="ElEnUp" || syst=="ElEnDown" || syst=="MuEnUp" || syst=="MuEnDown" || syst=="UnclEnUp" || syst=="UnclEnDown" )) titles.push_back(dataname+"_Nominal_D.root");

		XSec= xs*fact*fact2*fact3;
		
		cout<<" Found the correct cross section "<<xs<<" for Dataset "<<dataname<<" XSec "<<XSec<<"  "<<fact<<"  "<<fact2<<" "<<fact3<<endl;
		xsecs_.push_back(XSec);
		xsecs_.push_back(XSec);


	}

	string fout = "TransferFactor_"+syst+".root";
	FileList = new TList ();


	for (unsigned int i=0; i <titles.size();++i){

		cout<<" loading dataset "<<titles[i]<<endl;
		//string file=titles[i]+".root";
		string file=titles[i];
		FileList->Add (TFile::Open (file.c_str()));

	}

	    Target = TFile::Open (fout.c_str (), "RECREATE");
	    string np_title = titles[0];

            TString WInclname, W1Jname, W2Jname, W3Jname, W4Jname;
            TString DYInclname, DY1Jname, DY2Jname, DY3Jname, DY4Jname;
            TString app_ = "";
            TString s_ = "Nominal";

	    if (s_!="Nominal") app_=""+s_;
            WInclname = "WJetsToLNu_TuneCP5_13TeV-12Apr2018"+app_+"_Nominal_C.root";
            W1Jname = "W1JetsToLNu_TuneCP5_13TeV-12Apr2018"+app_+"_Nominal_C.root";
            W2Jname = "W2JetsToLNu_TuneCP5_13TeV-12Apr2018"+app_+"_Nominal_C.root";
            W3Jname = "W3JetsToLNu_TuneCP5_13TeV-12Apr2018"+app_+"_Nominal_C.root";
            W4Jname = "W4JetsToLNu_TuneCP5_13TeV-12Apr2018"+app_+"_Nominal_C.root";
            //W4Jname = "W3JetsToLNu_TuneCP5_13TeV-12Apr2018"+app_+"_Nominal_C.root";


            DYInclname = "DYJetsToLL_M-50_13TeV-12Apr2018"+app_+"_Nominal_C.root";
            DY1Jname = "DY1JetsToLL_M-50_13TeV-12Apr2018"+app_+"_Nominal_C.root";
            DY2Jname = "DY2JetsToLL_M-50_13TeV-12Apr2018"+app_+"_Nominal_C.root";
            DY3Jname = "DY3JetsToLL_M-50_13TeV-12Apr2018"+app_+"_Nominal_C.root";
            DY4Jname = "DY4JetsToLL_M-50_13TeV-12Apr2018"+app_+"_Nominal_C.root";

            TFile *WIncl = TFile::Open (WInclname, "read");
            TFile *W1J = TFile::Open (W1Jname, "read");
            TFile *W2J = TFile::Open (W2Jname, "read");
            TFile *W3J = TFile::Open (W3Jname, "read");
            TFile *W4J = TFile::Open (W4Jname, "read");

            TFile *DYIncl = TFile::Open (DYInclname, "read");
            TFile *DY1J = TFile::Open (DY1Jname, "read");
            TFile *DY2J = TFile::Open (DY2Jname, "read");
            TFile *DY3J = TFile::Open (DY3Jname, "read");
            TFile *DY4J = TFile::Open (DY4Jname, "read");

			TString Channel="mutau";
			DYInclw= (TH1D*)DYIncl->Get(Channel+"/histWeightsH");
			DY1Jw= (TH1D*)DY1J->Get(Channel+"/histWeightsH");
			DY2Jw= (TH1D*)DY2J->Get(Channel+"/histWeightsH");
			DY3Jw= (TH1D*)DY3J->Get(Channel+"/histWeightsH");
			DY4Jw= (TH1D*)DY4J->Get(Channel+"/histWeightsH");

			WInclw= (TH1D*)WIncl->Get(Channel+"/histWeightsH");
			W1Jw= (TH1D*)W1J->Get(Channel+"/histWeightsH");
			W2Jw= (TH1D*)W2J->Get(Channel+"/histWeightsH");
			W3Jw= (TH1D*)W3J->Get(Channel+"/histWeightsH");
			W4Jw= (TH1D*)W4J->Get(Channel+"/histWeightsH");

	Impose (Target, FileList, np_title,titles,xsecs_,syst);

	delete FileList;
	delete Target;
}


void Impose (TDirectory * target, TList * sourcelist, string & np_title_, vector<string> titles,vector<float> xsecs, string syst)

{
	cout << "	" << "========================================================" << endl;
	cout << "	" << "This is a macro to superimpose plots of different root files." << endl;
	cout << "	" << "Only TH1Dobjects are superimposed." << endl;
	cout << "	" << "Target path: " << target->GetPath () << endl;

	TString path ((char *) strstr (target->GetPath (), ":"));
	path.Remove (0, 2);

        //TFile *foutA = TFile::Open ("QCD_Nominal_A.root", "RECREATE");
        //TFile *foutC = TFile::Open ("QCD_Nominal_C.root", "RECREATE");
        //TFile *foutD = TFile::Open ("QCD_Nominal_D.root", "RECREATE");
	//foutA->mkdir("mutau");
	//foutC->mkdir("mutau");
	//foutD->mkdir("mutau");
	target->mkdir("mutau");

	float Lumi = 1.;
	Lumi = 38570.519400;
	//Lumi=58822.126;
	bool norm_=false;

	cout<<titles[0]<<"   "<<titles.size()<<endl;

	//not really useful if plots already weighted to lumi - usefull is plots are in a.u.
	vector <float > lumiweights;
	lumiweights.clear();
	vector <string> label_;
	vector <float> yieldA;
	vector <float> yieldC;
	vector <float> yieldD;
	yieldA.clear();
	yieldC.clear();
	yieldD.clear();

	vector <float> yieldAp;
	vector <float> yieldCp;
	vector <float> yieldDp;
	yieldAp.clear();
	yieldCp.clear();
	yieldDp.clear();

	TFile *first_source = (TFile *) sourcelist->First ();
	first_source->cd ("mutau");
	float norm=1.;
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

	TCanvas *c1 ;
	c1  = new TCanvas ("c1","c1",0,22,600,600);
	int count=0;
   

	 TH2D* hh[1000];
         TH2D* allRegA;
         TH2D* allbkgA;
         TH2D* allbkgC;
         TH2D* allbkgD;
         TH2D *allRegC;
         TH2D *allRegD;
         TH2D *hregA;
         TH2D *hregC;
         TH2D *hregD;

	while ((key = (TKey *) nextkey ())) {

		count++;
		//cout<<"Count: "<<count<<endl;
		// read object from first source file and create a canvas
		first_source->cd ("mutau");
		TObject *obj = key->ReadObj ();
		string nn = obj->GetName();

		//if ( string::npos == nn.find("nJet")  && (string::npos == nn.find("CutFlow"))) continue;
 		//if (string::npos == nn.find("DZeta1D_17") && string::npos == nn.find("CutFlow")) continue;
 		//if (string::npos == nn.find("IsoMu_12")) continue;
 		//if (string::npos == nn.find("CutFlow")) continue;
 		if (string::npos == nn.find("TauPtEta16")) continue;

 		cout<<"obj->IsA ()->InheritsFrom"<<obj->IsA ()->InheritsFrom ("TH2")<<endl;
		if (obj->IsA ()->InheritsFrom ("TH2") ) {
	
			c1->SetTitle(obj->GetName());
			// descendant of TH1D-> prepare the histograms to be superimposed

			TH2D* h1 = (TH2D*) obj;
			cout<<"h1->GetSumOfWeights()"<<h1->GetSumOfWeights()<<endl;

			if (h1->GetSumOfWeights()<0.001) continue;

			ModifyHist (h1,1,Lumi,lumiweights[0],titles[0],norm_);
			cout<<"first_source"<<first_source<<endl;
			TFile *nextsource = (TFile *) sourcelist->After (first_source);

			Int_t cl=0;
			cl=1;
			h1->SetStats(000000);
			h1->SetLineWidth(5);
 
	               cout <<"begin  "<< h1->GetSumOfWeights() << " cl :"<<cl<<endl;
			hh[cl]=h1;

			if ((int)cl==1){	
				allRegC  = (TH2D*) hh[1]->Clone();
				hregC  = (TH2D*) hh[1]->Clone();
				allbkgC  = (TH2D*) hh[1]->Clone();
				allbkgC->Reset();
			}

			string regA, regB,regC,regD;

			string sn="stau";string sdata="Single";
			string qcd="QCD_DataDriven";
			regA="_A ";
			regC="_C ";
			regD="_D ";
			while (nextsource) {

				string fname= nextsource->GetName();
				//cout<<"FNAME: "<<fname<<endl;
				bool flagg= false;
				if (std::string::npos != fname.find(qcd) || std::string::npos != fname.find(sdata)) flagg=true;
				//cout<<"FName  "<<fname<<endl;
				nextsource->cd("mutau");
				TH1D* eventCountt ;
				eventCountt = (TH1D*)nextsource->Get("mutau/histWeightsH");
			   //if  ( std::string::npos == fname.find("TT_TuneCUETP8M2T4_13TeV-powheg-pythia8"))
			   //eventCountt = (TH1D*)nextsource->Get("mutau/histWeightsH");
			   //if ( std::string::npos != fname.find("TT_TuneCUETP8M2T4_13TeV-powheg-pythia8") )
			   //eventCountt = (TH1D*)nextsource->Get("mutau/histTopPt");

				float normm =1.;
				//TH1D* hxsecc = (TH1D*)nextsource->Get("mutau/xsec");
				float xsecc = xsecs[cl];
				//float xsecc = hxsecc->GetMean();

				float nGenn = eventCountt->GetSumOfWeights();

				normm = float(xsecc*Lumi) / float(nGenn);

				if (flagg) { xsecc=1;normm =1.;}

				  
					if (std::string::npos != fname.find("WJetsToLNu_TuneCP5_13TeV-12Apr2018_1Parton") || std::string::npos != fname.find("W1JetsToLNu_TuneCP5_13TeV-12Apr2018"))
						normm = Lumi/ ( WInclw->GetSumOfWeights()/float(61526.7*0.8853) + W1Jw->GetSumOfWeights()/float(1.221*9644.5*0.8853));

					if (std::string::npos != fname.find("WJetsToLNu_TuneCP5_13TeV-12Apr2018_2Parton") || std::string::npos != fname.find("W2JetsToLNu_TuneCP5_13TeV-12Apr2018"))
						normm = Lumi/ ( WInclw->GetSumOfWeights()/float(61526.7*0.8853) + W2Jw->GetSumOfWeights()/float(1.221*3144.5*0.8853));
				
					if (std::string::npos != fname.find("WJetsToLNu_TuneCP5_13TeV-12Apr2018_3Parton") || std::string::npos != fname.find("W3JetsToLNu_TuneCP5_13TeV-12Apr2018"))
						normm = Lumi/ ( WInclw->GetSumOfWeights()/float(61526.7*0.8853) + W3Jw->GetSumOfWeights()/float(1.221*954.8*0.8853));

					if (std::string::npos != fname.find("WJetsToLNu_TuneCP5_13TeV-12Apr2018_4Parton") || std::string::npos != fname.find("W4JetsToLNu_TuneCP5_13TeV-12Apr2018"))
						normm = Lumi/ ( WInclw->GetSumOfWeights()/float(61526.7*0.8853) + W4Jw->GetSumOfWeights()/float(1.221*485.6*0.8853));


					if (std::string::npos != fname.find("DYJetsToLL_M-50_13TeV-12Apr2018_1Parton") || std::string::npos != fname.find("DYJetsToLL_M-50_13TeV-12Apr2018_isZTT_1Parton") || std::string::npos != fname.find("DY1JetsToLL_M-50_13TeV-12Apr2018"))
						normm = Lumi/ ( float(DYInclw->GetSumOfWeights())/float(5765.4*0.9611) + float(DY1Jw->GetSumOfWeights())/float(1.1637*1012.5*0.9611));


					if (std::string::npos != fname.find("DYJetsToLL_M-50_13TeV-12Apr2018_2Parton") || std::string::npos != fname.find("DYJetsToLL_M-50_13TeV-12Apr2018_isZTT_2Parton") || std::string::npos != fname.find("DY2JetsToLL_M-50_13TeV-12Apr2018"))
						normm = Lumi/ ( DYInclw->GetSumOfWeights()/float(5765.4*0.9611) + float(DY2Jw->GetSumOfWeights())/float(1.1637*332.8*0.9611));

					if (std::string::npos != fname.find("DYJetsToLL_M-50_13TeV-12Apr2018_3Parton") || std::string::npos != fname.find("DYJetsToLL_M-50_13TeV-12Apr2018_isZTT_3Parton") || std::string::npos != fname.find("DY3JetsToLL_M-50_13TeV-12Apr2018"))
						normm = Lumi/ ( DYInclw->GetSumOfWeights()/float(5765.4*0.9611) + float(DY3Jw->GetSumOfWeights())/float(1.1637*101.8*0.9611));

					if (std::string::npos != fname.find("DYJetsToLL_M-50_13TeV-12Apr2018_4Parton") || std::string::npos != fname.find("DYJetsToLL_M-50_13TeV-12Apr2018_isZTT_4Parton") || std::string::npos != fname.find("DY4JetsToLL_M-50_13TeV-12Apr2018"))
						normm = Lumi/ ( DYInclw->GetSumOfWeights()/float(5765.4*0.9611) + float(DY4Jw->GetSumOfWeights())/float(1.1637*54.8*0.9611));


				lumiweights.push_back(normm);

				TKey *key2 = (TKey *) gDirectory->GetListOfKeys ()->FindObject (h1->GetName ());

				if (key2) {
					cl++;
					TH2D *h2;

					h2 = (TH2D*) key2->ReadObj ();
					h2->SetLineWidth(4);
					ModifyHist (h2, cl,Lumi,lumiweights[cl-1],titles[cl-1],norm_);
					h2->SetStats(0);
					hh[(int)cl] = h2;

					if ((int)cl==2 ){	
						allRegD  = (TH2D*) h2->Clone();
						allbkgD  = (TH2D*) h2->Clone();
						allbkgD->Reset();
					}

			               cout <<fname<<"   "<<h2->GetSumOfWeights()  <<endl;
		                       cout<<"Binning X:"<<h2->GetNbinsX()<<endl;
				       cout<<"Binning Y:"<<h2->GetNbinsY()<<endl;
				       double int_ = allRegC->GetSumOfWeights();
				
                                	if ((int)cl>2 && h2->GetSumOfWeights()>0.)  {


						if (std::string::npos != fname.find("_C.root") ) {
							allRegC->Add(h2,-1);
							allbkgC->Add(h2,1);
							cout <<"Add:"<< fname << "   "<< allRegC->GetSumOfWeights() <<endl;
							}

						if (std::string::npos != fname.find("_D.root") ) {
						
							allRegD->Add(h2,-1);
							allbkgD->Add(h2,1);
							cout <<"Add:"<<fname << "   "<< allRegD->GetSumOfWeights() <<endl;

							}

					}

				}
				nextsource = (TFile *) sourcelist->After (nextsource);
				}
				// while ( nextsource )
			}
			if (!obj->IsA ()->InheritsFrom ("TH2") ) continue;
			//if (obj->IsA ()->InheritsFrom ("TH2") ) continue;
			//if (obj->IsA ()->InheritsFrom ("TH3") ) continue;
			//if (obj->IsA ()->InheritsFrom ("TTree") ) continue;
				cout  << "final C   "<< allRegC->GetSumOfWeights() <<endl;
				cout  << "final D  "<< allRegD->GetSumOfWeights() <<endl;
				target->cd ("mutau");

				TH2D * ratio = (TH2D*) allRegC->Clone();
				ratio->SetMarkerColor(kBlack);
				ratio->SetLineColor(kBlack);
				ratio->SetStats(0);
				ratio->Divide(allRegD);
				
				allRegC->Write();
				allRegD->Write();

				ratio->Write();

	ofstream fout;
        fout.open("TransferFactor.txt", ios_base::app);
        
        fout<<" if ( working_point == "<< '"'<< syst << '"'<< "){" <<endl;

	fout<<" if (  fabs(eta) < 0.8 )" <<endl;
        fout<<" {" <<endl;
        fout<<"        if (pt>30 && pt<40) SF = "<<ratio->GetBinContent(2,1)<<";" <<endl;
        fout<<" }" <<endl;

	fout<<" if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )" <<endl;
        fout<<" {" <<endl;
        
        fout<<"        if (pt>30 && pt<40) SF = "<<ratio->GetBinContent(2,2)<<";" <<endl;

	fout<<" }" <<endl;

	fout<<" if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 && pt<40)" <<endl;
        fout<<" {" <<endl;
        /*
		ratio->SetBinContent(1,3, (allRegC->GetBinContent(1,3)+allRegC->GetBinContent(2,3))/(allRegD->GetBinContent(1,3)+allRegD->GetBinContent(2,3)));
		*/
		double error1 = allRegC->GetBinError(1,3);
		double error2 = allRegC->GetBinError(2,3);
		double error3 = allRegC->GetBinError(3,3);
		double error4 = allRegD->GetBinError(1,3);
		double error5 = allRegD->GetBinError(2,3);
		double error6 = allRegD->GetBinError(3,3);
		
		double errorC = sqrt(error1*error1+error2*error2+error3*error3)/(error1*error1+error2*error2+error3*error3);
		double errorD = sqrt(error4*error4+error5*error5+error6*error6)/(error4*error4+error5*error5+error6*error6);

        //cout << errorC<<endl;
        //cout << errorD<<endl;

	ratio->SetBinError(2,3, ratio->GetBinContent(2,3));//*sqrt(errorC*errorC+errorD*errorD));
        fout<<"         if (pt>30 && pt<40) SF = "<<ratio->GetBinContent(2,3)<<";" <<endl;
	 fout<<" }" <<endl;
	fout<<" if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )" <<endl;
        fout<<" {" <<endl;

        fout<<"         if (pt>30 && pt<40) SF = "<<ratio->GetBinContent(2,4)<<";" <<endl;
        fout<<" }" <<endl;
        
        
        ratio->SetBinContent(3,1, (allRegC->GetBinContent(3,1)+allRegC->GetBinContent(3,2)+
        allRegC->GetBinContent(3,3)+allRegC->GetBinContent(3,4))/(allRegD->GetBinContent(3,1)+allRegD->GetBinContent(3,2)+allRegD->GetBinContent(3,3)+allRegD->GetBinContent(3,4)));

        ratio->SetBinContent(4,1, (allRegC->GetBinContent(4,1)+allRegC->GetBinContent(4,2)+
        allRegC->GetBinContent(4,3)+allRegC->GetBinContent(4,4))/(allRegD->GetBinContent(4,1)+allRegD->GetBinContent(4,2)+allRegD->GetBinContent(4,3)+allRegD->GetBinContent(4,4)));

        ratio->SetBinContent(5,1, (allRegC->GetBinContent(5,1)+allRegC->GetBinContent(5,2)+
        allRegC->GetBinContent(5,3)+allRegC->GetBinContent(5,4))/(allRegD->GetBinContent(5,1)+allRegD->GetBinContent(5,2)+allRegD->GetBinContent(5,3)+allRegD->GetBinContent(5,4)));

	//float pt_cut = ratio->GetBinContent(3,1);
	fout<<"    if (pt>40 && pt<70) SF = "<< ratio->GetBinContent(3,1)<<";" <<endl;
        fout<<"    if (pt>70 && pt<110) SF = " << ratio->GetBinContent(4,1)<<";" <<endl;
        fout<<"    if (pt>110) SF = "          << ratio->GetBinContent(5,1)<<";" <<endl;
    	fout<<"}"<<endl;
        
	cout<<"    if (pt>20 && pt<30) SF = "<< ratio->GetBinContent(1,2)<<";" <<endl;
        cout<<"    if (pt>30 && pt<40) SF = "<< ratio->GetBinContent(2,2)<<";" <<endl;
        cout<<"    if (pt>40 && pt<70) SF = "<< ratio->GetBinContent(3,2)<<";" <<endl;
        cout<<"    if (pt>70 && pt<110) SF = " << ratio->GetBinContent(4,2)<<";" <<endl;
        cout<<"    if (pt>110) SF = "          << ratio->GetBinContent(5,2)<<";" <<endl;

	cout<<"    if (pt>20 && pt<30) SF = "<< ratio->GetBinContent(1,3)<<";" <<endl;
        cout<<"    if (pt>30 && pt<40) SF = "<< ratio->GetBinContent(2,3)<<";" <<endl;
        cout<<"    if (pt>40 && pt<70) SF = "<< ratio->GetBinContent(3,3)<<";" <<endl;
        cout<<"    if (pt>70 && pt<110) SF = " << ratio->GetBinContent(4,3)<<";" <<endl;
        cout<<"    if (pt>110) SF = "          << ratio->GetBinContent(5,3)<<";" <<endl;

	cout<<"    if (pt>20 && pt<30) SF = "<< ratio->GetBinContent(1,4)<<";" <<endl;
        cout<<"    if (pt>30 && pt<40) SF = "<< ratio->GetBinContent(2,4)<<";" <<endl;
        cout<<"    if (pt>40 && pt<70) SF = "<< ratio->GetBinContent(3,4)<<";" <<endl;
        cout<<"    if (pt>70 && pt<110) SF = " << ratio->GetBinContent(4,4)<<";" <<endl;
        cout<<"    if (pt>110) SF = "          << ratio->GetBinContent(5,4)<<";" <<endl;

        cout<<"    if (pt>20 && pt<30) SF = "<< ratio->GetBinContent(1,5)<<";" <<endl;
        cout<<"    if (pt>30 && pt<40) SF = "<< ratio->GetBinContent(2,5)<<";" <<endl;
        cout<<"    if (pt>40 && pt<70) SF = "<< ratio->GetBinContent(3,5)<<";" <<endl;
        cout<<"    if (pt>70 && pt<110) SF = " << ratio->GetBinContent(4,5)<<";" <<endl;
        cout<<"    if (pt>110) SF = "          << ratio->GetBinContent(5,5)<<";" <<endl;
	fout<<" "<<endl;
        fout.close();
	cout<<"if (  fabs(eta) < 0.8 )" <<endl;
        cout<<"    if (pt>30 && pt<40) SF = "<<ratio->GetBinError(2,1)<<";" <<endl;
        cout<<"    if (pt>40 && pt<70) SF = "<<ratio->GetBinError(3,1)<<";" <<endl;
        cout<<"    if (pt>70 && pt<110 ) SF = "<<ratio->GetBinError(4,1)<<";" <<endl;
        cout<<"    if (pt>110 ) SF = "        <<ratio->GetBinError(5,1)<<";" <<endl;
	cout<<"if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )" <<endl;
        cout<<"   if (pt>20 && pt<30) SF = "<<ratio->GetBinError(2,2)<<";" <<endl;
        cout<<"   if (pt>30 && pt<40) SF = "<<ratio->GetBinError(3,2)<<";" <<endl;
        cout<<"   if (pt>40 ) SF = "<<ratio->GetBinError(4,2)<<";" <<endl;
        cout<<"   if (pt>70 ) SF = "<<ratio->GetBinError(5,2)<<";" <<endl;

	cout<<" if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )" <<endl;
        cout<<"        if (pt>30 && pt<40) SF = "<<ratio->GetBinError(2,3)<<";" <<endl;
        cout<<"         if (pt>40 && pt<70) SF = "<<ratio->GetBinError(3,3)<<";" <<endl;
        cout<<"         if (pt>70 && pt<110 ) SF = "<<ratio->GetBinError(4,3)<<";" <<endl;
        cout<<"         if (pt>110 ) SF = "<<ratio->GetBinError(5,3)<<";" <<endl;

	cout<<" if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )" <<endl;
        cout<<"        if (pt>30 && pt<40) SF = "<<ratio->GetBinError(2,4)<<";" <<endl;
        cout<<"         if (pt>40 && pt<70) SF = "<<ratio->GetBinError(3,4)<<";" <<endl;
        cout<<"         if (pt>40 && pt<110) SF = "<<ratio->GetBinError(4,4)<<";" <<endl;
        cout<<"         if (pt>110 ) SF = "<<ratio->GetBinError(5,4)<<";" <<endl;

			
		if (obj->IsA ()->InheritsFrom ("TH1")) {

				TH1F* v1 = new TH1F("", "", 1, 0, 1);v1->SetLineWidth(2);
				TH1F* v2 = new TH1F("", "", 1, 0, 1);v2->SetLineWidth(2);
				TH1F* v3 = new TH1F("", "", 1, 0, 1);v3->SetLineWidth(2);
				TH1F* v4 = new TH1F("", "", 1, 0, 1);v4->SetLineWidth(2);

				hh[1]->SetLineColor(kGreen-2);
				hh[1]->SetLineWidth(2);
				hh[1]->SetLineStyle(2);
				hh[1]->SetMarkerStyle(34);
				hh[1]->SetMarkerColor(kGreen-2);
				hh[1]->SetMarkerSize(0.8);


				hh[2]->SetLineColor(kBlue);
				hh[2]->SetMarkerStyle(27);
				hh[2]->SetMarkerColor(kBlue);
				allRegC->SetLineColor(kBlue);
				allRegC->SetMarkerStyle(27);
				allRegC->SetMarkerColor(kBlue);

				hh[3]->SetMarkerStyle(32);
				hh[3]->SetMarkerColor(kOrange-1);
				hh[3]->SetLineColor(kOrange-1);
				allRegD->SetMarkerStyle(32);
				allRegD->SetMarkerColor(kOrange-1);
				allRegD->SetLineColor(kOrange-1);


				//legend_c1->SetNColumns(3);
				TPad *pad1 = new TPad("pad1","pad1",0,0.25,1,1);
				TPad *pad1r = new TPad("pad1","pad1",0.5,0.25,1,1);

				TPad *pad2 = new TPad("pad2","pad2",0,0,1,0.249);


				pad1->SetTopMargin(0.1);
				pad1->SetBottomMargin(0.1);
				pad1->SetRightMargin(0.05);
				//pad1->SetGridy();
				pad1r->SetBottomMargin(0.07);
				pad1r->SetRightMargin(0.05);
				pad1r->SetGridy();

				pad2->SetBottomMargin(0.05);


				pad2->SetTopMargin(0);
				pad2->SetBottomMargin(0.25);
				pad2->SetRightMargin(0.05);


				c1->cd();


				c1->Clear();

				pad1->SetLogy();
				pad1->Draw();
				pad2->Draw();

				pad2->SetGridy(1);

				pad1->cd();
				pad1->Clear();
				char namee[100];

				sprintf(namee,"%s",key->GetName ());
			//	CheckHistZero(allRegA);
			//	CheckHistZero(allRegC);
			//	CheckHistZero(allRegD);

			    if ( string::npos != nn.find("CutFlow")  ) {			
				allRegC->Sumw2();
				allRegD->Sumw2();
				}

            cout<<"!!!!!!!!!!!  "<<endl;
            cout  << "final C   "<< allRegC->GetSumOfWeights() <<endl;
            cout  << "final D  "<< allRegD->GetSumOfWeights() <<endl;

            double nd = allRegD->GetSumOfWeights();
            double nc = allRegC->GetSumOfWeights();

			//if (string::npos != nn.find("METLowDzeta_17")) 
            cout  << "final C   "<< nc <<endl;
            cout  << "final D  "<< nd <<endl;

    		//if (nc>0 && nd >0 && allRegA->GetSumOfWeights()>0)	allRegA->Scale(double(nc/nd));
	    	//if (nc<0 || nd<0 || allRegA->GetSumOfWeights()<0) allRegA->Scale(0.);

            //if (nd>0) cout<<"allRegA  "<<allRegA->GetSumOfWeights()<<" ratio is nd "<<nd<<" nc "<<nc<<" nc/nd "<<double(nc/nd)<<endl;//"  and different approach  "<<hregA->GetSumOfWeights()<<"  "<<double(Anc/And)<<endl;
            //hh[1]->SetMinimum(1);
            allRegC->SetMinimum(1);
            allRegC->SetMaximum(500*allRegC->GetMaximum());
            //for (int nb=1;nb<=allRegA->GetNbinsX();++nb)cout <<allRegA->GetXaxis()->GetBinLabel(nb)<<"  "<<allRegA->GetBinContent(nb)<<"  "<<allRegC->GetBinContent(nb)<<"  "<< allRegD->GetBinContent(nb)<<endl;
            allRegC->SetMarkerSize(1.5);
            allRegC->Draw("p hist");
            //allRegC->Draw("p hist sames");
            allRegD->Draw("p hist sames");

            //allRegA->GetXaxis()->SetRange(allRegA->FindFirstBinAbove(0),allRegA->FindLastBinAbove(1));
            allRegC->GetXaxis()->SetRange(2,18);
            //allRegC->GetXaxis()->SetRange(2,19);
            //allRegD->GetXaxis()->SetRange(2,19);

            string nnn = obj->GetName();
			/*	if (std::string::npos != nnn.find("nJet"))  {
					yieldA.push_back(allRegA->GetSumOfWeights());
					yieldC.push_back(allRegC->GetSumOfWeights());
					yieldD.push_back(allRegD->GetSumOfWeights());
					yieldAp.push_back(allRegA->GetSumOfWeights()/(allRegA->GetSumOfWeights()+allbkgA->GetSumOfWeights()));
					yieldCp.push_back(allRegC->GetSumOfWeights()/(allRegC->GetSumOfWeights()+allbkgC->GetSumOfWeights()));
					yieldDp.push_back(allRegD->GetSumOfWeights()/(allRegD->GetSumOfWeights()+allbkgD->GetSumOfWeights()));
				}*/

				c1->SetFillColor(0);
				c1->SetBorderMode(0);
				c1->SetBorderSize(0);
				c1->SetFrameBorderMode(0);
				c1->SetBorderSize(0);
				pad1->SetFrameLineColor(0);;
				pad1r->SetFrameLineColor(0);;

				pad2->cd();


				TH1D * _ratio = (TH1D*) allRegC->Clone();
				_ratio->SetMarkerColor(kBlack);
				_ratio->SetLineColor(kBlack);
				_ratio->SetStats(0);
				_ratio->Divide(allRegD);

				_ratio->SetMarkerStyle(7);
				_ratio->SetMaximum( 1.5 );
				_ratio->SetMinimum( 0.5 );
				_ratio->GetYaxis()->SetTitle("");
				_ratio->SetTitleSize(0);
				_ratio->SetMarkerSize(0.25);
				_ratio->SetMarkerColor(39);
				_ratio->SetLineWidth(1);
				_ratio->GetYaxis()->SetNdivisions(5);

				_ratio->GetXaxis()->SetNdivisions(545);
				_ratio->GetXaxis()->SetLabelSize(0.1);
				_ratio->GetXaxis()->SetTitleSize(0.12);
				_ratio->GetXaxis()->SetTitleOffset(0.85);

				_ratio->GetYaxis()->SetLabelSize(0.1);
				_ratio->GetYaxis()->SetLabelSize(0.15);
				_ratio->GetYaxis()->SetTitleSize(0.12);
				_ratio->GetYaxis()->SetTitleOffset(0.35);
				_ratio->GetYaxis()->SetTitle("N_{C}/N_{D}");


				_ratio->SetTitleFont(62);

				_ratio->GetXaxis()->SetNdivisions(510);
				_ratio->SetTitle("");
				_ratio->Draw("ep");

				TAxis *axis = allRegC->GetXaxis();



				gPad->RedrawAxis();
				gPad->Modified();
				gPad->Update();
				c1->SetName(obj->GetName());
				c1->SetTitle(obj->GetName());
				c1->Update();
				c1->cd();
				c1->Modified();
				c1->cd();
				c1->Update();


			
				string nn = obj->GetName();

				target->cd ("mutau");

				c1->Write();
				c1->Print("TransferFactor_mutau.pdf");
				
				/*foutA->cd("mutau");
				allRegA->Scale(nd/nc);
				allRegA->Write();
				
				foutC->cd("mutau");
				allRegC->Write();
				
				foutD->cd("mutau");
				allRegD->Write();*/




			}

		}
	// while ( ( TKey *key = (TKey*)nextkey() ) )
    // save modifications to target file

    // for (int i=0;i<SValueVariables_.size();i++){
    //cout<<SValueVariables_[i].second<<endl;}
    target->SaveSelf (kTRUE);
    target->Write();
    /*foutA->SaveSelf (kTRUE);
    foutA->Write();
    foutC->SaveSelf (kTRUE);
    foutC->Write();
    foutD->SaveSelf (kTRUE);
    foutD->Write();*/
    //TH1::AddDirectory (status);
    //cout << "	" << "========================================================" << endl;
    //cout<< " Ended SuperImpose of files.... " <<endl;
	/*ofstream tfile;
	TFile * filee = new TFile("QCD_Nominal_B.root","update");
	filee->cd("mutau");
	//target->ls();
	TH1D * hcut = (TH1D*)filee->Get("mutau/CutFlowUnW");
	
	for (int nb=0;nb<yieldA.size();++nb)
		cout<<hcut->GetXaxis()->GetBinLabel(nb+2)<<"  "<<yieldA[nb]<<"  "<<yieldC[nb]<<"  "<<yieldD[nb]<<"  "<<yieldC[nb]/yieldD[nb]<<" pA "<<yieldAp[nb]<<" pC "<<yieldCp[nb]<<" pD "<<yieldDp[nb]<<endl;	

	cout<<" Comparing  "<<hcut->GetNbinsX()<<"  "<<yieldA.size()<<endl;
	//if (std::string::npos != title1.find("Cut Flow") ){
	TString textfilename = "cutflow_QCD.txt";
	tfile.open(textfilename);

	tfile << "########################################" << endl;
	tfile << " No Cut  & 0" << endl;
//	tfile << " No Cut after PU & 0" << endl;
	for (int b=0;b<yieldA.size();b++){
		//for (int b=0;b<19;b++){
		//tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<" & "<<" & "<<endl;	
		//if (h->GetBinContent(b) > 0 ) 
		tfile <<hcut->GetXaxis()->GetBinLabel(b+2)<<" & "<<yieldA[b]<<endl;	
		//else tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<0<<endl;	
		//cout <<title1<<" & "<<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<" & "<<" & "<<endl;	
	}
	//}
	tfile.close();

	for (int b=0;b<yieldA.size();b++){

		cout<<" was  "<<hcut->GetXaxis()->GetBinLabel(b+2)<<" content "<<hcut->GetBinContent(b+2)<<" will be "<<yieldA[b]<<endl;
		hcut->SetBinContent(b+2,yieldA[b]);
	}
	
	filee->cd("mutau");
	hcut->Write();*/


	}



void
CheckHistZero (TH1D* &h)
{


                        for (int nb=0;nb<=h->GetNbinsX();++nb)
                        {
                                float bc_ = h->GetBinContent(nb);

                        if (bc_ <=0.) h->SetBinContent(nb,0.0001);
                        float SoW = h->GetSumOfWeights();
                        int En = h->GetEntries();
                        if (bc_ <=0.) h->SetBinError(nb,float(SoW/En));
                        }


}


//WW_TuneCP5_13TeV-pythia8_Nominal_D.root
//WW_TuneCP5_13TeV-pythia8_Nominal_C.root


