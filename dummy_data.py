import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
import random
import datetime

from campaign.models import Project, ProjectImage, Category
from django.contrib.auth.models import User



def seed_category(n):
    fake = Faker()

    for _ in range(n):
        Category.objects.create(
            name = fake.name()
        )

def seed_project(n):
    fake = Faker()

    projects_images = ['1.jpeg', '2.jpg', '3.png', '5.jpeg']
    
    # Fetching existing user IDs
    user_ids = list(User.objects.values_list('id', flat=True))

    for _ in range(n):
         Project.objects.create(
            title = fake.name(),
            details = fake.text(max_nb_chars=100),
            image = f'projects/images/{projects_images[random.randint(0, 3)]}',
            catergory = Category.objects.get(id=random.randint(1, 20)),  # Assuming you have 20 categories
            owner = User.objects.get(id=random.choice(user_ids)),  # Choosing a random user ID from existing IDs
            target = round(random.uniform(10000, 300000), 2),
            end_date = datetime.date.today() + datetime.timedelta(days=random.randint(30, 365)),  # Assuming project lasts between 30 days to 1 year
        )





seed_category(20)


seed_project(20)
