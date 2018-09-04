
void genMET(TString Point="stau-stau_left_225_LSP50", TString Variable="METFB_15"){



TFile *in1  = new TFile(Point+"_Nominal_B.root","update");
TFile *in2  = new TFile(Point+"_genMET_B.root","read");



TH1D* h1 = (TH1D*)in1->Get("eltau/"+Variable);
TH1D* h2 = (TH1D*)in2->Get("eltau/"+Variable);
TH1D* hw = (TH1D*)in1->Get("eltau/histWeightsH");

						
TH1D* hUp  = (TH1D*) h1->Clone(Variable);
TH1D* hDown  = (TH1D*) h1->Clone(Variable);
TH1D* hww  = (TH1D*) hw->Clone("histWeightsH");

float SoW = hw->GetSumOfWeights();
int nBins = h1->GetNbinsX();

for (int iB=1;iB<=nBins+1;++iB) {
	
	float ch1 = h1->GetBinContent(iB);
	float ch2 = h2->GetBinContent(iB);
	float Errch1 = h1->GetBinError(iB);
	float Errch2 = h2->GetBinError(iB);
	float acceptance = 0.5*(ch1+ch2);
	float uncert = fabs(  (ch1-ch2));

	


	float errNom_ = 0;//
	if (ch1!=0 && ch2!=0) errNom_= sqrt(Errch1/ch1 * Errch1/ch1 + Errch2/ch2 * Errch2/ch2);

	h1->SetBinContent(iB,acceptance);
	hUp->SetBinContent(iB,max(ch1,ch2));
	hDown->SetBinContent(iB,min(ch1,ch2));

//delta x = Sqrt( (0.5*dx1)^2  + 0.5*dx2)^2  )
	float err = 0.5* sqrt( h1->GetBinError(iB)*h1->GetBinError(iB) + h2->GetBinError(iB)*h2->GetBinError(iB));

	h1->SetBinError(iB,err);
	hUp->SetBinError(iB,err);
	hDown->SetBinError(iB,err);

	//cout<<" h1 "<<in1->GetName()<<"  "<<in2->GetName()<<" bin "<<iB<<" h1BinCont "<<h1->GetBinContent(iB)<<" h2BinCont "<<h2->GetBinContent(iB)<<"  "<<hw->GetSumOfWeights()<<" acc "<<acceptance<<" uncert "<<uncert<<" error "<<acceptance*errNom_<<endl;

	}

in1->cd("eltau");
h1->Write();
in1->Close();
delete in1;

TFile *outUp  = new TFile(Point+"_METUp_B.root","update");
outUp->cd();
if (!(outUp->GetDirectory("eltau"))) outUp->mkdir("eltau");
outUp->cd("eltau");
hww->Write();
hUp->Write();
outUp->Close();
delete outUp;

TFile *outDown  = new TFile(Point+"_METDown_B.root","update");
outDown->cd();
if (!(outDown->GetDirectory("eltau"))) outDown->mkdir("eltau");
outDown->cd("eltau");
hww->Write();
hDown->Write();
outDown->Close();
delete outDown;

}
