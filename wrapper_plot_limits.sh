#dirr="/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/test/Processing/MuTau"
#dirr="/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/test/Processing/01Jets/MuTau"
#dirr="/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/test/Processing/01Jets/MuTau/NewBinning/"
dirr=/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/plots_mutau/Syst/SR/cards_mt


channel=$3

rg=$2

model=$1
rm points_${1}_list

if [[ ! -d Tables ]] ; then
	mkdir Tables
fi

if [[ ! -d Results ]] ; then
	mkdir Results
fi


if [[ ${model} == *"stau-stau_left"*  ]] || [[ $1 ==  *"Stau"* ]];
then

	echo stau it is then....
ls $dirr/${1}* | awk -F"_mt/" '{print $2}' |  cut -d "_" -f1 | sort -u  | awk -F "Stau" '{print $2}' | sort -V  > mass_$1

fi
#C1N2
if [[ $1 == *"C1"* || $1 == *"Chi"* ]] ; then
#else

	echo something else than staus

ls $dirr/cards_mt/${1}_* | awk -F"_mt/" '{print $2}' |  cut -d "_" -f1 | sort -u  | awk -F "Stau" '{print $2}' | sort -V  > mass_$1
fi

# awk 'NR % 2 == 0' mass_$1 > t ; mv t mass_$1

#if [[ $1 == "C1C1" ]] || [[ $1 == "C1N2" ]]; then

#ls $dir/cards_mt/$1*_LSP* | cut -d "/" -f2 | cut -d "_" -f2 | sort -u | sort -V  > mass_$1
#fi


while read line
do

if [[ $line -lt "800" ]] ; then


if [[ $1 == *"C1"*  || $1 == *"Chi"* ]] ; then
ls $dirr/cards_mt/$1_*${line}_LSP*_* | awk -F"_mt/" '{print $2}' | cut -d "_" -f1 | sort -u | awk -F "LSP" '{print $2}' | sort -V >   points_${1}_list
fi


if [[ $1 ==  "stau-stau_left"  ]] || [[ $1 ==  "Stau" ]];then

	echo for the points...
	echo $1
ls $dirr/$1*${line}_LSP* | awk -F"_mt/" '{print $2}' | cut -d "_" -f2 | sort -u | awk -F "LSP" '{print $2}' | sort -V >   points_${1}_list
fi


##use this to skip every other point in the LSP
#awk 'NR % 2 == 0'  points_${1}_list > t ; mv t  points_${1}_list

while read lsp


do

if [[ $line != $lsp ]] ; then


	echo RunLimits.sh $1 $line $lsp
. RunLimitsNEW.sh $1 $line $lsp $rg $channel

fi

done<points_${1}_list

fi
done<mass_$1
