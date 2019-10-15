for i in `seq 1 400`
do

	cat bss > good_${i}.sh
	echo combine -M GoodnessOfFit /nfs/dust/cms/user/alkaloge/Workdir/CMSSW_7_4_7/src/Limits/STau/combined_CRB/Bkg_C1N2_100_LSP1_met_MT2lester_DZeta01J1D_17_comb_35invfb.txt --algo=saturated -t 100 -s $i >> good_${i}.sh
	qsub good_${i}.sh -N good_$i

done


