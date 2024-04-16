import sched
import time
import signal
from src.main import ingest_weather_data
from src.db.operations import load_cities_from_yaml

scheduler = sched.scheduler(time.time, time.sleep)


def schedule_daily_task() -> None:
    """
    Schedule a daily task to ingest weather data.
    """
    daily_interval = 60 * 60 * 24
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    scheduler.enter(daily_interval, 1, schedule_daily_task)
    print(f"Ingesting weather data...{date}")
    ingest_weather_data()


def start_scheduled_task() -> None:
    """
    Start the scheduled task to run daily.
    """
    scheduler.enter(0, 1, schedule_daily_task)
    load_cities_from_yaml()
    try:
        scheduler.run()
    except KeyboardInterrupt:
        print("Stopped by user.")


def signal_handler(signum, frame) -> None:
    """
    Handle the signal interrupt from the user.
    """
    print("Signal handler called with signal", signum)
    raise KeyboardInterrupt


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

if __name__ == "__main__":
    start_scheduled_task()
