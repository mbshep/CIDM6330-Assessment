class DomainAssessment:
    """ 
        Domain model for assessments
    """

    def __init__(self, id, lab_id, timeframe, man_days, notes, type):
        self.id = id
        self.lab_id = lab_id
        self.timeframe = timeframe
        self.man_days = man_days
        self.notes = notes
        self.type = type

    def __str__(self):
        return f"{self.id}"
