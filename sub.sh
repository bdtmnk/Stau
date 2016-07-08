while read line
do

	qsub run_limits.sh $line

done<$1
