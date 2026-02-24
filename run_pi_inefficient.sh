#!/bin/bash
#SBATCH --partition=teaching
#SBATCH --account=teaching
#SBATCH --job-name=pi_inefficient
#SBATCH --output=pi_inefficient_%j.out
#SBATCH --time=10:00:00
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1
#SBATCH --hint=nomultithread

module load mpi

perf stat -e cycles,instructions,cache-misses mpirun -np 16 ./pi_inefficient.py