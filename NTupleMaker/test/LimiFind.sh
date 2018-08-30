#!/bin/sh
#
#(make sure the right shell will be used)
#$ -S /bin/sh
#
#(the cpu time for this job)
#$ -l h_cpu=2:25:00
#
#(the maximum memory usage of this job)
#$ -l h_vmem=1500M
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

cd /nfs/dust/cms/user/bobovnii/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test/;eval `scramv1 runtime -sh` ;
export X509_USER_PROXY=$HOME/k5-ca-proxy.pem

echo start > LumiDY1Jets3

while read line
do

echo ================= File
echo ================= File >> LumiDY1Jets3
echo $line
echo $line >> LumiDY1Jets3
edmLumisInFiles.py root://cms-xrd-global.cern.ch/$line >> LumiDY1Jets3

done <listDY1J_2

