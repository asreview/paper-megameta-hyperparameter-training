from setuptools import setup
from setuptools import find_namespace_packages

setup(
    name='asreview-plugin-model-cnn-17-layer',
    version='0.1.1',
    description='A special version of the CNN-17-layer model optimized for the Megameta project.',
    url='https://github.com/asreview/paper-megameta-hyperparameter-training',
    author='ASReview team, Jelle Teijema',
    author_email='asreview@uu.nl',
    classifiers=[
        'Development Status :: 1 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='systematic review',
    packages=find_namespace_packages(include=['asreviewcontrib.*']),
    python_requires='~=3.6',
    install_requires=[
        'sklearn',
        'asreview>=0.13',
        'tensorflow',
        'scipy'
    ],
    entry_points={
        'asreview.models.classifiers': [
            'power_cnn = asreviewcontrib.models.cnn:POWER_CNN',
        ],
        'asreview.models.feature_extraction': [
            # define feature_extraction algorithms
        ],
        'asreview.models.balance': [
            # define balance strategy algorithms
        ],
        'asreview.models.query': [
            # define query strategy algorithms
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/asreview/paper-megameta-hyperparameter-training/issues',
        'Source': 'https://github.com/asreview/paper-megameta-hyperparameter-training',
    },
)
