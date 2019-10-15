#include "tdrstyle.C"
#include "CMS_lumi.C"

const char *myarg = NULL;

using namespace std;


const char *myarg = NULL;

int PlotLimits(int argc, const char **argv) {

	myarg = argv[1];
	cout<<"  this is a test "<<argv[1]<<endl;

	fileName = argv[1];	
//}


//void PlotLimit(char *fileList){

	       float yMax = 50 ;
	       float xMax = 120;
	       TString Lumi = "12 fb^{-1}";
	       TString massLSP = "1";
	       TString massPart = "m(#tilde{#tau}) [GeV]";
	       bool blindData = true;

  // char * filelist - List of files (output RooT files
  //                   produced by 'combine -M Asymptotic')
  // blindData -  true : blind observed limits
  //             false : show observed limits 
  // int benchmark - 0 : mh-max, mu = +200 GeV
  //                 1 : mh-mod +
  //                 2 : mh-mod -

//  fileName = argv[1];
  setTDRStyle();
  gStyle->SetOptFit(0000);
  gStyle->SetErrorX(0.5);

  const int nPoints = 100;

  // signal strength limits sigma*BR / sigma*BR (at tanb=30)
  double mA[nPoints];      
  double minus2R[nPoints]; 
  double minus1R[nPoints]; 
  double medianR[nPoints]; 
  double plus1R[nPoints];  
  double plus2R[nPoints];  
  double obsR[nPoints];    

  double obs[nPoints];
  double minus2[nPoints];
  double minus1[nPoints];
  double median[nPoints];
  double plus1[nPoints];
  double plus2[nPoints];

  std::ifstream inputList(fileList);

  TString FileList(fileList);

  TString fileName;

  double MH;
  double LIMIT;

  int counter = 0;

  float massMin = 1000;
  float massMax = 0;

  while (inputList >> fileName) {

    //    std::cout << fileName << std::endl;

    TFile * file = new TFile(fileName);

    cout<<" now working for "<<fileName<<endl;
    TTree * tree = file->Get("limit");

    //    std::cout << "file : " << file << std::endl;
    //    std::cout << "tree : " << tree << std::endl;

    tree->SetBranchAddress("limit",&LIMIT);
    tree->SetBranchAddress("mh",&MH);

    tree->GetEntry(0);

    if (MH<massMin) massMin = MH;
    if (MH>massMax) massMax = MH;

    mA[counter] = float(MH);
    minus2R[counter] = float(LIMIT);

    //    std::cout << mA[counter] << std::endl;
    
    tree->GetEntry(1);
    minus1R[counter] = float(LIMIT);

    tree->GetEntry(2);
    medianR[counter] = float(LIMIT);

    tree->GetEntry(3);
    plus1R[counter] = float(LIMIT);

    tree->GetEntry(4);
    plus2R[counter] = float(LIMIT);

    tree->GetEntry(5);
    obsR[counter] = float(LIMIT);
    if (blindData)
      obsR[counter] = medianR[counter];

    counter++; 
      
  }


  std::cout << "m(LSP)  -2s   -1s   exp   +1s   +2s   obs " << std::endl; 
  //           "100  24.1  28.2  33.8  40.8  48.2  23.0


  for (int i=0; i<counter; ++i) {

    obs[i]    = obsR[i];
    minus2[i] = minus2R[i];
    minus1[i] = minus1R[i];
    median[i] = medianR[i];
    plus1[i]  = plus1R[i];
    plus2[i]  = plus2R[i];

    char strOut[200];
    sprintf(strOut,"%3i  %5.2f  %5.2f  %5.2f  %5.2f  %5.2f  %5.2f",
	    int(mA[i]),minus2[i],minus1[i],median[i],plus1[i],plus2[i],obs[i]);
    std::cout << strOut << std::endl;

  }

  double zeros[nPoints];
  double upper[nPoints];
  double lower[nPoints];
  double central[nPoints];
  for (int i=0; i<counter; ++i) {
    zeros[i] = 0;
    central[i] = 15; 
    minus2[i] = median[i] - minus2[i];
    minus1[i] = median[i] - minus1[i];
    plus1[i]  = plus1[i]  - median[i];
    plus2[i]  = plus2[i]  - median[i];
    upper[i] = 15 - central[i];
    lower[i] = central[i] - obs[i];
  }
  
  
  int nPointsX = counter;

  TGraph * obsG = new TGraph(nPointsX, mA, obs);
  obsG->SetLineWidth(3);
  obsG->SetLineColor(1);
  obsG->SetLineWidth(2);
  obsG->SetMarkerColor(1);
  obsG->SetMarkerStyle(20);
  obsG->SetMarkerSize(1.4);

  TGraph * expG = new TGraph(nPointsX, mA, median);
  expG->SetLineWidth(3);
  expG->SetLineColor(2);
  expG->SetLineStyle(2);
  
  TGraphAsymmErrors * observed = new TGraphAsymmErrors(nPointsX, mA, central, zeros, zeros, lower, upper);
  observed->SetFillColor(kCyan-4);
  observed->SetLineWidth(3);

  TGraphAsymmErrors * innerBand = new TGraphAsymmErrors(nPointsX, mA, median, zeros, zeros, minus1, plus1);
  innerBand->SetFillColor(kGreen);
  innerBand->SetLineColor(kGreen);

  TGraphAsymmErrors * outerBand = new TGraphAsymmErrors(nPointsX, mA, median, zeros, zeros, minus2, plus2);
  outerBand->SetFillColor(kYellow);
  outerBand->SetLineColor(kYellow);

  TH2F * frame = NULL;

  if (xMax>0) massMax = xMax;

  //  frame = new TH2F("frame","",2,100,500,2,0,70);
  frame = new TH2F("frame","",2,massMin,massMax,2,0,yMax);
  frame->GetXaxis()->SetTitle(massPart);
  frame->GetYaxis()->SetTitle("95% C.L. limit on #sigma/#sigma^{theo}");
  frame->GetXaxis()->SetNdivisions(505);
  frame->GetYaxis()->SetNdivisions(206);
  frame->GetYaxis()->SetTitleOffset(1.25);  
  frame->GetYaxis()->SetTitleSize(0.048);  
  

  TCanvas *canv = new TCanvas("canv", "histograms", 600, 600);

  frame->Draw();

  outerBand->Draw("3same");
  innerBand->Draw("3same");
  expG->Draw("lsame");
  if (!blindData)
    obsG->Draw("lpsame");

  float xLeg = 0.18;
  float yLeg = 0.83;
  float xLegend = 0.57;
  float yLegend = 0.41;
  float sizeLeg = 0.27;

  TLegend * leg = new TLegend(0.17,0.58,0.50,0.80);
  leg->SetFillColor(0);
  leg->SetTextSize(0.035);
  leg->SetBorderSize(0);
  if (!blindData) 
    leg->AddEntry(obsG,"Observed","lp");
  leg->AddEntry(expG,"Expected","l");
  leg->AddEntry(innerBand,"#pm1#sigma Expected","f");
  leg->AddEntry(outerBand,"#pm2#sigma Expected","f");
  leg->Draw();
  TLine * line = new TLine(massMin,1,massMax,1);
  line->SetLineWidth(2);
  line->SetLineStyle(2);
  line->Draw();
  TString legLSP = "m(LSP) = " + massLSP + " GeV";
  TLatex * lsp = new TLatex(0.20,0.52,legLSP);
  lsp->SetNDC();
  lsp->SetTextSize(0.034);
  lsp->Draw();

  TPad * pad = canv->GetPad(0);
  writeExtraText = true;
  lumi_13TeV = Lumi;
  extraText = "Simulation";
  CMS_lumi(pad,4,11); 
  pad->RedrawAxis();

  leg->Draw();
  canv->Update();
  TString suffix(fileList);
  canv->Print(suffix+".pdf","Portrait pdf");
  canv->Print(suffix+".png");

}
