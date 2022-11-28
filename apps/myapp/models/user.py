from datetime import datetime
from uuid import UUID


class Dob:
    date: datetime
    age: int

    def __init__(self, date: datetime, age: int) -> None:
        self.date = date
        self.age = age


class ID:
    name: str
    value: str

    def __init__(self, name: str, value: str) -> None:
        self.name = name
        self.value = value


class Coordinates:
    latitude: str
    longitude: str

    def __init__(self, latitude: str, longitude: str) -> None:
        self.latitude = latitude
        self.longitude = longitude


class Street:
    number: int
    name: str

    def __init__(self, number: int, name: str) -> None:
        self.number = number
        self.name = name


class Timezone:
    offset: str
    description: str

    def __init__(self, offset: str, description: str) -> None:
        self.offset = offset
        self.description = description


class Location:
    street: Street
    city: str
    state: str
    country: str
    postcode: int
    coordinates: Coordinates
    timezone: Timezone

    def __init__(self, street: Street, city: str, state: str,
                 country: str, postcode: int, coordinates: Coordinates,
                 timezone: Timezone) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.postcode = postcode
        self.coordinates = coordinates
        self.timezone = timezone


class Login:
    uuid: UUID
    username: str
    password: str
    salt: str
    md5: str
    sha1: str
    sha256: str

    def __init__(self, uuid: UUID, username: str, password: str,
                 salt: str, md5: str, sha1: str, sha256: str) -> None:
        self.uuid = uuid
        self.username = username
        self.password = password
        self.salt = salt
        self.md5 = md5
        self.sha1 = sha1
        self.sha256 = sha256


class Name:
    first: str
    last: str

    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last


class Picture:
    large: str
    medium: str
    thumbnail: str

    def __init__(self, large: str, medium: str, thumbnail: str) -> None:
        self.large = large
        self.medium = medium
        self.thumbnail = thumbnail


class User:
    gender: str
    name: Name
    location: Location
    email: str
    login: Login
    dob: Dob
    registered: Dob
    phone: str
    cell: str
    id: ID
    picture: Picture
    nat: str

    def __init__(self,
                 name: Name,
                 email: str,
                 gender: str = None,
                 location: Location = None,
                 login: Login = None,
                 dob: Dob = None,
                 registered: Dob = None,
                 phone: str = None,
                 cell: str = None,
                 id: ID = None,
                 picture: Picture = None,
                 nat: str = None
                 ) -> None:
        self.gender = gender
        self.name = name
        self.location = location
        self.email = email
        self.login = login
        self.dob = dob
        self.registered = registered
        self.phone = phone
        self.cell = cell
        self.id = id
        self.picture = picture
        self.nat = nat

    def __str__(self) -> str:
        return f'{self.name.first} {self.name.last} ({self.email})'
