while read line
do
	qdel $line
done<$1
