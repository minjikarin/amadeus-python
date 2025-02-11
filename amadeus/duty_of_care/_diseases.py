from amadeus.client.decorator import Decorator
from amadeus.duty_of_care.diseases import Covid19AreaReport
from amadeus.duty_of_care.diseases import Covid19Report


class Diseases(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.covid19_area_report = Covid19AreaReport(client)
        self.covid19_report = Covid19Report(client)
