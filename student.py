
"student.py"
#library for assignment

# 1. Define class
class Undergraduate:
    # __init___ method runs when a new object is created
    def __init__(self, name, age, major, course1, course2):
        self.name = name #instance attribute
        self.age = age #instance attribute
        self.major = major #instance attribute
        self.course1 = course1 #instance attribute
        self.course2 = course2 #instance attribute

    def __str__(self):
        return f"{self.name} (Age: {self.age}, Major: {self.major}, Courses: {self.course1}, {self.course2})"

    # methods (actions the objects can perform)
    def question(self):
        return f"{self.name} raises their hand!"

    # name comparisons for sorting alphabetically
    def __eq__ (self, other):
        if not isinstance(other, Undergraduate):
            return NotImplemented
        return self.name == other.name
    def __lt__(self, other):
        if not isinstance(other, Undergraduate):
            return NotImplemented
        return self.name < other.name

    def __ge__(self, other):
        if not isinstance(other, Undergraduate):
            return NotImplemented
        return self.name >= other.name

   
    # for sorting by age: 
    def age_eq(self, other):
        if not isinstance(other, Undergraduate):
            return NotImplemented
        return self.age == other.age
    def age_lt(self, other):
        if not isinstance(other, Undergraduate):
            return NotImplemented
        return self.age < other.age 

    def age_gt(self, other):
        if not isinstance(other, Undergraduate):
            return NotImplemented
        return self.age > other.age 


     # Academic comparison method
    def compare_academics(self, other):
        if not isinstance(other, Undergraduate):
            return NotImplemented

        same_major = self.major == other.major
        shared_courses = {self.course1, self.course2} & {other.course1, other.course2}
        has_shared_course = len(shared_courses) > 0
        courses_str = ", ".join(sorted(shared_courses))

        if same_major and not has_shared_course:
            return f"Same major ({self.major}), different courses ({self.course1}/{self.course2} vs {other.course1}/{other.course2})"
        elif has_shared_course and not same_major:
            courses_str = ", ".join(sorted(shared_courses))
            return f"Same course ({courses_str}), different majors ({self.major} vs {other.major})"
        elif same_major and has_shared_course:
            return f"Same major ({self.major}) and same course ({courses_str})"
        return "Different major and different course"



# 2. creates objects under class (name, age, major, course1, course 2)
undergraduate1 = Undergraduate("Bob", 35, "philosophy", "PHIL 101", "MUSC 101")
undergraduate2 = Undergraduate("Carl", 28, "business", "ECON 101", "MATH 101")
undergraduate3 = Undergraduate("Jeff", 22, "mathematics", "ECON 101", "MATH 101")
undergraduate4 = Undergraduate("Dracula", 450, "necromacy", "PHIL 101", "FIT 101")
undergraduate5 = Undergraduate("Smaug", 6273, "economics", "MUSC 101", "MATH 101")
undergraduate6 = Undergraduate("Bella", 22, "music", "PHIL 101", "FIT 101" )
undergraduate7 = Undergraduate("Frank", 35, "music", "MUSC 101", "FIT 101")
undergraduate8 = Undergraduate("Pharaoh", 6273, "necromacy", "ECON 101", "PHIL 101")
undergraduate9 = Undergraduate("Gordy", 28, "physical eduation", "FIT 101", "PHIL 101") 
undergraduate10 = Undergraduate("Stella", 42, "business", "FIT 101", "ECON 101")
undergraduate11 = Undergraduate("Rex", 38, "martial arts", "PHIL 101", "FIT 101")
undergraduate12 = Undergraduate("Emmett", 22, "construction", "MATH 101", "FIT 101")


#main function
def studentBody():
    undergraduates = [
        undergraduate1,
        undergraduate2,
        undergraduate3,
        undergraduate4,
        undergraduate5,
        undergraduate6,
        undergraduate7,
        undergraduate8,
        undergraduate9,
        undergraduate10,
        undergraduate11,
        undergraduate12,
        ]


    for i in range(len(undergraduates) - 1):
        a = undergraduates[i]
        b = undergraduates[i + 1]


        print(f"{a.name} ({a.age}) vs {b.name} ({b.age}):")
        print(f"  == : {a == b} | != : {a != b}")
        print(f"  <  : {a < b} | <= : {a <= b}")
        print(f"  >  : {a > b} | >= : {a >= b}")
        print(f"  Academics: {a.compare_academics(b)}\n")
     



if __name__ == "__main__":
    studentBody()
    print("Same name test (Bob == Bob):", undergraduate1 == Undergraduate("Bob", 20, "art", "ART 101", "MUSC 101")) #ensures that a == b can show up since other undergraduates don't have the same name

