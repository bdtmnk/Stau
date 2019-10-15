void CreateDatacards() {



  TFile * file = new TFile("BkgTemplates_hDZeta.root");
  TH1D * data_obs = (TH1D*)file->Get("data_hDZeta_15");
//  TH1D * wjets = (TH1D*)file->Get("wjets");
//  TH1D * TTJets = (TH1D*)file->Get("TT");
  TH1D * signal = (TH1D*)file->Get("C1C1_100_LSP1_B_hDZeta_15");
  TH1D * all_bkg = (TH1D*)file->Get("allbkg_hDZeta_15");

  std::ofstream textFile("C1C1_100_LSP1_mutau.txt");
  textFile << "imax 1   number of channels" << std::endl;
  textFile << "jmax *   number of backgrounds" << std::endl;
  textFile << "kmax *   number of nuisance parameters" << std::endl;
  textFile << "-----------------" << std::endl;
  textFile << "observation " << data_obs->GetSumOfWeights() << std::endl;
  textFile << "observation " << data_obs->Integral() << std::endl;
  textFile << "-----------------" << std::endl;
  textFile << "shapes * *  BkgTemplates_hDZeta.root  $PROCESS    $PROCESS_$SYSTEMATIC " << std::endl;
  textFile << "-----------------" << std::endl;
  textFile << "bin                  mutau	mutau	" << std::endl;
  textFile << "process              C1C1_100_LSP1  allbkg" << std::endl;
  textFile << "process                0      1  " << std::endl;
  textFile << "rate    "
	   << signal->Integral() << " " 
	   << all_bkg->Integral() << std::endl; 

 
  textFile << "-----------------------------" << std::endl;
  textFile << "bkg_norm        lnU   	-       10" << std::endl;
  textFile << "CMS_eff_m       lnN      1.03  1.03"<< std::endl;
  textFile << "CMS_eff_e       lnN      1.04  1.04"<< std::endl;
  textFile << "CMS_met         lnN      1.04  1.04"<< std::endl;
  textFile << std::endl;
	   cout<< all_bkg->Integral() << "  "<<all_bkg->GetSumOfWeights()<<endl;

} 
