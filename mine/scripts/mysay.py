#!/usr/bin/env python
import sys;
import rospy;
from sound_play.msg import SoundRequest;
from sound_play.libsoundplay import SoundClient;
import roslib;
from std_msgs.msg import Bool;

rospy.init_node('saying')

def say():
    
    if len(sys.argv) == 1:
      print 'Awaiting something to say on standard input.'
    # Ordered this way to minimize wait time.
    
    soundhandle = SoundClient()
    rospy.sleep(1)

    voice = 'voice_kal_diphone'
    volume = 1.0
    
    if len(sys.argv) == 1:
        s = sys.stdin.read();
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
    rospy.sleep(1)


if __name__ == '__main__':
    
    #rospy.Subscriber('say_victim_found', Bool, say);
    say();

    rospy.spin();

    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print 'Usage: %s \'String to say.\''%sys.argv[0]
        print '       %s < file_to_say.txt'%sys.argv[0]
        print
        print 'Says a string. For a string on the command line, you must use quotes as'
        print 'appropriate. For a string on standard input, the command will wait for'
        print 'EOF before saying anything.'
        exit(-1)

    # Import after printing usage for speed.

