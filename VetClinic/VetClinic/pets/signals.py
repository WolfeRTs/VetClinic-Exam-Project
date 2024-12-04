from django.contrib.auth import get_user_model
from django.db.models.signals import pre_delete
from django.dispatch import receiver


UserModel = get_user_model()

@receiver(pre_delete, sender=UserModel)
def update_medical_report_doctor_name(sender, instance, **kwargs):
    if instance.medical_reports.exists():
        for report in instance.medical_reports.all():
            report.doctor_name = instance.profile.get_name() or None
            report.save()
