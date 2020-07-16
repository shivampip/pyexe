from pyexe import Local, Remote

lc = Local()
lc.setPath("../project")
lc.git.put()

rm = Remote("162.158.50.246", "root", "password")
rm.connect()
rm.setPath("/var/www/project")
rm.git.get()

rm.setPath("/var/www/project")
rm.exe("npm run build")
