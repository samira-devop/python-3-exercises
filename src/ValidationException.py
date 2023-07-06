class ValidationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# custom class that extends the 'Exception' base class
# takes only 1 paprameter -message 
# line 4 INVOKES the __int__ of the 'Exception' class


raise ValidationException