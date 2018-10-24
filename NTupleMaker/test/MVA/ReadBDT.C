
#include "/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/MVA/dataset/weights/myTMVA_BDTmutau_stau-stau100_LSP50My.class.C"
#include "TMVA/Factory.h"
#include "TMVA/Tools.h"
#include "TTree.h"
#include <iostream>


//#include <ScaleFactor.h
#include <TLorentzVector.h>
#include <TVector2.h>

using namespace std;

int main(int argc, char * argv[]) {

//double ReadBDT (const std::vector<double>& inputValues)
//{
	std::vector<double>* inputVec = new std::vector<double>( 13 );

			(*inputVec)[0] = 100;
			(*inputVec)[1] = 100;
			(*inputVec)[2] = 100;
			(*inputVec)[3] = 0.1;
			(*inputVec)[4] = 100;
			(*inputVec)[5] = 0.1;
			(*inputVec)[6] = 100;
			(*inputVec)[7] = 0.5;
			(*inputVec)[8] = 100;
			(*inputVec)[9] = 100;
			(*inputVec)[10] = 100;
			(*inputVec)[11] = 0.1;
			(*inputVec)[12] = 0.1;


	std::vector<std::string> inputVarsAll = {"met_pt","Lept1Pt","Lept2Pt","EtaDil","MTtot","Dzeta","Minv","dR","MT","MCTb","MT2lester","dMETPhiL1","dMETPhiL2"};

	IClassifierReader* BDTResponse= new ReadBDTmutau_stau_stau100_LSP50My (inputVarsAll );

	double retval = BDTResponse->GetMvaValue( inputValues );

}
