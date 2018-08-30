
#include "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/interface/functionsSUSY.h"
//#include "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/interface/lester_mt2_bisect.h"
//#include "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/interface/mt2_bisect.h"
//#include "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/interface/mt2_bisect.cpp"
//#include "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/interface/Basic_Mt2_332_Calculator.h"
//#include "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/interface/Basic_Nt2_332_Calculator.h"
//#include "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/interface/mTBound.h"
//#include "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/interface/mTTrue.h"
//#include "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/interface/TMctLib.h"
//#include "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/interface/mctlib.h"
//#include "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/interface/Basic_MPairProd_Calculator.h"
#include "TTree.h"
#include <iostream>

//#include <ScaleFactor.h>
#include <TLorentzVector.h>
#include <TVector2.h>
using namespace std;


const  int CutN=31;
const  int CutF=31;
const int nBinsSR=51;


unsigned int RunMin = 9999999;
unsigned int RunMax = 0;
     

//bool isData = false;


double ChiMass=0;
double mIntermediate = tauMass;
double sumpT = 0;
double XSec=-1;
double xs,fact,fact2;
 
double ErrorSoW=0;
double sumOfWeight=0;

vector<TLorentzVector> AllJets_Lepton_noMet;
vector<TLorentzVector> JetsMV;
vector<TLorentzVector>  ElMV;
vector<TLorentzVector>  MuMV;
vector<TLorentzVector>  TauMV;
vector<TLorentzVector>  LeptMV;

Int_t 	   npart;
TTree *Tp;
void SetupTreeTp(){
Tp  = new TTree("Tp","Tp");
Tp->Branch("npart",&npart,"npart/I");

}



   int nBinsDZeta = 5;
   double binsDZeta[6] = {-500, -150,-100,0,50,1000};
   int nBinsDZetaR = 29;
   //double binsDZetaR[18] = {0, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,2,10};
   double binsDZetaR[30] = {0,0.25,0.5, 0.75, 1, 1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9, 2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.5,4,4.5,5,10};

int nBinsmet = 8;
//   double binsmet[7] =  {0, 40, 80,100,120,250,1000};
   double binsmet[9] =  {0, 10,20,30, 40, 80,120,250,1000};
   double binsmett[9] =  {0.1, 10,20,30, 40, 80,120,250,1000};

   int nBinsmetFB = 8;
   double binsmetFB[9] = {0, 40, 80,120,160,200,300,400,1000};

   int nBinsMT2lesterFB = 7;
   //double binsMT2lesterFB[7] = {0, 40,80,120,160,200,1000};
   double binsMT2lesterFB[8] = {0,10,20,30,40,80,120,1000};

   int nBinsDZetaFB = 5;
   //double binsDZetaFB[6] = {-500, -300,-150,-100, 50,1000};
   double binsDZetaFB[6] = {-500, -150,-100, 0,50,1000};

   int nBinsTauPt = 4;
   double binsTauPt[5] = {0, 40, 80,120,1000};

   int nBinsMTsum = 4;
   double binsMTsum[5] = {0, 40,120,260,1000};

   int nBinsMTtot = 4;
   double binsMTtot[5] = {0, 40,120,200,1000};

   int nBinsMCTb = 4;
   double binsMCTb[5] = {0, 50,100,200,1000};

   int nBinsMT = 4;
   double binsMT[5] = {0, 40,120,160,1000};

   int nBinsMTDil = 4;
   double binsMTDil[5] = {0, 40,120,200,1000};

   int nBinsDr = 5;
   double binsDr[6] = {0,1,2,3,4,7};


   int nBinsMT2lester = 8;
   double binsMT2lester[9] = {0,10,20,30,40,80,100,120,1000};
   double binsMT2lesterr[9] = {0.1,10,20,30,40,80,100,120,1000};

double HIP_SF(double pt,double eta)

{

	TString inputRootFile = "/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/data/HIP_mediumID.root";
TFile * fileIn = new TFile(inputRootFile, "read");
	if (fileIn->IsZombie() ) { std::cout << "ERROR in ScaleFactor::init_ScaleFactor(TString inputRootFile) " <<inputRootFile << " does not exist. Please check. " <<std::endl; exit(1); };


TIter nextkey (fileIn->GetListOfKeys ());
TKey *key = 0;
key = (TKey *) nextkey ();
TObject *obj = key->ReadObj ();
//cout << "2D histos name for SF = " << obj->GetName() << endl;
TH2D *histo = (TH2D*) obj;
//TH2D *histo = (TH2D*)fileIn->Get("histo2D");
double ptN = histo->GetXaxis()->FindBin(pt);
double etaN = histo->GetYaxis()->FindBin(eta);
double result = histo->GetBinContent(ptN,etaN);
delete histo;
delete fileIn;
return result;
}



