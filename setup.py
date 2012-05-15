# coding=utf-8
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.profile.signup.facebook',
    version=version,
    description="The pages and code required for user initiated sign-up via"\
        "facebook (registration)",
    long_description=open("README.txt").read() + "\n" +
                    open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: Other/Proprietary License",
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='sign up, registration, profile, user, join, facebook',
    author='Richard Waid',
    author_email='richard@onlinegroups.net',
    url='http://groupserver.org',
    license='ZPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.profile', 'gs.profile.signup'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.GSProfile',
        'gs.content.form',
        'gs.group.member.join',
        'gs.group.member.invite.base',
        'gs.profile.password',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)

