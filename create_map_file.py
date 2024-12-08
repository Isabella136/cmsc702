import collections
import pathlib
import functools
import typing

import treeswift


Accumulator: typing.TypeAlias = typing.Mapping[str, typing.Set[str]]


read_newick_tree = functools.partial(treeswift.read_tree, schema="newick")


def inner_reducer(accumulator: Accumulator, node: treeswift.Node) -> Accumulator:
    species, *_ = node.label.split("_")
    accumulator[species].add(node.label)
    return accumulator


def outer_reduce(accumulator: Accumulator, tree: treeswift.Tree) -> Accumulator:
    return functools.reduce(inner_reducer, tree.traverse_leaves(), accumulator)


def concatenate_gene_trees(
    dataset_path: pathlib.Path, output_path: pathlib.Path
) -> None:
    output_path.write_text(
        "\n".join(
            path.read_text().replace("[&R]", "").strip()
            for path in dataset_path.glob("g_trees*")
        )
    )


def create_name_map(dataset_path: pathlib.Path, output_path: pathlib.Path) -> None:
    trees = map(read_newick_tree, map(str, dataset_path.glob("g_trees*")))
    result = functools.reduce(outer_reduce, trees, collections.defaultdict(set))
    text = "\n".join(
        f"{species}:{','.join(individuals)}" for species, individuals in result.items()
    )
    output_path.write_text(text)


if __name__ == "__main__":
    import itertools
    import typer

    app = typer.Typer()

    def apply_function(
        f: typing.Callable[[pathlib.Path, pathlib.Path], None], output_filename: str
    ) -> None:
        for parent, child in itertools.product(
            ("biased_samples", "fix_samples", "unbiased_samples"),
            ("low", "mid", "high"),
        ):
            path = pathlib.Path(parent) / child
            for dataset in filter(pathlib.Path.is_dir, path.glob("*")):
                print(f"Applying {f.__name__} to {dataset}")
                f(dataset, dataset / output_filename)

    @app.command()
    def create_name_maps(output_filename: str = "name_map.txt"):
        """Loops through all datasets and creates the name map required by ASTRAL

        Args:
            output_filename (str, optional): _description_. Defaults to "name_map.txt".
        """
        apply_function(create_name_map, output_filename)

    @app.command()
    def concat(output_filename: str = "all_trees.tree"):
        """Loop through all datasets and create the combined gene tree file for each

        Args:
            output_filename (str, optional): _description_. Defaults to "all_trees.tree".
        """
        apply_function(concatenate_gene_trees, output_filename)

    app()
