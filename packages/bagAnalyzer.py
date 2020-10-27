import rosbag
import numpy as np
import cv2
from cv_bridge import CvBridge


if __name__ == '__main__':
    
    OG_BAG = './bags/2020-10-27-13-55-09.bag'
    NEW_BAG = './bags/processed_bag.bag'

    bag = rosbag.Bag(OG_BAG)
    outbag = rosbag.Bag(NEW_BAG, 'w')

    cam_topic = '/r2d2/camera_node/image/compressed'

    bridge = CvBridge()
    
    # camera topic processing
    cam_num_messages = bag.get_message_count(cam_topic)

    #loop over all image messages
    for (topic, msg, t) in bag.read_messages(topics=[cam_topic]):
        
        # exctract timestamp from message
        timestamp = t.to_time()

        # extract image data from the message
        cv_image = bridge.compressed_imgmsg_to_cv2(msg, desired_encoding='passthrough')

        # draw timestamp on image
        ts_image = cv2.putText(cv_image, str(timestamp), (100, 100), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)

        # write image to new bag file
        ros_image = bridge.cv2_to_compressed_imgmsg(ts_image)
        outbag.write(topic, ros_image, t)

        
    
    
