



wdir=$PWD;
cd  $wdir; eval `scramv1 runtime -sh`
channel=$2 

if [ ! -d Jobs_mc_${channel} ]
then
        mkdir Jobs_mc_${channel}
fi


##type MC or Data
type=MC

systematics="$3"

if [[ $3 == "all" || $3 == "All"  || $3 == "list" ]];then
systematics="Nominal JetEnUp JetEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown UnclEnUp UnclEnDown BTagUp BTagDown"

fi

if [[ -z $3  ]];then
systematics="Nominal"
syst="1"
fi

cp *.conf Jobs_mc_${channel}/.

for syst in $systematics
do


export dir=${2}_${syst}


if [[ $syst == "Nominal" ]] || [[ -z $3  ]];then
export	dir=${channel}
fi


while read line
do

ct=`ls ${dir}/${line}*_B_OS.root | wc -l`
ctt=`cat ${dir}/${line} | wc -l`


echo There are  $ct out of $ctt for $line in $dir dir for systematic $syst

if [[ $ct -ge $ctt ]] ;then
	continue;
fi

xsec=1
unset f
while read f
	do

unset bas
bas=`basename $f | awk -F ".root" '{print $1}'`

if [ ! -f $dir/$bas.root ] 
then
echo $f > $dir/$bas


	if [ -f Jobs_mc_${channel}/job${channel}${line}$dir${bas}_B${syst}.sh ] ; then
rm Jobs_mc_${channel}/job${channel}${line}$dir${bas}_B${syst}.sh
fi

cat bss > Jobs_mc_${channel}/job${channel}${line}$dir${bas}_B${syst}.sh

if [ ! -f ${dir}/${bas}_B_OS.root ] ;then

echo $bas $xsec $dir

if [[ ${channel} == "HZZmumu" ]] ; then 
echo SUSY${channel} analysisMacroSUSY_${type}_B.conf ${bas} ${channel} 1 $syst>> Jobs_mc_${channel}/job${channel}${line}$dir${bas}_B${syst}.sh

fi
if [[ ${channel} != "HZZmumu" ]] ; then 

	echo SUSY${channel}  analysisMacroSUSY_MC_B.conf ${bas} $dir 1 >> Jobs_mc_${channel}/job${channel}${line}$dir${bas}_B${syst}.sh

fi

chmod u+x $wdir/Jobs_mc_${channel}/job${channel}${line}$dir${bas}_B${syst}.sh
 ./HTC_submit.sh $wdir/Jobs_mc_${channel}/job${channel}${line}$dir${bas}_B${syst}.sh ${bas}
fi


fi

done<$dir/${line}
done<$1
done
