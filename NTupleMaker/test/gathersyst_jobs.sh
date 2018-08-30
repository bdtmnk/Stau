
dir=$1

#systematics="Nominal JetEnUp JetEnDown UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"
systematics="JetEnUp JetEnDown UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"
#systematics="TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"
#systematics="JetEnUp JetEnDown UnclEnUp UnclEnDown"
#systematics="UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"

alias ls='ls'


for syst in $systematics
do

unset dir
dir=${1}_${syst}

cat bss > job${dir}.sh

echo $syst... for $1
echo cd /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/$dir >>job${dir}.sh

echo `pwd` >>job${dir}.sh
echo ========================= Inside DIR  $dir  =====================================================================
echo cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/m /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/$dir/. >>job${dir}.sh
echo cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/dyj /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/$dir/. >>job${dir}.sh
echo cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/d /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/$dir/. >>job${dir}.sh
echo cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/copy_NJets.sh /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/$dir/. >>job${dir}.sh
echo cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/w /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/$dir/. >>job${dir}.sh

echo chmod 777 /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/$dir/m  >>job${dir}.sh
echo chmod 777 /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/$dir/dyj  >>job${dir}.sh
echo chmod 777 /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/$dir/copy_NJets.sh  >>job${dir}.sh

echo rm *ZTT*root >>job${dir}.sh
echo rm *Parton*root >>job${dir}.sh
echo ./m >>job${dir}.sh
echo ./dyj >>job${dir}.sh
echo ./copy_NJets.sh w >>job${dir}.sh

echo ============================= Done ========================================================================
echo cd ... >>job${dir}.sh

  qsub  -l h_vmem=3000M -l h_cpu=2:59:00 job${dir}.sh $1

done
