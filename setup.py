import os
from setuptools import setup, find_packages

version = os.environ.get('VERSION')

try:
    os.rename('/etc/foo', '/etc/bar')
except IOError as e:
    if (e[0] == errno.EPERM):
       print >> sys.stderr, "Please, execute setup.py with admin privileges"
	   print "Try running: sudo python setup.py"
       sys.exit(1)

def package_data_dirs(source, sub_folders):
	dirs = []

	for d in sub_folders:
		for dirname, _, files in os.walk(os.path.join(source, d)):
			dirname = os.path.relpath(dirname, source)
			for f in files:
				dirs.append(os.path.join(dirname, f))
	return dirs

setup(name='Sunrise',
      version=version,
      author='Jaime Garcia Villena',
      author_email='elgambitero@gmail.com',
      description='Sunrise-sw is a DLP 3D printer host',

      license='GPLv2',
      keywords = "sunrise dlp 3d printer host",

      packages = ['sunrise'],
      package_dir = {'sunrise': '.'},
      package_data = {'sunrise': package_data_dirs('.', ['src'])},

      data_files=[('/etc/init.d', ['init-script'])
                    ('/etc',['rc.local'])]
     )
