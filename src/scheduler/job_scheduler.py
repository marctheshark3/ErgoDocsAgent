"""
Job Scheduler Module

This module handles scheduling periodic runs of the documentation processor.
"""

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import signal
import sys
import time

logger = logging.getLogger(__name__)

class JobScheduler:
    """Class to handle scheduling of documentation processing jobs."""
    
    def __init__(self, schedule_config):
        """
        Initialize with schedule configuration.
        
        Args:
            schedule_config (dict): Configuration for scheduling
        """
        self.frequency = schedule_config.get("frequency", "weekly")
        self.day_of_week = schedule_config.get("day_of_week", "monday")
        self.time = schedule_config.get("time", "00:00")
        self.scheduler = BackgroundScheduler()
        
        # Set up signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self._shutdown)
        signal.signal(signal.SIGTERM, self._shutdown)
    
    def add_job(self, func, *args, **kwargs):
        """
        Add a job to the scheduler.
        
        Args:
            func: The function to run
            *args, **kwargs: Arguments to pass to the function
        """
        # Parse the time
        hour, minute = self._parse_time(self.time)
        
        if self.frequency == "daily":
            trigger = CronTrigger(hour=hour, minute=minute)
            schedule_desc = f"daily at {self.time}"
        elif self.frequency == "weekly":
            trigger = CronTrigger(day_of_week=self.day_of_week.lower()[:3], hour=hour, minute=minute)
            schedule_desc = f"weekly on {self.day_of_week} at {self.time}"
        elif self.frequency == "monthly":
            trigger = CronTrigger(day=1, hour=hour, minute=minute)
            schedule_desc = f"monthly on the 1st at {self.time}"
        else:
            logger.warning(f"Unknown frequency: {self.frequency}, defaulting to weekly")
            trigger = CronTrigger(day_of_week=self.day_of_week.lower()[:3], hour=hour, minute=minute)
            schedule_desc = f"weekly on {self.day_of_week} at {self.time}"
        
        # Add the job
        self.scheduler.add_job(func, trigger=trigger, args=args, kwargs=kwargs)
        logger.info(f"Added job to run {schedule_desc}")
    
    def start(self):
        """Start the scheduler and wait for jobs to complete."""
        if not self.scheduler.get_jobs():
            logger.warning("No jobs added to scheduler")
            return
        
        try:
            logger.info("Starting scheduler")
            self.scheduler.start()
            
            # Keep the main thread alive
            while True:
                time.sleep(1)
                
        except (KeyboardInterrupt, SystemExit):
            self._shutdown()
    
    def _shutdown(self, signum=None, frame=None):
        """
        Shutdown the scheduler gracefully.
        
        Args:
            signum: Signal number (for signal handler)
            frame: Frame object (for signal handler)
        """
        logger.info("Shutting down scheduler")
        self.scheduler.shutdown()
        sys.exit(0)
    
    def _parse_time(self, time_str):
        """
        Parse a time string into hour and minute.
        
        Args:
            time_str (str): Time string in format HH:MM
            
        Returns:
            tuple: (hour, minute)
        """
        try:
            hour, minute = time_str.split(":")
            return int(hour), int(minute)
        except ValueError:
            logger.warning(f"Invalid time format: {time_str}, using 00:00")
            return 0, 0 