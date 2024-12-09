import os
import pathlib
import ete3


def read_tree(path: os.PathLike | str) -> ete3.Tree:
    return ete3.Tree(pathlib.Path(path).read_text())


if __name__ == "__main__":
    import typer

    app = typer.Typer()

    @app.command()
    def main(estimated_tree: pathlib.Path, true_tree: pathlib.Path):
        """Prints the RF distance and Max RF for a given pair of trees

        Args:
            estimated_tree (pathlib.Path): _description_
            true_tree (pathlib.Path): _description_
        """
        estimated = read_tree(estimated_tree)
        true = read_tree(true_tree)
        print(",".join(map(str, estimated.robinson_foulds(true)[:2])))

    app()
