
variables="DZeta_MTsum DZeta_MTtot met_DZeta met_MCTb met_MT met_MTsum met_MTtot MTsum_MCTb MTtot_MCTb"


massp=$1
lspp=$2
lumi=12000

cut=13

model=$1

if [[ $1 == "stau" ]] ; then

model="stau_stau"
lmodel="#stau"

fi

if [[ $1 == "C1N2" ]] ; then

model="C1N2_"
lmodel="#chi_{1}^{\pm}/#chi_{2}^{\0}"
fi

if [[ $1 == "C1C1" ]] ; then

model="C1C1_"

lmodel="#chi_{1}^{\pm}"
fi

lsprange=$3

echo ============================ $lsprange

for var in $variables
do
    for masslsp in $lsprange
    do

	    for channel in  comb
	    do



#for mass in $2
#do
		echo "--> channel" $channel and $mass , LSP$masslsp
	rm temp



ls output/${model}_*_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}invfb.root > temp


#		cat bss > ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}.sh

point=${model}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}

xmax=`cat temp | sort -V | cut -d "_" -f3 | tail -1`
cat temp | sort -V > list_${model}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}invfb

cp PlotLimit_C PlotLimit${point}.C


sed -i 's/POINTHERE/'${point}'/g' PlotLimit${point}.C
sed -i 's/xmaxHERE/'${xmax}'/g' PlotLimit${point}.C

sed -i 's/LSPHERE/'${masslsp}'/g' PlotLimit${point}.C

sed -i 's/FILEHERE/list_'${point}'invfb/g' PlotLimit${point}.C

sed -i 's/MODELHERE/'${lmodel}'/g' PlotLimit${point}.C




cat bss > jlimit_${point}.sh

echo "mkdir -p Plots_${model}/${var}_${cut}_${channel}_${lumi}" >>jlimit_${point}.sh
echo "root -l -q -b PlotLimit${point}.C"  >> jlimit_${point}.sh
echo "mv list_${point}invfb.pdf Plots_${model}/${var}_${cut}_${channel}_${lumi}/. " >> jlimit_${point}.sh

. jlimit_${point}.sh

rm jlimit_${point}.sh

#echo qsub -N $point  jlimit_${point}.sh




		done #lspmasses


    done	#channel
done   #variables

