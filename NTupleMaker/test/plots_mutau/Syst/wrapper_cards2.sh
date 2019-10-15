# regions 1 = SR, 2 = CRA (bincont > 100) , 3= CRB (100<bincont<1000) 4= SR_CR)



model=$1

#Templ_met_MT2lester_DZeta01J1D_17_35invfb_mt_Up_C1N2_SR_CR1.root

channel=mt

unset region

region=$2



if [[ $2 == "0" ]] ; then
region="SR CRB CRC SR_CR1"
region="SR"

fi


for rg in $region
do

if [[ ! -d $rg/cards_$channel ]];then
	mkdir -p $rg/cards_$channel
fi


variables="met_MT2lester_DZeta01J1D_17"
#variables="Mt2lestermutauHighDzeta_17 Mt2lestermutauMiddleDzeta_17 Mt2lestermutauLowDzeta_17"
#variables="METHighDzeta_17 METMiddleDzeta_17 METLowDzeta_17 Mt2lestermutauHighDzeta_17 Mt2lestermutauMiddleDzeta_17 Mt2lestermutauLowDzeta_17"
variables="BDTmutau_stau100_LSP50My_15 BDTmutau_stau100_LSP1My_15 BDTmutau_stau150_LSP100My_15 BDTmutau_stau150_LSP1My_15 BDTmutau_stau150_LSP50My_15 BDTmutau_stau200_LSP100My_15 BDTmutau_stau200_LSP150My_15 BDTmutau_stau200_LSP1My_15 BDTmutau_stau200_LSP50My_15 BDTmutau_stau300_LSP1My_15"
variables="BDTmutau_stau100_LSP1My_15 BDTmutau_stau150_LSP1My_15 BDTmutau_stau200_LSP1My_15 BDTmutau_stau300_LSP1My_15"
#variables="BDTmutau_stau100_LSP1My_15"
#variables="BDTmutau_stau100_LSP1My_16 BDTmutau_stau150_LSP1My_16 BDTmutau_stau200_LSP1My_16 BDTmutau_stau300_LSP1My_16 BDTmutau_stau100_LSP1My_17 BDTmutau_stau150_LSP1My_17 BDTmutau_stau200_LSP1My_17 BDTmutau_stau300_LSP1My_17 BDTmutau_stau100_LSP1My_15 BDTmutau_stau150_LSP1My_15 BDTmutau_stau200_LSP1My_15 BDTmutau_stau300_LSP1My_15"


for var in $variables
do


ls Var_${var}_35invfb_*${channel}_${rg}.root


i=`ls  Var_${var}_35invfb_*${channel}_${rg}.root`


#ls Var_${var}_*${channel}_${rg}.root

#i=`ls  Var_${var}_*${channel}_${rg}.root`


ln=`echo $i  | cut -d '.' -f1`

echo the file is $ln and the region is ============= $rg ==================
rm *out.root
 . cards.sh $ln $1 $rg $channel

 cp *out.root $rg/cards_$channel/.

done
done
