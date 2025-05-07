from .models import FoodItem

def load_sample_data():
    if FoodItem.objects.exists():
        return  # Prevent duplicate insertion
    FoodItem.objects.create(name="Rice", quantity=50)
    FoodItem.objects.create(name="Wheat", quantity=30)
    FoodItem.objects.create(name="Lentils", quantity=20)