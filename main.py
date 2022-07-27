import click
from websites import Wallpapercave as wp

DEFAULT = "https://wallpapercave.com/"

@click.command()
@click.argument("url", default=DEFAULT)
def main(url):
	check = wp.is_website(url)
	if check:
		site = wp(url)
	site.get_images()
	
if __name__ == "__main__":
	main()




