import requests as r
import shutil
import click
from bs4 import BeautifulSoup as bs

DEFAULT = "https://wallpapercave.com/"

@click.command()
@click.argument("url", default=DEFAULT)
def main(url):
	headers = {"User-Agent":"MadeUpBrowser 1.0"}
	page = r.get(url, headers=headers)

	soup = bs(page.content, "html.parser")
	img_tags = soup.find_all("img")
	dl_imgs = []
	adress = ""
	for i in img_tags:
		if "/fwp" in i["src"]:
			adress = i["src"].replace("/fwp", "/wp")
		elif "fuwp" in i["src"]:
			adress = i["src"].replace("/fuwp", "/uwp" ) 
		if adress != "":
			dl_imgs.append(adress)
	get_images(url, dl_imgs, headers)


def get_images(url, img_tags, headers):
	links = []
	for num, image in enumerate(img_tags):
		imgurl = DEFAULT + image
		dl_img = r.get(imgurl,  headers=headers, stream=True)
		if dl_img.status_code == 200:
			with open(f"./images/image_{num}.jpg", "wb") as f:
				dl_img.raw.decode_content = True
				shutil.copyfileobj(dl_img.raw, f)

	
if __name__ == "__main__":
	main()




