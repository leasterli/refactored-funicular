import time

# 设置专注时间（以秒为单位）
focus_time = 25 * 60

# 计时
while focus_time:
    mins, secs = divmod(focus_time, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    focus_time -= 1

# 专注时间结束后的提示
print("Time's up!")
