import os
def env():
	choice=int(input("Enter Environment"))
	return choice
#-------------------------------------------------------------
def apt_update():
	os.system("sudo apt-get update")
#-------------------------------------------------------------
def apt_install(l):
	cmd="sudo apt-get install "+l
	os.system(cmd)
#-------------------------------------------------------------
ch=int(input("Enter choice for theme= "))
if ch==1:
	print "adapta"
	if env()==1:
		print "ubuntu"
		os.system("sudo apt-add-repository ppa:tista/adapta -y")
		apt_update()
		apt_install("adapta-gtk-theme")
elif ch==2:
	print "vertex"
	if env()==1:
		print "ubuntu"
		U_cmd="echo 'deb http://download.opensuse.org/repositories/home:/Horst3180/xUbuntu_16.04/ /' >> /etc/apt/sources.list.d/vertex-theme.list"
		os.system("sudo sh -c +U_cmd")
		apt_update()
		apt_install("vertex-theme")
		
