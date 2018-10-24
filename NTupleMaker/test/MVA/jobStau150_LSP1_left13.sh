#!/bin/sh
#
#(make sure the right shell will be used)
#$ -S /bin/sh
#
#(the cpu time for this job)
#$ -l h_cpu=61:10:00
#
#(the maximum memory usage of this job)
#$ -l h_vmem=20000M
#
#(use hh site)
#$ -l site=hh
#(stderr and stdout are merged together to stdout)
#$ -j y
#
# use SL5
#$ -l os=sld6
#
# use current dir and current environment
#$ -cwd
#$ -V
#

cd /nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_9_4_0_patch1/src/DesyTauAnalyses/NTupleMaker/test/MVA ;  eval `scramv1 runtime -sh` ;

root -l -b -q 'myTMVA.C("","TMVA_Stau150_LSP1_left_{13}2s.root","mutau_Stau150_LSP1_left",0.06334,"Stau150_LSP1_left","!H:!V:NTrees=850:MinNodeSize=0.05%:MaxDepth=3:BoostType=RealAdaBoost:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=35:UseRandomisedTrees=True")' > logTMVA_Stau150_LSP1_left13
