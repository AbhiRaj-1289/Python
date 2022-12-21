data = {'Name' : {0 : 'Abhinav', 1 :'Priyam', 2 :'Bhoomi', 3: 'Nikhil', 4 : 'Raj'}, 'ID' : { 0 : '205031', 1: '205014', 2 : '205004', 3 : '205020', 4 :'205000'}, 'Address' : { 0 :'Marwan', 1 : 'Samastipur', 2 : 'Muzaffarpur', 3 : 'Muzaffarpur', 4 : 'Patna'}, 'Salary' : { 0 : '12000', 1 : '12500', 2 : '1000', 3 : '11000', 4 : '9000'}}
id_value = input("Enter ID : ")
for key, value in data['ID'].items():
    if value == id_value:
        print("Name = ",data['Name'][key])
        print("Address = ",data['Address'][key])
        print("Salary = ",data['Salary'][key])
        break
else:
    print("ID Not Present in Databse")