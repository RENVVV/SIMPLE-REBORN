P = '\x1b[1;97m'
import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nKONEKSI INTERNET BURUK\n'%(P))
	exit()

if __name__ == "__main__":
	os.system("git pull")
	os.system("mkdir OK")
	os.system("mkdir CP")
	if "Indonesia" == fc:
		__import__("Simple").Line_()
	else:
		__import__("Simple").Line_()
