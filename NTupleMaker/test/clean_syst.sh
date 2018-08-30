dir=/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test
systematics="Nominal _JetEnUp _JetEnDown _UnclEnUp _UnclEnDown _TauEnUp _TauEnDown _ElEnUp _ElEnDown _MuEnUp _MuEnDown _BTagUp _BTagDown"


dirm=${dir}/mutau
dire=${dir}/eltau
dirme=${dir}/muel

#rm $dir/$1

for syst in $systematics
do

	
if [[ $syst != "Nominal" ]] ;then

dirm=${dir}/mutau${syst}
dire=${dir}/eltau${syst}
dirme=${dir}/muel${syst}
fi

echo $dirm $dire $dirme
	rm  $dirm/$1*root
	rm  $dire/$1*root
	rm  $dirme/$1*root




done
