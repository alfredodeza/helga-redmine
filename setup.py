from setuptools import setup, find_packages

version = '0.0.2'

setup(name="helga-redmine",
      version=version,
      description=('redmine plugin for helga'),
      classifiers=['Development Status :: 1 - Beta',
                   'Environment :: IRC',
                   'Intended Audience :: Twisted Developers, IRC Bot Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: IRC Bots'],
      keywords='irc bot redmine',
      author='alfredo deza',
      author_email='contact [at] deza [dot] pe',
      url='https://github.com/alfredodeza/helga-redmine',
      license='MIT',
      packages=find_packages(),
      entry_points = dict(
          helga_plugins = [
              'redmine = redmine:redmine',
          ],
      ),
)