double EWKWeight(float pt){
float sf = 1;

if (pt>0 && pt <50 ) sf = 1.;
if (pt>50 && pt <100 ) sf = 1.052;
if (pt>100 && pt <150 ) sf = 1.179;
if (pt>150 && pt <200 ) sf = 1.150;
if (pt>200 && pt <300 ) sf = 1.057;
if (pt>300 && pt <400 ) sf = 1.;
if (pt>400 && pt <600 ) sf = 0.912;
if (pt>600 ) sf = 0.783;

return sf;
}

double TauFakeRateFromDataVLoose(float pt,float eta, string sel,string working_point){
float SF = 1.;


//80x MVAid


if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.29099;
                if (pt>30 && pt<40) SF = 0.271191;
                if (pt>40 ) SF = 0.231226;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.298628;
                if (pt>30 && pt<40) SF = 0.274101;
                if (pt>40 ) SF = 0.173872;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.316511;
                if (pt>40) SF = 0.239111;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.272468;
                if (pt>40) SF = 0.274652;
        }

return SF;
}


double TauFakeRateFromData(float pt,float eta, string sel,string working_point){
float SF = 1.;


//80x MVAid


if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.726176;
                if (pt>30 && pt<40) SF = 0.661467;
                if (pt>40 ) SF = 0.560296;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.67626;
                if (pt>30 && pt<40) SF = 0.613248;
                if (pt>40 ) SF = 0.390183;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.681135;
                if (pt>40) SF = 0.639072;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.598693;
                if (pt>40) SF = 0.608262;
        }



if ( working_point == "JetEnUp"){

if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.693816;
                if (pt>30 && pt<40) SF = 0.755752;
                if (pt>40 ) SF = 0.799038;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.703645;
                if (pt>30 && pt<40) SF = 0.685642;
                if (pt>40 ) SF = 0.563055;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.750739;
                if (pt>40) SF = 0.92409;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.789474;
                if (pt>40) SF = 0.75253;
        }

}



if ( working_point == "JetEnDown"){

if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.698346;
                if (pt>30 && pt<40) SF = 0.766291;
                if (pt>40 ) SF = 0.81272;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.711696;
                if (pt>30 && pt<40) SF = 0.692606;
                if (pt>40 ) SF = 0.601689;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.7331;
                if (pt>40) SF = 0.894102;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.787022;
                if (pt>40) SF = 0.752606;
        }

}


if ( working_point == "UnclEnUp"){

if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.684853;
                if (pt>30 && pt<40) SF = 0.76416;
                if (pt>40 ) SF = 0.790217;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.698415;
                if (pt>30 && pt<40) SF = 0.677333;
                if (pt>40 ) SF = 0.577103;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.724432;
                if (pt>40) SF = 0.92409;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.790163;
                if (pt>40) SF = 0.745237;
        }

}


if ( working_point == "UnclEnDown"){

if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.699328;
                if (pt>30 && pt<40) SF = 0.772908;
                if (pt>40 ) SF = 0.809592;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.710733;
                if (pt>30 && pt<40) SF = 0.692155;
                if (pt>40 ) SF = 0.608349;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.765928;
                if (pt>40) SF = 0.866507;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.79236;
                if (pt>40) SF = 0.756964;
        }

}


if ( working_point == "MuEnUp"){

if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.645379;
                if (pt>30 && pt<40) SF = 0.661151;
                if (pt>40 ) SF = 0.562661;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.675891;
                if (pt>30 && pt<40) SF = 0.609651;
                if (pt>40 ) SF = 0.389478;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.675381;
                if (pt>40) SF = 0.662927;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.757503;
                if (pt>40) SF = 0.610973;
        }

}



if ( working_point == "MuEnDown"){

if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.648652;
                if (pt>30 && pt<40) SF = 0.662728;
                if (pt>40 ) SF = 0.562374;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.676839;
                if (pt>30 && pt<40) SF = 0.616648;
                if (pt>40 ) SF = 0.390872;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.678148;
                if (pt>40) SF = 0.686361;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.756978;
                if (pt>40) SF = 0.607251;
        }

}


