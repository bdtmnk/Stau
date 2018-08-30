
dir=$1

rm datasets${dir}
#sources="/nfs/dust/cms/user/rasp/storage/76x_JECv2_MVAMET0p6/ /nfs/dust/cms/group/susy-desy/Run2/Stau/MC/25ns/76x_JECv2_MVAMET0p6/"
#sources="/nfs/dust/cms/user/rasp/storage/76x_JECv2_MVAMET0p6/"

#sources="/nfs/dust/cms/group/higgs-kit/80x_v1 /nfs/dust/cms/group/higgs-kit/80x_v2 /nfs/dust/cms/group/higgs-kit/80x_SUSY_v1 80x_wMETFilters_v1"
sources="/nfs/dust/cms/user/alkaloge/8025_Moriond17MC_v1 /nfs/dust/cms/user/rasp/ntuples/Moriond17_MC_v1/"
source1="/nfs/dust/cms/group/higgs-kit/SingleElectron_Run2016-03Feb2017"
source2="/nfs/dust/cms/group/higgs-kit/MuonEG_Run2016-03Feb2017/"
source3="/nfs/dust/cms/user/fcost/store/Moriond17_03Feb2017/"
#source3="/nfs/dust/cms/group/susy-desy/Run2/Stau/Data/25ns/8020_23SeptReReco"


alias ls='ls'

#for i in `ls $source/`

for source in $sources
do
for i in `ls $source/`
do
	ls $source/$i/*.root > ${dir}/$i
	echo $i > $i
	echo $i >> datasets${dir}
	

	echo hadd $i.root ${i}_*.root >> ${dir}/merg.sh
	echo rm ${i}_* >> ${dir}/merg.sh
	echo "" >> ${dir}/merg.sh
done
done


ls $source1/SingleElectron*Run2016*/*.root > ${dir}/SingleElectron
ls $source3/SingleMuon*Run2016*/*.root > ${dir}/SingleMuon
ls $source2/MuonEG*/*.root > ${dir}/MuonEG

echo SingleMuon  > SingleMuon
echo SingleElectron > SingleElectron
echo MuonEG > MuonEG

rm GC*
rm ${dir}/GC*

rm *Glu*
rm $dir/*Glu*

rm AToZh*
rm $dir/AToZh*

rm Charged*
rm $dir/Charged*


sed -i '/AToZh/d' datasets$dir
sed -i '/Charged/d' datasets$dir
sed -i '/Glu/d' datasets$dir
sed -i '/GC/d' datasets$dir
