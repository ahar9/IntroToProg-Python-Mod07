# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Alexis Harris, 3/12/2025, Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.



# Data --------------------------------------- #
# TODO Create a Person Class (DONE)
class Person:
    """
    A collection of data and methods for a Person

    Properties:
        first_name (str): The Person's first name.
        last_name (str): The Person's last name.

    ChangeLog: (Who, When, What)
    Alexis Harris, 3.12.2025, created class
    """
    # TODO Add first_name and last_name properties to the constructor (DONE)
    def __init__(self, first_name:str = '', last_name:str = ''):
        """
        This function initializes first name and last name attributes to
        a Person class
        :param first_name:
        :param last_name:
        """
        self.first_name = first_name
        self.last_name = last_name

    # TODO Create a getter and setter for the first_name property (DONE)
    @property  # (Use this decorator for the getter or accessor)
    def first_name(self):
        """
        Returns first name attribute formatted with title
        :return:
        """
        return self.__first_name.title()  # formatting code

    @first_name.setter
    def first_name(self, value: str):
        """
        Sets first name attribute. Checks value to be alpha.
        :param value:
        :return:
        """
        if value.isalpha() or value == "":  # is character or empty string
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")


    # TODO Create a getter and setter for the last_name property (DONE)
    @property
    def last_name(self):
        """
        Returns last name attribute formatted with title
        :return:
        """
        return self.__last_name.title()  # formatting code

    @last_name.setter
    def last_name(self, value: str):
        """
        Sets last name attribute. Checks value to be alpha.
        :param value:
        :return:
        """
        if value.isalpha() or value == "":  # is character or empty string
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    # TODO Override the __str__() method to return Person data (DONE)
    def __str__(self):
        """
        String returning first name and last name of Person
        :return:
        """
        return f'{self.first_name},{self.last_name}'

# TODO Create a Student class the inherits from the Person class
class Student(Person):
    """
    A collection of data for a student

    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        course_name (str): The title of the course for the student.

    ChangeLog: (Who, When, What)
    Alexis Harris, 3.12.2025, created class
    """

    def __init__(self, first_name:str='', last_name:str = '', course_name:str = ''):
        """
        This function initializes student first name, student last name, and course
        name attributes to a Student class

        :param first_name:
        :param last_name:
        :param course_name:
        """
        # TODO call to the Person constructor and pass it the first_name and last_name data (DONE)
        super().__init__(first_name=first_name, last_name=last_name)
        # TODO add a assignment to the course_name property using the course_name parameter (DONE)
        self.course_name = course_name

    # TODO add the getter for course_name (DONE)
    @property
    def course_name(self):
        """
        Returns course name attribute formatted with title
        :return:
        """
        return self.__course_name.title()  # formatting code

    # TODO add the setter for course_name (DONE)
    @course_name.setter
    def course_name(self, value: str):
        """
        Sets last name attribute. Checks value to be alpha.
        :param value:
        :return:
        """
        self.__course_name = value

    # TODO Override the __str__() method to return the Student data (DONE)
    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.course_name}'



# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    Alexis Harris, 3.15.2025, Edits
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows
        then returns the list filled with student data.

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param file_name: string data with name of file to read from

        :return: list
        """

        try:
            # Get a list of dictionary rows from the data file
            file = open(file_name, "r")
            json_students = json.load(file)

            # Convert the list of dictionary rows into a list of Student objects
            # TODO replace this line of code to convert dictionary data to Student data (DONE)
            #student_objects = json_students
            for row in json_students:
                student_obj = Student(first_name=row["FirstName"],
                                      last_name=row["LastName"],
                                      course_name=row["CourseName"])
                student_data.append(student_obj)
            file.close()

        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()

        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        try:
            # TODO Add code to convert Student objects into dictionaries (Done)
            json_students = []
            for student in student_data:
                student_dict = {"FirstName":student.first_name,
                                "LastName":student.last_name,
                                "CourseName": student.course_name}
                json_students.append(student_dict)

            file = open(file_name, "w")
            json.dump(json_students, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:

            # TODO Add code to access Student object data instead of dictionary data (DONE)
            print(f'Student {student.first_name} '
                  f'{student.last_name} is enrolled in {student.course_name}')

        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            # Input the data
            # TODO Replace this code to use a Student objects instead of a dictionary objects (DONE)
            student = Student()
            student.first_name = input("Enter the student's first name: ")
            student.last_name = input("Enter the student's last name: ")
            student.course_name = input("Please enter the name of the course: ")
            student_data.append(student)

            print()
            print(f"You have registered {student.first_name} {student.last_name} for {student.course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
