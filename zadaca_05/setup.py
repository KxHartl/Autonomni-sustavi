from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'zadaca_05'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*config.rviz*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kresimirhartl',
    maintainer_email='kresimirhartl@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_tf2_broadcaster = zadaca_05.turtle_tf2_broadcaster:main',
            'goal_broadcaster = zadaca_05.goal_broadcaster:main',
        ],
    },
)
