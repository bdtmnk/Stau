// @(#)root/tmva $Id$
/**********************************************************************************
 * Project   : TMVA - a ROOT-integrated toolkit for multivariate data analysis    *
 * Package   : TMVA                                                               *
 * Root Macro: TMVAClassification                                                 *
 *                                                                                *
 * This macro provides examples for the training and testing of the               *
 * TMVA classifiers.                                                              *
 *                                                                                *
 * As input data is used a toy-MC sample consisting of four Gaussian-distributed  *
 * and linearly correlated input variables.                                       *
 *                                                                                *
 * The methods to be used can be switched on and off by means of booleans, or     *
 * via the prompt command, for example:                                           *
 *                                                                                *
 *    root -l ./TMVAClassification.C\(\"Fisher,Likelihood\"\)                     *
 *                                                                                *
 * (note that the backslashes are mandatory)                                      *
 * If no method given, a default set of classifiers is used.                      *
 *                                                                                *
 * The output file "TMVA.root" can be analysed with the use of dedicated          *
 * macros (simply say: root -l <macro.C>), which can be conveniently              *
 * invoked through a GUI that will appear at the end of the run of this macro.    *
 * Launch the GUI via the command:                                                *
 *                                                                                *
 *    root -l ./TMVAGui.C                                                         *
 *                                                                                *
 * You can also compile and run the example with the following commands           *
 *                                                                                *
 *    make                                                                        *
 *    ./TMVAClassification <Methods>                                              *
 *                                                                                *
 * where: <Methods> = "method1 method2"                                           *
 *        are the TMVA classifier names                                           *
 *                                                                                *
 * example:                                                                       *
 *    ./TMVAClassification Fisher LikelihoodPCA BDT                               *
 *                                                                                *
 * If no method given, a default set is of classifiers is used                    *
 **********************************************************************************/

/*
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TString.h>
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
*/


#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <fstream>

#include "TChain.h"
#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TObjString.h"
#include "TSystem.h"
#include "TROOT.h"

#include "TMVA/Factory.h"
#include "TMVA/Tools.h"
#include "TMVA/TMVAGui.h"

//#include "analyzer.h"
#include "/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/interface/functionsSUSY.h"
#include "/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/interface/lester_mt2_bisect.h"
//#include "/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/test/plots.h"

using namespace std;


