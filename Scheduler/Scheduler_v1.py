
from dateutil.relativedelta import relativedelta
import random 
import datetime
import csv
from numpy import number
import pandas as pd 

def group_into_area(scrambled_soc_lists:tuple)->dict[str:list]:
    area_dict  =  { }
    for society in scrambled_soc_lists:
        if society[4].lower().strip() not in area_dict.keys():
            area_dict[society[4].lower().strip()] = [society]
        else:
            area_dict[society[4].lower().strip()].append(society)
    return area_dict

def get_zone(zone_name:str,get_length=False)->list:
    zone_list = []
    repeat_check = {}
    with open('data.csv', 'r') as f:
        data = csv.reader(f)
        for row in data:
            if row[3] == zone_name and row[1].lower().strip() not in repeat_check.keys():
                zone_list.append(row)
                repeat_check[row[1].lower().strip()] = True
    if get_length:
        return len(zone_list)
    else:
        return zone_list

def classifier(zone_list:list)->tuple[tuple,tuple,tuple]:
    """

    """
    new_soc = []
    angel_soc = []
    worst_soc = []
    medium_soc = []
    classifier_dict = {'East':1600,'West':1600,'North':1000,'South':1000,'Central':1000}
    for society in zone_list:
        if society[-3] == 'new':
            new_soc.append(society)
        elif int(society[2])>=800:
            angel_soc.append(society)
        elif float(society[-1])<=2500:
            worst_soc.append(society)
        else:
            medium_soc.append(society)
    
    return tuple([tuple(new_soc), tuple(angel_soc), tuple(worst_soc),tuple( medium_soc)])


def print_schedule_dict(sc_dict:dict)->None:
    for date,soc_list in sorted(sc_dict.items()):
        print(f' {date} : {soc_list}')

def is_monday(d):
    return d.weekday() == 0

def is_tuesday(d):
    return d.weekday() == 1
def week_full(week:list):
    for i in range(len(week)):
        if len(week[i])<=2:
            return False
    return True

def get_day_societies(day_int:int , done_list:list,items_list,week):
    random.shuffle(items_list)
    area_reference = False
    for area, soc_list in items_list:
                    if not area_reference:
                            area_reference = area
                    for soc in soc_list :
                        
                        if soc[1] not in done_list and area_reference == area: 
                                week[day_int].append(soc[1])
                            
                                done_list.append(soc[1])
                        if len(week[day_int])>=2:
                                break 
                    if len(week[day_int])>=2:
                        week[day_int].append(area_reference)
                        break
                    area_reference = False

