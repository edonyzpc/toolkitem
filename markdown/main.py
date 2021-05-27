#!/usr/bin/python3

import click

from packages.iawriter import IAWriter
from packages.weeklyreport import WeeklyReport


@click.group()
def main():
    pass


@click.command("weeklyreport")
@click.argument('args1')
def weeklyreport():
    md = WeeklyReport()
    md.__doc__
    click.echo('Initialized the database')


@click.command("iawriter")
@click.argument('args2')
def iawriter():
    md = IAWriter()
    md.__doc__
    click.echo('Dropped the database')


main.add_command(weeklyreport)
main.add_command(iawriter)


# @click.command()
# @click.argument('args')
# @click.option('kind', default=1, help='number of ')
# def main(kind, count):
#    markdown_tools = {
#        "weekly": WeeklyReport(),
#        "iawriter": IAWriter(),
#    }.get(kind, default=IAWriter())
#    markdown_tools.generate()


if __name__ == "__main__":
    main()
