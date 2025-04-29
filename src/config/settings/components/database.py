import os
from config.settings import BASE_DIR
import pymysql
pymysql.install_as_MySQLdb()


# 数据库配置
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'datads',
       'USER': 'root',
       'PASSWORD': 'dDRpR5dwhLJnqLiL',
       'HOST': '127.0.0.1',
       'PORT': '3307',
       'OPTIONS': {
           'charset': 'utf8mb4',
           'init_command': 'SET sql_mode="STRICT_TRANS_TABLES", time_zone="+08:00"',
       },
        'CONN_MAX_AGE': 60,  # 连接复用
        'POOL_OPTIONS': {
            'POOL_SIZE': 20,  # 连接池大小
            'MAX_OVERFLOW': 10
        }
   }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
#    }
#}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
