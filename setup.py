import setuptools

setuptools.setup(
    name="nbgpserverproxy",
    version='0.1.0',
    url="https://github.com/jupyterhub/nbgpserverproxy",
    author="Ivan Chang",
    description="Jupyter extension to proxy GenePattern Server",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'notebook',
        'nbserverproxy >= 0.5.1'
    ],
    package_data={'nbgpserverproxy': ['static/*']},
)
