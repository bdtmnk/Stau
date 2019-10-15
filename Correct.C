void Correct() {

  TFile * file = new TFile("smT.root","read");
  file->cd("");
  TH1D * data_obs = (TH1D*)file->Get("data_obs");
  
  TH1D * TT = (TH1D*)file->Get("TTMG");
  TH1D * wj = (TH1D*)file->Get("wjets");
  TH1D * bkg = (TH1D*)file->Get("rest_bkg");
  TT->Scale(0.995);

  TFile * file1 = new TFile("smTv2.root","recreate");
  file1->cd();
  data_obs->Write("data_obs");
  TT->Rebin(2);
  bkg->Rebin(2);
  wj->Rebin(2);
  data_obs->Rebin(2);
  TT->Write("TTMG");
  bkg->Write("rest_bkg");
  wj->Write("wjets");
  file1->Write();
  file1->Close();

}
