from celery  import Celery
import os


broker = os.getenv("celery_broker")

app = Celery('tasks', broker=broker)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(300 ,runPeriodically.s(), name='Update Truck Locations Every 5 minutes')


@app.task(name="Run Periodically")
def runPeriodically():
    print("Running, Again?")
    return 1