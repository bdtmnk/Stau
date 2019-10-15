## syntax = cards.sh FILE_WITH_2D.root text_with_signal
channel=$4


unset Region
Region=$3

COUNTER=0

cp $2 tempF

'''
if [[ ${Region} != "SR_CR1" && ${Region} != "Stau" ]] ; then

	echo will copy single line
cat $2 | head -1 > tempF

fi
'''
while read line 
do


	
file=$1


if [[ ! -f ${file}.root ]]; then

echo the $1 is not a valid input...
return 0
fi

variable=`echo $1  | cut -d "_" -f2-5`

if [[ $1 == *"Var_"* ]] ; then
variable=`echo $1  | cut -d "_" -f2-4`
fi

echo variable is $variable

lumi=`echo $1 | cut -d "_" -f5 | cut -d "i" -f1`

lumi=35

cardd="$Region/cards_${channel}/${line}_${variable}_${channel}_${lumi}invfb.txt"

if [[ ! -f $cardd ]] ;then

echo Will create the card for channel $channel, signal $line, variable $variable, region $Region and lumi $lumi...

#if [[ $1 -eq "C1N2" ]] ; then
cp CreateDatacards_Stau_C CreateDatacards_${variable}_${channel}_${lumi}.C
#fi


sed  -i  's/CHANNEL/'$channel'/g' CreateDatacards_${variable}_${channel}_${lumi}.C
sed  -i  's/FILEOUT/'$file'_out/g' CreateDatacards_${variable}_${channel}_${lumi}.C
sed  -i  's/FILE/'$file'/g' CreateDatacards_${variable}_${channel}_${lumi}.C
sed  -i  's/VARIABLE/'$variable'/g' CreateDatacards_${variable}_${channel}_${lumi}.C
sed  -i  's/SIGNAL/'$line'/g' CreateDatacards_${variable}_${channel}_${lumi}.C
sed  -i  's/LUMI/'$lumi'/g' CreateDatacards_${variable}_${channel}_${lumi}.C
sed  -i  's/REGION/'$Region'/g' CreateDatacards_${variable}_${channel}_${lumi}.C

if [[ $COUNTER -eq 0 ]];then

	sed -i 's/FLAGG/true/g'  CreateDatacards_${variable}_${channel}_${lumi}.C
	echo Will also write the file....
fi

if [[ $COUNTER -ne 0 ]];then

	sed -i 's/FLAGG/false/g'  CreateDatacards_${variable}_${channel}_${lumi}.C
fi

let let COUNTER=COUNTER+1 

root -q -b -l CreateDatacards_${variable}_${channel}_${lumi}.C

#rm CreateDatacards_${variable}_${channel}_${lumi}.C
#sleep 0.001
fi


done<tempF
