dirr=/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/Processing/01Jets/MuTau/CRB


rg=$2

rm points_${1}_list

if [[ ! -d Tables ]] ; then
	mkdir Tables
fi

if [[ ! -d Results ]] ; then
	mkdir Results
fi

#if [[ $1 == "stau" ]] ; then

#ls cards_mt/$1*_LSP* | cut -d "/" -f2 | cut -d "_" -f2 | sort -u | awk -F "$1" '{print $2}' | sort -V  > mass_$1
ls $dirr/cards_mt/$1*_LSP* | awk -F"_mt/" '{print $2}' |  cut -d "_" -f2 | sort -u  | sort -V  > mass_$1
#fi

# awk 'NR % 2 == 0' mass_$1 > t ; mv t mass_$1

#if [[ $1 == "C1C1" ]] || [[ $1 == "C1N2" ]]; then

#ls $dir/cards_mt/$1*_LSP* | cut -d "/" -f2 | cut -d "_" -f2 | sort -u | sort -V  > mass_$1
#fi

cat mass_$1 | head -1  > t ; mv t mass_$1


while read line
do

if [[ $line -lt "925" ]] ; then

ls $dirr/cards_mt/$1*${line}_LSP*_* | awk -F"_mt/" '{print $2}' | cut -d "_" -f3 | sort -u | awk -F "LSP" '{print $2}' | sort -V >   points_${1}_list

cat points_${1}_list | head -1 > t ; mv t points_${1}_list

##use this to skip every other point in the LSP
#awk 'NR % 2 == 0'  points_${1}_list > t ; mv t  points_${1}_list

while read lsp


do

if [[ $line != $lsp ]] ; then


	echo RunLimits.sh $1 $line $lsp
. RunLimitsNEW2.sh $1 $line $lsp $rg $3

fi

done<points_${1}_list

fi
done<mass_$1
