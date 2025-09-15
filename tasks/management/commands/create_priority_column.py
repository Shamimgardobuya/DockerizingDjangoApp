from django.core.management.base import BaseCommand
from tasks.models import Tasks
from django.db import connection
class Command(BaseCommand):
    help = "Creates priority column and provides default for existing users"
                
    def chunking_generator(self, curs, query, chunk_size=2):
        curs.execute(query)
        while True:
            rows = curs.fetchmany(chunk_size)
            if not rows:
                break
            yield rows
            
            
    def handle(self, *args, **options):
        cursor = connection.cursor()
        
        try:
            with connection.cursor() as cursor:
                
                # create_priority_column = """ ALTER TABLE tasks_tasks 
                # ADD COLUMN priority INT 
                
                # """
                # cursor.execute(create_priority_column)
                # #update existing data for complete migration
                
                for chunk in self.chunking_generator(cursor, """
                        SELECT priority FROM tasks_tasks
                        """, 2):
                    update = []
                    for priority in chunk:
                        priority = 1 #transformation
                        update.append((priority,))
                        
                    
                print(update)
                cursor.executemany("""
                            UPDATE  tasks_tasks
                            SET priority = %s
                            WHERE priority IS NULL
                            """, update)
                
                #enforce future data by adding constraint and default
                cursor.execute(""" ALTER TABLE tasks_tasks
                        ALTER COLUMN priority SET DEFAULT 0;
                    
                """)
                cursor.execute(""" ALTER TABLE tasks_tasks
                        ALTER COLUMN priority SET NOT NULL ;
                    
                """)
                # cursor.commit()
                self.stdout.write("table tasks altered successfully")
        except Exception as e:
            connection.rollback()
            self.stdout.write(f"error occurred {str(e)}")
        