#include "HttStylesNew.cc"
#include "HtoH.h"
#include <iostream>
#include <string> 
#include <fstream>
#include <sstream> 

void CutFlowTableWork4()

{
	TString channel = "muel";
	//float QCD[]= {0,0,11210,11210,11210,11520,11650,10890,10890,10890,8047,3472,975.6,139.2,14.57,1.836,0.8592,0.0904,0,0,0,0,0,0,};//mutau
	//float QCD[]= {0,0,0,8628,8628,8628,8632,8745,8745,8747,8747,6149,6149,1679,435.3,28.66,9.391,9.391,3.483,0,0,0,0,0,0,};//eltau
	

	cout.setf(ios::fixed, ios::floatfield);
	cout.setf(ios::showpoint);
	string name;
	TString name2;
	TString name3;
	TString nameCutFlowUnWH;
	TString namexsecH;
	TString nameinputEventsH;
	int CutNumb;	
	TH1D *hist[50];
	float MClumi[50];	
	int i = 0;

	ifstream datasets;
	//datasets.open("datasets"+channel+"2_ext");
	datasets.open("datasets"+channel+"80_3");

	string SE ="SingleElectron";
	string SM ="SingleMuon";
	string MuonEG ="MuonEG";
	string QCDs ="QCD";
	float xsec;
	float SumOfWeights;	
	///float Lumi = 2320;
	float Lumi = 2040;
	float TTscale = 0.955;
	float Wjets = 0.945;

	
   	 while(getline(datasets, name))
		{
       		cout << i << endl;
       		cout << name << endl; 
		name2 = "/afs/desy.de/user/b/bobovnii/StauResults/plots_"+channel+"/"+name+"_B.root";
		name3 = name;
    		cout << name2 << endl;
		TFile * name3 = new TFile(name2);
		name3->cd(channel);

		nameCutFlowUnWH = "C_" + name;
		
		TH1D * NCutFlowUnWH = (TH1D*)name3->Get(channel+"/CutFlowUnW");

		string HHname = name;	
		if ((std::string::npos != HHname.find(SE)) || (std::string::npos != HHname.find(SM)) || (std::string::npos != HHname.find(MuonEG))/*|| (std::string::npos != HHname.find(QCDs))*/)
		{cout << "DATA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << endl;}
		else
		{
		TH1D * xsecH = (TH1D*)name3->Get(channel+"/xsec");
		TH1D * histWeightsH = (TH1D*)name3->Get(channel+"/histWeightsH");
		xsec = xsecH->GetMean();
		SumOfWeights = histWeightsH->GetSumOfWeights();
		cout << "xsec " << xsec<< endl;
		cout << "old Nevent = " << NCutFlowUnWH ->GetEntries() << endl;
		cout << "xsec*Lumi = " << xsec*Lumi << endl;
		cout << "SumOfWeights = " << SumOfWeights << endl;
		cout << "BinContent(1) = " << NCutFlowUnWH ->GetBinContent(1) << endl;
		
		NCutFlowUnWH -> Scale(xsec*Lumi/SumOfWeights);
		MClumi[i] = SumOfWeights/xsec;
		}
		//cout << "new Nevent = " << NCutFlowUnWH ->GetEntries() << endl;
		//cout << "BinContent(1) = " << NCutFlowUnWH ->GetBinContent(1) << endl;
		NCutFlowUnWH -> SetName(nameCutFlowUnWH);
		CutNumb = NCutFlowUnWH -> GetNbinsX();
		hist[i]= NCutFlowUnWH;
		i++;
    		}


	
    	datasets.close();

	
	// datasets depends code:
	cout << hist[1]->GetXaxis()->GetBinLowEdge(0) <<"   " <<  hist[1]->GetXaxis()->GetBinUpEdge(21) <<"   "<<  hist[1]->GetXaxis()->GetLast()  <<"   "<< endl;


	
	
	TH1D *TTJets = (TH1D*)hist[1]->Clone();
	TTJets -> Scale(0);	


	TH1D *WJets = (TH1D*)TTJets->Clone();
	TH1D *DYJets = (TH1D*)TTJets->Clone();
	///TH1D *QCD = TTJets;//don't know what to use
	TH1D *SingleT = (TH1D*)TTJets->Clone();
	TH1D *VVJets = (TH1D*)TTJets->Clone();//also
	TH1D *TTX = (TH1D*)TTJets->Clone();
	TH1D *VV = (TH1D*)TTJets->Clone();
	TH1D *Bkg = (TH1D*)TTJets->Clone();
	TH1D *Data = (TH1D*)TTJets->Clone();
	TH1D *C1N2 = (TH1D*)TTJets->Clone();
	TH1D *stau = (TH1D*)TTJets->Clone();
	TH1D *C1C1 = (TH1D*)TTJets->Clone();


	name2 = "/afs/desy.de/user/b/bobovnii/StauResults/plots_"+channel+"/QCD_DataDriven_B.root";
	TFile *QCDF = new TFile(name2);
	QCDF->cd(channel);
	TH1D *QCD = (TH1D*)QCDF->Get(channel+"/CutFlowUnW;1");


	float TTJetsL = 0;	
	float WJetsL = 0;
	float DYJetsL = 0;
	///TH1D *QCD = TTJets;//don't know what to use
	float SingleTL = 0;
	float VVJetsL= 0;//also
	float TTXL = 0;
	float VVL = 0;

	
	string TTS1 = "TT_Tune";
	string TTS2 = "TTJets";
	string SingleTS = "ST";
	string WJetsS = "WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8";
	string DYJetsS1 = "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8";
	string DYJetsS2 = "DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8";
	string DataS1 = "SingleElectron";
	string DataS2 = "SingleMuon";
	string DataS3 = "MuonEG";
	string VVJetsS = "WJetsToLNu";
	string VV1 = "ZZ";
	string VV2 = "WW";
	string VV3 = "WZT";
	string VV4 = "WG";
	string VV5 = "VV";
	string TTXS1 = "tGJets";
	string TTXS2 = "TTGJets";
	string TTXS3 = "ttWJets";
	string TTXS4 = "ttZJets";
	string TTXS5 = "tZq";
	string C1N2S = "C1N2";
	string stauS = "stau";
	string C1C1S = "C1C1";
	string QCDS = "QCD";

	
	for (int j=0;j<(i);j++)
		{
		string Hname = hist[j]->GetName();
		if (std::string::npos != Hname.find(TTS1))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;
			 TTJets -> Add(hist[j]); TTJetsL+=MClumi[j];}
		if (std::string::npos != Hname.find(TTS2))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;
			 TTJets -> Add(hist[j]); TTJetsL+=MClumi[j];}

		if (std::string::npos != Hname.find(WJetsS))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;
			WJets -> Add(hist[j]); WJetsL+=MClumi[j];}

		if (std::string::npos != Hname.find(DYJetsS1))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;DYJets-> Add(hist[j]);DYJetsL+=MClumi[j];}
		if (std::string::npos != Hname.find(DYJetsS2))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;DYJets-> Add(hist[j]);DYJetsL+=MClumi[j];}

		if (std::string::npos != Hname.find(SingleTS))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;SingleT -> Add(hist[j]);SingleTL+=MClumi[j];}
		if (std::string::npos != Hname.find(DataS1))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;Data -> Add(hist[j]);}
		if (std::string::npos != Hname.find(DataS2))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;Data -> Add(hist[j]);}
		if (std::string::npos != Hname.find(DataS3))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;Data -> Add(hist[j]);}
	//	if (std::string::npos != Hname.find(VVJetsS))
	//		{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;VVJets -> Add(hist[j]);WJetsL+=MClumi[j];}

		if (std::string::npos != Hname.find(VV1))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;VV -> Add(hist[j]);VVL+=MClumi[j];}	
		if (std::string::npos != Hname.find(VV2))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;VV -> Add(hist[j]);VVL+=MClumi[j];}	
		if (std::string::npos != Hname.find(VV3))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;VV -> Add(hist[j]);VVL+=MClumi[j];}
		if (std::string::npos != Hname.find(VV4))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;VV -> Add(hist[j]);VVL+=MClumi[j];}
		if (std::string::npos != Hname.find(VV5))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;VV -> Add(hist[j]);VVL+=MClumi[j];}


		if (std::string::npos != Hname.find(TTXS1))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;TTX -> Add(hist[j]);TTXL+=MClumi[j];}
		if (std::string::npos != Hname.find(TTXS2))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;TTX -> Add(hist[j]);TTXL+=MClumi[j];}
		if (std::string::npos != Hname.find(TTXS3))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;TTX -> Add(hist[j]);TTXL+=MClumi[j];}
		if (std::string::npos != Hname.find(TTXS4))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;TTX -> Add(hist[j]);TTXL+=MClumi[j];}
		if (std::string::npos != Hname.find(TTXS5))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;TTX -> Add(hist[j]);TTXL+=MClumi[j];}


	if (std::string::npos != Hname.find(C1N2S))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;C1N2 -> Add(hist[j]);}

	if (std::string::npos != Hname.find(C1C1S))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;C1C1 -> Add(hist[j]);}

	if (std::string::npos != Hname.find(stauS))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;stau -> Add(hist[j]);}


