#include "TH1.h"
#include "TH2F.h"
#include "TFile.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TSystem.h"
#include "TF1.h"
#include "TKey.h"
#include "TH1F.h"
#include "TStyle.h"
#include "TProfile.h"
#include "TLegend.h"
#include "TLine.h"
#include "TArrow.h"
#include "TLatex.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TFormula.h"
#include "TAxis.h"
#include "TRandom3.h"
#include "TMath.h"
#include "THStack.h"

#include <cmath>
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iomanip>

void ReBin(TH1F * &h, TAxis * &ax,int entries_);
void ReBinTTbar(TH1F * &h , TTree * &t);
void ReBinTree(TH1F * &h, TTree * &t );

void ReBin2SIGNAL()
{
  using namespace std;
  
  gStyle->SetOptStat(0);

  TString fileName = FILENAME;
  TFile *target = new TFile(fileBin,"recreate" );
  TFile *file = TFile::Open(fileName);

  if (!file) abort();


  //// Find in the file the TH1 = MVA_MLP_TT , make the custom binning and save a TAxis
  TH1F * ht ;
  ht= (TH1F*) file->Get("MVA_CLASS_TTnlo");
  int entries = ht->GetEntries();
  
  char treename[100];
  sprintf(treename,"Tree_%s",ht->GetName());
  TTree *trT =  (TTree*)file->Get(treename);
 //trT->ls();  
/////////make the binning
  //cout<<"  before  rebinning"<<ht->GetNbinsX()<<endl;
  ReBinTTbar(ht, trT);
  //cout<<" OK, done with the TTJets......"<<endl; 


  //for (unsigned int gg=1;gg<ht->GetNbinsX()+1;gg++){
  //cout<<"  after returning in the main class   "<<ht->GetBinContent(gg)<<"    "<<ht->GetBinLowEdge(gg)<<endl;
  //}


  ///create a new TAxis based on the previous binning
  /*  TFile *target2 = new TFile("test.root","recreate" );
  
  target->cd();
  ht->Write();
  target2->cd();
  ht->Write();

  target2->Write();
  target2->Close();
  delete target2;
  TH1F *ht_norm;
  ht_norm=ht;
  target->cd();
  ht->Write();

  */
 
  //Now, you should have a file TT_axis.root with the TAxis and the TH1 of the Binned template coming from the the MVA_MLP_TT

  TFile *first_source = TFile::Open(fileName);
  TString path ((char *) strstr (target->GetPath (), ":"));
  path.Remove (0, 2);
  ///////Loop in the source for the rest of TH1 
  first_source->cd (path);
   
  TDirectory *current_sourcedir = gDirectory;
  //gain time, do not add the objects in the list in memory
  Bool_t status = TH1::AddDirectoryStatus ();
  TH1::AddDirectory (kFALSE);

  ///////// loop over all keys in this directory
  TChain *globChain = 0;
  TIter nextkey (current_sourcedir->GetListOfKeys ());
  TKey *key, *oldkey = 0;
  while ((key = (TKey *) nextkey ())) {

    //keep only the highest cycle number for each key
    if (oldkey && !strcmp (oldkey->GetName (), key->GetName ()))
      continue;

    first_source->cd (path);
    TObject *obj = key->ReadObj ();
   
    TLegend *legend_c1 = new TLegend (0.35, 0.90, 0.80, 0.70);
    

    if (obj->IsA ()->InheritsFrom ("TH1F")) {

      TH1F *h1 = (TH1F *) obj;
      string name=h1->GetName();
    string t2="CLASS";
     if (std::string::npos != name.find(t2)){

      /////////If TH1 is not MVA_MLP_TT rebin it by using the TAxis obtained from the previous step
      file->cd();
      char treename[100];
      sprintf(treename,"Tree_%s",h1->GetName());
      string str2 ("Normalized");
       //cout<<" for ...."<<treename<<endl;
      if (name.find(str2) == string::npos) {
        //if( name.find("Normalized")==0){ 
        TTree *t =  (TTree*)file->Get(treename);
        ReBinTree(h1,t);
	target->cd();
      string strtt ("TT");
      string strw ("W4Jets");
      string strd ("Data");

     //if (name.find(strtt) != string::npos) h1->Scale(151392.8375/160000);
     //if (name.find(strw) != string::npos) h1->Scale(52433.8092/62536.38);
     //if (name.find(strd) != string::npos) h1->Scale(1.04);
     
	     //h1->Write();
     TH1F * h11 = (TH1F*) h1->Clone();
    //h11->Scale(0.5);
    h11->Write();


      string str3 ("T2tt");
     if (name.find(str3) != string::npos) {
     TH1F * h1x1 = (TH1F*) h1->Clone();
     TH1F * h1x2 = (TH1F*) h1->Clone();
     TH1F * h1x05 = (TH1F*) h1->Clone();
     char nn[100];
     
     sprintf(nn,"%s_x%d",h1->GetName(),1);
     h1x1->SetName(nn);
     h1x1->SetTitle(nn);
     h1x1->Write();
   
     sprintf(nn,"%s_x%d",h1->GetName(),2);
     h1x2->Scale(2.);
     h1x2->SetName(nn);
     h1x2->SetTitle(nn);
     h1x2->Write(nn);
   
     sprintf(nn,"%s_x0.5",h1->GetName());
     h1x05->Scale(0.5);
     h1x05->SetName(nn);
     h1x05->SetTitle(nn);
     h1x05->Write(nn);
      
     }
        h1->Scale(1/h1->Integral());
        char hnormname[100];
        sprintf(hnormname,"%s_Normalized",h1->GetName());
	h1->SetName(hnormname);
	h1->SetTitle(hnormname);
	h1->Write();
      }

    }
  }
}
  target->cd();
  target->Write();
  target->Close();



}
//////////////// This will make a binning  of the TT_MVA Classification- Default range is -05 to 1.5 .
///We will first merge all bins below 0 and then scan the bins where x>0 - If one bin
// is found to have less than  10 entries all bins from this to the end will be merged to one bin.

