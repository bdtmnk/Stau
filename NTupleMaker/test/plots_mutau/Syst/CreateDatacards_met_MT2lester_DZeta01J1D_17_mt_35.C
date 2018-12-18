void CreateDatacards_met_MT2lester_DZeta01J1D_17_mt_35() {


bool bFirst = true;

  //TFile * file = new TFile("Templ_met_MT2lester_DZeta01J1D_17_35invfb_mt_C1N2_SR_CR1");
  TFile *file = TFile::Open ("Templ_met_MT2lester_DZeta01J1D_17_35invfb_mt_C1N2_SR_CR1.root", "read");
  TFile *fileout = TFile::Open ("Templ_met_MT2lester_DZeta01J1D_17_35invfb_mt_C1N2_SR_CR1_out.root", "update");
  //file->cd("mt");
  
  TH1D * data_obs = (TH1D*)file->Get("data_obs_met_MT2lester_DZeta01J1D_17");
//  TH1D * data_obs = (TH1D*)file->Get("1D_allbkg_met_MT2lester_DZeta01J1D_17");

  data_obs->SetName("data_obs");

  TH1D * signal = (TH1D*)file->Get("1D_C1N2_100_LSP1_B_met_MT2lester_DZeta01J1D_17");


  TH1D * tt = (TH1D*)file->Get("1D_tt_met_MT2lester_DZeta01J1D_17");
  TH1D * wj = (TH1D*)file->Get("1D_wj_met_MT2lester_DZeta01J1D_17");
  TH1D * dyj = (TH1D*)file->Get("1D_dyj_met_MT2lester_DZeta01J1D_17");
  TH1D * ztt = (TH1D*)file->Get("1D_ztt_met_MT2lester_DZeta01J1D_17");
  TH1D * dib = (TH1D*)file->Get("1D_dib_met_MT2lester_DZeta01J1D_17");
  TH1D * ww = (TH1D*)file->Get("1D_ww_met_MT2lester_DZeta01J1D_17");
  TH1D * ttx = (TH1D*)file->Get("1D_ttx_met_MT2lester_DZeta01J1D_17");
  TH1D * sT = (TH1D*)file->Get("1D_sT_met_MT2lester_DZeta01J1D_17");
  TH1D * qcd = (TH1D*)file->Get("1D_qcd_met_MT2lester_DZeta01J1D_17");


  vector <string> Systematics;
  Systematics.push_back("JetEnUp");
  Systematics.push_back("UnclEnUp");
  Systematics.push_back("MuEnUp");
  Systematics.push_back("ElEnUp");
  Systematics.push_back("TauEnUp");
  Systematics.push_back("TopPtUp");
  Systematics.push_back("ZPtUp");

  Systematics.push_back("JetEnDown");
  Systematics.push_back("UnclEnDown");
  Systematics.push_back("MuEnDown");
  Systematics.push_back("ElEnDown");
  Systematics.push_back("TauEnDown");
  Systematics.push_back("TopPtDown");
  Systematics.push_back("ZPtDown");

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
	qcd->Write();
/*
  for (int iB=1; iB<=nBins; ++iB) {
    TH1D * ttUp = (TH1D*)tt->Clone("1D_tt_met_MT2lester_DZeta01J1D_17_ttBin"+binName[iB]+"Up");
    TH1D * ttDown = (TH1D*)tt->Clone("1D_tt_met_MT2lester_DZeta01J1D_17_ttBin"+binName[iB]+"Down");
    float xtt = ttUp->GetBinContent(iB);
    float ett = ttUp->GetBinError(iB);
    ttUp->SetBinContent(iB,xtt+ett);
    ttDown->SetBinContent(iB,xtt-ett);
    ttUp->Write("1D_tt_met_MT2lester_DZeta01J1D_17_ttBin_mt"+binName[iB]+"Up");
    ttDown->Write("1D_tt_met_MT2lester_DZeta01J1D_17_ttBin_mt"+binName[iB]+"Down");
	

    TH1D * WUp = (TH1D*)wj->Clone("1D_wj_met_MT2lester_DZeta01J1D_17_wjBin"+binName[iB]+"Up");
    TH1D * WDown = (TH1D*)wj->Clone("1D_wj_met_MT2lester_DZeta01J1D_17_wjBin"+binName[iB]+"Down");
    float xwj = WUp->GetBinContent(iB);
    float ewj = WUp->GetBinError(iB);
    WUp->SetBinContent(iB,xwj+ewj);
    WDown->SetBinContent(iB,xwj-ewj);
    WUp->Write("1D_wj_met_MT2lester_DZeta01J1D_17_wjBin_mt"+binName[iB]+"Up");
    WDown->Write("1D_wj_met_MT2lester_DZeta01J1D_17_wjBin_mt"+binName[iB]+"Down");

    TH1D * dyjUp = (TH1D*)dyj->Clone("1D_dyj_met_MT2lester_DZeta01J1D_17_dyjBin"+binName[iB]+"Up");
    TH1D * dyjDown = (TH1D*)dyj->Clone("1D_dyj_met_MT2lester_DZeta01J1D_17_dyjBin"+binName[iB]+"Down");
    float xdyj = dyjUp->GetBinContent(iB);
    float edyj = dyjUp->GetBinError(iB);
    dyjUp->SetBinContent(iB,xdyj+ett);
    dyjDown->SetBinContent(iB,xdyj-ett);
    dyjUp->Write("1D_dyj_met_MT2lester_DZeta01J1D_17_dyjBin_mt"+binName[iB]+"Up");
    dyjDown->Write("1D_dyj_met_MT2lester_DZeta01J1D_17_dyjBin_mt"+binName[iB]+"Down");

    TH1D * zttUp = (TH1D*)ztt->Clone("1D_ztt_met_MT2lester_DZeta01J1D_17_zttBin"+binName[iB]+"Up");
    TH1D * zttDown = (TH1D*)ztt->Clone("1D_ztt_met_MT2lester_DZeta01J1D_17_zttBin"+binName[iB]+"Down");
    float xztt = zttUp->GetBinContent(iB);
    float eztt = zttUp->GetBinError(iB);
    zttUp->SetBinContent(iB,xztt+ett);
    zttDown->SetBinContent(iB,xztt-ett);
    zttUp->Write("1D_ztt_met_MT2lester_DZeta01J1D_17_zttBin_mt"+binName[iB]+"Up");
    zttDown->Write("1D_ztt_met_MT2lester_DZeta01J1D_17_zttBin_mt"+binName[iB]+"Down");


    TH1D * dibUp = (TH1D*)dib->Clone("1D_dib_met_MT2lester_DZeta01J1D_17_dibBin_mt"+binName[iB]+"Up");
    TH1D * dibDown = (TH1D*)dib->Clone("1D_dib_met_MT2lester_DZeta01J1D_17_dibBin_mt"+binName[iB]+"Down");
    float xdib = dibUp->GetBinContent(iB);
    float edib = dibUp->GetBinError(iB);
    dibUp->SetBinContent(iB,xdib+edib);
    dibDown->SetBinContent(iB,xdib-edib);
    dibUp->Write("1D_dib_met_MT2lester_DZeta01J1D_17_dibBin_mt"+binName[iB]+"Up");
    dibDown->Write("1D_dib_met_MT2lester_DZeta01J1D_17_dibBin_mt"+binName[iB]+"Down");


    TH1D * wwUp = (TH1D*)ww->Clone("1D_ww_met_MT2lester_DZeta01J1D_17_wwBin_mt"+binName[iB]+"Up");
    TH1D * wwDown = (TH1D*)ww->Clone("1D_ww_met_MT2lester_DZeta01J1D_17_wwBin_mt"+binName[iB]+"Down");
    float xww = wwUp->GetBinContent(iB);
    float eww = wwUp->GetBinError(iB);
    wwUp->SetBinContent(iB,xww+eww);
    wwDown->SetBinContent(iB,xww-eww);
    wwUp->Write("1D_ww_met_MT2lester_DZeta01J1D_17_wwBin_mt"+binName[iB]+"Up");
    wwDown->Write("1D_ww_met_MT2lester_DZeta01J1D_17_wwBin_mt"+binName[iB]+"Down");



    TH1D * sTUp = (TH1D*)sT->Clone("1D_sT_met_MT2lester_DZeta01J1D_17_sTBin"+binName[iB]+"Up");
    TH1D * sTDown = (TH1D*)sT->Clone("1D_sT_met_MT2lester_DZeta01J1D_17_sTBin"+binName[iB]+"Down");
    float xsT = sTUp->GetBinContent(iB);
    float esT = sTUp->GetBinError(iB);
    sTUp->SetBinContent(iB,xsT+esT);
    sTDown->SetBinContent(iB,xsT-esT);
    sTUp->Write("1D_sT_met_MT2lester_DZeta01J1D_17_sTBin_mt"+binName[iB]+"Up");
    sTDown->Write("1D_sT_met_MT2lester_DZeta01J1D_17_sTBin_mt"+binName[iB]+"Down");


    TH1D * ttxUp = (TH1D*)ttx->Clone("1D_ttx_met_MT2lester_DZeta01J1D_17_ttxBin"+binName[iB]+"Up");
    TH1D * ttxDown = (TH1D*)ttx->Clone("1D_ttx_met_MT2lester_DZeta01J1D_17_ttxBin"+binName[iB]+"Down");
    float xttx = ttxUp->GetBinContent(iB);
    float ettx = ttxUp->GetBinError(iB);
    ttxUp->SetBinContent(iB,xttx+ettx);
    ttxDown->SetBinContent(iB,xttx-ettx);
    ttxUp->Write("1D_ttx_met_MT2lester_DZeta01J1D_17_ttxBin_mt"+binName[iB]+"Up");
    ttxDown->Write("1D_ttx_met_MT2lester_DZeta01J1D_17_ttxBin_mt"+binName[iB]+"Down");



    TH1D * qcdUp = (TH1D*)qcd->Clone("1D_qcd_met_MT2lester_DZeta01J1D_17_qcdBin"+binName[iB]+"Up");
    TH1D * qcdDown = (TH1D*)qcd->Clone("1D_qcd_met_MT2lester_DZeta01J1D_17_qcdBin"+binName[iB]+"Down");
    float xqcd= qcdUp->GetBinContent(iB);
    float eqcd = qcdUp->GetBinError(iB);
    qcdUp->SetBinContent(iB,xqcd+eqcd);
    qcdDown->SetBinContent(iB,xqcd-eqcd);
    qcdUp->Write("1D_qcd_met_MT2lester_DZeta01J1D_17_qcdBin_mt"+binName[iB]+"Up");
    qcdDown->Write("1D_qcd_met_MT2lester_DZeta01J1D_17_qcdBin_mt"+binName[iB]+"Down");
	
  }//loop in nBins
  
*/

}//bFirst
  for (int j=0;j<sz;++j){

 TString sys = Systematics[j].c_str();

  TFile *filesyst = TFile::Open ("Templ_met_MT2lester_DZeta01J1D_17_35invfb_mt_C1N2_SR_CR1_"+sys+".root", "read");

if (bFirst){

  TH1D * tt_syst = (TH1D*)filesyst->Get("1D_tt_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * wj_syst = (TH1D*)filesyst->Get("1D_wj_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * dyj_syst = (TH1D*)filesyst->Get("1D_dyj_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * ztt_syst = (TH1D*)filesyst->Get("1D_ztt_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * dib_syst = (TH1D*)filesyst->Get("1D_dib_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * ww_syst = (TH1D*)filesyst->Get("1D_ww_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * sT_syst = (TH1D*)filesyst->Get("1D_sT_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * ttx_syst = (TH1D*)filesyst->Get("1D_ttx_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * qcd_syst = (TH1D*)filesyst->Get("1D_qcd_met_MT2lester_DZeta01J1D_17_"+sys);

  fileout->cd();
  tt_syst->Write();
  wj_syst->Write();
  dyj_syst->Write();
  ztt_syst->Write();
  dib_syst->Write();
  ww_syst->Write();
  sT_syst->Write();
  ttx_syst->Write();
  qcd_syst->Write();
}
  TH1D * signal_syst = (TH1D*)filesyst->Get("1D_C1N2_100_LSP1_B_met_MT2lester_DZeta01J1D_17_"+sys);
  fileout->cd();

	//cout<<" syst "<<signal_syst->GetName()<<endl;

  signal_syst->Write();
 

}


}
 
