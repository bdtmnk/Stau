
dir=$1


systematics="Nominal JetEnUp JetEnDown UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown"
#systematics="JetEnUp JetEnDown UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown"
#systematics="JetEnUp JetEnDown UnclEnUp UnclEnDown"


alias ls='ls'


for syst in $systematics
do

unset dir
dir=${1}_${syst}

if [[ $syst == "Nominal" ]] ; then

dir=${1}

fi


cd $dir
#rm *root
#*root
rm stau*root
#. m
#. dyj

#. d
cd .. 

done

