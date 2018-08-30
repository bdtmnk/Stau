#!/bin/sh
#
#(make sure the right shell will be used)
#$ -S /bin/sh
#
#(the cpu time for this job)
#$ -l h_cpu=1:29:00
#
#(the maximum memory usage of this job)
#$ -l h_vmem=1500M
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



cd /nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test;eval `scramv1 runtime -sh` ;


dir="/nfs/dust/cms/user/alkaloge/TauAnalysis/new/new/StauAnalysis/New8025/CMSSW_8_0_25/src/DesyTauAnalyses/NTupleMaker/test"

channel=$2
channel2=$2
btag="0.8484"


#systematics="Nominal JetEnUp JetEnDown UnclEnUp UnclEnDown TopPt ZPtUp  ZPtDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown"
#systematics="Nominal"
#systematics="TopPtUp TopPtDown"
#systematics="Nominal  ZPtUp  ZPtDown"
#systematics="Nominal JetEnUp JetEnDown UnclEnUp UnclEnDown TopPt ZPtUp  ZPtDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown"
#systematics="Nominal JetEnUp JetEnDown"


systematics="$3"

if [[  $3 == "list" ||  $3 == "all" ]];then
systematics="Nominal TopPtUp TopPtDown ZPtUp ZPtDown JetEnUp JetEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown UnclEnUp UnclEnDown genMET ScalesDown ScalesUp PDFUp PDFDown BTagUp BTagDown METRecoilUp METRecoilDown"
systematics="Nominal JetEnUp JetEnDown TopPtUp TopPtDown ZPtUp ZPtDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown UnclEnUp UnclEnDown ScalesDown ScalesUp PDFUp PDFDown BTagUp BTagDown METRecoilUp METRecoilDown TFRJetEnUp TFRJetEnDown TFRMuEnUp TFRMuEnDown TFRTauEnUp TFRTauEnDown"
#systematics="Nominal JetEnUp JetEnDown TopPtUp TopPtDown ZPtUp ZPtDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown UnclEnUp UnclEnDown genMET ScalesDown ScalesUp PDFUp PDFDown"
#systematics="JetEnUp JetEnDown UnclEnUp UnclEnDown"
fi

if [[  $3 == "listme" ]];then
systematics="Nominal JetEnUp JetEnDown TopPtUp TopPtDown ZPtUp ZPtDown ElEnUp ElEnDown MuEnUp MuEnDown UnclEnUp UnclEnDown ScalesDown ScalesUp PDFUp PDFDown BTagUp BTagDown METRecoilUp METRecoilDown"
fi

if [[  $3 == "listSignal" ]];then
systematics="Nominal JetEnUp JetEnDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown UnclEnUp UnclEnDown genMET ScalesDown ScalesUp PDFUp PDFDown BTagUp BTagDown EWKUp EWKDown"
#systematics="ScalesDown ScalesUp PDFUp PDFDown"
#systematics="Nominal ScalesUp ScalesDown genMET"
fi

if [[  $3 == "New" ]];then
systematics="genMET ScalesDown ScalesUp PDFUp PDFDown BTagUp BTagDown METRecoilUp METRecoilDown"
#systematics="Nominal JetEnUp JetEnDown TopPtUp TopPtDown ZPtUp ZPtDown TauEnUp TauEnDown ElEnUp ElEnDown MuEnUp MuEnDown UnclEnUp UnclEnDown genMET ScalesDown ScalesUp PDFUp PDFDown"
fi


if [[  $3 == "listTT" ]];then
systematics="Nominal JetEnUp JetEnDown TopPtUp TopPtDown ZPtUp ZPtDown ElEnUp ElEnDown MuEnUp MuEnDown UnclEnUp UnclEnDown ScalesDown ScalesUp PDFUp PDFDown BTagUp BTagDown METRecoilUp METRecoilDown"
#systematics="JetEnUp JetEnDown ElEnUp ElEnDown MuEnUp MuEnDown UnclEnUp UnclEnDown BTagUp BTagDown"
#systematics="Nominal  TopPtUp TopPtDown ZPtUp ZPtDown ElEnUp ElEnDown MuEnUp MuEnDown UnclEnUp UnclEnDown ScalesDown ScalesUp PDFUp PDFDown BTagUp BTagDown METRecoilUp METRecoilDown"
fi

