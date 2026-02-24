#!/usr/bin/env python3

import math
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nproc = comm.Get_size()

# samples
N = 100000000
delta = 1.0 / N


def integrand(x: float) -> float:
    return 4.0 / (1.0 + x * x)


comm.Barrier()
t0 = MPI.Wtime()

terms = []
append = terms.append
for i in range(rank, N, nproc):
    x = (i + 0.5) * delta
    append(integrand(x) * delta)

local_I = math.fsum(terms)
I = comm.reduce(local_I, op=MPI.SUM, root=0)

comm.Barrier()
t1 = MPI.Wtime()
#end timed compute region

if rank == 0:
    print(f"nproc={nproc} N={N} Integral={I:.10f} time_seconds={t1 - t0:.6f}")
