from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='karlisr_packages',
    url='https://github.com/jladan/package_demo',
    author='Karlis R',
    author_email='karlisr@dati.lv',
    # Needed to actually package something
    packages=['karlisr_packages'],
    # Needed for dependencies
    install_requires=['pandas'],
    # *strongly* suggested for sharing
    version='1.2.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
