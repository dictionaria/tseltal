from setuptools import setup


setup(
    name='cldfbench_tseltal',
    py_modules=['cldfbench_tseltal'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'tseltal=cldfbench_tseltal:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
        'pydictionaria>=2.0',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
