from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

import os
import yaml
from yaml import load, Loader

def generate_launch_description():
    commonFilePath = os.path.join(get_package_share_directory('py_gps'), 'launch/common.yaml')
    with open(commonFilePath, 'r') as f:
        data = yaml.load(f, Loader=Loader)
    return LaunchDescription([
        Node(
            package="py_gps",
            namespace=data['node_prop']['namespace'],
            executable="pub",
            output="screen",
            emulate_tty=True,
            parameters=[
                {
                    "topic_GPS_nodeName" : data['topic_GPS']['nodeName'], 
                    "topic_GPS_topicName" : data['topic_GPS']['topicName'], 
                    "topic_GPS_pubInterval" : data['topic_GPS']['publishInterval'], 
                    "mainNodeName" : data['node_prop']['nodeName'], 
                    "module" : data['GPS_prop']['module'], 
                    "caster" : data['GPS_prop']['caster'], 
                    "port" : data['GPS_prop']['port'], 
                    "mountpoint" : data['GPS_prop']['mountpoint'], 
                    "username" : data['GPS_prop']['username'], 
                    "password" : data['GPS_prop']['password'], 
                }
            ]
        )
    ])
