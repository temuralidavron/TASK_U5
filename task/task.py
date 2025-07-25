from celery import shared_task


@shared_task()
def add():
    print(f"I love python")
    return "I love python"