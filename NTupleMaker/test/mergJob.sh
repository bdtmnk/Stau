#!/bin/sh
#
#(make sure the right shell will be used)
#$ -S /bin/sh
#
#(the cpu time for this job)
#$ -l h_cpu=5:25:00
#
#(the maximum memory usage of this job)
#$ -l h_vmem=30000M
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

cd mutau
./merge_data.sh
