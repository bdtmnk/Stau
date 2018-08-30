
systematics="JetEnUp JetEnDown UnclEnUp UnclEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown BTagUp BTagDown"
systematics="BTagDown"

sed -n '/JetEnUp/,/JetEnDown/p'  log_hadd > JetEnUpl

grep "probably" JetEnUpl | awk -F "file " '{print $2}' | awk -F "probably" '{print $1}' > temp ; mv temp JetEnUpl

sed -n '/JetEnDown/,/UnclEnUp/p'  log_hadd > JetEnDownl
grep "probably" JetEnDownl | awk -F "file " '{print $2}' | awk -F "probably" '{print $1}' > temp ; mv temp JetEnDownl


sed -n '/UnclEnUp/,/UnclEnDown/p'  log_hadd >  UnclEnUpl
grep "probably" UnclEnUpl | awk -F "file " '{print $2}' | awk -F "probably" '{print $1}' > temp ; mv temp UnclEnUpl


sed -n '/UnclEnDown/,/TauEnUp/p'  log_hadd > UnclEnDownl
grep "probably" UnclEnDownl | awk -F "file " '{print $2}' | awk -F "probably" '{print $1}' > temp ; mv temp UnclEnDownl


sed -n '/TauEnUp/,/TauEnDown/p'  log_hadd > TauEnUpl
grep "probably" TauEnUpl | awk -F "file " '{print $2}' | awk -F "probably" '{print $1}' > temp ; mv temp TauEnUpl


sed -n '/TauEnDown/,/ElEnUp/p'  log_hadd > TauEnDownl
grep "probably" TauEnDownl | awk -F "file " '{print $2}' | awk -F "probably" '{print $1}' > temp ; mv temp TauEnDownl


sed -n '/ElEnUp/,/ElEnDown/p'  log_hadd > ElEnUpl
grep "probably" ElEnUpl | awk -F "file " '{print $2}' | awk -F "probably" '{print $1}' > temp ; mv temp ElEnUpl


sed -n '/ElEnDown/,/MuEnUp/p'  log_hadd > ElEnDownl
grep "probably" ElEnDownl | awk -F "file " '{print $2}' | awk -F "probably" '{print $1}' > temp ; mv temp ElEnDownl


sed -n '/MuEnUp/,/MuEnDown/p'  log_hadd > MuEnUpl
grep "probably" MuEnUpl | awk -F "file " '{print $2}' | awk -F "probably" '{print $1}' > temp ; mv temp MuEnUpl


sed -n '/MuEnDown/,/BTagUp/p'  log_hadd > MuEnDownl
grep "probably" MuEnDownl | awk -F "file " '{print $2}' | awk -F "probably" '{print $1}' > temp ; mv temp MuEnDownl


sed -n '/BTagUp/,/BTagDown/p'  log_hadd > BTagUpl
grep "probably" BTagUpl | awk -F "file " '{print $2}' | awk -F "probably" '{print $1}' > temp ; mv temp BTagUpl

cat JetEnUpl > l
cat JetEnDownl >> l
cat UnclEnUpl >> l
cat UnclEnDownl >> l
cat TauEnUpl >> l
cat TauEnDownl >> l
cat MuEnUpl >> l
cat MuEnDownl >> l
cat ElEnUpl >> l
cat ElEnDownl >> l
cat BTagUpl >> l
cat BTagDownl >> l

for syst in $systematics 
do
	
	while read line

	do
		echo rm mutau_$syst/$line 
	done<${syst}l

done


#while read line
#do
#	rm $1/$line
#done<f




