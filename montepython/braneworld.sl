#!/bin/bash -l

#SBATCH -p regular
#SBATCH -N 1
#SBATCH -C haswell
#SBATCH -o braneworld_o
#SBATCH -e braneworld_e
#SBATCH --mail-type=begin,end,fail
#SBATCH --mail-user sunny.vagnozzi@fysik.su.se
#SBATCH -J braneworld
#SBATCH -t 00:40:00

cd $SLURM_SUBMIT_DIR   # optional, since this is the default behavior
export OMP_NUM_THREADS=4

srun -N 1 -n 8 -c 4 python montepython/MontePython.py run -p braneworld.param -o chains/braneworld -N 100000 --chain-num 1 --update 300 -c covmat/braneworld.covmat
