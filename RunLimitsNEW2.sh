


variables="met_MT2lester_DZeta01J1D"
#variables="METHighDzeta METMiddleDzeta METLowDzeta"
#variables="Mt2lestermutauHighDzeta Mt2lestermutauMiddleDzeta Mt2lestermutauLowDzeta METHighDzeta METMiddleDzeta METLowDzeta"

dirc="/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/Processing/01Jets/"

Region=$4

dir=`pwd`
#variables="MT2lester_MCTb"
#variables="met_MCTb"

massp=$1
lspp=$2

lumi=35

comb="comb"

cut=17

model=$1

if [[ $1 == "stau" ]] ; then

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


	if [[ ${mass} -gt ${masslsp} ]] ; then


if [[ ! -f  Results_$Region/mlfit_${channel}.root ]] ; then

#cardnew= $dirc/MuTau/cards_${channel}/${model}_${mass}_LSP${masslsp}_${var}_${cut}_mt_${lumi}invfb.txt


cardmt=$dirc/MuTau/$Region/cards_mt/${model}_${mass}_LSP${masslsp}_${var}_${cut}_mt_${lumi}invfb.txt
cardet=$dirc/ElTau/$Region/cards_et/${model}_${mass}_LSP${masslsp}_${var}_${cut}_et_${lumi}invfb.txt
cardme=$dirc/MuEl/$Region/cards_me/${model}_${mass}_LSP${masslsp}_${var}_18_me_${lumi}invfb.txt



if [[ $5 == "me" ]] ;then

export cardet=""
export cardmt=""
channel="me_only"


elif [[ $5 == "mt" ]]; then

export cardme=""
export cardet=""
channel="mt_only"

elif [[ $5 == "et" ]];then

export cardme=""
export cardmt=""
channel="et_only"


elif [[ $5 == "mt_et" ]] ;then

export cardme=""
channel="mt_et"



else 
	echo "all channels in "
channel="all"

fi

cardnew=$dir/combined_$Region/Bkg_${model}_${mass}_LSP${masslsp}_${var}_${cut}_comb_${lumi}invfb_${channel}.txt

combineCards.py $cardmt $cardet  $cardme > $cardnew

echo will fit $channel now...

mkdir fit_${channel}_${Region}
cd fit_${channel}_${Region}
cp ../Fitting.sh .

	. Fitting.sh $cardnew $Region
	mv mlfit.root ../Results_$Region/mlfit_${var}_${cut}_${channel}.root 
	cd ..
#	rm -fr fit_${channel}_${Region}
fi
 	fi
	done
    done
done
done


