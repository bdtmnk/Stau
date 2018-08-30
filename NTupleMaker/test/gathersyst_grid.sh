
dir=$1

systematics="Nominal JetEnUp JetEnDown UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"
systematics="JetEnUp JetEnDown UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"
systematics="UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"
systematics="JetEnUp JetEnDown UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"
systematics="JetEnUp"

alias ls='ls'


for syst in $systematics
do

unset dir
dir=${1}_${syst}

if [[ $syst == "Nominal" ]] ; then

dir=${1}

fi


cat bss > j${1}${syst}merge.sh
#echo "cd /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test;eval `scramv1 runtime -sh` ;" > j${1}${syst}merge.sh
echo "cd /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/$dir" >> j${1}${syst}merge.sh
echo "cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/m m.sh"  >> j${1}${syst}merge.sh
echo "cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/dyj dyj.sh"  >> j${1}${syst}merge.sh
echo "cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/d d.sh" >> j${1}${syst}merge.sh
#cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/eltau/s .

echo "chmod u+x m.sh">>j${1}${syst}merge.sh
echo "chmod u+x dyj.sh">>j${1}${syst}merge.sh
echo "rm *ZTT*root"  >> j${1}${syst}merge.sh
echo "pwd" >> j${1}${syst}merge.sh
echo "source  /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/$dir/m.sh"  >> j${1}${syst}merge.sh
echo "source  /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/$dir/dyj.sh"  >> j${1}${syst}merge.sh



#echo "cd /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test"  >> j${1}${syst}merge.sh 

#qsub -l h_rt=1:45:00 -l h_cpu=3500M -e /dev/null -o /dev/null j${1}${syst}merge.sh
qsub -l h_rt=1:45:00 -l h_cpu=5500M -o log j${1}${syst}merge.sh

done