int N_TMVA(TString myMethodList = "", int NVars = 33, 
		TString outfileName = "TMVA_Test.root",///////// 
		string BDTname = "mutau",/////
		double Sxsec = 1,
		TString Signal = "stau-stau",  
		TString WorkDir = "/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/test/",
		TString channel = "mutau", 
		double EntriesProc = 0.5,
		double EntriesProcTest = 0.5, /// from EntriesProc!!!!!
		bool OnlyPositiveWeights = false,
		string Sdatasets = "datasets"
		)
{
////////////// definition!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  const double muMass = 0.105658367;
  const double tauMass = 1.776;
  const double electronMass = 0.51100e-3;
  const double muonMass = 0.10565837;
  const double pionMass = 0.1396;
  const double bTagCut  = 0.8000;


  // Fixed size dimensions of array or collections stored in the TTree if any.

  // Declaration of leaf types
  Int_t	   nbtag;
  Int_t	   njets;
  Float_t         met_ex;
  Float_t         met_ey;
  Float_t         met_ez;
  Float_t         met_pt;
  Float_t         met_phi;
  Float_t         met_ex_JetEnUp;
  Float_t         met_ey_JetEnUp;
  Float_t         met_ex_JetEnDown;
  Float_t         met_ey_JetEnDown;
  Float_t		met_ex_UnclusteredEnUp;
  Float_t		met_ey_UnclusteredEnUp;
  Float_t		met_ex_UnclusteredEnDown;
  Float_t		met_ey_UnclusteredEnDown;

  Float_t         met_ex_JetEnUp_recoil;
  Float_t         met_ey_JetEnUp_recoil;
  Float_t         met_ex_JetEnDown_recoil;
  Float_t         met_ey_JetEnDown_recoil;
  Float_t         met_ex_UnclusteredEnUp_recoil;
  Float_t         met_ey_UnclusteredEnUp_recoil;
  Float_t         met_ex_UnclusteredEnDown_recoil;
  Float_t         met_ey_UnclusteredEnDown_recoil;
  Float_t         met_ex_recoil;
  Float_t         met_ey_recoil;
  Float_t         genmet;
  Float_t         genmetphi;
  Float_t         met_scaleUp;
  Float_t         metphi_scaleUp;
  Float_t         met_scaleDown;
  Float_t         metphi_scaleDown;
  Float_t         met_resoUp;
  Float_t         met_resoDown;
  Float_t         metphi_resoUp;
  Float_t         metphi_resoDown;

  Float_t         gen_weight;
  Float_t         pu_weight;
  Float_t         LSF_weight;
  Float_t         LSF_weight_el;
  Float_t         LSF_weight_mu;
  Float_t         LSF_weight_2;
  Float_t         LSF_weight_1;
  Float_t         TFR_weight;
  Float_t         top_weight;
  Float_t         all_weight;
  Float_t         trig_weight;
  Float_t         trig_weight_1;
  Float_t         trig_weight_2;
  Float_t         zptmassweight;
  Float_t         xsecs;
  Int_t           muon_index;
  Int_t           muon_index_1;
  Int_t           muon_index_2;
  Int_t           electron_index;
  Int_t           taus_index;
  Int_t           primvert_count;
  Float_t         primvert_x;
  Float_t         primvert_y;
  Float_t         primvert_z;
  Int_t           mu_count;
  Float_t         mu_px[20];
  Float_t         mu_py[20];
  Float_t         mu_pz[20];
  Float_t         mu_pt[20];
  Float_t         mu_eta[20];
  Float_t         mu_phi[20];
  Float_t         mu_charge[20];
  Float_t         mu_miniISO[20];
  Float_t         mu_dxy[20];
  Float_t         mu_dz[20];
  Float_t         mu_dzerr[20];
  Float_t         mu_dxyerr[20];
  Float_t         mu_relIso[20];
		
  Float_t     mu_neutralHadIso[20]; 
  Float_t     mu_photonIso[20]; 
  Float_t     mu_chargedHadIso[20]; 
  Float_t     mu_puIso[20]; 
  Float_t     mu_neutralIso[20];
  Float_t     mu_absIsoMu[20]; 
  Float_t     mu_relIsoMu[20]; 

  Float_t     el_neutralHadIso[20]; 
  Float_t     el_photonIso[20]; 
  Float_t     el_chargedHadIso[20]; 
  Float_t     el_puIso[20]; 
  Float_t     el_neutralIso[20];
  Float_t     el_absIsoEl[20]; 
  Float_t     el_relIsoEl[20]; 
  Float_t     el_isMVA[20]; 
               
  Int_t           jet_count;
  Int_t           npv;
  Int_t           npu;
  Int_t           jets_cleaned[30];
  Float_t         jet_e[30];
  Float_t         jet_px[30];
  Float_t         jet_py[30];
  Float_t         jet_pz[30];
  Float_t         jet_pt[30];
  Float_t         jet_eta[30];
  Float_t         jet_phi[30];
  Float_t         jet_flavour[30];
  Float_t         jet_btag[30];
  Float_t         CFCounter_[30];
  Int_t           jet_isLoose[30];
  Int_t           el_count;
  Float_t         el_px[20];
  Float_t         el_py[20];
  Float_t         el_pz[20];
  Float_t         el_pt[20];
  Float_t         el_eta[20];
  Float_t         el_phi[20];
  Float_t         el_miniISO[20];
  Float_t         el_dxy[20];
  Float_t         el_dxyerr[20];
  Float_t         el_dz[20];
  Float_t         el_dzerr[20];
  Float_t         el_charge[20];
  Float_t         el_relIso[20];
  Int_t           ta_count;
  Float_t         ta_px[30];
  Float_t         ta_py[30];
  Float_t         ta_pz[30];
  Float_t         ta_mass[30];
  Float_t         ta_eta[30];
  Float_t         ta_phi[30];
  Float_t         ta_pt[30];
  Float_t         ta_dxy[30];
  Float_t         ta_dz[30];
  Float_t         ta_charge[30];
  Float_t         ta_relIso[30];
  Float_t         ta_IsoFlag;
  Float_t         event_sign;
  Float_t         met_flag;
  Float_t         event_secondLeptonVeto;
  Float_t         eleMVA;
  Float_t         event_thirdLeptonVeto;
  Float_t         event_leptonDrTrigger;
  //   string 	   datasetName;
  string * datasetName = new std::string(); 
  string          *regionName;

  Float_t 	genTauMatched;
  Float_t 	genLeptonMatched;
  Float_t 	genLeptonMatchedEl;
  Float_t 	genLeptonMatchedMu;
  Float_t 	genTauDecayedMuMatched;
  Float_t 	genTauDecayedElMatched;
  Float_t 	genLeptonPromptElMatched;
  Float_t 	genLeptonPromptMuMatched;
  Float_t         genLeptonMatchedPrompEl;
  Float_t         genLeptonMatchedPrompMu;
  Float_t         genElMatchedToTauDecay;
  Float_t         genMuMatchedToTauDecay;
  Float_t         genTauMatchedToTauDecay;
  Float_t	        genLeptonMatchedPromptEl;
  Float_t	        genLeptonMatchedPromptMu;
  Float_t	        genLeptonMatchedPromptTau;
  Float_t	   genElMatchedHadrDecay;
  Float_t	   genMuMatchedHadrDecay;
  Float_t	   genTauMatchedHadrDecay;
  Float_t	   genLeptonMatchedGluon;
  Float_t	   genLeptonMatchedHFQ;
  Float_t	   genLeptonMatchedLFQ;

  Float_t         matchedTauToPromptEl;
  Float_t         matchedTauToPromptMu;
  Float_t         matchedTauToPromptTau;
  Float_t         matchedTauToTauDecEl;
  Float_t         matchedTauToTauDecMu;
  Float_t         matchedTauToTauDecTau;

  Float_t	   matchedTauToElHadronDec;
  Float_t	   matchedTauToMuHadronDec;
  Float_t	   matchedTauToTauHadronDec;


  Float_t	   qcdweight;
  Float_t	   qcdweightup;
  Float_t	   qcdweightdown;
  Int_t 	   npartons;

  // List of branches
  TBranch        *b_met_ex;   //!
  TBranch        *b_met_ey;   //!
  TBranch        *b_met_ez;   //!
  TBranch        *b_met_pt;   //!
  TBranch        *b_met_phi;   //!
  TBranch        *b_met_ex_JetEnUp;
  TBranch        *b_met_ey_JetEnUp;
  TBranch        *b_met_ex_JetEnDown;
  TBranch        *b_met_ey_JetEnDown;
  TBranch	       *b_met_ex_UnclusteredEnUp;
  TBranch	       *b_met_ey_UnclusteredEnUp;
  TBranch	       *b_met_ex_UnclusteredEnDown;
  TBranch	       *b_met_ey_UnclusteredEnDown;
  TBranch        *b_met_ex_JetEnUp_recoil;
  TBranch        *b_met_ey_JetEnUp_recoil;
  TBranch        *b_met_ex_JetEnDown_recoil;
  TBranch        *b_met_ey_JetEnDown_recoil;
  TBranch	       *b_met_ex_UnclusteredEnUp_recoil;
  TBranch	       *b_met_ey_UnclusteredEnUp_recoil;
  TBranch	       *b_met_ex_UnclusteredEnDown_recoil;
  TBranch	       *b_met_ey_UnclusteredEnDown_recoil;
  TBranch        *b_met_ex_recoil;
  TBranch        *b_met_ey_recoil;
  TBranch        *b_genmet;
  TBranch        *b_genmetphi;
  TBranch        *b_met_scaleUp;
  TBranch        *b_metphi_scaleUp;
  TBranch        *b_met_scaleDown;
  TBranch        *b_metphi_scaleDown;
  TBranch        *b_met_resoUp;
  TBranch        *b_met_resoDown;
  TBranch        *b_metphi_resoUp;
  TBranch        *b_metphi_resoDown;

  TBranch        *b_gen_weight;   //!
  TBranch        *b_pu_weight;   //!
  TBranch        *b_LSF_weight;   //!
  TBranch        *b_LSF_weight_mu;   //!
  TBranch        *b_LSF_weight_el;   //!
  TBranch        *b_LSF_weight_1;   //!
  TBranch        *b_LSF_weight_2;   //!
  TBranch        *b_TFR_weight;   //!
  TBranch        *b_top_weight;   //!
  TBranch        *b_all_weight;   //!
  TBranch        *b_trig_weight;   //!
  TBranch        *b_trig_weight_1;   //!
  TBranch        *b_trig_weight_2;   //!
  TBranch        *b_zptmassweight;   //!
  TBranch        *b_xsecs;   //!
  TBranch        *b_muon_index;   //!
  TBranch        *b_muon_index_1;   //!
  TBranch        *b_muon_index_2;   //!
  TBranch        *b_electron_index;   //!
  TBranch        *b_taus_index;   //!
  TBranch        *b_primvert_count;   //!
  TBranch        *b_primvert_x;   //!
  TBranch        *b_primvert_y;   //!
  TBranch        *b_primvert_z;   //!
  TBranch        *b_mu_count;   //!
  TBranch        *b_mu_px;   //!
  TBranch        *b_mu_py;   //!
  TBranch        *b_mu_pz;   //!
  TBranch        *b_mu_pt;   //!
  TBranch        *b_mu_eta;   //!
  TBranch        *b_mu_phi;   //!
  TBranch        *b_mu_charge;   //!
  TBranch        *b_mu_miniISO;   //!
  TBranch        *b_mu_dxy;   //!
  TBranch        *b_mu_dz;   //!
  TBranch        *b_mu_dxyerr;   //!
  TBranch        *b_mu_dzerr;   //!
  TBranch     *b_mu_neutralHadIso; 
  TBranch     *b_mu_photonIso; 
  TBranch     *b_mu_chargedHadIso; 
  TBranch     *b_mu_puIso; 
  TBranch     *b_mu_neutralIso;
  TBranch     *b_mu_absIsoMu; 
  TBranch     *b_mu_relIsoMu; 

  TBranch     *b_el_neutralHadIso; 
  TBranch     *b_el_photonIso; 
  TBranch     *b_el_chargedHadIso; 
  TBranch     *b_el_puIso; 
  TBranch     *b_el_neutralIso;
  TBranch     *b_el_absIsoEl; 
  TBranch     *b_el_relIsoEl; 
  TBranch     *b_el_isMVA; 
  TBranch        *b_mu_relIso;   //!
  TBranch        *b_jet_count;   //!
  TBranch        *b_npv;   //!
  TBranch        *b_npu;   //!
  TBranch        *b_jets_cleaned;   //!
  TBranch        *b_jet_e;   //!
  TBranch        *b_jet_px;   //!
  TBranch        *b_jet_py;   //!
  TBranch        *b_jet_pz;   //!
  TBranch        *b_jet_pt;   //!
  TBranch        *b_jet_eta;   //!
  TBranch        *b_jet_phi;   //!
  TBranch        *b_jet_flavour;   //!
  TBranch        *b_jet_btag;   //!
  TBranch        *b_jet_isLoose;   //!
  TBranch        *b_el_count;   //!
  TBranch        *b_el_px;   //!
  TBranch        *b_el_py;   //!
  TBranch        *b_el_pz;   //!
  TBranch        *b_el_pt;   //!
  TBranch        *b_el_eta;   //!
  TBranch        *b_el_phi;   //!
  TBranch        *b_el_miniISO;   //!
  TBranch        *b_el_dxy;   //!
  TBranch        *b_el_dz;   //!
  TBranch        *b_el_dxyerr;   //!
  TBranch        *b_el_dzerr;   //!
  TBranch        *b_el_charge;   //!
  TBranch        *b_el_relIso;   //!
  TBranch        *b_ta_count;   //!
  TBranch        *b_ta_px;   //!
  TBranch        *b_ta_py;   //!
  TBranch        *b_ta_pz;   //!
  TBranch        *b_ta_mass;   //!
  TBranch        *b_ta_eta;   //!
  TBranch        *b_ta_phi;   //!
  TBranch        *b_ta_pt;   //!
  TBranch        *b_ta_dxy;   //!
  TBranch        *b_ta_dz;   //!
  TBranch        *b_ta_charge;   //!
  TBranch        *b_ta_IsoFlag;   //!
  TBranch        *b_ta_Iso;   //!
  TBranch        *b_ta_relIso;   //!
  TBranch        *b_datasetName;   //!
  TBranch        *b_CFCounter_;   //!
  TBranch        *b_regionName;   //!
  TBranch        *b_event_sign;   //!
  TBranch        *b_met_flag;   //!
  TBranch        *b_event_secondLeptonVeto;   //!
  TBranch        *b_eleMVA;   //!
  TBranch        *b_event_thirdLeptonVeto;   //!
  TBranch        *b_event_leptonDrTrigger;   //!
  TBranch        *b_genTauMatched;   //!
  TBranch        *b_genLeptonMatched;   //!
  TBranch        *b_genLeptonMatchedEl;   //!
  TBranch        *b_genLeptonMatchedMu;   //!
  TBranch        *b_genTauDecayedMuMatched;   //!
  TBranch        *b_genTauDecayedElMatched;   //!
  TBranch        *b_genLeptonPromptElMatched;   //!
  TBranch        *b_genLeptonPromptMuMatched;   //!
  TBranch        *b_genLeptonMatchedPrompEl;   //!
  TBranch        *b_genLeptonMatchedPrompMu;   //!
  TBranch        *b_genTauMatchedToTauDecay;   //!
  TBranch        *b_matchedTauToPromptEl;   //!
  TBranch        *b_matchedTauToPromptMu;   //!
  TBranch        *b_matchedTauToPromptTau;   //!
  TBranch        *b_matchedTauToTauDecEl;   //!
  TBranch        *b_matchedTauToTauDecMu;   //!
  TBranch        *b_matchedTauToTauDecTau;   //!
  TBranch        *b_matchedTauToElHadronDec;   //!
  TBranch        *b_matchedTauToMuHadronDec;   //!
  TBranch        *b_matchedTauToTauHadronDec;   //!
  TBranch        *b_genLeptonMatchedPromptEl;   //!
  TBranch        *b_genLeptonMatchedPromptMu;   //!
  TBranch        *b_genLeptonMatchedPromptTau;   //!
  TBranch        *b_genElMatchedHadrDecay;   //!
  TBranch        *b_genMuMatchedHadrDecay;   //!
  TBranch        *b_genTauMatchedHadrDecay;   //!
  TBranch        *b_genLeptonMatchedGluon;   //!
  TBranch        *b_genLeptonMatchedLFQ;   //!
  TBranch        *b_genLeptonMatchedHFQ;   //!
  TBranch        *b_genElMatchedToTauDecay;   //!
  TBranch        *b_genMuMatchedToTauDecay;   //!





  TBranch        *b_qcdweight;   //!
  TBranch        *b_qcdweightup;   //!
  TBranch        *b_qcdweightdown;   //!
  TBranch        *b_npartons;   //!
  TBranch        *b_nbtag;   //!
  TBranch        *b_njets;   //!
		
///////////////////////////////////////// END of definition!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111111






   //---------------------------------------------------------------
   // This loads the library
   TMVA::Tools::Instance();
   // Default MVA methods to be trained + tested
   std::map<std::string,int> Use;
   // --- Cut optimisation
   Use["Cuts"]            = 0;
   Use["CutsD"]           = 0;
   Use["CutsPCA"]         = 0;
   Use["CutsGA"]          = 0;
   Use["CutsSA"]          = 0;
   // 
   // --- 1-dimensional likelihood ("naive Bayes estimator")
   Use["Likelihood"]      = 0;
   Use["LikelihoodD"]     = 0; // the "D" extension indicates decorrelated input variables (see option strings)
   Use["LikelihoodPCA"]   = 0; // the "PCA" extension indicates PCA-transformed input variables (see option strings)
   Use["LikelihoodKDE"]   = 0;
   Use["LikelihoodMIX"]   = 0;
   //
   // --- Mutidimensional likelihood and Nearest-Neighbour methods
   Use["PDERS"]           = 0;
   Use["PDERSD"]          = 0;
   Use["PDERSPCA"]        = 0;
   Use["PDEFoam"]         = 0;
   Use["PDEFoamBoost"]    = 0; // uses generalised MVA method boosting
   Use["KNN"]             = 0; // k-nearest neighbour method
   Use["KNNup"]             = 0; // k-nearest neighbour method
   Use["KNNdown"]             = 0; // k-nearest neighbour method
   //
   // --- Linear Discriminant Analysis
   Use["LD"]              = 0; // Linear Discriminant identical to Fisher
   Use["Fisher"]          = 0;
   Use["FisherG"]         = 0;
   Use["BoostedFisher"]   = 0; // uses generalised MVA method boosting
   Use["HMatrix"]         = 0;
   //
   // --- Function Discriminant analysis
   Use["FDA_GA"]          = 0; // minimisation of user-defined function using Genetics Algorithm
   Use["FDA_SA"]          = 0;
   Use["FDA_MC"]          = 0;
   Use["FDA_MT"]          = 0;
   Use["FDA_GAMT"]        = 0;
   Use["FDA_MCMT"]        = 0;
   //
   // --- Neural Networks (all are feed-forward Multilayer Perceptrons)
   Use["MLP"]             = 0; // Recommended ANN
   Use["MLP1"]             = 0; // Recommended ANN
   Use["MLP2"]             = 0; // Recommended ANN
   Use["MLP3"]             = 0; // Recommended ANN
   Use["MLP4"]             = 0; // Recommended ANN
   Use["MLP5"]             = 0; // Recommended ANN
   Use["MLP6"]             = 0; // Recommended ANN
   Use["MLPGA"]             = 0; // Recommended ANN
   Use["MLPGA1"]             = 0; // Recommended ANN
   Use["MLPGA2"]             = 0; // Recommended ANN

   Use["MLPBFGS"]         = 0; // Recommended ANN with optional training method
   Use["MLPBFGS1"]         = 0; // Recommended ANN with optional training method
   Use["MLPBFGS2"]         = 0; // Recommended ANN with optional training method
   Use["MLPBFGS3"]         = 0; // Recommended ANN with optional training method

   Use["MLPBNN"]          = 0; // Recommended ANN with BFGS training method and bayesian regulator
   Use["MLPBNN1"]          = 0; // Recommended ANN with BFGS training method and bayesian regulator
   Use["MLPBNN2"]          = 0; // Recommended ANN with BFGS training method and bayesian regulator
   Use["MLPBNN3"]          = 0; // Recommended ANN with BFGS training method and bayesian regulator
   Use["MLPBNN4"]          = 0; // Recommended ANN with BFGS training method and bayesian regulator
   Use["MLPBNN5"]          = 0; // Recommended ANN with BFGS training method and bayesian regulator
   Use["MLPBNN6"]          = 0; // Recommended ANN with BFGS training method and bayesian regulator
   Use["MLPBNN7"]          = 0; // Recommended ANN with BFGS training method and bayesian regulator
   Use["MLPBNNmoreHiddenLayers"]          = 0; // Recommended ANN with BFGS training method and bayesian regulator


   Use["CFMlpANN"]        = 0; // Depreciated ANN from ALEPH
   Use["TMlpANN"]         = 0; // ROOT's own ANN
   //
   // --- Support Vector Machine 
   Use["SVM"]             = 0;

   Use["SVM1"]             = 0;
   Use["SVM2"]             = 0;
   Use["SVM3"]             = 0;
   Use["SVM4"]             = 0;

   // 
   // --- Boosted Decision Trees
   Use["BDT"]             = 0; // uses Adaptive Boost
   Use["BDT"+BDTname]             = 1; // uses Adaptive Boost
//   Use["BDTmutau"]             = 0; // uses Adaptive Boost
//   Use["BDTeltau"]             = 0; // uses Adaptive Boost
//   Use["BDTmuel"]             = 0; // uses Adaptive Boost
   Use["BDT1"]             = 0; // uses Adaptive Boost
   Use["BDT2"]             = 0; // uses Adaptive Boost
   Use["BDT3"]             = 0; // uses Adaptive Boost
   Use["BDT4"]             = 0; // uses Adaptive Boost
   Use["BDT5"]             = 0; // uses Adaptive Boost
   Use["BDT6"]             = 0; // uses Adaptive Boost
   Use["BDT7"]             = 0; // uses Adaptive Boost
   Use["BDT8"]             = 0; // uses Adaptive Boost

   Use["BDTG"]            = 0; // uses Gradient Boost
   Use["BDTB"]            = 0; // uses Bagging
   Use["BDTD"]            = 0; // decorrelation + Adaptive Boost
   Use["BDTF"]            = 0; // allow usage of fisher discriminant for node splitting 
   // 
   // --- Friedman's RuleFit method, ie, an optimised series of cuts ("rules")
   Use["RuleFit"]         = 0;
   // ---------------------------------------------------------------

   std::cout << std::endl;
   std::cout << "==> Start TMVAClassification" << std::endl;

   // Select methods (don't look at this code - not of interest)
   if (myMethodList != "") {
      for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) it->second = 0;

      std::vector<TString> mlist = TMVA::gTools().SplitString( myMethodList, ',' );
      for (UInt_t i=0; i<mlist.size(); i++) {
         std::string regMethod(mlist[i]);

         if (Use.find(regMethod) == Use.end()) {
            std::cout << "Method \"" << regMethod << "\" not known in TMVA under this name. Choose among the following:" << std::endl;
            for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) std::cout << it->first << " ";
            std::cout << std::endl;
            return 1;
         }
         Use[regMethod] = 1;
      }
   }

   // --------------------------------------------------------------------------------------------------

   // --- Here the preparation phase begins

   // Create a ROOT output file where TMVA will store ntuples, histograms, etc.
   //TString outfileName( "TMVA_NEwStauSampleNewVariablesTestMoreCuts.root" );
   TFile* outputFile = TFile::Open( outfileName, "RECREATE" );

   // Create the factory object. Later you can choose the methods
   // whose performance you'd like to investigate. The factory is 
   // the only TMVA object you have to interact with
   //
   // The first argument is the base of the name of all the
   // weightfiles in the directory weight/
   //
   // The second argument is the output file for the training results
   // All TMVA output can be suppressed by removing the "!" (not) in
   // front of the "Silent" argument in the option string


   //TMVA::Factory *factory = new TMVA::Factory( "myTMVA", outputFile,
