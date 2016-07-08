rm points_${1}_list


if [[ $1 == "stau" ]] ; then

ls cards_mt/$1*_LSP* | cut -d "/" -f2 | cut -d "_" -f2 | sort -u | awk -F "$1" '{print $2}' | sort -V  > mass_$1
fi

if [[ $1 == "C1C1" ]] || [[ $1 == "C1N2" ]]; then

ls cards_mt/$1*_LSP* | cut -d "/" -f2 | cut -d "_" -f2 | sort -u | sort -V  > mass_$1
fi


while read line
do


ls cards_mt/$1*${line}_LSP*_* | cut -d "/" -f2 | cut -d "_" -f3 | sort -u | awk -F "LSP" '{print $2}' | sort -V >   points_${1}_list

while read lsp


do

	echo RunLimitsC1C1.sh $1 $line $lsp
. get_lists_for_limits.sh $1 $line $lsp

done<points_${1}_list

done<mass_$1
