#!/bin/bash
#SBATCH --partition=teaching
#SBATCH --account=teaching
#SBATCH --job-name=pi_ineff_sweep
#SBATCH --output=pi_ineff_sweep_%j.out
#SBATCH --time=23:00:00
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1
#SBATCH --hint=nomultithread

set -euo pipefail

echo "Running on: $(hostname)"
echo "Python: $(python3 -V 2>&1)"
echo

# Must match the constant in pi_inefficient.py
N=100000000

NPROCS="1 2 4 8 16"
echo -e "nproc\tN\tIntegral\ttime_seconds"

for p in $NPROCS; do
  SECONDS=0

  # capture output (stdout+stderr)
  out="$(mpirun -np "$p" python3 pi_inefficient.py 2>&1)"

  elapsed="$SECONDS"
  integral="$(echo "$out" | awk '/^Integral /{print $2; exit}')"

  integral="${integral:-NA}"
  echo -e "${p}\t${N}\t${integral}\t${elapsed}"
done