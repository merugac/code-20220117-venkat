import json

def read_json_content():
    list_of_row = []
    key = ['Gender','HeightCm','WeightKg']
    list_of_row.append(key)
    with open('Input_Data_for_BMI_Calculator.json','r') as file:
        alllines = json.load(file)
        for row in alllines:
            val = []
            for i, j in row.items():
                val.append(str(j))
            list_of_row.append(val)
     
        return list_of_row

def finaldata_with_bmi(alldata):
    line_count = 0
    notValidData = []
    validData = []
    for row in alldata:
        if line_count == 0:
            line_count = 1
        elif row[0].isalpha() == True and row[1].isnumeric() == True and row[2].isnumeric() == True :
            bmi = calculate_bmi(row)
            validData.append(row+bmi)
            line_count +=1
        else:
            notValidData.append(row)
            line_count +=1
    return validData

class BMI:
    bmi_categoty ={ 'UW' :'Underweight',
                    'NW': 'Normal weight',
                    'OW': 'Overweight',
                    'MO': 'Moderately obese',
                    'SO': 'Severely obese',
                    'VSO': 'Very Severely obese',
                   }

    health_risk = {
                    'MR':'Malnutrition risk',
                    'LR': 'Low risk',
                    'ER': 'Enhanced risk',
                    'MRS': 'Medium risk',
                    'HR': 'High risk',
                    'VHR': 'Very high risk',
                    }

def calculate_bmi(data):
    BMI_categoty= None
    Health_risk= None
    BMI_range = None
    x =int(data[1])
    y = int(data[2])
    bmi = y/((x/100)**2)
    if bmi <= 18.4 :
        BMI_categoty = BMI.bmi_categoty.get('UW')
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('MR')
    elif bmi >=18.5 and bmi <= 24.9:
        BMI_categoty = BMI.bmi_categoty.get('NW')
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('LR')
    elif bmi >=25 and bmi <= 29.9:
        BMI_categoty = BMI.bmi_categoty.get("OW")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('ER')
    elif bmi >=30 and bmi <= 34.9:
        BMI_categoty = BMI.bmi_categoty.get("MO")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('MRS')
    elif bmi >= 35 and bmi <= 39.9:
        BMI_categoty = BMI.bmi_categoty.get("SO")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('HR')
    elif bmi > 40:
        BMI_categoty = BMI.bmi_categoty.get("VSO")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('VHR')
    bmi_list =[BMI_categoty,BMI_range,Health_risk]
    return bmi_list

def write_json(data):
    with open('Output_BMI_Calculator.json', 'w',newline='') as file:
        final_json = []
        
        keys = ['Gender', 'Height', 'Weight', 'BMI_categoty', 'BMI_range', 'Health_risk']
        for values in data:
            json_data = {keys[i]: values[i] for i in range(len(keys))}
            final_json.append(json_data)
        file.write(json.dumps(final_json))
 
    total_overweight = 0
    for key in data:
        if "Overweight" in key:
            total_overweight+=1

    return f'JSON file created successfully.. & Total Number of Overweighted person {total_overweight}'

if __name__ == '__main__':
    contents = read_json_content()
    finaldata = finaldata_with_bmi(contents)
    result = write_json(finaldata)
    print(result)
