from services.local_db_client_repository import LocalDBClientRepository
from services.local_db_pet_repository import LocalDBCPetRepository
from services.local_db_consultation_repository import LocalDBCConsultationRepository


def get_client_repository():
    return LocalDBClientRepository('clinic.db')


def get_pet_repository():
    return LocalDBCPetRepository('clinic.db')


def get_consultation_repository():
    return LocalDBCConsultationRepository('clinic.db')
