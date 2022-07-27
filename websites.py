import requests as r
import shutil
from bs4 import BeautifulSoup as bs

class Wallpapercave:
	default = "wallpapercave.com"
	http = "https://"
	def __init__ (self, url):
		self.is_default = False
		self.url = url
		if self.url == self.default:
			self.is_default = True

	@classmethod
	def is_website(cls, url):
		if cls.default in url: 
			return True
		else:
			return False

	def get_images(self):
		headers = {"User-Agent":"MadeUpBrowser 1.0"}
		page = r.get(self.url, headers=headers)
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

		dl_imgs = set(dl_imgs)
		for num, image in enumerate(dl_imgs):
			imgurl = self.http + self.default + "/" + image
			dl_img = r.get(imgurl,  headers=headers, stream=True)
			if dl_img.status_code == 200:
				with open(f"./images/image_{num}.jpg", "wb") as f:
					dl_img.raw.decode_content = True
					shutil.copyfileobj(dl_img.raw, f)




