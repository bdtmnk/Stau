#include <cmath>
#include <sstream>
#include <iomanip>
#include "TChain.h"
#include "TH1.h"
#include "TTree.h"
#include "TKey.h"
#include "Riostream.h"
#include "TCanvas.h"
#include "TFile.h"
#include "TH2.h"
#include "TLegend.h"
#include "TROOT.h"
#include "TFrame.h"
#include "TGaxis.h"
#include "TStyle.h"
#include <vector>
#include <iostream>
#include <algorithm>
#include "TList.h"
#include <string>
#include "TObject.h"
#include "TBranch.h"
#include <functional>
#include "TAxis.h"
#include "TChain.h"
#include "TMath.h"
#include "Riostream.h"
#include <iostream>
#include <fstream>
#include "tdrstyle.C"
#include "CMS_lumi.C"


using namespace std;

void Impose( TDirectory *ttarget, TList *ssourcelist, string &np_legend , vector<string> titles_ );
void ModifyHist (TH1D* &h, int cl,vector <string> title);
void ModifyHist (TH1D* &h, int cl,vector <string> title, TLegend * & tleg);
void ModifyHist (TH1D* &h, int cl);

// void MergeRootfile( TDirectory *target, TList *sourcelist );


void OverlapMC()
{
       
    gROOT->SetStyle ("Plain");
    gStyle->SetPalette (1);
    gStyle->SetTextFont(22) ;
    gStyle->SetTitleFont(22,"xyz") ;
    gStyle->SetLabelFont(22,"xyz") ;
 //   setTDRStyle();
 

  writeExtraText = true;       // if extra text
  extraText  = "Preliminary";  // default extra text is "Preliminary"
  lumi_8TeV  = "19.1 fb^{-1}"; // default is "19.7 fb^{-1}"
  lumi_7TeV  = "4.9 fb^{-1}";  // default is "5.1 fb^{-1}"
  lumi_sqrtS = "13 TeV";       // used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

  int iPeriod = 3;    // 1=7TeV, 2=8TeV, 3=7+8TeV, 7=7+8+13TeV, 0=free form (uses lumi_sqrtS)

  // second parameter in example_plot is iPos, which drives the position of the CMS logo in the plot
  // iPos=11 : top-left, left-aligned
  // iPos=33 : top-right, right-aligned
  // iPos=22 : center, centered
  // mode generally : 
  //   iPos = 10*(alignement 1/2/3) + position (1/2/3 = left/center/right)

  //example_plot( iPeriod, 0 );   // out of frame (in exceptional cases)
  //  example_plot( iPeriod, 11 );  // left-aligned
  //  example_plot( iPeriod, 33 );  // right-aligned

  //  writeExtraText = false;       // remove Preliminary
  
  //  example_plot( iPeriod, 0 );   // out of frame (in exceptional cases)

  //  example_plot( iPeriod, 11 );  // default: left-aligned
  //  example_plot( iPeriod, 22 );  // centered
  //  example_plot( iPeriod, 33 );  // right-aligned  
  
 vector <string> titles;
    // void MergeRootfile( TDirectory *target, TList *sourcelist );
    //TTrees
    TList *FileList;
    TFile *Target;
    titles.clear();
    int np=1;
 
   Float_t value=0;
   ifstream ifs("mc");
   string line;
   while(std::getline(ifs, line)) // read one line from ifs
    {
    istringstream iss(line); // access line as a stream
    string dataname;
    iss >> dataname ; // no need to read further
    titles.push_back(dataname);
    }
    
    string fout = "mergedplotsTau.root";
    
    
    FileList = new TList ();
        
    
    for (unsigned int i=0; i <titles.size();++i){
        //string ext=".root";
        cout<<" loading dataset "<<titles[i]<<endl;
        //string file=titles[i]+".root";
        string file=titles[i];
        FileList->Add (TFile::Open (file.c_str()));
    }
    
        
    //return;
    Target = TFile::Open (fout.c_str (), "RECREATE");
    
    string np_title = titles[0];
    Impose (Target, FileList, np_title,titles);
    delete FileList;
    delete Target;
}


