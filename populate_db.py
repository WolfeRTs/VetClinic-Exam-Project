import os
import django
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('DJANGO_SETTINGS_MODULE'))

django.setup()

from django.contrib.auth.models import Group, Permission
from VetClinic.images.models import Image
from VetClinic.services.models import ServiceCategory, Service, Medicine


def populate_groups_and_permissions():
    manager_group, _ = Group.objects.get_or_create(name='Manager')
    vet_group, _ = Group.objects.get_or_create(name='Vet')

    manager_permissions = Permission.objects.filter(codename__in=[
        'change_customuser', 'delete_customuser', 'view_customuser',
        'change_profile', 'delete_profile', 'view_profile',
        'add_logentry', 'view_logentry',
        'add_image', 'change_image', 'delete_image', 'view_image',
        'add_medicine', 'change_medicine', 'view_medicine', 'delete_medicine',
        'add_service', 'change_service', 'view_service', 'delete_service',
        'add_servicecategory', 'change_servicecategory', 'view_servicecategory', 'delete_servicecategory',
    ]).values_list('id', flat=True)
    for perm_id in manager_permissions:
        manager_group.permissions.add(perm_id)

    vet_permissions = Permission.objects.filter(codename__in=[
        'add_medicalreport', 'change_medicalreport', 'view_medicalreport', 'delete_medicalreport',
        'add_medicine', 'change_medicine', 'view_medicine', 'delete_medicine',
        'add_service', 'change_service', 'view_service', 'delete_service',
    ]).values_list('id', flat=True)
    for perm_id in vet_permissions:
        vet_group.permissions.add(perm_id)


