"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Dbt_Jinja_Tests."""


if __name__ == "__main__":
    main(prog_name="dbt_jinja_tests")  # pragma: no cover
