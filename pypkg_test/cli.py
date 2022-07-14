"""Console script for pypkg_test."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("pypkg-test")
    click.echo("=" * len("pypkg-test"))
    click.echo("Skeleton project created by Cookiecutter PyPackage")


if __name__ == "__main__":
    main()  # pragma: no cover
