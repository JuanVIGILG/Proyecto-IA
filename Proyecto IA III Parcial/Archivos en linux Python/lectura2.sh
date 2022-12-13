#!/bin/bash
sshpass -p "mendez" ssh -l pi 192.168.20.206 "sudo gpio read 21" > /home/mendez/ExamenArq/estado21.txt
sshpass -p "mendez" ssh -l pi 192.168.20.206 "sudo gpio read 22" > /home/mendez/ExamenArq/estado22.txt
sshpass -p "mendez" ssh -l pi 192.168.20.206 "sudo gpio read 23" > /home/mendez/ExamenArq/estado23.txt



