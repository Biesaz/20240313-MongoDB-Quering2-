import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
def change_password(password):
    click.echo(f'Password changed to: {password}')

@cli.command()
@click.option('--username', prompt=True)
@click.password_option()
def create_user(username, password):
    click.echo(f'User {username} created with password: {password}')

if __name__ == '__main__':
    cli()