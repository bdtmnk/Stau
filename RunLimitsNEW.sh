


mode="left"



variables="met_MT2lester_DZeta01J1D"
variables="BDTmutau_stau100_LSP50My_15 BDTmutau_stau100_LSP1My_15 BDTmutau_stau150_LSP100My_15 BDTmutau_stau150_LSP1My_15 BDTmutau_stau150_LSP50My_15 BDTmutau_stau200_LSP100My_15 BDTmutau_stau200_LSP150My_15 BDTmutau_stau200_LSP1My_15 BDTmutau_stau200_LSP50My_15 BDTmutau_stau300_LSP1My_15"
variables="BDTmutau_stau150_LSP1My_15 BDTmutau_stau200_LSP1My_15 BDTmutau_stau300_LSP1My_15 BDTmutau_stau100_LSP1My_15"


variables="stau250_LSP1MyNew_15 stau90_LSP1MyNew_15 stau150_LSP1MyNew_15 stau200_LSP1MyNew_15 stau300_LSP1MyNew_15 stau100_LSP1MyNew_15"

variables="Stau100_16 Stau150_16 Stau200_16"


if [ $mode == "left" ]; then
dircMT="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/plots_mutau/Syst/SR/cards_mt"
dircET="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/plots_eltau/Syst/SR/cards_mt"


dircMT2017="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_9_4_0_patch1/src/DesyTauAnalyses/NTupleMaker/test/plots_mutau/Syst/SR/cards_mt"
dircET2017="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_9_4_0_patch1/src/DesyTauAnalyses/NTupleMaker/test/plots_eltau/Syst/SR/cards_mt"
dircTT="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_1_0/src/Limits/STau/DataCards_RunII_Approval_Final_Two_Cleaned_6/left_Ilya/"


fi



if [ $mode == "degen" ]; then

dircMT="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/plots_mutau/Syst/SR/cards_mt_degen"
dircET="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/plots_eltau/Syst/SR/cards_mt_degen"
#
#
dircMT2017="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_9_4_0_patch1/src/DesyTauAnalyses/NTupleMaker/test/plots_mutau/Syst/SR/cards_mt_degen"
dircET2017="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_9_4_0_patch1/src/DesyTauAnalyses/NTupleMaker/test/plots_eltau/Syst/SR/cards_mt_degen"
dircTT="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_1_0/src/Limits/STau/DataCards_RunII_Approval_Final_Two_Cleaned_6/degenerate_Ilya/"


fi

#dircTT="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_1_0/src/Limits/STau/datacards_2/"
#dircTT="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_1_0/src/Limits/STau/DatacardsFinal/degenerate_Ilya/"

#dircTT="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_1_0/src/Limits/STau/DatacardsFinal/left_Ilya/"


Region=$4

dir=`pwd`

massp=$1
lspp=$2

lumi=35

combination="comb"

cut=15
model=$1


channel=$5

model=$1

lsprange=$3

echo ============================ $lsprange

for mass in $2
#for mass in '90'

do
    for masslsp in '1'
    #for masslsp in $lsprange
    do
	    #for channel in mt et muel
	    for comb in  $combination
	    do
		echo "--> channel" $comb and $mass , LSP$masslsp



for var in $variables
do


	if [[ ${mass} -gt ${masslsp} ]] ; then

if [[ ! -f  Results_${Region}${channel}/${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}invfb.root ]] ; then

#cardnew= $dirc/MuTau/cards_${channel}/${model}_${mass}_LSP${masslsp}_${var}_${cut}_mt_${lumi}invfb.txt

dirc="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_1_0/src/Limits/STau/"
dir="/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_1_0/src/Limits/STau/"


cardnew2=${model}_${mass}_LSP${masslsp}_${var}_${cut}_comb_${lumi}invfb.txt

cardnew=$dirc/combined_SR/${model}_${mass}_LSP${masslsp}_${var}_${cut}_comb_${lumi}invfb.txt
#if [[ $channel == "comb" ]] && [[ ! -f $cardnew ]] ; then

