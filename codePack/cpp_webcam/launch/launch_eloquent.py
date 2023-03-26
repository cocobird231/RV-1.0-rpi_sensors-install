from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

import os
import yaml
from yaml import load, Loader

def generate_launch_description():
    commonFilePath = os.path.join(get_package_share_directory('cpp_webcam'), 'launch/common.yaml')
    with open(commonFilePath, 'r') as f:
        data = yaml.load(f, Loader=Loader)
    return LaunchDescription([
        Node(
            package="cpp_webcam",
            node_namespace=data['node_prop']['namespace'],
            node_executable="pub",
            output="screen",
            emulate_tty=True,
            parameters=[
                {
                    "topic_Webcam_nodeName" : data['topic_Webcam']['nodeName'], 
                    "topic_Webcam_topicName" : data['topic_Webcam']['topicName'], 
                    "topic_Webcam_pubInterval_s" : data['topic_Webcam']['publishInterval_s'], 
                    "topic_Webcam_width" : data['topic_Webcam']['width'], 
                    "topic_Webcam_height" : data['topic_Webcam']['height'], 
                    "mainNodeName" : data['node_prop']['nodeName'], 
                    "operationMode" : data['camera_prop']['operationMode'], 
                    "camera_cap_id" : data['camera_prop']['cap_id'], 
                    "camera_fps" : data['camera_prop']['fps'], 
                    "camera_width" : data['camera_prop']['width'], 
                    "camera_height" : data['camera_prop']['height'], 
                    "camera_use_color" : data['camera_prop']['use_color'], 
                }
            ]
        )
    ])