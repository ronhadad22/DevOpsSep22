# deansorie@icloud.com

### Q1: bg
### Q2: False
### Q3: jobs
### Q4: CTRL+c
### Q5: CTRL+z
### Q6: sleep 10
### Q7: kill 4846
### Q8: kill -9 4846
### Q9: kill -CHLD 4828
### Q10: k
### Q11: The program has implemented a custom signal handler for the SIGINT signal.

```bash
dean       16332  0.4  0.0   8752  3152 pts/2    D    15:50   0:00 /bin/bash ./write_to_file_sequentially.sh
dean       16334  0.4  0.0   8752  3084 pts/2    D    15:50   0:00 /bin/bash ./write_to_file_sequentially.sh
dean       16336  0.2  0.0   8752  3136 pts/2    D    15:50   0:00 /bin/bash ./write_to_file_sequentially.sh
dean       16337  0.2  0.0   8752  3132 pts/2    D    15:50   0:00 /bin/bash ./write_to_file_sequentially.sh
dean       16384  0.0  0.0  10616  3440 pts/0    R+   15:51   0:00 ps aux
```

#### According to the man page, D means uninterruptible sleep (usually IO)