if [[  $3 == "listDY" ]];then
systematics="Nominal JetEnUp JetEnDown ZPtUp ZPtDown MuEnUp MuEnDown UnclEnUp UnclEnDown ScalesDown ScalesUp PDFUp PDFDown METRecoilUp METRecoilDown"

fi

if [[  $3 == "listWJ" ]];then
systematics="Nominal ZpTUp ZPtDown TopPtUp TopPtDown JetEnUp JetEnDown MuEnUp MuEnDown UnclEnUp UnclEnDown ScalesDown ScalesUp PDFUp PDFDown METRecoilUp METRecoilDown  BTagUp BTagDown"
#systematics="JetEnUp JetEnDown MuEnUp MuEnDown UnclEnUp UnclEnDown METRecoilUp METRecoilDown  BTagUp BTagDown"

fi

if [[ -z $3 ]];then
systematics="Nominal"
echo You will run with nominal systematics
fi

if [[ $2 == "Ttemplate" ]] 
then
	channel2="muel"
fi

if [[  $2 == *"fakesmu"* || $2 == *"TFR"*   || $2 == "WJetsmu" ]]
then
	channel2="mutau"
fi



###########start looking 
while read line
do

#unset isDataSyst
isDataSyst=0

unset isSystTopZpt
export isSystTopZPt=0


for syst in $systematics
do

unset file
file=`echo $line | cut -d '/' -f2`
unset fileB
fileB=`echo $file | awk -F "_B_OS" '{print $1}'`
	
mkdir dir_${file}_${channel}_$syst
cd dir_${file}_${channel}_$syst
echo ==============================================


if [[ $file == *"Single"* || $file == *"MuonEG"* ]] && [[ $syst != "Nominal" ]]; then

	echo For data we dont run systematics....
isDataSyst=1
fi

if  [[ $syst == "genMET" ]]; then

#if [[ $file == *"stau"* || $file == *"Chi"* || $file == *"C1"* ]] ; then
#if [[  $file == *"Chi"*  ]] ; then

isDataSyst=0
	echo we will run genMET syst only for signal ....$file , isData $isDataSyst
#fi

fi



if [[ $isDataSyst == 0 ]] ; then

if [[ $line == *"stau"* || $line == *"C1"* || $line == *"Chi"* ]] ; then
lsp=`echo $line | awk -F "_LSP" '{print $2}' | cut -d '_' -f1`
else
lsp=0

fi


cp $dir/analyzerTFRInvertTau_h .
cp $dir/analyzer${channel}_C .


#cp $dir/analyzerTFRInvertTau_hInvMET_C .

#fi


echo $line , $fileB


if [[ $file == *"B_OS"* ]];then


######### B region non inverted OS

#if [[ ! -f $dir/plots_$channel/${fileB}_${syst}_B.root  ]] && [[ ! -f $dir/plots_$channel/${fileB}_B.root ]]  &&  [[ $file != *"stau"* && $file != *"C1"* ]]; then
#if [[ ! -f $dir/plots_$channel/${fileB}_B.root  ]]   &&  [[ $file == *"stau"* || $file == *"C1"*  ||  $file == *"Chi"*  ==  $file == *"TFRInvertTau"* ]]; then
if [[ ! -f $dir/plots_$channel/${fileB}_Nominal_B.root  ]] ;
then

cp analyzerTFRInvertTau_h analyzer.h
echo cp analyzer${channel}_C analyzer.C
cp analyzer${channel}_C analyzer.C
cp $dir/plotsFakes.h plots.h
cp $dir/runme.C .

echo the filein : $file , the fileout : ${fileB}_B.root NonInvertedLepton OS
sed -i 's/FILEIN/'$file'/g' analyzer*
sed -i 's/LEPTONHERE/false/g' analyzer.C
sed -i 's/SIGNHERE/OS/g' analyzer.C
sed -i 's/CHANNELHERE/'$channel2'/g' analyzer*
sed -i 's/BTAGCUT/'$btag'/g' analyzer*
sed -i 's/CHIMASSS/'$lsp'/g' analyzer*C


export fileB=${fileB}_${syst}


sed -i 's/SYSTEMATICHERE/'$syst'/g' analyzer*


rm plots.root
root -l -q -b runme.C 
mv plots.root $dir/plots_$channel/${fileB}_B.root

fi




cd ${dir}

rm -fr dir_${file}_${channel}_$syst
fi

fi
done
done<$1
