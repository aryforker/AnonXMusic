# Base image پایدار Python
FROM python:3.12-slim

# نصب ابزارهای مورد نیاز (ffmpeg و build-essential)
RUN apt-get update && apt-get install -y \
    build-essential \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# ست کردن دایرکتوری کاری
WORKDIR /app

# کپی کل پروژه قبل از نصب پکیج‌ها
COPY . /app

# آپدیت pip و نصب requirements
RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# دستور اجرای برنامه
CMD ["bash", "start"]

