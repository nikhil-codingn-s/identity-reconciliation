from flask import Blueprint, request, jsonify
from .database import db
from .models import Contact
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/identify', methods=['POST'])
def identify():
    data = request.get_json()
    email = data.get('email')
    phone = data.get('phoneNumber')

    # Step 1: Find existing contacts by email or phone
    existing_contacts = Contact.query.filter(
        (Contact.email == email) | (Contact.phoneNumber == phone)
    ).all()

    if not existing_contacts:
        # Step 2: No match found, create new primary contact
        new_contact = Contact(email=email, phoneNumber=phone, linkPrecedence='primary')
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({
            "primaryContactId": new_contact.id,
            "emails": [new_contact.email],
            "phoneNumbers": [new_contact.phoneNumber],
            "secondaryContactIds": []
        }), 200

    # Step 3: Determine the primary contact
    primary_contact = min(existing_contacts, key=lambda c: c.createdAt)
    all_contacts = set(existing_contacts)

    # Step 4: Add new info as secondary if missing
    already_exists = any(c.email == email and c.phoneNumber == phone for c in existing_contacts)
    if not already_exists:
        new_contact = Contact(
            email=email,
            phoneNumber=phone,
            linkedId=primary_contact.id,
            linkPrecedence='secondary'
        )
        db.session.add(new_contact)
        db.session.commit()
        all_contacts.add(new_contact)

    # Step 5: Prepare the response
    emails = list(set(c.email for c in all_contacts if c.email))
    phones = list(set(c.phoneNumber for c in all_contacts if c.phoneNumber))
    secondary_ids = [c.id for c in all_contacts if c.linkPrecedence == 'secondary']

    return jsonify({
        "primaryContactId": primary_contact.id,
        "emails": emails,
        "phoneNumbers": phones,
        "secondaryContactIds": secondary_ids
    }), 200
