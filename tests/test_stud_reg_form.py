from demoqa_tests.pages.registration_page import RegistrationPage


def test_fill_form_automation_flow():
    registration_page = RegistrationPage()
    registration_page.open()
    # WHEN
    (
        registration_page
        .fill_first_name('Max')
        .fill_last_name('Cheshire')
        .fill_email('Maxcheshire1@gmail.com')
        .select_gender('Male')
        .fill_mobile_number('7999123121')
        .fill_date_of_birth('26 March 1998')
        .fill_subject('Maths')
        .select_hobby('Reading')
        .upload_picture('123.jpeg')
        .fill_current_address('Sushkina-kolotushkina, Moscow, Russia')
        .select_state('NCR')
        .select_city('Delhi')
        .submit()
    )

    # THEN
    registration_page.should_register_user_with('Max Cheshire',
                                                'Maxcheshire1@gmail.com',
                                                'Male',
                                                '7999123121',
                                                '26 March,1998',
                                                'Maths',
                                                'Reading',
                                                '123.jpeg',
                                                'Pushkina-kolotushkina, Moscow, Russia',
                                                'NCR Delhi'

                                                )