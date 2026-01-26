from pyscript import display, document #Intrams Checker

def Intrams_checker(e):
    document.getElementById('output1').innerHTML = ''  # Clear previous output

    Registered = document.getElementById('Reg').checked
    Clearance = document.getElementById('Med').checked
    Name =  document.getElementById('Name').value
    Section = document.querySelector('input[name="section"]:checked').value
    Grade = document.querySelector('input[name="grade"]:checked').value

    if Registered and Clearance == True : #Checks for both conditions. If both are true, it proceeds for checking the section
        if Section == "Sapphire": 
            display(f"CONGRATS! {Name} from {Grade}-{Section} is qualified for Intrams. {Name} is playing for the Yellow Tigers", target="output1")
        elif Section == "Ruby": 
            display(f"CONGRATS! {Name} from {Grade}-{Section} is qualified for Intrams. {Name} is playing for the Green Hornets", target="output1")
        elif Section == "Topaz": 
            display(f"CONGRATS! {Name} from {Grade}-{Section} is qualified for Intrams. {Name} is playing for the Red Bulldogs", target="output1")
        elif Section == "Emerald": 
            display(f"CONGRATS! {Name} from {Grade}-{Section} is qualified for Intrams. {Name} is playing for the Blue Bears", target="output1")
    elif Registered == False and Clearance == True : #Provides on condition for ineligibility
        display(f"{Name} from {Grade}-{Section} is not qualified for Intrams. {Name} should register with his advisor.", target="output1")
    elif Registered == True and Clearance == False : #Provides on condition for ineligibility
        display(f"{Name} from {Grade}-{Section} is not qualified for Intrams. {Name} should go to the clinic for medical clearance.", target="output1")
    else: #Last Condition for ineligibility if both conditions are false
        display(f"{Name} from {Grade}-{Section} is not qualified for Intrams. {Name} should register with his advisor and go to the clinic for medical clearance ", target="output1")




    
