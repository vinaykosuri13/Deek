# ==========================
# Date & Time Tool
# Version: 2.0
# ==========================

from datetime import datetime
from zoneinfo import ZoneInfo


class DateTimeTool:

    def execute(self):

        now = datetime.now(ZoneInfo("Asia/Kolkata"))

        return now.strftime("%d %B %Y %I:%M %p")
