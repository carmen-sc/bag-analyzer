import rosbag
import numpy as np

if __name__ == '__main__':
    
    BAG_NAME = './bags/example_rosbag_H3.bag'

    bag = rosbag.Bag(BAG_NAME)
    
    cam_topic = '/tesla/camera_node/camera_info'
    line_topic = '/tesla/line_detector_node/segment_list'
    wheel_topic = '/tesla/wheels_driver_node/wheels_cmd'
     

    # camera topic processing
    cam_num_messages = bag.get_message_count(cam_topic)

    cam_period = np.empty([cam_num_messages, 1])
    i = 0
    t_old = 0
    #create numpy array containing period lengths
    for (topic, msg, t) in bag.read_messages(topics=[cam_topic]):
        t_new = t.to_time()
        period_val = t_new - t_old
        cam_period[i, 0] = period_val
        i = i+1
        t_old = t_new
    
    # remove initial value
    cam_period = np.delete(cam_period, [0])
    
    # use numpy for analysis
    cam_min = np.around(np.min(cam_period), 2)
    cam_max = np.around(np.max(cam_period), 2)
    cam_avg = np.around(np.average(cam_period), 2)
    cam_med = np.around(np.median(cam_period), 2)
            
    # print analysis to terminal            
    print(cam_topic, ":")
    print("num_messages: ", cam_num_messages)
    print("period: ")
    print("min: ", cam_min)
    print("max: ", cam_max)
    print("average: ", cam_avg)
    print("median: ", cam_med)
    print("\n")


    # line topic processing
    line_num_messages = bag.get_message_count(line_topic)

    line_period = np.empty([line_num_messages, 1])
    i = 0
    t_old = 0
    #create numpy array containing period lengths
    for (topic, msg, t) in bag.read_messages(topics=[line_topic]):
        t_new = t.to_time()
        period_val = t_new - t_old
        line_period[i, 0] = period_val
        i = i+1
        t_old = t_new
    
    # remove initial value
    line_period = np.delete(line_period, [0])
    
    # use numpy for analysis
    line_min = np.around(np.min(line_period), 2)
    line_max = np.around(np.max(line_period), 2)
    line_avg = np.around(np.average(line_period), 2)
    line_med = np.around(np.median(line_period), 2)

    # print analysis to terminal            
    print(line_topic, ":")
    print("num_messages: ", line_num_messages)
    print("period: ")
    print("min: ", line_min)
    print("max: ", line_max)
    print("average: ", line_avg)
    print("median: ", line_med)
    print("\n")

    # wheel topic processing
    wheel_num_messages = bag.get_message_count(wheel_topic)

    wheel_period = np.empty([wheel_num_messages, 1])
    i = 0
    t_old = 0
    #create numpy array containing period lengths
    for (topic, msg, t) in bag.read_messages(topics=[wheel_topic]):
        t_new = t.to_time()
        period_val = t_new - t_old
        wheel_period[i, 0] = period_val
        i = i+1
        t_old = t_new
    
    # remove initial value
    wheel_period = np.delete(wheel_period, [0])
    
    # use numpy for analysis
    wheel_min = np.around(np.min(wheel_period), 2)
    wheel_max = np.around(np.max(wheel_period), 2)
    wheel_avg = np.around(np.average(wheel_period), 2)
    wheel_med = np.around(np.median(wheel_period), 2)

    # print analysis to terminal            
    print(wheel_topic, ":")
    print("num_messages: ", wheel_num_messages)
    print("period: ")
    print("min: ", wheel_min)
    print("max: ", wheel_max)
    print("average: ", wheel_avg)
    print("median: ", wheel_med)
    print("\n")