from setuptools import setup, find_packages

setup(name='lifx_control_panel',
      version='1.7.3',
      description='An open source application for controlling your LIFX brand lights',
      url='http://github.com/samclane/LIFX-Control-Panel',
      author='Sawyer McLane',
      author_email='samclane@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      scripts=['lifx_control_panel/__main__.pyw'],
      include_package_data=True)
