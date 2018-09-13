#include <iostream>
#include <vector>
#include <map>
#include "boost/lexical_cast.hpp"
#include "boost/algorithm/string.hpp"
#include "boost/format.hpp"
#include "boost/program_options.hpp"
#include "boost/range/algorithm.hpp"
#include "boost/range/algorithm_ext.hpp"
#include "TPad.h"
#include "TROOT.h"
#include "TColor.h"
#include "TEfficiency.h"
#include "TMath.h"

/*root [1] TTree * tree = (TTree*)_file0->Get("makeroottree/AC1B");
root [2] TH1D *hist = new TH1D("hist","hist",50,-0.5,49.5);
root [3] tree->Draw("primvertex_count>>hist")
Info in <TCanvas::MakeDefCanvas>:  created default TCanvas with name c1
root [4] hist->Integral(0,20)
(Double_t) 126963.
root [5] hist->Integral(21,50)
(Double_t) 64478.0
root [6] 
*/

float Fit(Float_t N1,Float_t N2,Float_t Nvtx, Float_t r)
{
	Float_t fit=1+(r-1)*(Nvtx-N1)/(N2-N1);
	return fit;
}

void forPU(TString Signal ="C1N2_400_LSP25"  )
{
    //TFile * NPVmore20 = new TFile("C1N2_200_LSP25_NPVmore20.root");
    //TFile * NPVless20 = new TFile("C1N2_200_LSP25_NPVless20.root");
    TFile * NPVmore20 = new TFile(Signal+"_NPVmore20.root");
    TFile * NPVless20 = new TFile(Signal+"_NPVless20.root");



    TFile * Ntuple;
    if (Signal.Contains("stau")) Ntuple = new TFile("/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/Skims/stau_stau/"+Signal+".root");
    if (Signal.Contains("C1N2")) Ntuple = new TFile("/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/Skims/C1N2/"+Signal+".root");
TTree * tree = (TTree*)Ntuple->Get("makeroottree/AC1B");
TH1D *hist = new TH1D("hist","hist",50,-0.5,49.5);
tree->Draw("primvertex_count>>hist");

Float_t	Nmore20 = hist->Integral(22,50);
Float_t	Nless20 = hist->Integral(0,21);


//Float_t	Nmore20 = 53605;
//Float_t	Nless20 = 137836;

    TH1D * histmore20 = (TH1D*)NPVmore20->Get("eltau/met_MT2lester_DZeta01J1D_17");
    TH1D * hNPVmore20 = (TH1D*)NPVmore20->Get("eltau/npv_17");
TH1D * histmore20notScaled = (TH1D*)histmore20->Clone("histmore20notScaled");
    TH1D * histless20 = (TH1D*)NPVless20->Get("eltau/met_MT2lester_DZeta01J1D_17");
    TH1D * hNPVless20 = (TH1D*)NPVless20->Get("eltau/npv_17");
TH1D * histless20notScaled = (TH1D*)histless20->Clone("histless20notScaled");


	cout <<"histless20->GetSumOfWeights() "<<histless20->GetSumOfWeights() <<"  " <<histless20->GetSumOfWeights()/Nless20<< endl;
	cout <<"histmore20->GetSumOfWeights() "<<histmore20->GetSumOfWeights() <<"  " <<histmore20->GetSumOfWeights()/Nmore20<<endl;
	Float_t N1 = hNPVless20->GetMean();
	Float_t N2 = hNPVmore20->GetMean();

	histmore20->Scale(1/Nmore20);
	histless20->Scale(1/Nless20);

	for (int i=1; i<59; ++i) {if (histless20->GetBinContent(i)<0.000000001) {histless20->SetBinContent(i,10000);}}


	TH1D * R = (TH1D*)histmore20->Clone("R");
	R->Divide(histless20);


cout <<histless20->GetBinContent(20) <<endl;
cout <<histmore20->GetBinContent(20) <<endl;
cout <<R->GetBinContent(20) <<endl;

Float_t sum=0;
Int_t ii=0;
for (int i=1; i<59; ++i) {if (R->GetBinContent(i)>0.01&&(histmore20notScaled->GetBinContent(i)>5) &&(histless20notScaled->GetBinContent(i)>5)) {sum=sum+R->GetBinContent(i);ii++;}}

cout<<ii<<endl;
cout<<sum<<endl;
cout<<"average??  "<<sum/ii<<endl;

Float_t Delta=0;
Int_t iii=0;
for (int i=1; i<59; ++i) {if ((R->GetBinContent(i)>0.01) &&(histmore20notScaled->GetBinContent(i)>5) &&(histless20notScaled->GetBinContent(i)>5)) {Delta=Delta+(R->GetBinContent(i)-sum/ii)*(R->GetBinContent(i)-sum/ii);iii++;}}

cout<<"delta=  "<<TMath::Sqrt(Delta/iii)<<endl;
Delta=Delta/iii;
//R0J->Draw();

  //TH1D * histAcceptmore20 = (TH1D*)NPVmore20->Clone("data_obs");




   TCanvas *canv1 = new TCanvas("Canvas_1", "Canvas_1",400,300,1200,800);
   R->SetTitle(Signal);
   R->GetXaxis()->SetTitle("N cut");
   R->GetYaxis()->SetTitle("r");

   R->Draw("");
   TLine *line = new TLine(0.,1.0,59.,1.0);
   line->SetLineColor(2);
   line->Draw("same");
   canv1->Print("/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/test/plots_eltau/"+Signal+"efficiencies.pdf");



	TFile *Target = TFile::Open ("/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/test/plots_eltau/"+Signal+"efficiencies.root", "recreate");    
	Target->cd();
	
	histmore20notScaled->Write();
	histless20notScaled->Write();
	histmore20->Write();
	histless20->Write();
	R->Write();

	//Target->Write();
	delete Target;

cout<<"systemayic!!!" <<endl;

    TFile * NPVdata = new TFile("NVtx_SLe_03Feb2017_35p9ifb.root");
    TH1D * hNPVdata = (TH1D*)NPVdata->Get("nvertex_SingleElectron");

Float_t check =0;
Float_t def =0;
Float_t up =0;
Float_t down =0;
for (int i=1; i<80; ++i) { check=check+hNPVdata->GetBinContent(i+1); }
for (int i=1; i<80; ++i) { def=def+hNPVdata->GetBinContent(i+1)*Fit(N1,N2,i,sum/ii); }
for (int i=1; i<80; ++i) { up=up+hNPVdata->GetBinContent(i+1)*Fit(N1,N2,i,sum/ii+Delta); }
for (int i=1; i<80; ++i) { down=down+hNPVdata->GetBinContent(i+1)*Fit(N1,N2,i,sum/ii-Delta); }

hist->Scale(1/hist->GetSumOfWeights());
Float_t defFastSim =0;
for (int i=1; i<80; ++i) { defFastSim=defFastSim+hist->GetBinContent(i+1)*Fit(N1,N2,i,sum/ii); }


cout <<"check  " <<check<<endl;
cout <<"def  " <<def<<endl;
cout <<"up  " <<up<<endl;
cout <<"down  " <<down<<endl;
cout <<"defFastSim  " <<defFastSim<<endl;

}