void ReBinTTbar(TH1F * &h,TTree * &trTT){
  float binContent[1000];
  binContent{1000}=0;

  bool fixed_bins=false;
  

  //TH1F *histo = new TH1F(h->GetName(),h->GetTitle(),h->GetNbinsX(),-0.5,1.5);
      
  vector <float> *values;
  Double_t weight;
  vector <float> values_;values_.clear();
  TBranch *bEvaluation = 0;
  TBranch *bWeight = 0;
  trTT->SetBranchAddress("Evaluation_CLASS",&values,&bEvaluation);
  trTT->SetBranchAddress("Weight_CLASS",&weight,&bWeight);
  Long64_t tentry = trTT->LoadTree(0);
  bEvaluation->GetEntry(tentry);
  bWeight->GetEntry(tentry);
  for (UInt_t j = 0; j < values->size(); ++j) {
	  values_.push_back(values->at(j));
	  //values_.push_back(vl);
  }



  sort (values_.begin (), values_.end ());
   string tt_file="../Skimmed/TTnlo_1_tree.root";
   TFile *fl = new TFile(tt_file.c_str(),"read");
  TTree *treeT =  (TTree*)fl->Get("OBS_full");
  float weightSF; TBranch *b_weight=0;
  treeT->SetBranchAddress("weight",&weightSF,&b_weight);

  Long64_t ttentry = treeT->LoadTree(0);
  int nT = treeT->GetEntries();

 // cout<<"  check the size "<<nT<<" values "<<values_.size()<<"   "<<trTT->GetEntries()<<endl;

  TH1F *histo = new TH1F(h->GetName(),h->GetTitle(),NBINS,values_[0],values_[values_.size()-1]);
  //TH1F *histo = new TH1F(h->GetName(),h->GetTitle(),100,-1,1.5);
 // TH1F *histo = new TH1F(h->GetName(),h->GetTitle(),100,-1,2);
       cout<<values_[0]<<"   "<<values_[values_.size()-1]<<endl;
  for (UInt_t kk = 0; kk < values_.size(); kk++) {
	  treeT->GetEntry(kk);
    histo->Fill(values_[kk],weightSF*weight);
    //histo->Fill(values_[kk],weightSF);
    //cout<<"  i "<<kk<<"  weightSF "<<weightSF<<"  "<<weight<<endl;
    //if (values_[kk] > 2 || values_[kk] <-1)   cout<<values_[kk]<<"   "<<histo->GetName()<< "   "<<weight<<endl;
  }
  //histo->Scale(1/histo->Integral());
  //histo->Scale(LUMI);
  //histo->Scale(weight);

  h=histo;
  int count_new_bins=0;
  int last_big_bin=0;
  int merge_up_to_this_bin=0;
  
  vector <double> low_edges;
  low_edges.clear();
  int MINENTRIES=nentries;
  int histo_size=h->GetNbinsX();
  for  (unsigned int nb = 0;nb<int(h->GetNbinsX()+1);nb++){
    
    ///////First find the first bin above x>0 which has more than 10 entries - merge_up_to_this_bin refers to this exact bin
    float  small_bins=0;	
    if ( h->GetBinContent(nb)>=MINENTRIES && h->GetBinContent(nb-1)<MINENTRIES && h->GetBinLowEdge(nb-1)<0){
      merge_up_to_this_bin=nb-1;
      // low_edges.push_back(float (h->GetBinLowEdge(nb)));
      //  cout<<" WILL MERGE NEGATIVE BINS with <MINENTRIES up to "<<nb<<"  "<<h->GetBinLowEdge(nb)<<endl;
  
      //   low_edges.push_back(float (h->GetBinLowEdge(nb)));
    }

    //  if ( h->GetBinContent(nb)>MINENTRIES && h->GetBinLowEdge(nb)>0) low_edges.push_back(float (h->GetBinLowEdge(nb)));
    if ( h->GetBinContent(nb)>=MINENTRIES && h->GetBinLowEdge(nb)> h->GetBinLowEdge(merge_up_to_this_bin-1)  ) {
  
  
      //cout<<" found >  "<<MINENTRIES<< "  entries  for  "<<nb<<"  "<<h->GetBinLowEdge(nb)<<"   "<<h->GetBinContent(nb)<<endl;
      low_edges.push_back(float (h->GetBinLowEdge(nb)));
    }

    //////// the last_big_bin counts for the last bin with more than 10 entries      	
    if (h->GetBinContent(nb)<MINENTRIES && h->GetBinContent(nb-1)>=MINENTRIES && h->GetBinLowEdge(nb)>0){
      last_big_bin=nb-1;
      //    low_edges.push_back(float ( h->GetBinLowEdge(last_big_bin)));
    //  break;
    cout<<" we are here  "<<nb<<"  "<<h->GetNbinsX()<<endl;
    for (unsigned int b=nb;b<int(h->GetNbinsX()+1);b++){
    float sum_two_bins = h->GetBinContent(b);	
	
	    cout<<" ===================  bin "<<b<<" info "<<h->GetBinContent(b)<<endl;

    sum_two_bins+=h->GetBinContent(b+1);
    
    if (sum_two_bins<MINENTRIES) { 
 cout<<" did not find a value that is satisfying you...."<<sum_two_bins<<"  "<<h->GetBinContent(b)<<"  "<<h->GetBinContent(b+1)<<"  "<<b<<endl;


    }
    if (sum_two_bins>=MINENTRIES) { 
	    low_edges.push_back(float (h->GetBinLowEdge(b+2))); 
	    cout<<" now merged the "<<b<<" and  "<<b+1<<"  bins "<<"  "<<h->GetBinContent(b)<<"  "<<h->GetBinContent(b+1)<<endl;
	b++;break;
    }
    

    }
    
    }
  }

 
  sort (low_edges.begin (), low_edges.end ());

  double *valsContent = new double[(low_edges.size()+1)];

  for (unsigned int t=0;t<low_edges.size();t++){
    valsContent[t]=low_edges[t];
    //cout<<" SIZEEEEEEEEEEEEEE=========== > "<<low_edges[t]<<" i "<<t<<" size  "<<low_edges.size()<<" value "<<endl;//valsContent[t+1]<<endl;
  }

  valsContent[low_edges.size()]=values_[values_.size()-1];
  //valsContent[0]=-0.5;



  //valsContent[low_edges.size()]<<"  "<<low_edges[low_edges.size()-1]<<endl;

  //cout<<valsContent[low_edges.size()]<<"  "<<low_edges[low_edges.size()-1]<<endl;
  TAxis * axiss= new TAxis(low_edges.size(), valsContent);

  cout<<" OK here with the myNewAxis....."<<endl;

  ///////merge the bin contents of the x<0 area
  for (int k=0;k<merge_up_to_this_bin+1;k++){
    small_bins+=h->GetBinContent(k);
  }

  ////////assign the new bin content
  for  (unsigned int n_big = merge_up_to_this_bin+1;n_big<last_big_bin+1;n_big++){

    count_new_bins++;
    binContent[count_new_bins] = float(h->GetBinContent(n_big));
  }

  binContent[0]+=small_bins;


  for  (unsigned int n_small = last_big_bin+1;n_small<int(h->GetNbinsX());n_small++){
    binContent[count_new_bins+1]+= float(h->GetBinContent(n_small));
  }


  ///now make a new TH1 which will hold  the new "binned" distribution
  TH1F *histo_binned;

//if (fixed_bins) histo_binned = new TH1F("","",NBINS,values_[0], values_[values_.size()-1]);
  if (fixed_bins) histo_binned = new TH1F("","",NBINS,-1.5,2);
  if (!fixed_bins) histo_binned = new TH1F("","",axiss->GetNbins(), axiss->GetXbins ()->fArray );

  /////get the same name,title from the input TH1
  histo_binned->SetName(h->GetName());
  histo_binned->SetTitle(h->GetTitle());
  
  ////now, make the new binning and return the new histogram

 
  // histo_binned->SetBinContent(merge_up_to_this_bin+1,small_bins);

  for (UInt_t kk = 0; kk < values_.size(); kk++) {
      treeT->GetEntry(kk);
     histo_binned->Fill(values_[kk],weight*weightSF);
      //histo_binned->Fill(values_[kk],weightSF);
    //histo_binned->Fill(values_[kk]);
  }
 // histo_binned->Scale(1/histo->Integral());
//  histo_binned->Scale(LUMI);
  int ls_bin = histo_binned->GetNbinsX();
  float  ls_bin_cont = histo_binned->GetBinContent(ls_bin);
  float  ls_bin_cont1 = histo_binned->GetBinContent(ls_bin+1);
 //histo_binned->SetBinContent(ls_bin, ls_bin_cont+ls_bin_cont1);
 //cout<<" was ls_bin "<<ls_bin<<" last bin "<<ls_bin_cont<<" last+1 "<<ls_bin_cont1<<endl;
  
  histo_binned->Sumw2();
  h=histo_binned;
  /*TFile *target2 = new TFile("test.root","recreate" );
  target2->cd();
  h->Write();
  target2->Write();
  target2->Close();
  delete target2;*/
  // for (unsigned int nbb=1;nbb<h->GetNbinsX()+1;nbb++){
  //cout<<" From the histo_binned "<<h->GetBinContent(nbb)<<"   "<<h->GetBinLowEdge(nbb)<<endl;
 // }

  TFile *taxisFile;
  // TAxis *axiss;
  taxisFile = new TFile ("TT_axis/TT_axis_POINT_CLASS_nentriesEVNTS.root", "recreate");
  taxisFile->cd ();
  axiss = histo_binned->GetXaxis();
  axiss->Write();
  histo_binned->SetName("Binning_Template_POINT_nentriesEVNTS");
  histo_binned->Write();
  //taxisFile->Write ();
  taxisFile->Close ();
   
  cout<<" ============================================================== end of RebinTTbar ============================================="<<endl;
}

