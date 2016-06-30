for i in `ls $1[1-9]*.root`
do
f=`echo $i | awk -F ".root" '{print $1}'`
#	ls `pwd`/$i > ../25ns/$f
	ls `pwd`/$i > ../mutau/$f
	ls `pwd`/$i > ../eltau/$f
	ls `pwd`/$i > ../muel/$f
	echo $i | awk -F ".root" '{print $1}' > ../$f

	echo $f
done