def generate_week_capsules(zone:str):
    _zone = get_zone(zone)
    _classified = classifier(_zone)
    capsule_holder = []
    done = []
    angel_dict = group_into_area(_classified[1])
    medium_dict = group_into_area(_classified[3])
    worst_dict = group_into_area(_classified[2])
    new_dict = group_into_area(_classified[0])
    med_items = list(medium_dict.items())
    new_items = list(new_dict.items())
    worst_items = list(worst_dict.items())
    angel_items = list(angel_dict.items())

    for i in range(5):
        area_reference = [False,False,False,False,False,False,False]
        week = [[],[],[],[],[],[]]
        # get_day_societies(0,done,new_items,week)
        # get_day_societies(1,done,new_items,week)
        # get_day_societies(2,done,med_items,week)
        # get_day_societies(3,done,med_items,week)
        # get_day_societies(4,done,angel_items,week)
        # get_day_societies(5,done,angel_items,week)
        
        for area, soc_list in med_items:
                    if not area_reference[0]:
                            area_reference[0] = area
                    for soc in soc_list :
                        
                        if soc[1] not in done and area_reference[0] == area: 
                                week[0].append(soc[1])
                            
                                done.append(soc[1])
                        if len(week[0])>=2:
                                break 
                    if len(week[0])>=2:
                        week[0].append(area_reference[0])
                        break
                    area_reference = [False,False,False,False,False,False,False]
        random.shuffle(new_items)
        random.shuffle(med_items)
        for area, soc_list in new_items:
                    if not area_reference[1]:
                            area_reference[1] = area
                    for soc in soc_list :
                        
                        if soc[1] not in done and area_reference[1] == area: 
                                week[1].append(soc[1])
                            
                                done.append(soc[1])
                        if len(week[1])>=2:
                                break 
                    if len(week[1])>=2:
                        week[1].append(area_reference[1])
                        break
                    area_reference = [False,False,False,False,False,False,False]
        random.shuffle(new_items)
        for area, soc_list in new_items:
                    if not area_reference[2]:
                            area_reference[2] = area
                    for soc in soc_list :
                        
                        if soc[1] not in done and area_reference[2] == area: 
                                week[2].append(soc[1])
                            
                                done.append(soc[1])
                        if len(week[2])>=2:
                                break 
                    if len(week[2])>=2:
                        week[2].append(area_reference[2])
                        break
                    area_reference = [False,False,False,False,False,False,False]
        random.shuffle(new_items)
        for area, soc_list in new_items:
                    if not area_reference[3]:
                            area_reference[3] = area
                    for soc in soc_list :
                        
                        if soc[1] not in done and area_reference[3] == area: 
                                week[3].append(soc[1])
                            
                                done.append(soc[1])
                        if len(week[3])>=2:
                                break 
                    if len(week[3])>=2:
                        week[3].append(area_reference[3])
                        break
                    area_reference = [False,False,False,False,False,False,False]
        random.shuffle(new_items)
        for area, soc_list in angel_items:
                    if not area_reference[4]:
                            area_reference[4] = area
                    for soc in soc_list :
                        
                        if  area_reference[4] == area: 
                                week[4].append(soc[1])
                           
                        if len(week[4])>=2:
                                break 
                    if len(week[4])>=2:
                        week[4].append(area_reference[4])
                        break
                    area_reference = [False,False,False,False,False,False,False]
        random.shuffle(angel_items)
        for area, soc_list in angel_items:
                    if not area_reference[5]:
                            area_reference[5] = area
                    for soc in soc_list :
                        
                        if  area_reference[5] == area: 
                                week[5].append(soc[1])
                            
                        if len(week[5])>=2:
                                break 
                    if len(week[5])>=2:
                        week[5].append(area_reference[5])
                        break
                    area_reference = [False,False,False,False,False,False,False]
        #filler
        for day in week:
            if len(day) == 0 :
                area_reference = [False,False,False,False,False,False,False]
                for area, soc_list in new_items:
                    if not area_reference[2]:
                            area_reference[2] = area
                    for soc in soc_list :
                        
                        if soc[1] not in done and area_reference[2] == area: 
                                day.append(soc[1])
                            
                                done.append(soc[1])
                        if len(day)>=2:
                                break 
                    if len(day)>=2:
                        day.append(area_reference[2])
                        break
                    area_reference = [False,False,False,False,False,False,False]
        #extra filler not working 
        for day in week:
            if len(day) == 0 :
                area_reference = [False,False,False,False,False,False,False]
                for area, soc_list in worst_items:
                    if not area_reference[2]:
                            area_reference[2] = area
                    for soc in soc_list :
                        
                        if soc[1] not in done and area_reference[2] == area: 
                                day.append(soc[1])
                            
                                done.append(soc[1])
                        if len(day)>=2:
                                break 
                    if len(day)>=2:
                        day.append(area_reference[2])
                        break
                    area_reference = [False,False,False,False,False,False,False]
        print(week)

        capsule_holder.append(week)
    
    return capsule_holder

def week_number_generator(seed:int,total_weeks:int)->list:
    number_set= set()
    h, m, a = seed,seed,seed
    for i in range(seed,total_weeks):
        if h<total_weeks:
            number_set.add(h)
        if a<total_weeks :
            number_set.add(a)
        if m<total_weeks:
            number_set.add(m)
        h += 30
        a += 5
        m += 15
    number_list = list(number_set)
    number_list.sort()
    return number_list

def lay_schedule_per_zone(start_date,zone_week_numbers,week_capsule,schedule_dict):
    for i in range(len(zone_week_numbers)):
        current_date = start_date + relativedelta(weeks=zone_week_numbers[i])
        
        while not is_tuesday(current_date):
            current_date += relativedelta(days=1)
        for j in range(len(week_capsule[1])):
            schedule_dict[f'{current_date:%m-%d-%Y}'] = week_capsule[1][j]
            current_date += relativedelta(days=1)


