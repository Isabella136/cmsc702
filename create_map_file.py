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


def main(dataset_path: pathlib.Path, output_path: pathlib.Path) -> None:
    trees = map(read_newick_tree, map(str, dataset_path.glob("g_trees*")))
    result = functools.reduce(outer_reduce, trees, collections.defaultdict(set))
    text = "\n".join(
        f"{species}:{','.join(individuals)}" for species, individuals in result.items()
    )
    output_path.write_text(text)


if __name__ == "__main__":
    import sys

    inpath, outpath = map(pathlib.Path, sys.argv[1:])
    main(inpath, outpath)