void
Impose (TDirectory * target, TList * sourcelist, string & np_title_, vector<string> titles)
{
    cout << "	" << "========================================================" << endl;
    cout << "	" << "This is a macro to superimpose plots of different root files." << endl;
    cout << "	" << "Only TH1Dobjects are superimposed." << endl;
    cout << "	" << "Target path: " << target->GetPath () << endl;
    TString path ((char *) strstr (target->GetPath (), ":"));
    path.Remove (0, 2);

   
    //float Lumi= 7.301;
    //float Lumi= 5000;
    float Lumi=2094;
    bool norm_=false;
    cout<<titles[0]<<"   "<<titles.size()<<endl;
    
    //not really useful if plots already weighted to lumi - usefull is plots are in a.u.
    vector <float > lumiweights;
    lumiweights.clear();
    
    
    TH1D* allbkg;
    TFile *first_source = (TFile *) sourcelist->First ();
    first_source->cd ("mutau");
    
    TH1D* eventCount = (TH1D*)first_source->Get("mutau/histWeightsH");
    //TH1D* eventCount = (TH1D*)first_source->Get("mutau/inputEventsH");
    TH1D* hxsec = (TH1D*)first_source->Get("mutau/xsec");
    float nGen = eventCount->GetSumOfWeights();
    //float nGen = eventCount->GetBinContent(1);
    float xsec = hxsec->GetMean();
    float norm = xsec*Lumi/nGen;
     
    norm =1;
    lumiweights.push_back(float(norm));
    
  
            //  cout<< " for first source "<<count<<" file, there where "<<nGen<<" events with xsec "<<xsec<<" weight "<<lumiweights[0]<<" weight "<<float(xsec*Lumi/nGen)<<"  norm "<<norm<<endl;

    TDirectory *current_sourcedir = gDirectory;
    //gain time, do not add the objects in the list in memory
    Bool_t status = TH1::AddDirectoryStatus ();
    TH1::AddDirectory (kFALSE);
    // loop over all keys in this directory
    TChain *globChain = 0;
    TIter nextkey (current_sourcedir->GetListOfKeys ());
    //TIter nextkey (((TDirectory *) current_sourcedir->Get ("ana"))->GetListOfKeys ());
    TKey *key, *oldkey = 0;
    int count=0;
    while ((key = (TKey *) nextkey ())) {
        count++;
        if (count>20) break;
        //keep only the highest cycle number for each key
//        if (oldkey && !strcmp (oldkey->GetName (), key->GetName ()))
//            continue;
        
        // read object from first source file and create a canvas
       // first_source->cd (path);
        first_source->cd ("mutau");
        TObject *obj = key->ReadObj ();
        
      //  if (obj->GetName () != "CutFlow" ) continue;
	//string nn = obj->GetName();
      // if (std::string::npos == nn.find("Cut")) continue;
        //cout<<obj->GetName()<<endl;
       
        
        TCanvas *c1 = new TCanvas ("c1",obj->GetName (),0,22,600,600);
        
        if (obj->IsA ()->InheritsFrom ("TH1D") ) {
            // descendant of TH1D-> prepare the histograms to be superimposed
            
            TH1D* hh[300];
           TH1D* h1 = (TH1D*) obj;
    	   TLegend *legend_c1 = new TLegend (0.65, 0.97, 0.95, 0.6);
    	   legend_c1->SetFillColor(1);
           legend_c1->SetFillStyle(0);
           legend_c1->SetLineColor(0);
           legend_c1->SetTextFont (132);
           legend_c1->SetTextSize (0.035);
                
           ModifyHist (h1,1,Lumi,lumiweights[0],titles[0],norm_);

            //if (! h1->Integral() >0 &&  obj->GetName()!="dPhi_1") continue;
            //if (! h1->Integral() >0 ) continue;
            
            // loop over all source files and modify the correspondant
            // histogram to the one pointed to by "h1"
            TFile *nextsource = (TFile *) sourcelist->After (first_source);
            
            int cl;
            h1->SetStats(000000);
            h1->SetLineWidth(5);
            cl=1;
            
            hh[cl]=h1;
            
            THStack *hs = new THStack(h1->GetName(),h1->GetTitle());
            
            
            // QCD DY WJets TTJets
            
            string n1,n2,n3,n4,fname,sn,sdata,st1,st2,st3,st4,st5,st6,wj,wj1,dy1,dy2,tt,qcd, st_t, st_s, st_tw_t, st_tw_a,qcd1,qcd2,qcd3,qcd4,qcd5,qcd6,qcd7,qcd8,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10;             


 	r1="WWTo2L2Nu" ;// 3 file, there xsec is 0 SuOfWeights 1.96013e+06 Lumi 1263.9 lumiweight 0 weight 0  norm 0 cl 2
 	r2="WWZ";//.root  3 file, there xsec is 0 SuOfWeights 41059.5 Lumi 1263.9 lumiweight 0 weight 0  norm 0 cl 3
 	r3="WZJets";//.root  3 file, there xsec is 0 SuOfWeights 1.0854e+08 Lumi 1263.9 lumiweight 0 weight 0  norm 0 cl 4
        r4="WZZ";//  3 file, there xsec is 0 SuOfWeights 13879.6 Lumi 1263.9 lumiweight 0 weight 0  norm 0 cl 5
 	r5="ZZTo2L2Q";//  3 file, there xsec is 0 SuOfWeights 9.5091e+07 Lumi 1263.9 lumiweight 0 weight 0  norm 0 cl 6
        r6="TTWJetsToLept" ;// 3 file, there xsec is 0.2043 SuOfWeights 85209.1 Lumi 1263.9 lumiweight 0.00303037 weight 0.00303037  norm 0.00303037 cl 7
        r7="TTWJetsToQQ" ;// 3 file, there xsec is 0 SuOfWeights 568023 Lumi 1263.9 lumiweight 0 weight 0  norm 0 cl 8
        r8="TTZToQQ"  ;//3 file, there xsec is 0 SuOfWeights 395631 Lumi 1263.9 lumiweight 0 weight 0  norm 0 cl 9
        r9="ZZTo2L2Nu"  ;//3 file, there xsec is 0 SuOfWeights 395631 Lumi 1263.9 lumiweight 0 weight 0  norm 0 cl 9

	/*WWToLNuQQ.root
	ZZTo2Q2Nu.root
	tZqToLL.root
	tZqToNuNu.root
	TTGJets.root
	*/


	    wj="WJetsToLNu";
	    wj1="wJetsToLNu";
            tt="TTJets";
            dy1="DYJetsToLL_M-50";
            dy2="DYJetsToLL_M-10to50";
            st_t="ST_t-channel_4f_leptonDecays";
            st_s="ST_s-channel_4f_leptonDecays";
            st_tw_t="ST_tW_top";
            st_tw_a="ST_tW_antitop_5f";
             n1="QCD";n2="DY";n3="WJ",n4="TT", sn="stau";sdata="Single";st1="DataDriven";st2="0.5";
            
            
		qcd1="QCD_HT100to200" ;//27540000
		qcd2="QCD_HT200to300" ;//1735000
		qcd3="QCD_HT300to500" ;//367000
		qcd4="QCD_HT500to700" ;//29400
		qcd5="QCD_HT700to1000" ;//6524

		qcd6="QCD_HT1000to1500" ;//1064
		qcd7="QCD_HT1500to2000" ;//121.5
		qcd8="QCD_HT2000toInf" ;//25.42
	        qcd="DataDriven";
            while (nextsource) {
                
                fname= nextsource->GetName();
                
                bool flagg= false;
              
  		//if (std::string::npos != fname.find(sn) || std::string::npos != fname.find(sdata)  || std::string::npos != fname.find(st1) || std::string::npos != fname.find(st2)   ) 	flagg=true;
  		if (std::string::npos != fname.find(sn) || std::string::npos != fname.find(sdata)  ||std::string::npos != fname.find(st1)   ) 	flagg=true;

             //   if (flagg) cout<<"=============================================================== "<<fname<<endl;
                // make sure we are at the correct directory level by cd'ing to path
                nextsource->cd("mutau");
                
                TH1D* eventCountt = (TH1D*)nextsource->Get("mutau/histWeightsH");
    		TH1D* hxsecc = (TH1D*)nextsource->Get("mutau/xsec");
                //float nGenn = eventCountt->GetSum();
    		float xsecc = hxsecc->GetMean();
    		if (std::string::npos != fname.find(wj)) xsecc = 61526.7;	
    		if (std::string::npos != fname.find(wj1)) xsecc = 61526.7;	
    		if (std::string::npos != fname.find(dy1)) xsecc = 6025.2;	
    		if (std::string::npos != fname.find(dy2)) xsecc = 18610;	
    		if (std::string::npos != fname.find(tt)) xsecc = 831.76;	
    		if (std::string::npos != fname.find(st_t)) xsecc = 70.69;	
    		if (std::string::npos != fname.find(st_s)) xsecc = float(10.32*0.328);	 
    		if (std::string::npos != fname.find(st_tw_t)) xsecc = float(35.85*0.328);	
    		if (std::string::npos != fname.find(st_tw_a)) xsecc = float(35.85*0.328);

    		if (std::string::npos != fname.find(qcd1)) xsecc = 27850000;
    		if (std::string::npos != fname.find(qcd2)) xsecc = 1717000;	
    		if (std::string::npos != fname.find(qcd3)) xsecc = 351300;	
    		if (std::string::npos != fname.find(qcd4)) xsecc = 31630;
    		if (std::string::npos != fname.find(qcd5)) xsecc = 6802;	
    		if (std::string::npos != fname.find(qcd6)) xsecc = 1206;	
    		if (std::string::npos != fname.find(qcd7)) xsecc = 120.4;	
    		if (std::string::npos != fname.find(qcd8)) xsecc = 25.25;	
		if (std::string::npos != fname.find(r1)) xsecc = 12.178;	
		if (std::string::npos != fname.find(r2)) xsecc = 0.1651;	
		if (std::string::npos != fname.find(r3)) xsecc = 5.26;	
		if (std::string::npos != fname.find(r4)) xsecc = 0.05565;	
		if (std::string::npos != fname.find(r5)) xsecc = 3.22;	
		if (std::string::npos != fname.find(r6)) xsecc = 0.2043;	
		if (std::string::npos != fname.find(r7)) xsecc = 0.4062;	
		if (std::string::npos != fname.find(r8)) xsecc = 0.5297;	
		if (std::string::npos != fname.find(r9)) xsecc = 0.564;	

		//if (std::string::npos != fname.find(qcd)) xsecc = 302672;	
		//if (std::string::npos != fname.find(qcd)) xsecc = 1;	
        
                float nGenn = eventCountt->GetSumOfWeights();
                float normm = xsecc*Lumi /nGenn  ;

		//if (std::string::npos != fname.find(qcd)) {xsecc=1.;normm=1.;}
		if (std::string::npos != fname.find(sdata)) {xsecc=1.;normm=1.;}
		if (flagg) normm=1.;
                lumiweights.push_back(normm);
                
                
                TKey *key2 = (TKey *) gDirectory->GetListOfKeys ()->FindObject (h1->GetName ());
                
                if (key2) {
                    cl++;
                    
                    TH1D *h2;
                    
                    h2 = (TH1D*) key2->ReadObj ();
                    h2->SetLineWidth(4);
                    ModifyHist (h2, cl,Lumi,lumiweights[cl-1],titles[cl-1],norm_);
                    h2->SetStats(0);
                    hh[cl] = h2;
		 
		     if (cl==2){	
                         allbkg  = (TH1D*) h2->Clone();
            		//allbkg->Add(hh[2],-1);
            		 allbkg->Reset();
			
			}
                   
               cout<< " for "<<fname<<"  "<<count<<" file, there xsec is "<<xsecc<<" SuOfWeights "<<nGenn<<" Lumi "<<Lumi<<" lumiweight "<<lumiweights[cl-1]<<" weight "<<float(xsecc*Lumi/nGenn)<<"  norm "<<normm<<" cl "<<cl<<endl; 	 	

     		if (!flagg)     
               {
                        //cout<<" will add histogram "<<h2->GetName()<< " for "<<titles[cl-1]<<"  "<<fname<<"  cl  "<<cl<<endl;
                       hs->Add(h2);
                       allbkg->Add(h2);
                    }
                    
                }
                
                nextsource = (TFile *) sourcelist->After (nextsource);
            }				// while ( nextsource )
        }
        
        // now draw and write the superimposed histograms to the target file
        // note that this will just store the canvas c1->in the current directory level,
        // which is not persistent until the complete directory itself is stored
        // by "target->Write()" below
            
        if (obj) {
            target->cd ();
            //legend_c1->SetNColumns(3);
            
            //TPad *pad1 = new TPad("pad1","pad1",0,0.25,0.5,1);
            TPad *pad1 = new TPad("pad1","pad1",0,0.0,1,1);
            TPad *pad1r = new TPad("pad1","pad1",0.5,0.25,1,1);
            //TPad *pad2 = new TPad("pad2","pad2",0.5,0.11,1,1);
            
            TPad *pad2 = new TPad("pad2","pad2",0,0,1,0.249);
            
            
            pad1->SetBottomMargin(0.07);
            pad1->SetRightMargin(0.05);
            pad1->SetGridy();
            pad1r->SetBottomMargin(0.07);
            pad1r->SetRightMargin(0.05);
            pad1r->SetGridy();
            
            pad2->SetBottomMargin(0.05);
            
            
	    pad2->SetTopMargin(0);
	    pad2->SetBottomMargin(0.25);
            pad2->SetRightMargin(0.05);


            //hs->Draw("nostack");
            c1->cd();
            

            c1->Clear();
            
            pad1->SetLogy();
            pad1->Draw();
            //pad1r->Draw();
            //pad2->Draw();
            
	    pad2->SetGridy(1);
            
            pad1->cd();
            pad1->Clear();
            
            
            
            TH1D *hsum = ((TH1D*)(hs->GetStack()->Last())); // the "SUM"
            //hsum->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(0));
            
            char namee[100];
            sprintf(namee,"%s",key->GetName ());
            char nnn[100];
            sprintf(nnn,"Entries  / %d GeV",hsum->GetBinWidth(1));
            
            hsum->GetYaxis()->SetTitle(nnn);
            
            
            
            //hh[1]->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[titles.size()-1]->FindLastBinAbove(0));
 /*           
    	   for (unsigned int i=0; i <titles.size();i++){
           string str_ = titles[i];
           str_.resize (str_.size () - 5);
	   //cout<<" adding info for "<<str_.c_str()<<"  "<<col_<<endl;
           if (i>0  && (hh[i-1]->GetLineColor() != hh[i]->GetLineColor())) legend_c1->AddEntry(hh[i], str_.c_str(), "l");
    	   }
   */        
            if (cl=1){ 
	    TH1F* v1 = new TH1F("", "", 1, 0, 1);v1->SetLineWidth(4);
	    TH1F* v2 = new TH1F("", "", 1, 0, 1);v2->SetLineWidth(4);
	    TH1F* v3 = new TH1F("", "", 1, 0, 1);v3->SetLineWidth(4);
	    TH1F* v4 = new TH1F("", "", 1, 0, 1);v4->SetLineWidth(4);
	    TH1F* v5 = new TH1F("", "", 1, 0, 1);v5->SetLineWidth(4);
	    TH1F* v6 = new TH1F("", "", 1, 0, 1);v6->SetLineWidth(4);
	    TH1F* v7 = new TH1F("", "", 1, 0, 1);v7->SetLineWidth(4);
	    TH1F* v8 = new TH1F("", "", 1, 0, 1);v8->SetLineWidth(4);
	    TH1F* v9 = new TH1F("", "", 1, 0, 1);v9->SetLineWidth(4);
	    v9->SetMarkerSize(0.4);
	    v9->SetMarkerColor(49);
	    v1->SetMarkerSize(0.4);
             
	    v1->SetLineColor(kBlack);legend_c1->AddEntry(hh[1], "QCD DataDriven  ", "LEP");
	    //v1->SetLineColor(kBlack);legend_c1->AddEntry(v1, "Stau_0.2/0.1", "LEP");
	    v9->SetLineColor(49);legend_c1->AddEntry(hh[2], "Data in Region B", "LEP");
	    v5->SetLineColor(kPink);legend_c1->AddEntry(hh[3], "QCD MC", "l");
/*
	    v6->SetLineColor(kBlue);legend_c1->AddEntry(v6, "TTJets", "l");
	   // v7->SetLineColor(kBlue);legend_c1->AddEntry(v7, "TTX", "l");
	    v2->SetLineColor(kYellow-7);legend_c1->AddEntry(v2, "QCD", "l");
	     v8->SetLineColor(kTeal+9);legend_c1->AddEntry(v8, "DYJets", "l");
	    v4->SetLineColor(kAzure+10);legend_c1->AddEntry(v4, "SingleTop", "l");
            v3->SetLineColor(kMagenta+2);legend_c1->AddEntry(v3, "VV", "l");
*/
	    }
 	    //TH1D *sign;	
	    TH1D* sign = new TH1D("sign", "sign", hh[1]->GetNbinsX(), 0, 12);
               // sign = (TH1D*) hh[1]->Clone();
		//for (int k=0;k<hh[1]->GetNbinsX()<k++) {
		/*for (int k=0;k<hh[1]->GetNbinsX();k++) {
		sign->SetBinContent(k+1, hh[1]->GetBinContent(k+1)/sqrt(allbkg->GetBinContent(k+1)));
		cout<< " sign -> "<<sign->GetBinContent(k+1)<<endl;
		}*/
	
		sign->SetMarkerStyle(20);
		sign->SetMarkerColor(kOrange);

            hsum->SetMaximum(1.5*hs->GetMaximum());
            hsum->SetMinimum(1);
            hsum->Draw("hist");
            //hs->Draw("same hist");
	    hh[1]->Draw("same ep hist");
//	    sign->Draw("same p hist");
	    hh[2]->Draw("same ep hist");
	    //allbkg->Draw("same ep hist");
	    
   	    //c1->cd();
            legend_c1->Draw("sames");
	    c1->SetFillColor(0);
            c1->SetBorderMode(0);
            c1->SetBorderSize(0);
            c1->SetFrameBorderMode(0);
            c1->SetBorderSize(0);
            pad1->SetFrameLineColor(0);;
            pad1r->SetFrameLineColor(0);;


/*
            hsum->SetMaximum(1.5*hs->GetMaximum());
            hs->SetMaximum(1.2*hs->GetMaximum());
            hsum->Draw("hist");
            hs->Draw("same hist");
	    hh[1]->Draw("same ep hist");
	    hh[2]->Draw("same ep hist");
            legend_c1->Draw("sames");
		

*/

	 pad2->cd();
 	 TH1D * ratio = (TH1D*) hh[1]->Clone();
	 ratio->SetStats(0);
	 //ratio->Sumw2();
	 ratio->Divide(allbkg);
	 ratio->SetMarkerStyle(7);
	 ratio->SetMaximum( 1.5 );
	 ratio->SetMinimum(0.5);
	 ratio->GetXaxis()->SetTitle(hh[1]->GetXaxis()->GetTitle());
	 ratio->GetYaxis()->SetTitle("");
	 ratio->SetTitleSize(0);
	 ratio->SetMarkerSize(0.05);
	 ratio->SetMarkerColor(39);
	 ratio->SetLineColor(39);
	 ratio->SetLineWidth(2);
	 ratio->GetYaxis()->SetNdivisions(5);
	 
	 ratio->GetXaxis()->SetNdivisions(545);
	 ratio->GetXaxis()->SetLabelSize(0.15);
	 ratio->GetXaxis()->SetTitleSize(0.12);
	 ratio->GetXaxis()->SetTitleOffset(0.85);
	 
	 ratio->GetYaxis()->SetLabelSize(0.1);
	 ratio->GetYaxis()->SetLabelSize(0.15);
	 ratio->GetYaxis()->SetTitleSize(0.12);
	 ratio->GetYaxis()->SetTitleOffset(0.25);
	 ratio->GetYaxis()->SetTitle("Data / MC");
	 
	 
	 ratio->SetTitleFont(62);
      	 //ratio->GetXaxis()->SetRange(ratio->FindFirstBinAbove(0),ratio->FindLastBinAbove(0));
      	 //ratio->GetXaxis()->SetRange(hh[1]->FindFirstBinAbove(0),hh[1]->FindLastBinAbove(0));
	
	 ratio->GetXaxis()->SetNdivisions(510);
	 ratio->SetTitle("");
	 ratio->Draw("ep");


            gPad->RedrawAxis();
            gPad->Modified();
            gPad->Update();
	    c1->Update();
            
	    c1->Write (namee);
            
            
            char f[100];char ff[100];
            if (!norm_)sprintf(f,"TauMC/%s.png",namee);
            else sprintf(f,"TauMC/%s_Norm.png",namee);
         
	    if (!norm_)sprintf(ff,"TauMC/%s_Log.png",namee);
            else sprintf(ff,"TauMC/%s_Log_Norm.png",namee);
            
	    //if (!norm_)sprintf(f,"Tau/%s.png",namee);
            
		TH1D* ht;
            // ht = (TH1D*)c1->GetPrimitive(namee);
	    c1->SaveAs (f);
            //hsum->SetMaximum(10*hs->GetMaximum());
            /*gPad->SetLogy();
            pad1->SetLogy();
	    c1->SaveAs (ff);
	    c1->Write (namee);
	    */
            
            //sprintf(namee,"%s_ratio",key->GetName ());
            //c3->Write (namee);
            
            
            //string titlee=key->GetName ();
            
            
    
        }

  	} 			// while ( ( TKey *key = (TKey*)nextkey() ) )
    
    
    
    
    // save modifications to target file
    target->SaveSelf (kTRUE);
    TH1::AddDirectory (status);
    cout << "	" << "========================================================" << endl;
    cout<< " Ended SuperImpose of files.... " <<endl;
    
    // for (int i=0;i<SValueVariables_.size();i++){
    //cout<<SValueVariables_[i].second<<endl;}
    
    
    
}

