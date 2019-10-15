#!/bin/sh

	model=$1
	mass=$2
	masslsp=$3
	var=$4
	cut=$5
	channel=$6
	lumi=$7
	cardd=$8
	Region=$9

	unset tempfile
	tempfile="temp${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}.log" 
	#combine -M Significance --significance ${cardd} --expectSignal=1 2>&1 | tee  ${tempfile}
	#sigobs=`grep "Significance:" $tempfile | cut -d " " -f2` 
	#echo A posteriori expected `grep  Significance $tempfile`	



	#combine -M Significance --significance $cardd -t -1 --expectSignal=1 --toysFreq  2>&1 | tee  $tempfile 
	#sigobs=`grep "Significance" $tempfile | cut -d " " -f2` 
	#sigexp=`grep "Significance:" $tempfile | awk -F " " '{print $2}'` 
	#echo A priori expected `grep  "Significance" $tempfile` 

	echo Will run for the limit now....
	combine -M AsymptoticLimits $cardd -m 120 -n ${mass}_LSP${masslsp}_${var}   --rMin=0  --rMax=15  2>&1 | tee  $tempfile 
	#combine -M AsymptoticLimits --run blind $cardd -m ${mass} -n ${mass}_LSP${masslsp}_${var} --rMin=0  --rMax=15  2>&1 | tee  $tempfile 

	#combine -M AsymptoticLimits $cardd -m ${mass} -n ${mass}_LSP${masslsp}_${var} -t -1 2>&1 | tee  $tempfile 
	pdown=`grep "Expected 16.0%" $tempfile | cut -d " " -f5` 
	#pdown=`grep "Expected 2.5%" $tempfile | cut -d "<" -f2` 
	pexp=`grep  "Expected 50.0%" $tempfile | cut -d "<" -f2` 
	pup=`grep "Expected 84.0%" $tempfile | cut -d " " -f5` 
	#pup=`grep "Expected 97.5%" $tempfile | cut -d "<" -f2` 
	pobs=`grep "Observed Limit: r <"  $tempfile | cut -d "<" -f2` 
	echo A priori `grep "Expected 16.0%" $tempfile` 
	echo A priori `grep "Expected 50.0%" $tempfile` 
	echo A priori `grep "Expected 84.0%" $tempfile` 
	echo  "Observed Limit: r <"  $pobs 


	pmx=${mass} 
	pmy=${masslsp}

	#pxsec=`grep "${model}_${mass}_LSP${masslsp} " xsecs | cut -d " " -f3` 
	pxsec=`grep "stau_${mass}_" /nfs/dust/cms/user/alkaloge/Workdir/CMSSW_8_1_0/src/Limits/xsecs | cut -d " " -f3 | sort -u` 
	echo XSEC $pxsec for "$stau-stau_left_${mass}_LSP${masslsp}"
	#pobs=$pobs 
	pobsup=$pup
	pobsdown=$pdown
	#pobs=$pexp
 	echo " "$pmx $pmy $pxsec $pobs $pobsup $pobsdown $pexp $pup $pdown $sigobs $sigexp 
 	echo " "$pmx $pmy $pxsec $pobs $pobsup $pobsdown $pexp $pup $pdown $sigobs $sigexp > /nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_1_0/src/Limits/STau/Tables_$Region/TABLE${model}_${mass}_LSP${masslsp}_${var}_${cut}_${channel}_${lumi}invfb_${Region}
	#rm $tempfile
