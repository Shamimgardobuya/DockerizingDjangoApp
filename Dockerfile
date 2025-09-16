FROM python:3.11-slim

#setting working directory

WORKDIR /app

#install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy app files
COPY . .

# Expose the port Django runs on (default 8000)
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "devops_lite.wsgi:application"]
