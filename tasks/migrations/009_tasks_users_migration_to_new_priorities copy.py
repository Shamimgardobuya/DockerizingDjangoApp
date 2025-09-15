from django.db import migrations, models


    
def update_all_tasks_to_new_priority(apps, schema_editor):
        Tasks =  apps.get_model('tasks', 'Tasks') 
        all_tasks = Tasks.objects.all()
        buffer = []
        chunk_size = 2
        for task in all_tasks.iterator(chunk_size=chunk_size):
            if task:
                if task.status == "not_done" :
                    task.new_status = "pending"
                
                buffer.append(task)
                if len(buffer) >= chunk_size:
                    Tasks.objects.bulk_update(
                                buffer, ["new_status"]
                            )
                    buffer.clear()
#11, #2  1
        if buffer: #caters for leftover values that dont fit to chunk
            Tasks.objects.bulk_update(
                    buffer, ["new_status"]
            )
                

class Migration(migrations.Migration):
    
    dependencies = [
        ('tasks', '0008_tasks_new_status_alter_tasks_reminder_time')
    ]
    operations = [
        migrations.RunPython(update_all_tasks_to_new_priority),
    ]