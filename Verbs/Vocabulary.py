import VF #module containg the verb forms

doing_word = input("Enter a verb of any form: ").lower()            # taking input of verb of any form

verb_found = False      #flag to check if verb is found or not

for verb, forms in VF.verb_forms.items():       #iterating through dictionary
    if any(doing_word == form.lower().split(' - ')[1].lower() for form in forms):   #checking if verb found
        verb_found = True               #flag value changed if verb found 
        print(f"Forms of '{verb.capitalize()}':")   
        for form in forms:
            print(form)

if not verb_found:
    print(f"Error: '{doing_word}' is not found in the dictionary.")             #if not found