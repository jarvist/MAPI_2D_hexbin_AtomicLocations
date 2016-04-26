# MAPI_XYZ_to_Fractional_PBCs.sh
# Jarvist Moore Frost ~March 2014
# Nothing very clever.

for f 
do

grep Pb "${f}" > Pb.dat
grep I "${f}" > I.dat
grep " C " "${f}" > C.dat

cat Pb.dat | ./XYZ_to_Fractional_PBCs.awk > Pb_symm.dat
cat I.dat | ./XYZ_to_Fractional_PBCs.awk > I_symm.dat
cat C.dat | ./XYZ_to_Fractional_PBCs.awk > C_symm.dat

done

