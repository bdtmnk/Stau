void CreateDatacardsS() {


	/*

 KEY: TH1D	hDZeta_19;1	hDZetaInvMass gt 90
  KEY: TH1D	tt;1	hDZetaInvMass gt 90
  KEY: TH1D	wj;1	hDZetaInvMass gt 90
  KEY: TH1D	dyj;1	hDZetaInvMass gt 90
  KEY: TH1D	sT;1	hDZetaInvMass gt 90
  KEY: TH1D	dib;1	hDZetaInvMass gt 90
  KEY: TH1D	ttx;1	hDZetaInvMass gt 90
  KEY: TH1D	qcd;1	hDZetaInvMass gt 90
  KEY: TH1D	data_obs;1	hDZetaInvMass gt 90
  KEY: TH1D	signal;1	hDZetaInvMass gt 90

*/


  TFile * file = new TFile("BkgTemplates_hDZeta.root");
  TFile * fileS = new TFile("SignalTemplates_hDZeta.root");
  TH1D * data_obs = (TH1D*)file->Get("data_obs_hDZeta_19");
  TH1D * data_obsMC = (TH1D*)file->Get("data_obsMC_hDZeta_19");
  TH1D * TTJets = (TH1D*)file->Get("tt_hDZeta_19");
  TH1D * WJ = (TH1D*)file->Get("wj_hDZeta_19");
  TH1D * DYJ = (TH1D*)file->Get("dyj_hDZeta_19");
  TH1D * STOP = (TH1D*)file->Get("sT_hDZeta_19");
  TH1D * TTX = (TH1D*)file->Get("ttx_hDZeta_19");
  TH1D * VV = (TH1D*)file->Get("dib_hDZeta_19");
  TH1D * QCD = (TH1D*)file->Get("qcd_hDZeta_19");
  TH1D * Sig = (TH1D*)fileS->Get("stau150_LSP1_B_hDZeta");

  TFile * fileO = new TFile("signal.root","recreate");
  fileO->cd();
  Sig->Write("stau150_LSP1_B_hDZeta");
  TTJets->Write("tt");
  WJ->Write("wj");
  DYJ->Write("dyj");
  STOP->Write("sT");
  TTX->Write("ttx");
  VV->Write("dib");
  QCD->Write("qcd");
  data_obs->SetName("data_obs");
 // data_obs->Write();
  data_obsMC->Reset();
  data_obsMC->Add(TTJets,1);
  data_obsMC->Add(WJ,1);
  data_obsMC->Add(DYJ,1);
  data_obsMC->Add(STOP,1);
  data_obsMC->Add(TTX,1);
  data_obsMC->Add(VV,1);
  data_obsMC->Add(QCD,1);
  data_obsMC->Write("data_obs");

  fileO->Write();

  std::ofstream textFile("smS.txt");
  textFile << "imax 1   number of channels" << std::endl;
  textFile << "jmax *   number of backgrounds" << std::endl;
  textFile << "kmax *   number of nuisance parameters" << std::endl;
  textFile << "-----------------" << std::endl;
  textFile << "observation " << data_obsMC->GetSumOfWeights() << std::endl;
  //textFile << "observation " << data_obs->Integral() << std::endl;
  textFile << "-----------------" << std::endl;
 // textFile << "shapes * *  signal.root  $PROCESS    $PROCESS_$SYSTEMATIC " << std::endl;
 // textFile << "-----------------" << std::endl;
  textFile << "bin            stau    	stau    stau	stau 	stau	stau	stau	stau" << std::endl;
  textFile << "process        stau150_LSP1_B_hDZeta 	tt	wj	dyj	sT	ttx	dib	qcd" << std::endl;
  textFile << "process         0      	1       2	3	4	5	6	7" << std::endl;
  textFile << "rate    "
	   << Sig->GetSumOfWeights() << " " 
	   << TTJets->GetSumOfWeights() << " "
	   << WJ->GetSumOfWeights() << " "
	   << DYJ->GetSumOfWeights() << " "
	   << STOP->GetSumOfWeights() << " "
	   << TTX->GetSumOfWeights() << " "
	   << VV->GetSumOfWeights() << " "
	   << QCD->GetSumOfWeights() << endl;

 
  textFile << "-----------------------------" << std::endl;
//  textFile << "sign_xsec       lnN   	1.15    -	-	-	-	-	-	-" << std::endl;
  textFile << "top_norm        lnN   	-	1.10      -	-	-	-	-	-" << std::endl;
  textFile << "wj_norm         lnN   	-	-      1.10	-	-	-	-	-" << std::endl;
  textFile << "dyj_norm        lnN   	-	-      -	1.10	-	-	-	-" << std::endl;
  textFile << "sT_norm         lnN   	-	-      -	-	1.10	-	-	-" << std::endl;
  textFile << "ttx_norm        lnN   	-	-      -	-	-	1.10	-	-" << std::endl;
  textFile << "vv_norm         lnN   	-	-      -	-	-	-	1.10	-" << std::endl;
  textFile << "qcd_norm        lnN   	-	-      -	-	-	-	-	1.10" << std::endl;
  textFile << "CMS_eff_tau     lnN      1.05   1.05    1.05   	1.05    1.05    1.05    1.05    1.05"<< std::endl;
  textFile << "CMS_eff_m       lnN      1.03   1.03    1.03    	1.03    1.03    1.03    1.03    1.03"<< std::endl;
//  textFile << "CMS_eff_e       lnN      1.04   1.04    1.04    	1.04    1.04    1.04    1.04    1.04"<< std::endl;
  textFile << "CMS_met         lnN      1.04   1.04    1.04	1.04    1.04    1.04    1.04    1.04"<< std::endl;
  textFile << "CMS_lumi        lnN      1.027	1.027	1.027	1.027	1.027	1.027	1.027	1.027"<< std::endl;
  textFile << std::endl;
//	   cout<< wjets->Integral() << "  "<<wjets->GetSumOfWeights()<<endl;
cout<<" "<<Sig->GetSumOfWeights()<<"  "<<data_obsMC->Integral()<<endl;
} 