///////input is the initial histo, the TAxis and the netries from the template histo
//void ReBinTree(TH1F * &h, TTree *&tr ,TAxis *&axis){
void ReBinTree(TH1F * &h, TTree *&tr ){
  // TH1F *histo;
  //  histo=h; 

  TFile *taxisF = TFile::Open("TT_axis/TT_axis_POINT_CLASS_nentriesEVNTS.root");
  taxisF ->cd();
  TH1F * httt = (TH1F*) taxisF->Get("Binning_Template_POINT_nentriesEVNTS"); 
  TAxis *axis;
  taxisF->cd();
  axis = httt->GetXaxis();
  /*
    for (unsigned int nbbs=1;nbbs<httt->GetNbinsX()+1;nbbs++){
    cout<<" From the histo_binned in ReBinTree class   "<<httt->GetBinContent(nbbs)<<" BinLowEdge  "<<httt->GetBinLowEdge(nbbs)<<" #Bin "<<nbbs<<" BinWidth  "<<httt->GetBinWidth(nbbs)<<" Integral  "<<float(httt->Integral())<<endl;
    }*/
  /////// make a new histo, with TAxis 
  //TH1F *histo_binned = new TH1F(h->GetName(),h->GetTitle(),axis->GetNbins(), axis->GetXmin(), axis->GetXmax() );
  //TH1F *histo_binned = new TH1F(h->GetName(),h->GetTitle(),axis->GetNbins(), axis->GetXbins ()->fArray );
  vector <float> *values;
  Double_t weight=0;
  vector <float> values_;values_.clear();
  TBranch *bEvaluation = 0;
  TBranch *bWeight = 0;
  tr->SetBranchAddress("Evaluation_CLASS",&values,&bEvaluation);
  tr->SetBranchAddress("Weight_CLASS",&weight,&bWeight);
  Long64_t tentry = tr->LoadTree(0);
  bEvaluation->GetEntry(tentry);
  bWeight->GetEntry(tentry);
  for (UInt_t j = 0; j < values->size(); ++j) {
	  values_.push_back(values->at(j));
  }
  sort (values_.begin (), values_.end ());
  char sgn_file[100];
  string str = h->GetName();
  //cout<<str<<endl;
  if (std::string::npos == str.find("TMlpANN"))
  str.erase (0,8);
  if (std::string::npos != str.find("TMlpANN"))
  str.erase (0,12);
  //cout<<str<<endl;
  sprintf(sgn_file,"../Skimmed/%s_1_tree.root",str.c_str());

  //if (std::string::npos != str.find("Plus"))
   //string sgn_file="../Skimmed/_second_tree.root";
   TFile *sgn = new TFile(sgn_file,"read");
  TTree *treeS =  (TTree*)sgn->Get("OBS_full");
  float weightSF=0; TBranch *b_weight=0;
  treeS->SetBranchAddress("weight",&weightSF,&b_weight);

  Long64_t stentry = treeS->LoadTree(0);
  int nS = treeS->GetEntries();

  //cout<<"  check the size ... "<<nS<<" values "<<values_.size()<<"   "<<treeS->GetEntries()<<"  "<<h->GetName()<<endl;

  //cout<<" after making the histo "<<histo_binned->GetName()<<"  bin0 "<<histo_binned->GetBinLowEdge(0)<<" bin1  "<<histo_binned->GetBinLowEdge(1)<<endl;
  sort (values_.begin (), values_.end ());
  string str_signal="T2tt";
  string str_signall="us";
  TH1F* histo_binned,*histo2;
  string nn=h->GetName();
  //if (nn.find(str_signal)  != string::npos){
  //histo_binned = new TH1F(h->GetName(),h->GetTitle(),axis->GetNbins(), -0.2,0.9 );
  //histo2 = new TH1F(histo_binned->GetName(),histo_binned->GetTitle(),histo_binned->GetNbinsX(),0.2,0.9);
  
  histo_binned = new TH1F(h->GetName(),h->GetTitle(),axis->GetNbins(), axis->GetXbins ()->fArray );
 // histo_binned = new TH1F(h->GetName(),h->GetTitle(),axis->GetNbins(), values_[0],2);
  histo2 = new TH1F(histo_binned->GetName(),histo_binned->GetTitle(),histo_binned->GetNbinsX(),0,1);
 // histo2 = new TH1F(histo_binned->GetName(),histo_binned->GetTitle(),histo_binned->GetNbinsX(),axis->GetXbins ()->fArray);
  
  //histo_binned = new TH1F(h->GetName(),h->GetTitle(),axis->GetNbins(), values_[0],values_[values_.size()-1]);
  //histo2 = new TH1F(histo_binned->GetName(),histo_binned->GetTitle(),histo_binned->GetNbinsX(),values_[0],values_[values_.size()-1]);
  //}
  //else{ // (nn.find(str_signal) == string::npos )
  //histo_binned = new TH1F(h->GetName(),h->GetTitle(),axis->GetNbins(), values_[0],values_[values_.size()-1]);
  //histo2 = new TH1F(histo_binned->GetName(),histo_binned->GetTitle(),histo_binned->GetNbinsX(),values_[0],values_[values_.size()-1]);
 // }
      //string name=histo_binned->GetName();

      /////////If TH1 is not MVA_MLP_TT rebin it by using the TAxis obtained from the previous step
     // if (name.find(str_signal) != string::npos) {weight *=scale;
      //   cout<<" weight  "<<weight<<" name "<<name<<endl;
      //}
   //cout<<" histo_binned->GetName() "<<histo_binned->GetName()<<endl;
   //}
   //weight=1;
  //cout<<" Weightss ? histo_binned "<<histo_binned->GetName()<<"  "<<weight<<endl;
   float w=0;
  for (unsigned int k = 0; k < values_.size(); k++) {
  
	  treeS->GetEntry(k);
	  
   //histo_binned->Fill(values_[k],weight);
   string dd="TTnlo"; 
   string name=histo_binned->GetName(); 
	w=weight;
       /*	
   if (std::string::npos != name.find(dd))
   	{ 
		if (values_[k]>=0.5){ 
   	w*=0.85;
	
		}
		
	//cout<<" w "<<w<<"  "<<weight<<endl;
	}
	//weight=w;
	*/
   histo_binned->Fill(values_[k],w*weightSF);
    //if( histo_binned->GetName().c_str() == "MVA_MLP_DataMu" )
 //if (weight==1 && values_[k]>0.75) weight*=1.1;    
   //cout<<values_[k]<<"   "<<histo_binned->GetName()<< "  weight  "<<weight<<"  ievnt  "<<k<<endl;
   //histo_binned->Fill(values_[k],weightSF);
  //cout<<" Weightss ? histo_binned "<<histo_binned->GetName()<<"  "<<weight<<"   "<<weightSF<<endl;
  }



//if (histo_binned->GetName()=="WJets_HT_400_Inf") 
//cout <<"  "<<histo_binned->GetName()<<"  "<<values_[0]<<"  "<<values_[values_.size()-1]<<endl;
//cout<<" hist_binned  "<<histo_binned->GetName()<<"  "<<histo_binned->GetNbinsX()<<endl;
//histo_binned->Scale(weight);

//cout<<" here again..."<<histo_binned->GetName()<<"   "<<values_[0]<<"   "<<values_[values_.size()-1]<<"   "<<histo_binned->GetNbinsX()<<endl;

 //TH1F *histo2 = new TH1F(histo_binned->GetName(),histo_binned->GetTitle(),axis->GetNbins(), axis->GetXbins ()->fArray );
 //TH1F *histo2 = new TH1F(histo_binned->GetName(),histo_binned->GetTitle(),histo_binned->GetNbinsX(), axis->GetXbins ()->fArray );
 //TH1F *histo2 = new TH1F(histo_binned->GetName(),histo_binned->GetTitle(),histo_binned->GetNbinsX(),-0.5,1.5);

  for (unsigned int n = 1; n < histo_binned->GetNbinsX()+1; n++) {
  histo2->SetBinContent(n,histo_binned->GetBinContent(n));
  //if ( histo_binned->GetBinContent(n) < 0 || histo_binned->GetBinContent(n) > 1)
  //cout<<" Filling the fixed widht histo.... "<<n<<"   "<<histo_binned->GetBinContent(n)<<"   "<<histo_binned->GetNbinsX()<<"   "<<histo2->GetNbinsX()<<endl;
  //cout<<" Filling the fixed widht histo.... "<<histo2->GetBinContent(n)<<"   "<<histo2->GetName()<<"   "<<histo2->GetNbinsX()<<"  "<<histo2->GetBinContent(histo_binned->GetNbinsX())<<endl;
  }


  //cout<<" Filling the fixed widht histo.... "<<histo2->GetBinContent(0)<<"   "<<histo2->GetName()<<"   "<<histo2->GetNbinsX()<<"  "<<histo2->GetBinContent(histo_binned->GetNbinsX())<<endl;

  //h=histo_binned; 
  h=histo2; 
  //h=histo2; 
  //float bin_zero=h->GetBinContent(0);
  //float bin_one=h->GetBinContent(1);
  //h->SetBinContent(1,bin_zero+bin_one);
  //h->SetBinContent(0,0);
   //cout<<"  The binned histogram is  "<<h->GetName()<< "  axis_min "<<axis->GetXmin()<<" axis_max  "<<axis->GetXmax()<<" Integral  "<<float(histo_binned->Integral())<<" histo with fixed width  "<<float(histo2->Integral())<<endl;
/*
    for (unsigned int bn=1;bn<int(h->GetNbinsX()+1);bn++){
    cout<<"  The binned histogram is  "<<h->GetName()<<"  "<<bn<<"  "<<h->GetBinContent(bn)<<"  "<<h->GetBinLowEdge(bn)<<" axis_min "<<axis->GetXmin()<<" axis_max  "<<axis->GetXmax()<<" Integral  "<<float(h->Integral())<<endl;
    }*/
}

