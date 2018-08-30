

systematics="JetEnUp JetEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown"

systematics="Nominal"

unset systematics

systematics="$3"

if [[ $3 == "syst" ]] ; then

#systematics="UnclEnUp UnclEnDown"
systematics="Nominal JetEnUp JetEnDown UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown"
systematics="JetEnUp JetEnDown UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"
fi

if [[ $3 == "list" ]] ; then

#systematics="UnclEnUp UnclEnDown"
systematics="Nominal JetEnUp JetEnDown UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"
#systematics="JetEnUp JetEnDown UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"
#systematics="Nominal JetEnUp JetEnDown UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown"
#systematics="TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"
fi

if [[ $3 == "listDY" ]] ; then

#systematics="UnclEnUp UnclEnDown"
systematics="JetEnUp JetEnDown UnclEnUp UnclEnDown MuEnUp MuEnDown"
fi

if [[ $3 == "listTT" ]] ; then

#systematics="UnclEnUp UnclEnDown"
systematics="JetEnUp JetEnDown UnclEnUp UnclEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"
fi

if [[ $3 == "Jes" ]] ; then

#systematics="UnclEnUp UnclEnDown"
systematics="JetEnUp JetEnDown"
fi

if [[ $3 == "Uncl" ]] ; then

#systematics="UnclEnUp UnclEnDown"
systematics="UnclEnUp UnclEnDown"
fi

if [[ $3 == "lept" ]] ; then

#systematics="UnclEnUp UnclEnDown"
systematics="TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown"
fi

if [[ $3 == "el" ]] ; then

#systematics="UnclEnUp UnclEnDown"
systematics="ElEnUp ElEnDown"
fi


if [[ $3 == "mu" ]] ; then

#systematics="UnclEnUp UnclEnDown"
systematics="MuEnUp MuEnDown"
fi



if [[ $3 == "tau" ]] ; then

#systematics="UnclEnUp UnclEnDown"
systematics="TauEnUp TauEnDown"
fi


if [[ $3 == "BTag" ]] ; then

systematics="BTagUp BTagDown"
fi

cd /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test 
while read line
do

lt=`echo $line`
echo $line > $lt

for syst in $systematics
do
	



	#echo $line > dt
	
	echo submitting  run_mc.sh $line for $2 channel and systematic = $syst
	
			qsub  -l h_vmem=3000M -l h_cpu=2:59:00 run_mc2.sh $line $2 $syst  

done
done<$1