void
//ModifyHist (TH1D* &h, int cl_ ,float & lumi,float & weight,string & title_, bool norm_=false,TLegend *& legend)
ModifyHist (TH1D* &h, int cl_ ,float & lumi,float & weight,string & title_, bool norm_=false)
{

  
    int nbins=h->GetNbinsX();
    int nn=1;
    
    if (  nbins<=150)  nn=5;
    if (  nbins>150)  nn=5;
    if (  nbins>200)  nn=10;
    if (  nbins<=50)  nn=1;
    if (nbins%64 == 0) nn=2;
    if (nbins%38 == 0) nn=2;
    //h->Rebin(4);
    
    h->SetMinimum(0.001);
    h->GetXaxis()->SetNdivisions(512);
    string titlee=h->GetName();
    int col=;//kOrange;
    string title1,title2;
    title1= h->GetTitle();
//    if(title_.find("Data") == 0) col= kBlack;//TT
//    if(title_.find("Stau") == 0) col= kBlack;//TT
   

    if (std::string::npos != title_.find("Data") || std::string::npos != title_.find("Single") || std::string::npos != title_.find("StauA") ||  std::string::npos != title_.find("Sq") || std::string::npos != title_.find("Gl") || std::string::npos != title_.find("0.2")  )  {

    //if ( std::string::npos != title_.find("StauA") ){
	
            col=kBlack ;
            h->SetLineStyle(1);
            h->SetMarkerStyle(20+cl_);
            h->SetMarkerSize(0.4);
            h->SetMarkerColor(col);
            h->SetLineColor(col);
	}
   

    if ( std::string::npos != title_.find("StauA") || std::string::npos != title_.find("0.5") ){
	
            col=49 ;
            h->SetLineStyle(1);
            h->SetMarkerStyle(21+cl_);
            h->SetMarkerSize(0.4);
            h->SetMarkerColor(col);
            h->SetLineColor(col);
	}
   
   
    //h->SetLineWidth(2);
    int nb = h->GetNbinsX();
    float over_ = h->GetBinContent(nb+1);
    float contlast = h->GetBinContent(nb);
    h->SetBinContent(nb,contlast+over_);

    if (std::string::npos != title_.find("QCD"))  col= kBlue-7;
    if (std::string::npos != title_.find("DYJets"))  col= kTeal+9;
    if (std::string::npos != title_.find("DataDriven"))  col= kTeal+9;
    if (std::string::npos != title_.find("WJ"))  col= kPink;
    if (std::string::npos != title_.find("TTJets"))  col= kBlue;//kOr-3
//    if (std::string::npos != title_.find("TTV"))  col= kBlue;
    
    if (std::string::npos != title_.find("TBar") || std::string::npos != title_.find("channel")  || std::string::npos != title_.find("ST"))  col= kAzure+10;

    if (std::string::npos != title_.find("WZ") || std::string::npos != title_.find("WW") || std::string::npos != title_.find("ZZ")) col=kMagenta+2;

    //legend->AddEntry(h, title_.c_str(), "l");



 //cout<< "  "<<cl_<<"  "<<title_<<endl;
   
    if (std::string::npos != title1.find("MET"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
    if (std::string::npos != title1.find("mass"))  h->GetXaxis()->SetTitle("GeV/c");
    if (std::string::npos != title1.find("Inv"))  h->GetXaxis()->SetTitle("GeV/c");
    if (std::string::npos != title1.find("Mass"))  h->GetXaxis()->SetTitle("GeV/c");
    if (std::string::npos != title1.find("met"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
    if (std::string::npos != title1.find("ST"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
    if (std::string::npos != title1.find("HT"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
    if (std::string::npos != title1.find("Jetp"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
    if (std::string::npos != title1.find("Phi"))  h->GetXaxis()->SetTitle("");
    if (std::string::npos != title1.find("dPhi"))  h->GetXaxis()->SetTitle("");
    if (std::string::npos != title1.find("pT"))  h->GetXaxis()->SetTitle("GeV/c^{2}");
    if (std::string::npos != title1.find("nB"))  h->GetXaxis()->SetTitle("B-Jets");
    if (std::string::npos != title1.find("nJ"))  h->GetXaxis()->SetTitle("#Jets");
    if (std::string::npos != title1.find("nL"))  h->GetXaxis()->SetTitle("#Lept");
    
    h->GetXaxis()->SetTitleOffset(0.8);
    
    h->GetYaxis()->SetTitleOffset(1.5);
    
    //h->SetLineColor (col);
       
    //h->SetFillColor (col);
    h->SetMinimum(0.001);
    h->SetLineStyle (col);
//    h->SetFillStyle (3000+cl_);
 // h->SetFillColorAlpha (col,0.9);


   //cout<<" for "<<title_.c_str()<<"  Weight to be applied " <<weight<<"  "<<title1<<"  "<<cl_<<endl;   
    //if (std::string::npos != title1.find("CutFlow")) 
     //if (std::string::npos == title_.find("Single")) 
     
    //if (cl_>0) 
     h->Scale(weight);
     h->SetFillColor(col);
     h->SetLineColor(col);
 // if (  cl_ == 5 ) 
/* if (  cl_ == 5 || cl_== 9  || cl_>=11  ) 
	{  
	   h->SetLineColor (kBlack);
    	   h->SetLineWidth (1);
		}
*/
 
  ofstream tfile;
    if (std::string::npos != title1.find("Cut Flow") ){
  TString outname=title_;
  TString textfilename = "cutflow_"+outname +".txt";
  tfile.open(textfilename);

   tfile << "########################################" << endl;
   for (int b=0;b<16;b++){
   //tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<" & "<<" & "<<endl;	
   if (h->GetBinContent(b) > 0 ) tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<endl;	
   else tfile <<h->GetXaxis()->GetBinLabel(b)<<" & "<<0<<endl;	
   //cout <<title1<<" & "<<h->GetXaxis()->GetBinLabel(b)<<" & "<<h->GetBinContent(b)<<" & "<<" & "<<endl;	
	}}
    tfile.close();
    //if (norm_)    
    //  h->Scale (1/h->Integral());
    
    
    //double dic=double(lumi)/double(weight);
    //double dic=0;
    //if (h->Integral()>0)
    //dic=double(lumi)/double(weight);
    //dic=1;
    string namet=h->GetName();
    
    // double q[5];
    // double probs[5] = {0.025, 0.16, 0.5, 1 - 0.16, 0.975 };
    //  h->GetQuantiles( 5, q, probs );
    
    //    cout<<" Median and Mean values for  process"<<title_<<" variable"<<h->GetName()<<" median "<<q[2]<<" mean "<<h->GetMean()<<endl;
    
    
}





