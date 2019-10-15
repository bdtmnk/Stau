rm points_${1}_list
dir="/nfs/dust/cms/user/bobovnii/new/CMSSW_8_0_20/src/DesyTauAnalyses/NTupleMaker/test/Processing/mutauMVAtest2/"



ls $dir/cards_mt/$1*_LSP* | awk -F"_mt/" '{print $2}' |  cut -d "_" -f2 | sort -u  | sort -V  > mass_$1

while read line
do


ls $dir/cards_mt/$1*${line}_LSP*_* | awk -F"_mt/" '{print $2}' | cut -d "_" -f3 | sort -u | awk -F "LSP" '{print $2}' | sort -V >   points_${1}_list

while read lsp


do

	echo RunLimitsC1C1.sh $1 $line $lsp
. RunLimitsC1C1.sh $1 $line $lsp

done<points_${1}_list

done<mass_$1
