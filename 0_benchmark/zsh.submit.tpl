#!/bin/bash -l

#PBS -S /bin/bash
#PBS -A GT-jkretchmer3-chemx
#PBS -l nodes=1:ppn=16
#PBS -l pmem=16gb
#PBS -l walltime=2:00:00
#PBS -N TMPL_JOB_NAME 
##PBS -e TMPL_JOB_NAME.err
##PBS -o TMPL_JOB_NAME.out
#PBS -V
#PBS -j oe

#if [ -f /etc/bashrc ]; then
#. /etc/bashrc
#fi

cd $PBS_O_WORKDIR

module load anaconda3
conda activate nw702 

nwchem TMPL_JOB_NAME.nw > TMPL_JOB_NAME.nwo 
#sh hello.sh #> yes_to_stop.out
#python3 run_tdhf.py > dariia.out