def schedule_generator(start_date: datetime.date, duration_months:int):
    #capsules contain the week capsules - 5 
    east_capsules = generate_week_capsules('East')
    west_capsules = generate_week_capsules('West')
    south_capsules = generate_week_capsules('South')
    north_capsules = generate_week_capsules('North')
    central_capsules = generate_week_capsules('Central')
    while not is_monday(start_date):
        start_date += datetime.timedelta(days=1)
    end_date = start_date + relativedelta(months=duration_months)
    total_days = (end_date - start_date).days 

    total_weeks = total_days//7
    schedule_dict = {}
    east_numbers = []
    west_numbers = []
    south_numbers = []
    north_numbers = []
    central_numbers = []
    #assigning week numbers
    seed = 1
    east_numbers = week_number_generator(seed,total_weeks)
    west_numbers = week_number_generator(seed+1,total_weeks)
    south_numbers = week_number_generator(seed+2,total_weeks)
    north_numbers = week_number_generator(seed+3,total_weeks)
    central_numbers = week_number_generator(seed+4,total_weeks)


    lay_schedule_per_zone(start_date,east_numbers,east_capsules,schedule_dict)
    lay_schedule_per_zone(start_date,west_numbers,west_capsules,schedule_dict)
    lay_schedule_per_zone(start_date,south_numbers,south_capsules,schedule_dict)
    lay_schedule_per_zone(start_date,north_numbers,north_capsules,schedule_dict)
    lay_schedule_per_zone(start_date,central_numbers,central_capsules,schedule_dict)


    # for i in range(len(east_numbers)):
    #     current_date = start_date + relativedelta(weeks=east_numbers[i])
        
    #     while not is_tuesday(current_date):
    #         current_date += relativedelta(days=1)
    #     for j in range(len(east_capsules[1])):
    #         schedule_dict[f'{current_date:%m-%d-%Y}'] = east_capsules[1][j]
    #         current_date += relativedelta(days=1)


    # for i in range(len(west_numbers)):
    #     current_date = start_date + relativedelta(weeks=west_numbers[i])
        
    #     while not is_tuesday(current_date):
    #         current_date += relativedelta(days=1)
    #     for j in range(len(west_capsules[1])):
    #         schedule_dict[f'{current_date:%m-%d-%Y}'] = west_capsules[1][j]
    #         current_date += relativedelta(days=1)


    # for i in range(len(north_numbers)):
    #     current_date = start_date + relativedelta(weeks=north_numbers[i])
        
    #     while not is_tuesday(current_date):
    #         current_date += relativedelta(days=1)
    #     for j in range(len(north_capsules[1])):
    #         schedule_dict[f'{current_date:%m-%d-%Y}'] = north_capsules[1][j]
    #         current_date += relativedelta(days=1)


    # for i in range(len(south_numbers)):
    #     current_date = start_date + relativedelta(weeks=south_numbers[i])
        
    #     while not is_tuesday(current_date):
    #         current_date += relativedelta(days=1)
    #     for j in range(len(south_capsules[1])):
    #         schedule_dict[f'{current_date:%m-%d-%Y}'] = south_capsules[1][j]
    #         current_date += relativedelta(days=1)

    # for i in range(len(central_numbers)):
    #     current_date = start_date + relativedelta(weeks=central_numbers[i])
        
    #     while not is_tuesday(current_date):
    #         current_date += relativedelta(days=1)
    #     for j in range(len(central_capsules[1])):
    #         schedule_dict[f'{current_date:%m-%d-%Y}'] = central_capsules[1][j]
    #         current_date += relativedelta(days=1)
    
    return schedule_dict

dict_data = []
schedule_dict = schedule_generator(datetime.date(2022,1,24),24)
print(schedule_dict)
for date , soc_list in schedule_dict.items():
    dict_data.append({'Date':date,'Society names':(soc_list[0],soc_list[1]),'Area':soc_list[-1]})

csv_file = "Schedule.csv"
csv_columns = ['Date','Society names','Area']
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")

df_new = pd.read_csv('Schedule.csv')
  
# saving xlsx file
schedule_xlsx = pd.ExcelWriter('Schedule.xlsx')
df_new.to_excel(schedule_xlsx, index = False)
  
schedule_xlsx.save()

