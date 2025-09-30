Number_of_Specialization=20
Max_OF_Number_of_Patients=10
class Patient:
    def __init__(self, name='', age=0,status=0):
        self.name = name
        self.age = age
        self.status = status

class Hospital:

    def __init__(self):
        self.queue_list = [list() for _ in range(Number_of_Specialization + 1)]  # 20 specialization ,x patient

    def add_patient(self, patient = Patient() , specialization=0 ,):
        self.name = patient.name
        self.age = patient.age
        self.specialization = specialization
        self.status = patient.status

        if 0<= specialization <= Number_of_Specialization:
           ret = len(self.queue_list[specialization])
           if len(self.queue_list[specialization]) <= Max_OF_Number_of_Patients :
                self.queue_list[specialization].append(patient)
                self.sort_patients(specialization)
                return True
           else:
               print("Failed to add patient, Full Specialization")
               return False

        else:
            print("Failed to add patient, Wrong specialization value")
            return False



    def sort_patients(self, specialization=0):
        self.specialization = specialization
        self.queue_list[specialization].sort(key=lambda x:x.status,reverse=True)

    def print_patients(self, specialization):
        if not self.queue_list[specialization]:
            print("No patients in specialization {}".format(specialization))
            return False
        print(f"All patients in specialization {specialization}:")
        for patient in self.queue_list[specialization]:
            print(f"Patient {patient.name} status: {patient.status} Age: {patient.age} \n -------- \n")
        return True



    def Get_next_patient(self, specialization):
        if not self.queue_list[specialization]:
            print("No patients in specialization {}".format(specialization))
            return False
        next_p= self.queue_list[specialization].pop(0)
        print(f"Next Patient {next_p.name} status: {next_p.status} Age: {next_p.age} go specialization number {specialization} to \n -------- \n")
        return True
    def remove_patient(self, specialization,name):
       for patient in  self.queue_list[specialization] :
           if patient.name == name:
               self.queue_list[specialization].remove(patient)
               self.sort_patients(specialization)
               return True
       return False


def main():
    hospital = Hospital()
    while True:
        print("1) Add patient")
        print("2) Remove patient")
        print("3) Get next patient")
        print("4) print all patients")
        print("5) Exit")
        while True:
            opt = int(input())
            if opt == 1:
                print("Please Add patient Name")
                name = str(input())
                print("Please Add patient Age")
                age = int(input())
                print("Please Add patient specialization")
                specialization = int(input())
                print("Please Add patient Status ( 0 Normal , 1 Urgent , 2 Super Urgent )")
                status = int(input())
                patient = Patient(name, age, status)
                print(f"Patient {patient.name} Added to Specialization{specialization}" )if hospital.add_patient(patient,specialization) else print(f"Patient {patient.name} NOT Added to Specialization{specialization}" )
                break
            if opt == 2:
                print("Please Enter Patient Name")
                name = str(input())
                print("Please Add patient specialization")
                specialization = int(input())
                print(f"Patient {patient.name} Removed from Specialization{specialization}")  if hospital.remove_patient(specialization=specialization,name=name) else print(f"Patient {patient.name} Not found in Specialization{specialization}" )
                break
            if opt == 3:
                print("Please Add patient specialization")
                specialization = int(input())
                hospital.Get_next_patient(specialization)
                break
            if opt == 4:
                print("Please Add patient specialization")
                specialization = int(input())
                hospital.print_patients(specialization)
                break
            if opt == 5:
                return True




if __name__ == '__main__':
    main()