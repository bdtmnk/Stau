

 cp DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_isZTT.root
 cp DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_isZTT.root
 cp DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_isZTT.root
 cp DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_isZTT.root
 cp DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_isZTT.root


cp DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.root DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_isZTT.root

files="DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_isZTT DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8 WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8"

for line in $files
do


	cp ${line}.root ${line}_0Parton.root
	cp ${line}.root ${line}_1Parton.root
	cp ${line}.root ${line}_2Parton.root
	cp ${line}.root ${line}_3Parton.root
	cp ${line}.root ${line}_4Parton.root
done