if ( working_point == "ElEnUp"){

if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.646808;
                if (pt>30 && pt<40) SF = 0.661467;
                if (pt>40 ) SF = 0.560296;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.676055;
                if (pt>30 && pt<40) SF = 0.614288;
                if (pt>40 ) SF = 0.390694;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.681135;
                if (pt>40) SF = 0.639072;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.75731;
                if (pt>40) SF = 0.608262;
        }

}


if ( working_point == "ElEnDown"){

if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.646804;
                if (pt>30 && pt<40) SF = 0.65908;
                if (pt>40 ) SF = 0.558602;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.676066;
                if (pt>30 && pt<40) SF = 0.613408;
                if (pt>40 ) SF = 0.389452;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.677844;
                if (pt>40) SF = 0.640211;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.756993;
                if (pt>40) SF = 0.610414;
        }

}


if ( working_point == "TauEnUp"){

if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.648833;
                if (pt>30 && pt<40) SF = 0.644346;
                if (pt>40 ) SF = 0.531448;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.672807;
                if (pt>30 && pt<40) SF = 0.60031;
                if (pt>40 ) SF = 0.362064;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.680111;
                if (pt>40) SF = 0.590337;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.753283;
                if (pt>40) SF = 0.594045;
        }

}

if ( working_point == "TauEnDown"){

if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.649911;
                if (pt>30 && pt<40) SF = 0.663066;
                if (pt>40 ) SF = 0.601234;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.674619;
                if (pt>30 && pt<40) SF = 0.634861;
                if (pt>40 ) SF = 0.404108;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.710257;
                if (pt>40) SF = 0.629404;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.759325;
                if (pt>40) SF = 0.622256;
        }

}

if ( working_point == "BTagUp"){

if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.653137;
                if (pt>30 && pt<40) SF = 0.670859;
                if (pt>40 ) SF = 0.586556;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.681814;
                if (pt>30 && pt<40) SF = 0.62254;
                if (pt>40 ) SF = 0.413818;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.71083;
                if (pt>40) SF = 0.606968;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.760291;
                if (pt>40) SF = 0.631967;
        }

}

if ( working_point == "BTagDown"){

if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 0.641497;
                if (pt>30 && pt<40) SF = 0.655955;
                if (pt>40 ) SF = 0.520607;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 0.668485;
                if (pt>30 && pt<40) SF = 0.594856;
                if (pt>40 ) SF = 0.354048;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.654878;
                if (pt>40) SF = 0.594868;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.753953;
                if (pt>40) SF = 0.589413;
        }

}

return SF;

}



double TauFakeRate(float pt,float eta, string sel,string working_point){
float SF = 1.;


//80x MVAid


if ( working_point == "TFRJetEnUp"){

if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 1.13395;
                if (pt>30 && pt<40) SF = 1.12674;
                if (pt>40 ) SF = 1.28658;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 1.12286;
                if (pt>30 && pt<40) SF = 1.22019;
                if (pt>40 ) SF = 1.05257;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.976482;
                if (pt>40) SF = 2.1966;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.896117;
                if (pt>40) SF = 1.07363;
        }

}//mutau MVA


else if ( working_point == "TFRJetEnDown"){
if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 1.16832;
                if (pt>30 && pt<40) SF = 1.13744;
                if (pt>40 ) SF = 1.27319;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 1.15464;
                if (pt>30 && pt<40) SF = 1.17642;
                if (pt>40 ) SF = 1.16929;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 1.13535;
                if (pt>40) SF = 2.70057;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.914509;
                if (pt>40) SF = 1.11113;
        }

}//mutau MVA



else if ( working_point == "TFRTauEnUp"){
if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 1.09872;
                if (pt>30 && pt<40) SF = 0.961079;
                if (pt>40 ) SF = 0.897534;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 1.07447;
                if (pt>30 && pt<40) SF = 1.04198;
                if (pt>40 ) SF = 0.741901;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.888785;
                if (pt>40) SF = 1.20708;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.837741;
                if (pt>40) SF = 0.902976;
        }

}//mutau MVA


else if ( working_point == "TFRTauEnDown"){
if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 1.18576;
                if (pt>30 && pt<40) SF = 1.04045;
                if (pt>40 ) SF = 1.14634;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 1.16617;
                if (pt>30 && pt<40) SF = 1.18176;
                if (pt>40 ) SF = 0.864892;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 1.05005;
                if (pt>40) SF = 1.94742;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.912782;
                if (pt>40) SF = 0.950736;
        }

}//mutau MVA