/*	if (std::string::npos != Hname.find(QCDS))
			{cout <<" outside loop "<<hist[j]->GetName()<<" "<<hist[j]->GetMean()<<" "<<endl;QCD -> Add(hist[j]);}
*/		}



///just table of Lequiv
/*	for (int jj=0;jj<(i);jj++)
		{string Hname = hist[jj]->GetName();
		cout << "Sample = "<< Hname << "  Lequiv="<< MClumi[jj]/Lumi<<endl;
		}

*/
//	TTJets -> Scale(TTscale);
//	WJets -> Scale(Wjets);
	
	Bkg -> Add(TTJets);
	Bkg -> Add(WJets);
	Bkg -> Add(VVJets);
	Bkg -> Add(SingleT);
	Bkg -> Add(TTX);
	Bkg -> Add(DYJets);
	Bkg -> Add(VV);
	Bkg -> Add(QCD);

	TString DataCell;
	TString DataVSmc;
	cout << "N"<<"\r\t| "<< "   Cut"<< 
	"\r\t\t\t| "<< " TTJets"  << 
	"\r\t\t\t\t\t| " << " WJets" << 
	"\r\t\t\t\t\t\t\t| " <<  " DYJets"  << 
	"\r\t\t\t\t\t\t\t\t\t| "  << " SingleT" << 
	//"\r\t\t\t\t\t\t\t\t\t\t\t| " << "VVJets"  << 
	"\r\t\t\t\t\t\t\t\t\t\t\t| " << "TTX"  << 
	"\r\t\t\t\t\t\t\t\t\t\t\t\t\t| " << "VV"  << 
	"\r\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t| " << "QCD"  << 
	"\r\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t| " << "Bkg"  << 
	"\r\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t| " << "Data"  << 
	endl;
	for (int iCut = 0; iCut < CutNumb-2; iCut++)

		{if (iCut+1 < 7.5) {	std::stringstream stm;
 					stm << Data->GetBinContent(iCut+1);
					DataCell = stm.str();} else {DataCell="O_o";}
		cout << iCut+1<<"\r\t| "<<    hist[1]->GetXaxis()->GetBinLabel(iCut+1)<< 
		"\r\t\t\t| "<< TTJets->GetBinContent(iCut+1)  << 
		"\r\t\t\t\t\t| " << WJets->GetBinContent(iCut+1) << 
		"\r\t\t\t\t\t\t\t| " <<  DYJets->GetBinContent(iCut+1)  << 
		"\r\t\t\t\t\t\t\t\t\t| "  << SingleT->GetBinContent(iCut+1) << 
		//"\r\t\t\t\t\t\t\t\t\t\t\t| " <<   VVJets->GetBinContent(iCut+1)<< 
		"\r\t\t\t\t\t\t\t\t\t\t\t| " <<   TTX->GetBinContent(iCut+1)<< 
		"\r\t\t\t\t\t\t\t\t\t\t\t\t\t| " <<   VV->GetBinContent(iCut+1)<< 
		"\r\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t| " <<   QCD->GetBinContent(iCut+1)<<  
		"\r\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t| " <<   Bkg->GetBinContent(iCut+1)<< 
		"\r\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t| " <<   DataCell << 
		endl;
			

		}  	


