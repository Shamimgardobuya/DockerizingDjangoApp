from django.core.management.base import BaseCommand
from tasks.models import Tasks
from django.db import transaction

class Command(BaseCommand):
    help = "Updates priority default for existing users"
                
            
    def handle(self, *args, **options):
        chunk_size = 2

        try:
            all_tasks = Tasks.objects.all()
            buffer = []
            for task in all_tasks.iterator(chunk_size=chunk_size):
                if task:
                    task.priority = 2
                    buffer.append(task)
                    if len(buffer) >= chunk_size:
                        with transaction.atomic():
                            Tasks.objects.bulk_update(
                                buffer, ["priority"]
                            )
                        buffer.clear()
                    
            if buffer: #caters for leftover values that dont fit to chunk
                with transaction.atomic():
                    Tasks.objects.bulk_update(
                        buffer, ["priority"]
                    )
                self.stdout.write("table tasks altered successfully")
        except Exception as e:
            transaction.rollback()
            self.stdout.write(f"error occurred {e}")
        