else if ( working_point == "TFRMuEnUp"){
if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 1.11923;
                if (pt>30 && pt<40) SF = 1.02944;
                if (pt>40 ) SF = 0.96733;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 1.1246;
                if (pt>30 && pt<40) SF = 1.07141;
                if (pt>40 ) SF = 0.844204;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.908234;
                if (pt>40) SF = 1.77257;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.87063;
                if (pt>40) SF = 0.92934;
        }

}//mutau MVA


else if ( working_point == "TFRMuEnDown"){
if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 1.12687;
                if (pt>30 && pt<40) SF = 1.00911;
                if (pt>40 ) SF = 0.958254;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 1.12647;
                if (pt>30 && pt<40) SF = 1.10256;
                if (pt>40 ) SF = 0.841932;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.900177;
                if (pt>40) SF = 1.80231;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.875394;
                if (pt>40) SF = 0.911063;
        }

}//mutau MVA


else {
if (  fabs(eta) < 0.8 )
        {
                if (pt>20 && pt<30) SF = 1.12667;
                if (pt>30 && pt<40) SF = 1.0178;
                if (pt>40 ) SF = 0.961808;
        }
if (  fabs(eta) > 0.8 && fabs(eta) < 1.44 )
        {

                if (pt>20 && pt<30) SF = 1.12651;
                if (pt>30 && pt<40) SF = 1.08668;
                if (pt>40 ) SF = 0.832438;
        }

if (  fabs(eta) > 1.44 && fabs(eta) < 1.566 )
        {

                if (pt>20 && pt<40) SF = 0.907089;
                if (pt>40) SF = 1.70447;
        }
if (  fabs(eta) > 1.566 && fabs(eta) < 2.3 )
        {

                if (pt>20 && pt<40) SF = 0.875675;
                if (pt>40) SF = 0.91729;
        }

}//mutau MVA

return SF;

}

double MuonFakeRate(float pt, float eta){
float muonfake = 1.;

if (  fabs(eta) < 1.2 ) muonfake = 1.04;
if (  fabs(eta) > 1.2 && fabs(eta) < 1.7 ) muonfake = 1.54;
if (  fabs(eta) > 1.7 && fabs(eta) < 2.3 ) muonfake = 1.42;
	
return muonfake;
}


double ElectronFakeRate(float pt, float eta){
float elefake = 1.;

if (  fabs(eta) < 1.460 ) elefake = 1.80;
if (  fabs(eta) > 1.558 ) elefake = 1.30;
	
return elefake;
}



double TauiD(string sel,string working_point){

float SF = 1;

if ((sel =="mutau" || sel == "eltau")  && working_point == "CutBased_Loose" )
	SF = 0.81;

if ((sel =="mutau" || sel == "eltau")  && working_point == "CutBased_Medim" )
	SF = 0.79;
if ((sel =="mutau" || sel == "eltau")  && working_point == "CutBased_Tight" )
	SF = 0.79;


if ((sel =="mutau" || sel == "eltau")  && working_point == "MVA_Vloose" )
	SF = 0.83;
if ((sel =="mutau" || sel == "eltau")  && working_point == "MVA_Vloose" )
	SF= 0.84;
if ((sel =="mutau" || sel == "eltau")  && working_point == "MVA_Medium" )
	SF = 0.84;

if ((sel =="mutau" || sel == "eltau")  && working_point == "MVA_Tight" )
	SF = 0.83;

if ((sel =="mutau" || sel == "eltau")  && working_point == "MVA_Vtight" )
	SF = 0.80;



return SF;

}

float Dzeta(TLorentzVector LV, TLorentzVector muV, TLorentzVector MetV)
	{
				float LUnitX = LV.Px()/LV.Pt();
				float LUnitY = LV.Py()/LV.Pt();

				//	cout<<" CHECK =========== "<<tauV.Pt()<<"  "<<ta_pt[tIndex]<<endl;	
				float muonUnitX = muV.Px()/muV.Pt();
				float muonUnitY = muV.Py()/muV.Pt();

				float zetaX = LUnitX + muonUnitX;
				float zetaY = LUnitY + muonUnitY;

				float normZeta = TMath::Sqrt(zetaX*zetaX+zetaY*zetaY);

				zetaX = zetaX/normZeta;
				zetaY = zetaY/normZeta;

				float vectorX = MetV.Px() + muV.Px() + LV.Px();
				float vectorY = MetV.Py() + muV.Py() + LV.Py();

				float vectorVisX = muV.Px() + LV.Px();
				float vectorVisY = muV.Py() + LV.Py();

				// computation of DZeta variable
				// pfmet
				float pzetamiss = MetV.Px()*zetaX + MetV.Py()*zetaY;
				float pzetavis = vectorVisX*zetaX + vectorVisY*zetaY;
				float dzeta = pzetamiss - 0.85*pzetavis;


				return dzeta;
}




