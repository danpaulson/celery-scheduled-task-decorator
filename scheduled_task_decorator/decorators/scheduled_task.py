from datetime import timedelta
from celery.schedules import crontab


def scheduled_task(name: str = None,  minutes=None, hour=None, day_of_week=None, day_of_month=None, seconds=None):
    def decorator(func):
        if seconds is not None:
            # If seconds are specified, use timedelta for scheduling
            func._celery_schedule = timedelta(seconds=seconds)
        else:
            # Otherwise, use crontab for scheduling
            schedule_args = {}
            if minutes is not None:
                schedule_args['minute'] = minutes
            if hour is not None:
                schedule_args['hour'] = hour
            if day_of_week is not None:
                schedule_args['day_of_week'] = day_of_week
            if day_of_month is not None:
                schedule_args['day_of_month'] = day_of_month

            func._celery_schedule = crontab(**schedule_args)

        func._celery_task_name = f"{name}"
        return func

    return decorator
