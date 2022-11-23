# deansorie@icloud.com

### Processes handling

###### Q1: bg
###### Q2: False
###### Q3: jobs
###### Q4: CTRL+c
###### Q5: CTRL+z
###### Q6: sleep 10
###### Q7: kill 4846
###### Q8: kill -9 4846
###### Q9: kill -CHLD 4828
###### Q10: k
###### Q11: The program has implemented a custom signal handler for the SIGINT signal.

### Process states

```bash
    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
  23907 root      20   0    8752   3680   3152 S   0.3   0.0   0:00.06 multi_process_f
  24542 root      20   0    8752   3144   2920 D   0.3   0.0   0:00.01 write_to_file_s
      1 root      20   0  174836  12116   8612 S   0.0   0.1   0:02.85 systemd
     42 root      19  -1   52064  15900  14916 S   0.0   0.2   0:00.14 systemd-journal
     65 root      20   0   22312   7316   3764 S   0.0   0.1   0:00.16 systemd-udevd
```

```bash
dean       16332  0.4  0.0   8752  3152 pts/2    D    15:50   0:00 /bin/bash ./write_to_file_sequentially.sh
dean       16334  0.4  0.0   8752  3084 pts/2    D    15:50   0:00 /bin/bash ./write_to_file_sequentially.sh
dean       16336  0.2  0.0   8752  3136 pts/2    D    15:50   0:00 /bin/bash ./write_to_file_sequentially.sh
dean       16337  0.2  0.0   8752  3132 pts/2    D    15:50   0:00 /bin/bash ./write_to_file_sequentially.sh
dean       16384  0.0  0.0  10616  3440 pts/0    R+   15:51   0:00 ps aux
```

##### According to the ps aux man page, D means uninterruptible sleep (usually IO)

