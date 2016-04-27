for i
do
 echo "Processing ${i}"
 
 prefix="${i%.*}" # loop off extension

 # Calculate Trace of POSCAR unit cell thingy at the top, divided by two (size of unit cell, assuming 2x2x2 supercell)
 unitcell=` cat "${prefix}.POSCAR" | awk 'BEGIN{v=0.0} NR==3{v=v+$1} NR==4{v=v+$2} NR==5{v=v+$3} END{print (v/3)/2}' `
 
 grep "Pb\|Sn\|Ge" "${i}" > HeavyMetal.dat
 grep "I\|Br\|Cl" "${i}" > Halogen.dat
 grep " C \|Cs" "${i}" > C.dat

# unitcell optionally passed to the AWK PBC program to chop PBCs at a different place
 cat HeavyMetal.dat | ./XYZ_to_Fractional_PBCs.awk "unitcell=${unitcell}" > HeavyMetal_symm.dat
 cat Halogen.dat | ./XYZ_to_Fractional_PBCs.awk "unitcell=${unitcell}" > Halogen_symm.dat
 cat C.dat | ./XYZ_to_Fractional_PBCs.awk "unitcell=${unitcell}" > C_symm.dat
 
# And finally...
 python MAPI_2D_hexbin_AtomicLocations.py "${unitcell}" "${prefix}"
done
