from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from your_module import extract_file_data_2021, extract_file_data_2022


class Upload_File(models.Model):
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'upload_file'
        verbose_name_plural = 'upload_files'


@receiver(post_save, sender=Upload_File)
def upload_file_post_save(sender, instance, created, **kwargs):
    if created and instance.file:
        extract_file_data_2021(file_name=instance.file.path, file_id=instance.id)
        return {'status': 'ok'}


class Upload_File2(models.Model):
    file = models.FileField(upload_to='files2/')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'upload_file2'
        verbose_name_plural = 'upload_files2'


@receiver(post_save, sender=Upload_File2)
def upload_file2_post_save(sender, instance, created, **kwargs):
    if created and instance.file:
        extract_file_data_2022(file_name=instance.file.path, file_id=instance.id)
        return {'status': 'ok'}


class Mark(models.Model):
    mark_name = models.CharField(max_length=100)

    def __str__(self):
        return self.mark_name

    class Meta:
        db_table = 'mark'
        verbose_name_plural = 'marks'


class Model1(models.Model):
    model_name = models.CharField(max_length=100)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name='models')

    def __str__(self):
        return self.model_name

    class Meta:
        db_table = 'model1'
        verbose_name_plural = 'models'


class DATA21(models.Model):
    time = models.DateTimeField(auto_created=True, default=datetime.datetime.now, verbose_name='data yaratilgan vaqti')
    file_id = models.ForeignKey(Upload_File, on_delete=models.CASCADE)
    sana = models.DateField()
    model = models.ForeignKey(Model1, on_delete=models.CASCADE, related_name='data21')
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)

    def __str__(self):
        return f"Data21 - {self.sana}, file_id: {self.file_id}"

    class Meta:
        db_table = 'data21'
        verbose_name_plural = 'data21'


class DATA22(models.Model):
    time = models.DateTimeField(auto_created=True, default=datetime.datetime.now, verbose_name='data yaratilgan vaqti')
    file_id = models.ForeignKey(Upload_File2, on_delete=models.CASCADE)
    sana = models.DateField()
    model = models.ForeignKey(Model1, on_delete=models.CASCADE, related_name='data22')
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"Data22 - {self.model.model_name}, {self.sana}, {self.country}"

    class Meta:
        db_table = 'data22'
        verbose_name_plural = 'data22'
