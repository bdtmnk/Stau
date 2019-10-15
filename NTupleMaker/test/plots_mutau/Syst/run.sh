variables="MET METFB hDZeta Mt2lestermutau"
variables="Mt2lestermutau hDZeta MET"

channel=MuTau
cut=17

chan=mt

for var in $variables
do

if [[ -f Var_${var}_${cut}_35invfb_${chan}_CRB.root ]] ; then

unset file
file=Var_${var}_${cut}_35invfb_${chan}_CRB

	cp PlotsForUnrolledDistrSyst_C PlotsForUnrolledDistrSyst.C
	sed -i 's/FILEHERE/'$file'/g' PlotsForUnrolledDistrSyst.C
	sed -i 's/VARIABLEHERE/'$var'/g' PlotsForUnrolledDistrSyst.C
	sed -i 's/CHANNELHERE/'$channel'/g' PlotsForUnrolledDistrSyst.C
	sed -i 's/CUTT/'$cut'/g' PlotsForUnrolledDistrSyst.C
	root -l -q -b PlotsForUnrolledDistrSyst.C

fi
done