def populate_categories_services_and_medicines():

    categories = {
        'Профилактични грижи': 'Preventive Care',
        'Хирургия': 'Surgery',
        'Диагностика': 'Diagnostics',
        'Стоматология': 'Dentistry',
        'Офталмология': 'Ophtalmology',
        'Ваксинация': 'Vaccination',
        'Груминг': 'Grooming'
    }
    created_categories = {}
    for category, category_en in categories.items():
        ServiceCategory.objects.get_or_create(name=category, name_bg=category, name_en=category_en)
        category_saved, _ = ServiceCategory.objects.get_or_create(
            name=category,
            defaults={'name_bg': category, 'name_en': category_en}
        )
        created_categories[category] = category_saved

    existing_services = Service.objects.values_list('name', flat=True)
    services = [
        {
            'name': 'Годишен преглед', 'name_bg': 'Годишен преглед', 'name_en': 'Annual Check-Up',
            'description': 'Комплексен здравен преглед за осигуряване на доброто състояние на вашия домашен любимец',
            'description_bg': 'Комплексен здравен преглед за осигуряване на доброто състояние на вашия домашен любимец',
            'description_en': 'Comprehensive health assessment to ensure your pet’s wellbeing',
            'category': 'Профилактични грижи',
        },
        {
            'name': 'Кастрация', 'name_bg': 'Кастрация', 'name_en': 'Spaying and Neutering',
            'description': 'Сигурна и ефективна хирургична стерилизация за домашни любимци',
            'description_bg': 'Сигурна и ефективна хирургична стерилизация за домашни любимци',
            'description_en': 'Safe and effective surgical sterilization for pets',
            'category': 'Хирургия',
        },
        {
            'name': 'Ортопедична хирургия', 'name_bg': 'Ортопедична хирургия', 'name_en': 'Orthopedic Surgery',
            'description': 'Хирургично лечение на фрактури и ставни проблеми',
            'description_bg': 'Хирургично лечение на фрактури и ставни проблеми',
            'description_en': 'Surgical treatment for fractures and joint issues',
            'category': 'Хирургия',
        },
        {
            'name': 'Кръвни тестове', 'name_bg': 'Кръвни тестове', 'name_en': 'Blood Tests',
            'description': 'Подробен кръвен анализ за откриване на скрити здравословни проблеми',
            'description_bg': 'Подробен кръвен анализ за откриване на скрити здравословни проблеми',
            'description_en': 'Detailed blood analysis to detect underlying health conditions',
            'category': 'Диагностика',
        },
        {
            'name': 'Рентгенография', 'name_bg': 'Рентгенография', 'name_en': 'X-ray Imaging',
            'description': 'Съвременна визуализация за диагностициране на вътрешни наранявания или заболявания',
            'description_bg': 'Съвременна визуализация за диагностициране на вътрешни наранявания или заболявания',
            'description_en': 'Advanced imaging to identify internal injuries or conditions',
            'category': 'Диагностика',
        },
        {
            'name': 'Ваксина срещу бяс', 'name_bg': 'Ваксина срещу бяс', 'name_en': 'Rabies Vaccine',
            'description': 'Важна ваксина за предпазване от инфекция с бяс',
            'description_bg': 'Важна ваксина за предпазване от инфекция с бяс',
            'description_en': 'Essential vaccine to protect against rabies infection',
            'category': 'Ваксинация',
        },
        {
            'name': 'Ваксина срещу парвовирус', 'name_bg': 'Ваксина срещу парвовирус', 'name_en': 'Parvovirus Vaccine',
            'description': 'Превенция срещу парвовирус при кученца и кучета',
            'description_bg': 'Превенция срещу парвовирус при кученца и кучета',
            'description_en': 'Prevention against parvovirus in puppies and dogs',
            'category': 'Ваксинация',
        },
        {
            'name': 'Поставяне на микрочип', 'name_bg': 'Поставяне на микрочип', 'name_en': 'Microchipping',
            'description': 'Имплантиране на микрочип за постоянна идентификация',
            'description_bg': 'Имплантиране на микрочип за постоянна идентификация',
            'description_en': 'Implanting a microchip for permanent identification',
            'category': 'Профилактични грижи',
        },
        {
            'name': 'Обезпаразитяване', 'name_bg': 'Обезпаразитяване', 'name_en': 'Deworming',
            'description': 'Рутинно лечение срещу вътрешни паразити',
            'description_bg': 'Рутинно лечение срещу вътрешни паразити',
            'description_en': 'Routine treatment for internal parasites',
            'category': 'Профилактични грижи',
        },
        {
            'name': 'Премахване на тумори', 'name_bg': 'Премахване на тумори', 'name_en': 'Tumor Removal',
            'description': 'Хирургично отстраняване на доброкачествени или злокачествени тумори',
            'description_bg': 'Хирургично отстраняване на доброкачествени или злокачествени тумори',
            'description_en': 'Surgical excision of benign or malignant tumors',
            'category': 'Хирургия',
        },
        {
            'name': 'Хирургия на меки тъкани', 'name_bg': 'Хирургия на меки тъкани', 'name_en': 'Soft Tissue Surgery',
            'description': 'Хирургия на вътрешни органи или меки тъкани като кожа',
            'description_bg': 'Хирургия на вътрешни органи или меки тъкани като кожа',
            'description_en': 'Surgery on internal organs or soft tissues like skin',
            'category': 'Хирургия',
        },
        {
            'name': 'Ултразвукови изследвания', 'name_bg': 'Ултразвукови изследвания', 'name_en': 'Ultrasound Scans',
            'description': 'Изследване за преглед на вътрешни органи и структури',
            'description_bg': 'Изследване за преглед на вътрешни органи и структури',
            'description_en': 'Imaging to examine internal organs and structures',
            'category': 'Диагностика',
        },
        {
            'name': 'Тестове за алергии', 'name_bg': 'Тестове за алергии', 'name_en': 'Allergy Testing',
            'description': 'Установяване на алергени, предизвикващи нежелани реакции при домашните любимци',
            'description_bg': 'Установяване на алергени, предизвикващи нежелани реакции при домашните любимци',
            'description_en': 'Identifying allergens causing adverse reactions in pets',
            'category': 'Диагностика',
        },
        {
            'name': 'Почистване на зъби', 'name_bg': 'Почистване на зъби', 'name_en': 'Dental Cleaning',
            'description': 'Професионално почистване за премахване на зъбен камък и плака',
            'description_bg': 'Професионално почистване за премахване на зъбен камък и плака',
            'description_en': 'Professional cleaning to remove tartar and plaque',
            'category': 'Стоматология',
        },
        {
            'name': 'Изваждане на зъб', 'name_bg': 'Изваждане на зъб', 'name_en': 'Tooth Extraction',
            'description': 'Премахване на увредени или изгнили зъби',
            'description_bg': 'Премахване на увредени или изгнили зъби',
            'description_en': 'Removal of damaged or decayed teeth',
            'category': 'Стоматология',
        },
        {
            'name': 'Ваксина срещу кучешки грип', 'name_bg': 'Ваксина срещу кучешки грип', 'name_en': 'Canine Influenza Vaccine',
            'description': 'Имунизация срещу щамове на кучешки грип',
            'description_bg': 'Имунизация срещу щамове на кучешки грип',
            'description_en': 'Immunization against canine flu strains',
            'category': 'Ваксинация',
        },
        {
            'name': 'Подстригване на козината', 'name_bg': 'Подстригване на козината', 'name_en': 'Hair Trimming',
            'description': 'Подстригване на козината за комфорт и хигиена',
            'description_bg': 'Подстригване на козината за комфорт и хигиена',
            'description_en': 'Styling and trimming fur for comfort and hygiene',
            'category': 'Груминг',
        },
        {
            'name': 'Подрязване на ноктите', 'name_bg': 'Подрязване на ноктите', 'name_en': 'Nail Clipping',
            'description': 'Редовна поддръжка за предотвратяване на прекомерно израстване',
            'description_bg': 'Редовна поддръжка за предотвратяване на прекомерно израстване',
            'description_en': 'Regular maintenance to prevent overgrowth',
            'category': 'Груминг',
        },
        {
            'name': 'Цялостен преглед на очите', 'name_bg': 'Цялостен преглед на очите', 'name_en': 'Comprehensive Eye Examination',
            'description': 'Подробен преглед за оценка на зрението, здравето на очите и установяване на отклонения',
            'description_bg': 'Подробен преглед за оценка на зрението, здравето на очите и установяване на отклонения',
            'description_en': 'A detailed examination to assess vision, eye health, and detect abnormalities',
            'category': 'Офталмология',
        },
        {
            'name': 'Лечение на очни инфекции', 'name_bg': 'Лечение на очни инфекции', 'name_en': 'Treatment of Eye Infections',
            'description': 'Диагностика и лечение на бактериални, вирусни или гъбични инфекции в очите',
            'description_bg': 'Диагностика и лечение на бактериални, вирусни или гъбични инфекции в очите',
            'description_en': 'Diagnosis and treatment of bacterial, viral, or fungal infections in the eyes',
            'category': 'Офталмология',
        },
    ]

    service_instances = [
        Service.objects.get_or_create(
            name=service['name'],
            category=created_categories[service['category']],
            name_bg=service['name_bg'],
            name_en=service['name_en'],
            description=service['description'],
            description_bg=service['description_bg'], description_en=service['description_en'],
        )
        for service in services
        if service['name'] not in existing_services
    ]

    existing_medicines = Medicine.objects.values_list('name', flat=True)
    medicines = [
        {
            'name':'Amoxicillin',
            'description':'Антибиотик за лечение на бактериални инфекции',
            'description_bg':'Антибиотик за лечение на бактериални инфекции',
            'description_en':'Antibiotic for treating bacterial infections',
            'dosages':'10-20 mg/kg',
        },
        {
            'name':'Meloxicam',
            'description':'Нестероидно противовъзпалително лекарство за облекчаване на болката',
            'description_bg':'Нестероидно противовъзпалително лекарство за облекчаване на болката',
            'description_en':'Non-steroidal anti-inflammatory drug (NSAID) for pain relief',
            'dosages':'10-20 mg/kg',
        },
        {
            'name':'Metronidazole',
            'description':'Лечение на стомашно-чревни инфекции и протозойни заболявания',
            'description_bg':'Лечение на стомашно-чревни инфекции и протозойни заболявания',
            'description_en':'Treatment for gastrointestinal infections and protozoal diseases',
            'dosages':'10-25 mg/kg',
        },
        {
            'name':'Enrofloxacin (Baytril)',
            'description':'Широкоспектърен антибиотик за лечение на бактериални инфекции при домашни любимци',
            'description_bg':'Широкоспектърен антибиотик за лечение на бактериални инфекции при домашни любимци',
            'description_en':'Broad-spectrum antibiotic for bacterial infections in pets',
            'dosages':'5–20 mg/kg',
        },
        {
            'name':'Carprofen (Rimadyl)',
            'description':'Облекчава болката при артрит или след операции',
            'description_bg':'Облекчава болката при артрит или след операции',
            'description_en':'Pain management for arthritis or surgery recovery',
            'dosages':'2–4 mg/kg',
        },
        {
            'name':'Praziquantel (Droncit)',
            'description':'Лекарство за лечение на тении',
            'description_bg':'Лекарство за лечение на тении',
            'description_en':'Dewormer for tapeworms',
            'dosages':'5–10 mg/kg',
        },
        {
            'name':'Tobramycin Eye Drops',
            'description':'Антибиотик за бактериални очни инфекции',
            'description_bg':'Антибиотик за бактериални очни инфекции',
            'description_en':'Antibiotic for bacterial eye infections',
            'dosages':'1–2 drops',
        },
        {
            'name':'Rabies Vaccine',
            'description':'Ваксина против бяс',
            'description_bg':'Ваксина против бяс',
            'description_en':'Prevents rabies in pets',
            'dosages':'1 ml',
        },
    ]
    medicine_instances = [
        Medicine.objects.get_or_create(
            name=medicine['name'],
            defaults={
                'description': medicine['description'],
                'description_bg': medicine['description_bg'],
                'description_en': medicine['description_en'],
                'dosages': medicine['dosages'],
            }
        )
        for medicine in medicines
        if medicine['name'] not in existing_medicines
    ]


