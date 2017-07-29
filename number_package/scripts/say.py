#!/usr/bin/env python

import sys
import roslib;
from std_msgs.msg import String;
import rospy;
import rospy
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
def say(str):
    if len(sys.argv) == 1:
        print 'Awaiting something to say on standard input.'

    # Ordered this way to minimize wait time.
    soundhandle = SoundClient()
    

    voice = 'voice_kal_diphone'
    volume = 1.0

    if len(sys.argv) == 1:
        s = str.data
    else:
        s = sys.argv[1]

        if len(sys.argv) > 2:
            voice = sys.argv[2]
        if len(sys.argv) > 3:
            volume = float(sys.argv[3])

    print 'Saying: %s' % s
    print 'Voice: %s' % voice
    print 'Volume: %s' % volume

    soundhandle.say(s, voice, volume)

def listen():
    rospy.Subscriber("/sayings", String, say);

if __name__ == '__main__':
    rospy.sleep(5)
    rospy.init_node('your_sayings', anonymous=True)
    listen();
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print 'Usage: %s \'String to say.\''%sys.argv[0]
        print '       %s < file_to_say.txt'%sys.argv[0]
        print
        print 'Says a string. For a string on the command line, you must use quotes as'
        print 'appropriate. For a string on standard input, the command will wait for'
        print 'EOF before saying anything.'
        exit(-1)
    while not rospy.is_shutdown():
        rospy.loginfo('not subbing')
        rospy.sleep(100000000)