vector<string> var;
vector < string > vec;
double var_[1000];

vector<string> CutList;
vector<string> FakeList;
vector<string> FakeListJet;



//TH1::SetDefaultSumw2(true);
TH1D *CutFlow= new TH1D("CutFlow","Cut Flow",CutN,1,CutN+1);

TH1D *CutFlowUnW= new TH1D("CutFlowUnW","Cut Flow",CutN,1,CutN+1);
TH1D *CutFlowUnWLoose= new TH1D("CutFlowUnWLoose","Cut Flow",CutN,1,CutN+1);
TH1D *CutFlowUnWTight= new TH1D("CutFlowUnWTight","Cut Flow",CutN,1,CutN+1);

TH1D *CutFlowUnWFakeRateT[CutF];
TH1D *CutFlowUnWFakeRateL[CutF];
TH1D *CutFlowUnWFakeRateJetL[CutF];
TH1D *CutFlowUnWFakeRateJetT[CutF];
TH1D *CutFlowUnWFakeRate[CutF][nBinsSR];
TH1D *CutFlowUnWFakeRateJet[CutF][nBinsSR];
TH1D *hMETFake[CutN][CutF];
TH1D *hnJetFake[CutN][CutF];
TH1D *hMuptFake[CutN][CutF];
TH1D *hMuetaFake[CutN][CutF];
TH1D *hTauetaFake[CutN][CutF];
TH1D *hTauptFake[CutN][CutF];
TH1D *hIsoMuFake[CutN][CutF];
TH1D *hIsoTauFake[CutN][CutF];
TH1D *hMt2lesterFake[CutN][CutF];
TH1D *hDZetaFake[CutN][CutF];
TH1D *hTauDecayMode1[CutN];
TH1D *hTauDecayMode2[CutN];
TH1D *hTauDecayModeAll[CutN];
TH1D *hMETFB[CutN];
TH1D *hGenMETFB[CutN];

  const int nCuts = 5;
 const int nPtBins = 3;
 const int nPtBins2 = 2;
const  int nEtaBins = 4;

  float ptBins[4] = {20,30,40,1000};
	

  TString PtBins[3] = {
    "Pt20to30",
    "Pt30to40",
    "PtGt40"};//,

  float ptBins2[3] = {20,40,1000};

  TString PtBins2[2] = {
    "Pt20to40",
    "PtGt40"};//,

    float etaBins[5] = {0, 0.8, 1.444, 1.566, 2.3}; 

    TString EtaBins[4] = {"EtaLt0p8",
    "Eta0p8to1p44",
    "Eta1p44to1p566",
    "EtaGt1p566"};


  TH1D * inputEventsH = new TH1D("inputEventsH","",1,-0.5,0.5);
  TH1D * histWeightsH = new TH1D("histWeightsH","",1,-0.5,0.5);
  TH1D *hnpv[nCuts];
  TH1D *hnpu[nCuts];


  TH1D * hxsec = new TH1D("xsec","",1,0,10e+20);

  TH1D * hnJets[CutN];
  TH1D * hnJetsL[CutN];
  TH1D * hnJetsT[CutN];
  TH1D * hnbJets[CutN];
  TH1D * hnbJetsT[CutN];
  TH1D * hnbJetsL[CutN];
  TH1D * hRatioSumL[CutN];
  TH1D * hRatioSumT[CutN];

  TH1D * hMuIsoL[CutN];
  TH1D * hMuIsoT[CutN];
  TH1D * hMTCutL[CutN];
  TH1D * hMTCutT[CutN];
  TH1D * hMRatioSumL[CutN];
  TH1D * hMRatioSumT[CutN];
  TH1D * hDPhiCutL[CutN];
  TH1D * hDPhiCutT[CutN];
  TH1D * hMETCutL[CutN];
  TH1D * hMETCutT[CutN];


  TH1D * hLooseIndex = new TH1D("hLooseIndex","",5,0,5);
  TH1D * hTightIndex = new TH1D("hTightIndex","",5,0,5);





  TString Cuts[5] = {"met","mT","DPhi","metgt40","All"};
  /////first stands for the Eta bin, second array for the cut 
  TH1D * FakeRatePtIncLoose[nEtaBins][nCuts];
  TH1D * FakeRatePtIncTight[nEtaBins][nCuts];

  TH1D * FakeRatePtIncLooseUpQ[nEtaBins][nCuts];
  TH1D * FakeRatePtIncTightUpQ[nEtaBins][nCuts];
  TH1D * FakeRatePtIncLooseDownQ[nEtaBins][nCuts];
  TH1D * FakeRatePtIncTightDownQ[nEtaBins][nCuts];
  TH1D * FakeRatePtIncLooseCharmQ[nEtaBins][nCuts];
  TH1D * FakeRatePtIncTightCharmQ[nEtaBins][nCuts];
  TH1D * FakeRatePtIncLooseStrangeQ[nEtaBins][nCuts];
  TH1D * FakeRatePtIncTightStrangeQ[nEtaBins][nCuts];
  TH1D * FakeRatePtIncLooseGluon[nEtaBins][nCuts];
  TH1D * FakeRatePtIncTightGluon[nEtaBins][nCuts];
  TH1D * FakeRatePtIncLooseBottomQ[nEtaBins][nCuts];
  TH1D * FakeRatePtIncTightBottomQ[nEtaBins][nCuts];
  TH1D * FakeRatePtIncLooseNothing[nEtaBins][nCuts];
  TH1D * FakeRatePtIncTightNothing[nEtaBins][nCuts];



