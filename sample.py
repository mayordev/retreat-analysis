# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:12:12 2024

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 22:26:23 2023

@author: user
"""
import pandas as pd

cycle = 0

# Functions to correct and validate phone numbers

def formatNigeriaPhoneNumber(phone_number):
    # Convert phone_number to string for consistent processing
    phone_str = str(phone_number)

    # Case 1: If the phone number starts with '234' and is 13 digits, add '+'
    if phone_str.startswith('234') and len(phone_str) == 13:
        return '+' + phone_str

    # Case 2: If the phone number starts without '0' and is 10 digits, add '+234'
    elif not phone_str.startswith('0') and len(phone_str) == 10:
        return '+234' + phone_str

    # Case 3: If the phone number is 11 digits and starts with '0', format it as +234
    elif len(phone_str) == 11 and phone_str.startswith('0'):
        return '+234' + phone_str[1:]

    # Case 4: If the phone number is 14 digits and starts with '+234', leave it as is
    elif len(phone_str) == 14 and phone_str.startswith('+234'):
        return phone_str

    # Case 5: Invalid phone number format
    else:
        return 'Invalid phone number'

# Functions to correct the phone numbers in a list
def correctListNum(lst):
    return [formatNigeriaPhoneNumber(num) for num in lst]

# Import the file to be analyzed
data = pd.read_csv("DLCF_DELTA-NORTH_EASTER_RETRERAT_2024_REG_FORM.csv" , sep=";")


# Remove the unneeded columns in the data
data = data.drop(["start", "end", "_id", "_uuid", "_submission_time", "_validation_status", "_index", "_tags", "_status", "_submitted_by", "_notes"], axis=1)

# Check for any duplicate data
data = data.drop_duplicates(keep='first')

# Convert surnames and first names to uppercase
data['SURNAME'] = data['SURNAME'].str.upper()
data['FIRST NAME'] = data['FIRST NAME'].str.upper()

# Correct and validate the phone number column
if cycle == 0:
    data['WhatsApp NUMBER'] = correctListNum(data['WhatsApp NUMBER'])
    cycle = 1
    data.to_csv("new_dlcf_deltanorth_easter_retreat_2024_reg.csv", index=False)
else:
    pass

data.head(20)



# Check total number of male that registered
maleData = data[data.SEX == "MALE"]
maleCount = len(maleData)  #len for direct count

# Check total number of female that registered
femaleData = data[data.SEX == "FEMALE"]
femaleCount = len(femaleData)  #len for direct count

# Check total number that registered
totalCount = len(data)  #len for direct count

# Check total number of workers that registered
workersData = data[data["MEMBERSHIP STATUS"] == "WORKER"]
workersCount = len(workersData)  # Use len for direct count
    
# print out the values
print("TOTAL REGISTRATION RESULT")
print("NO OF MALES = " + str(maleCount))
print("NO OF FEMALES = " + str(femaleCount))
print("TOATAL RESULT = " + str(totalCount))
print("TOTAL NUMBER OF WORKERS = ", str( workersCount) + '\n')


# Filter registrations for the first day
firstDayData = data[data["REGISTRATION DATE"] == "THUR. 28/03/2024"]

# Count registrations by category on the first day
femaleCountDay1 = len(firstDayData[firstDayData.SEX == "FEMALE"])
maleCountDay1 = len(firstDayData[firstDayData.SEX == "MALE"])
totalCountDay1 = len(firstDayData)
workerCountDay1 = len(firstDayData[firstDayData["MEMBERSHIP STATUS"] == "WORKER"])

# Print registration results for the first day
print("THUR. 28/03/2024 REGISTRATION RESULT")
print("NO OF MALES = ", maleCountDay1)
print("NO OF FEMALES = ", femaleCountDay1)
print("NO OF WORKERS = ", workerCountDay1)
print("TOTAL REGISTRATIONS = ", totalCountDay1, "\n")


# Filter registrations for the second day
firstDayData = data[data["REGISTRATION DATE"] == "FRI. 29/03/2024"]

# Count registrations by category on the second day
femaleCountDay2 = len(firstDayData[firstDayData.SEX == "FEMALE"])
maleCountDay2 = len(firstDayData[firstDayData.SEX == "MALE"])
totalCountDay2 = len(firstDayData)
workerCountDay2 = len(firstDayData[firstDayData["MEMBERSHIP STATUS"] == "WORKER"])

# Print registration results for the first day
print("FRI. 29/03/2024 REGISTRATION RESULT")
print("NO OF MALES = ", maleCountDay2)
print("NO OF FEMALES = ", femaleCountDay2)
print("NO OF WORKERS = ", workerCountDay2)
print("TOTAL REGISTRATIONS = ", totalCountDay2, "\n")



# Filter registrations for the third day
firstDayData = data[data["REGISTRATION DATE"] == "SAT. 30/03/2024"]

# Count registrations by category on the third day
femaleCountDay3 = len(firstDayData[firstDayData.SEX == "FEMALE"])
maleCountDay3 = len(firstDayData[firstDayData.SEX == "MALE"])
totalCountDay3 = len(firstDayData)
workerCountDay3 = len(firstDayData[firstDayData["MEMBERSHIP STATUS"] == "WORKER"])

# Print registration results for the third day
print("SAT. 30/03/2024 REGISTRATION RESULT")
print("NO OF MALES = ", maleCountDay3)
print("NO OF FEMALES = ", femaleCountDay3)
print("NO OF WORKERS = ", workerCountDay3)
print("TOTAL REGISTRATIONS = ", totalCountDay3, "\n")




# Filter registrations for the fourth day
firstDayData = data[data["REGISTRATION DATE"] == "SUN. 31/03/2024"]

# Count registrations by category on the fourth day
femaleCountDay4 = len(firstDayData[firstDayData.SEX == "FEMALE"])
maleCountDay4 = len(firstDayData[firstDayData.SEX == "MALE"])
totalCountDay4 = len(firstDayData)
workerCountDay4 = len(firstDayData[firstDayData["MEMBERSHIP STATUS"] == "WORKER"])

# Print registration results for the fourth day
print("SUN. 30/03/2024 REGISTRATION RESULT")
print("NO OF MALES = ", maleCountDay4)
print("NO OF FEMALES = ", femaleCountDay4)
print("NO OF WORKERS = ", workerCountDay4)
print("TOTAL REGISTRATIONS = ", totalCountDay4, "\n")





# Filter registrations for the fifth day
firstDayData = data[data["REGISTRATION DATE"] == "MON. 01/04/2024"]

# Count registrations by category on the fifth day
femaleCountDay5 = len(firstDayData[firstDayData.SEX == "FEMALE"])
maleCountDay5 = len(firstDayData[firstDayData.SEX == "MALE"])
totalCountDay5 = len(firstDayData)
workerCountDay5 = len(firstDayData[firstDayData["MEMBERSHIP STATUS"] == "WORKER"])

# Print registration results for the fifth day
print("MON. 01/04/2024 REGISTRATION RESULT")
print("NO OF MALES = ", maleCountDay5)
print("NO OF FEMALES = ", femaleCountDay5)
print("NO OF WORKERS = ", workerCountDay5)
print("TOTAL REGISTRATIONS = ", totalCountDay5, "\n")


# Filter registrations for the sixth day
firstDayData = data[data["REGISTRATION DATE"] == "TUE. 02/04/2024"]

# Count registrations by category on the fourth day
femaleCountDay6 = len(firstDayData[firstDayData.SEX == "FEMALE"])
maleCountDay6 = len(firstDayData[firstDayData.SEX == "MALE"])
totalCountDay6 = len(firstDayData)
workerCountDay6 = len(firstDayData[firstDayData["MEMBERSHIP STATUS"] == "WORKER"])

# Print registration results for the fourth day
print("TUE. 02/04/2024 REGISTRATION RESULT")
print("NO OF MALES = ", maleCountDay6)
print("NO OF FEMALES = ", femaleCountDay6)
print("NO OF WORKERS = ", workerCountDay6)
print("TOTAL REGISTRATIONS = ", totalCountDay6, "\n")





# convert the result to tabular form
tableData = {'DAYS' : ['THUR', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'ALL DAYS'],
             'MALE' : [maleCountDay1, maleCountDay2, maleCountDay3, maleCountDay4, maleCountDay5, maleCountDay6, maleCount],
             'FEMALE' : [femaleCountDay1, femaleCountDay2, femaleCountDay3, femaleCountDay4, femaleCountDay5, femaleCountDay6, femaleCount],
             'TOTAL' : [totalCountDay1, totalCountDay2, totalCountDay3, totalCountDay4, totalCountDay5, totalCountDay5, totalCount]
            }

table = pd.DataFrame(tableData, columns = ['DAYS', 'MALE', 'FEMALE', 'TOTAL'])

print("summary of the general campus registration\n")
print(table, '\n')

#print total number of workers
workersCount = list(data["MEMBERSHIP STATUS"]).count('WORKER')
print("TOTAL NUMBER OF WORKERS = ", str( workersCount) + '\n') 





#DLCF DOU
douData = data[data["FELLOWSHIP LOCATION"] == "DLCF DOU"]
douCount = len(douData)  # Use len for direct count
print("TOTAL NUMBER OF REGISTERED PARTICIPANTS FROM DLCF DOU = ", douCount, "\n")


#DEEPER LIFE CORPERS' FELLOWSHIP
dlcfData = data[data["FELLOWSHIP LOCATION"] == "DEEPER LIFE CORPERS' FELLOWSHIP ASABA"]
dlcfCount = len(dlcfData)  # Use len for direct count
print("TOTAL NUMBER OF REGISTERED PARTICIPANTS FROM CORPERS FELLOWSHIP = ", dlcfCount, "\n")


#DLCF FCE
fceData = data[data["FELLOWSHIP LOCATION"] == "DLCF FCE PERMANENT SITE"]
fceCount = len(fceData)  # Use len for direct count
print("TOTAL NUMBER OF REGISTERED PARTICIPANTS FROM DLCF FCE PERMANENT SITE  = ", fceCount, "\n")


#DLCF JUNIC
junicData = data[data["FELLOWSHIP LOCATION"] == "DLCF JUNIC"]
junicCount = len(junicData)  # Use len for direct count
print("TOTAL NUMBER OF REGISTERED PARTICIPANTS FROM DLCF JUNIC = ", junicCount, "\n")


#DLCF PARADISE
paradiseData = data[data["FELLOWSHIP LOCATION"] == "DLCF PARADISE"]
paradiseCount = len(paradiseData)  # Use len for direct count
print("TOTAL NUMBER OF REGISTERED PARTICIPANTS FROM DLCF PARADISE = ", paradiseCount, "\n")


#OTHER INSTITUTIONS
othersData = data[data["FELLOWSHIP LOCATION"] == "OTHERS"]
othersCount = len(othersData)  # Use len for direct count
print("TOTAL NUMBER OF REGISTERED PARTICIPANTS FROM OTHER FELLOWSHIPS = ", othersCount, "\n")



# check if a particiant has registered / is present in the "Name" column
surname_to_check = 'ADSINA'
name_to_check = 'MAYOWA'
is_name_present = surname_to_check in data['SURNAME'].values and name_to_check in data['FIRST NAME'].values 
# print the result
print("HAS MAYOWA REGISTERED?")
print(str(is_name_present)  + '\n')

'''
#Code to check for the nuber of registered females and males from all locations except Other locactions outside Asaba for each day
'''
# List of fellowship locations 
fellowship_locations = ["DLCF DOU", "DEEPER LIFE CORPERS' FELLOWSHIP ASABA", 
                         "DLCF FCE PERMANENT SITE", "DLCF JUNIC", "DLCF PARADISE"]

total_female_count = 0  # Initialize a variable to store the total count
# Loop through each fellowship location
for location in fellowship_locations:
  # Filter data for Tuesday registrations and specific fellowship location
  filtered_data = data[(data["REGISTRATION DATE"] == "FRI. 29/03/2024") & 
                        (data["FELLOWSHIP LOCATION"] == location)]

  # Count females from that location
  female_count = len(filtered_data[filtered_data.SEX == "FEMALE"])

  # Print the result (modify formatting as needed)
  print(f"Number of females from {location} who registered on Friday (29/03/2024): {female_count}")
    
     # Accumulate the female count for the total
  total_female_count += female_count

# Print the total count
print(f"Total number of females registered on Friday (29/03/2024) across all fellowships: {total_female_count}\n")



# List of fellowship locations 
fellowship_locations = ["DLCF DOU", "DEEPER LIFE CORPERS' FELLOWSHIP ASABA", 
                         "DLCF FCE PERMANENT SITE", "DLCF JUNIC", "DLCF PARADISE"]

total_male_count = 0  # Initialize a variable to store the total count


# Loop through each fellowship location
for location in fellowship_locations:
  # Filter data for Tuesday registrations and specific fellowship location
  filtered_data = data[(data["REGISTRATION DATE"] == "FRI. 29/03/2024") & 
                        (data["FELLOWSHIP LOCATION"] == location)]

  # Count males from that location
  male_count = len(filtered_data[filtered_data.SEX == "MALE"])

  # Print the result (modify formatting as needed)
  print(f"Number of males from {location} who registered on Friday (29/03/2024): {male_count}")
    
     # Accumulate the female count for the total
  total_male_count += male_count

# Print the total count
print(f"Total number of males registered on Friday (29/03/2024) across all fellowships: {total_male_count}\n")


'''
#Code to check for the nuber of registered females and males from all other locations outside Asaba for each day.
'''
fridayData = data[data["REGISTRATION DATE"] == "FRI. 29/03/2024"]
femaleCountFriday = len(fridayData[fridayData.SEX == "FEMALE"])
othersCountFriday = len(fridayData[
    (fridayData.SEX == "FEMALE") & (fridayData["FELLOWSHIP LOCATION"] == "OTHERS")
])

# Print the result
print(f"Number of females from outside Campuses who registered on Friday (29/03/2024): {othersCountFriday}\n")


fridayData = data[data["REGISTRATION DATE"] == "FRI. 29/03/2024"]
maleCountFriday = len(fridayData[fridayData.SEX == "MALE"])
othersCountFriday = len(fridayData[
    (fridayData.SEX == "MALE") & (fridayData["FELLOWSHIP LOCATION"] == "OTHERS")
])

# Print the result
print(f"Number of males from outside Campuses who registered on Friday (29/03/2024): {othersCountFriday}\n")
