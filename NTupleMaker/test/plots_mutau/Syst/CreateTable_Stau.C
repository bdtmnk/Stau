#include <math.h>
#include <iostream>
void CreateTable_Stau(
TString FILE = "Var_BDTmutau_stau100_LSP1My_16_35invfb_mt_Syst.root",
TString VARIABLE = "_BDTmutau_stau100_LSP1My_16"
) 
{





  //TFile * file = new TFile("FILE");
  TFile *file = TFile::Open (FILE, "read");
  //TFile *fileout = TFile::Open ("FILEOUT.root", "update");
  //file->cd("CHANNEL");
  

  TH1D * data_obs = (TH1D*)file->Get("data_obs"+VARIABLE);
//  TH1D * data_obs = (TH1D*)file->Get("allbkg"+VARIABLE);

  data_obs->SetName("data_obs");


  TH1D * tt = (TH1D*)file->Get("tt"+VARIABLE);
  TH1D * wj = (TH1D*)file->Get("wj"+VARIABLE);
  TH1D * dyj = (TH1D*)file->Get("dyj"+VARIABLE);
  TH1D * ztt = (TH1D*)file->Get("ztt"+VARIABLE);
  TH1D * dib = (TH1D*)file->Get("dib"+VARIABLE);
  TH1D * ww = (TH1D*)file->Get("ww"+VARIABLE);
  TH1D * ttx = (TH1D*)file->Get("ttx"+VARIABLE);
  TH1D * sT = (TH1D*)file->Get("sT"+VARIABLE);
  TH1D * fakes = (TH1D*)file->Get("fakes"+VARIABLE);
  TH1D * rest = (TH1D*)file->Get("rest"+VARIABLE);

TH1D * signal1 = (TH1D*)file->Get("stau-stau_left_90_LSP1_B"+VARIABLE);
TH1D * signal2 = (TH1D*)file->Get("stau-stau_left_100_LSP1_B"+VARIABLE);
TH1D * signal3 = (TH1D*)file->Get("stau-stau_left_200_LSP1_B"+VARIABLE);

cout << "AAA"<< endl;



  TH1D * allbkg = (TH1D*)tt->Clone("total_background");
/*
  TH1D * tt_shape = (TH1D*)tt->Clone("tt_shape");
  TH1D * wj_shape = (TH1D*)wj->Clone("wj_shape");
  TH1D * dyj_shape = (TH1D*)dyj->Clone("dyj_shape");
  TH1D * ztt_shape = (TH1D*)ztt->Clone("ztt_shape");
  TH1D * dib_shape = (TH1D*)dib->Clone("dib_shape");
  TH1D * ww_shape = (TH1D*)ww->Clone("ww_shape");
  TH1D * ttx_shape = (TH1D*)ttx->Clone("ttx_shape");
  TH1D * sT_shape = (TH1D*)sT->Clone("sT_shape");
  TH1D * fakes_shape = (TH1D*)fakes->Clone("fakes_shape");
  TH1D * rest_shape = (TH1D*)rest->Clone("rest_shape");

  TH1D * tt_norm = (TH1D*)tt->Clone("tt_norm");
  TH1D * wj_norm = (TH1D*)wj->Clone("wj_norm");
  TH1D * dyj_norm = (TH1D*)dyj->Clone("dyj_norm");
  TH1D * ztt_norm = (TH1D*)ztt->Clone("ztt_norm");
  TH1D * dib_norm = (TH1D*)dib->Clone("dib_norm");
  TH1D * ww_norm = (TH1D*)ww->Clone("ww_norm");
  TH1D * ttx_norm = (TH1D*)ttx->Clone("ttx_norm");
  TH1D * sT_norm = (TH1D*)sT->Clone("sT_norm");
  TH1D * fakes_norm = (TH1D*)fakes->Clone("fakes_norm");
  TH1D * rest_norm = (TH1D*)rest->Clone("rest_norm");

  float tt_error[60][40]={0.};
  float wj_error[60][40]={0.};
  float dyj_error[60][40]={0.};
  float ztt_error[60][40]={0.};
  float dib_error[60][40]={0.};
  float ww_error[60][40]={0.};
  float ttx_error[60][40]={0.};
  float sT_error[60][40]={0.};
  float fakes_error[60][40]={0.};
  float rest_error[60][40]={0.};
  float signal_error[60]={0.};

  float tt_errorStat[60]={0.};
  float wj_errorStat[60]={0.};
  float dyj_errorStat[60]={0.};
  float ztt_errorStat[60]={0.};
  float dib_errorStat[60]={0.};
  float ww_errorStat[60]={0.};
  float ttx_errorStat[60]={0.};
  float sT_errorStat[60]={0.};
  float fakes_errorStat[60]={0.};
  float rest_errorStat[60]={0.};
  float signal_errorStat[60]={0.};

*/
cout << "AAA"<< endl;

  allbkg->Add(wj);
  allbkg->Add(dyj);
  allbkg->Add(ztt);
  allbkg->Add(dib);
  allbkg->Add(ww);
  allbkg->Add(ttx);
  allbkg->Add(sT);
  allbkg->Add(fakes);
cout << "AAA"<< endl;



//cout<<" ========================= "<<metU<<"  "<<metD<<"   "<<btagU<<"  "<<btagD<<"  "<<fabs(Syst_SofWUp-Nom_SofW)<<"  "<<fabs(Syst_SofWDown-Nom_SofW)<<"  "<<Syst_SofWUp<<"  "<<Syst_SofWDown<<"  "<<Nom_SofW<<endl;


  //std::ofstream textFile("table.txt");

cout << "\\begin{table}[h] "<<endl;
cout << "\\begin{center}"<<endl;
cout << "\resizebox{1.\textwidth}{!}"<<endl;
cout << "\\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|l|}"<<endl;
cout << "\\hline"<<endl;

int FirstBin = 23;
int LastBin = fakes->GetNbinsX();

cout << "BDT"<< 
	" & "<< " TTJets"  << 
	" & " << " rest" << 
	" & " <<  " DYJets"  << 
	" & " << "WW"  << 
	" & " << "sT"  << 
	" & " << "fakes"  << 
	" & " << "Bkg"  << 
	" & " << "Stau (90,1)"  << 
	" & " << "Stau (100,1)"  << 	
	" & " << "Stau (200,1)"  << 	
//	" & " << "Data"  << 
//	" & " << "(Data-Bkg)/Data"  << 
	"\\\\" <<
	endl;


for (int iCut = FirstBin+1; iCut < LastBin+1; iCut++)
	{
		cout << setprecision(3) << fixed<< "BDT("<< allbkg->GetXaxis()->GetBinLowEdge(iCut)<<","<<allbkg->GetXaxis()->GetBinUpEdge(iCut) <<")"<<
		" & "<<setprecision(2)<< tt->GetBinContent(iCut)  << 
		" & " <<setprecision(2)<< rest->GetBinContent(iCut) << 
		" & "  <<setprecision(2)<< ztt->GetBinContent(iCut)+dyj->GetBinContent(iCut+1) << 
		" & " << setprecision(2)<<  ww->GetBinContent(iCut)<< 
		" & " << setprecision(2)<<  sT->GetBinContent(iCut)<< 
		" & " << setprecision(2)<<  fakes->GetBinContent(iCut)<< 
		" & " << setprecision(2)<<  allbkg->GetBinContent(iCut)<< 
		" & " <<  setprecision(2)<< signal1->GetBinContent(iCut)<< 
		" & " << setprecision(2)<<  signal2->GetBinContent(iCut) <<
		" & " << setprecision(2)<<  signal3->GetBinContent(iCut) <<

		//" & " <<  setprecision(2)<< C1C1->GetBinContent(iCut+1)<< 
		//" & " <<  setprecision(2)<< C1N2->GetBinContent(iCut+1)<< 
//		" & " <<  setprecision(2)<< stau->GetBinContent(iCut+1)<< 
	"\\\\" <<
		endl;
		}
		  	
cout << "\\hline  "<<endl;
cout << "\\end{tabular}} "<<endl;
cout << "\\end{center} "<<endl;
cout << "\\caption{Event yelds in SR for main backgrounds and signals for BDT training with the signal point (100,1)   } "<<endl;
cout << "\\label{yelds} "<<endl;
cout << "\\end{table} "<<endl;


/*
	   << signal1->Integral() << "  " 
	   << tt->Integral() << "  " 
	   << rest->Integral() << "  " 
	   << dyj->Integral() << "  " 
	   << ztt->Integral() << "  " 
	   << ww->Integral() << "  " 
	   << sT->Integral() << "  " 
	   << fakes->Integral() << std::endl; 

*/



}

 
