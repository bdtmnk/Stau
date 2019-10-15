source ~/root534.sh
variables="met_MT2lester_DZeta01J1D"
variables="met_MT2lester_DZeta01J1D_17_Nominal BDTmutau_stau150_LSP100My_17_Nominal BDTmutau_stau100_LSP50My_17_Nominal BDTmutau_stau150_LSP1My_17_Nominal BDTmutau_stau200_LSP100My_17_Nominal BDTmutau_stau200_LSP150My_17_Nominal BDTmutau_stau200_LSP1My_17_Nominal BDTmutau_stau200_LSP50My_17_Nominal BDTmutau_stau300_LSP1My_17_Nominal BDTmutau_stau300_LSP200My_17_Nominal BDT_17_Nominal"
#variables="BDT_17_Nominal"
variables="BDTmutau_stau150_LSP100My BDTmutau_stau100_LSP50My BDTmutau_stau150_LSP1My BDTmutau_stau200_LSP100My BDTmutau_stau200_LSP150My BDTmutau_stau200_LSP1My BDTmutau_stau200_LSP50My BDTmutau_stau300_LSP1My BDTmutau_stau300_LSP200My"
variables="BDTmutau"
lumi=35

cut=17

model=$1
Region=$2
masslsp=1

comb="mt"

if [[ $1 == "*stau*" ]] ; then

model="stau-stau_left"
model1="stau"
lmodel="stau"

fi

if [[ $1 == "C1N2" ]] ; then

model1="C1N2"
#model1=$model
lmodel="#chi_{1}^{\pm}/#chi_{2}^{\0}"
fi

if [[ $1 == "C1C1" ]] ; then

model="C1C1"
model1=$model

lmodel="#chi_{1}^{\pm}"
fi

lsprange=`ls Results_$2/${model}_*$var* | awk -F "LSP" '{print $2}' | cut -d "_" -f1 | sort -u | sort -V`
#lsprange="1 10 20"

echo ============================ $lsprange

echo ====================================== $masslsp

for var in $variables
do
	    for channel in  $comb
	    do



#for mass in $2
#do
		echo "--> channel" $channel and $mass , LSP$masslsp
	rm temp



#ls Results_$2/${model}_*_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}invfb.root > temp # for normal workflow

ls Results_$2/${model}_*_LSP${masslsp}_${var}*LSP${masslsp}My*_${cut}_${channel}_${lumi}invfb.root > temp
while read line
do
	stau1=$(echo $line | cut -d "_" -f5)
	stau2=$(echo $line | cut -d "_" -f8)
	line2=$(echo $line | cut -d "_" -f4-9)
	#echo "$stau1"
	#echo "$stau2"
	#echo "$line2"
	echo "$stau2" > temp2
	#sleep 10
	if [  -z $(grep "$stau1" temp2) ]; then sed -i '/'${line2}'/d' temp; fi

done<temp


#		cat bss > ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}.sh

point1=${model1}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}
point=${model}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}

#xmax=`cat temp | sort -V | cut -d "_" -f3 | tail -1 | awk -F "LSP" '{print $2}'`
xmax=`cat temp | sort -V | cut -d "_" -f2 | tail -1`
cat temp | sort -V > list_${model}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}invfb

cp PlotLimit_C PlotLimit${point1}.C

xmax=400
sed -i 's/POINTHERE/'${point1}'/g' PlotLimit${point1}.C
sed -i 's/xmaxHERE/'${xmax}'/g' PlotLimit${point1}.C

sed -i 's/LSPHERE/'${masslsp}'/g' PlotLimit${point1}.C

sed -i 's/FILEHERE/list_'${point}'invfb/g' PlotLimit${point1}.C

sed -i 's/MODELHERE/'${lmodel}'/g' PlotLimit${point1}.C




echo "" > jlimit_${point}.sh

#echo "mkdir -p Plots_${model}/${var}_${cut}_${channel}_${lumi}" >>jlimit_${point}.sh
echo "mkdir  -p Plots_${model}/LSP${masslsp} " >> jlimit_${point}.sh
echo "root -l -q -b PlotLimit${point1}.C"  >> jlimit_${point}.sh
#echo "mv list_${point}invfb.pdf Plots_${model}/${var}_${cut}_${channel}_${lumi}/. " >> jlimit_${point}.sh
#echo "mv list_${point}invfb.pdf Plots_${model}/LSP${masslsp}/. " >> jlimit_${point}.sh



 . jlimit_${point}.sh

#rm jlimit_${point}.sh

#echo qsub -N $point  jlimit_${point}.sh




		done #lspmasses


done   #variables

