import pytz
import time
import threading
from datetime import datetime

class TimeZoneModel:

    def __init__(self):
        self.zone = "Australia/Sydney" # Default Timezone
        self.fmt_datetime = "%Y-%m-%d %I:%M:%S %p"
        self.fmt_date = "%a %Y-%m-%d"
        self.fmt_time = "%I:%M:%S %p"

    def get_zone(self):
        return self.zone

    def set_zone(self, zone):
        self.zone = zone

    def get_native_time(self):
        # get local time
        native_time = datetime.now()
        return native_time

    def get_zone_time(self, zone=None):
        if zone is None:
            zone_time = datetime.now(pytz.timezone(self.zone)).strftime(self.fmt_datetime)
        else:
            zone_time = datetime.now(pytz.timezone(zone)).strftime(self.fmt_datetime)
        return zone_time

    def get_zonedate(self, zone=None):
        if zone is None:
            zonedate = datetime.now(pytz.timezone(self.zone)).strftime(self.fmt_date)
        else:
            zonedate = datetime.now(pytz.timezone(zone)).strftime(self.fmt_date)
        return zonedate

    def get_zonetime(self, zone=None):
        if zone is None:
            zonetime = datetime.now(pytz.timezone(self.zone)).strftime(self.fmt_time)
        else:
            zonetime = datetime.now(pytz.timezone(zone)).strftime(self.fmt_time)
        return zonetime

    '''
    def get_syd_time(self):
        syd_time = datetime.now(pytz.timezone("Australia/Sydney")).strftime("%Y-%m-%d %I:%M:%S %p")
        return syd_time

    def get_kr_time(self):
        kr_time = datetime.now(pytz.timezone('Asia/Seoul')).strftime("%Y-%m-%d %I:%M:%S %p")
        return kr_time
    '''

    def get_common_timezones(self):
        common_timezones = pytz.common_timezones
        return common_timezones

    def convert_to_timezone(self, date_str, trg_timezone):
        print("date string: "+date_str)
        print("target timezone: "+trg_timezone)
        datetime_obj = datetime.strptime(date_str, self.fmt_datetime)

        # datetime_obj_trg = datetime_obj.replace(tzinfo=pytz.timezone(trg_timezone))
        datetime_obj_trg = datetime_obj.astimezone(pytz.timezone(trg_timezone))
        #print("return value is: " + datetime_obj_trg)
        return datetime_obj_trg.strftime(self.fmt_datetime)