void SetupFakeHist(){
  for (int iEta=0; iEta<nEtaBins; ++iEta) {
    for (int iCut=0; iCut<nCuts; ++iCut) {
    	if (iEta<2){  
      		FakeRatePtIncLoose[iEta][iCut] = new TH1D("FakeRatePtIncLoose"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncTight[iEta][iCut] = new TH1D("FakeRatePtIncTight"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);

      		FakeRatePtIncLooseUpQ[iEta][iCut] = new TH1D("FakeRatePtIncLooseUpQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncTightUpQ[iEta][iCut] = new TH1D("FakeRatePtIncTightUpQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncLooseDownQ[iEta][iCut] = new TH1D("FakeRatePtIncLooseDownQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncTightDownQ[iEta][iCut] = new TH1D("FakeRatePtIncTightDownQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncLooseCharmQ[iEta][iCut] = new TH1D("FakeRatePtIncLooseCharmQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncTightCharmQ[iEta][iCut] = new TH1D("FakeRatePtIncTightCharmQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncLooseStrangeQ[iEta][iCut] = new TH1D("FakeRatePtIncLooseStrangeQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncTightStrangeQ[iEta][iCut] = new TH1D("FakeRatePtIncTightStrangeQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncLooseBottomQ[iEta][iCut] = new TH1D("FakeRatePtIncLooseBottomQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncTightBottomQ[iEta][iCut] = new TH1D("FakeRatePtIncTightBottomQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncLooseGluon[iEta][iCut] = new TH1D("FakeRatePtIncLooseGluon"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncTightGluon[iEta][iCut] = new TH1D("FakeRatePtIncTightGluon"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncLooseNothing[iEta][iCut] = new TH1D("FakeRatePtIncLooseNothing"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);
      		FakeRatePtIncTightNothing[iEta][iCut] = new TH1D("FakeRatePtIncTightNothing"+EtaBins[iEta]+Cuts[iCut],"",nPtBins,ptBins);

	}
  
   	if (iEta>1) {
      		FakeRatePtIncLoose[iEta][iCut] = new TH1D("FakeRatePtIncLoose"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncTight[iEta][iCut] = new TH1D("FakeRatePtIncTight"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);

      		FakeRatePtIncLooseUpQ[iEta][iCut] = new TH1D("FakeRatePtIncLooseUpQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncTightUpQ[iEta][iCut] = new TH1D("FakeRatePtIncTightUpQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncLooseDownQ[iEta][iCut] = new TH1D("FakeRatePtIncLooseDownQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncTightDownQ[iEta][iCut] = new TH1D("FakeRatePtIncTightDownQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncLooseCharmQ[iEta][iCut] = new TH1D("FakeRatePtIncLooseCharmQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncTightCharmQ[iEta][iCut] = new TH1D("FakeRatePtIncTightCharmQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncLooseStrangeQ[iEta][iCut] = new TH1D("FakeRatePtIncLooseStrangeQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncTightStrangeQ[iEta][iCut] = new TH1D("FakeRatePtIncTightStrangeQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncLooseBottomQ[iEta][iCut] = new TH1D("FakeRatePtIncLooseBottomQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncTightBottomQ[iEta][iCut] = new TH1D("FakeRatePtIncTightBottomQ"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncLooseGluon[iEta][iCut] = new TH1D("FakeRatePtIncLooseGluon"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncTightGluon[iEta][iCut] = new TH1D("FakeRatePtIncTightGluon"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncLooseNothing[iEta][iCut] = new TH1D("FakeRatePtIncLooseNothing"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
      		FakeRatePtIncTightNothing[iEta][iCut] = new TH1D("FakeRatePtIncTightNothing"+EtaBins[iEta]+Cuts[iCut],"",nPtBins2,ptBins2);
    		}
    }


  }
}


std::vector<pair<string,float> > variables_;
std::vector<pair<string,float> > variablesMC_;

TTree *T;


void SetupHistsFake(int CutNF){


  for(int cj = 0; cj < CutNF; cj++)
    	{
      TString nCut;
      nCut.Form("%i",cj);
      TString cutName=CutList[cj];
      
     // cout<<" setting histo now "<<"CutFlowUnWFakeRate_"<<nCut<<"_"<<nsr<<endl;

      CutFlowUnWFakeRateL[cj]= new TH1D("CutFlowUnWFakeRateL_"+nCut,"CutFlow",CutNF,1,CutNF+1);
      CutFlowUnWFakeRateT[cj]= new TH1D("CutFlowUnWFakeRateT_"+nCut,"CutFlow",CutNF,1,CutNF+1);
      //CutFlowUnWFakeRateInvert[cj]->SetTitle(cutName);

	int sz = FakeList.size();
	for (int j=0;j<sz;++j){
	TString l_ = FakeList[j].c_str();
	//cout<<" set up "<<FakeList[cj].c_str()<<endl;
       CutFlowUnWFakeRateL[cj]->GetXaxis()->SetBinLabel(j+1,l_);
       CutFlowUnWFakeRateT[cj]->GetXaxis()->SetBinLabel(j+1,l_);
			}

      CutFlowUnWFakeRateJetL[cj]= new TH1D("CutFlowUnWFakeRateJetL_"+nCut,"CutFlow",CutNF,1,CutNF+1);
      CutFlowUnWFakeRateJetT[cj]= new TH1D("CutFlowUnWFakeRateJetT_"+nCut,"CutFlow",CutNF,1,CutNF+1);
      //CutFlowUnWFakeRateJetInvert[cj]->SetTitle(cutName);

	int szz = FakeListJet.size();
	for (int jj=0;jj<szz;++jj){
	TString l_ = FakeListJet[jj].c_str();
//	cout<<" set up "<<FakeListJet[cj].c_str()<<" for "<<nSR<<endl;
       CutFlowUnWFakeRateJetL[cj]->GetXaxis()->SetBinLabel(jj+1,l_);
       CutFlowUnWFakeRateJetT[cj]->GetXaxis()->SetBinLabel(jj+1,l_);
			}
    		}
}



void SetupHists(int CutNer){

for(int cj = 0; cj < CutList.size(); cj++){
      TString cutName=CutList[cj];
      TString nCut;
      nCut.Form("%i",cj);
      TString fCut;
      ///generic variables
     
      CutFlowUnWFakeRateL[cj]= new TH1D("CutFlowUnWFakeRateL_"+nCut,"CutFlow",CutF,1,CutF+1);
      CutFlowUnWFakeRateL[cj]->SetTitle(cutName);
      CutFlowUnWFakeRateT[cj]= new TH1D("CutFlowUnWFakeRateT_"+nCut,"CutFlow",CutF,1,CutF+1);
      CutFlowUnWFakeRateT[cj]->SetTitle(cutName);

	int sz = FakeList.size();
	for (int j=0;j<sz;++j){
	TString l_ = FakeList[j].c_str();
	//cout<<" set up "<<FakeList[cj].c_str()<<"  j "<<j+1<<endl;
	
       CutFlowUnWFakeRateL[cj]->GetXaxis()->SetBinLabel(j+1,l_);
       CutFlowUnWFakeRateT[cj]->GetXaxis()->SetBinLabel(j+1,l_);
			}

      CutFlowUnWFakeRateJetL[cj]= new TH1D("CutFlowUnWFakeRateJetL_"+nCut,"CutFlow",19,1,20);
      CutFlowUnWFakeRateJetL[cj]->SetTitle(cutName);
      CutFlowUnWFakeRateJetT[cj]= new TH1D("CutFlowUnWFakeRateJetT_"+nCut,"CutFlow",19,1,20);
      CutFlowUnWFakeRateJetT[cj]->SetTitle(cutName);

	int szz = FakeListJet.size();
	for (int jj=0;jj<szz;++jj){
	TString l_ = FakeListJet[jj].c_str();
//	cout<<" set up "<<FakeListJet[cj].c_str()<<" for "<<nSR<<endl;
       CutFlowUnWFakeRateJetL[cj]->GetXaxis()->SetBinLabel(jj+1,l_);
       CutFlowUnWFakeRateJetT[cj]->GetXaxis()->SetBinLabel(jj+1,l_);
	}
}

for(int cj = 0; cj < CutNer; cj++)
    {
      CutFlow->GetXaxis()->SetBinLabel(cj+1,CutList[cj].c_str());
      CutFlowUnW->GetXaxis()->SetBinLabel(cj+1,CutList[cj].c_str());
      CutFlowUnWLoose->GetXaxis()->SetBinLabel(cj+1,CutList[cj].c_str());
      CutFlowUnWTight->GetXaxis()->SetBinLabel(cj+1,CutList[cj].c_str());

      TString cutName=CutList[cj];
      TString nCut;
      nCut.Form("%i",cj);
      TString fCut;
      ///generic variables
     

     hnJets[cj] = new TH1D ("nJets_"+nCut,cutName,15,-0.5,14.5);
     hnJets[cj] ->Sumw2();
     hnJetsL[cj] = new TH1D ("nJetsL_"+nCut,cutName,15,-0.5,14.5);
     hnJetsL[cj] ->Sumw2();
     hnJetsT[cj] = new TH1D ("nJetsT_"+nCut,cutName,15,-0.5,14.5);
     hnJetsT[cj] ->Sumw2();
     hnbJets[cj] = new TH1D ("nbJets_"+nCut,cutName,15,-0.5,14.5);
     hnbJets[cj] ->Sumw2();
     hnbJetsL[cj] = new TH1D ("nbJetsL_"+nCut,cutName,15,-0.5,14.5);
     hnbJetsL[cj] ->Sumw2();
     hnbJetsT[cj] = new TH1D ("nbJetsT_"+nCut,cutName,15,-0.5,14.5);
     hnbJetsT[cj] ->Sumw2();

     hMTCutL[cj] = new TH1D ("hMTCutL_"+nCut,cutName,20,0,200);
     hMTCutT[cj] = new TH1D ("hMTCutT_"+nCut,cutName,20,0,200);
     hMTCutL[cj]->Sumw2();
     hMTCutT[cj]->Sumw2();
     
     hRatioSumL[cj] = new TH1D ("hRatioSumL_"+nCut,cutName,10,0,1);
     hRatioSumL[cj]->Sumw2();
     hRatioSumT[cj] = new TH1D ("hRatioSumT_"+nCut,cutName,10,0,1);
     hRatioSumT[cj]->Sumw2();

     hDPhiCutL[cj] = new TH1D ("hDPhiCutL_"+nCut,cutName,70,0,3.5);
     hDPhiCutT[cj] = new TH1D ("hDPhiCutT_"+nCut,cutName,70,0,3.5);

     hDPhiCutL[cj] ->Sumw2();
     hDPhiCutT[cj] ->Sumw2();

     hMETCutL[cj] = new TH1D ("hMETCutL_"+nCut,cutName,10,0,200);
     hMETCutT[cj] = new TH1D ("hMETCutT_"+nCut,cutName,10,0,200);
     hMETCutL[cj]->Sumw2();
     hMETCutT[cj]->Sumw2();

     hMuIsoL[cj] = new TH1D ("hMuIsoL_"+nCut,cutName,20,0,20);
     hMuIsoL[cj]->Sumw2();
     hMuIsoT[cj] = new TH1D ("hMuIsoT_"+nCut,cutName,20,0,20);
     hMuIsoT[cj]->Sumw2();

    }


  TH1D * etaBinsH = new TH1D("etaBinsH", "etaBinsH", nEtaBins, etaBins);
  etaBinsH->GetXaxis()->Set(nEtaBins, etaBins);
  for (int i=0; i<nEtaBins; ++i){ etaBinsH->GetXaxis()->SetBinLabel(i+1, EtaBins[i]);}
  
  TH1D * PtBinsH = new TH1D("PtBinsH", "PtBinsH", nPtBins, ptBins);
  PtBinsH->GetXaxis()->Set(nPtBins, ptBins);
  for (int i=0; i<nPtBins; ++i){ PtBinsH->GetXaxis()->SetBinLabel(i+1, PtBins[i]);}

}




void WriteTree() 

  {
	  T->Print();
	  //T->Write();
	  T->AutoSave();
  }


void FillTree() {

	  T->Fill();
}

