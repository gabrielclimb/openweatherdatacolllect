import sched
import time
import signal
from src.data_collect import ingest_weather_data

scheduler = sched.scheduler(time.time, time.sleep)


def schedule_daily_task():
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    scheduler.enter(10, 1, schedule_daily_task)
    print(f"Ingesting weather data...{date}")
    ingest_weather_data()


def start_scheduled_task():
    scheduler.enter(0, 1, schedule_daily_task)
    try:
        scheduler.run()
    except KeyboardInterrupt:
        print("Stopped by user.")


def signal_handler(signum, frame):
    print("Signal handler called with signal", signum)
    raise KeyboardInterrupt


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

if __name__ == "__main__":
    start_scheduled_task()
