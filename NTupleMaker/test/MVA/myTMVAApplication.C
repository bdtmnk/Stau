/**********************************************************************************
 * Project   : TMVA - a Root-integrated toolkit for multivariate data analysis    *
 * Package   : TMVA                                                               *
 * Exectuable: myTMVAApplication                              *
 *                                                                                *
 * This macro provides a simple example on how to use the trained classifiers     *
 * (with categories) within an analysis module                                    *
 **********************************************************************************/

#include <cstdlib>
#include <vector>
#include <iostream>
#include <map>
#include <string>

#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TH1F.h"
#include "TStopwatch.h"

#if not defined(__CINT__) || defined(__MAKECINT__)
#include "TMVA/Tools.h"
#include "TMVA/Reader.h"
#include "TMVA/MethodCuts.h"
#endif
#include "/nfs/dust/cms/user/bobovnii/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/interface/functionsSUSY.h"
#include "/nfs/dust/cms/user/bobovnii/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/interface/lester_mt2_bisect.h"
// two types of category methods are implemented
Bool_t UseOffsetMethod = kTRUE;

void myTMVAApplication()
{
//////////////stupid definition!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		const double MuMass = 0.105658367;
		const double tauMass = 1.776;
		const double electronMass = 0.51100e-3;
		const double muonMass = 0.10565837;
		const double pionMass = 0.1396;
		const double bTagCut  = 0.8000;
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
		Float_t         TFR_weight;
		Float_t         top_weight;
		Float_t         all_weight;
		Float_t         trig_weight;
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
		Float_t         event_thirdLeptonVeto;
		Float_t         event_leptonDrTrigger;
		//   string 	   datasetName;
		string * datasetName = new std::string(); 
		string          *regionName;
		Float_t 	genTauMatched;
		Float_t 	genLeptonMatched;
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
		TBranch        *b_TFR_weight;   //!
		TBranch        *b_top_weight;   //!
		TBranch        *b_all_weight;   //!
		TBranch        *b_trig_weight;   //!
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
		TBranch        *b_event_thirdLeptonVeto;   //!
		TBranch        *b_event_leptonDrTrigger;   //!
		TBranch        *b_genTauMatched;   //!
		TBranch        *b_genLeptonMatched;   //!
		TBranch        *b_qcdweight;   //!
		TBranch        *b_qcdweightup;   //!
		TBranch        *b_qcdweightdown;   //!
		TBranch        *b_npartons;   //!
		TBranch        *b_nbtag;   //!
		TBranch        *b_njets;   //!
///////////////////////////////////////// END of stupid definition!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111111




   // ---------------------------------------------------------------
   // default MVA methods to be trained + tested
   std::map<std::string,int> Use;
   // ---
   //Use["LikelihoodCat"] = 1;
   //Use["FisherCat"]     = 1;
   Use["BDT"]     = 1;
   // ---------------------------------------------------------------

   std::cout << std::endl
             << "==> Start myTMVAApplication" << std::endl;

   // --- Create the Reader object

   TMVA::Reader *reader = new TMVA::Reader( "!Color:!Silent" );    

   // Create a set of variables and spectators and declare them to the reader
   // - the variable names MUST corresponds in name and type to those given in the weight file(s) used
   Float_t var1, var2, var3, var4, eta;
   reader->AddVariable( "var1", &var1 );
   reader->AddVariable( "var2", &var2 );
   reader->AddVariable( "var3", &var3 );
   reader->AddVariable( "var4", &var4 );

   reader->AddSpectator( "eta", &eta );

   // --- Book the MVA methods

   for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) {
      if (it->second) {
         TString methodName = it->first + " method";
         TString weightfile = "weights/TMVAClassificationCategory_" + TString(it->first) + ".weights.xml";
         reader->BookMVA( methodName, weightfile ); 
      }
   }

   // Book output histograms
   UInt_t nbin = 100;
   std::map<std::string,TH1*> hist;
   //hist["LikelihoodCat"] = new TH1F( "MVA_LikelihoodCat",   "MVA_LikelihoodCat", nbin, -1, 0.9999 );
   //hist["FisherCat"]     = new TH1F( "MVA_FisherCat",       "MVA_FisherCat",     nbin, -4, 4 );
   hist["BDT"]     = new TH1F( "MVA_BDT",       "MVA_BDT",     nbin, -1, 1 );

   // Prepare input tree (this must be replaced by your data source)
   // in this example, there is a toy tree with signal and one with background events
   // we'll later on use only the "signal" events for the test in this example.
   //
   /*TString fname = TString(gSystem->DirName(__FILE__) ) + "/data/";
   // if directory data not found try using tutorials dir
   if (gSystem->AccessPathName( fname )) {
      fname = TString(gROOT->GetTutorialsDir()) + "/tmva/data/";
   }
   if (UseOffsetMethod) fname += "toy_sigbkg_categ_offset.root";
   else                 fname += "toy_sigbkg_categ_varoff.root";
   std::cout << "--- TMVAClassificationApp    : Accessing " << fname << "!" << std::endl;*/
   TFile *input = TFile::Open(fname);
   if (!input) {
      std::cout << "ERROR: could not open data file: " << fname << std::endl;
      exit(1);
   }

   // --- Event loop

   // Prepare the tree
   // - here the variable names have to corresponds to your tree
   // - you can use the same variables as above which is slightly faster,
   //   but of course you can use different ones and copy the values inside the event loop
   //
   TTree* theTree = (TTree*)input->Get("/nfs/dust/cms/user/bobovnii/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/test/mutau/SingleMuon_InvMuIso_15invfb_B_OS.root");
   std::cout << "--- Use signal sample for evalution" << std::endl;
   factory->AddVariable( "met_pt","met_pt", 'F' );
   factory->AddVariable( "mu_pt", "mu_pt", "", 'F' );
   factory->AddVariable( "ta_pt", "ta_pt", "units", 'F' );
   factory->AddVariable( "njets", "njets", "units", 'I' );
   factory->AddVariable( "nbtag", "nbtag", "units", 'I' );
   factory->AddVariable( "MTsum", "MTsum", "units", 'F' );
   factory->AddVariable( "Dzeta", "Dzeta", "units", 'F' );
   factory->AddVariable( "Minv", "Minv", "units", 'F' );
   factory->AddVariable( "dR", "dR", "units", 'F' );
   factory->AddVariable( "MTmutau", "MTmutau", "units", 'F' );
   factory->AddVariable( "MCTb", "MCTb", "units", 'F' );
   factory->AddVariable( "MT2lester", "MT2lester", "units", 'F' );

   std::cout << "--- Processing: " << theTree->GetEntries() << " events" << std::endl;
   TStopwatch sw;
   sw.Start();


		//////////////////////////////////////////////////////////////////////////////////////BAD waY!!!!!!!!!!!!!!!!!!!!!!!1

			theTree->SetBranchAddress("met_ex", &met_ex, &b_met_ex);
			theTree->SetBranchAddress("met_ey", &met_ey, &b_met_ey);
			theTree->SetBranchAddress("met_ez", &met_ez, &b_met_ez);
			theTree->SetBranchAddress("met_pt", &met_pt, &b_met_pt);
			theTree->SetBranchAddress("met_phi", &met_phi, &b_met_phi);

			theTree->SetBranchAddress("met_ex_recoil", &met_ex_recoil, &b_met_ex_recoil);
			theTree->SetBranchAddress("met_ey_recoil", &met_ey_recoil, &b_met_ey_recoil);
			theTree->SetBranchAddress("genmet", &genmet, &b_genmet);
			theTree->SetBranchAddress("genmetphi", &genmetphi, &b_genmetphi);
			theTree->SetBranchAddress("met_scaleUp", &met_scaleUp, &b_met_scaleUp);
			theTree->SetBranchAddress("met_scaleDown", &met_scaleDown, &b_met_scaleDown);
			theTree->SetBranchAddress("metphi_scaleUp", &metphi_scaleUp, &b_metphi_scaleUp);
			theTree->SetBranchAddress("metphi_scaleDown", &metphi_scaleDown, &b_metphi_scaleDown);
			theTree->SetBranchAddress("met_resoUp", &met_resoUp, &b_met_resoUp);
			theTree->SetBranchAddress("met_resoDown", &met_resoDown, &b_met_resoDown);
			theTree->SetBranchAddress("metphi_resoUp", &metphi_resoUp, &b_metphi_resoUp);
			theTree->SetBranchAddress("metphi_resoDown", &metphi_resoDown, &b_metphi_resoDown);

			theTree->SetBranchAddress("gen_weight", &gen_weight, &b_gen_weight);
			theTree->SetBranchAddress("pu_weight", &pu_weight, &b_pu_weight);
			theTree->SetBranchAddress("LSF_weight", &LSF_weight, &b_LSF_weight);
			theTree->SetBranchAddress("TFR_weight", &TFR_weight, &b_TFR_weight);
			theTree->SetBranchAddress("top_weight", &top_weight, &b_top_weight);
			theTree->SetBranchAddress("all_weight", &all_weight, &b_all_weight);
			theTree->SetBranchAddress("trig_weight", &trig_weight, &b_trig_weight);
			theTree->SetBranchAddress("zptmassweight", &zptmassweight, &b_zptmassweight);
			theTree->SetBranchAddress("xsecs", &xsecs, &b_xsecs);
			theTree->SetBranchAddress("muon_index", &muon_index, &b_muon_index);
			theTree->SetBranchAddress("muon_index_1", &muon_index_1, &b_muon_index_1);
			theTree->SetBranchAddress("muon_index_2", &muon_index_2, &b_muon_index_2);
			theTree->SetBranchAddress("electron_index", &electron_index, &b_electron_index);
			theTree->SetBranchAddress("taus_index", &taus_index, &b_taus_index);
			theTree->SetBranchAddress("primvert_count", &primvert_count, &b_primvert_count);
			theTree->SetBranchAddress("primvert_x", &primvert_x, &b_primvert_x);
			theTree->SetBranchAddress("primvert_y", &primvert_y, &b_primvert_y);
			theTree->SetBranchAddress("primvert_z", &primvert_z, &b_primvert_z);
			theTree->SetBranchAddress("mu_count", &mu_count, &b_mu_count);
			theTree->SetBranchAddress("mu_px", mu_px, &b_mu_px);
			theTree->SetBranchAddress("mu_py", mu_py, &b_mu_py);
			theTree->SetBranchAddress("mu_pz", mu_pz, &b_mu_pz);
			theTree->SetBranchAddress("mu_pt", mu_pt, &b_mu_pt);
			theTree->SetBranchAddress("mu_eta", mu_eta, &b_mu_eta);
			theTree->SetBranchAddress("mu_phi", mu_phi, &b_mu_phi);
			theTree->SetBranchAddress("mu_charge", mu_charge, &b_mu_charge);
			theTree->SetBranchAddress("mu_miniISO", mu_miniISO, &b_mu_miniISO);
			theTree->SetBranchAddress("mu_dxy", mu_dxy, &b_mu_dxy);
			theTree->SetBranchAddress("mu_dz", mu_dz, &b_mu_dz);
			theTree->SetBranchAddress("mu_dxyerr", mu_dxyerr, &b_mu_dxyerr);
			theTree->SetBranchAddress("mu_dzerr", mu_dzerr, &b_mu_dzerr);

			theTree->SetBranchAddress("mu_neutralHadIso", mu_neutralHadIso, &b_mu_neutralHadIso);
			theTree->SetBranchAddress("mu_photonIso", mu_photonIso, &b_mu_photonIso);
			theTree->SetBranchAddress("mu_chargedHadIso", mu_chargedHadIso, &b_mu_chargedHadIso);
			theTree->SetBranchAddress("mu_puIso", mu_puIso, &b_mu_puIso);
			theTree->SetBranchAddress("mu_neutralIso", mu_neutralIso, &b_mu_neutralIso);
			theTree->SetBranchAddress("mu_absIsoMu", mu_absIsoMu, &b_mu_absIsoMu);
			theTree->SetBranchAddress("mu_relIsoMu", mu_relIsoMu, &b_mu_relIsoMu);
			theTree->SetBranchAddress("el_neutralHadIso", el_neutralHadIso, &b_el_neutralHadIso);
			theTree->SetBranchAddress("el_photonIso", el_photonIso, &b_el_photonIso);
			theTree->SetBranchAddress("el_chargedHadIso", el_chargedHadIso, &b_el_chargedHadIso);
			theTree->SetBranchAddress("el_puIso", el_puIso, &b_el_puIso);
			theTree->SetBranchAddress("el_neutralIso", el_neutralIso, &b_el_neutralIso);
			theTree->SetBranchAddress("el_absIsoEl", el_absIsoEl, &b_el_absIsoEl);
			theTree->SetBranchAddress("el_relIsoEl", el_relIsoEl, &b_el_relIsoEl);

			theTree->SetBranchAddress("mu_relIso", mu_relIso, &b_mu_relIso);
			theTree->SetBranchAddress("jet_count", &jet_count, &b_jet_count);
			theTree->SetBranchAddress("npv", &npv, &b_npv);
			theTree->SetBranchAddress("npu", &npu, &b_npu);
			theTree->SetBranchAddress("jets_cleaned", &jets_cleaned, &b_jets_cleaned);
  			theTree->SetBranchAddress("njets", &njets, &b_njets);
			theTree->SetBranchAddress("jet_e", jet_e, &b_jet_e);
			theTree->SetBranchAddress("jet_px", jet_px, &b_jet_px);
			theTree->SetBranchAddress("jet_py", jet_py, &b_jet_py);
			theTree->SetBranchAddress("jet_pz", jet_pz, &b_jet_pz);
			theTree->SetBranchAddress("jet_pt", jet_pt, &b_jet_pt);
			theTree->SetBranchAddress("jet_eta", jet_eta, &b_jet_eta);
			theTree->SetBranchAddress("jet_phi", jet_phi, &b_jet_phi);
			theTree->SetBranchAddress("jet_flavour", jet_flavour, &b_jet_flavour);
			theTree->SetBranchAddress("jet_btag", jet_btag, &b_jet_btag);
			theTree->SetBranchAddress("jet_isLoose", jet_isLoose, &b_jet_isLoose);
			
			theTree->SetBranchAddress("el_count", &el_count, &b_el_count);
			theTree->SetBranchAddress("el_px", el_px, &b_el_px);
			theTree->SetBranchAddress("el_py", el_py, &b_el_py);
			theTree->SetBranchAddress("el_pz", el_pz, &b_el_pz);
			theTree->SetBranchAddress("el_pt", el_pt, &b_el_pt);
			theTree->SetBranchAddress("el_eta", el_eta, &b_el_eta);
			theTree->SetBranchAddress("el_phi", el_phi, &b_el_phi);
			theTree->SetBranchAddress("el_miniISO", el_miniISO, &b_el_miniISO);
			theTree->SetBranchAddress("el_dxy", el_dxy, &b_el_dxy);
			theTree->SetBranchAddress("el_dz", el_dz, &b_el_dz);
			theTree->SetBranchAddress("el_dxyerr", el_dxyerr, &b_el_dxyerr);
			theTree->SetBranchAddress("el_dzerr", el_dzerr, &b_el_dzerr);
			theTree->SetBranchAddress("el_charge", el_charge, &b_el_charge);
			theTree->SetBranchAddress("el_relIso", el_relIso, &b_el_relIso);

			theTree->SetBranchAddress("ta_count", &ta_count, &b_ta_count);
			theTree->SetBranchAddress("ta_px", ta_px, &b_ta_px);
			theTree->SetBranchAddress("ta_py", ta_py, &b_ta_py);
			theTree->SetBranchAddress("ta_pz", ta_pz, &b_ta_pz);
			theTree->SetBranchAddress("ta_mass", ta_mass, &b_ta_mass);
			theTree->SetBranchAddress("ta_eta", ta_eta, &b_ta_eta);
			theTree->SetBranchAddress("ta_phi", ta_phi, &b_ta_phi);
			theTree->SetBranchAddress("ta_pt", ta_pt, &b_ta_pt);
			theTree->SetBranchAddress("ta_dxy", ta_dxy, &b_ta_dxy);
			theTree->SetBranchAddress("ta_dz", ta_dz, &b_ta_dz);
			theTree->SetBranchAddress("ta_charge", ta_charge, &b_ta_charge);
			theTree->SetBranchAddress("ta_IsoFlag", &ta_IsoFlag, &b_ta_IsoFlag);
			theTree->SetBranchAddress("ta_relIso", ta_relIso, &b_ta_relIso);

			theTree->SetBranchAddress("datasetName", &datasetName);
			theTree->SetBranchAddress("CFCounter_", CFCounter_,&b_CFCounter_);
			theTree->SetBranchAddress("event_sign", &event_sign, &b_event_sign);
			theTree->SetBranchAddress("met_flag", &met_flag, &b_met_flag);
			theTree->SetBranchAddress("event_secondLeptonVeto", &event_secondLeptonVeto, &b_event_secondLeptonVeto);
			theTree->SetBranchAddress("event_thirdLeptonVeto", &event_thirdLeptonVeto, &b_event_thirdLeptonVeto);
			theTree->SetBranchAddress("event_leptonDrTrigger", &event_leptonDrTrigger, &b_event_leptonDrTrigger);
			theTree->SetBranchAddress("genTauMatched", &genTauMatched, &b_genTauMatched);
			theTree->SetBranchAddress("genLeptonMatched", &genLeptonMatched, &b_genLeptonMatched);

   			theTree->SetBranchAddress("qcdweight", &qcdweight, &b_qcdweight);
			theTree->SetBranchAddress("qcdweightup", &qcdweightup, &b_qcdweightup);
			theTree->SetBranchAddress("qcdweightdown", &qcdweightdown, &b_qcdweightdown);
		        theTree->SetBranchAddress("nbtag", &nbtag, &b_nbtag);

  			theTree->SetBranchAddress("npartons",&npartons,&b_npartons);




		//////////////////////////////////////////////////////////////////////////////////////End of BAD waY!!!!!!!!!!!!!!!!!!!!!!!1
   for (Long64_t ievt=0; ievt<theTree->GetEntries();ievt++) {

      if (ievt%10000 == 0) std::cout << "--- ... Processing event: " << ievt << std::endl;

      theTree->GetEntry(ievt);

      // --- Return the MVA outputs and fill into histograms

      for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) {
         if (!it->second) continue;
         TString methodName = it->first + " method";
         hist[it->first]->Fill( reader->EvaluateMVA( methodName ) );         
      }

   }
   sw.Stop();
   std::cout << "--- End of event loop: "; sw.Print();

   // --- Write histograms

   TFile *target  = new TFile( "TMVApp.root","RECREATE" );
   for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++)
      if (it->second) hist[it->first]->Write();

   target->Close();
   std::cout << "--- Created root file: \"TMVApp.root\" containing the MVA output histograms" << std::endl;

   delete reader;
   std::cout << "==> TMVAClassificationApplication is done!" << std::endl << std::endl;
}

int main( int argc, char** argv )
{
   myTMVAApplication();
   return 0;
}
