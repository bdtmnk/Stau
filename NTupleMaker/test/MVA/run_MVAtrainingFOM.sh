#methods="MLP1 MLP2 MLP3 MLPGA MLPBFGS1 MLPBFGS2 MLPBFGS3 MLPBNN1 MLPBNN2 MLPBNN3"

#methods="MLPBNN4 MLPBNN5 MLPBNN6 MLPBNN7 MLPBNNmoreHiddenLayers SVM MLPGA1 MLPGA2 MLP1 MLP2"
echo start> logFOM
while read line
do

unset xsec

input=$(echo $line | cut -d " " -f2)
file=$(echo $line | cut -d " " -f1)

echo FOUND INPUT for ${file} to be ${input}

for ii in {1..1}
do

root -l -b -q 'N_FOM.C("'"${input}_${ii}"'","'"${file}_{$ii}2s1j.root"'")' >> logFOM_$file
done
done<$1

