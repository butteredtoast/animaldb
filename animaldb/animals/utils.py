from animals.models import Owner, Cat, Dog
from django.db import IntegrityError


class Animals:
    
    def __init__(self):
        self.model_mappings = {'owner': Owner, 'cat': Cat, 'dog': Dog}

    def create_value(self, model_name, **kwargs):
        """Used to create an object in the database
            :param model_name: The name of the model for which an object is being created
            :param kwargs: Any extra values to be added to the model
        """
        model = self.model_mappings.get(model_name.lower())
        return model.objects.create(**kwargs)

    def create_owner(self, **kwargs):
        try:
            owner = self.create_value('owner', **kwargs)
            print(owner)
        except IntegrityError:
            print("Please provide the correct values for Owner: first_name, last_name and birthday (optional)")

    def create_cat(self, **kwargs):
        try:
            owner = Owner.objects.get(id=kwargs.get('owner_id', ''))
            cat = self.create_value('cat', **kwargs)
            print(cat)
        except Owner.DoesNotExist:
            print("Owner with specified ID does not exist in the database")
        except IntegrityError:
            print("Please provide the correct values for Cat: Owner ID, name and birthday (optional)")

    def create_dog(self, **kwargs):
        try:
            owner = Owner.objects.get(id=kwargs.get('owner_id', ''))
            dog = self.create_value('dog', **kwargs)
            print(dog)
        except Owner.DoesNotExist:
            print("Owner with specified ID does not exist in the database")
        except IntegrityError:
            print("Please provide the correct values for Dog: Owner ID, name and birthday (optional)")

    def list_values(self, model_name, **kwargs):
        """Used to list all objects of the specified model in the database
            :param model_name: The name of the model for which objects are being retreived
            :return: A list of objects            
        """
        model = self.model_mappings.get(model_name.lower())
        models = model.objects.filter(**kwargs)
        for row in models:
            print(row)

    def list_owner(self, **kwargs):
        self.list_values('owner', **kwargs)

    def list_dog(self, **kwargs):
        self.list_values('dog', **kwargs)

    def list_cat(self, **kwargs):
        self.list_values('cat', **kwargs)

    def update_value(self, model_name, **kwargs):
        """Used to update an object in the database
            :param model_name: The name of the model for which an object is being created
            :param kwargs: Any extra values to be added to the model
        """
        model = self.model_mappings.get(model_name.lower())
        try:
            obj = model.objects.get(pk=kwargs.pop(pk, None))
            for kw, val in kwargs.items():
                setattr(obj, kw, val)
        except Exception:
            print("An invalid value was provided")

    def update_value(self, model_name, **kwargs):
        """Used to delete an object in the database
            :param model_name: The name of the model for which an object is being deleted
            :param kwargs: Any extra values to be added to the model
        """
        model = self.model_mappings.get(model_name.lower())        
        try:
            all = kwargs.get('all', False)
            if all:
                model.objects.all()
            else:
                pk = kwargs.get('pk', False)
                model.objects.get(pk=pk).delete()            
        except Exception:
            print("An invalid value was provided!")