//                                               "!V:!Silent:Color:DrawProgressBar:Transformations=I;D;P;G,D:AnalysisType=Classification" );

   TMVA::Factory *factory = new TMVA::Factory( "myTMVA", outputFile,
                                               "!V:!Silent:Color:DrawProgressBar:Transformations=I");

   // If you wish to modify default settings
   // (please check "src/Config.h" to see all available global options)
   //    (TMVA::gConfig().GetVariablePlotting()).fTimesRMS = 8.0;
   //    (TMVA::gConfig().GetIONames()).fWeightFileDir = "myWeightDirectory";

   // Define the input variables that shall be used for the MVA training
   // note that you may also use variable expressions, such as: "3*var1/var2*abs(var3)"
   // [all types of expressions that can also be parsed by ttree::draw( "expression" )]
if (NVars>=1)	factory->AddVariable("MTsum","MTsum","units",'F');
if (NVars>=2)	factory->AddVariable("MTtotal","MTtotal","units",'F');
if (NVars>=3)	factory->AddVariable("Dr","Dr","units",'F');
if (NVars>=4)	factory->AddVariable("LeptV2Pt","LeptV2Pt","units",'F');
if (NVars>=5)	factory->AddVariable("DiLM","DiLM","units",'F');
if (NVars>=6)	factory->AddVariable("Mcta","Mcta","units",'F');
if (NVars>=7)	factory->AddVariable("MT2as","MT2as","units",'F');
if (NVars>=8)	factory->AddVariable("MTmin","MTmin","units",'F');
if (NVars>=9)	factory->AddVariable("METPt","METPt","units",'F');
if (NVars>=10)	factory->AddVariable("HText","HText","units",'F');
if (NVars>=11)	factory->AddVariable("Dzeta","Dzeta","units",'F');
if (NVars>=12)	factory->AddVariable("Meff","Meff","units",'F');
if (NVars>=13)	factory->AddVariable("MTmax","MTmax","units",'F');
if (NVars>=14)	factory->AddVariable("RHT","RHT","units",'F');
if (NVars>=15)	factory->AddVariable("MTdif","MTdif","units",'F');
if (NVars>=16)	factory->AddVariable("HTOsqrtMET","HTOsqrtMET","units",'F');
if (NVars>=17)	factory->AddVariable("MT","MT","units",'F');
if (NVars>=18)	factory->AddVariable("LeptV1Pt","LeptV1Pt","units",'F');
if (NVars>=19)	factory->AddVariable("HT","HT","units",'F');
if (NVars>=20)	factory->AddVariable("PtOHT","PtOHT","units",'F');
if (NVars>=21)	factory->AddVariable("dEtaLeptV1LeptV2","dEtaLeptV1LeptV2","units",'F');
if (NVars>=22)	factory->AddVariable("dEtaJ0LeptV1","dEtaJ0LeptV1","units",'F');
if (NVars>=23)	factory->AddVariable("dEtaJ0LeptV2","dEtaJ0LeptV2","units",'F');
if (NVars>=24)	factory->AddVariable("dPhiLeptV1LeptV2","dPhiLeptV1LeptV2","units",'F');
if (NVars>=25)	factory->AddVariable("dPhiJ0LeptV1","dPhiJ0LeptV1","units",'F');
if (NVars>=26)	factory->AddVariable("dPhiJ0LeptV2","dPhiJ0LeptV2","units",'F');
if (NVars>=27)	factory->AddVariable("LeptV1Eta","LeptV1Eta","units",'F');
if (NVars>=28)	factory->AddVariable("LeptV2Eta","LeptV2Eta","units",'F');
if (NVars>=29)	factory->AddVariable("JetEta","JetEta","units",'F');
if (NVars>=30)	factory->AddVariable("LeptV2Phi","LeptV2Phi","units",'F');
if (NVars>=31)	factory->AddVariable("LeptV1Phi","LeptV1Phi","units",'F');
if (NVars>=32)	factory->AddVariable("JetPhi","JetPhi","units",'F');
if (NVars>=33)	factory->AddVariable("njets","njets","units",'I');









///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// FILLING



	ifstream datasets;
	datasets.open(Sdatasets);



	cout.setf(ios::fixed, ios::floatfield);
	cout.setf(ios::showpoint);
	string name;
	TString name2;
	TString name3;
	TString treeName;
	TString nameinputEventsH;
	int CutNumb;	
	TH1D *hist[50];
	int i = 0;


	string SE ="SingleElectron";
	string SM ="SingleMuon";
	string MuonEG ="MuonEG";
	string QCDs ="QCD";
	string Tau ="Tau";
	string stau ="stau";
	string TT ="TT_Tune";
	string WJ ="JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM";
	string DY ="DY";
	string W0J ="WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM";
	string DY0J ="DYJetsToLL_M-50";	
	double xsec;
	double SumOfWeights;	
	double Lumi = 35800;
	//double TTscale = 0.925;
	//double WJscale = 0.84;
	double QCDscale = 2;
	double MCweight = 1;



	TString inputRootFile = "/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/data/HIP_mediumID.root";
	TFile * fileInHIP = new TFile(inputRootFile, "read");

	TGraphAsymmErrors * TGr_hip;
	TGr_hip = new TGraphAsymmErrors();
	TGr_hip = (TGraphAsymmErrors*)fileInHIP->Get("ratio_eta");


	TString inputRootFile2 = "/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/data/sf_mu_medium.root";

	TFile * fileInFast = new TFile(inputRootFile2, "read");


	TIter nextkey (fileInFast->GetListOfKeys ());
	TKey *key = 0;
	key = (TKey *) nextkey ();
	TObject *obj = key->ReadObj ();
	TH2D *histo = (TH2D*) obj;

	TLorentzVector  ElV;
	TLorentzVector  MuV;
	TLorentzVector  TauV;
	TLorentzVector  JetsV;
	TLorentzVector  LeptV1;
	TLorentzVector  LeptV2;
	TLorentzVector  METV;
	vector<TLorentzVector> JetsMV;

