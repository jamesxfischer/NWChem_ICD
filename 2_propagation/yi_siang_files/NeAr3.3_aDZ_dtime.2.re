echo

permanent_dir ./per
scratch_dir ./scr

restart NeAr3.3_aDZ_dtime.2  

rt_tddft
  tmax 3000 
  dt 2
  load restart
  print charge dipole field energy moocc

#  mocap
#    expconst 1.0     # exponential constant for CAP
#    emin 0.07         # any MO with eigenvalue >= 0.5 Ha will have CAP applied to it
#    prefac 1.0       # prefactor for exponential
#    maxval 1000.0    # clamp CAP at this value (in Ha)
#    on               # turn off CAP
#    nochecks         # disable checks for speed
##    noprint          # don't print CAP value
#  end

end
task dft rt_tddft
