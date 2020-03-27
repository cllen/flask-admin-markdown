import setuptools


# with open("README.md", "r") as fh:
# 	long_description = fh.read()

long_description = "markdown for flask-admin"


setuptools.setup(
	name = "flask-admin-markdown",
	version="2020.3.27.1",
	auth="hxh",
	author_email="13750192465@163.com",
	description=long_description,
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/suckmybigdick/flask-admin-markdown",
	packages=setuptools.find_packages(),
	include_package_data=True,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	install_requires=[
		"setuptools==41.0.1",
		"Flask_Admin==1.5.5",
		"Flask_CKEditor==0.4.3",
		"WTForms==2.2.1",
		"Flask==0.10.1",
		"peewee==3.13.1",
		"wtf-peewee==3.0.0",
	],
)




