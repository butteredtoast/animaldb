#!/usr/bin/env python
import os
import sys

import argparse

os.environ['DJANGO_SETTINGS_MODULE'] = 'animaldb.settings'

import django
django.setup()

from animals.utils import Animals
from django.core.management import call_command


class DatabaseRunner:
    
    def __init__(self, **kwargs):
        self.animaldb = Animals()

    def createdb(self):
        """Used to create a database. Only sqlite is supported for now"""
        call_command('makemigrations')
        call_command('migrate')

    def create_owner(self):
        """Used to create an owner"""
        self.animaldb.create_owner()

    def create_cat(self):
        """Used to create a cat"""
        self.animaldb.create_cat()

    def create_dog(self):
        """Used to create a dog"""
        self.animaldb.create_dog()

    def update_owner(self):
        """Used to update an owner"""
        self.animaldb.create_owner()

    def update_cat(self):
        """Used to update a cat"""
        self.animaldb.create_cat()

    def update_dog(self):
        """Used to update a dog"""
        self.animaldb.create_dog()

    def delete_owner(self):
        """Used to delete an owner"""
        self.animaldb.delete_owner()

    def delete_cat(self):
        """Used to delete a cat"""
        self.animaldb.delete_cat()

    def delete_dog(self):
        """Used to delete a dog"""
        self.animaldb.delete_dog()

    def list_owners(self):
        """Used to list all owners"""
        self.animaldb.list_owners()

    def list_cats(self):
        """Used to list all cats belonging to a cat"""
        self.animaldb.delete_cat()

    def list_dogs(self):
        """Used to list all dogs belonging to an owner"""
        self.animaldb.delete_dog()
    


if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'animaldb.settings'

    parser = argparse.ArgumentParser("Interact with the AnimalDB database")
    subparsers = parser.add_subparsers(help='sub-command help')

    parser.add_argument(
        '-c', '--createdb', dest='createdb', action='store_true', default=False,
        help="Tells AnimalDB to create the database."
    )

    parser.add_argument(
        '-co', '--create_owner', dest='create_owner', nargs='?',
        help="Tells AnimalDB to create an owner. A first_name, last_name and birthday (optional) should be provided"
    )
    

    parser.add_argument(
        '-cc', '--create_cat', dest='create_cat', nargs='?',
        help="Tells AnimalDB to create a cat. An owner_id, name and birthday (optional) should be provided"
    )

    parser.add_argument(
        '-cd', '--create_dog', dest='create_dog', nargs='?',
        help="Tells AnimalDB to create a dog. An owner_id, name and birthday (optional) should be provided"
    )

    parser.add_argument(
        '-lo', '--list_owners', dest='list_owners',
        help="Tells AnimalDB to list all owners."
    )

    parser.add_argument(
        '-lc', '--list_cats', dest='list_cats', nargs='?', type=int,
        help="Tells AnimalDB to list all cats belonging to an owner. An owner_id should be provided"
    )

    parser.add_argument(
        '-ld', '--list_dogs', dest='list_dogs', nargs='+', type=int,
        help="Tells AnimalDB to list all dogs belonging to an owner. An owner_id should be provided"
    )

    parser.add_argument(
        '-uo', '--update_owner', dest='update_owner', nargs='?',
        help="Tells AnimalDB to update an owner. (Only the first name came be modified). An owner ID should be provided"
    )

    parser.add_argument(
        '-uc', '--update_cat', dest='update_cat', nargs='?',
        help="Tells AnimalDB to update a cat. (Only the name came be modified). A cat ID should be provided"
    )

    parser.add_argument(
        '-ud', '--update_dog', dest='update_dog', nargs='?',
        help="Tells AnimalDB to update a dog. (Only the  name came be modified). A dog ID should be provided"
    )

    parser.add_argument(
        '-do', '--delete_owner', dest='delete_owner', nargs='+', type=int,
        help="Tells AnimalDB to delete an owner. An owner ID should be provided"
    )

    parser.add_argument(
        '-dc', '--delete_cat', dest='delete_cat', nargs='+', type=int,
        help="Tells AnimalDB to delete a cat. A cat ID should be provided"
    )

    parser.add_argument(
        '-dd', '--delete_dog', dest='delete_dog', nargs='+', type=int,
        help="Tells AnimalDB to delete a dog. A dog ID should be provided"
    )
    
    options = parser.parse_args()

    database = DatabaseRunner()

    # TODO: Refactor to not use unmaintainable if-chain
    if options.createdb: database.createdb()
    elif options.create_owner: database.create_owner(),        
    elif options.create_cat: database.create_cat(),
    elif options.create_dog: database.create_dog(),
    elif options.list_owners: database.list_owners(),
    elif options.list_cats: database.list_cats(),
    elif options.list_dogs: database.list_dogs(),
    elif options.update_owner: database.update_owner(),        
    elif options.update_cat: database.update_cat(),
    elif options.update_dog: database.update_dog(),
    elif options.delete_owner: database.delete_owner(),        
    elif options.delete_cat: database.delete_cat(),
    else: database.delete_dog()    