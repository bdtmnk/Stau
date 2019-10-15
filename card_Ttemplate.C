void card_Ttemplate() {


	/*

  KEY: TH1D	data_obs;1	hInvMassMuel topPtRwgt
  KEY: TH1D	wjets;1	hInvMassMuel topPtRwgt
  KEY: TH1D	TTPowHeg;1	hInvMassMuel topPtRwgt
  KEY: TH1D	TTPowHegHeg;1	hInvMassMuel topPtRwgt
  KEY: TH1D	rest_bkg;1	hInvMassMuel topPtRwgt
  KEY: TCanvas	hInvMassMuEl_6;1	hInvMassMuEl_6
*/

  TFile * file = new TFile("Ttemplate.root");
  TH1D * data_obs = (TH1D*)file->Get("data_obs");
  TH1D * wjets = (TH1D*)file->Get("wj");
  TH1D * TTJets = (TH1D*)file->Get("tt");
  TH1D * rest_bkg = (TH1D*)file->Get("rest_bkg");

  std::ofstream textFile("smTtemplate.txt");
  textFile << "imax 1   number of channels" << std::endl;
  textFile << "jmax *   number of backgrounds" << std::endl;
  textFile << "kmax *   number of nuisance parameters" << std::endl;
  textFile << "-----------------" << std::endl;
  textFile << "observation " << data_obs->GetSumOfWeights() << std::endl;
  textFile << "observation " << data_obs->Integral() << std::endl;
  textFile << "-----------------" << std::endl;
  textFile << "shapes * *  Ttemplate.root  $PROCESS    $PROCESS_$SYSTEMATIC " << std::endl;
  textFile << "-----------------" << std::endl;
  textFile << "bin                   stau    stau" << std::endl;
  textFile << "process              tt  rest_bkg" << std::endl;
  textFile << "process                0     1" << std::endl;
  textFile << "rate    "
	   << TTJets->Integral() << " " 
	   << rest_bkg->Integral() << std::endl; 

 
  textFile << "-----------------------------" << std::endl;
  textFile << "bkg_norm        lnU   -         10" << std::endl;
  textFile << "CMS_eff_m       lnN      1.03   1.03"<< std::endl;
  textFile << "CMS_eff_e       lnN      1.04   1.04"<< std::endl;
//  textFile << "CMS_met         lnN      1.04    1.04"<< std::endl;
  textFile << std::endl;
	   cout<< wjets->Integral() << "  "<<wjets->GetSumOfWeights()<<endl;

} 
