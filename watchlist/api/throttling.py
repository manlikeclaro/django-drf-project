from datetime import datetime, timedelta

from django.utils.timesince import timesince
from rest_framework.exceptions import Throttled
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


# Function to format the wait time into a human-readable string
def format_wait_time(seconds):
    future_time = datetime.now() + timedelta(seconds=seconds)
    return timesince(datetime.now(), future_time)


class FormattedUserRateThrottle(UserRateThrottle):
    def wait(self):
        # Call the super class's wait method to get the wait time in seconds
        wait_time = super().wait()
        if wait_time:
            return format_wait_time(wait_time)
        return None

    def throttle_failure(self):
        wait_time = self.wait()
        detail = f"Request was throttled. Expected available in {wait_time}."
        raise Throttled(detail=detail)


class FormattedAnonRateThrottle(AnonRateThrottle):
    def wait(self):
        # Call the super class's wait method to get the wait time in seconds
        wait_time = super().wait()
        if wait_time:
            return format_wait_time(wait_time)
        return None

    def throttle_failure(self):
        wait_time = self.wait()
        detail = f"Request was throttled. Expected available in {wait_time}."
        raise Throttled(detail=detail)
