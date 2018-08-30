
systematics="Nominal JetEnUp JetEnDown UnclEnUp UnclEnDown MuEnUp MuEnDown TauEnUp TauEnDown ElEnUp ElEnDown BTagUp BTagDown plots"

systematics="plots"
while read line
do
for syst in $systematics
do

unset dir
dir=${1}_${syst}
ext="B_OS.root"

	if  [[ $syst == "Nominal" ]] ; then

		dir=${1}
	fi
	if  [[ $syst == "plots" ]] ; then
		ext="*.root"

		dir=plots_${1}
	fi


	rm $dir/${line}_${ext}



done
done<$2
