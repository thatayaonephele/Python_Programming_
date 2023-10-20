#s.a.tl Example Application: Date Conversion
def date_converter():
    output = ''
    output_day = ''
    month_list = ["Jan","Feb","March","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    len_list = len(month_list)
    usr_input = input("Please enter the date in mm/dd/yyyy format: ")
    dilemeter = "/"
    for x in usr_input:
        output = usr_input.split(dilemeter)
    index = int(output[0])
    for y in range(1,len_list+1):
        if index == y:
            print(f"The converted date is: {output[1]} {month_list[index-1]} {output[2]}")
date_converter()