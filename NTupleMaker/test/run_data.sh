#!/bin/sh
#
#(make sure the right shell will be used)
#$ -S /bin/sh
#
#(the cpu time for this job)
#$ -l h_cpu=2:29:00
#
#(the maximum memory usage of this job)
#$ -l h_vmem=1000M
#
#(use hh site)
#$ -l site=hh
#(stderr and stdout are merged together to stdout)
#$ -j y
#
# use SL5
#$ -l os=sld6
#
# use current dir and current environment
#$ -cwd
#$ -V
#
#
#mkdir $1

cd $PWD;
eval `scramv1 runtime -sh`
channel=$2 
dir=$2



if [ ! -d Jobs_data_${channel} ]
then
	mkdir Jobs_data_${channel}
fi


cp *.conf Jobs_data_${channel}/.

while read line
do

ct=`ls ${dir}/${line}*_B_OS.root | wc -l`
ctt=`cat ${dir}/${line} | wc -l`


echo There are  $ct out of $ctt for $line in $dir dir for systematic $syst

if [[ $ct -ge $ctt ]] ;then
        continue;
fi

unset xsec
xsec=1
echo FOUND XSEC for $line to be $xsec
echo $f
unset f
while read f
	do



echo $f
unset bas
bas=`basename $f | awk -F ".root" '{print $1}'`


#echo $bas $xsec >> xsecs
echo $bas $xsec 

if [ ! -f $dir/${bas}_B_OS.root ]
then
	echo $dir/${bas}_B_OS_DataDriven.root
echo $f > $dir/$bas
cat bss > Jobs_data_${channel}/job$line${channel}$dir${bas}_B.sh
echo SUSY${channel} analysisMacroSUSY_Data_B.conf ${bas} $dir 1 >> Jobs_data_${channel}/job$line${channel}$dir${bas}_B.sh
chmod u+x Jobs_data_${channel}/job$line${channel}$dir${bas}_B.sh

wr=$3
if [[ ${wr} == grid ]] ; 
then
	./HTC_submit.sh Jobs_data_${channel}/job$line${channel}$dir${bas}_B.sh ${bas} 
else
	. Jobs_data_${channel}/job$line${channel}$dir${bas}_B.sh 
fi

fi





done<$dir/$line
done<$1



