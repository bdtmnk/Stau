#include <math.h>
#include <iostream>
void CreateDatacards_BDTeltau_stau150_LSP1MyNew_15_mt_35() {



float ttUnc = 0.;
float wjUnc = 0;
float dyjUnc = 0;
float zttUnc = 0;
float wwUnc = 0.;
float dibUnc = 0.;
float sTUnc = 0.;
float ttxUnc = 0.;
float fakesUnc = 0.;
float restUnc = 0.;
float snUnc = 0.;


bool bFirst = false;

  //TFile * file = new TFile("Var_BDTeltau_stau150_LSP1MyNew_15_35invfb_mt_SR");
  TFile *file = TFile::Open ("Var_BDTeltau_stau150_LSP1MyNew_15_35invfb_mt_SR.root", "read");
  TFile *fileout = TFile::Open ("Var_BDTeltau_stau150_LSP1MyNew_15_35invfb_mt_SR_out.root", "update");
  //file->cd("mt");
  

  TH1D * data_obs = (TH1D*)file->Get("data_obs_BDTeltau_stau150_LSP1MyNew_15");
//  TH1D * data_obs = (TH1D*)file->Get("allbkg_BDTeltau_stau150_LSP1MyNew_15");

  data_obs->SetName("data_obs");

  TH1D * signal = (TH1D*)file->Get("stau-stau_left_90_LSP10_B_BDTeltau_stau150_LSP1MyNew_15");
  float Nom_SofW =  signal->Integral();
  float Syst_SofWUp =0;
  float Syst_SofWDown = 0;
  float Syst_SofWUpBtag = 0;
  float Syst_SofWDownBtag = 0;

  float Syst_SofW = 0.;
  float Syst_SofWBtag = 0.;


  TH1D * tt = (TH1D*)file->Get("tt_BDTeltau_stau150_LSP1MyNew_15");
  TH1D * wj = (TH1D*)file->Get("wj_BDTeltau_stau150_LSP1MyNew_15");
  TH1D * dyj = (TH1D*)file->Get("dyj_BDTeltau_stau150_LSP1MyNew_15");
  TH1D * ztt = (TH1D*)file->Get("ztt_BDTeltau_stau150_LSP1MyNew_15");
  TH1D * dib = (TH1D*)file->Get("dib_BDTeltau_stau150_LSP1MyNew_15");
  TH1D * ww = (TH1D*)file->Get("ww_BDTeltau_stau150_LSP1MyNew_15");
  TH1D * ttx = (TH1D*)file->Get("ttx_BDTeltau_stau150_LSP1MyNew_15");
  TH1D * sT = (TH1D*)file->Get("sT_BDTeltau_stau150_LSP1MyNew_15");
  TH1D * fakes = (TH1D*)file->Get("fakes_BDTeltau_stau150_LSP1MyNew_15");
  TH1D * rest = (TH1D*)file->Get("rest_BDTeltau_stau150_LSP1MyNew_15");


  TH1D * allbkg = (TH1D*)tt->Clone("total_background");

  TH1D * tt_shape = (TH1D*)tt->Clone("tt_shape");
  TH1D * wj_shape = (TH1D*)wj->Clone("wj_shape");
  TH1D * dyj_shape = (TH1D*)dyj->Clone("dyj_shape");
  TH1D * ztt_shape = (TH1D*)ztt->Clone("ztt_shape");
  TH1D * dib_shape = (TH1D*)dib->Clone("dib_shape");
  TH1D * ww_shape = (TH1D*)ww->Clone("ww_shape");
  TH1D * ttx_shape = (TH1D*)ttx->Clone("ttx_shape");
  TH1D * sT_shape = (TH1D*)sT->Clone("sT_shape");
  TH1D * fakes_shape = (TH1D*)fakes->Clone("fakes_shape");
  TH1D * rest_shape = (TH1D*)rest->Clone("rest_shape");

  TH1D * tt_norm = (TH1D*)tt->Clone("tt_norm");
  TH1D * wj_norm = (TH1D*)wj->Clone("wj_norm");
  TH1D * dyj_norm = (TH1D*)dyj->Clone("dyj_norm");
  TH1D * ztt_norm = (TH1D*)ztt->Clone("ztt_norm");
  TH1D * dib_norm = (TH1D*)dib->Clone("dib_norm");
  TH1D * ww_norm = (TH1D*)ww->Clone("ww_norm");
  TH1D * ttx_norm = (TH1D*)ttx->Clone("ttx_norm");
  TH1D * sT_norm = (TH1D*)sT->Clone("sT_norm");
  TH1D * fakes_norm = (TH1D*)fakes->Clone("fakes_norm");
  TH1D * rest_norm = (TH1D*)rest->Clone("rest_norm");

  float tt_error[60][40]={0.};
  float wj_error[60][40]={0.};
  float dyj_error[60][40]={0.};
  float ztt_error[60][40]={0.};
  float dib_error[60][40]={0.};
  float ww_error[60][40]={0.};
  float ttx_error[60][40]={0.};
  float sT_error[60][40]={0.};
  float fakes_error[60][40]={0.};
  float rest_error[60][40]={0.};
  float signal_error[60]={0.};

  float tt_errorStat[60]={0.};
  float wj_errorStat[60]={0.};
  float dyj_errorStat[60]={0.};
  float ztt_errorStat[60]={0.};
  float dib_errorStat[60]={0.};
  float ww_errorStat[60]={0.};
  float ttx_errorStat[60]={0.};
  float sT_errorStat[60]={0.};
  float fakes_errorStat[60]={0.};
  float rest_errorStat[60]={0.};
  float signal_errorStat[60]={0.};



  allbkg->Add(wj);
  allbkg->Add(dyj);
  allbkg->Add(ztt);
  allbkg->Add(dib);
  allbkg->Add(ww);
  allbkg->Add(ttx);
  allbkg->Add(sT);
  allbkg->Add(fakes);



  vector <string> Systematics;

  Systematics.push_back("JetEnUp");
  Systematics.push_back("UnclEnUp");
  Systematics.push_back("MuEnUp");
  Systematics.push_back("ElEnUp");
  Systematics.push_back("TauEnUp");
//  Systematics.push_back("TopPtUp");
  Systematics.push_back("ZPtUp");
  Systematics.push_back("METUp");
  Systematics.push_back("EWKUp");
  Systematics.push_back("ScalesUp");
  Systematics.push_back("PDFUp");
//  Systematics.push_back("METRecoilUp");
  Systematics.push_back("BTagUp");
//  Systematics.push_back("TFRJetEnUp");
//  Systematics.push_back("TFRTauEnUp");
//  Systematics.push_back("TFRMuEnUp");

  Systematics.push_back("JetEnDown");
  Systematics.push_back("UnclEnDown");
  Systematics.push_back("MuEnDown");
  Systematics.push_back("ElEnDown");
  Systematics.push_back("TauEnDown");
//  Systematics.push_back("TopPtDown");
  Systematics.push_back("ZPtDown");
  Systematics.push_back("METDown");
  Systematics.push_back("EWKDown");
  Systematics.push_back("ScalesDown");
  Systematics.push_back("PDFDown");
//  Systematics.push_back("METRecoilDown");
  Systematics.push_back("BTagDown");
//  Systematics.push_back("TFRJetEnDown");
//  Systematics.push_back("TFRTauEnDown");
//  Systematics.push_back("TFRMuEnDown");



  int sz=Systematics.size();

  fileout->cd();

  TString binName[60] = {"0","1","2","3","4","5","6","7","8","9","10",
			 "11","12","13","14","15","16","17","18","19","20",
			 "21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"};


	signal->Write();
  int nBins = tt->GetNbinsX();
if (bFirst){
	data_obs->Write();
	tt->Write();
	ttx->Write();
	dib->Write();
	ww->Write();
	sT->Write();
	wj->Write();
	dyj->Write();
	ztt->Write();
	rest->Write();
	fakes->Write();


  for (int iB=1; iB<=nBins; ++iB) {
    TH1D * ttUp = (TH1D*)tt->Clone("tt_BDTeltau_stau150_LSP1MyNew_15_ttBin"+binName[iB]+"Up");
    TH1D * ttDown = (TH1D*)tt->Clone("tt_BDTeltau_stau150_LSP1MyNew_15_ttBin"+binName[iB]+"Down");
    float xtt = tt->GetBinContent(iB);
    float ett = tt->GetBinError(iB);

float rtt = ett/xtt;
if (ttUp->GetBinError(iB)<0.) ttUp->SetBinError(iB,0.);
if (ttDown->GetBinError(iB)<0.) ttDown->SetBinError(iB,0.);

if (xtt+ett>0. && rtt>ttUnc) { ttUp->SetBinContent(iB,xtt+ett);ttUp->SetBinError(iB,sqrt(ttUp->GetBinContent(iB)));}
if (xtt-ett>0. && rtt>ttUnc) { ttDown->SetBinContent(iB,xtt-ett);ttDown->SetBinError(iB,sqrt(ttDown->GetBinContent(iB)));}

    ttUp->Write("tt_BDTeltau_stau150_LSP1MyNew_15_ttBin_mt"+binName[iB]+"Up");
    ttDown->Write("tt_BDTeltau_stau150_LSP1MyNew_15_ttBin_mt"+binName[iB]+"Down");

    TH1D * WUp = (TH1D*)wj->Clone("wj_BDTeltau_stau150_LSP1MyNew_15_wjBin"+binName[iB]+"Up");
    TH1D * WDown = (TH1D*)wj->Clone("wj_BDTeltau_stau150_LSP1MyNew_15_wjBin"+binName[iB]+"Down");
    float xwj = wj->GetBinContent(iB);
    float ewj = wj->GetBinError(iB);

float rwj = ewj/xwj;
if (WUp->GetBinError(iB)<0 ) WUp->SetBinError(iB,0.);
if (WDown->GetBinError(iB)<0.) WDown->SetBinError(iB,0.);

if (xwj+ewj>0. && rwj>wjUnc) { WUp->SetBinContent(iB,xwj+ewj);WUp->SetBinError(iB,sqrt(WUp->GetBinContent(iB)));}
if (xwj-ewj>0. && rwj>wjUnc) { WDown->SetBinContent(iB,xwj-ewj);WDown->SetBinError(iB,sqrt(WDown->GetBinContent(iB)));}

    WUp->Write("wj_BDTeltau_stau150_LSP1MyNew_15_wjBin_mt"+binName[iB]+"Up");
    WDown->Write("wj_BDTeltau_stau150_LSP1MyNew_15_wjBin_mt"+binName[iB]+"Down");

    TH1D * dyjUp = (TH1D*)dyj->Clone("dyj_BDTeltau_stau150_LSP1MyNew_15_dyjBin"+binName[iB]+"Up");
    TH1D * dyjDown = (TH1D*)dyj->Clone("dyj_BDTeltau_stau150_LSP1MyNew_15_dyjBin"+binName[iB]+"Down");
    float xdyj = dyj->GetBinContent(iB);
    float edyj = dyj->GetBinError(iB);

float rdyj = edyj/xdyj;
if (dyjUp->GetBinError(iB)<0.) dyjUp->SetBinError(iB,0.);
if (dyjDown->GetBinError(iB)<0.) dyjDown->SetBinError(iB,0.);


if (xdyj+edyj>0. && rdyj>dyjUnc) { dyjUp->SetBinContent(iB,xdyj+edyj);dyjUp->SetBinError(iB,sqrt(dyjUp->GetBinContent(iB)));}
if (xdyj-edyj>0. && rdyj>dyjUnc) { dyjDown->SetBinContent(iB,xdyj-edyj);dyjDown->SetBinError(iB,sqrt(dyjDown->GetBinContent(iB)));}

    dyjUp->Write("dyj_BDTeltau_stau150_LSP1MyNew_15_dyjBin_mt"+binName[iB]+"Up");
    dyjDown->Write("dyj_BDTeltau_stau150_LSP1MyNew_15_dyjBin_mt"+binName[iB]+"Down");

    TH1D * zttUp = (TH1D*)ztt->Clone("ztt_BDTeltau_stau150_LSP1MyNew_15_zttBin"+binName[iB]+"Up");
    TH1D * zttDown = (TH1D*)ztt->Clone("ztt_BDTeltau_stau150_LSP1MyNew_15_zttBin"+binName[iB]+"Down");
    float xztt = ztt->GetBinContent(iB);
    float eztt = ztt->GetBinError(iB);

float rztt=eztt/xztt;
if (zttUp->GetBinError(iB)<0.) zttUp->SetBinError(iB,0.);
if (zttDown->GetBinError(iB)<0.) zttDown->SetBinError(iB,0.);

if (xztt+eztt>0. && rztt>zttUnc) { zttUp->SetBinContent(iB,xztt+eztt);zttUp->SetBinError(iB,sqrt(zttUp->GetBinContent(iB)));}
if (xztt-eztt>0. && rztt>zttUnc) { zttDown->SetBinContent(iB,xztt-eztt);zttDown->SetBinError(iB,sqrt(zttDown->GetBinContent(iB)));}

    zttUp->Write("ztt_BDTeltau_stau150_LSP1MyNew_15_zttBin_mt"+binName[iB]+"Up");
    zttDown->Write("ztt_BDTeltau_stau150_LSP1MyNew_15_zttBin_mt"+binName[iB]+"Down");


    TH1D * dibUp = (TH1D*)dib->Clone("dib_BDTeltau_stau150_LSP1MyNew_15_dibBin_mt"+binName[iB]+"Up");
    TH1D * dibDown = (TH1D*)dib->Clone("dib_BDTeltau_stau150_LSP1MyNew_15_dibBin_mt"+binName[iB]+"Down");
    float xdib = dib->GetBinContent(iB);
    float edib = dib->GetBinError(iB);

float rdib=edib/xdib;
if (dibUp->GetBinError(iB)<0.) dibUp->SetBinError(iB,0.);
if (dibDown->GetBinError(iB)<0.) dibDown->SetBinError(iB,0.);

if (xdib+edib>0. && rdib>dibUnc) { dibUp->SetBinContent(iB,xdib+edib);dibUp->SetBinError(iB,sqrt(dibUp->GetBinContent(iB)));}
if (xdib-edib>0. && rdib>dibUnc) { dibDown->SetBinContent(iB,xdib-edib);dibDown->SetBinError(iB,sqrt(dibDown->GetBinContent(iB)));}

    dibUp->Write("dib_BDTeltau_stau150_LSP1MyNew_15_dibBin_mt"+binName[iB]+"Up");
    dibDown->Write("dib_BDTeltau_stau150_LSP1MyNew_15_dibBin_mt"+binName[iB]+"Down");


    TH1D * wwUp = (TH1D*)ww->Clone("ww_BDTeltau_stau150_LSP1MyNew_15_wwBin_mt"+binName[iB]+"Up");
    TH1D * wwDown = (TH1D*)ww->Clone("ww_BDTeltau_stau150_LSP1MyNew_15_wwBin_mt"+binName[iB]+"Down");
    float xww = ww->GetBinContent(iB);
    float eww = ww->GetBinError(iB);

float rww=eww/xww;
if (wwUp->GetBinError(iB)<0.) wwUp->SetBinError(iB,0.);
if (wwDown->GetBinError(iB)<0.) wwDown->SetBinError(iB,0.);

if (xww+eww>0. && rww>wwUnc) { wwUp->SetBinContent(iB,xww+eww);wwUp->SetBinError(iB,sqrt(wwUp->GetBinContent(iB)));}
if (xww-eww>0. && rww>wwUnc) { wwDown->SetBinContent(iB,xww-eww);wwDown->SetBinError(iB,sqrt(wwDown->GetBinContent(iB)));}

    wwUp->Write("ww_BDTeltau_stau150_LSP1MyNew_15_wwBin_mt"+binName[iB]+"Up");
    wwDown->Write("ww_BDTeltau_stau150_LSP1MyNew_15_wwBin_mt"+binName[iB]+"Down");



    TH1D * sTUp = (TH1D*)sT->Clone("sT_BDTeltau_stau150_LSP1MyNew_15_sTBin"+binName[iB]+"Up");
    TH1D * sTDown = (TH1D*)sT->Clone("sT_BDTeltau_stau150_LSP1MyNew_15_sTBin"+binName[iB]+"Down");
    float xsT = sT->GetBinContent(iB);
    float esT = sT->GetBinError(iB);

float rsT=esT/xsT;
if (sTUp->GetBinError(iB)<0.) sTUp->SetBinError(iB,0.);
if (sTDown->GetBinError(iB)<0.) sTDown->SetBinError(iB,0.);


if (xsT+esT>0. && rsT>sTUnc) { sTUp->SetBinContent(iB,xsT+esT);sTUp->SetBinError(iB,sqrt(sTUp->GetBinContent(iB)));}
if (xsT-esT>0. && rsT>sTUnc) { sTDown->SetBinContent(iB,xsT-esT);sTDown->SetBinError(iB,sqrt(sTDown->GetBinContent(iB)));}
    
    sTUp->Write("sT_BDTeltau_stau150_LSP1MyNew_15_sTBin_mt"+binName[iB]+"Up");
    sTDown->Write("sT_BDTeltau_stau150_LSP1MyNew_15_sTBin_mt"+binName[iB]+"Down");


    TH1D * ttxUp = (TH1D*)ttx->Clone("ttx_BDTeltau_stau150_LSP1MyNew_15_ttxBin"+binName[iB]+"Up");
    TH1D * ttxDown = (TH1D*)ttx->Clone("ttx_BDTeltau_stau150_LSP1MyNew_15_ttxBin"+binName[iB]+"Down");
    float xttx = ttx->GetBinContent(iB);
    float ettx = ttx->GetBinError(iB);

float rttx=ettx/xttx;
if (ttxUp->GetBinError(iB)<0.) ttxUp->SetBinError(iB,0.);
if (ttxDown->GetBinError(iB)<0.) ttxDown->SetBinError(iB,0.);

if (xttx+ettx>0. && rttx>ttxUnc) { ttxUp->SetBinContent(iB,xttx+ettx);ttxUp->SetBinError(iB,sqrt(ttxUp->GetBinContent(iB)));}
if (xttx-ettx>0. && rttx>ttxUnc) { ttxDown->SetBinContent(iB,xttx-ettx);ttxDown->SetBinError(iB,sqrt(ttxDown->GetBinContent(iB)));}



    ttxUp->Write("ttx_BDTeltau_stau150_LSP1MyNew_15_ttxBin_mt"+binName[iB]+"Up");
    ttxDown->Write("ttx_BDTeltau_stau150_LSP1MyNew_15_ttxBin_mt"+binName[iB]+"Down");



    TH1D * fakesUp = (TH1D*)fakes->Clone("fakes_BDTeltau_stau150_LSP1MyNew_15_fakesBin"+binName[iB]+"Up");
    TH1D * fakesDown = (TH1D*)fakes->Clone("fakes_BDTeltau_stau150_LSP1MyNew_15_fakesBin"+binName[iB]+"Down");
    float xfakes= fakes->GetBinContent(iB);
    float efakes = fakes->GetBinError(iB);

float rfakes=efakes/xfakes;

if (fakesUp->GetBinError(iB)<0.) fakesUp->SetBinError(iB,0.);
if (fakesDown->GetBinError(iB)<0.) fakesDown->SetBinError(iB,0.);

if (xfakes+efakes>0. && rfakes>fakesUnc) { fakesUp->SetBinContent(iB,xfakes+efakes);fakesUp->SetBinError(iB,sqrt(fakesUp->GetBinContent(iB)));}
if (xfakes-efakes>0. && rfakes>fakesUnc) { fakesDown->SetBinContent(iB,xfakes-efakes);fakesDown->SetBinError(iB,sqrt(fakesDown->GetBinContent(iB)));}

    fakesUp->Write("fakes_BDTeltau_stau150_LSP1MyNew_15_fakesBin_mt"+binName[iB]+"Up");
    fakesDown->Write("fakes_BDTeltau_stau150_LSP1MyNew_15_fakesBin_mt"+binName[iB]+"Down");

    TH1D * restUp = (TH1D*)rest->Clone("rest_BDTeltau_stau150_LSP1MyNew_15_restBin"+binName[iB]+"Up");
    TH1D * restDown = (TH1D*)rest->Clone("rest_BDTeltau_stau150_LSP1MyNew_15_restBin"+binName[iB]+"Down");
    float xrest= rest->GetBinContent(iB);
    float erest = rest->GetBinError(iB);


float rrest=erest/xrest;

if (restUp->GetBinError(iB)<0.) restUp->SetBinError(iB,0.);
if (restDown->GetBinError(iB)<0.) restDown->SetBinError(iB,0.);

if (xrest+erest>0. && rrest>restUnc) { restUp->SetBinContent(iB,xrest+erest);restUp->SetBinError(iB,sqrt(restUp->GetBinContent(iB)));}
if (xrest-erest>0. && rrest>restUnc) { restDown->SetBinContent(iB,xrest-erest);restDown->SetBinError(iB,sqrt(restDown->GetBinContent(iB)));}

    restUp->Write("rest_BDTeltau_stau150_LSP1MyNew_15_restBin_mt"+binName[iB]+"Up");
    restDown->Write("rest_BDTeltau_stau150_LSP1MyNew_15_restBin_mt"+binName[iB]+"Down");
/*
    tt_error[iB] +=  pow((tt->GetBinContent(iB) - ttUp->GetBinContent(iB)),2.);
    wj_error[iB] +=  pow((wj->GetBinContent(iB) - WUp->GetBinContent(iB)),2.);
    dyj_error[iB] +=  pow((dyj->GetBinContent(iB) - dyjUp->GetBinContent(iB)),2.);
    ztt_error[iB] +=  pow((ztt->GetBinContent(iB) - zttUp->GetBinContent(iB)),2.);
    ttx_error[iB] +=  pow((ttx->GetBinContent(iB) - ttxUp->GetBinContent(iB)),2.);
    dib_error[iB] +=  pow((dib->GetBinContent(iB) - dibUp->GetBinContent(iB)),2.);
    ww_error[iB] +=  pow((ww->GetBinContent(iB) - wwUp->GetBinContent(iB)),2.);
    sT_error[iB] +=  pow((sT->GetBinContent(iB) - sTUp->GetBinContent(iB)),2.);
    fakes_error[iB] +=  pow((fakes->GetBinContent(iB) - fakesUp->GetBinContent(iB)),2.);
*/
	
  }//loop in nBins
  

}//bFirst
  for (int j=0;j<sz;++j){

 TString sys = Systematics[j].c_str();

  TFile *filesyst = TFile::Open ("Var_BDTeltau_stau150_LSP1MyNew_15_35invfb_mt_SR_"+sys+".root", "read");

 TH1D *tt_syst,* wj_syst, * dyj_syst, * ztt_syst, * dib_syst, * ww_syst, * sT_syst,* ttx_syst,* fakes_syst,*rest_syst;

if (bFirst){

   tt_syst = (TH1D*)filesyst->Get("tt_BDTeltau_stau150_LSP1MyNew_15_"+sys);
   wj_syst = (TH1D*)filesyst->Get("wj_BDTeltau_stau150_LSP1MyNew_15_"+sys);
   dyj_syst = (TH1D*)filesyst->Get("dyj_BDTeltau_stau150_LSP1MyNew_15_"+sys);
   ztt_syst = (TH1D*)filesyst->Get("ztt_BDTeltau_stau150_LSP1MyNew_15_"+sys);
   dib_syst = (TH1D*)filesyst->Get("dib_BDTeltau_stau150_LSP1MyNew_15_"+sys);
   ww_syst = (TH1D*)filesyst->Get("ww_BDTeltau_stau150_LSP1MyNew_15_"+sys);
   sT_syst = (TH1D*)filesyst->Get("sT_BDTeltau_stau150_LSP1MyNew_15_"+sys);
   ttx_syst = (TH1D*)filesyst->Get("ttx_BDTeltau_stau150_LSP1MyNew_15_"+sys);
   fakes_syst = (TH1D*)filesyst->Get("fakes_BDTeltau_stau150_LSP1MyNew_15_"+sys);
   rest_syst = (TH1D*)filesyst->Get("rest_BDTeltau_stau150_LSP1MyNew_15_"+sys);

for (int iB=1;iB<=tt_syst->GetNbinsX();++iB){
if (tt_syst->GetBinContent(iB)<1e-4){ tt_syst->SetBinContent(iB,0.); tt_syst->SetBinError(iB,0.);}
if (wj_syst->GetBinContent(iB)<1e-4){ wj_syst->SetBinContent(iB,0.); wj_syst->SetBinError(iB,0.);}
if (dyj_syst->GetBinContent(iB)<1e-4){ dyj_syst->SetBinContent(iB,0.); dyj_syst->SetBinError(iB,0.);}
if (ztt_syst->GetBinContent(iB)<1e-4){ ztt_syst->SetBinContent(iB,0.); ztt_syst->SetBinError(iB,0.);}
if (dib_syst->GetBinContent(iB)<1e-4){ dib_syst->SetBinContent(iB,0.); dib_syst->SetBinError(iB,0.);}
if (ww_syst->GetBinContent(iB)<1e-4){ ww_syst->SetBinContent(iB,0.); ww_syst->SetBinError(iB,0.);}
if (sT_syst->GetBinContent(iB)<1e-4){ sT_syst->SetBinContent(iB,0.); sT_syst->SetBinError(iB,0.);}
if (ttx_syst->GetBinContent(iB)<1e-4){ ttx_syst->SetBinContent(iB,0.); ttx_syst->SetBinError(iB,0.);}
if (fakes_syst->GetBinContent(iB)<1e-4){ fakes_syst->SetBinContent(iB,0.); fakes_syst->SetBinError(iB,0.);}
if (rest_syst->GetBinContent(iB)<1e-4){ rest_syst->SetBinContent(iB,0.); rest_syst->SetBinError(iB,0.);}



}

if (sys=="BTagUp") {
	
		wj_syst->SetName("wj_BDTeltau_stau150_LSP1MyNew_15_misBTagUp");
		dib_syst->SetName("dib_BDTeltau_stau150_LSP1MyNew_15_misBTagUp");
		ww_syst->SetName("ww_BDTeltau_stau150_LSP1MyNew_15_misBTagUp");
		ztt_syst->SetName("ztt_BDTeltau_stau150_LSP1MyNew_15_misBTagUp");
		dyj_syst->SetName("dyj_BDTeltau_stau150_LSP1MyNew_15_misBTagUp");

}

if (sys=="BTagDown") {
	
		wj_syst->SetName("wj_BDTeltau_stau150_LSP1MyNew_15_misBTagDown");
		dib_syst->SetName("dib_BDTeltau_stau150_LSP1MyNew_15_misBTagDown");
		ww_syst->SetName("ww_BDTeltau_stau150_LSP1MyNew_15_misBTagDown");
		ztt_syst->SetName("ztt_BDTeltau_stau150_LSP1MyNew_15_misBTagDown");
		dyj_syst->SetName("dyj_BDTeltau_stau150_LSP1MyNew_15_misBTagDown");

}


  fileout->cd();
  tt_syst->Write();
  sT_syst->Write();
  ttx_syst->Write();
  fakes_syst->Write();
  rest_syst->Write();
  wj_syst->Write();
  ww_syst->Write();
  dib_syst->Write();
  dyj_syst->Write();
  ztt_syst->Write();
}
  TString Sname="stau-stau_left_90_LSP10_B_BDTeltau_stau150_LSP1MyNew_15_"+sys;
  if (sys =="TopPtUp" || sys =="TopPtDown" || sys =="ZPtUp" || sys =="ZPtDown" || sys =="METRecoilUp" || sys =="METRecoilDown") Sname="stau-stau_left_90_LSP10_Nominal_B_BDTeltau_stau150_LSP1MyNew_15_"+sys;
  TH1D * signal_syst = (TH1D*)filesyst->Get(Sname);
  fileout->cd();

for (int iB=1;iB<=signal_syst->GetNbinsX();++iB){
if (signal_syst->GetBinContent(iB)<1e-4){ signal_syst->SetBinContent(iB,0.); signal_syst->SetBinError(iB,0.);}

}

if (sys=="METUp") Syst_SofWUp =  signal_syst->Integral();
if (sys=="METDown") Syst_SofWDown =  signal_syst->Integral();
if (sys=="BTagUp") Syst_SofWUpBtag =  signal_syst->Integral();
if (sys=="BTagDown") Syst_SofWDownBtag =  signal_syst->Integral();



if (sys=="METUp") signal_syst->SetName("stau-stau_left_90_LSP10_B_BDTeltau_stau150_LSP1MyNew_15_METsignalUp");
if (sys=="METDown") signal_syst->SetName("stau-stau_left_90_LSP10_B_BDTeltau_stau150_LSP1MyNew_15_METsignalDown");
if (sys=="BTagUp")  signal_syst->SetName("stau-stau_left_90_LSP10_B_BDTeltau_stau150_LSP1MyNew_15_misBTagUp");
if (sys=="BTagDown") signal_syst->SetName("stau-stau_left_90_LSP10_B_BDTeltau_stau150_LSP1MyNew_15_misBTagDown");


  signal_syst->Write();
 

}
  for (int iB=1; iB<=nBins; ++iB) {
    TH1D * signalUp = (TH1D*)signal->Clone("stau-stau_left_90_LSP10_B_BDTeltau_stau150_LSP1MyNew_15_signalBin"+binName[iB]+"Up");
    TH1D * signalDown = (TH1D*)signal->Clone("stau-stau_left_90_LSP10_B_BDTeltau_stau150_LSP1MyNew_15_signalBin"+binName[iB]+"Down");
    float xsn = signal->GetBinContent(iB);
    float esn = signal->GetBinError(iB);

float rsn=esn/xsn;

// for signal assign a 10% uncorrelated instead of PDF
if (signalUp->GetBinError(iB)<0.) signalUp->SetBinError(iB,0.);
if (signalDown->GetBinError(iB)<0.) signalDown->SetBinError(iB,0.);



if (xsn+esn>0. && rsn>snUnc) { signalUp->SetBinContent(iB,xsn+esn);signalUp->SetBinError(iB,sqrt(signalUp->GetBinContent(iB)));}
if (xsn-esn>0. && rsn>snUnc) { signalDown->SetBinContent(iB,xsn-esn);signalDown->SetBinError(iB,sqrt(signalDown->GetBinContent(iB)));}

//if (bFirst){
    signalUp->Write("stau-stau_left_90_LSP10_B_BDTeltau_stau150_LSP1MyNew_15_signalBin_mt"+binName[iB]+"Up");
    signalDown->Write("stau-stau_left_90_LSP10_B_BDTeltau_stau150_LSP1MyNew_15_signalBin_mt"+binName[iB]+"Down");
//	}
  }

float metU=1,metD=1,btagU=1,btagD=1;;
if (Syst_SofWUp >1 && Syst_SofWDown>1){
metU = fabs(  (Syst_SofWUp-Nom_SofW)/Nom_SofW);
metD = fabs(  (Syst_SofWDown-Nom_SofW)/Nom_SofW);
Syst_SofW = max(metU,metD);
}

if (Syst_SofWUpBtag >1 && Syst_SofWDownBtag>1){
btagU = fabs(  (Syst_SofWUpBtag-Nom_SofW)/Nom_SofW);
btagD = fabs(  (Syst_SofWDownBtag-Nom_SofW)/Nom_SofW);

Syst_SofWBtag = max(btagU,btagD);
}

//cout<<" ========================= "<<metU<<"  "<<metD<<"   "<<btagU<<"  "<<btagD<<"  "<<fabs(Syst_SofWUp-Nom_SofW)<<"  "<<fabs(Syst_SofWDown-Nom_SofW)<<"  "<<Syst_SofWUp<<"  "<<Syst_SofWDown<<"  "<<Nom_SofW<<endl;


  std::ofstream textFile("SR/cards_mt/stau-stau_left_90_LSP10_BDTeltau_stau150_LSP1MyNew_15_mt_35invfb.txt");
  textFile << "imax 1   number of channels" << std::endl;
  textFile << "jmax *   number of backgrounds" << std::endl;
  textFile << "kmax *   number of nuisance parameters" << std::endl;
  textFile << "-----------------" << std::endl;
  textFile << "observation " << data_obs->Integral() << std::endl;
//  textFile << "observation " << data_obs->Integral() << std::endl;
  textFile << "-----------------" << std::endl;
  textFile << "shapes * *  Var_BDTeltau_stau150_LSP1MyNew_15_35invfb_mt_SR_out.root  $PROCESS    $PROCESS_$SYSTEMATIC " << std::endl;
  textFile << "-----------------" << std::endl;
  textFile << "bin                  mt	mt	mt	mt	mt mt mt mt" << std::endl;
//  textFile << "process              stau-stau_left_90_LSP10_B_BDTeltau_stau150_LSP1MyNew_15 tt_BDTeltau_stau150_LSP1MyNew_15 wj_BDTeltau_stau150_LSP1MyNew_15 dyj_BDTeltau_stau150_LSP1MyNew_15 ztt_BDTeltau_stau150_LSP1MyNew_15 ttx_BDTeltau_stau150_LSP1MyNew_15 dib_BDTeltau_stau150_LSP1MyNew_15 ww_BDTeltau_stau150_LSP1MyNew_15 sT_BDTeltau_stau150_LSP1MyNew_15 fakes_BDTeltau_stau150_LSP1MyNew_15" << std::endl;

  textFile << "process              stau-stau_left_90_LSP10_B_BDTeltau_stau150_LSP1MyNew_15 tt_BDTeltau_stau150_LSP1MyNew_15 rest_BDTeltau_stau150_LSP1MyNew_15 dyj_BDTeltau_stau150_LSP1MyNew_15 ztt_BDTeltau_stau150_LSP1MyNew_15 ww_BDTeltau_stau150_LSP1MyNew_15 sT_BDTeltau_stau150_LSP1MyNew_15  fakes_BDTeltau_stau150_LSP1MyNew_15" << std::endl;
  textFile << "process              0		1	2	3	4	5	6	7" << std::endl;
  textFile << "rate    "
	   << signal->Integral() << "  " 
	   << tt->Integral() << "  " 
	   << rest->Integral() << "  " 
	   << dyj->Integral() << "  " 
	   << ztt->Integral() << "  " 
	   << ww->Integral() << "  " 
	   << sT->Integral() << "  " 
	   << fakes->Integral() << std::endl; 

 
  textFile << "-----------------------------" << std::endl;
  textFile << "BDTshape            lnN	1.05	1.05	1.05	1.05	1.05	1.05	1.05 -" << std::endl;
  textFile << "lumi            lnN   	1.025   -	1.025	-	-	1.025 1.025 -" << std::endl;
  textFile << "tt_norm         lnN   	-       1.025	-	-	-	-	-	-" << std::endl;
  textFile << "rest_norm         lnN   	-       -	1.25	-	-	-	-	-" << std::endl;
  textFile << "dy_norm         lnN   	-       -	-	1.05	1.05	-	-	-" << std::endl;
  textFile << "ww_norm         lnN   	-       -	-	-	-	1.40	-	-" << std::endl;
  textFile << "sT_norm         lnN   	-       -	-	-	-	-	1.25	-" << std::endl;

  textFile << "fakes_norm        lnN   	-       -	-	-	-	-	-	1.10" << std::endl;

  textFile << "lept_tfr        lnN   	-       1.01	1.01	1.10	- 	1.01	1.01	-" << std::endl;
  textFile << "tauID   	       lnN   	1.05    1.01	1.05	-    1.05	1.10	1.10	-" << std::endl;

//  textFile << "PDF	       lnN      -  	1.1	1.1	1.1	1.1	1.1	1.1	1.1	1.1	-"<< std::endl;
  textFile << "CMS_btag        lnN      -  	1.09	1.1	-	-	-	-	-"<< std::endl;
  textFile << "CMS_missbtag    lnN      "<<std::fixed<<std::setprecision(3)<<1+0.5*Syst_SofWBtag<<"  	-	1.002	-	-	-	-	-"<< std::endl;

  textFile << "METrecoil        lnN      -  	-	-	1.1	1.02	-	-	-"<< std::endl;
  textFile << "METsignal        lnN      "<<std::fixed<<std::setprecision(3)<<1+0.5*Syst_SofW<<"	-  	-	-	-	-	-	-"<< std::endl;

//  textFile << "CMS_eff_e        lnN      1.03  	1.03	1.03	1.03	1.03	1.03	1.03	-"<< std::endl;
  textFile << "CMS_eff_m        lnN      1.02  	1.02	1.02	1.02	1.02	1.02	1.02	-"<< std::endl;

  textFile << "JetEn         	shape  	1	1	1	-	-    	1	1	-"<< std::endl;
  textFile << "UnclEn         	shape  	1	1	1	-	-    	1	1	-"<< std::endl;
  textFile << "MuEn         	shape  	1	1	1	-	-	1	1	-"<< std::endl;
  textFile << "ElEn         	shape  	1	1	1	-	-   	1	1	-"<< std::endl;
  textFile << "TauEn         	shape  	1	1	1	-	-   	1	1	-"<< std::endl;
//  textFile << "TopPt         	shape  	-	1	-	-	-    	-	-	-"<< std::endl;
  textFile << "ZPt         	shape  	-	-	-	1	1    	-	-	-"<< std::endl;
//  textFile << "METRecoil       	shape  	-	-	1	1	1    	-	-	-	-	-"<< std::endl;
//  textFile << "BTag     	shape  	-	1	-	-	-   	1	-	-	1	-"<< std::endl;
//  textFile << "misBTag     	shape  	1	-	1	1	1   	-	1	1	-	-"<< std::endl;
  textFile << "EWK	     	shape  	1	-	-	-	-   	-	-	-"<< std::endl;
  textFile << "PDF	     	shape  	-	1	1	1	1   	1	-	-"<< std::endl;
  textFile << "Scales	     	shape  	1	1	1	1	1   	1	-	-"<< std::endl;

textFile << "* autoMCStats 0"<<std::endl;

  textFile << std::endl;
/*
 for (int iB=1; iB<=nBins; ++iB) {
	  if (signal->GetBinContent(iB)>0.)
    textFile << "signalBin_mt" << binName[iB] << " shape  1.00	-	-	- 	-  	-	-	-" << std::endl;
	  if (tt->GetBinContent(iB)>0.)
    textFile << "ttBin_mt" << binName[iB] << "  shape	-	1.00	-	-	-	-	-	-" << std::endl;
	  if (rest->GetBinContent(iB)>0.)
    textFile << "restBin_mt" << binName[iB] << "  shape  	- 	- 	1.00  	-   	-  	-	-	-" << std::endl;
	  if (dyj->GetBinContent(iB)>0.)
    textFile << "dyjBin_mt" << binName[iB] << " shape  	- 	-  	- 	1.00    -  	-	-	-" << std::endl;
	  if (ztt->GetBinContent(iB)>0.)
    textFile << "zttBin_mt" << binName[iB] << " shape  	- 	-  	- 	-	1.00    -  	-	-" << std::endl;
	  if (ww->GetBinContent(iB)>0.)
    textFile << "wwBin_mt" << binName[iB] << " shape  	- 	-  	 - 	-	-	1.00  	-	-" << std::endl;
	  if (sT->GetBinContent(iB)>0.)
    textFile << "sTBin_mt" << binName[iB] << " shape  	- 	- 	-	-	-	-	1.00  	-" << std::endl;
	  if (fakes->GetBinContent(iB)>0.)
    textFile << "fakesBin_mt" << binName[iB] << " shape  	- 	-  	-  	- 	-	-	-	1.00 " << std::endl;



  }
*/
if (bFirst) {

	fileout->cd();
	allbkg->Write();
	tt_shape->Write();
	wj_shape->Write();
	dyj_shape->Write();
	ztt_shape->Write();
	dib_shape->Write();
	ww_shape->Write();
	sT_shape->Write();
	ttx_shape->Write();
	fakes_shape->Write();
	rest_shape->Write();

	tt_norm->Write();
	wj_norm->Write();
	dyj_norm->Write();
	ztt_norm->Write();
	dib_norm->Write();
	ww_norm->Write();
	sT_norm->Write();
	ttx_norm->Write();
	fakes_norm->Write();
	rest_norm->Write();

}

}

 
