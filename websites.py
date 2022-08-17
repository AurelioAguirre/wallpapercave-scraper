import requests as r
import shutil, os
from bs4 import BeautifulSoup as bs

class Wallpapercave:
	headers = {"User-Agent":"MadeUpBrowser 1.0"}
	default = "https://wallpapercave.com/"

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
		dl_imgs = []
		adress = ""
		page = r.get(self.url, headers=self.headers)
		soup = bs(page.content, "html.parser")
		if "search" in self.url or self.url == self.default:
			img_tags = soup.find_all("img")
			for i in img_tags:
				if "/fwp" in i["src"]:
					adress = i["src"].replace("/fwp", "/wp")
				elif "fuwp" in i["src"]:
					adress = i["src"].replace("/fuwp", "/uwp" ) 
				if adress != "":
					dl_imgs.append(adress)
		elif "-wallpapers" in self.url:
			class_tags = soup.find_all(class_="wpinkw")
			for i in class_tags:
				if "/w/" in i["href"]:
					adress = i["href"].replace("/w/", "/wp/")
					adress = adress + ".jpg"
					dl_imgs.append(adress)

		dl_imgs = set(dl_imgs)

		self.write_images(dl_imgs)

	def write_images(self, dl_imgs):
		l = 0
		current_d = os.getcwd()
		image_dir = f"{current_d}/images"
		if os.path.isdir(image_dir):
			dirinfo = list(os.walk(image_dir))
			l = len(dirinfo[0][2])
		else:
			os.mkdir(image_dir)

		for num, image in enumerate(dl_imgs):
			imgurl = self.default + image
			if "webp" not in imgurl:
				dl_img = r.get(imgurl,  headers=self.headers, stream=True)
				if dl_img.status_code == 200:
					with open(f"{image_dir}/image_{num+l}.jpg", "wb") as f:
						dl_img.raw.decode_content = True
						shutil.copyfileobj(dl_img.raw, f)



