from setuptools import find_packages, setup
import os

package_name = 'led_blink_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='saeed',
    maintainer_email='saeedmridha42@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'blink_led_node = led_blink_package.esp32_blink_code_ros2_side:main',
        ],
    },
)
