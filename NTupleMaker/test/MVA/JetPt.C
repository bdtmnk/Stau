void	CompareTwoHistsFromRoot()
{
	TString File2 = "/nfs/dust/cms/user/bobovnii/HLLHCntuples_ver2/WToLNu_2J_14TeV1_ntuple/WToLNu_2J_14TeV1_ntuple.root"
	TString File1 = "/nfs/dust/cms/user/bobovnii/HLLHCntuples_ver2/WToLNu_2J_14TeV-madgraphMLM-pythia8/test.root"
	TString Variable = "pfjet_pt"; //
	TString histName2 = "jetPtDelphes"
	TString histName1 = "jetPtFullSim"

	Float nBins = 50;
	Float xmin = 20;
	Float xmax = 500;


	TH1D * hist1 = new TH1D(histName1,"",nBins,xmin,xmax);
  	TH1D * hist2 = new TH1D(histName2,"",nBins,xmin,xmax);


    TFile * file1 = new TFile(File1);
    TFile * file2 = new TFile(File2);

    TTree * tree1 = (TTree*)file1->Get("makeroottree/AC1B"); 
    TTree * tree2 = (TTree*)file2->Get("AC1B");
    tree1->Draw(Variable+">>"+histName1);
    tree2->Draw(Variable+">>"+histName2);


    TCanvas* canv1 = new TCanvas("c1", "c1");
    canv1->cd();
    std::vector<TPad*> pads = TwoPadSplit(0.29, 0.00, 0.00);
    //pads[0]->SetLogy(logY);
    
    std::vector<TH1*> h = CreateAxisHists(2, hist1, hist1->GetXaxis()->GetXmin(), hist1->GetXaxis()->GetXmax()-0.01);\
	//if (Variable.Contains("MT")) h = CreateAxisHists(2, hist1, 0, 120-0.01);
	//if(!logY && Variable.Contains("pt")) h = CreateAxisHists(2, hist1, 0, 100-0.01);
	//if(!logY && Variable.Contains("pt[0]")) h = CreateAxisHists(2, hist1, 25, 100-0.01);
	//if(!logY && Variable.Contains("Ut")) h = CreateAxisHists(2, hist1, 0, 200-0.01);
	//if(!logY && Variable.Contains("Utr")) h = CreateAxisHists(2, hist1, -100, 100-0.01);
	if(!logY && Variable.Contains("Ucol")) h = CreateAxisHists(2, hist1, -150, 50-0.01);
    h[0]->Draw();
    
    std::string units="";
    std::string xtitle_ = (std::string) xtitle;
    size_t pos = xtitle_.find("[");
    if(pos!=std::string::npos) {
        units = xtitle_.substr(pos+1, xtitle_.find("]") - pos -1 );
        xtitle_ = xtitle_.substr(0, pos);
    }
        
    pads[1]->cd();
    h[1]->Draw();    
    SetupTwoPadSplitAsRatio(pads, "weighted/unweighted", true, 0.4, 1.6);
    StandardAxes(h[1]->GetXaxis(), h[0]->GetYaxis(),xtitle_ ,units);
    h[1]->GetYaxis()->SetNdivisions(4);
    h[1]->GetXaxis()->SetTitleOffset(1.2);
    h[1]->GetYaxis()->SetTitleOffset(2.0);
    pads[0]->cd();
    h[0]->GetYaxis()->SetTitleOffset(2.0);
    pads[1]->SetGrid(0,1);
    //it complains if the minimum is set to 0 and you try to set log y scale
    //if(logY) h[0]->SetMinimum(1);
    pads[0]->cd();





    canv1->Update();


	TH1D * ratioH = (TH1D*)hist1->Clone("ratioH");


    for (int iB=1; iB<=nBins; ++iB) {
        float x1 = hist1->GetBinContent(iB);
        float x2 = hist2->GetBinContent(iB);
   
        if (x1>0&&x2>0) {
            float e1 = hist1->GetBinError(iB);
            float ratio = x1/x2;
            float eratio = e1/x2;
            ratioH->SetBinContent(iB,ratio);
            ratioH->SetBinError(iB,eratio);
        }
        else {
            ratioH->SetBinContent(iB,1000);
        }
    }
 pads[1]->cd();
    //ratioErrH->GetYaxis()->SetRangeUser(0.4,1.6);
    //ratioErrH->GetXaxis()->SetRangeUser(50,120);
    //ratioErrH->Draw("e2same");
    ratioH->GetYaxis()->SetRangeUser(0.4,1.6);
    ratioH->SetMarkerSize(0.5);
    ratioH->Draw("pe0same");


    pads[0]->cd();



   TLegend *legend = PositionedLegend(0.55, 0.20, 3, 0.03);
    legend->SetTextFont(42);
    //legend-> SetNColumns(2);
    hist1->SetMarkerColor(1);
    hist1->SetLineColor(1);
    hist1->SetFillColor(1);
    hist1->SetFillStyle(0);
    hist1->SetLineWidth(2);
    hist1->SetMarkerStyle(20);
    hist1->SetMarkerSize(1.1);
    
    legend->AddEntry(hist1, "FullSim", "ple");

    hist2->SetMarkerColor(kRed);
    hist2->SetLineColor(1);
    hist2->SetFillColor(1);
    hist2->SetFillStyle(0);
    hist2->SetLineWidth(2);
    hist2->SetMarkerStyle(20);
    hist2->SetMarkerSize(1.1);
    legend->AddEntry(hist2,"Delphes", "ple");
    hist1->Draw();
    hist2->Draw("same");



    legend->Draw();

    canv1->Print("/nfs/dust/cms/user/bobovnii//Final_"+Variable+".pdf");


}
