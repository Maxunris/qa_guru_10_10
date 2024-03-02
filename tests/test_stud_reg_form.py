from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.data import users


def test_user_registration_form():
    client = users.user
    registration_pages = RegistrationPage()
    registration_pages.open()
    registration_pages.registration_form_page(client)
    registration_pages.should_registration_form(client)