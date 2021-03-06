"""Main cli file"""
import click

from rawsec_cli.cli.command.listCommand import listCommand
from rawsec_cli.cli.command.searchCommand import search
from rawsec_cli.cli.command.submitCommand import submit
from rawsec_cli.tools import loadInventoryJson


@click.group()
@click.pass_context
def cli(ctx):
    """
    Rawsec's Cybersecurity Inventory is an inventory with 4 category(Tools, Resources, Ctf Platforms, OS).\n
    This cli can search a project,list all projects by category, you can filter your research with option --help for more information.\n
    full documentation: https://rawsec-cli.readthedocs.io/
    \f
    :param ctx: click context
    :return:
    """
    ctx.ensure_object(dict)
    ctx.obj["json"] = loadInventoryJson()


cli.add_command(search)
cli.add_command(listCommand)
cli.add_command(submit)

if __name__ == "__main__":
    cli(obj={})
