# Base image پایدار Python
FROM python:3.12-slim

# نصب ابزارهای مورد نیاز (برای ffmpeg و build-essential)
RUN apt-get update && apt-get install -y \
    build-essential \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# دایرکتوری کاری داخل کانتینر
WORKDIR /app

# کپی فایل requirements.txt قبل از نصب پکیج‌ها
COPY requirements.txt .

# آپدیت pip و نصب تمام پکیج‌ها
RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# کپی کل پروژه
COPY . .

# دستور اجرای برنامه
CMD ["bash", "start"]
