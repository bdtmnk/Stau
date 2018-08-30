while read line 
do
	echo $line | cut -d " " -f1
done<$1