#cardmt=$dirc/MuTau/NewBinning/Max100Events/cards_mt/${model}_${mass}_LSP${masslsp}_${var}_${cut}_mt_${lumi}invfb.txt
#cardet=$dirc/ElTau/NewBinning/Max100Events/cards_et/${model}_${mass}_LSP${masslsp}_${var}_${cut}_et_${lumi}invfb.txt
#cardmt=$dirc/${model}_${mass}_LSP${masslsp}_${var}_mt_${lumi}invfb.txt



cardmt=$dircMT/${model}${mass}_LSP${masslsp}_left_BDTmutau_${var}_mt_${lumi}invfb.txt
cardet=$dircET/${model}${mass}_LSP${masslsp}_left_BDTeltau_${var}_mt_${lumi}invfb.txt

cardmt2017=$dircMT2017/${model}${mass}_LSP${masslsp}_left_BDTmutau_${var}_mt_${lumi}invfb.txt
cardet2017=$dircET2017/${model}${mass}_LSP${masslsp}_left_BDTeltau_${var}_mt_${lumi}invfb.txt

#cardme=""
#cardet=""
#cardmt=""


#combineCards.py $cardmt $cardet > $cardnew

#combineCards.py $cardmt2017 $cardet2017 > $cardnew



#combineCards.py $cardmt $cardet $cardmt2017 $cardet2017 > $cardnew



#combineCards.py $cardmt $cardet $cardmt2017 $cardet2017 > $cardnew

#python ./../../../../CombineHarvester/CombineTools/scripts/partialCorrelationEdit.py Stau90_LSP1_left_BDTmutau_Stau100_16_mt_35invfb.txt --process TauEn,0.5  --postfix-uncorr _2016  --output-txt new_Stau90_LSP1_left_BDTmutau_Stau100_16_mt_35invfb.txt


#combineCards.py -S $dircTT/mStau_${mass}_mLSP_0_*2016.card $cardmt $cardet > card2016.txt

if [ $masslsp == "1" ];
then

#combineCards.py -S $dircTT/mStau_${mass}_mLSP_0_*.card $cardmt $cardet $cardmt2017 $cardet2017 >  $cardnew

#combineCards.py -S $dircTT/mStau_${mass}_mLSP_0_*.card $cardmt $cardet $cardmt2017 $cardet2017 $dircTT/mStau_${mass}_mLSP_0_*.card $cardmt $cardet $cardmt2017 $cardet2017 $dircTT/mStau_${mass}_mLSP_0_*.card $cardmt $cardet $cardmt2017 $cardet2017 $dircTT/mStau_${mass}_mLSP_0_*.card $cardmt $cardet $cardmt2017 $cardet2017 >  $cardnew


#combineCards.py -S $dircTT/mStau_${mass}_mLSP_0_*2016.card $cardmt $cardet >  $cardnew

cp $cardmt2017 $cardnew

fi


if [ $masslsp != "1" ];
then
 
combineCards.py -S $dircTT/mStau_${mass}_mLSP_${masslsp}_*.card $cardmt $cardet $cardmt2017 $cardet2017 >  $cardnew


fi

