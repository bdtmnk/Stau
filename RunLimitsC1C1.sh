
#variables="DZeta_MTsum DZeta_MTtot met_DZeta met_MCTb met_MT met_MTsum met_MTtot MTsum_MCTb MTtot_MCTb"
variables="MT2lester_MCTb MT2lester_met MT2lester_DZeta"
variables="MT2lester_met"

dirc="/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/CMSSW_8_0_12/src/DesyTauAnalyses/NTupleMaker/test/Processing/01Jets"
comb="comb"

massp=$1
lspp=$2
lumi=16

cut=19

model=$1

if [[ $1 == "*stau*" ]] ; then

model="stau-stau"

fi

if [[ $1 == "C1N2" ]] ; then

model="C1N2"

fi

if [[ $1 == "C1C1" ]] ; then

model="C1C1"

fi

lsprange=$3

echo ============================ $lsprange

#for mass in `seq 100 25 100`
#for mass in 60 70 80 90 100 110 120
for mass in $2
do
    #for masslsp in 1 10 20
    for masslsp in $lsprange
    do
	    #for channel in mt et muel
	    for channel in  $comb
	    do
		echo "--> channel" $channel and $mass , LSP$masslsp



for var in $variables
do

if [[ ! -f  output/${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}invfb.root ]] ; then

cardnew=combined/${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}invfb.txt

if [[ $channel == "comb" ]] && [[ ! -f $cardnew ]] ; then

cardmt=$dirc/MuTau/cards_mt/${model}_${mass}_LSP${masslsp}_${var}_${cut}_mt_${lumi}invfb.txt
cardet=$dirc/ElTau/cards_et/${model}_${mass}_LSP${masslsp}_${var}_${cut}_et_${lumi}invfb.txt
cardme=$dirc/MuEl/cards_me/${model}_${mass}_LSP${masslsp}_${var}_13_me_${lumi}invfb.txt
#cardme=""

cardnew=combined/${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}invfb.txt

#combineCards.py $cardmt $cardet  $cardme > $cardnew

cardd=$cardnew

fi

		cat bss > ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}.sh

		echo     combine -M Asymptotic $cardd -m ${mass} -n ${mass}_LSP${masslsp}_${var} >>ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}.sh
	    #rm ${i}_${model}_et.${2}.txt ${i}_${model}_mt.${2}.txt ${i}_${model}.${2}.txt

	echo    mv higgsCombine${mass}_LSP${masslsp}_${var}.Asymptotic.mH${mass}.root output/${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}invfb.root  >> ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}.sh

echo	qsub -N ${model}_${mass}_${masslsp}_${var} ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}.sh
fi
	done
    done
done
done

