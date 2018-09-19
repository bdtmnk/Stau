#include <iostream>
#include <vector>
#include <map>
#include "boost/lexical_cast.hpp"
#include "boost/algorithm/string.hpp"
#include "boost/format.hpp"
#include "boost/program_options.hpp"
#include "boost/range/algorithm.hpp"
#include "boost/range/algorithm_ext.hpp"
#include "Plotting.h"
#include "Plotting_Style.h"
#include "HttStylesNew.cc"
#include "TPad.h"
#include "TROOT.h"
#include "TColor.h"
#include "TEfficiency.h"
#include "TMath.h"
//WithoutNPV/
void PlotsForUnrolledDistrSyst(TString directory = "",
	  TString suffix = "_MuTau",
	  //TString File = "Var_MET_17_35invfb_mt_CRB",
	  TString File = "Var_BDTmutau_Stau200_16_35invfb_mt_SR",
	  string varN  = "Var_BDTmutau_Stau200_16_35invfb_mt_SR",
	  TString variable = "",
	  TString Suffix = "Syst",
	  TString xtitle = "",
	  TString ytitle = "Events",
      bool logY = true,
 	    bool BlindData = false,
	    bool OverlayFit = true

          )


{
	  vector<TString> vars_;vars_.clear();
	  vector<TString> syst_;syst_.clear();
	  vars_.push_back("BDTmutau_Stau200_16");
	//  vars_.push_back("BDTmutau_stau150_LSP1My_15");
	//  vars_.push_back("BDTmutau_stau200_LSP1My_15");
	//  vars_.push_back("BDTmutau_stau300_LSP1My_15");

	  syst_.push_back("Nominal");
	  syst_.push_back("JetEnUp");
	  syst_.push_back("JetEnDown");

	  syst_.push_back("UnclEnUp");
	  syst_.push_back("UnclEnDown");

	  syst_.push_back("ElEnUp");
	  syst_.push_back("ElEnDown");

	  syst_.push_back("MuEnUp");
	  syst_.push_back("MuEnDown");

	  syst_.push_back("TauEnUp");
	  syst_.push_back("TauEnDown");

	  //syst_.push_back("TopPtUp");
	  //syst_.push_back("TopPtDown");

	  syst_.push_back("ZPtUp");
	  syst_.push_back("ZPtDown");

	  syst_.push_back("ScalesUp");
	  syst_.push_back("ScalesDown");

	  syst_.push_back("PDFUp");
	  syst_.push_back("PDFDown");



int mycolor=TColor::GetColor("#ffcc66");
int mycolorvv=TColor::GetColor("#8646ba");
int mycolorqcd=TColor::GetColor("#ffccff");
int mycolortt=TColor::GetColor("#9999cc");
int mycolorttx=TColor::GetColor("#33CCFF");
int mycolorwjet=TColor::GetColor("#de5a6a");
int mycolordyj=TColor::GetColor("#ffcc66");
int mycolorztt=TColor::GetColor("#58d885");
int mycolorst=TColor::GetColor("#b6d0ea");
int mycolorww=TColor::GetColor("#C390D4");


  bool plotLeg = true;
  int position = 2; // 0 - right, 1 - left, 2 - central
  int npos = 1;

  TH1::SetDefaultSumw2();
  TH2::SetDefaultSumw2();


  //  TString topweight("");

TString BinLabels[100] = {
"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31",
"32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60",
"61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93"
};


/*
	ifstream BinLabelsFile;
	BinLabelsFile.open("LabelListTESR");
	int i=0;
	string name;
   	 while(getline(BinLabelsFile, name))
		{
//		BinLabels[i]=name;
		i++;
		}
*/


 TH1D *TT[20];
 TH1D *TTcl[20];
 TH1D *WJ[20];
 TH1D *DY[20];
 TH1D *ZTT[20];
 TH1D *ST[20];
 TH1D *VV[20];
 TH1D *WW[20];
 TH1D *TTX[20];
 TH1D *fakes[20];
 TH1D *rest[20];
 TH1D *allbkg[20];
 TH1D * histData;
 THStack * hs[20];
 TH1D *hsum[20];// = ((TH1D*)(hs->GetStack()->Last()));

    int nBins;//  =   histData->GetNbinsX();
	
    TString _out;

	cout<<" check "<<endl;
for (int svar=0;svar<vars_.size();++svar)
{

	TString Variable=vars_.at(svar);


	cout<<" check "<<Variable<<endl;
for (int syst=0;syst<syst_.size();++syst)
{

	if (syst_.at(syst) == "Nominal") _out =".root";
	else {
		_out = "_"+syst_.at(syst) +".root";
		Variable = vars_.at(svar)+"_"+syst_.at(syst);
	}

 	TFile * file = new TFile(File+_out);
    
	cout<<" Will try now to open "<<file->GetName()<<" for syst "<<syst<<endl;

     TT[syst] = (TH1D*)file->Get("tt_"+Variable);
     WJ[syst] = (TH1D*)file->Get("wj_"+Variable);
     DY[syst] = (TH1D*)file->Get("dyj_"+Variable);
     ZTT[syst] = (TH1D*)file->Get("ztt_"+Variable);
     ST[syst] = (TH1D*)file->Get("sT_"+Variable);
     VV[syst] = (TH1D*)file->Get("dib_"+Variable);
     WW[syst] = (TH1D*)file->Get("ww_"+Variable);
     TTX[syst] = (TH1D*)file->Get("ttx_"+Variable);
     fakes[syst] = (TH1D*)file->Get("fakes_"+Variable);
     rest[syst] = (TH1D*)file->Get("rest_"+Variable);
     allbkg[syst] = (TH1D*)file->Get("tt_"+Variable);
  if (syst_.at(syst) == "Nominal") histData = (TH1D*)file->Get("data_obs");

     nBins  =   histData->GetNbinsX();

if (BlindData && syst_.at(syst) == "Nominal" ) {for (int iB=1; iB<=nBins; ++iB) {histData->SetBinContent(iB,0);  cout<<"  Nameeeeeeeeeeeee "<<histData->GetXaxis()->GetBinLabel(iB)<<endl; }}
if (syst_.at(syst) == "Nominal" ) {for (int iB=1; iB<=nBins; ++iB) { cout<<"  Nameeeeeeeeeeeee "<<histData->GetXaxis()->GetBinLabel(iB)<<"  "<<histData->GetBinLowEdge(iB)<<endl; }}

   TTcl[syst] = (TH1D*)TT[syst]->Clone("dummy");

   allbkg[syst]->Reset();
//   allbkg[syst]->Add(WJ[syst]);
   allbkg[syst]->Add(TTcl[syst]);
   allbkg[syst]->Add(DY[syst]);
   allbkg[syst]->Add(ST[syst]);
   allbkg[syst]->Add(ZTT[syst]);
   allbkg[syst]->Add(WW[syst]);
//   allbkg[syst]->Add(VV[syst]);
//   allbkg[syst]->Add(TTX[syst]);
   allbkg[syst]->Add(fakes[syst]);
   allbkg[syst]->Add(rest[syst]);

cout << "!!!!!!"<<endl;
  std::cout << "TT  : " << TTcl[syst]->GetSumOfWeights() << " : "  <<" GetNbinsX= " << TTcl[syst]->GetNbinsX()<<endl;// "  Purity  "<<TTcl->GetSumOfWeights()/allbkg->GetSumOfWeights()<< std::endl;
  std::cout << "WJ   : " << WJ[syst]->GetSumOfWeights() << " : "  <<" GetNbinsX= " << WJ[syst]->GetNbinsX()<<endl;// "  Purity  "<<WJ->GetSumOfWeights()/allbkg->GetSumOfWeights()<< std::endl;
  std::cout << "DY : " << DY[syst]->GetSumOfWeights() << " : "  <<" GetNbinsX= " << DY[syst]->GetNbinsX()<<endl;// "  Purity  "<<DY->GetSumOfWeights()/allbkg->GetSumOfWeights()<< std::endl;
  std::cout << "ZTT : " << ZTT[syst]->GetSumOfWeights() << " : "  <<" GetNbinsX= " << ZTT[syst]->GetNbinsX()<<endl;// "  Purity  "<<ZTT->GetSumOfWeights()/allbkg->GetSumOfWeights()<< std::endl;
  std::cout << "ST   : " << ST[syst]->GetSumOfWeights() << " : "  <<" GetNbinsX= " << ST[syst]->GetNbinsX()<<endl;// "  Purity  "<<ST->GetSumOfWeights()/allbkg->GetSumOfWeights()<< std::endl;
  std::cout << "VV   : " << VV[syst]->GetSumOfWeights() << " : "  <<" GetNbinsX= " << VV[syst]->GetNbinsX() <<endl;// "  Purity  "<<VV->GetSumOfWeights()/allbkg->GetSumOfWeights()<< std::endl;
  std::cout << "WW   : " << WW[syst]->GetSumOfWeights() << " : "  <<" GetNbinsX= " << WW[syst]->GetNbinsX() <<endl;// "  Purity  "<<WW->GetSumOfWeights()/allbkg->GetSumOfWeights()<< std::endl;
  std::cout << "fakes   : " << fakes[syst]->GetSumOfWeights() << " : " <<" GetNbinsX= " << fakes[syst]->GetNbinsX()<<endl;// "  Purity  "<<fakes->GetSumOfWeights()/allbkg->GetSumOfWeights()<< std::endl;
  std::cout << "TTX  : " << TTX[syst]->GetSumOfWeights() << " : "  <<" GetNbinsX= " << TTX[syst]->GetNbinsX()<<endl;// "  Purity  "<<TTX->GetSumOfWeights()/allbkg->GetSumOfWeights()<< std::endl;
  std::cout << "histData : " << histData->GetSumOfWeights() << " : "  <<" GetNbinsX= " << histData->GetNbinsX()<<endl;// endl;

  
  std::cout << "BKG : " << allbkg[syst]->GetSumOfWeights() << " : " << allbkg[syst]->Integral(0,nBins+1) << std::endl;
  std::cout << "DAT : " << histData->GetSumOfWeights() << " : " << histData->Integral(0,nBins+1) << std::endl;
  //std::cout << "DAT/BKG = " << histData->GetSumOfWeights()/allbkg[syst]->GetSumOfWeights() << "+/-"   << TMath::Sqrt(histData->GetSumOfWeights())/allbkg[syst]->GetSumOfWeights() << std::endl;
  cout<<"==========="<<endl;

    InitHist(rest[syst],mycolorvv);
    InitHist(fakes[syst],mycolorttx);
    InitHist(DY[syst],mycolordyj);
    InitHist(TT[syst],mycolortt);
    InitHist(TTcl[syst],mycolortt);
    InitHist(ST[syst],mycolorst);
    InitHist(TTX[syst],mycolorttx);
    InitHist(WJ[syst],mycolorwjet);
    InitHist(VV[syst],mycolorvv);
    InitHist(ZTT[syst],mycolorztt);
    InitHist(WW[syst],mycolorww);
//for (int iB=1; iB<=nBins; ++iB) {WJ[syst]->SetBinError(iB,0);TT[syst]->SetBinError(iB,0);DY[syst]->SetBinError(iB,0);fakes[syst]->SetBinError(iB,0);VV[syst]->SetBinError(iB,0);TTX[syst]->SetBinError(iB,0);ST[syst]->SetBinError(iB,0);ZTT[syst]->SetBinError(iB,0);}

//    WJ[syst]->SetMarkerStyle(0);
    TT[syst]->SetMarkerStyle(0);
    TTcl[syst]->SetMarkerStyle(0);
    DY[syst]->SetMarkerStyle(0);
    ZTT[syst]->SetMarkerStyle(0);
    fakes[syst]->SetMarkerStyle(0);
    rest[syst]->SetMarkerStyle(0);
//    VV[syst]->SetMarkerStyle(0);
    WW[syst]->SetMarkerStyle(0);
//    TTX[syst]->SetMarkerStyle(0);
    ST[syst]->SetMarkerStyle(0);

    hs[syst] = new THStack("","");
//    hs[syst]->Add(TTX[syst]);
    hs[syst]->Add(ST[syst]);
    hs[syst]->Add(WW[syst]);
//    hs[syst]->Add(VV[syst]);
    hs[syst]->Add(rest[syst]);
    hs[syst]->Add(TTcl[syst]);
//    hs[syst]->Add(WJ[syst]);
    hs[syst]->Add(DY[syst]);
    hs[syst]->Add(ZTT[syst]);
    hs[syst]->Add(fakes[syst]);


}
cout<< " done with syst "<<endl;
///////////////////////////////////////////////////////////////////////////////////////////////
//

for (int syst=0;syst<syst_.size();++syst)
    hsum[syst] = ((TH1D*)(hs[syst]->GetStack()->Last()));


    //ModTDRStyle();
    TH1D * bkgdErr = (TH1D*)allbkg[0]->Clone("bkgdErr");
    TH1D * bkgdErrSyst = (TH1D*)allbkg[0]->Clone("bkgdErrSyst");
    TH1D * bkgdErrStat = (TH1D*)allbkg[0]->Clone("bkgdErrStat");
  
   bkgdErr->GetXaxis()->SetTitleOffset(1.2);
   bkgdErrStat->GetXaxis()->SetTitleOffset(1.2);
   bkgdErrSyst->GetXaxis()->SetTitleOffset(1.2);

    ModTDRStyle();

  
    TCanvas* canv1 = new TCanvas("c1", "c1");
    canv1->cd();
    std::vector<TPad*> pads = TwoPadSplit(0.29, 0.00, 0.00);
    pads[0]->SetLogy(logY);
    histData->GetXaxis()->SetLabelSize(0.025);
    std::vector<TH1*> h = CreateAxisHists(2, histData, 0.1, histData->GetXaxis()->GetXmax()-0.01);
    h[0]->Draw();
    
    
    std::string units="GeV";
    units="";

    std::string xtitle_ = (std::string) xtitle;
    size_t pos = xtitle_.find("[");
    if(pos!=std::string::npos) {
        units = xtitle_.substr(pos+1, xtitle_.find("]") - pos -1 );
        xtitle_ = xtitle_.substr(0, pos);
    }
    
    string variable_="BDT";
    if ( std::string::npos != variable_.find("lester"))	 xtitle_="M_{T2}";
    if ( std::string::npos != variable_.find("MET"))	 xtitle_="#it{p}_{T}^{miss}";
    if ( std::string::npos != variable_.find("DZeta"))	 xtitle_="D#zeta";
    if ( std::string::npos != variable_.find("BDT"))	 xtitle_="BDT";
    		if (std::string::npos != varN.find("BDTmutau_Stau100"))  xtitle_="BDT (100,1)";
			if (std::string::npos != varN.find("BDTmutau_Stau150")) xtitle_="BDT (150,1)";
			if (std::string::npos != varN.find("BDTmutau_Stau200")) xtitle_="BDT (200,1)";
			if (std::string::npos != varN.find("BDTmutau_Stau300_LSP1")) xtitle_="BDT (300,1)";

    pads[1]->cd();
    h[1]->Draw();
    SetupTwoPadSplitAsRatio(pads, "Obs/Exp", true, 0.1, 2.55);
    StandardAxes(h[1]->GetXaxis(), h[0]->GetYaxis(),xtitle_ ,units);
    h[1]->GetYaxis()->SetNdivisions(4);
    h[1]->GetXaxis()->SetTitleOffset(1.2);
    h[1]->GetYaxis()->SetTitleOffset(1.2);
    pads[0]->cd();
    h[0]->GetYaxis()->SetTitleOffset(1.2);
    pads[1]->SetGrid(0,1);
    //it complains if the minimum is set to 0 and you try to set log y scale
    if(logY) h[0]->SetMinimum(0.009);
    pads[0]->cd();
    
    
    histData->SetMarkerColor(1);
    histData->SetLineColor(1);
    histData->SetFillColor(1);
    histData->SetFillStyle(0);
    histData->SetLineWidth(2);
    histData->SetMarkerStyle(20);
    histData->SetMarkerSize(1);


//    int color = CreateTransparentColor(13,0.);

    TLegend *legend = PositionedLegend(0.4, 0.20, 3, 0.03);
    if (!BlindData)legend->AddEntry(histData, "Observed", "ple");
    legend->AddEntry(TT[0],"TTJets","f");
    legend->AddEntry(ST[0],"singleTop","f");
//    legend->AddEntry(TTX[0],"TTX/TG","f");
//    legend->AddEntry(WJ[0],"WJets","f");
    legend->AddEntry(fakes[0],"misId #tau","f");
    legend->AddEntry(ZTT[0],"DY#rightarrow#tau#tau","f");
    legend->AddEntry(DY[0],"DY#rightarrow#mu#mu/ee","f");
    legend->AddEntry(WW[0],"WW","f");
    legend->AddEntry(rest[0],"Rest","f");
    legend->SetTextFont(42);
    legend-> SetNColumns(2);
cout<<" check "<<endl;
    

/*
 gStyle->SetLineStyleString(11,"400 200");
 gStyle->SetLineStyleString(12,"500 200");
 gStyle->SetLineStyleString(13,"600 200");
*/
  cout<<" check again"<<endl;
  hsum[0]->Draw("same hist");
  hs[0]->Draw("same hist");
for (int iS=1;iS<syst_.size();++iS){
  hsum[iS]->SetFillColor(0);
  hsum[iS]->SetLineWidth(4);
  hsum[iS]->SetMarkerStyle(19+iS);
  hsum[iS]->SetMarkerSize(1);
  hsum[iS]->SetLineColor(kBlue);
  hsum[iS]->SetMarkerColor(kBlue);
 if (iS%2==0) hsum[iS]->SetLineColor(kRed);
 if (iS%2==0) hsum[iS]->SetMarkerColor(kRed);
 // legend->AddEntry(hsum[iS], syst_.at(iS),"p" );
 // hsum[iS]->Draw("same hist p");

}

    canv1->Update();

///////////////////////////////////////////////
//Errors

    float errLumi = 0.1; // plus BDT
    float errMuon = 0.02;
    float errElectron = 0.03;
    float errTau = 0.0;
    float errTauID = 0.05;
    float errBTag = 0.04;
    float errMET = 0.0;
    float errTFR = 0.05;
    float errLTFR = 0.05;
    float errDY = 0.05;
    float errZTT = 0.05;
    float errWJ = 0.0;
    float errTT = 0.05;
    float errfakes = 0.10;
    float errrest = 0.25;
    float errST = 0.25;
    float errVV = 0.0;
    float errWW = 0.25;
    float errTTX = 0.;

if (suffix=="_MuEl") {errTFR = 0;errLTFR =0;errTau =0;}

    nBins=histData->GetNbinsX();
double ex[20];
double sum_syst=0;

 for (int iB=1; iB<=nBins; ++iB) {
	 sum_syst=0;
        allbkg[0]->SetBinError(iB,0);


for (int iS=0;iS<syst_.size()-1;++iS)
{
        float X= hsum[0]->GetBinContent(iB);
	float xUp = hsum[iS]->GetBinContent(iB); // TauES Up
        float xDown = hsum[iS+1]->GetBinContent(iB); // TauES Up
        ex[iS] = max( fabs(X-xUp),fabs(X-xDown));
        cout <<"xUp  "<<xUp << endl;
        cout <<"xDown  "<<xDown << endl;
        cout <<"x  "<<X << endl;


        cout <<"Syst  " << ex[iS]*ex[iS]<< endl;
	sum_syst += ex[iS]*ex[iS];
	iS++;
	}


        float eStat =  bkgdErr->GetBinError(iB);
        float X = hsum[0]->GetBinContent(iB);
        float eLumi = errLumi * X;
        float eMuon = errMuon * X;
        float eElectron = errElectron * X;
        float eTauID = errTauID * X;
        float eTFR = errTFR * X;
        float eLTFR = errLTFR * X;
        float eMET = errMET * X;
        float eTau = errTau * X;
 
	double stat_TT = TTcl[0]->GetBinContent(iB) * errTT;
	double stat_TTX = TTX[0]->GetBinContent(iB) * errTTX;
	double stat_WJ = WJ[0]->GetBinContent(iB) * errWJ;
	double stat_DY = DY[0]->GetBinContent(iB) * errDY;
	double stat_ZTT = ZTT[0]->GetBinContent(iB) * errZTT;
	double stat_ST = ST[0]->GetBinContent(iB) * errST;
	double stat_VV = VV[0]->GetBinContent(iB) * errVV;
	double stat_WW = WW[0]->GetBinContent(iB) * errWW;
	double stat_fakes = fakes[0]->GetBinContent(iB) * errfakes;
	double stat_rest = rest[0]->GetBinContent(iB) * errrest;

	double stat_errorNorm = stat_TT*stat_TT +stat_TTX*stat_TTX +  stat_WJ*stat_WJ + stat_DY*stat_DY + stat_ZTT*stat_ZTT +  stat_ST* stat_ST + stat_VV*stat_VV + stat_WW*stat_WW + stat_fakes*stat_fakes + stat_rest*stat_rest;

	double stat_error = eStat*eStat+eLumi*eLumi + eElectron*eElectron + eMuon*eMuon + eTau*eTau + eMET*eMET + eTFR*eTFR + eLTFR*eLTFR + eTauID*eTauID;
	//cout <<"eStat  "<<eStat <<endl;
	double Err = TMath::Sqrt(stat_error + sum_syst +  stat_errorNorm);

        bkgdErr->SetBinError(iB,Err);
        bkgdErrStat->SetBinError(iB,sqrt(stat_error));
        bkgdErrSyst->SetBinError(iB,sqrt(sum_syst));
	
	
	//cout<<" ======================================= iB "<<iB<<" Pre "<<float(eStat/X)<<" Err "<<Err<<" Stat Err "<<sqrt(stat_error)<<" Syst Err  "<<sqrt(sum_syst)<<" X "<<X<<endl;
    }

    bkgdErr->SetMarkerSize(0);
    int new_idx = CreateTransparentColor(kRed,0.5);
    int new_idxStat = CreateTransparentColor(kRed,0.5);
    int new_idxSyst = CreateTransparentColor(kGreen,0.5);

    bkgdErr->SetFillColor(new_idx);
    bkgdErr->SetFillStyle(3002);
    bkgdErr->SetLineWidth(1);

    bkgdErrStat->SetFillColor(new_idxStat);
    bkgdErrStat->SetLineWidth(1);
    
    bkgdErrSyst->SetFillColor(new_idxSyst);
    bkgdErrSyst->SetLineWidth(1);

	
    pads[1]->cd();
    TLegend *legend2 = new TLegend (0.4, 0.28, 0.6, 0.23);
    legend2->SetFillColor(0);
    legend2->SetFillStyle(0);
    legend2->AddEntry(bkgdErr, "Stat + Shape Uncrt" , "F" );
    legend2->AddEntry(bkgdErrSyst, "Shape Uncrt" , "F" );
    //legend->AddEntry(bkgdErrStat, "Stat Uncrt" , "F" );

    canv1->Update();

    TH1D * ratioH = (TH1D*)histData->Clone("ratioH");

    TH1D * ratioErrH = (TH1D*)bkgdErr->Clone("ratioErrH");
    TH1D * ratioErrHStat = (TH1D*)bkgdErrStat->Clone("ratioErrHStat");
    TH1D * ratioErrHSyst = (TH1D*)bkgdErrSyst->Clone("ratioErrHSyst");
 
    for (int iB=1; iB<=nBins; ++iB) {

        float x1 = histData->GetBinContent(iB);
  	  float x2 = allbkg[0]->GetBinContent(iB);


	ratioErrH->SetBinError(iB,0.0);
        ratioErrH->SetBinContent(iB,1.0);
	ratioErrHSyst->SetBinError(iB,0.0);
	ratioErrHStat->SetBinError(iB,0.0);
        ratioErrHSyst->SetBinContent(iB,1.0);
        ratioErrHStat->SetBinContent(iB,1.0);


        float xBkg = bkgdErr->GetBinContent(iB);
        float errBkg = bkgdErr->GetBinError(iB);
        float xBkgSyst = bkgdErrSyst->GetBinContent(iB);
        float errBkgSyst = bkgdErrSyst->GetBinError(iB);
        float xBkgStat = bkgdErrStat->GetBinContent(iB);
        float errBkgStat = bkgdErrStat->GetBinError(iB);



        if (xBkg>0) {
            float relErr = errBkg/xBkg;
            float relErrS1 = errBkgSyst/xBkgSyst;
            float relErrS2 = errBkgStat/xBkgStat;

            ratioErrH->SetBinError(iB,relErr);
            ratioErrHSyst->SetBinError(iB,relErrS1);
            ratioErrHStat->SetBinError(iB,relErrS2);


            
        }
        if (x1>0&&x2>0) {
            float e1 = histData->GetBinError(iB);
            float ratio = x1/x2;

            float eratio = e1/x2;

            ratioH->SetBinContent(iB,ratio);
            ratioH->SetBinError(iB,eratio);

        }
        else {
            ratioH->SetBinContent(iB,0);
        }
    }

    
    pads[1]->cd();

    ratioErrH->Draw("e2same");
    ratioErrHSyst->Draw("e2same");
 //   ratioErrHSyst->Draw("e2same");
    ratioH->Draw("pe0same");
    legend2->Draw("same");
//    cout<<ratioErrHStat->GetBinError(1)<<"  "<<ratioErrHStat->GetBinError(3)<<endl;

    pads[0]->cd();
    histData->Draw("pesame");
    
    if (variable_== "MET" || variable_== "Mt2lestermuel" || variable_== "Mt2lestermutau" || variable_== "Mt2lestereltau"){  pads[1]->SetLogx();pads[0]->SetLogx();}
    string v="";
    FixTopRange(pads[0], GetPadYMax(pads[0]), 0.5);
    DrawCMSLogo(pads[0], "CMS", "Preliminary", 11, 0.045, 0.035, 1.2);
    DrawTitle(pads[0], "35.9 fb^{-1} (13 TeV)", 3);
    //DrawTitle(pads[0], v, 1);

    FixBoxPadding(pads[0], legend, 0.05);
    legend->Draw();
    FixOverlay();
    canv1->Update();
    pads[0]->GetFrame()->Draw();
    canv1->Print(vars_.at(svar)+suffix+".pdf");
}
}
