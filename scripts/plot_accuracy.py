import os
import typing
import pathlib

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def plot_accuracy(
    name: str,
    data_path: os.PathLike,
    plot_directory: typing.Optional[os.PathLike] = None,
):
    plot_directory = pathlib.Path(plot_directory or "plots")
    plot_directory.mkdir(exist_ok=True, parents=True)
    df = pd.read_csv(str(data_path))

    fp_fn_agg = (
        df.groupby(["Sample Type", "Subgroup"])[
            ["Number of False Positives", "Number of False Negatives"]
        ]
        .sum()
        .reset_index()
    )
    fig, ax = plt.subplots(figsize=(12, 6))
    subgroups = ["low", "mid", "high"]
    colors = sns.color_palette(
        "coolwarm", 2
    )  # Two colors for False Positives and False Negatives
    sample_types = fp_fn_agg["Sample Type"].unique()
    x_positions = {
        sample: idx * (len(subgroups) + 1) for idx, sample in enumerate(sample_types)
    }
    bar_width = 0.8
    max_value = 50
    for sample_type, x_start in x_positions.items():
        for idx, subgroup in enumerate(subgroups):
            subgroup_data = fp_fn_agg[
                (fp_fn_agg["Sample Type"] == sample_type)
                & (fp_fn_agg["Subgroup"] == subgroup)
            ]

            false_positives = subgroup_data["Number of False Positives"].values[0]
            false_negatives = subgroup_data["Number of False Negatives"].values[0]

            # Bar positions
            x = x_start + idx

            # Plot False Positives (bottom of stack)
            ax.bar(
                x,
                false_positives,
                width=bar_width,
                label="False Positives" if idx == 0 else "",
                color=colors[0],
            )

            # Plot False Negatives (top of stack)
            ax.bar(
                x,
                false_negatives,
                width=bar_width,
                bottom=false_positives,
                label="False Negatives" if idx == 0 else "",
                color=colors[1],
                alpha=0.8,
            )

            max_value = max(max_value, false_negatives + false_positives)

    ax.set_title(
        f"{name} False Positives and False Negatives by Subgroup and Sample Type"
    )
    ax.set_xlabel("Sample Type and Subgroup")
    ax.set_ylabel("Total Count")
    ax.set_ylim(0, int(max_value + 10))

    # Set x-ticks and labels
    x_ticks = [
        x_start + i for x_start in x_positions.values() for i in range(len(subgroups))
    ]
    x_labels = [
        f"{sample_type}\n{subgroup}"
        for sample_type in sample_types
        for subgroup in subgroups
    ]
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, rotation=45, ha="right")

    # Add a single legend
    custom_legend = [
        plt.Rectangle((0, 0), 1, 1, color=colors[0], label="False Positives"),
        plt.Rectangle((0, 0), 1, 1, color=colors[1], label="False Negatives"),
    ]
    ax.legend(
        handles=custom_legend,
        title="Metric",
        bbox_to_anchor=(1.05, 1),
        loc="upper left",
    )

    # Adjust layout and save
    plt.tight_layout()
    fig.savefig(
        str(plot_directory / f"{name}_stacked_bar_false_positives_negatives.png")
    )


if __name__ == "__main__":
    for name, path in [
        ("Astral-4", "../results/astral-4.csv"),
        ("Astral-Multi", "../results/astral-multi.csv"),
        ("Astral-Pro", "../results/astral-pro.csv"),
        ("Weighted Astral", "../results/wastral.csv"),
        ("Tree-QMC", "../results/execution_and_comparison_results1.csv"),
    ]:
        plot_accuracy(name, path)
