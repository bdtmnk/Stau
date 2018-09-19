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


void FixBoxPadding(TPad *pad, TBox *box, TH1D* &h1, double frac);

void FixOverlay();
void FixTopRange(TPad *pad, TH1D* &h1, double fix_y, double fraction);
ReBin(TH1* &h);
TCanvas *modifyCanvas (TCanvas *c1);
TCanvas *example_plot(int iPeriod, int iPos , TString name);


int mycolor=TColor::GetColor("#ffcc66");
int mycolorvv=TColor::GetColor("#8646ba");
//int mycolorww=TColor::GetColor("#6F2D35");
//int mycolorvv=TColor::GetColor("#FF6633");
int mycolorqcd=TColor::GetColor("#33CCFF");
//int mycolorqcd=TColor::GetColor("#ffccff");
//int mycolorqcd=TColor::GetColor("#de5a6a");
int mycolortt=TColor::GetColor("#9999cc");
//int mycolorttx=TColor::GetColor("#bbccdd");
int mycolorttx=TColor::GetColor("#33CCFF");
int mycolorwjet=TColor::GetColor("#de5a6a");
//int mycolorwjet=TColor::GetColor("#66CC66");
int mycolordyj=TColor::GetColor("#ffcc66");
int mycolorztt=TColor::GetColor("#58d885");
int mycolorst=TColor::GetColor("#b6d0ea");

int mycolorww=TColor::GetColor("#C390D4");


TH1D* WInclw,*W1Jw,*W2Jw,*W3Jw,*W4Jw;
TH1D* DYInclw,*DY1Jw,*DY2Jw,*DY3Jw,*DY4Jw;


	bool norm_=false;
	bool SO_=true;
	bool WDD=true;
	bool QCDMC=false;
	bool drawData=true;
	TString Channel="mutau";
