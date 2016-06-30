model=$1
##for c1n2 c1c1
ls RootFiles/$model*run*.root  | cut -d '_' -f1-3 | sort -u  | cut -d "/" -f2 > temp

#for stau
#ls RootFiles/stau2*run*.root  | cut -d '_' -f2-3 | sort -u > temp

while read line
do
if [[ ! -f ${line}.root ]] 
then

hadd -f -k ${line}.root RootFiles/${line}_*.root
#hadd -f $line.root ${line}_*run*.root
fi
done <temp
