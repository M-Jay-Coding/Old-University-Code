
class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        self.first_name = first_name
        self.surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        #ToDo1
        pass
        self.__doctor = 'Not-assigned'
       

    
    def full_name(self) :
        
        """full name is first_name and surname"""
        return (f'{self.first_name},{self.surname}')


    def get_doctor(self) :
        return self.__doctor
    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        print("Your Symptoms: ")
        print("Nausea ")
        print("Coughing ")
        print("Watery eyes ")
 
    def __str__(self):
        return f'{self.full_name()}|{self.__doctor}|{self.__age}|{self.__mobile}|{self.__postcode}'
