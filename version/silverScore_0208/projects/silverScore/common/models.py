from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.

# phone, created_at 추가. custom
class ExtendUserForm(AbstractUser):  # -> config/settings.py 에 AUTH_USER_MODEL = 'common.User' 로서 추가. why? : AbstractUser 로서 사용하므로
    phone_regex = RegexValidator(regex=r'^01([0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})$') # 정규식 011-123-4567 혹은 010-1234-5678 기준
    phone = models.CharField(validators=[phone_regex], max_length=13, unique=True, verbose_name='phone') # 010-1234-5678 기준 갯수
    # ref : https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.DateField.auto_now_add

    def save(self, *args, **kwargs):
        print('saving')
        try:
            self.save()
        except:
            print('not save')
        super(ExtendUserForm, self).save(*args, **kwargs)

    class Meta:
        abstract = True