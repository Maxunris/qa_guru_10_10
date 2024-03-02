import dataclasses


@dataclasses.dataclass
class Users:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    day: str
    moth: str
    year: str
    subjects: str
    hobbies: str
    photo: str
    current_address: str
    state: str
    city: str
    date_of_birth: str


user = Users(first_name='Max',
             last_name='Cheshire',
             email='Maxcheshire1@gmail.com',
             gender='Male',
             phone='7999123121',
             day='26',
             moth='March',
             year='1998',
             subjects='Computer Science',
             hobbies='Reading',
             photo='123.jpeg',
             current_address='Pushkina-kolotushkina, Moscow, Russia',
             state='NCR',
             city='Delhi',
             date_of_birth='26 March,1998')
