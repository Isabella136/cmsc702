import functools
import pathlib
import typing
import collections

import treeswift

Accumulator: typing.TypeAlias = typing.Mapping[str, typing.Set[str]]

read_newick_tree: typing.Callable[[str], treeswift.Tree] = functools.partial(
    treeswift.read_tree, schema="newick"
)


def tree_reducer(accumulator: Accumulator, node: treeswift.Node) -> Accumulator:
    species, *_ = node.label.split("_")
    accumulator[species].add(node.label)
    return accumulator


def trees_reducer(accumulator: Accumulator, tree: treeswift.Tree):
    return functools.reduce(tree_reducer, tree.traverse_leaves(), accumulator)


def format_astral_map(accumulator: Accumulator) -> str:
    return "\n".join(
        f"{species}:{','.join(individuals)}"
        for species, individuals in sorted(accumulator.items(), key=lambda x: x[0])
    )


def format_wastral_map(accumulator: Accumulator) -> str:
    return "\n".join(
        "\n".join(f"{individual} {species}" for individual in individuals)
        for species, individuals in sorted(accumulator.items(), key=lambda x: x[0])
    )


def generate_name_map(
    f: typing.Callable[[Accumulator], str],
    dataset_path: pathlib.Path,
    output_name: str = "name_map.txt",
) -> None:
    trees = map(read_newick_tree, map(str, dataset_path.glob("g_trees*")))
    result = functools.reduce(trees_reducer, trees, collections.defaultdict(set))
    (dataset_path / output_name).write_text(f(result))


def concat_gene_trees(
    dataset_path: pathlib.Path, output_name: str = "all_trees.tree"
) -> None:
    (dataset_path / output_name).write_text(
        "\n".join(
            path.read_text().replace("[&R]", "").strip()
            for path in dataset_path.glob("g_trees*")
        )
    )


if __name__ == "__main__":
    import enum
    import typer

    class Mode(str, enum.Enum):
        astral = "astral"
        wastral = "wastral"
        qmc = "qmc"

    app = typer.Typer()

    @app.command()
    def main(mode: Mode, dataset_path: pathlib.Path):
        concat_gene_trees(dataset_path)

        if mode in [Mode.wastral, Mode.astral]:
            filename = f"name_map.{mode.value}.txt"
            format_func = {
                Mode.astral: format_astral_map,
                Mode.wastral: format_wastral_map,
            }[mode]
            generate_name_map(format_func, dataset_path, output_name=filename)

    app()
