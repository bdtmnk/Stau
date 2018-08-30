
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

if [[ $syst == "Nominal" ]] ; then

dir=${1}

fi

echo $syst... for $1
cd $dir 

echo ========================= Inside DIR  $dir  =====================================================================
cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/m .
cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/dyj .
cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/d .
cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/copy_NJets.sh .
cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/mutau/w .


#cp /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/eltau/rmm .
#. rmm
#. copy_NJets.sh w

#rm *
#rm C1*
#rm stau*
#rm *ZTT*root
#rm *Parton*root
#find . -type f -name "*.root" -size -1000c -exec rm {} \;
#. m
#. dyj
#. copy_NJets.sh w
#. d 

rm *right*root
#tar -cvf tfr${syst}.tar *.root
#gzip  tfr${syst}.tar
#echo mv  tfr${syst}.tar.gz ~/.

echo ============================= Done ========================================================================
cd ..

done

