from apscheduler.schedulers.blocking import BlockingScheduler
from bot import send_msg

def job_function():
    print("Hello World")

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_msg, 'interval', seconds=10)

sched.start()