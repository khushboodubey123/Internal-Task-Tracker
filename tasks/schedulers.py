
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from .models import Task
import logging
from resources.constant import *

logger = logging.getLogger(__name__)

def expire_tasks_cron():

    now = timezone.now().date()
    expired_count = Task.objects.filter(
        end_date__lt=now,
        status__in=[PENDING, STATUS_IN_PROGRESS]
    ).update(status=EXPIRED)
   
    logger.info(f"Scheduler ran: {expired_count} tasks expired.")

def task_expire_scheduler():
    logger.info("::::::::::::::::::: Task Expire Scheduler Started :::::::::::::::::::")
    
    scheduler = BackgroundScheduler()
    scheduler.start()   
    scheduler.add_job(expire_tasks_cron, 'cron', hour=0, minute=0)

    
    
