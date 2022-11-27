# download vin decoding of NYS DMV DB, run each process in parallel
# each process can be monitored with tail -f <log file?
cd ~/code/repo/cind820-dataanalytics 
/usr/bin/python3 vin-decode.py 0 500000 50 > a.log & 
/usr/bin/python3 vin-decode.py 500000 1000000 50 > b.log &
/usr/bin/python3 vin-decode.py 1000000 2000000 50 > c.log &
/usr/bin/python3 vin-decode.py 2000000 3000000 50 > d.log &
/usr/bin/python3 vin-decode.py 3000000 4000000 50 > e.log &
/usr/bin/python3 vin-decode.py 4000000 5000000 50 > f.log &
/usr/bin/python3 vin-decode.py 5000000 6000000 50 > g.log &
/usr/bin/python3 vin-decode.py 6000000 7000000 50 > h.log &
/usr/bin/python3 vin-decode.py 7000000 8000000 50 > i.log &
/usr/bin/python3 vin-decode.py 8000000 9000000 50 > j.log &
/usr/bin/python3 vin-decode.py 9000000 10000000 50 > k.log &
/usr/bin/python3 vin-decode.py 10000000 11000000 50 > l.log &
/usr/bin/python3 vin-decode.py 11000000 12586700 50 > m.log &

 