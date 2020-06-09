
TH1D * unrolled(TH2D * hist2D,
                TString name) {

  int nBinsX = hist2D->GetNbinsX();
  int nBinsY = hist2D->GetNbinsY();

  int nBins = nBinsX * nBinsY;

  TH1D * hist1D = new TH1D(name,"",nBins,double(0.),double(nBins));
  for (int ix=0; ix<nBinsX; ++ix) {
    for (int iy=0; iy<nBinsY; ++iy) {
      int bin = iy*nBinsX + ix + 1;
      double x = hist2D->GetBinContent(ix+1,iy+1);
      double ex = hist2D->GetBinError(ix+1,iy+1);
      hist1D->SetBinContent(bin,x);
      hist1D->SetBinError(bin,ex);
    }
  }


  return hist1D;

}


void Unroll(){
TH1D hist;
    

       TString histName


      hist = (TH1D*)unrolled(hist2D,histName);
      for (int iB=1; iB<=nBins; ++iB) {
        double x = hist[i]->GetBinContent(iB);
        double e = hist[i]->GetBinError(iB);
        hist->SetBinContent(iB,norm*x);
        hist->SetBinError(iB,norm*e);
      }

		TString fout = " FILEHERE"
		TFile *Target;
	        Target = TFile::Open (fout, "RECREATE");



}



