#Author: S.A.S.D.Senanayake
#Date: 22.12.2024
#IIT Student ID: 20240476
#UOW ID: w2119872

import csv
from collections import Counter
import tkinter as tk

# Task A: Input Validation

def validate_date_input(d_m_y,minValue,maxValue,dateFormat): #creating a function to get the day, month and year in the correct format.
    while True:   # it will loop until it returns a correct value
        try:
            date = str(input(f"Please enter the {d_m_y} of the survey in the format {dateFormat} : "))
            if minValue<= int(date) <=maxValue: #if you enter a string value in this step it will raise an error message (ValueError: invalid literal for int())
                return date #the date will be returned and will automatically break the while loop
            else:
                print (f'Out of range - values must be in the range of {minValue} to {maxValue}')
        except ValueError: #handling the value error
            print ('Integer required!!')
            
def validate_continue_input(): #creating a function to prompt the user to decide whether to load another data set
    while True:
        print("**************************************")
        loop = input("Do you want to select another data file for a different date? (Y/N) : ").strip().upper() #getting the input in uppercase
        if loop == "Y":
            print("**************************************")
            return True
        elif loop == "N":
            print("End of the program.")
            return False 
        else:
            print('Please Enter "Y" or "N"')


# Task B: Processed Outcomes
def process_csv_data(file_path): #creating a function to extract data from csv file and process 
    try:
        with open (file_path, newline='') as csvfile: #opening the selected file. the with statement automatically closes the file after using it.
            readcsv= csv.reader (csvfile) # reading the file
            next (readcsv) #to skip the first row  
            tot_vehicles=0 #initializing variables to 0
            tot_trucks = 0
            tot_e_vehi = 0
            tot_2wheeled_vehi=0
            tot_bus_elm_north=0
            tot_vehi_straight=0
            no_of_bicycles=0
            speedy_vehi = 0
            elm_vehi = 0
            hanley_vehi = 0
            elm_scoot = 0
            hour_list = []
            rainy_hours = []
            tot_rainy_hours = 0
            
            for row in readcsv:
                #The total number of vehicles passing through all junctions for the selected date.
                tot_vehicles += 1
                #The total number of trucks passing through all junctions for the selected date. 
                if row[8] == "Truck":
                    tot_trucks += 1
                #The total number of electric vehicles passing through all junctions for the selected date. 
                if row[9] == "True":
                    tot_e_vehi += 1
                #The number of “two wheeled” vehicles through all junctions for the date (bikes, motorbike, scooters)
                if row[8] == "Bicycle" or row[8] =="Scooter" or row[8] =="Motorcycle":
                    tot_2wheeled_vehi += 1
                #The total number of busses leaving Elm Avenue/Rabbit Road junction heading north 
                if row[0]=='Elm Avenue/Rabbit Road' and row[4]=='N' and row[8]=="Buss" :
                    tot_bus_elm_north += 1
                #The total number of vehicles passing through both junctions without turning left or right
                if row[3]==row[4]:
                    tot_vehi_straight += 1 
                #The percentage of all vehicles recorded that are Trucks for the selected date (rounded to an integer)
                truck_percent = format(((tot_trucks/tot_vehicles)*100), '.0f')
                #The average number Bicycles per hour for the selected date (rounded to an integer)
                if row[8] =="Bicycle":
                    no_of_bicycles += 1
                avg_bicycle = format(((no_of_bicycles)/24), '.0f') # formatting the intiger value to zero decimal places
                    
                #The total number of vehicles recorded as over the speed limit for the selected date
                if int(row[6]) < int(row[7]):   
                    speedy_vehi += 1  
                #The total number of vehicles recorded through only Elm Avenue/Rabbit Road junction for the selected date    
                if row[0] =="Elm Avenue/Rabbit Road":
                    elm_vehi += 1
                #The total number of vehicles recorded through only Hanley Highway/Westway junction for the selected date
                if row[0] =="Hanley Highway/Westway":
                    hanley_vehi += 1
                #The percentage of vehicles through Elm Avenue/Rabbit Road that are Scooters (rounded to integer)
                if row[0] =="Elm Avenue/Rabbit Road" and row[8] == "Scooter":
                    elm_scoot +=1
                scoot_percentage = int((elm_scoot/elm_vehi)*100)
                   
                #The number of vehicles recorded in the peak (busiest) hour on Hanley Highway/Westway
                if row[0] == "Hanley Highway/Westway":
                    hours = (row[2])[0:2] #getting the first 2 digits from the timeOfDay column in excel sheet to get the hours
                    hour_list.append(hours) #appending the hours to the hour_list
                    counted_dict = Counter(hour_list) #making counted dictionary by using Counter
                    #so an item of this dictionary will look like this {hour:no of time it is repeated}
                    peak_hour, vehicle_count = counted_dict.most_common(1)[0] #the vehicle_count equals to the count of the most common hour(count of peak_hour)
                    # mostcommon(1) will give the most common elements as a list of tuples 
                    # and the [0] will result the first tuple resulted by mostcommon(1) - (peak_hour, count of peak_hour)
                    
                #The total number of hours of rain on the selected date    
                if 'rain' in row[5].lower(): #converting the values in the Weather_Conditions column into lowercase and searching if there is substring 'rain', using the in keyword
                    rhour = (row[2])[0:2] 
                    rainy_hours.append(rhour)
                    r_hour = set(rainy_hours) #converting the rainy_hours list into a set named r_hour to remove the duplicated hours.
                    tot_rainy_hours = len(r_hour)
                    
            # creating a list of outcomes using the processed data            
            list_of_outcomes = [("**************************************"),\
                                (f"Data file selected is {file_path}"),\
                                ("**************************************"),\
                                (f"The total number of vehicles recorded for this date is : {tot_vehicles}"),\
                                (f"The total number of trucks recorded for this date is : {tot_trucks}"),\
                                (f"The total number of electric vehicles for this date is : {tot_e_vehi}"),\
                                (f"The total number of two-wheeled vehicles for this date is : {tot_2wheeled_vehi}"),\
                                (f"The total number of busses leaving Elm Avenue/Rabbit Road heading north is : {tot_bus_elm_north}"),\
                                (f"The total number of vehicles passing through both junctions without turning left or right is : {tot_vehi_straight}"),\
                                (f"The percentage of total vehicles recorded that are trucks for this date is : {truck_percent}%"),\
                                (f"The average number of bikes per hour for this date is : {avg_bicycle}"),\
                                (f"The total number of vehicles recorded as over the speed limit for this date is : {speedy_vehi}"),\
                                (f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is : {elm_vehi}"),\
                                (f"The total number of vehicles recorded through Hanley Highway/Westway junction is : {hanley_vehi}"),\
                                (f"{scoot_percentage}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters."),\
                                (f"The highest number of vehicles in an hour on Hanley Highway/Westway is : {vehicle_count}"),\
                                (f"The most vehicles through Hanley Highway/Westway were recorded between {peak_hour}:00 and {(int(peak_hour)+1):02d}:00"),\
                                #:02d ensures the resulting number is displayed as a two-digit integer, padding with a leading zero if needed.
                                (f"The number of hours of rain for this date is : {tot_rainy_hours}"),\
                                ("")]
            return list_of_outcomes
                
    except FileNotFoundError:
        return [] #then it will return [] to the display_outcomes() and save_results_to_file() functions as 'outcomes' 
            
                
def display_outcomes(file_name): #creating a function to display the outcomes on the screen
    outcomes = process_csv_data(file_name) #calling this function to get the 'list_of_outcomes' as 'outcomes'
    if len(outcomes) == 0:  #if the file is not found it will return an empty list as the 'outcomes' so the length would be 0
        print(f"{file_name} File Not Found!\nPlease enter the data again.\n")
    else:
        for item in outcomes:
            print(item)


# Task C: Save Results to Text File
def save_results_to_file(file_name):  #creating a function to save the results in a txt file  
    outcomes = process_csv_data(file_name)
    with open("results.txt","a") as txtfile: # we use 'a' to append the data to the file
        for item in outcomes:
            txtfile.write (item+ "\n") #by using \n we can write the items line by line in the txt file




# Task D: Histogram Display
class HistogramApp:
    def __init__(self, traffic_data, date):  #Initializes the histogram application with the traffic data and selected date.
        self.traffic_data = traffic_data
        self.date = date
        self.root = tk.Tk()
        self.canvas = None  # Will hold the canvas for drawing
        
    def setup_window(self):  # Sets up the Tkinter window and canvas for the histogram.  
        #settingup the window
        self.root.title("Histogram")
        self.root.geometry("1200x600")
        #settingup the canvas
        self.canvas = tk.Canvas(self.root, width=1200, height=600, bg="white")
        self.canvas.pack()    # here "pack()" method is used to place this canvas in the window and make it visible
       
    def draw_histogram(self):  # Draws the histogram with axes, labels, and bars.  Drawing logic goes here
        margin = 100
        canvas_width = 1200
        canvas_height = 600
        bar_width = 15
        
        category_spacing = (canvas_width-2*margin)/len(self.traffic_data)
        max_height = canvas_height - 2*margin
        max_value = max(max(x) for x in self.traffic_data.values())
        
        for i, (label,values) in enumerate(self.traffic_data.items()):
            x_start = margin + i*category_spacing
            
            bar1_x1 = x_start
            bar1_x2 = bar1_x1 + bar_width
            
            bar2_x1 = bar1_x2
            bar2_x2 = bar2_x1 + bar_width
            
            bar1_height = (values[0]/max_value)*max_height
            bar1_y1 = canvas_height - margin/2 - bar1_height
            
            bar2_height = (values[1]/max_value)*max_height
            bar2_y1 = canvas_height - margin/2 - bar2_height
            
            y2 = canvas_height - margin/2
                        
            # creating bar 1
            self.canvas.create_rectangle(bar1_x1 , bar1_y1 , bar1_x2 , y2 , fill = 'SteelBlue1')
            self.canvas.create_text(bar1_x1 + bar_width/2 , bar1_y1 - 6 , text = str(values[0]), font=("Helvetica", 8, "bold"), fill = 'SteelBlue1') # this will display the value(no of vehicles) above the bar
            
            # creating bar 2
            self.canvas.create_rectangle(bar2_x1 , bar2_y1 , bar2_x2 , y2 , fill = 'pale violet red')
            self.canvas.create_text(bar2_x1 + bar_width/2 , bar2_y1 - 6 , text = str(values[1]), font=("Helvetica", 8, "bold"), fill = 'pale violet red')
            
            # naming/labeling the bars
            self.canvas.create_text((bar1_x1 + bar2_x2)/2 , y2 + 8 , text = label , font=("Helvetica", 8))
            
        # drawing the x axis
        self.canvas.create_line(margin, y2 , canvas_width - margin - category_spacing , y2)
        
        # Add title and X-axis label
        self.canvas.create_text(margin, margin/2 , text=f"Histogram of Vehicle Frequency per Hour ({self.date})", font=("Helvetica", 15, "bold"), anchor="w")
        self.canvas.create_text(canvas_width/2, canvas_height - margin/5, text="Hours 00:00 to 24:00", font=("Helvetica", 10, "bold"), fill="#474747")
                
        
    def add_legend(self): # Adds a legend to the histogram to indicate which bar corresponds to which junction.   Logic for adding a legend        
        margin = 100
        
        box1_x1 = margin
        box1_x2 = box1_x1 + 15
        box1_y1 = margin
        box1_y2 = box1_y1 + 15
        
        box2_x1 = margin
        box2_x2 = box2_x1 + 15
        box2_y1 = box1_y2 + 3
        box2_y2 = box2_y1 +15
        
        # legend 1
        self.canvas.create_rectangle(box1_x1 , box1_y1 , box1_x2 , box1_y2 , fill = 'SteelBlue1')
        self.canvas.create_text(box1_x2 + 5 , box1_y1 + (box1_y2-box1_y1)/2 , text = "Elm Avenue/Rabbit Road", font=("Helvetica", 9, "bold"), fill="#474747", anchor="w")  
        
        # legend 2
        self.canvas.create_rectangle(box2_x1 , box2_y1 , box2_x2 , box2_y2 , fill = 'pale violet red')
        self.canvas.create_text(box2_x2 + 5 , box2_y1 + (box2_y2-box2_y1)/2 , text = "Hanley Highway/Westway", font=("Helvetica", 9, "bold"), fill="#474747", anchor="w")
        

    def run(self):  # Runs the Tkinter main loop to display the histogram.   Tkinter main loop logic
        self.setup_window() #calling methods
        self.draw_histogram()
        self.add_legend()
        self.root.mainloop()
          
          
          
          
# Task E: Code Loops to Handle Multiple CSV Files

class MultiCSVProcessor:
    def __init__(self):  # Initializes the application for processing multiple CSV files.
        self.current_data = None

    def load_csv_file(self, file_path): # Loads a CSV file and processes its data.  
        elm_counted_dict: dict[str, int] = Counter() # An empty dictionary where keys are strings and values are integers.
        hanley_counted_dict: dict[str, int] = Counter()  

        with open(file_path, newline='') as csvfile:
            readcsv = csv.reader(csvfile)
            next(readcsv)     
            for row in readcsv:
                if row[0] == "Elm Avenue/Rabbit Road":
                    hours = row[2][0:2]  # getting the first 2 digits from the timeOfDay column in excel sheet to get the hours
                    elm_counted_dict[hours] += 1  # incrementing the count for that hour to get the no of vehicles passed through elm junction in that hour
                elif row[0] == "Hanley Highway/Westway":
                    hours = row[2][0:2]
                    hanley_counted_dict[hours] += 1

        combined_dict = {}  # creating a combined dictionary to get a single output which contains both the total vehical counts of elm junction and hanley 
        # the key of this dictionary is hour and the values are represented as a tuple which contains count of elm hours and count of hanley hours respectively 

        for hour, elm_vehicle_count in elm_counted_dict.items(): #the for loop is iterating over each key(hour), value(elm_vehicle_count) pair in the 'elm_counted_dict' dictionary
            combined_dict[hour] = [elm_vehicle_count, 0]  # initializing hanley count to 0 and addinng the count of the elm hours for the respective hour

        for hour, hanley_vehicle_count in hanley_counted_dict.items():
            if hour in combined_dict:  # for each hour it checks whether that hour is already there in the combined dictionary 
                combined_dict[hour][1] = hanley_vehicle_count  # so if that hour is there, it will update the hanley_vehicle_count
            else:
                combined_dict[hour] = [0, hanley_vehicle_count]  # if the hour isn't there in the combined dictionary, it will initialize the elm vehicle count to 0 for that hour        
                
        return combined_dict


    def clear_previous_data(self): # Clears data from the previous run to process a new dataset.   
        self.current_data = None
        with open("results.txt", "w") as txtfile:
            txtfile.write("Previous data cleared...\n")
        print("Previous data in the results.txt file cleared.")

    def handle_user_interaction(self): # Handles user input for processing multiple files.                 
        return validate_continue_input()
        
            

    def process_files(self):  # Main loop for handling multiple CSV files until the user decides to quit. 
        need_to_repeat = True
        while need_to_repeat: #this part will loop until the 'need_to_repeat' gets false       
            # task A
            validate_day = (validate_date_input("day",1,31,"DD")).zfill(2) #it will add a leading zero if needed
            validate_month = (validate_date_input("month",1,12,"MM")).zfill(2)
            validate_year = validate_date_input("year",2000,2024,"YYYY")

            # task B
            string_file_name = 'traffic_data'+(validate_day)+(validate_month)+(validate_year)+'.csv' #creating the file name using user input
            process_csv_data(string_file_name) #calling the function
            display_outcomes(string_file_name) 

            # task C
            save_results_to_file(string_file_name) 
            
            # task DE
            try:
                displaying_date = f"{validate_day}/{validate_month}/{validate_year}"
                self.current_data = self.load_csv_file(string_file_name)
                histo = HistogramApp(self.current_data, displaying_date)
                histo.run()
                self.clear_previous_data()
            except FileNotFoundError:
                need_to_repeat = self.handle_user_interaction()
                continue
            need_to_repeat = self.handle_user_interaction()  #when the user enter n for this, that will return false and 'need_to_repeat' will be false and the loop will stop.





# main program 

if __name__ == "__main__":
    main_program = MultiCSVProcessor()
    main_program.process_files()





# if you have been contracted to do this assignment please do not remove this line
