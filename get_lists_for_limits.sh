variables="BDTmutau_stau100_LSP50My_15 BDTmutau_stau100_LSP1MyNew_15 BDTmutau_stau150_LSP100My_15 BDTmutau_stau150_LSP1MyNew_15 BDTmutau_stau150_LSP50My_15 BDTmutau_stau200_LSP100My_15 BDTmutau_stau200_LSP150My_15 BDTmutau_stau200_LSP1MyNew_15 BDTmutau_stau200_LSP50My_15 BDTmutau_stau300_LSP1MyNew_15"

variables="Stau100_16 Stau150_16 Stau200_16"

#variables="BDTmutau"

lumi=35

cut=15

model=$1
Region=$2


comb="comb"

if [[ $1 == "*left*" ]] ; then

model="stau-stau_left"
model1="stau"
lmodel="#stau"

fi
if [[ $1 == "*right*" ]] ; then

model="stau-stau_right"
model1="stau"
lmodel="#stau"

fi
if [[ $1 == "*max*" ]] ; then

model="stau-stau_max"
model1="stau"
lmodel="#stau"

fi

if [[ $1 == "C1N2" ]] ; then

model="C1N2"
model1=$model
lmodel="#chi_{1}^{\pm}/#chi_{2}^{\0}"
fi

if [[ $1 == "C1C1" ]] ; then

model="C1C1"
model1=$model

lmodel="#chi_{1}^{\pm}"
fi

lsprange=`ls Results_$2/${model}_*$var* | awk -F "LSP" '{print $2}' | cut -d "_" -f1 | sort -u | sort -V`
lsprange="1"

echo ============================ $lsprange

for var in $variables
do
    for masslsp in $lsprange
    do
echo ====================================== $masslsp
	    for channel in  comb
	    do



#for mass in $2
#do
		echo "--> channel" $channel and $mass , LSP$masslsp
	rm temp



#ls Results_$2/${model}_*_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}invfb.root > temp

#echo Results_Systmutau/stau-stau_left_90_LSP${masslsp}_BDTmutau_stau100_LSP1MyNew_15_15_comb_35invfb.root > temp
#echo Results_Systmutau/stau-stau_left_100_LSP${masslsp}_BDTmutau_stau100_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_Systmutau/stau-stau_left_125_LSP${masslsp}_BDTmutau_stau100_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_Systmutau/stau-stau_left_150_LSP${masslsp}_BDTmutau_stau150_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_Systmutau/stau-stau_left_175_LSP${masslsp}_BDTmutau_stau150_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_Systmutau/stau-stau_left_200_LSP${masslsp}_BDTmutau_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_Systmutau/stau-stau_left_225_LSP${masslsp}_BDTmutau_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_Systmutau/stau-stau_left_250_LSP${masslsp}_BDTmutau_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_Systmutau/stau-stau_left_275_LSP${masslsp}_BDTmutau_stau300_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_Systmutau/stau-stau_left_300_LSP${masslsp}_BDTmutau_stau300_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_Systmutau/stau-stau_left_350_LSP${masslsp}_BDTmutau_stau300_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_Systmutau/stau-stau_left_400_LSP${masslsp}_BDTmutau_stau300_LSP1MyNew_15_15_comb_35invfb.root >> temp



echo Results_SR/Stau_90_LSP${masslsp}_Stau100_16_15_comb_35invfb.root > temp
echo Results_SR/Stau_100_LSP${masslsp}_Stau100_16_15_comb_35invfb.root >> temp
echo Results_SR/Stau_125_LSP${masslsp}_Stau100_16_15_comb_35invfb.root >> temp
echo Results_SR/Stau_150_LSP${masslsp}_Stau200_16_15_comb_35invfb.root >> temp
echo Results_SR/Stau_175_LSP${masslsp}_Stau200_16_15_comb_35invfb.root >> temp
echo Results_SR/Stau_200_LSP${masslsp}_Stau100_16_15_comb_35invfb.root >> temp
#echo Results_SR/Stau_225_LSP${masslsp}_Stau200_16_15_comb_35invfb.root >> temp
#echo Results_SR/Stau_250_LSP${masslsp}_Stau200_16_15_comb_35invfb.root >> temp
#echo Results_SR/Stau_275_LSP${masslsp}_Stau200_16_15_comb_35invfb.root >> temp
#echo Results_SR/Stau_300_LSP${masslsp}_Stau200_16_15_comb_35invfb.root >> temp
#echo Results_SR/Stau_350_LSP${masslsp}_Stau200_16_15_comb_35invfb.root >> temp
#echo Results_SR/Stau_400_LSP${masslsp}_Stau200_16_15_comb_35invfb.root>> temp


#echo Results_SR/stau-stau_left_90_LSP${masslsp}_stau200_LSP1MyNew_15_15_comb_35invfb.root > temp
#echo Results_SR/stau-stau_left_100_LSP${masslsp}_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_SR/stau-stau_left_125_LSP${masslsp}_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_SR/stau-stau_left_150_LSP${masslsp}_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_SR/stau-stau_left_175_LSP${masslsp}_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_SR/stau-stau_left_200_LSP${masslsp}_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_SR/stau-stau_left_225_LSP${masslsp}_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_SR/stau-stau_left_250_LSP${masslsp}_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_SR/stau-stau_left_275_LSP${masslsp}_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_SR/stau-stau_left_300_LSP${masslsp}_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_SR/stau-stau_left_350_LSP${masslsp}_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp
#echo Results_SR/stau-stau_left_400_LSP${masslsp}_stau200_LSP1MyNew_15_15_comb_35invfb.root >> temp


#		cat bss > ljob_${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}.sh

point1=${model1}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}
point=${model}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}

#xmax=`cat temp | sort -V | cut -d "_" -f3 | tail -1 | awk -F "LSP" '{print $2}'`
xmax=`cat temp | sort -V | cut -d "_" -f2 | tail -1`
cat temp | sort -V > list_${model}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}invfb
cat temp | sort -V > list_${model}_LSP${masslsp}

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


    done	#channel
done   #variables
