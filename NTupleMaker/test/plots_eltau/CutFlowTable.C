#include <iostream>
#include <string> 
#include <fstream> 

using namespace std;
void CutFlowTable()

{
		
	string name;
	TString name2;
//	TString name3;
	TString nameCutFlowUnWH;
	TString namexsecH;
	TString nameinputEventsH;
	int CutNumb;	
	TH1D *hist[50];	
	int i = 0;

	ifstream datasets;
	datasets.open("datasets");


	float xsec;
	float SumOfWeights;	
	float Lumi = 2301;

	
		TString n;
  	 while(getline(datasets, name))
		{
      		cout << i << endl; 
      		cout << name << endl; 
		name2 = name;
//		name3 = name;
	//	cout <<"name3  " << name3 << endl;
   		cout << name2 << endl;
		TFile * name3 = new TFile(name2);
		name3->cd("mutau");
	//	cout <<"name3  " << name3 << endl;

		nameCutFlowUnWH = "CutFlowUnWH_";
      		n.Form("CutFlowUnWH_%s",name.c_str());

//		nameCutFlowUnWH = name;
//		namexsecH = "xsecH" + name;
//		nameinputEventsH = "inputEventsH" + name;
		
		TH1D * NCutFlowUnWH = (TH1D*)name3->Get("mutau/CutFlowUnW");
		TH1D * xsecH = (TH1D*)name3->Get("mutau/xsec");
		TH1D * inputEventsH = (TH1D*)name3->Get("mutau/CutFlowUnW");


		 xsec = xsecH->GetMean();
		SumOfWeights = inputEventsH->GetSumOfWeights();
		
//		cout << "xsec " << xsec<< endl;
//		cout << "SumOfWeights " << SumOfWeights<< endl;
		NCutFlowUnWH -> Scale(xsec*Lumi/SumOfWeights);
		CutNumb = NCutFlowUnWH -> GetNbinsX();
		

	//	NCutFlowUnWH -> SetName(nameCutFlowUnWH);
		hist[i]= NCutFlowUnWH;
		
		hist[i]  = (TH1D*) NCutFlowUnWH->Clone();
		//hist[i]->SetName(nameCutFlowUnWH);
		cout<<"  test before "<<hist[i]->GetName()<<endl;
		hist[i]->SetName(n);
		cout<<"  test "<<n<<endl;
		i++;


		
   		}


	
   	datasets.close();
	
	string nn = "TT";
	
	
for (int j=0;j<25;j++) 
{
 string Hname = hist[j]->GetName();
  if (std::string::npos != Hname.find(nn))
cout<<"  outside loop "<<hist[j]->GetName()<<"  "<<hist[j]->GetMean()<<"  "<<endl;

}
	cout << "something1 " << hist[25]->GetName()  <<endl;
	cout << "something2 " << xsecH->GetMean() << endl;


	//cout << "something " << hist[25]->GetMean()  << endl;
	cout << "something " << hist[21]->GetName()  << endl;
	
}