void OverlapAllSyst(TString var= "BDTmutau_stau100_LSP1My_15")
{
	setTDRStyle();

	writeExtraText = true;       // if extra text
	extraText  = "Preliminary";  // default extra text is "Preliminary"
	lumi_8TeV  = "19.1 fb^{-1}"; // default is "19.7 fb^{-1}"
	lumi_7TeV  = "4.9 fb^{-1}";  // default is "5.1 fb^{-1}"
	lumi_sqrtS = "13 TeV";       // used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

	int iPeriod = 3;    // 1=7TeV, 2=8TeV, 3=7+8TeV, 7=7+8+13TeV, 0=free form (uses lumi_sqrtS)

	

	
	  TFile *file = TFile::Open ("ST/cards_mt/Var_"var+"_35invfb_mt_SR_out.root", "read");
  TH1D * data_obs = (TH1D*)file->Get("data_obs_var");
  TH1D * tt = (TH1D*)file->Get("tt_var");
  TH1D * wj = (TH1D*)file->Get("wj_var");
  TH1D * dyj = (TH1D*)file->Get("dyj_var");
  TH1D * ztt = (TH1D*)file->Get("ztt_var");
  TH1D * dib = (TH1D*)file->Get("dib_var");
  TH1D * ww = (TH1D*)file->Get("ww_var");
  TH1D * ttx = (TH1D*)file->Get("ttx_var");
  TH1D * sT = (TH1D*)file->Get("sT_var");
  TH1D * fakes = (TH1D*)file->Get("fakes_var");
  TH1D * rest = (TH1D*)file->Get("rest_var");
	
	
	
	
	
	  TH1D * ttUp, wjUp, dyjUp, zttUp, dibUp, wwUp, ttxUp, sTUp, fakesUp, restUp;
	  TH1D * ttDown, wjDown, dyjDown, zttDown, dibDown, wwDown, ttxDown, sTDown, fakesDown, restDown;
	
	
	TH1D * ratioErr  = (TH1D*) data_obs->Clone("ratioErr");
  TH1D * allbkg = (TH1D*)tt->Clone("total_background");
  allbkg->Add(wj);
  allbkg->Add(dyj);
  allbkg->Add(ztt);
  allbkg->Add(dib);
  allbkg->Add(ww);
  allbkg->Add(ttx);
  allbkg->Add(sT);
  allbkg->Add(fakes);	
	
	
	ifstream ifs("listSyst");
		string line;
	while(std::getline(ifs, line)) // read one line from ifs
	{
		istringstream iss(line); // access line as a stream
		string syst;
		iss >> syst ;
		TString Tsyst = syst;
		cout<<" Syst "<<syst<<endl;
		
		TH1D * ttUp = (TH1D*)file->Get("tt_var_"+Tsyst+"Up");
		TH1D * wjUp = (TH1D*)file->Get("wj_var_"+Tsyst+"Up");
		TH1D * dyjUp = (TH1D*)file->Get("dyj_var_"+Tsyst+"Up");
		TH1D * zttUp = (TH1D*)file->Get("ztt_var_"+Tsyst+"Up");
		TH1D * dibUp = (TH1D*)file->Get("dib_var_"+Tsyst+"Up");
		TH1D * wwUp = (TH1D*)file->Get("ww_var_"+Tsyst+"Up");
		TH1D * ttxUp = (TH1D*)file->Get("ttx_var_"+Tsyst+"Up");
		TH1D * sTUp = (TH1D*)file->Get("sT_var_"+Tsyst+"Up");
		TH1D * fakesUp = (TH1D*)file->Get("fakes_var_"+Tsyst+"Up");
		TH1D * restUp = (TH1D*)file->Get("rest_var_"+Tsyst+"Up");
		
		TH1D * ttDown = (TH1D*)file->Get("tt_var_"+Tsyst+"Down");
		TH1D * wjDown = (TH1D*)file->Get("wj_var_"+Tsyst+"Down");
		TH1D * dyjDown = (TH1D*)file->Get("dyj_var_"+Tsyst+"Down");
		TH1D * zttDown = (TH1D*)file->Get("ztt_var_"+Tsyst+"Down");
		TH1D * dibDown = (TH1D*)file->Get("dib_var_"+Tsyst+"Down");
		TH1D * wwDown = (TH1D*)file->Get("ww_var_"+Tsyst+"Down");
		TH1D * ttxDown = (TH1D*)file->Get("ttx_var_"+Tsyst+"Down");
		TH1D * sTDown = (TH1D*)file->Get("sT_var_"+Tsyst+"Down");
		TH1D * fakesDown = (TH1D*)file->Get("fakes_var_"+Tsyst+"Down");
		TH1D * restDown = (TH1D*)file->Get("rest_var_"+Tsyst+"Down");
		
		   TH1D * allbkgUp = (TH1D*)ttUp->Clone("total_background");
			allbkgUp->Add(wjUp);
			allbkgUp->Add(dyjUp);
			allbkgUp->Add(zttUp);
			allbkgUp->Add(dibUp);
			allbkgUp->Add(wwUp);
			allbkgUp->Add(ttxUp);
			allbkgUp->Add(sTUp);
			allbkgUp->Add(fakesUp);
			
			TH1D * allbkgDown = (TH1D*)ttDown->Clone("total_background");
			allbkgDown->Add(wjDown);
			allbkgDown->Add(dyjDown);
			allbkgDown->Add(zttDown);
			allbkgDown->Add(dibDown);
			allbkgDown->Add(wwDown);
			allbkgDown->Add(ttxDown);
			allbkgDown->Add(sTDown);
			allbkgDown->Add(fakesDown);
			
			 int nBins = tt->GetNbinsX();

			for (int iB=1; iB<=nBins; ++iB) 
			{
				float eStat	= allbkg->GetBinError(iB);
				eSyst_JUp = TMath::Abs(allbkgUp->GetBinContent(iB)- allbkg->GetBinContent(iB));
				eSyst_Down = TMath::Abs(allbkgUp->GetBinContent(iB)- allbkg->GetBinContent(iB));
			}
	}
	
				


						
}
