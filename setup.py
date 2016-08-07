from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='what_the_license',
      version='0.1',
      description='Returns the content of a jar file\'s MANIFEST as dict.',
      long_description=readme(),
      classifiers=[
      	'Development Status :: 4 - Beta',
      	'License :: OSI Approved :: MIT License',
      	'Programming Language :: Python :: 2.7'
      ],
      keywords='open source license file(1)',
      url='http://github.com/nlohmann/what_the_license',
      author='Niels Lohmann',
      author_email='mail@nlohmann.me',
      license='MIT',
      scripts=['what_the_license/bin/wtl'],
      packages=['what_the_license'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
