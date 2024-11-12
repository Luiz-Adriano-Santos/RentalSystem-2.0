from enum import Enum

class GenderEnum(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class StatusEnum(Enum):
    SENT = "SENT"
    CANCELED = "CANCELED"
    IN_PROGRESS = "IN PROGRESS"
    RETURNED = "RETURNED"