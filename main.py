import psutil
memory = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage("/").percent
boot_ts = psutil.boot_time()
cpu_1 = psutil.cpu_percent(interval=1)
cpu_2 = psutil.cpu_percent(interval=1, percpu=True)
cpu_3 = psutil.cpu_percent(interval=None)
connections = psutil.net_connections()
THRESHOLD = 100 * 1024 * 1024  # 100MB
def ma():
    if memory.available <= THRESHOLD:
        print("warning") #Works in shell
    else:
        print("safe")
def statistics():
    print("Memory:",memory)
    print("Disk Usage:",disk_usage)
    print("Boot Time :",boot_ts)
    print("blocking",cpu_1)
    print("non-blocking (percentage since last call)",cpu_3)
    print("blocking, per-cpu",cpu_2)
def c():
    print(connections)
menu = """ 
           1-Ram control
           2-Statistics
           3-Connections
"""
print(menu)
selection = int(input(":"))
if selection == 1:
    ma()
elif selection == 2:
    statistics()
elif selection == 3:
    c()