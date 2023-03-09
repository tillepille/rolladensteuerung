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

PATH=/bin:/usr/bin:/sbin:/usr/sbin
set -e

case "$1" in
    start)
        #Aktion wenn start uebergeben wird
        echo "Start Homekit Client"
        python3 /home/pi/rolladensteuerung/roll.py > access.log &
            ;;

    stop)
        #Aktion wenn stop uebergeben wird
        echo "Stop Homekit Client"
        killall python3
            ;;

    restart)
        #Aktion wenn restart uebergeben wird
            echo "Restart Homekit Client"
            ;;
    *)
          ;;
esac

exit 0
