Documantation for mutau and eltau Stau analysis

From Ntuples to datacards:

Short overwiew: 

1) Produce skimms
2) Produce histogramms in control (for corrections) and signal regions (for data to MC agreement)
3) Train MVA and optimize MVA method
4) Produce histogramms for MVA approach
5) Produce histogramms with uncertainty source up and down variation 
6) Produce datdacards and root file with all shapes



PRODUCE SKIMMS

main code: 

DesyTauAnalyses/NTupleMaker/bin/AnalysisMacroSUSYeltau.cpp
DesyTauAnalyses/NTupleMaker/bin/AnalysisMacroSUSYmutau.cpp

Update Triggers, all ID recommendations, PU file and etc.

how to run:

SUSY$channel analysisMacroSUSY_${type}_B.conf ${fileName with all pathes to Ntuples} ${channel} 1 $systematic

usefull script: 
./list.sh $channel #creats list of Ntuples, merg.sh and delete.sh scripts for deleting and merging skimms

Wrapper for data to send jobs (IMPORTANT!!! check output root file before sending hundrends jobs!!!):
run_dataHTC.sh
run_mc2HTC.sh

example:
./run_dataHTC.sh {filelist} {channel} grid 
./run_mc2HTC.sh {filelist} {channel} 

Skimms appear in the folder: tast/${channel}_${systematic} 

For many systematic sources just use corresponding option in run_dataHTC.sh/run_mc2HTC.sh
Check that all folders test/${channel}_${systematic} exist and have list of ntuples.

use ${channel}/merg.sh and delete.sh to merge skimms and delete separrate files.
use 









