#!/bin/bash
#SBATCH --partition=teaching
#SBATCH --account=teaching
#SBATCH --job-name=pi_scaling_sweep
#SBATCH --output=pi_scaling_sweep_%j.out
#SBATCH --time=00:59:00
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1
#SBATCH --hint=nomultithread

set -euo pipefail

echo "Running on: $(hostname)"
echo "Python: $(python3 -V 2>&1)"
echo

NPROCS="1 2 4 8 16"
echo -e "nproc\tN\tIntegral\ttime_seconds"

for p in $NPROCS; do

  line="$(
    mpirun -np "$p" python3 pi_efficient.py 2>/dev/null \
      | grep '^nproc=' | head -n 1 | tr -d '\r'
  )"

  nproc="${line#nproc=}" ; nproc="${nproc%% *}"
  rest="${line#* N=}" ; N="${rest%% *}"
  rest="${line#* Integral=}" ; I="${rest%% *}"
  rest="${line#* time_seconds=}" ; t="${rest%% *}"

  echo -e "${nproc}\t${N}\t${I}\t${t}"
done
