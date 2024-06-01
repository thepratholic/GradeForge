print("Welcome to GradeForge!!\n")


class grade_sheet:

    def calculate_marks(self):
        specialization = input("What are you doing, DE(Diploma in engineering)/BE(Bachelors of Engineering) : ")

        if specialization == "DE" or "Diploma in Engineering":

            first_sem = float(input("Enter spi of first sem : "))

            second_sem = float(input("Enter spi of second sem : "))
            
            third_sem = float(input("Enter spi of third sem : "))
            
            fourth_sem = float(input("Enter spi of fourth sem : "))
            
            fifth_sem = float(input("Enter spi of fifth sem : "))
            
            sixth_sem = float(input("Enter spi of sixth sem : "))

            
            diploma_spi = first_sem + second_sem + third_sem + fourth_sem + fifth_sem + sixth_sem
            
            diploma_cpi = (first_sem + second_sem + third_sem + fourth_sem + fifth_sem + sixth_sem) / 6
            
            diploma_cgpa = (third_sem + fourth_sem + fifth_sem + sixth_sem) / 4

            
            print(f"Your total SPI of all semesters in Engineering is : {diploma_spi}")
            
            print(f"Your CPI in Diploma Engineering is : {diploma_cpi}")
            
            print(f"Your CGPA in Diploma Engineering is : {diploma_cgpa}")

        else:

            
            first_sem = float(input("Enter spi of first sem : "))
            
            second_sem = float(input("Enter spi of second sem : "))
            
            third_sem = float(input("Enter spi of third sem : "))
            
            fourth_sem = float(input("Enter spi of fourth sem : "))
            
            fifth_sem = float(input("Enter spi of fifth sem : "))
            
            sixth_sem = float(input("Enter spi of sixth sem : "))
            
            seventh_sem = float(input("Enter spi of seventh sem : "))
            
            eighth_sem = float(input("Enter spi of eighth sem : "))

            
            degree_spi = first_sem + second_sem + third_sem + fourth_sem + fifth_sem + sixth_sem + seventh_sem + eighth_sem
            
            degree_cpi = (first_sem + second_sem + third_sem + fourth_sem + fifth_sem + sixth_sem + seventh_sem + eighth_sem) / 8
            
            degree_cgpa = (third_sem + fourth_sem + fifth_sem + sixth_sem) / 4

            
            print(f"Your total SPI of all semesters in Engineering is : {degree_spi}")
            
            print(f"Your CPI in Diploma Engineering is : {degree_cpi}")
            
            print(f"Your CGPA in Diploma Engineering is : {degree_cgpa}")

        if diploma_cgpa or degree_cgpa >= 5.5:
            
            print("Congratulations, you are eligible to collect your Engineering degree!!!")
        
        else:
            
            print("Sorry, You need to pass all the pending subject exams to collect your Engineering degree!!")


gs = grade_sheet()

if __name__ == "__main__":

    gs.calculate_marks()