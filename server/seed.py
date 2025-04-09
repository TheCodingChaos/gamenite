#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Clearing db...")
        db.drop_all()
        db.create_all()

        print("Seeding users...")

        users = []
        for _ in range(5):
            user = User(
                name=fake.name(),
                email=fake.email(),
            )
            user.password_hash = 'password123'
            users.append(user)

        admin = User(
            name="Admin User",
            email="admin@gamenite.dev",
            is_admin=True
        )
        admin.password_hash = 'adminpass'
        users.append(admin)

        db.session.add_all(users)
        db.session.commit()

        print("Seeding complete.")