TH1D *hMt2lestermutau = new TH1D ("Mt2lestermutauFB_","Mt2lestermutau ",100,2,302);


	int NselectedEv;
	string line;
   	 while(getline(datasets, line))
		{
		istringstream iss(line); // access line as a stream
		double xs,fact,fact2;
		xs=1;fact=1;fact2=1;
		iss >> name >> xs >> fact >> fact2;



		name2 = WorkDir+channel+"/"+name+"_B_OS.root";
		string HHname = name;	
		if (std::string::npos != HHname.find(stau)) name2 = WorkDir+channel+"/"+name+".root";
		if (std::string::npos != HHname.find(stau) && Sxsec < 0.9) {name2 = WorkDir+channel+"/stau-"+Signal+".root"; name=Signal;HHname=Signal;xs=Sxsec;}
       		cout << i << endl;
       		cout << name << endl; 
		name3 = name;
		//treeName = "tree"+name;
    		cout << name2 << endl;
		TFile * name3 = new TFile(name2);
		name3->cd(channel);

		TH1D * histWeightsH = (TH1D*)name3->Get(channel+"/histWeightsH");
		TTree *treeName = (TTree*)name3->Get(channel+"/T");


		xsec = xs*fact*fact2;
		SumOfWeights = histWeightsH->GetSumOfWeights();
		cout << "SumOfWeights = " << SumOfWeights << endl;
		cout << "xsec " << xsec<< endl;
		cout << "xsec*Lumi = " << xsec*Lumi << endl;
		cout << "norm  "<< xsec*Lumi/SumOfWeights << endl;
		MCweight = xsec*Lumi/SumOfWeights;
		//if (std::string::npos != HHname.find(TT)) {MCweight *=TTscale; }
		//if (std::string::npos != HHname.find(WJ)) {MCweight *=WJscale; }
		//////////////////////////////////////////////////////////////////////////////////////BAD waY!!!!!!!!!!!!!!!!!!!!!!!1

    treeName->SetBranchAddress("met_ex", &met_ex, &b_met_ex);
  treeName->SetBranchAddress("met_ey", &met_ey, &b_met_ey);
  treeName->SetBranchAddress("met_ez", &met_ez, &b_met_ez);
  treeName->SetBranchAddress("met_pt", &met_pt, &b_met_pt);
  treeName->SetBranchAddress("met_phi", &met_phi, &b_met_phi);
  treeName->SetBranchAddress("met_ex_recoil", &met_ex_recoil, &b_met_ex_recoil);
  treeName->SetBranchAddress("met_ey_recoil", &met_ey_recoil, &b_met_ey_recoil);
  treeName->SetBranchAddress("genmet", &genmet, &b_genmet);
  treeName->SetBranchAddress("genmetphi", &genmetphi, &b_genmetphi);
  treeName->SetBranchAddress("met_scaleUp", &met_scaleUp, &b_met_scaleUp);
  treeName->SetBranchAddress("met_scaleDown", &met_scaleDown, &b_met_scaleDown);
  treeName->SetBranchAddress("metphi_scaleUp", &metphi_scaleUp, &b_metphi_scaleUp);
  treeName->SetBranchAddress("metphi_scaleDown", &metphi_scaleDown, &b_metphi_scaleDown);
  treeName->SetBranchAddress("met_resoUp", &met_resoUp, &b_met_resoUp);
  treeName->SetBranchAddress("met_resoDown", &met_resoDown, &b_met_resoDown);
  treeName->SetBranchAddress("metphi_resoUp", &metphi_resoUp, &b_metphi_resoUp);
  treeName->SetBranchAddress("metphi_resoDown", &metphi_resoDown, &b_metphi_resoDown);


  treeName->SetBranchAddress("met_ex_JetEnUp_recoil", &met_ex_JetEnUp_recoil, &b_met_ex_JetEnUp_recoil);
  treeName->SetBranchAddress("met_ey_JetEnUp_recoil", &met_ey_JetEnUp_recoil, &b_met_ey_JetEnUp_recoil);

  treeName->SetBranchAddress("met_ex_JetEnDown_recoil", &met_ex_JetEnDown_recoil, &b_met_ex_JetEnDown_recoil);
  treeName->SetBranchAddress("met_ey_JetEnDown_recoil", &met_ey_JetEnDown_recoil, &b_met_ey_JetEnDown_recoil);

  treeName->SetBranchAddress("met_ex_UnclusteredEnDown_recoil", &met_ex_UnclusteredEnDown_recoil, &b_met_ex_UnclusteredEnDown_recoil);
  treeName->SetBranchAddress("met_ey_UnclusteredEnDown_recoil", &met_ey_UnclusteredEnDown_recoil, &b_met_ey_UnclusteredEnDown_recoil);

  treeName->SetBranchAddress("met_ex_UnclusteredEnUp_recoil", &met_ex_UnclusteredEnUp_recoil, &b_met_ex_UnclusteredEnUp_recoil);
  treeName->SetBranchAddress("met_ey_UnclusteredEnUp_recoil", &met_ey_UnclusteredEnUp_recoil, &b_met_ey_UnclusteredEnUp_recoil);

  treeName->SetBranchAddress("met_ex_JetEnUp", &met_ex_JetEnUp, &b_met_ex_JetEnUp);
  treeName->SetBranchAddress("met_ey_JetEnUp", &met_ey_JetEnUp, &b_met_ey_JetEnUp);

  treeName->SetBranchAddress("met_ex_JetEnDown", &met_ex_JetEnDown, &b_met_ex_JetEnDown);
  treeName->SetBranchAddress("met_ey_JetEnDown", &met_ey_JetEnDown, &b_met_ey_JetEnDown);

  treeName->SetBranchAddress("met_ex_UnclusteredEnDown", &met_ex_UnclusteredEnDown, &b_met_ex_UnclusteredEnDown);
  treeName->SetBranchAddress("met_ey_UnclusteredEnDown", &met_ey_UnclusteredEnDown, &b_met_ey_UnclusteredEnDown);

  treeName->SetBranchAddress("met_ex_UnclusteredEnUp", &met_ex_UnclusteredEnUp, &b_met_ex_UnclusteredEnUp);
  treeName->SetBranchAddress("met_ey_UnclusteredEnUp", &met_ey_UnclusteredEnUp, &b_met_ey_UnclusteredEnUp);



  treeName->SetBranchAddress("gen_weight", &gen_weight, &b_gen_weight);
  treeName->SetBranchAddress("pu_weight", &pu_weight, &b_pu_weight);
  treeName->SetBranchAddress("LSF_weight", &LSF_weight, &b_LSF_weight);
  treeName->SetBranchAddress("LSF_weight_mu", &LSF_weight_mu, &b_LSF_weight_mu);
  treeName->SetBranchAddress("LSF_weight_el", &LSF_weight_el, &b_LSF_weight_el);
  treeName->SetBranchAddress("LSF_weight_1", &LSF_weight_1, &b_LSF_weight_1);
  treeName->SetBranchAddress("LSF_weight_2", &LSF_weight_2, &b_LSF_weight_2);
  treeName->SetBranchAddress("TFR_weight", &TFR_weight, &b_TFR_weight);
  treeName->SetBranchAddress("top_weight", &top_weight, &b_top_weight);
  treeName->SetBranchAddress("all_weight", &all_weight, &b_all_weight);
  treeName->SetBranchAddress("trig_weight", &trig_weight, &b_trig_weight);
  treeName->SetBranchAddress("trig_weight_1", &trig_weight_1, &b_trig_weight_1);
  treeName->SetBranchAddress("trig_weight_2", &trig_weight_2, &b_trig_weight_2);
  treeName->SetBranchAddress("zptmassweight", &zptmassweight, &b_zptmassweight);
  treeName->SetBranchAddress("xsecs", &xsecs, &b_xsecs);
  treeName->SetBranchAddress("muon_index", &muon_index, &b_muon_index);
  treeName->SetBranchAddress("muon_index_1", &muon_index_1, &b_muon_index_1);
  treeName->SetBranchAddress("muon_index_2", &muon_index_2, &b_muon_index_2);
  treeName->SetBranchAddress("electron_index", &electron_index, &b_electron_index);
  treeName->SetBranchAddress("taus_index", &taus_index, &b_taus_index);
  treeName->SetBranchAddress("primvert_count", &primvert_count, &b_primvert_count);
  treeName->SetBranchAddress("primvert_x", &primvert_x, &b_primvert_x);
  treeName->SetBranchAddress("primvert_y", &primvert_y, &b_primvert_y);
  treeName->SetBranchAddress("primvert_z", &primvert_z, &b_primvert_z);
  treeName->SetBranchAddress("mu_count", &mu_count, &b_mu_count);
  treeName->SetBranchAddress("mu_px", mu_px, &b_mu_px);
  treeName->SetBranchAddress("mu_py", mu_py, &b_mu_py);
  treeName->SetBranchAddress("mu_pz", mu_pz, &b_mu_pz);
  treeName->SetBranchAddress("mu_pt", mu_pt, &b_mu_pt);
  treeName->SetBranchAddress("mu_eta", mu_eta, &b_mu_eta);
  treeName->SetBranchAddress("mu_phi", mu_phi, &b_mu_phi);
  treeName->SetBranchAddress("mu_charge", mu_charge, &b_mu_charge);
  treeName->SetBranchAddress("mu_miniISO", mu_miniISO, &b_mu_miniISO);
  treeName->SetBranchAddress("mu_dxy", mu_dxy, &b_mu_dxy);
  treeName->SetBranchAddress("mu_dz", mu_dz, &b_mu_dz);
  treeName->SetBranchAddress("mu_dxyerr", mu_dxyerr, &b_mu_dxyerr);
  treeName->SetBranchAddress("mu_dzerr", mu_dzerr, &b_mu_dzerr);


  treeName->SetBranchAddress("mu_neutralHadIso", mu_neutralHadIso, &b_mu_neutralHadIso);
  treeName->SetBranchAddress("mu_photonIso", mu_photonIso, &b_mu_photonIso);
  treeName->SetBranchAddress("mu_chargedHadIso", mu_chargedHadIso, &b_mu_chargedHadIso);
  treeName->SetBranchAddress("mu_puIso", mu_puIso, &b_mu_puIso);
  treeName->SetBranchAddress("mu_neutralIso", mu_neutralIso, &b_mu_neutralIso);
  treeName->SetBranchAddress("mu_absIsoMu", mu_absIsoMu, &b_mu_absIsoMu);
  treeName->SetBranchAddress("mu_relIsoMu", mu_relIsoMu, &b_mu_relIsoMu);
  treeName->SetBranchAddress("el_neutralHadIso", el_neutralHadIso, &b_el_neutralHadIso);
  treeName->SetBranchAddress("el_photonIso", el_photonIso, &b_el_photonIso);
  treeName->SetBranchAddress("el_chargedHadIso", el_chargedHadIso, &b_el_chargedHadIso);
  treeName->SetBranchAddress("el_puIso", el_puIso, &b_el_puIso);
  treeName->SetBranchAddress("el_neutralIso", el_neutralIso, &b_el_neutralIso);
  treeName->SetBranchAddress("el_absIsoEl", el_absIsoEl, &b_el_absIsoEl);
  treeName->SetBranchAddress("el_relIsoEl", el_relIsoEl, &b_el_relIsoEl);
  treeName->SetBranchAddress("el_isMVA", el_isMVA, &b_el_isMVA);


  treeName->SetBranchAddress("mu_relIso", mu_relIso, &b_mu_relIso);
  treeName->SetBranchAddress("jet_count", &jet_count, &b_jet_count);
  treeName->SetBranchAddress("npv", &npv, &b_npv);
  treeName->SetBranchAddress("npu", &npu, &b_npu);
  treeName->SetBranchAddress("jets_cleaned", &jets_cleaned, &b_jets_cleaned);
  treeName->SetBranchAddress("njets", &njets, &b_njets);
  treeName->SetBranchAddress("jet_e", jet_e, &b_jet_e);
  treeName->SetBranchAddress("jet_px", jet_px, &b_jet_px);
  treeName->SetBranchAddress("jet_py", jet_py, &b_jet_py);
  treeName->SetBranchAddress("jet_pz", jet_pz, &b_jet_pz);
  treeName->SetBranchAddress("jet_pt", jet_pt, &b_jet_pt);
  treeName->SetBranchAddress("jet_eta", jet_eta, &b_jet_eta);
  treeName->SetBranchAddress("jet_phi", jet_phi, &b_jet_phi);
  treeName->SetBranchAddress("jet_flavour", jet_flavour, &b_jet_flavour);
  treeName->SetBranchAddress("jet_btag", jet_btag, &b_jet_btag);
  treeName->SetBranchAddress("jet_isLoose", jet_isLoose, &b_jet_isLoose);


  treeName->SetBranchAddress("el_count", &el_count, &b_el_count);
  treeName->SetBranchAddress("el_px", el_px, &b_el_px);
  treeName->SetBranchAddress("el_py", el_py, &b_el_py);
  treeName->SetBranchAddress("el_pz", el_pz, &b_el_pz);
  treeName->SetBranchAddress("el_pt", el_pt, &b_el_pt);
  treeName->SetBranchAddress("el_eta", el_eta, &b_el_eta);
  treeName->SetBranchAddress("el_phi", el_phi, &b_el_phi);
  treeName->SetBranchAddress("el_miniISO", el_miniISO, &b_el_miniISO);
  treeName->SetBranchAddress("el_dxy", el_dxy, &b_el_dxy);
  treeName->SetBranchAddress("el_dz", el_dz, &b_el_dz);
  treeName->SetBranchAddress("el_dxyerr", el_dxyerr, &b_el_dxyerr);
  treeName->SetBranchAddress("el_dzerr", el_dzerr, &b_el_dzerr);
  treeName->SetBranchAddress("el_charge", el_charge, &b_el_charge);
  treeName->SetBranchAddress("el_relIso", el_relIso, &b_el_relIso);


  treeName->SetBranchAddress("ta_count", &ta_count, &b_ta_count);
  treeName->SetBranchAddress("ta_px", ta_px, &b_ta_px);
  treeName->SetBranchAddress("ta_py", ta_py, &b_ta_py);
  treeName->SetBranchAddress("ta_pz", ta_pz, &b_ta_pz);
  treeName->SetBranchAddress("ta_mass", ta_mass, &b_ta_mass);
  treeName->SetBranchAddress("ta_eta", ta_eta, &b_ta_eta);
  treeName->SetBranchAddress("ta_phi", ta_phi, &b_ta_phi);
  treeName->SetBranchAddress("ta_pt", ta_pt, &b_ta_pt);
  treeName->SetBranchAddress("ta_dxy", ta_dxy, &b_ta_dxy);
  treeName->SetBranchAddress("ta_dz", ta_dz, &b_ta_dz);
  treeName->SetBranchAddress("ta_charge", ta_charge, &b_ta_charge);
  treeName->SetBranchAddress("ta_IsoFlag", &ta_IsoFlag, &b_ta_IsoFlag);
  treeName->SetBranchAddress("ta_relIso", ta_relIso, &b_ta_relIso);

  treeName->SetBranchAddress("datasetName", &datasetName);

  treeName->SetBranchAddress("CFCounter_", CFCounter_,&b_CFCounter_);

  //treeName->SetBranchAddress("regionName", &regionName, &b_regionName);

  treeName->SetBranchAddress("event_sign", &event_sign, &b_event_sign);

  treeName->SetBranchAddress("met_flag", &met_flag, &b_met_flag);


  treeName->SetBranchAddress("eleMVA", &eleMVA, &b_eleMVA);


  treeName->SetBranchAddress("event_secondLeptonVeto", &event_secondLeptonVeto, &b_event_secondLeptonVeto);
  treeName->SetBranchAddress("event_thirdLeptonVeto", &event_thirdLeptonVeto, &b_event_thirdLeptonVeto);
  treeName->SetBranchAddress("event_leptonDrTrigger", &event_leptonDrTrigger, &b_event_leptonDrTrigger);


  treeName->SetBranchAddress("genTauMatched", &genTauMatched, &b_genTauMatched);
  treeName->SetBranchAddress("genLeptonMatched", &genLeptonMatched, &b_genLeptonMatched);
  treeName->SetBranchAddress("genLeptonMatchedEl", &genLeptonMatchedEl, &b_genLeptonMatchedEl);
  treeName->SetBranchAddress("genLeptonMatchedMu", &genLeptonMatchedMu, &b_genLeptonMatchedMu);
  treeName->SetBranchAddress("genTauDecayedMuMatched", &genTauDecayedMuMatched, &b_genTauDecayedMuMatched);
  treeName->SetBranchAddress("genTauDecayedElMatched", &genTauDecayedElMatched, &b_genTauDecayedElMatched);
  treeName->SetBranchAddress("genLeptonPromptElMatched", &genLeptonPromptElMatched, &b_genLeptonPromptElMatched);
  treeName->SetBranchAddress("genLeptonPromptMuMatched", &genLeptonPromptMuMatched, &b_genLeptonPromptMuMatched);


  treeName->SetBranchAddress("genLeptonMatchedPromptEl", &genLeptonMatchedPromptMu, &b_genLeptonMatchedPromptEl);
  treeName->SetBranchAddress("genLeptonMatchedPromptMu", &genLeptonMatchedPromptMu, &b_genLeptonMatchedPromptMu);
  //			treeName->SetBranchAddress("genLeptonMatchedPromptTau", &genLeptonMatchedPromptMu, &b_genLeptonMatchedPromptTau);



  treeName->SetBranchAddress("genLeptonMatchedPrompEl", &genLeptonMatchedPrompEl, &b_genLeptonMatchedPrompEl);
  treeName->SetBranchAddress("genLeptonMatchedPrompMu", &genLeptonMatchedPrompMu, &b_genLeptonMatchedPrompMu);
  treeName->SetBranchAddress("genElMatchedToTauDecay", &genElMatchedToTauDecay, &b_genElMatchedToTauDecay);
  treeName->SetBranchAddress("genMuMatchedToTauDecay", &genMuMatchedToTauDecay, &b_genMuMatchedToTauDecay);
  treeName->SetBranchAddress("genTauMatchedToTauDecay", &genTauMatchedToTauDecay, &b_genTauMatchedToTauDecay);
  treeName->SetBranchAddress("matchedTauToPromptEl", &matchedTauToPromptEl, &b_matchedTauToPromptEl);
  treeName->SetBranchAddress("matchedTauToPromptMu", &matchedTauToPromptMu, &b_matchedTauToPromptMu);
  treeName->SetBranchAddress("matchedTauToPromptTau", &matchedTauToPromptTau, &b_matchedTauToPromptTau);
  treeName->SetBranchAddress("matchedTauToTauDecEl", &matchedTauToTauDecEl, &b_matchedTauToTauDecEl);
  treeName->SetBranchAddress("matchedTauToTauDecMu", &matchedTauToTauDecMu, &b_matchedTauToTauDecMu);
  treeName->SetBranchAddress("matchedTauToTauDecTau", &matchedTauToTauDecTau, &b_matchedTauToTauDecTau);
  treeName->SetBranchAddress("matchedTauToElHadronDec", &matchedTauToElHadronDec, &b_matchedTauToElHadronDec);
  treeName->SetBranchAddress("matchedTauToMuHadronDec", &matchedTauToMuHadronDec, &b_matchedTauToMuHadronDec);
  treeName->SetBranchAddress("matchedTauToTauHadronDec", &matchedTauToTauHadronDec, &b_matchedTauToTauHadronDec);
  treeName->SetBranchAddress("genLeptonMatchedGluon", &genLeptonMatchedGluon, &b_genLeptonMatchedGluon);
  treeName->SetBranchAddress("genLeptonMatchedLFQ", &genLeptonMatchedLFQ, &b_genLeptonMatchedLFQ);
  treeName->SetBranchAddress("genLeptonMatchedHFQ", &genLeptonMatchedHFQ, &b_genLeptonMatchedHFQ);




			
  treeName->SetBranchAddress("qcdweight", &qcdweight, &b_qcdweight);
  treeName->SetBranchAddress("qcdweightup", &qcdweightup, &b_qcdweightup);
  treeName->SetBranchAddress("qcdweightdown", &qcdweightdown, &b_qcdweightdown);
  treeName->SetBranchAddress("nbtag", &nbtag, &b_nbtag);

  treeName->SetBranchAddress("npartons",&npartons,&b_npartons);




		//////////////////////////////////////////////////////////////////////////////////////End of BAD waY!!!!!!!!!!!!!!!!!!!!!!!1
		NselectedEv =0;
		//if (std::string::npos != HHname.find(stau)) EntriesProc=1;
		for (UInt_t i=0; i<(EntriesProc*treeName->GetEntries()); i++) {           		treeName->GetEntry(i);

			double all_weights = 1.;
			JetsV.SetPxPyPzE(0.,0.,0.,0.);
			MuV.SetPxPyPzE(0.,0.,0.,0.);
			ElV.SetPxPyPzE(0.,0.,0.,0.);
			TauV.SetPxPyPzE(0.,0.,0.,0.);
			double dEta;
			JetsMV.clear();
		

			if(muon_index>-1 && muon_index<8)			MuV.SetPtEtaPhiM(mu_pt[muon_index], mu_eta[muon_index], mu_phi[muon_index], muonMass);
			if(electron_index>-1 && electron_index<8)		ElV.SetPtEtaPhiM(el_pt[electron_index], el_eta[electron_index], el_phi[electron_index],electronMass);
			if (taus_index>-1 && taus_index<8)			TauV.SetPtEtaPhiM(ta_pt[taus_index], ta_eta[taus_index], ta_phi[taus_index], tauMass);
			for (int nj=0;nj<njets;++nj) {JetsV.SetPxPyPzE(jet_px[jets_cleaned[nj]], jet_py[jets_cleaned[nj]],jet_pz[jets_cleaned[nj]],jet_e[jets_cleaned[nj]]);
			JetsMV.push_back(JetsV);}

			METV.SetPx(met_ex);
			METV.SetPy(met_ey);
			met = sqrt(met_ex*met_ex + met_ey*met_ey);
			
			if (std::string::npos != HHname.find(WJ) || std::string::npos != HHname.find(DY)) 
			{
				METV.SetPx(met_ex_recoil);
				METV.SetPy(met_ey_recoil);
				met=sqrt(met_ex_recoil*met_ex_recoil+met_ey_recoil*met_ey_recoil);
			}

			if (channel == "mutau") {LeptV1 = MuV; LeptV2 = TauV;}
			if (channel == "eltau") {LeptV1 = ElV; LeptV2 = TauV;}
			if (channel == "muel") {LeptV1 = MuV; LeptV2 = ElV;}
//cout <<"V1 and V2  !!!   "<< LeptV1.Pt() <<"  "<< 	LeptV2.Pt() <<"  "<< TauV.Pt()<<endl;		

			if (std::string::npos != HHname.find(W0J) && (npartons>0 && npartons<5)) continue;
	
			if (std::string::npos != HHname.find(DY0J) && (npartons>0 && npartons<5)) continue;

			if (abs(mu_count) > 8 || abs(el_count) > 8 || abs(ta_count) >8) continue;

			all_weights = pu_weight * gen_weight;
			if (OnlyPositiveWeights && gen_weight>0) all_weights = pu_weight;
			if (OnlyPositiveWeights && gen_weight<0) continue;
                 	double Dr=deltaR(LeptV1.Eta(), LeptV1.Phi(),
					LeptV2.Eta(),LeptV2.Phi());
		///// iso cut.....
			if (mu_relIso[0] > 0.15 &&  channel == "mutau") continue;
			if (el_relIso[0] > 0.1 && channel == "eltau") continue;
			if ((el_relIso[0] > 0.1 || mu_relIso[0] > 0.15) && channel == "muel") continue;
			if (Dr>3.5) continue;
		//////////
//cout<<i <<endl;
		double charge_;
		if (channel == "mutau")
			{
			if ( fabs(mu_dz[muon_index]) > 0.2) continue;
			if ( fabs(mu_dxy[muon_index]) > 0.045) continue;
			if ( fabs(mu_charge[muon_index]) !=1 ) continue;
			if ( fabs(ta_charge[taus_index]) !=1 ) continue;
			 charge_ =mu_charge[muon_index]  * ta_charge[taus_index];
			if (event_secondLeptonVeto >0.5) continue;
			}

		if (channel == "eltau")
			{
			if ( fabs(el_dz[electron_index]) > 0.2) continue;
			if ( fabs(el_dxy[electron_index]) > 0.045) continue;
			if ( fabs(el_charge[electron_index]) !=1 ) continue;
			if ( fabs(ta_charge[taus_index]) !=1 ) continue;
			 charge_ =el_charge[electron_index]  * ta_charge[taus_index];
			if (event_secondLeptonVeto >0.5) continue;
			}

		if (channel == "muel")
			{
			if ( fabs(mu_charge[muon_index]) !=1 ) continue;
			if ( fabs(el_charge[electron_index]) !=1 ) continue;
			 charge_ =mu_charge[muon_index]  * el_charge[electron_index];
			if (event_secondLeptonVeto >0.5) continue;
			}



			if ( charge_ > 0.) continue;
			if (event_thirdLeptonVeto >0.5) continue;   ////////////???????? zdes' zakocnchil


		if (channel == "muel") {double trigw =   ( 17677*trig_weight_1 +   18188 * trig_weight_2)/double(35865.) ;
					all_weights *= trigw;}
		else{all_weights *= trig_weight;}
			all_weights *= LSF_weight;
			// end of baseline selection
			if (njets>1.5) continue;
			if (nbtag!=0) continue;
         		double MT, dPhi;
		 	TLorentzVector DiL;


		

		if (channel == "eltau" || channel == "mutau")
			{
		 	DiL = LeptV1  ;
			dPhi=dPhiFrom2P( DiL.Px(), DiL.Py(), METV.Px(),  METV.Py() );
			MT = 0;MT=sqrt(2*DiL.Pt()*METV.Pt()*(1-TMath::Cos(dPhi)));

			if (MT > 60. && MT < 120. ) continue;
			if (MT < 20.) continue;
			}



		if (channel == "muel") 
			{
		 	DiL = LeptV1 + LeptV2 ;
			if (DiL.M() > 30. && DiL.M() < 90. ) continue;
			if (DiL.M() > 250.) continue;
			}


			dPhi=dPhiFrom2P( LeptV1.Px(), LeptV1.Py(), METV.Px(),  METV.Py() );		
			MT = TMath::Sqrt(2*LeptV1.Pt()*METV.Pt()*(1-TMath::Cos(dPhi)));


			dPhi=dPhiFrom2P( LeptV2.Px(), LeptV2.Py(), METV.Px(),  METV.Py() );
			double MTt = TMath::Sqrt(2*LeptV2.Pt()*METV.Pt()*(1-TMath::Cos(dPhi)));
			double MTsum = MT+MTt;
			double mttotal = sqrt(MT*MT + MTt*MTt);
			double deta=deltaEta(LeptV1.Px(),  LeptV1.Py(),LeptV1.Pz(), LeptV2.Px(),  LeptV2.Py(),LeptV2.Pz() );
			//double Dr = MuV.DeltaR(TauV);
			//cout <<"Dr      "<< Dr<< endl;

			//// additional cuts for mutau channel!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!			dEta = LeptV1.Eta() - LeptV2.Eta();
			double dEtaJMu = -1.; if (JetsMV.size()>0) dEtaJMu = JetsMV.at(0).Eta() - LeptV1.Eta();
			double dEtaJTau = -1.; if (JetsMV.size()>0) dEtaJTau = JetsMV.at(0).Eta() - LeptV2.Eta();
               		double Dr2=-1; if  (JetsMV.size()>0) {Dr2=deltaR(JetsMV.at(0).Eta(),JetsMV.at(0).Phi(), LeptV2.Eta(),LeptV2.Phi());}
			double dPhiDiL=dPhiFrom2P( LeptV1.Px(), LeptV1.Py(), LeptV2.Px(),  LeptV2.Py() );
			/// DZETA calculation
				double tauUnitX = LeptV2.Px()/LeptV2.Pt();
				double tauUnitY = LeptV2.Py()/LeptV2.Pt();

				double muonUnitX = LeptV1.Px()/LeptV1.Pt();
				double muonUnitY = LeptV1.Py()/LeptV1.Pt();

				double zetaX = tauUnitX + muonUnitX;
				double zetaY = tauUnitY + muonUnitY;

				double normZeta = TMath::Sqrt(zetaX*zetaX+zetaY*zetaY);

				zetaX = zetaX/normZeta;
				zetaY = zetaY/normZeta;

				double vectorVisX = LeptV1.Px() + LeptV2.Px();
				double vectorVisY = LeptV1.Py() + LeptV2.Py();

				// computation of DZeta variable
				// pfmet
				double pzetamiss = METV.Px()*zetaX + METV.Py()*zetaY;
				double pzetavis = vectorVisX*zetaX + vectorVisY*zetaY;
				double dzeta = pzetamiss - 0.85*pzetavis;

				DiL = LeptV1  + LeptV2;
				double mcta = sqrt( 2*LeptV1.Pt()*LeptV2.Pt()*(1+cos(LeptV1.Phi()-LeptV2.Phi())) );
				double Mt2as = 0; 
				if (channel == "mutau") Mt2as = asymm_mt2_lester_bisect::get_mT2(muonMass, MuV.Px(), MuV.Py(),tauMass,TauV.Px(),TauV.Py(),METV.Px(),METV.Py(),0,0,0);
      				if (channel == "eltau") Mt2as = asymm_mt2_lester_bisect::get_mT2(electronMass, ElV.Px(), ElV.Py(),tauMass,TauV.Px(),TauV.Py(),METV.Px(),METV.Py(),0,0,0);
				if (channel == "muel") Mt2as = asymm_mt2_lester_bisect::get_mT2(muonMass, MuV.Px(), MuV.Py(),electronMass,ElV.Px(),ElV.Py(),METV.Px(),METV.Py(),0,0,0);

    double sumpT=0;

    if (JetsMV.size()>0) {for (unsigned int ij=0;ij<JetsMV.size();ij++){
      //sumpT+=jet_pt[ij];
      sumpT+=JetsMV.at(ij).Pt();
      //double dPhiJ=dPhiFrom2P( jet_px[ij], jet_py[ij], MetV.Px(),  MetV.Py() );
    }}
	double HTOsqrMET;
	if (METV.Pt()>0. )
       HTOsqrMET= (sumpT/sqrt(METV.Pt()));
	dEta = LeptV1.Eta() - LeptV2.Eta();
	double HT = sumpT;
	double HText = HT ; 
			if ((channel=="mutau"&&muon_index != -1) || (channel=="eltau"&& electron_index !=-1) )    HText += LeptV1.Pt();
			if (channel=="muel" && electron_index !=-1 &&  muon_index !=-1) HText += LeptV1.Pt()+LeptV2.Pt();
				double v1[4] = {ElV.Px(),ElV.Py(),ElV.Pz(),electronMass};
				double v2[4] = {TauV.Px(),TauV.Py(),TauV.Pz(),tauMass};
				double ecm = 13000.0;
				double mxlo = 0;
				double ptm[2] = {METV.Px(),METV.Py()};
				double vds[4] = {0,0,0,0};
	
	double MCTCorr = mctcorr(v1,v2,vds,ptm,ecm,mxlo);
	double MCTmutau = mct(v1,v2);
	double MCTxmutau = mcx(v1,v2,vds,ptm);
	double MCTymutau = mcy(v1,v2,vds,ptm);
//	double MTBoundmutau = Lester::mTBound(MuV.M(), MuV.Px(), MuV.Py(), MuV.Pz(), tauMass,TauV.Px(),TauV.Py(),TauV.Pz(),METV.Px(),METV.Py(), mintermediate);
//	double MTTruemutau = Lester::mTTrue(MuV.M(), MuV.Px(), MuV.Py(), MuV.Pz(), tauMass,TauV.Px(),TauV.Py(),TauV.Pz(),METV.Px(),METV.Py(), mintermediate);
	double MTdif = fabs(MT-MTt);
	double MTmax = max(MT,MTt);
	double MTmin = min(MT,MTt);
	double Mueta = MuV.Eta();
	double Taueta = TauV.Eta();
	double Rht = 0;
	double PtOHT = 0;


			if ((channel=="mutau" && muon_index !=-1 && JetsMV.size()>0)||(channel=="eltau" && electron_index !=-1 && JetsMV.size()>0)) 
					{ Rht=LeptV1.Pt()/HText;PtOHT = LeptV1.Pt()/HT;}
			if (channel=="muel" && electron_index !=-1 && muon_index !=-1 && JetsMV.size()>0) 				  	     {	 Rht=(LeptV1.Pt()+LeptV2.Pt())/HText;PtOHT = (LeptV1.Pt()+LeptV2.Pt())/HT;}
		double dEtaJ0LeptV1=0,dEtaJ0LeptV2=0,dPhiJ0LeptV1=0,dPhiJ0LeptV2=0,dEtaJ0MET=0,dPhiJ0MET=0, JetEta=0, JetPhi=0;
		if(	JetsMV.size()>0)
	{
		dEtaJ0LeptV1 = LeptV1.Eta()-JetsMV.at(0).Eta();
		dEtaJ0LeptV2 = LeptV2.Eta()-JetsMV.at(0).Eta();
		dPhiJ0LeptV1 = dPhiFrom2P( JetsMV.at(0).Px(), JetsMV.at(0).Py(), LeptV1.Px(),  LeptV1.Py() );
		dPhiJ0LeptV2 = dPhiFrom2P( JetsMV.at(0).Px(), JetsMV.at(0).Py(), LeptV2.Px(),  LeptV2.Py() );
		dEtaJ0MET = JetsMV.at(0).Eta()-METV.Eta();
		dPhiJ0MET = dPhiFrom2P(JetsMV.at(0).Px(), JetsMV.at(0).Py(),METV.Px(),METV.Py());
		JetEta = JetsMV.at(0).Eta();
		JetPhi = JetsMV.at(0).Phi();
	};
		double Meff = LeptV1.Pt()+HT+LeptV2.Pt()+METV.Pt();		
		double dEtaLeptV1MET = LeptV1.Eta() - METV.Eta();
		double dEtaLeptV2MET = LeptV2.Eta() - METV.Eta();
		double dEtaLeptV1LeptV2 = LeptV1.Eta() - LeptV2.Eta();
		double dPhiLeptV1LeptV2 = dPhiFrom2P( LeptV1.Px(),  LeptV1.Py(), LeptV2.Px(),  LeptV2.Py()  );
		double dPhiLeptV1MET = dPhiFrom2P( LeptV1.Px(),  LeptV1.Py(), METV.Px(),  METV.Py()  );
		double dPhiLeptV2MET = dPhiFrom2P( LeptV2.Px(),  LeptV2.Py(), METV.Px(),  METV.Py()  );
if (std::string::npos != HHname.find(stau)) hMt2lestermutau->Fill(Mt2as,MCweight*all_weights);
		vector<Double_t> vars(NVars); 
/* 1st order

	vars[0] = MTtotal;
	vars[1] = MTsum;
	vars[2] = MTmax;
	vars[3] = Meff;
	vars[4] = MET.Pt();
	vars[5] = Dil.M();
	vars[6] = MTdif;
	vars[7] = LeptV2.Pt();
	vars[8] = dzeta;
	vars[9] = LeptV1.Pt();
	vars[10] = MT2as;
	vars[11] = HText;
	vars[12] = MT;
	vars[13] = mcta;
	vars[14] = MTmin;
	vars[15] = dPhiLeptV1MET;
	vars[16] = dPhiLeptV2MET;
	vars[17] = dPhiLeptV1LeptV2;
	vars[18] = Dr;
	vars[19] = Rht;
	vars[20] = PtOHT;
	vars[21] = HTOsqrMET;
	vars[22] = HT;
	vars[23] = dPhiJ0LeptV1;
	vars[24] = dPhiJ0LeptV2;
	vars[25] = dEtaJ0LeptV2;
	vars[26] = dEtaJ0LeptV1;
	vars[27] = dPhiJ0MET;
	vars[28] = Jet.Eta();
	vars[29] = Jet.Phi();
	vars[30] = njets;
	vars[31] = METV.Phi();
	vars[32] = LeptV2.Eta();
	vars[33] = LeptV2.Phi();
	vars[34] = LeptV1.Eta();
	vars[35] = LeptV1.Phi();
	vars[36] = dEtaLeptV1LeptV2;

 */ 
if(NVars>0)	vars[0]=MTsum;
if(NVars>1)	vars[1]=mttotal;
if(NVars>2)	vars[2]=Dr;
if(NVars>3)	vars[3]=LeptV2.Pt();
if(NVars>4)	vars[4]=DiL.M();
if(NVars>5)	vars[5]=mcta;
if(NVars>6)	vars[6]=Mt2as;
if(NVars>7)	vars[7]=MTmin;
if(NVars>8)	vars[8]=METV.Pt();
if(NVars>9)	vars[9]=HText;
if(NVars>10)	vars[10]=dzeta;
if(NVars>11)	vars[11]=Meff;
if(NVars>12)	vars[12]=MTmax;
if(NVars>13)	vars[13]=Rht;
if(NVars>14)	vars[14]=MTdif;
if(NVars>15)	vars[15]=HTOsqrMET;
if(NVars>16)	vars[16]=MT;
if(NVars>17)	vars[17]=LeptV1.Pt();
if(NVars>18)	vars[18]=HT;
if(NVars>19)	vars[19]=PtOHT;
if(NVars>20)	vars[20]=dEtaLeptV1LeptV2;
if(NVars>21)	vars[21]=dEtaJ0LeptV1;
if(NVars>22)	vars[22]=dEtaJ0LeptV2;
if(NVars>23)	vars[23]=dPhiLeptV1LeptV2;
if(NVars>24)	vars[24]=dPhiJ0LeptV1;
if(NVars>25)	vars[25]=dPhiJ0LeptV2;
if(NVars>26)	vars[26]=LeptV1.Eta();
if(NVars>27)	vars[27]=LeptV2.Eta();
if(NVars>28)	vars[28]=JetEta;
if(NVars>29)	vars[30]=LeptV2.Phi();
if(NVars>30)	vars[31]=LeptV1.Phi();
if(NVars>31)	vars[32]=JetPhi;
if(NVars>32)	vars[33]=njets;







			NselectedEv++;
			if (std::string::npos != HHname.find(stau))
				{
				
           			if (i < (EntriesProc*treeName->GetEntries())*(1-EntriesProcTest)) factory->AddSignalTrainingEvent( vars, MCweight*all_weights );
				//factory->AddSignalTrainingEvent( vars, 0.25*MCweight*all_weights );
           			else factory->AddSignalTestEvent( vars, MCweight*all_weights );
				//factory->AddSignalTestEvent( vars, 0.25*MCweight*all_weights );
				if (MCweight*all_weights >1) {
				cout << NselectedEv <<endl; 
				cout << MCweight*all_weights <<endl; 
				cout << MCweight <<endl; 
				cout << all_weights <<endl; }
				}
			else
				{
           			if (i < (EntriesProc*treeName->GetEntries())*(1-EntriesProcTest)) factory->AddBackgroundTrainingEvent( vars, MCweight*all_weights );
           			else factory->AddBackgroundTestEvent( vars, MCweight*all_weights );
        			}
		}

		cout << "N selected events = " << NselectedEv <<endl;

		i++;
    		}


	
    	datasets.close();
