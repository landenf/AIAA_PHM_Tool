#!/usr/bin/python3
import rospy
from std_msgs.msg import String

class Node3:
    def __init__(self):
        rospy.init_node('node_3')

        # Publisher for topic_3
        self.pub_topic_3 = rospy.Publisher('topic_3', String, queue_size=10)

        # Subscribers to the other topics
        rospy.Subscriber('topic_1', String, self.callback_topic_1)
        rospy.Subscriber('topic_2', String, self.callback_topic_2)

        self.rate = rospy.Rate(1)  # 1 Hz for publishing

    def callback_topic_1(self, data):
        rospy.loginfo(f"Node 3 heard from topic_1: {data.data}")

    def callback_topic_2(self, data):
        rospy.loginfo(f"Node 3 heard from topic_2: {data.data}")

    def publish_to_topic_3(self):
        msg = "Message from node 3 to topic_3"
        rospy.loginfo(f"Publishing to topic_3: {msg}")
        self.pub_topic_3.publish(msg)

    def run(self):
        rospy.loginfo("Node 3 starting...")
        while not rospy.is_shutdown():
            self.publish_to_topic_3()
            self.rate.sleep()

if __name__ == "__main__":
    try:
        node = Node3()
        node.run()
    except rospy.ROSInterruptException:
        pass