#methods="MLP1 MLP2 MLP3 MLPGA MLPBFGS1 MLPBFGS2 MLPBFGS3 MLPBNN1 MLPBNN2 MLPBNN3"

#methods="MLPBNN4 MLPBNN5 MLPBNN6 MLPBNN7 MLPBNNmoreHiddenLayers SVM MLPGA1 MLPGA2 MLP1 MLP2"

while read line
do

unset xsec

xsec=$(echo $line | cut -d " " -f2)
file=$(echo $line | cut -d " " -f1)
echo FOUND XSEC for ${file} to be ${xsec}

cat bss > job${file}.sh
echo root -l -b -q "'"'myTMVA.C("","'TMVA_nonorm_${file}.root'","'mutau_${file}'",'${xsec}',"'${file}'")'"'" ">" logTMVA_nonorm_$file >> job${file}.sh
chmod 777 job${file}.sh
qsub job${file}.sh
#./job${file}.sh
done<$1
