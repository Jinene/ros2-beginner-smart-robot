from setuptools import setup

package_name = 'smart_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    description='Beginner ROS2 Smart Robot',
    license='MIT',
    entry_points={
        'console_scripts': [
            'obstacle_avoidance = smart_robot.obstacle_avoidance:main',
            'random_walker = smart_robot.random_walker:main',
            'status_service = smart_robot.status_service:main',
        ],
    },
)
