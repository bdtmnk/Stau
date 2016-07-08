#!/bin/sh
#
#(make sure the right shell will be used)
#$ -S /bin/sh
#
#(the cpu time for this job)
#$ -l h_cpu=0:5:00
#
#(the maximum memory usage of this job)
#$ -l h_vmem=500M
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

cd /nfs/dust/cms/user/alkaloge/Workdir/CMSSW_7_1_14/src/Limits/STau;  eval `scramv1 runtime -sh` ;

channel=mutau

input=`echo $1 | awk -F "/" '{print $2}'`

process=`echo $input | awk -F "_$channel" '{print $1}'`

xsec=`grep "$process" xsecs | awk -F " " '{print $2}'`


sp=`echo $process |  cut -d "_" -f3 | awk -F "LSP" '{print $2}'`
lsp=`echo $process | cut -d "_" -f2`

echo  $input  process $process and xsecs $xsec for $sp , $lsp

. lim.sh cards/$input > results/limit_$input

#Observed Limit: r < 4.1630
#Expected  2.5%: r < 1.0389
#Expected 16.0%: r < 1.4001
#Expected 50.0%: r < 1.9922
#Expected 84.0%: r < 2.8578
#Expected 97.5%: r < 3.9453

em=`cat results/limit_$input | grep " 50.0" | cut -d "<" -f2`
emp1=`cat results/limit_$input | grep " 84.0" | cut -d "<" -f2`
emm1=`cat results/limit_$input | grep " 16.0" | cut -d "<" -f2`
emp2=`cat results/limit_$input | grep " 97.5" | cut -d "<" -f2`
emm2=`cat results/limit_$input | grep " 2.5" | cut -d "<" -f2`
obs=`cat results/limit_$input | grep "Observed Limit:" | head -1 | cut -d "<" -f2`


echo ================================
echo $em 
echo $emp1 
echo $emp2 
echo $emm1 
echo $emm2 
echo $obs

excl=`echo "scale=3; $em * $xsec" |bc`

#echo $sp $lsp $em $excl $obs $emp1 $emm1 $emp2 $emm2
echo $sp $lsp $em $obs $emp1 $emm1 $emp2 $emm2

