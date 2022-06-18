from unittest import case

class CalcIMC:
    def __init__(self, name, age, height, weight, biologicalSex):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.biologicalSex = biologicalSex
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_biologicalSex(self):
        return self.biologicalSex

    def imc(self):
        return round(self.get_weight() / (self.get_height() ** 2),2)

    def case_imc_m(self):
        imc = self.imc()
        age = self.get_age()
        if age == 1:
            if imc >= 19.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 18.2:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade.")
            elif imc >= 14.5:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 2:
            if imc >= 18.7:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 17.4:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 14:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 3:
            if imc >= 18.2:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 17:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13.4:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 4:
            if imc >= 18:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 16.7:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13.2:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 5:
            if imc >= 18.1:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 16.7:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 6:
            if imc >= 18.4:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 16.9:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13.2:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 7:
            if imc >= 18.7:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 17.2:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13.3:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 8:
            if imc >= 19.4:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 17.5:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13.5:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 9:
            if imc >= 20.1:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 18:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 10:
            if imc >= 28.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 25:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 17.5:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 11:
            if imc >= 22:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 19.3:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 14.2:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 12:
            if imc >= 23:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 20:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 14.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 13:
            if imc >= 24.2:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 21:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 15:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 14:
            if imc >= 25.3:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 21.9:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 15.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 15:
            if imc >= 26.4:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 22.8:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 16.2:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 16:
            if imc >= 27.3:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 23.7:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 16.7:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 17:
            if imc >= 28:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 24.5:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 17.2:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 18:
            if imc >= 28.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 25:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 17.5:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age >= 19:
            if imc >= 30:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 25:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 18.5:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

    def case_imc_f(self):    
        imc = self.imc()
        age = self.get_age()
        if age == 1:
            if imc >= 19.4:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 17.9:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13.9:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 2:
            if imc >= 18.5:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 17.2:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13.5:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 3:
            if imc >= 18.2:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 16.8:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13.2:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 4:
            if imc >= 18.3:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 16.8:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 5:
            if imc >= 18.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 17:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 12.8:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 6:
            if imc >= 18.9:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 17.1:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 12.8:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 7:
            if imc >= 19.5:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 17.4:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 12.9:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 8:
            if imc >= 20.1:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 17.8:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 9:
            if imc >= 21:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 18.5:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13.3:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 10:
            if imc >= 22:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 19.1:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 13.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 11:
            if imc >= 23.2:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 20:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 14:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 12:
            if imc >= 24.4:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 20.9:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 14.5:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 13:
            if imc >= 25.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 22:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 15.1:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 14:
            if imc >= 26.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 22.9:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 15.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 15:
            if imc >= 27.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 23.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 16.1:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 16:
            if imc >= 28.3:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 24.3:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 16.4:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 17:
            if imc >= 28.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 24.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 16.6:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                print(self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age == 18:
            if imc >= 28.9:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 24.9:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 16.7:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

        if age >= 19:
            if imc >= 30:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are obese I.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com obsidade I.")
            elif imc >= 24.9:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are pre-obese.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com pré obsidade..")
            elif imc >= 18.5:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are of normal weight.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com peso normal.")
            else:
                return (self.get_name() + " your BMI is " + str(imc) + ", in other words, you are too thin.\n\t" + self.get_name() + " o seu IMC é " + str(imc) + ", ou seja, você está com magreza.")

    def BSex(self):
        if self.get_biologicalSex() == "M":
            return self.case_imc_m()
        elif self.get_biologicalSex() == "F":
            return self.case_imc_f()

    def get_resultIMC(self):
        return self.BSex()