/*
    TCanvas* canv3 = new TCanvas("c3", "c3");
    hMt2lestermutau->Draw("sameh");
    canv3->Print("hMt2lestermutau2.pdf");
*/
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 	END FILLING



   // Apply additional cuts on the signal and background samples (can be different)
   TCut mycuts = ""; // for example: TCut mycuts = "abs(var1)<0.5 && abs(var2-0.5)<1";
   TCut mycutb = ""; // for example: TCut mycutb = "abs(var1)<0.5";


   // Tell the factory how to use the training and testing events
   //
   // If no numbers of events are given, half of the events in the tree are used 
   // for training, and the other half for testing:
       factory->PrepareTrainingAndTestTree( mycuts, "" );
   // To also specify the number of testing events, use:
   //    factory->PrepareTrainingAndTestTree( mycut,
   //                                         "NSigTrain=3000:NBkgTrain=3000:NSigTest=3000:NBkgTest=3000:SplitMode=Random:!V" );
   //factory->PrepareTrainingAndTestTree( mycuts, mycutb);

   // ---- Book MVA methods
   //
   // Please lookup the various method configuration options in the corresponding cxx files, eg:
   // src/MethoCuts.cxx, etc, or here: http://tmva.sourceforge.net/optionRef.html
   // it is possible to preset ranges in the option string in which the cut optimisation should be done:
   // "...:CutRangeMin[2]=-1:CutRangeMax[2]=1"...", where [2] is the third input variable

   // Cut optimisation
   if (Use["Cuts"])
      factory->BookMethod( TMVA::Types::kCuts, "Cuts",
                           "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart" );

   if (Use["CutsD"])
      factory->BookMethod( TMVA::Types::kCuts, "CutsD",
                           "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart:VarTransform=Decorrelate" );

   if (Use["CutsPCA"])
      factory->BookMethod( TMVA::Types::kCuts, "CutsPCA",
                           "!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart:VarTransform=PCA" );

   if (Use["CutsGA"])
      factory->BookMethod( TMVA::Types::kCuts, "CutsGA",
                           "H:!V:FitMethod=GA:CutRangeMin[0]=-10:CutRangeMax[0]=10:VarProp[1]=FMax:EffSel:Steps=30:Cycles=3:PopSize=400:SC_steps=10:SC_rate=5:SC_factor=0.95" );

   if (Use["CutsSA"])
      factory->BookMethod( TMVA::Types::kCuts, "CutsSA",
                           "!H:!V:FitMethod=SA:EffSel:MaxCalls=150000:KernelTemp=IncAdaptive:InitialTemp=1e+6:MinTemp=1e-6:Eps=1e-10:UseDefaultScale" );

   // Likelihood ("naive Bayes estimator")
   if (Use["Likelihood"])
      factory->BookMethod( TMVA::Types::kLikelihood, "Likelihood",""
                           /*"H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmoothBkg[1]=10:NSmooth=1:NAvEvtPerBin=50"*/ );

   // Decorrelated likelihood
   if (Use["LikelihoodD"])
      factory->BookMethod( TMVA::Types::kLikelihood, "LikelihoodD",
                           "!H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmooth=5:NAvEvtPerBin=50:VarTransform=Decorrelate" );

   // PCA-transformed likelihood
   if (Use["LikelihoodPCA"])
      factory->BookMethod( TMVA::Types::kLikelihood, "LikelihoodPCA",
                           "!H:!V:!TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmooth=5:NAvEvtPerBin=50:VarTransform=PCA" ); 

   // Use a kernel density estimator to approximate the PDFs
   if (Use["LikelihoodKDE"])
      factory->BookMethod( TMVA::Types::kLikelihood, "LikelihoodKDE",
                           "!H:!V:!TransformOutput:PDFInterpol=KDE:KDEtype=Gauss:KDEiter=Adaptive:KDEFineFactor=0.3:KDEborder=None:NAvEvtPerBin=50" ); 

   // Use a variable-dependent mix of splines and kernel density estimator
   if (Use["LikelihoodMIX"])
      factory->BookMethod( TMVA::Types::kLikelihood, "LikelihoodMIX",
                           "!H:!V:!TransformOutput:PDFInterpolSig[0]=KDE:PDFInterpolBkg[0]=KDE:PDFInterpolSig[1]=KDE:PDFInterpolBkg[1]=KDE:PDFInterpolSig[2]=Spline2:PDFInterpolBkg[2]=Spline2:PDFInterpolSig[3]=Spline2:PDFInterpolBkg[3]=Spline2:KDEtype=Gauss:KDEiter=Nonadaptive:KDEborder=None:NAvEvtPerBin=50" ); 

   // Test the multi-dimensional probability density estimator
   // here are the options strings for the MinMax and RMS methods, respectively:
   //      "!H:!V:VolumeRangeMode=MinMax:DeltaFrac=0.2:KernelEstimator=Gauss:GaussSigma=0.3" );
   //      "!H:!V:VolumeRangeMode=RMS:DeltaFrac=3:KernelEstimator=Gauss:GaussSigma=0.3" );
   if (Use["PDERS"])
      factory->BookMethod( TMVA::Types::kPDERS, "PDERS",
                           "!H:!V:NormTree=T:VolumeRangeMode=Adaptive:KernelEstimator=Gauss:GaussSigma=0.3:NEventsMin=400:NEventsMax=600" );

   if (Use["PDERSD"])
      factory->BookMethod( TMVA::Types::kPDERS, "PDERSD",
                           "!H:!V:VolumeRangeMode=Adaptive:KernelEstimator=Gauss:GaussSigma=0.3:NEventsMin=400:NEventsMax=600:VarTransform=Decorrelate" );

   if (Use["PDERSPCA"])
      factory->BookMethod( TMVA::Types::kPDERS, "PDERSPCA",
                           "!H:!V:VolumeRangeMode=Adaptive:KernelEstimator=Gauss:GaussSigma=0.3:NEventsMin=400:NEventsMax=600:VarTransform=PCA" );

   // Multi-dimensional likelihood estimator using self-adapting phase-space binning
   if (Use["PDEFoam"])
      factory->BookMethod( TMVA::Types::kPDEFoam, "PDEFoam",
                           "!H:!V:SigBgSeparate=F:TailCut=0.001:VolFrac=0.0666:nActiveCells=500:nSampl=2000:nBin=5:Nmin=100:Kernel=None:Compress=T" );

   if (Use["PDEFoamBoost"])
      factory->BookMethod( TMVA::Types::kPDEFoam, "PDEFoamBoost",
                           "!H:!V:Boost_Num=30:Boost_Transform=linear:SigBgSeparate=F:MaxDepth=4:UseYesNoCell=T:DTLogic=MisClassificationError:FillFoamWithOrigWeights=F:TailCut=0:nActiveCells=500:nBin=20:Nmin=400:Kernel=None:Compress=T" );

   // K-Nearest Neighbour classifier (KNN)///////////////////////////////////1111111111111111111111111111111111111111111111111111111111111111111111111111111111
   if (Use["KNN"])
      factory->BookMethod( TMVA::Types::kKNN, "KNN",
                           "H:nkNN=20:ScaleFrac=0.8:SigmaFact=1.0:Kernel=Gaus:UseKernel=F:UseWeight=T:!Trim" );

   if (Use["KNNdown"])
      factory->BookMethod( TMVA::Types::kKNN, "KNNdown",
                           "H:nkNN=10:ScaleFrac=0.8:SigmaFact=1.0:Kernel=Gaus:UseKernel=F:UseWeight=T:!Trim" );


   if (Use["KNNup"])
      factory->BookMethod( TMVA::Types::kKNN, "KNNup",
                           "H:nkNN=40:ScaleFrac=0.8:SigmaFact=1.0:Kernel=Gaus:UseKernel=F:UseWeight=T:!Trim" );

   // H-Matrix (chi2-squared) method
   if (Use["HMatrix"])
      factory->BookMethod( TMVA::Types::kHMatrix, "HMatrix", "!H:!V:VarTransform=None" );

   // Linear discriminant (same as Fisher discriminant)
   if (Use["LD"])
      factory->BookMethod( TMVA::Types::kLD, "LD", "H:!V:VarTransform=None:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=50:NsmoothMVAPdf=10" );

   // Fisher discriminant (same as LD)
   if (Use["Fisher"])
      factory->BookMethod( TMVA::Types::kFisher, "Fisher", "H:!V:Fisher:VarTransform=None:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=50:NsmoothMVAPdf=10" );

   // Fisher with Gauss-transformed input variables
   if (Use["FisherG"])
      factory->BookMethod( TMVA::Types::kFisher, "FisherG", "H:!V:VarTransform=Gauss" );

   // Composite classifier: ensemble (tree) of boosted Fisher classifiers
   if (Use["BoostedFisher"])
      factory->BookMethod( TMVA::Types::kFisher, "BoostedFisher", 
                           "H:!V:Boost_Num=20:Boost_Transform=log:Boost_Type=AdaBoost:Boost_AdaBoostBeta=0.2:!Boost_DetailedMonitoring" );

   // Function discrimination analysis (FDA) -- test of various fitters - the recommended one is Minuit (or GA or SA)
   if (Use["FDA_MC"])
      factory->BookMethod( TMVA::Types::kFDA, "FDA_MC",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=MC:SampleSize=100000:Sigma=0.1" );

   if (Use["FDA_GA"]) // can also use Simulated Annealing (SA) algorithm (see Cuts_SA options])
      factory->BookMethod( TMVA::Types::kFDA, "FDA_GA",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=GA:PopSize=300:Cycles=3:Steps=20:Trim=True:SaveBestGen=1" );

   if (Use["FDA_SA"]) // can also use Simulated Annealing (SA) algorithm (see Cuts_SA options])
      factory->BookMethod( TMVA::Types::kFDA, "FDA_SA",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=SA:MaxCalls=15000:KernelTemp=IncAdaptive:InitialTemp=1e+6:MinTemp=1e-6:Eps=1e-10:UseDefaultScale" );

   if (Use["FDA_MT"])
      factory->BookMethod( TMVA::Types::kFDA, "FDA_MT",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=MINUIT:ErrorLevel=1:PrintLevel=-1:FitStrategy=2:UseImprove:UseMinos:SetBatch" );

   if (Use["FDA_GAMT"])
      factory->BookMethod( TMVA::Types::kFDA, "FDA_GAMT",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=GA:Converger=MINUIT:ErrorLevel=1:PrintLevel=-1:FitStrategy=0:!UseImprove:!UseMinos:SetBatch:Cycles=1:PopSize=5:Steps=5:Trim" );

   if (Use["FDA_MCMT"])
      factory->BookMethod( TMVA::Types::kFDA, "FDA_MCMT",
                           "H:!V:Formula=(0)+(1)*x0+(2)*x1+(3)*x2+(4)*x3:ParRanges=(-1,1);(-10,10);(-10,10);(-10,10);(-10,10):FitMethod=MC:Converger=MINUIT:ErrorLevel=1:PrintLevel=-1:FitStrategy=0:!UseImprove:!UseMinos:SetBatch:SampleSize=20" );

   // TMVA ANN: MLP (recommended ANN) -- all ANNs in TMVA are Multilayer Perceptrons
   if (Use["MLP"])
      factory->BookMethod( TMVA::Types::kMLP, "MLP");      
	//factory->BookMethod( TMVA::Types::kMLP, "MLP", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=50:!UseRegulator" );

   if (Use["MLP1"])
      //factory->BookMethod( TMVA::Types::kMLP, "MLP1", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5" );
      factory->BookMethod( TMVA::Types::kMLP, "MLP1", "H:!V:NeuronType=sigmoid:VarTransform=N:NCycles=1700:HiddenLayers=N+5,N:TestRate=5:UseRegulator" );


   if (Use["MLP2"])
      //factory->BookMethod( TMVA::Types::kMLP, "MLP2", "H:!V:NeuronType=tanh:VarTransform=N,G,D:NCycles=600:HiddenLayers=N+5:TestRate=5:!UseRegulator" );
      factory->BookMethod( TMVA::Types::kMLP, "MLP2", "H:!V:NeuronType=sigmoid:VarTransform=N:NCycles=2000:HiddenLayers=N+5,N:TestRate=5:UseRegulator" );

   if (Use["MLP3"])
      factory->BookMethod( TMVA::Types::kMLP, "MLP3", "H:!V:NeuronType=sigmoid:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:!UseRegulator" );

   if (Use["MLP4"])
      factory->BookMethod( TMVA::Types::kMLP, "MLP4", "H:!V:NeuronType=sigmoid:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:UseRegulator" );

   if (Use["MLP5"])
      factory->BookMethod( TMVA::Types::kMLP, "MLP5", "H:!V:NeuronType=sigmoid:VarTransform=N:NCycles=600:HiddenLayers=N+5,N:TestRate=5:UseRegulator" );

   if (Use["MLP6"])
      factory->BookMethod( TMVA::Types::kMLP, "MLP6", "H:!V:NeuronType=sigmoid:VarTransform=N:NCycles=1000:HiddenLayers=N+5,N:TestRate=5:UseRegulator" );

   if (Use["MLPGA"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPGA", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:TrainingMethod=GA" );

   if (Use["MLPGA1"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPGA", "H:!V:NeuronType=sigmoid:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:TrainingMethod=GA:UseRegulator" );

   if (Use["MLPGA2"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPGA", "H:!V:NeuronType=sigmoid:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:TrainingMethod=GA:!UseRegulator" );





   if (Use["MLPBFGS"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPBFGS", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:TrainingMethod=BFGS:!UseRegulator" );

   if (Use["MLPBFGS1"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPBFGS1", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=1000:HiddenLayers=N+5:TestRate=5:TrainingMethod=BFGS:!UseRegulator" );

   if (Use["MLPBFGS2"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPBFGS2", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5,N:TestRate=5:TrainingMethod=BFGS:!UseRegulator" );

   if (Use["MLPBFGS3"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPBFGS3", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=1000:HiddenLayers=N+5,N:TestRate=5:TrainingMethod=BFGS:!UseRegulator" );




   if (Use["MLPBNN"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPBNN", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5:TestRate=5:TrainingMethod=BFGS:UseRegulator" ); // BFGS training with bayesian regulators

   if (Use["MLPBNN1"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPBNN1", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=1000:HiddenLayers=N+5:TestRate=5:TrainingMethod=BFGS:UseRegulator" ); // BFGS training with bayesian regulators

   if (Use["MLPBNN2"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPBNN2", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=600:HiddenLayers=N+5,N:TestRate=5:TrainingMethod=BFGS:UseRegulator" ); // BFGS training with bayesian regulators

   if (Use["MLPBNN3"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPBNN3", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=1000:HiddenLayers=N+5,N:TestRate=5:TrainingMethod=BFGS:UseRegulator" ); // BFGS training with bayesian regulators

   if (Use["MLPBNN4"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPBNN4", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=1500:HiddenLayers=N+5,N:TestRate=5:TrainingMethod=BFGS:UseRegulator" ); // BFGS training with bayesian regulators

   if (Use["MLPBNN5"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPBNN5", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=2000:HiddenLayers=N+5,N:TestRate=5:TrainingMethod=BFGS:UseRegulator" ); // BFGS training with bayesian regulators

   if (Use["MLPBNN6"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPBNN6", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=2500:HiddenLayers=N+5,N:TestRate=5:TrainingMethod=BFGS:UseRegulator" ); // BFGS training with bayesian regulators

   if (Use["MLPBNN7"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPBNN7", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=3000:HiddenLayers=N+5,N:TestRate=5:TrainingMethod=BFGS:UseRegulator" ); // BFGS training with bayesian regulators


   if (Use["MLPBNNmoreHiddenLayers"])
      factory->BookMethod( TMVA::Types::kMLP, "MLPBNNmoreHiddenLayers", "H:!V:NeuronType=tanh:VarTransform=N:NCycles=1000:HiddenLayers=N+5,N,N:TestRate=5:TrainingMethod=BFGS:UseRegulator" ); // BFGS training with bayesian regulators







   // CF(Clermont-Ferrand)ANN
   if (Use["CFMlpANN"])
      factory->BookMethod( TMVA::Types::kCFMlpANN, "CFMlpANN", "!H:!V:NCycles=2000:HiddenLayers=N+1,N"  ); // n_cycles:#nodes:#nodes:...  

   // Tmlp(Root)ANN
   if (Use["TMlpANN"])
      factory->BookMethod( TMVA::Types::kTMlpANN, "TMlpANN", "!H:!V:NCycles=200:HiddenLayers=N+1,N:LearningMethod=BFGS:ValidationFraction=0.3"  ); // n_cycles:#nodes:#nodes:...

   // Support Vector Machine///////////////////////////////////1111111111111111111111111111111111111111111111111111111111111111111111111111111111
   if (Use["SVM"])
      factory->BookMethod( TMVA::Types::kSVM, "SVM", "Gamma=0.25:Tol=0.001:VarTransform=Norm:MaxIter=2000" );

   if (Use["SVM1"])
      factory->BookMethod( TMVA::Types::kSVM, "SVM1", "Gamma=1:Tol=0.001:VarTransform=Norm:MaxIter=2000" );

   if (Use["SVM2"])
      factory->BookMethod( TMVA::Types::kSVM, "SVM2", "Gamma=0.25:Tol=0.01:VarTransform=Norm:MaxIter=2000" );

   if (Use["SVM3"])
      factory->BookMethod( TMVA::Types::kSVM, "SVM3", "Gamma=0.25:Tol=0.001:VarTransform=Norm:MaxIter=20000" );

   if (Use["SVM4"])
      factory->BookMethod( TMVA::Types::kSVM, "SVM4", "Gamma=0.25:C=2:Tol=0.001:VarTransform=Norm:MaxIter=2000" );


/*   if (Use["SVMdownGamma"])
      factory->BookMethod( TMVA::Types::kSVM, "SVMdownGamma", "Gamma=0.1:Tol=0.001:VarTransform=Norm:MaxIter=2000" );

   if (Use["SVMupTol"])
      factory->BookMethod( TMVA::Types::kSVM, "SVMupTol", "Gamma=0.25:Tol=0.01:VarTransform=Norm:MaxIter=2000" );

   if (Use["SVMdownTol"])
      factory->BookMethod( TMVA::Types::kSVM, "SVMdownTol", "Gamma=0.25:Tol=0.0001:VarTransform=Norm:MaxIter=2000" );

   if (Use["SVMdownC"])
      factory->BookMethod( TMVA::Types::kSVM, "SVMdownC", "Gamma=0.25:Tol=0.001:VarTransform=Norm:C=0.5:MaxIter=2000" );

   if (Use["SVMupC"])
      factory->BookMethod( TMVA::Types::kSVM, "SVMupC", "Gamma=0.25:Tol=0.001:VarTransform=Norm:C=2:MaxIter=2000" );
*/
   // Boosted Decision Trees///////////////////////////////////1111111111111111111111111111111111111111111111111111111111111111111111111111111111
   if (Use["BDT"+BDTname])  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDT"+BDTname,
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );


   if (Use["BDTG"]) // Gradient Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTG",
                           "!H:!V:NTrees=1000:MinNodeSize=2.5%:BoostType=Grad:Shrinkage=0.10:UseBaggedBoost:BaggedSampleFraction=0.5:nCuts=20:MaxDepth=2" );

   if (Use["BDT"])  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDT",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );

/*   if (Use["BDTmutau"])  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTmutau",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );

   if (Use["BDTeltau"])  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTeltau",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );

   if (Use["BDTmuel"])  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTmuel",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );
*/
   if (Use["BDT1"])  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDT1",
                           "!H:!V:NTrees=10000:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );

   if (Use["BDT2"])  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDT2",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=4:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );

   if (Use["BDT3"])  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDT3",
                           "!H:!V:NTrees=850:MinNodeSize=5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );

   if (Use["BDT4"])  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDT4",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );

   if (Use["BDT5"])  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDT5",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20:UseRandomisedTrees=True" );
   if (Use["BDT6"])  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDT6",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=50" );

   if (Use["BDT7"])  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDT7",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=-1" );

 if (Use["BDT8"])  // Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDT8",
                           "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.1:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20" );


   if (Use["BDTB"]) // Bagging
      factory->BookMethod( TMVA::Types::kBDT, "BDTB",
                           "!H:!V:NTrees=1000:BoostType=Bagging:SeparationType=GiniIndex:nCuts=20" );

   if (Use["BDTD"]) // Decorrelation + Adaptive Boost
      factory->BookMethod( TMVA::Types::kBDT, "BDTD",
                           "!H:!V:NTrees=1000:MinNodeSize=5%:MaxDepth=3:BoostType=AdaBoost:SeparationType=GiniIndex:nCuts=20:VarTransform=Decorrelate" );

   if (Use["BDTF"])  // Allow Using Fisher discriminant in node splitting for (strong) linearly correlated variables
      factory->BookMethod( TMVA::Types::kBDT, "BDTMitFisher",
                           "!H:!V:NTrees=1000:MinNodeSize=2.5%:UseFisherCuts:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:SeparationType=GiniIndex:nCuts=20" );

   // RuleFit -- TMVA implementation of Friedman's method
   if (Use["RuleFit"])
      factory->BookMethod( TMVA::Types::kRuleFit, "RuleFit",
                           "H:!V:RuleFitModule=RFTMVA:Model=ModRuleLinear:MinImp=0.001:RuleMinDist=0.001:NTrees=20:fEventsMin=0.01:fEventsMax=0.5:GDTau=-1.0:GDTauPrec=0.01:GDStep=0.01:GDNSteps=10000:GDErrScale=1.02" );

   // For an example of the category classifier usage, see: TMVAClassificationCategory

   // --------------------------------------------------------------------------------------------------

   // ---- Now you can optimize the setting (configuration) of the MVAs using the set of training events

   // ---- STILL EXPERIMENTAL and only implemented for BDT's ! 
   // factory->OptimizeAllMethods("SigEffAt001","Scan");
   // factory->OptimizeAllMethods("ROCIntegral","FitGA");

   // --------------------------------------------------------------------------------------------------

   // ---- Now you can tell the factory to train, test, and evaluate the MVAs

   // Train MVAs using the set of training events
   factory->TrainAllMethods();

   // ---- Evaluate all MVAs using the set of test events
   factory->TestAllMethods();

   // ----- Evaluate and compare performance of all configured MVAs
   factory->EvaluateAllMethods();

   // --------------------------------------------------------------

   // Save the output
   outputFile->Close();

   std::cout << "==> Wrote root file: " << outputFile->GetName() << std::endl;
   std::cout << "==> TMVAClassification is done!" << std::endl;

   delete factory;

   // Launch the GUI for the root macros
   //if (!gROOT->IsBatch()) TMVA::TMVAGui( outfileName );
   TMVA::TMVAGui( outfileName );
   return 0;
}

int main( int argc, char** argv )
{
   // Select methods (don't look at this code - not of interest)
   TString methodList; 
   for (int i=1; i<argc; i++) {
      TString regMethod(argv[i]);
      if(regMethod=="-b" || regMethod=="--batch") continue;
      if (!methodList.IsNull()) methodList += TString(","); 
      methodList += regMethod;
   }
   return N_TMVA(methodList); 
}



