#include "/nfs/dust/cms/user/bobovnii/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/Plotting.h"
#include "/nfs/dust/cms/user/bobovnii/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/Plotting_Style.h"
#include "/nfs/dust/cms/user/bobovnii/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/HttStylesNew.cc"
#include "TPad.h"
#include "TROOT.h"
#include "TColor.h"
#include "TEfficiency.h"
#include "TMath.h"

void	CompareTwoHistsFromRoot()
{
//	TString File2 = "/nfs/dust/cms/user/alkaloge/MoriondMC_v1_wWeights//WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext2/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext2_997.root";
//	TString File1 = "/nfs/dust/cms/user/alkaloge/MoriondMC_v1_wWeights//WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext2/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext2_997.root";

      // TString File2 = "/nfs/dust/cms/user/rasp/ntuples/DYJets//DYJetsToLL_M-50_13TeV-madgraphMLM-pythia_ext2/DYJetsToLL_M-50_13TeV-madgraphMLM-pythia_ext2_997.root";
      // TString File1 = "/nfs/dust/cms/user/rasp/ntuples/DYJets//DYJetsToLL_M-50_13TeV-madgraphMLM-pythia_ext2/DYJetsToLL_M-50_13TeV-madgraphMLM-pythia_ext2_997.root";

//       TString File1 = "/nfs/dust/cms/user/alkaloge/MoriondMC_v1_wWeights//TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_97.root";
//       TString File2 = "/nfs/dust/cms/user/alkaloge/MoriondMC_v1_wWeights//TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_97.root";

      // TString File2 = "/nfs/dust/cms/user/alkaloge/MoriondMC_v1_wWeights//WWToLNuQQ_13TeV-powheg_ext/WWToLNuQQ_13TeV-powheg_ext_96.root";
      // TString File1 = "/nfs/dust/cms/user/alkaloge/MoriondMC_v1_wWeights//WWToLNuQQ_13TeV-powheg_ext/WWToLNuQQ_13TeV-powheg_ext_96.root";


	//TString File2 = "/nfs/dust/cms/user/bobovnii/HLLHCntuples_ver3/WToLNu/WToLNu_1J_14TeV_249960_ntuple.root";//


//without PU
	
	//TString File1 = "/nfs/dust/cms/user/bobovnii/HLLHCntuples_ver3/TEST/MiniEvents.root";
	//TString File2 = "/nfs/dust/cms/user/bobovnii/HLLHCntuples_ver3/TEST/WToLNu_1J_14TeV0_ntuple.root";


//TString File1 = "/nfs/dust/cms/user/bobovnii/HLLHCntuples_ver3/DYToLL-M-50_2J_14TeV-madgraphMLM-pythia8/DYToLL-M-50_2J_14TeV-madgraphMLM-pythia8_526.root";
//TString File2 = "/nfs/dust/cms/user/bobovnii/HLLHCntuples_ver4/Delphes/DYToLL_M_50_2J_14TeV_madgraphMLM_pythia8_165670_ntuple.root";

TString File1 = "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/Skims/stau_stau_left/stau-stau_left_100_LSP1.root";
TString File2 = "/nfs/dust/cms/user/bobovnii/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/StauNtuples//NtupleTestStau100LSP1/MiniAOD_StauStau_sum.root";

//TString File1 = "/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/stau-stau_left_100_LSP1_B_OS.root";
//TString File2 = "/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/stau-stau100_LSP1My.root";



//TString File1 = "/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/stau-stau_left_100_LSP1_B_OS.root";
//TString File2 = "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/Skims/stau_stau_left/stau-stau_left_100_LSP1.root";



	TString histName2 = "private";
	TString histName1 = "official";

/*
	TString Variable = "pfjet_count[0]"; //
	TString xtitle = Variable;
	float nBins = 20;
	float xmin = -0.5;
	float xmax = 19.5;
*/

	//TString Variable = "(gentau_px[0]*gentau_px[0]+gentau_py[0]*gentau_py[0])"; //

	TString Variable = "genparticles_e"; //
	TString xtitle = "genparticles_e";
	
	   //int nBins = 4;
   double bins[5] = {0,100,200,300,1000};
	
	//int nBins = 41;
	//float xmin = -0.5;
	//float xmax = 40.5;
	
	
	int nBins = 30;
	float xmin = 0;
	float xmax = 300;

/*
	TString Variable = "pfjet_eta"; //
	TString xtitle = "pfjet_eta";
	float nBins = 40;
	float xmin = -3;
	float xmax = 3;
*/

gStyle->SetOptStat(0);
    TFile * file1 = new TFile(File1);
    TFile * file2 = new TFile(File2);

    TTree * tree1 = (TTree*)file1->Get("makeroottree/AC1B"); 
    TTree * tree2 = (TTree*)file2->Get("makeroottree/AC1B");
    
    //TTree * tree1 = (TTree*)file1->Get("mutau/T"); 
    //TTree * tree2 = (TTree*)file2->Get("mutau/T");

    //TTree * tree2 = (TTree*)file2->Get("makeroottree/AC1B"); 

    //TTree * tree2 = (TTree*)file2->Get("makeroottree/AC1B");
    //tree1->Draw(Variable+">>"+histName1);
    //tree2->Draw(Variable+">>"+histName2);


	TH1D * hist1genWeight = new TH1D("hist1genWeight","hist1genWeight",1,-10,10);
  	TH1D * hist2genWeight = new TH1D("hist2genWeight","hist2genWeight",1,-10,10);

	TH1D * hist1 = new TH1D("official","official",nBins,xmin,xmax);
  	TH1D * hist2 = new TH1D("private","private",nBins,xmin,xmax);
  	
  	//TH1D * hist1 = new TH1D("jetPtFullSim","jetPtFullSim",nBins,bins);
  	//TH1D * hist2 = new TH1D("jetPtDelphes","jetPtDelphes",nBins,bins);
    tree1->Draw(Variable+">>official","abs(genparticles_pdgid)==13");//, ,"pu_weight""muon_pt[0]>20 ""abs(genparticles_pdgid[2])==13");//|| muon_pt[0]>20 || electron_pt[0]>20");//&& pfjet_btag[0][0]  < 0.84 && pfjet_flavour[0]<7 "pfjet_pt>40 "
    tree2->Draw(Variable+">>private","abs(genparticles_pdgid)==13");//, "muon_pt[0]>20 ");//|| muon_pt[0]>20 || electron_pt[0]>20");

    tree1->Draw("genweight>>hist1genWeight");
    tree2->Draw("genweight>>hist2genWeight");

	cout <<" hist1->GetSumOfWeights() "<<hist1->GetSumOfWeights() <<endl;
	cout <<" hist2->GetSumOfWeights() "<<hist2->GetSumOfWeights() <<endl;

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
	//if(!logY && Variable.Contains("Ucol")) h = CreateAxisHists(2, hist1, -150, 50-0.01);
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
    SetupTwoPadSplitAsRatio(pads, "official/private", true, 0.0, 2.0);
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

    hist1->Sumw2();
    hist2->Sumw2();
    
    //TH1D * hist1W= (TH1D*)file1->Get("mutau/histWeightsH");
    //TH1D * hist2W= (TH1D*)file2->Get("mutau/histWeightsH");

    
    //hist1->Scale(1/hist1W->GetSumOfWeights());
	//hist2->Scale(1/hist2W->GetSumOfWeights());
    
	hist1->Scale(1/hist1genWeight->GetSumOfWeights());
	hist2->Scale(1/hist2genWeight->GetSumOfWeights());


    canv1->Update();


	TH1D * ratioH = (TH1D*)hist1->Clone("ratioH");


    for (int iB=1; iB<=nBins; ++iB) {
        float x1 = hist1->GetBinContent(iB);
        float x2 = hist2->GetBinContent(iB);
       cout << x1<<endl;
       cout << x2<<endl;

        if (x1>0&&x2>0) {
            float e1 = hist1->GetBinError(iB);
            float ratio = x1/x2;
            float eratio = e1/x2;
            ratioH->SetBinContent(iB,ratio);
            ratioH->SetBinError(iB,eratio);
    //cout << x1<<endl;

	cout << ratio<<endl;
        }
        else {
            ratioH->SetBinContent(iB,1000);
        }
    }
 pads[1]->cd();
    //ratioErrH->GetYaxis()->SetRangeUser(0.4,1.6);
    //ratioErrH->GetXaxis()->SetRangeUser(50,120);
    //ratioErrH->Draw("e2same");
    ratioH->GetYaxis()->SetRangeUser(0.0,2.0);
    ratioH->SetMarkerSize(0.5);
    ratioH->Draw("pe0same");



    pads[0]->cd();


   TLegend *legend = PositionedLegend(0.25, 0.15, 3, 0.01);
    legend->SetTextFont(32);
    //legend-> SetNColumns(2);
    hist1->SetMarkerColor(1);
    hist1->SetLineColor(1);
    hist1->SetFillColor(1);
    hist1->SetFillStyle(0);
    hist1->SetLineWidth(2);
    hist1->SetMarkerStyle(20);
    hist1->SetMarkerSize(1.1);
    
    legend->AddEntry(hist1, "official", "ple");

    hist2->SetMarkerColor(kRed);
    hist2->SetLineColor(kRed);
    hist2->SetFillColor(1);
    hist2->SetFillStyle(0);
    hist2->SetLineWidth(2);
    hist2->SetMarkerStyle(20);
    hist2->SetMarkerSize(1.1);
    legend->AddEntry(hist2,"private", "ple");
    //hist2->SetMaximum(0.06);
    hist2->Draw();
    hist1->Draw("same");

	TFile *smFile = TFile::Open ("PUsignalReweighting.root", "recreate");
	
				smFile->cd();
				hist2->Write();		
				hist1->Write();
				smFile->Write();
				smFile->Close();
				delete smFile;

    legend->Draw();

    canv1->Print("/nfs/dust/cms/user/bobovnii//test.pdf");


}
