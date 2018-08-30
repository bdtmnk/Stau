#!/bin/sh
#
#(make sure the right shell will be used)
#$ -S /bin/sh
#
#(the cpu time for this job)
#$ -l h_cpu=10:29:00
#
#(the maximum memory usage of this job)
#$ -l h_vmem=5000M
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

cd /nfs/dust/cms/user/bobovnii/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test ;  eval `scramv1 runtime -sh` ;


LSPlist='1 10 20 30'
staulist='100 150 200 250 300'
export X509_USER_PROXY=$HOME/k5-ca-proxy.pem

for stau in $staulist
do
for LSP in $LSPlist
do

point=stau${stau}_LSP${LSP}



ls /pnfs/desy.de/cms/tier2/store/user/ibabouni/FullSim/Step4/Step4_${point}/$1*.root > filesMC${point}
#cat filesMC | head -1  > t 
#mv t

if [[ ! -d Ntuple_${point} ]] ; then
mkdir Ntuple_${point}
fi

while read line 
do

	fname=$(basename $line)
	echo the name is $fname
	if [[ ! -f $PWD/Ntuple_${point}/Ntuple${fname} ]]  && [[ ! -f $PWD/Ntuple_${point}/Ntuple${fname} ]]; then 
	cat bss > ${fname}_exec_${point}.sh

	echo cmsRun Ntuple_${point}/TreeProducerFromMiniAOD_80x_MC25ns_signal_${fname}.py >> ${fname}_exec_${point}.sh


	cp TreeProducerFromMiniAOD_80x_MC25ns_signal_template.py TreeProducerFromMiniAOD_80x_MC25ns_signal_${fname}.py

        sed -i 's/FOLDERIN/'Step4_${point}'/g' TreeProducerFromMiniAOD_80x_MC25ns_signal_${fname}.py
	sed -i 's/FILEIN/'${fname}'/g' TreeProducerFromMiniAOD_80x_MC25ns_signal_${fname}.py
	sed -i 's/FILEOUT/'Ntuple${fname}'/g' TreeProducerFromMiniAOD_80x_MC25ns_signal_${fname}.py
        sed -i 's/FOLDEROUT/'Ntuple_${point}'/g' TreeProducerFromMiniAOD_80x_MC25ns_signal_${fname}.py
	mv TreeProducerFromMiniAOD_80x_MC25ns_signal_${fname}.py Ntuple_${point}/
	echo $fname
	qsub ${fname}_exec_${point}.sh

fi

done <filesMC${point}

done             
done
