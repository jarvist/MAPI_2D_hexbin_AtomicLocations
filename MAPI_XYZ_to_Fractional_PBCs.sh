# MAPI_XYZ_to_Fractional_PBCs.sh
# Jarvist Moore Frost ~March 2014
# Nothing very clever.

for f 
do

grep "Pb\|Sn\|Ge" "${f}" > HeavyMetal.dat
grep "I\|Br\|Cl" "${f}" > Halogen.dat
grep " C " "${f}" > C.dat

cat HeavyMetal.dat | ./XYZ_to_Fractional_PBCs.awk > HeavyMetal_symm.dat
cat Halogen.dat | ./XYZ_to_Fractional_PBCs.awk > Halogen_symm.dat
cat C.dat | ./XYZ_to_Fractional_PBCs.awk > C_symm.dat

done

