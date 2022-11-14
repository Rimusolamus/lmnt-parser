To run, go to elementparser directory, run:
cat input.txt | python3 parser.py HH:MM

Feel free to change input.txt, but format has to be:
*|MM *|HH task_string

for example:
30 1 /bin/run_me_daily
45 * /bin/run_me_hourly
* * /bin/run_me_every_minute
* 19 /bin/run_me_sixty_times
