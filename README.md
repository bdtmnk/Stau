# DesyTauAnalysesRun2_25ns

Instructions and tips for newcomers

The master branch is used for most analyses while other branches are used for NTuple production or other operations which are heavily dependent on the CMSSW version.

To work with this repository please install the appropriate CMSSW version and follow the instructions in our working twiki:
https://twiki.cern.ch/twiki/bin/viewauth/CMS/DesyTauAnalysesRun2

To upload your code:
- please fork the master branch (or the appropriate branch if needed) of this repository, by clicking the fork button in the top right corner (if working via browser)
- from terminal go in the directory `${CMSSW_BASE}/src/DesyTauAnalyses` and link your personal repository by running `git remote add upstream https://github.com/GITHUB_USERNAME/DesyTauAnalysesRun2_25ns.git` (upstream will be the name of the remote, any other name is valid)
- checkout your working branch with `git checkout from-CMSSW_VERSION` (or check the name of the current working branch with `git branch` in case you do not want to make changes to the master branch)
- stage the changes you want to upload with `git add list-of-edited-files`
- commit your changes adding a small comment with `git commit -m "comment" list-of-edited-files`
- push your changes with `git push upstream from-CMSSW_VERSION`
- from browser make a pull request (PR)



# DesyTauAnalysesRun2_25ns


https://twiki.cern.ch/twiki/bin/viewauth/CMS/DesyTauAnalysesRun2

Installation:

export CMSSW_GIT_REFERENCE=/nfs/dust/cms/user/${USER}/.cmsgit-cache
source /cvmfs/cms.cern.ch/cmsset_default.sh

export SCRAM_ARCH=slc7_amd64_gcc700

cmsrel CMSSW_10_2_22
cd CMSSW_10_2_22/src
cmsenv

git cms-init

### EGamma (from here: https://twiki.cern.ch/twiki/bin/view/CMS/EgammaMiniAODV2#2018_MiniAOD changed on 14/06/2019)
git cms-merge-topic cms-egamma:EgammaPostRecoTools #just adds in an extra file to have a setup function to make things easier 
#git cms-merge-topic cms-egamma:PhotonIDValueMapSpeedup1029 #optional but speeds up the photon ID value module so things fun faster
git cms-merge-topic cms-egamma:slava77-btvDictFix_10210 #fixes the Run2018D dictionary issue, see https://github.com/cms-sw/cmssw/issues/26182, may not be necessary for later releases, try it first and see if it works
#now to add the scale and smearing for 2018 (eventually this will not be necessary in later releases but is harmless to do regardless)
git cms-addpkg EgammaAnalysis/ElectronTools
rm EgammaAnalysis/ElectronTools/data -rf
git clone https://github.com/cms-data/EgammaAnalysis-ElectronTools.git EgammaAnalysis/ElectronTools/data
#now build everything
scram b -j 8

git cms-merge-topic KIT-CMS:embedded_metcov_fix_10_2_22
scram b -j 8

### DeepTauIdv2 Inclusion (from here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID#Running_of_the_DeepTauIDs_ver_20)
#Add DeepTau code from Tau POG repository (note "-u" option preventing checkout of unnecessary stuff)
git cms-merge-topic -u cms-tau-pog:CMSSW_10_2_X_tau-pog_DeepTau2017v2p1_nanoAOD

### Add fix for JER parametrisation (see here: https://hypernews.cern.ch/HyperNews/CMS/get/jes/898/2/1/1/1/1/1.html)
git cms-merge-topic -u ahinzmann:resolutionSmearingFix102

git cms-merge-topic -u danielwinterbottom:from-CMSSW_10_2_16-mvaDM
scram b -j 8

git clone https://github.com/cms-analysis/HiggsAnalysis-ZZMatrixElement.git ZZMatrixElement
cd ZZMatrixElement/
sh setup.sh -j 8
cd ..

cd ${CMSSW_BASE}/src
git clone https://github.com/CMS-HTT/HiggsCPinTauDecays.git

### SVfit (needed for backward compatibility)
git clone https://github.com/veelken/SVfit_standalone.git ${CMSSW_BASE}/src/TauAnalysis/SVfitStandalone
cd ${CMSSW_BASE}/src/TauAnalysis/SVfitStandalone
git checkout HIG-16-006
cd ${CMSSW_BASE}/src/

### SVfit-updated
git clone https://github.com/svfit/ClassicSVfit TauAnalysis/ClassicSVfit -b fastMTT_19_02_2019
git clone https://github.com/svfit/SVfitTF TauAnalysis/SVfitTF

### Lepton efficiencies interface and ROOT files from CMS-HTT
git clone https://github.com/CMS-HTT/LeptonEff-interface HTT-utilities
cd HTT-utilities/LepEffInterface/
rm -rf data
git clone https://github.com/CMS-HTT/LeptonEfficiencies.git data
cd ${CMSSW_BASE}/src

### Corrections workspace from CMS-HTT
git clone https://github.com/CMS-HTT/CorrectionsWorkspace HTT-utilities/CorrectionsWorkspace
cd ${CMSSW_BASE}/src/HTT-utilities/CorrectionsWorkspace
root -l -q CrystalBallEfficiency.cxx++
cd ${CMSSW_BASE}/src

### RecoilCorrections
cd ${CMSSW_BASE}/src
git clone https://github.com/CMS-HTT/RecoilCorrections.git HTT-utilities/RecoilCorrections

### RecoilCorrections KIT
cd ${CMSSW_BASE}/src
git clone https://github.com/marmeyer/RecoilCorrections.git HTT-utilities/RecoilCorrections_KIT

### QCD background model in emu channel
cd ${CMSSW_BASE}/src
git clone https://github.com/CMS-HTT/QCDModelingEMu.git HTT-utilities/QCDModelingEMu

### Tau POG SF (trigger, DeepTauvsJet and against-electron/muon)
cd ${CMSSW_BASE}/src
git clone -b tauTriggers2017_MCv2_PreReMiniaod https://github.com/truggles/TauTriggerSFs.git HTT-utilities/TauTriggerSFs2017
git clone -b run2_SFs https://github.com/cms-tau-pog/TauTriggerSFs TauAnalysisTools/TauTriggerSFs
git clone https://github.com/cms-tau-pog/TauIDSFs.git TauPOG/TauIDSFs

### Jet2TauFakes 
cd ${CMSSW_BASE}/src
git clone https://github.com/CMS-HTT/Jet2TauFakes.git HTTutilities/Jet2TauFakes

### DesyTau
cd ${CMSSW_BASE}/src
git clone https://github.com/DesyTau/DesyTauAnalysesRun2_25ns.git ${CMSSW_BASE}/src/DesyTauAnalyses

### patch for SVFitStandalone (for backward compatibility)
cp ${CMSSW_BASE}/src/DesyTauAnalyses/patch/SVFit/SVfitStandaloneAlgorithm.h TauAnalysis/SVfitStandalone/interface/
cp ${CMSSW_BASE}/src/DesyTauAnalyses/patch/SVFit/SVfitStandaloneAlgorithm.cc TauAnalysis/SVfitStandalone/src
cp ${CMSSW_BASE}/src/DesyTauAnalyses/patch/SVFit/testSVfitStandalone.cc TauAnalysis/SVfitStandalone/bin
rm TauAnalysis/SVfitStandalone/interface/SVfitStandaloneQuantities.h
rm TauAnalysis/SVfitStandalone/src/SVfitStandaloneQuantities.cc

scram b -j 8
scram b -j 8

