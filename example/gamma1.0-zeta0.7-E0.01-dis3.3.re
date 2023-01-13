echo

restart gamma1.0-zeta0.7-E0.01-dis3.3 

rt_tddft
  tmax 1
  dt 0.2
  load restart
  print charge dipole field energy moocc
end
task dft rt_tddft
