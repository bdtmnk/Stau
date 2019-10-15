void PlotToys(TString fileName = "higgsCombineTest.FitDiagnostics.mH120.root",
	      int nBins = 100,
	      double xmin = -10,
	      double xmax = 10) {


 gStyle->SetOptFit(1111);

  TFile * file = new TFile(fileName);
  double limit;
  TTree * tree = (TTree*)file->Get("limit");
  tree->SetBranchAddress("limit",&limit);
  unsigned int nEntries = tree->GetEntries();
  TH1D * hist = new TH1D("hist","",nBins,xmin,xmax);

  for (unsigned int i=0; i<nEntries; ++i) {
    tree->GetEntry(i);
    if (i%4==0 && limit>-10 ) {
    //if (limit>-49) {
      hist->Fill(limit);
    }

  }

 // hist->SetStats(0);
  hist->Fit("gaus");


}