def populate_images():
    existing_images = Image.objects.values_list('image', flat=True)
    images = [
        {
            'image':'images/slide1.jpg',
            'category':'Carousel',
        },
        {
            'image':'images/slide2.jpg',
            'category':'Carousel',
        },
        {
            'image':'images/slide3.jpg',
            'category':'Carousel',
        },
        {
            'image':'images/slide4.jpg',
            'category':'Carousel',
        },
        {
            'image':'images/slide5.jpg',
            'category':'Carousel',
        },
        {
            'image':'images/slide6.jpg',
            'category':'Carousel',
        },
        {
            'image':'images/slide7.jpg',
            'category':'Carousel',
        },
        {
            'image':'images/slide8.jpg',
            'category':'Carousel',
        },
        {
            'image':'images/slide9.jpg',
            'category':'Carousel',
        },
        {
            'image':'images/slide10.jpg',
            'category':'Carousel',
        },
        {
            'image':'images/gallery1.jpg',
            'category':'Gallery',
        },
        {
            'image':'images/gallery2.jpg',
            'category':'Gallery',
        },
        {
            'image':'images/gallery3.jpg',
            'category':'Gallery',
        },
        {
            'image':'images/gallery4.jpg',
            'category':'Gallery',
        },
        {
            'image':'images/gallery5.jpg',
            'category':'Gallery',
        },
        {
            'image':'images/gallery6.jpg',
            'category':'Gallery',
        },
        {
            'image':'images/gallery7.jpg',
            'category':'Gallery',
        },
        {
            'image':'images/gallery8.jpg',
            'category':'Gallery',
        },
        {
            'image':'images/gallery9.jpg',
            'category':'Gallery',
        },
        {
            'image':'images/gallery10.jpg',
            'category':'Gallery',
        }
    ]

    image_instances = [
        Image.objects.get_or_create(
            image=img['image'],
            category=img['category'],
        )
        for img in images
    ]
    images_to_create = [img for img, _ in image_instances if img.image not in existing_images]
    Image.objects.bulk_create(images_to_create)


populate_groups_and_permissions()
populate_categories_services_and_medicines()
populate_images()