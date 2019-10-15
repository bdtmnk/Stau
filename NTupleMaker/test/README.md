Documantation for mutau and eltau Stau analysis
From Ntuples to datacards.

For analysis details check my Thesis: 
	http://inspirehep.net/record/1751235/
	Search for supersymmetry with tau leptons in the CMS experiment
	Illia Babounikau (DESY)
	2019 - 205 pages
    Hamburg: Verlag Deutsches Elektronen-Synchrotron (2019)
    (2019)
    DOI: 10.3204/PUBDB-2019-03086
    DESY-THESIS-2019-020
    Experiment: CERN-LHC-CMS

nfs path:
/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_9_4_0_patch1/src/DesyTauAnalyses/NTupleMaker/

Short overwiew: 

1) Produce skimms
2) Produce histogramms in control (for corrections) and signal regions (for data to MC agreement)
3) Make nice control plots
4) Train MVA and optimize MVA method
5) Produce histogramms for MVA approach (histogramms with uncertainty source up and down variation)
6) Produce datdacards and root file with all shapes

I wouldn't recommend to run any codes/skripts without looking inside and understnading. 

1 PRODUCE SKIMMS

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
use ${channel}/copy_NJets.sh to copy DY and WJets with naming for isZTT and NParton category


2 PRODUCE HISTOGRAMMS
with some set of cuts

main codes: 
analyzermutau_C
analyzereltau_C
analyzer_h <-new variables
plots.h <- new Transfer factores for datadriven estimation fake estimation

Create a list of files

ls ${channel}/*.root > list${channel}

send jobs

./subm_plots.sh list${channel} ${channel}

It uses run_plots_newDataDriven.sh to create A and B (SR) regions (for datadriven estimation)
Root file with histos should arrive to plots_${channel} directory.

In addition: 
run_plots_newTF.sh creates C and D regions for datadriven fake estimation
run_plots_newCR.sh creates some CRs populated by  DY and WJets (can be used for normalization estimation)
run_plots_newWW.sh creates some CRs with WW events

For Transfer factor calculation use plots_$channel/OverlapTF.C after getting all C and D regions.
It produces text file with all transfer factors to be inserted in plots.h
For histos for fakes estimation use plots_$channel/OverlapTauFakes.C after getting all A regions -> it will produce Fakes_${syst}_B.root

example of running: root -l -b -q OverlapTF.C

For all systematics sources:
make_TF.sh
make_Fakes.sh

Check all cross sections, background normalization and etc. 

3 MAKING NICE CONTROL PLOTS

in plots_${channel}

use older root....
module load root/5.32 

root -l -b -q OverlapWDD.C #produces nice plots defined inside and move them to the folder TauWDD.

Check all cross sections, background normalization and DATA/Backgrund agreement. 

4 TRAIN and TESTING MVA

all codes are in test/MVA/

main code - myTMVA.C makes preselection from flat trees in mutau_${channel} and train MVA with optional parameters. 
Outputs are root files with smaller trees and MVA discriminator, and *.C classe for MVA discriminator to be used in plots.h

run_MVAtrainingMy.sh can send many jobs for training with different options (can be used for hyperparameter optimization) and signal points

N_FOM.C makes FOM plots for MVA testing

run_MVAtrainingFOM.sh runs N_FOM.C for several trainings. 

example:

./run_MVAtrainingFOM.sh listStauFullSim
./N_FOM.C listfom

5 FINAL MVA HISTOS

After implementing MVA discriminator in plots.h rerun subm_plots.sh to get again histos for A and B regions for central value
 and up and down systematic variation, OverlapTauFakes.C to reproduce fakes and OverlapWDD.C to check agreeement.

If you have all systematic in place run: 
OverlapVarsCR.C for creating root file with MVA disctiminators distribution for all bkgs, signals, systematic vatiations and data.
(OverlapVarsCRdegen.C for degenerate scenatio)

wrapper: 
./make_TemplateRootFilesVarsCR.sh

IMPORTANT!!! check carefully output root files. 

move to Syst:
cd Syst

./wrapper_cards.sh stau-stau_left # produces datacards and shapes in ./SR/cards_mt/ to be used in limits production

it uses script cards.sh and code CreateDatacards_Stau_C

usefull tools

OverlapAllSyst.C can be usufull for plotting all systematic sources on one histo
TableForUnrolledDistrSyst.C creates table with event yields.

Now, go to branch limits to run limits 
 

























