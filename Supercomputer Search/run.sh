#!/bin/bash
#SBATCH --job-name=mpi4py-test   # create a name for your job
#SBATCH --nodes=8                # node count
#SBATCH --time=00:01:00          # total run time limit (HH:MM:SS)

module purge
module load anaconda3/2020.11
module load openmpi/4.1.1-gcc8.3.1  # REPLACE <x.y.z>
conda activate fast-mpi4py

python mpi.py