#python ./../../CombineHarvester/CombineTools/scripts/partialCorrelationEdit.py $cardmt --process TauEn,0.5  --postfix-uncorr _2016  --output-txt new_card2016mt$masslsp.txt --output-root shape${model}${mass}_LSP${masslsp}_left_BDTmutau_${var}2016mt.root
#python ./../../CombineHarvester/CombineTools/scripts/partialCorrelationEdit.py $cardet --process TauEn,0.5  --postfix-uncorr _2016  --output-txt new_card2016et$masslsp.txt --output-root shape${model}${mass}_LSP${masslsp}_left_BDTeltau_${var}2016et.root
#python ./../../CombineHarvester/CombineTools/scripts/partialCorrelationEdit.py $cardmt2017 --process TauEn,0.5  --postfix-uncorr _2017  --output-txt new_card2017mt$masslsp.txt --output-root shape${model}${mass}_LSP${masslsp}_left_BDTmutau_${var}2017mt.root
#python ./../../CombineHarvester/CombineTools/scripts/partialCorrelationEdit.py $cardet2017 --process TauEn,0.5  --postfix-uncorr _2017  --output-txt new_card2017et$masslsp.txt --output-root shape${model}${mass}_LSP${masslsp}_left_BDTeltau_${var}2017et.root
#
#combineCards.py $dircTT/mStau_${mass}_mLSP_0_*2016.card > card2016$masslsp.txt
#combineCards.py $dircTT/mStau_${mass}_mLSP_0_*2017.card > card2017$masslsp.txt
##
#python ./../../CombineHarvester/CombineTools/scripts/partialCorrelationEdit.py card2016$masslsp.txt --process TauEn,0.5  --postfix-uncorr _2016  --output-txt new_card2016$masslsp.txt 
#python ./../../CombineHarvester/CombineTools/scripts/partialCorrelationEdit.py card2017$masslsp.txt --process TauEn,0.5  --postfix-uncorr _2017  --output-txt new_card2017$masslsp.txt


#combineCards.py -S $dircTT/mStau_${mass}_mLSP_0_*.card > $cardnew

#combineCards.py -S  new_card2016$masslsp.txt new_card2017$masslsp.txt > $cardnew2


#combineCards.py -S  new_card2016$masslsp.txt new_card2017$masslsp.txt new_card2016mt$masslsp.txt  new_card2017mt$masslsp.txt  new_card2016et$masslsp.txt  new_card2017et$masslsp.txt > $cardnew2

#combineCards.py -S  new_card2016mt$masslsp.txt  new_card2017mt$masslsp.txt  new_card2016et$masslsp.txt  new_card2017et$masslsp.txt > $cardnew2

#cp shape${model}${mass}_LSP${masslsp}_left_BDTmutau_${var}2016mt.root combined_SR/
#cp shape${model}${mass}_LSP${masslsp}_left_BDTeltau_${var}2016et.root combined_SR/ 
#cp shape${model}${mass}_LSP${masslsp}_left_BDTmutau_${var}2017mt.root combined_SR/ 
#cp shape${model}${mass}_LSP${masslsp}_left_BDTeltau_${var}2017et.root combined_SR/ 
#
#cp $cardnew2 combined_SR/


#combineCards.py -S $dircTT/mStau_${mass}_mLSP_0_*.card > $cardnew

#echo $cardmt
#echo $cardnew
#cp $cardmt2017  $cardnew

#fi

cardd=$cardnew
	cat bss > ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}_${Region}${channel}.sh
	echo   cd $dir >> ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}_${Region}${channel}.sh
	echo mkdir work_${model}_${mass}_LSP${masslsp}_${Region}${channel}${var} >> ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}_${Region}${channel}.sh
	echo cd $dir/work_${model}_${mass}_LSP${masslsp}_${Region}${channel}${var} >> ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}_${Region}${channel}.sh
	echo  source $dir/CreateTableLimits.sh ${model} ${mass} ${masslsp} ${var} ${cut} ${comb} ${lumi} ${cardd} ${Region}${channel} >> ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}_${Region}${channel}.sh
	echo    mv higgsCombine${mass}_LSP${masslsp}_${var}.AsymptoticLimits.mH120.root $dir/Results_${Region}${channel}/${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}invfb.root  >> ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}_${Region}${channel}.sh
	echo cd $dir  >> ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}_${Region}${channel}.sh
	echo rm -fr $dir/work_${model}_${mass}_LSP${masslsp}_${Region}${channel}${var} >> ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}_${Region}${channel}.sh


	chmod 777 ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}_${Region}${channel}.sh	
# 	./HTC_submit.sh  ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}_${Region}${channel}.sh ${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}_${Region}${channel}
echo ${masslsp}
	#if [[ ${masslsp} == "1" ]];	then 
	./ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}_${Region}${channel}.sh ${model}_${mass}_LSP${masslsp}_${var}_${cut}_${comb}_${lumi}_${Region}${channel}
	#fi
	#echo . ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}_${Region}.sh
fi
 	fi
	done
    done
done
done


