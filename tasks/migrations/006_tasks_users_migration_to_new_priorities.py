from django.db import migrations, models


    
def update_all_tasks_to_new_priority(apps, schema_editor):
        Tasks =  apps.get_model('tasks', 'Tasks') 
        all_tasks = Tasks.objects.all()
        buffer = []
        chunk_size = 2
        for task in all_tasks.iterator(chunk_size=chunk_size):
            if task:
                if task.priority == 1 :
                    task.new_priority = "medium"
                if task.priority == 2:
                    task.new_priority = "high"
                if task.priority == 0:
                    task.new_priority = "low"
                
                buffer.append(task)
                if len(buffer) >= chunk_size:
                    Tasks.objects.bulk_update(
                                buffer, ["new_priority"]
                            )
                    buffer.clear()
#11, #2  1
        if buffer: #caters for leftover values that dont fit to chunk
            Tasks.objects.bulk_update(
                    buffer, ["new_priority"]
            )
                

class Migration(migrations.Migration):
    
    dependencies = [
        ('tasks', '0005_tasks_new_priority_alter_tasks_reminder_time')
    ]
    operations = [
        migrations.RunPython(update_all_tasks_to_new_priority),
    ]