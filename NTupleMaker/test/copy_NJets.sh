

while read line
do


p1=`echo $line | awk -F "_B" '{print $1}'`

	cp $line ${p1}_0Parton_B_OS.root
	cp $line ${p1}_1Parton_B_OS.root
	cp $line ${p1}_2Parton_B_OS.root
	cp $line ${p1}_3Parton_B_OS.root
	cp $line ${p1}_4Parton_B_OS.root
done<$1
