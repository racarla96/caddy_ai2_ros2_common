from setuptools import setup

package_name = 'caddy_ai2_ros2_common'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    package_dir={'': 'python'},
    data_files=[
        ('share/ament_index/resource_index/packages', []),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
)
