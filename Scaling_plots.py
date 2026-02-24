#!/usr/bin/env python3

import matplotlib.pyplot as plt

EFFICIENT = [
    (1, 30.917560),
    (2, 15.851649),
    (4, 8.311354),
    (8, 4.215430),
    (16, 2.636761),
]

INEFFICIENT = [
    (1, 56.0),
    (2, 261.0),
    (4, 358.0),
    (8, 425.0),
    (16, 449.0),
]


def speedup(series):
    t1 = series[0][1]
    return [(p, t1 / t) for p, t in series]


def plot_time_two_axes(efficient, inefficient, out_path="scaling_time_two_axes.png"):
    x = [p for p, _ in efficient]
    y_eff = [t for _, t in efficient]
    y_ine = [t for _, t in inefficient]

    fig, ax1 = plt.subplots()

    ax1.plot(x, y_eff, marker="o", color="tab:blue", label="Efficient")
    ax1.set_xlabel("MPI ranks (nproc)")
    ax1.set_ylabel("Efficient time (s)", color="tab:blue")
    ax1.tick_params(axis="y", labelcolor="tab:blue")
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.plot(x, y_ine, marker="o", color="tab:red", label="Inefficient")
    ax2.set_ylabel("Inefficient time (s)", color="tab:red")
    ax2.tick_params(axis="y", labelcolor="tab:red")

    fig.suptitle("Strong scaling: Time vs MPI ranks (two y-axes)")

    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    fig.legend(h1 + h2, l1 + l2, loc="upper right")

    fig.savefig(out_path, dpi=200, bbox_inches="tight")


def plot_speedup_single_axis(efficient, inefficient, out_path="scaling_speedup.png"):
    eff_s = speedup(efficient)
    ine_s = speedup(inefficient)

    x_eff = [p for p, _ in eff_s]
    y_eff = [s for _, s in eff_s]
    x_ine = [p for p, _ in ine_s]
    y_ine = [s for _, s in ine_s]

    plt.figure()
    plt.plot(x_eff, y_eff, marker="o", label="Efficient")
    plt.plot(x_ine, y_ine, marker="o", label="Inefficient")
    plt.plot(x_eff, x_eff, marker="o", label="Ideal (S=p)")

    plt.xlabel("MPI ranks (nproc)")
    plt.ylabel("Speedup (T1/Tp)")
    plt.title("Strong scaling: Speedup vs MPI ranks")
    plt.grid(True)
    plt.legend()
    plt.savefig(out_path, dpi=200, bbox_inches="tight")


def main():
    plot_time_two_axes(EFFICIENT, INEFFICIENT, "scaling_time_two_axes.png")
    plot_speedup_single_axis(EFFICIENT, INEFFICIENT, "scaling_speedup.png")
    print("Wrote: scaling_time_two_axes.png, scaling_speedup.png")


if __name__ == "__main__":
    main()