////  Table for LaTex/////////////////////////////////////////////////////////////////////////////////

cout << "\\begin{table}[h] "<<endl;
cout << "\\begin{center}"<<endl;
cout << "\\begin{tabular}{|l|l|l|l|l|}"<<endl;
cout << "\\hline"<<endl;

cout << "N"<< "&   Cut"<< 
	" & "<< " TTJets"  << 
	" & " << " WJets" << 
	" & " <<  " DYJets"  << 
	" & "  << " SingleT" << 
//	" & " << "VVJets"  << 
	" & " << "TTX"  << 
	" & " << "VV"  << 
	" & " << "QCD"  << 
	" & " << "Bkg"  << 
	" & " << "Data"  << 
	" & " << "(Data-Bkg)/Data"  << 
	//" & " << "C1C1"  << 
	//" & " << "C1N2"  << 
///	" & " << "stau"  << 
	"\\\\" <<
	endl;
	for (int iCut = 2; iCut < CutNumb-2; iCut++)

		{if (iCut+1 < 7.5) {	std::stringstream stm;
 					stm << Data->GetBinContent(iCut+1);
					DataCell = stm.str();} else {DataCell="Oo";}
		if (iCut+1 < 7.5) {	std::stringstream stm;
 					stm << (Data->GetBinContent(iCut+1) - (Bkg->GetBinContent(iCut+1)/*+QCD[iCut+1]*/))/Data->GetBinContent(iCut+1);
					DataVSmc = stm.str();} else {DataVSmc="Oo";}		
		cout << iCut+1<<"& "<<    hist[1]->GetXaxis()->GetBinLabel(iCut+1)<< 
		" & "<<setprecision(2)<< TTJets->GetBinContent(iCut+1)  << 
		" & " <<setprecision(2)<< WJets->GetBinContent(iCut+1) << 
		" & " <<setprecision(2)<<  DYJets->GetBinContent(iCut+1)  << 
		" & "  <<setprecision(2)<< SingleT->GetBinContent(iCut+1) << 
//		" & " << setprecision(2)<<  VVJets->GetBinContent(iCut+1)<< 
		" & " << setprecision(2)<<  TTX->GetBinContent(iCut+1)<< 
		" & " << setprecision(2)<<  VV->GetBinContent(iCut+1)<< 
		" & " << setprecision(2)<<  QCD->GetBinContent(iCut+1)<< 
		" & " << setprecision(2)<<  Bkg->GetBinContent(iCut+1)/*+QCD[iCut+1]*/<< 
		" & " <<  setprecision(2)<< DataCell<< 
		" & " << setprecision(2)<<  DataVSmc <<
		//" & " <<  setprecision(2)<< C1C1->GetBinContent(iCut+1)<< 
		//" & " <<  setprecision(2)<< C1N2->GetBinContent(iCut+1)<< 
//		" & " <<  setprecision(2)<< stau->GetBinContent(iCut+1)<< 
	"\\\\" <<
		endl;
		}
/*
	cout << " "<< "& L_equiv"<< 
	" & "<<  TTJetsL  << 
	" & " <<  WJetsL << 
	" & " <<   DYJetsL  << 
	" & "  <<  SingleTL << 
//	" & " << VVJetsL  << 
	" & " << TTXL  << 
	" & " << VVL  << 
	" & " << "  "  << 
//	" & " << "Data"  << 
//	" & " << "(Data-Bkg)/Data"  << 
	"\\\\" <<
	endl;		
*/
		  	
cout << "\\hline  "<<endl;
cout << "\\end{tabular} "<<endl;
cout << "\\end{center} "<<endl;
cout << "\\caption{Scale factor, uncertainty and purity for different combination's of topological cuts } "<<endl;
cout << "\\label{TTbart} "<<endl;
cout << "\\end{table} "<<endl;



}


