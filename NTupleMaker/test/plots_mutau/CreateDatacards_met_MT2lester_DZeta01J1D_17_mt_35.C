void CreateDatacards_met_MT2lester_DZeta01J1D_17_mt_35() {


bool bFirst = false;

  //TFile * file = new TFile("Templ_met_MT2lester_DZeta01J1D_17_35invfb_mt_C1N2_SR");
  TFile *file = TFile::Open ("Templ_met_MT2lester_DZeta01J1D_17_35invfb_mt_C1N2_SR.root", "read");
  TFile *fileout = TFile::Open ("Templ_met_MT2lester_DZeta01J1D_17_35invfb_mt_C1N2_SR_out.root", "update");
  //file->cd("mt");
  
  TH1D * data_obs = (TH1D*)file->Get("data_obs_met_MT2lester_DZeta01J1D_17");

  data_obs->SetName("data_obs");

  TH1D * signal = (TH1D*)file->Get("1D_C1N2_700_LSP75_B_met_MT2lester_DZeta01J1D_17");
  //TH1D * rest_bkg = (TH1D*)file->Get("1D_rest_bkg_met_MT2lester_DZeta01J1D_17");
  TH1D * rest_bkg = (TH1D*)file->Get("1D_dib_met_MT2lester_DZeta01J1D_17");
  TH1D * ttx = (TH1D*)file->Get("1D_ttx_met_MT2lester_DZeta01J1D_17");
  TH1D * stop = (TH1D*)file->Get("1D_sT_met_MT2lester_DZeta01J1D_17");
  rest_bkg ->Add(ttx,1);
  rest_bkg ->Add(stop,1);
  rest_bkg->SetName("1D_rest_bkg_met_MT2lester_DZeta01J1D_17");
  TH1D * tt = (TH1D*)file->Get("1D_tt_met_MT2lester_DZeta01J1D_17");
  TH1D * wj = (TH1D*)file->Get("1D_wj_met_MT2lester_DZeta01J1D_17");
  TH1D * dyj = (TH1D*)file->Get("1D_dyj_met_MT2lester_DZeta01J1D_17");
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
	rest_bkg->Write();
	tt->Write();
	wj->Write();
	dyj->Write();
	qcd->Write();
/*
  for (int iB=1; iB<=nBins; ++iB) {
    TH1D * ttUp = (TH1D*)tt->Clone("1D_tt_met_MT2lester_DZeta01J1D_17_ttBin"+binName[iB]+"Up");
    TH1D * ttDown = (TH1D*)tt->Clone("1D_tt_met_MT2lester_DZeta01J1D_17_ttBin"+binName[iB]+"Down");
    float xtt = ttUp->GetBinContent(iB);
    float ett = ttUp->GetBinError(iB);
    ttUp->SetBinContent(iB,xtt+ett);
    ttDown->SetBinContent(iB,xtt-ett);
    ttUp->Write("1D_tt_met_MT2lester_DZeta01J1D_17_ttBin"+binName[iB]+"Up");
    ttDown->Write("1D_tt_met_MT2lester_DZeta01J1D_17_ttBin"+binName[iB]+"Down");
	

    TH1D * WUp = (TH1D*)wj->Clone("1D_wj_met_MT2lester_DZeta01J1D_17_wjBin"+binName[iB]+"Up");
    TH1D * WDown = (TH1D*)wj->Clone("1D_wj_met_MT2lester_DZeta01J1D_17_wjBin"+binName[iB]+"Down");
    float xwj = WUp->GetBinContent(iB);
    float ewj = WUp->GetBinError(iB);
    WUp->SetBinContent(iB,xwj+ewj);
    WDown->SetBinContent(iB,xwj-ewj);
    WUp->Write("1D_wj_met_MT2lester_DZeta01J1D_17_wjBin"+binName[iB]+"Up");
    WDown->Write("1D_wj_met_MT2lester_DZeta01J1D_17_wjBin"+binName[iB]+"Down");

    TH1D * dyjUp = (TH1D*)dyj->Clone("1D_dyj_met_MT2lester_DZeta01J1D_17_dyjBin"+binName[iB]+"Up");
    TH1D * dyjDown = (TH1D*)dyj->Clone("1D_dyj_met_MT2lester_DZeta01J1D_17_dyjBin"+binName[iB]+"Down");
    float xdyj = dyjUp->GetBinContent(iB);
    float edyj = dyjUp->GetBinError(iB);
    dyjUp->SetBinContent(iB,xdyj+ett);
    dyjDown->SetBinContent(iB,xdyj-ett);
    dyjUp->Write("1D_dyj_met_MT2lester_DZeta01J1D_17_dyjBin"+binName[iB]+"Up");
    dyjDown->Write("1D_dyj_met_MT2lester_DZeta01J1D_17_dyjBin"+binName[iB]+"Down");


    TH1D * rest_bkgUp = (TH1D*)rest_bkg->Clone("1D_rest_bkg_met_MT2lester_DZeta01J1D_17_rest_bkgBin"+binName[iB]+"Up");
    TH1D * rest_bkgDown = (TH1D*)rest_bkg->Clone("1D_rest_bkg_met_MT2lester_DZeta01J1D_17_rest_bkgBin"+binName[iB]+"Down");
    float xrest = rest_bkgUp->GetBinContent(iB);
    float erest = rest_bkgUp->GetBinError(iB);
    rest_bkgUp->SetBinContent(iB,xrest+erest);
    rest_bkgDown->SetBinContent(iB,xrest-erest);
    rest_bkgUp->Write("1D_rest_bkg_met_MT2lester_DZeta01J1D_17_rest_bkgBin"+binName[iB]+"Up");
    rest_bkgDown->Write("1D_rest_bkg_met_MT2lester_DZeta01J1D_17_rest_bkgBin"+binName[iB]+"Down");

    TH1D * qcdUp = (TH1D*)qcd->Clone("1D_qcd_met_MT2lester_DZeta01J1D_17_qcdBin"+binName[iB]+"Up");
    TH1D * qcdDown = (TH1D*)qcd->Clone("1D_qcd_met_MT2lester_DZeta01J1D_17_qcdBin"+binName[iB]+"Down");
    float xqcd= qcdUp->GetBinContent(iB);
    float eqcd = qcdUp->GetBinError(iB);
    qcdUp->SetBinContent(iB,xqcd+eqcd);
    qcdDown->SetBinContent(iB,xqcd-eqcd);
    qcdUp->Write("1D_qcd_met_MT2lester_DZeta01J1D_17_qcdBin"+binName[iB]+"Up");
    qcdDown->Write("1D_qcd_met_MT2lester_DZeta01J1D_17_qcdBin"+binName[iB]+"Down");
	
  }//loop in nBins
  
*/

}//bFirst
  for (int j=0;j<sz;++j){

 TString sys = Systematics[j].c_str();

  TFile *filesyst = TFile::Open ("Templ_met_MT2lester_DZeta01J1D_17_35invfb_mt_C1N2_SR_"+sys+".root", "read");

if (bFirst){

  TH1D * tt_syst = (TH1D*)filesyst->Get("1D_tt_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * wj_syst = (TH1D*)filesyst->Get("1D_wj_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * dyj_syst = (TH1D*)filesyst->Get("1D_dyj_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * qcd_syst = (TH1D*)filesyst->Get("1D_qcd_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * dib_syst = (TH1D*)filesyst->Get("1D_dib_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * sT_syst = (TH1D*)filesyst->Get("1D_sT_met_MT2lester_DZeta01J1D_17_"+sys);
  //TH1D * rest_bkg_syst = (TH1D*)filesyst->Get("1D_rest_bkg_met_MT2lester_DZeta01J1D_17_"+sys);
  TH1D * rest_bkg_syst = (TH1D*)filesyst->Get("1D_ttx_met_MT2lester_DZeta01J1D_17_"+sys);
  rest_bkg_syst->Add( dib_syst,1);
  rest_bkg_syst->Add( sT_syst,1);
  rest_bkg_syst->SetName("1D_rest_bkg_met_MT2lester_DZeta01J1D_17_"+sys);

  fileout->cd();
  tt_syst->Write();
  wj_syst->Write();
  dyj_syst->Write();
  qcd_syst->Write();
  rest_bkg_syst->Write();
}
  TH1D * signal_syst = (TH1D*)filesyst->Get("1D_C1N2_700_LSP75_B_met_MT2lester_DZeta01J1D_17_"+sys);
  fileout->cd();

	//cout<<" syst "<<signal_syst->GetName()<<endl;

  signal_syst->Write();
 

}

/*

  for (int iB=1; iB<=nBins; ++iB) {
    TH1D * signalUp = (TH1D*)signal->Clone("1D_C1N2_700_LSP75_B_met_MT2lester_DZeta01J1D_17_signalBin"+binName[iB]+"Up");
    TH1D * signalDown = (TH1D*)signal->Clone("1D_1D_C1N2_700_LSP75_B_met_MT2lester_DZeta01J1D_17_signalBin"+binName[iB]+"Down");
    float xsn = signalUp->GetBinContent(iB);
    float esn = signalUp->GetBinError(iB);
    signalUp->SetBinContent(iB,xsn+esn);
    signalDown->SetBinContent(iB,xsn-esn);
//if (bFirst){
    signalUp->Write("1D_C1N2_700_LSP75_B_met_MT2lester_DZeta01J1D_17_signalBin"+binName[iB]+"Up");
    signalDown->Write("1D_C1N2_700_LSP75_B_met_MT2lester_DZeta01J1D_17_signalBin"+binName[iB]+"Down");
//	}
  }

*/

  std::ofstream textFile("SR/cards_mt/C1N2_700_LSP75_met_MT2lester_DZeta01J1D_17_mt_35invfb.txt");
  textFile << "imax 1   number of channels" << std::endl;
  textFile << "jmax *   number of backgrounds" << std::endl;
  textFile << "kmax *   number of nuisance parameters" << std::endl;
  textFile << "-----------------" << std::endl;
  textFile << "observation " << data_obs->GetSumOfWeights() << std::endl;
//  textFile << "observation " << data_obs->Integral() << std::endl;
  textFile << "-----------------" << std::endl;
  textFile << "shapes * *  Templ_met_MT2lester_DZeta01J1D_17_35invfb_mt_C1N2_SR_out.root  $PROCESS    $PROCESS_$SYSTEMATIC " << std::endl;
  textFile << "-----------------" << std::endl;
  textFile << "bin                  mt	mt	mt	mt	mt mt" << std::endl;
  textFile << "process              1D_C1N2_700_LSP75_B_met_MT2lester_DZeta01J1D_17 1D_tt_met_MT2lester_DZeta01J1D_17 1D_wj_met_MT2lester_DZeta01J1D_17 1D_dyj_met_MT2lester_DZeta01J1D_17 1D_rest_bkg_met_MT2lester_DZeta01J1D_17 1D_qcd_met_MT2lester_DZeta01J1D_17" << std::endl;
  textFile << "process              0		1	2	3	4	5" << std::endl;
  textFile << "rate    "
	   << signal->GetSumOfWeights() << "  " 
	   << tt->GetSumOfWeights() << "  " 
	   << wj->GetSumOfWeights() << "  " 
	   << dyj->GetSumOfWeights() << "  " 
	   << rest_bkg->GetSumOfWeights() << "  "
	   << qcd->GetSumOfWeights() << std::endl; 

 
  textFile << "-----------------------------" << std::endl;
//  textFile << "lumi            lnN   	1.026   -	-	-	-	-" << std::endl;
  textFile << "lumi            lnN   	1.026   1.026	1.026	1.026	1.026	-" << std::endl;
  textFile << "sign_xsec       lnN      1.20     -      -       -       -	-" << std::endl;
  textFile << "tt_norm         lnN   	-       1.05	-	-	-	-" << std::endl;
  textFile << "wj_norm         lnN   	-       -	1.10	-	-	-" << std::endl;
  textFile << "dy_norm         lnN   	-       -	-	1.02	-	-" << std::endl;
  textFile << "bkg_norm        lnN   	-       -	-	-	1.20	-" << std::endl;
  textFile << "qcd_norm        lnN   	-       -	-	-	-	1.10" << std::endl;
  textFile << "jet_tfr         lnN   	1.10    1.10	1.10	1.10	1.10	-" << std::endl;
  textFile << "lept_tfr        lnN   	1.10    1.10	1.10	1.10	1.10	-" << std::endl;
  textFile << "tauID   	       lnN   	1.05    1.05	1.05	1.05	1.05	-" << std::endl;
  textFile << "CMS_btag        lnN      1.04  1.04	1.04	1.04	1.04	-"<< std::endl;
  textFile << "CMS_eff_m       lnN      1.02  1.02	1.02	1.02	1.02	-"<< std::endl;
  textFile << "CMS_eff_t       lnN      1.03  1.03	1.03	1.03	1.03	-"<< std::endl;
  textFile << "CMS_met         lnN      1.04  1.04	1.04	1.04	1.04	-"<< std::endl;
  textFile << "JetEn         	shape  	1	1	1	1	1    	1"<< std::endl;
  textFile << "UnclEn         	shape  	1	1	1	1	1    	1"<< std::endl;
  textFile << "MuEn         	shape  	1	1	1	1	1    	1"<< std::endl;
  textFile << "ElEn         	shape  	1	1	1	1	1    	1"<< std::endl;
  textFile << "TauEn         	shape  	1	1	1	1	1    	1"<< std::endl;
  textFile << "TopPt         	shape  	0	1	0	0	0    	1"<< std::endl;
  textFile << "ZPt         	shape  	0	0	0	1	0    	1"<< std::endl;
/*
  textFile << "ttBar rateParam    mt  1D_tt_met_MT2lester_DZeta01J1D_17 1.0 [0.5,1.5]		   "<< std::endl;
  textFile << "wjets rateParam    mt  1D_wj_met_MT2lester_DZeta01J1D_17 1.0 [0.5,1.5]		   "<< std::endl;
  textFile << "dyjets rateParam    mt  1D_dyj_met_MT2lester_DZeta01J1D_17 1.0 [0.5,1.5]		   "<< std::endl;
  textFile << "rest rateParam    mt  1D_rest_bkg_met_MT2lester_DZeta01J1D_17 1.0 [0.5,1.5]		   "<< std::endl;
  textFile << "qcd rateParam    mt  1D_qcd_met_MT2lester_DZeta01J1D_17 1.0 [0.5,1.5]		   "<< std::endl;
*/

  textFile << std::endl;
 /* for (int iB=1; iB<=nBins; ++iB) {
 //   textFile << "signalBin" << binName[iB] << " shape  1.00	- 	-  	-  	-	" << std::endl;
    textFile << "ttBin" << binName[iB] << "     shape	-	1.00	-	-	-  " << std::endl;
    textFile << "wjBin" << binName[iB] << "     shape  	- 	- 	1.00  	-   	-  " << std::endl;
    textFile << "dyjBin" << binName[iB] << "     shape  - 	-  	- 	1.00    -  " << std::endl;
    textFile << "rest_bkgBin" << binName[iB] << " shape  - 	-  	-  	- 	1.00  " << std::endl;

  }
*/
}

 
