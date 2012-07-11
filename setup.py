from setuptools import setup, find_packages

version = '1.0'

setup(name='dreamcatcherfarm.produce',
      version=version,
      description="",
      long_description="",
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dreamcatcherfarm'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
