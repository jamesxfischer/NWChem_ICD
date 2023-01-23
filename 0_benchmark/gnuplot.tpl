reset
set term png
set output output_fname
set title input_fname
plot input_fname using 1:2 w l lt 7 title 'Ar'  #, input_fname using 1:4 w l lt 6 title 'Ar2' 

