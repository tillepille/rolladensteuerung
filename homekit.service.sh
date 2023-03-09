#! /bin/sh
#
# Copy to /etc/init.d/
#
### BEGIN INIT INFO
# Provides:          pitracker
# Required-Start:    $all
# Required-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: start homekit servers
# Description:       This service starts both homekit servers
### END INIT INFO

PATH=/home/pi/.local/bin:/bin:/usr/bin:/sbin:/usr/sbin
set -e

case "$1" in
    start)
        python3 /home/pi/rolladensteuerung/roll.py > access.log &
            ;;

    stop)
        killall python3
            ;;

    restart)
            echo "Restart Homekit Client"
            ;;
    *)
          ;;
esac

exit 0
