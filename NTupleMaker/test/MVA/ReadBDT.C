
#include "/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/MVA/dataset/weights/myTMVA_BDTmutau_stau-stau100_LSP50My.class.C"
#include "TMVA/Factory.h"
#include "TMVA/Tools.h"
#include "TTree.h"
#include <iostream>


//#include <ScaleFactor.h
#include <TLorentzVector.h>
#include <TVector2.h>

using namespace std;


double ReadBDT (const std::vector<double>& inputValues)
{
	std::vector<std::string> inputVarsAll = {"met_pt","Lept1Pt","Lept2Pt","EtaDil","MTtot","Dzeta","Minv","dR","MT","MCTb","MT2lester","dMETPhiL1","dMETPhiL2"};

	IClassifierReader* BDTResponse= new ReadBDTmutau_stau_stau100_LSP50My (inputVarsAll );

	double retval = BDTResponse->GetMvaValue( inputValues );
	return retval;

}
