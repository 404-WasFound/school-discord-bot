from datetime import datetime as dt
import requests as req
from os import listdir


def format_table(list_of_data):

    # Setup
    raw_lod = list_of_data
    lod = []
    mil = 50
    limited_itemS = []

    # Prase and split data
    for d in raw_lod:

        d = d.replace("[",           "")
        d = d.replace("]",           "")
        d = d.replace("\'",          "")
        d = d.replace("SUMMARY",     "")
        d = d.replace("LOCATION",    "")
        d = d.replace("DESCRIPTION", "")
        d = d.replace(":",           "")

        lod.append(d)


    for item in lod:

        if len(item) > mil:

            substring_count = len(item) - mil
            limited_item = item[:-substring_count]
            limited_itemS.append(limited_item)

        if len(item) < mil:

            addstring_count = mil - len(item)
            limited_item = item + " " * addstring_count
            limited_itemS.append(limited_item)

    # Create menu

    topper_length = mil + 4
    topper_string = "=" * topper_length
    final_lineS = []

    for l_item in limited_itemS:

        final_line = "| "
        final_line += l_item + " |"
        final_lineS.append(final_line)



    # FINAL MENU STRING

    final_string = ""

    final_string += topper_string + "\n"

    for line in final_lineS:
        final_string += line + "\n"

    final_string += topper_string

    #*
    return final_string


def get(url, filename):

    files = listdir()

    if f"{filename}.ics" not in files:

        r = req.get(url, allow_redirects=True)
        open(f"{filename}.ics", "wb").write(r.content)


def get_data(url, filename):

    get(url, filename)

    with open(f"{filename}.ics", "r") as file:

        data = file.read().splitlines()

    all_data = []
    final_data = []

    # DTSTART;TZID=Pacific/Auckland:20220209T113500
    # DTEND;TZID=Pacific/Auckland:20220209T123000

    def chunks(lst, n):

        """Yield successive n-sized chunks from lst."""

        for i in range(0, len(lst), n):

            yield lst[i:i + n]


    for item in data:

        if "SUMMARY" in item:

            all_data.append(item.split(" ")[0])

        if "LOCATION" in item:

            all_data.append(item)

        if "DESCRIPTION" in item:

            all_data.append(item)

        if "DTSTART" in item:

            # 20220209T123000
            # 2022/02/09 T=12:30.00

            tzid = item.split(":")[1]

            time = list(chunks(tzid.split("T")[1], 2))
            time_str = f"{time[0]};{time[1]}"
            # 12, 30, 00

            date = list(chunks(tzid.split("T")[0], 2))
            date_obj = dt(int(f"{date[0]}{date[1]}"), int(date[2]), int(date[3]), int(time[0]), int(time[1]), int(time[2]))
            date_str = str(date_obj.strftime("%A"))
            # 20, 22, 02, 09

            all_data.append(f"{date_str} ({time_str})")


        if "DTEND" in item:


            tzid = item.split(":")[1]

            time = list(chunks(tzid.split("T")[1], 2))
            time_str = f"{time[0]};{time[1]}"

            date = list(chunks(tzid.split("T")[0], 2))
            date_obj = dt(int(f"{date[0]}{date[1]}"), int(date[2]), int(date[3]), int(time[0]), int(time[1]), int(time[2]))
            date_str = str(date_obj.strftime("%A"))

            all_data.append(f"{date_str} ({time_str})")


    with open("output.txt", "w") as file:

        file.truncate()

        for item in list(chunks(all_data, 5)):

            file.write(str(item) + "\n")

    with open("output2.txt", "r+") as file:

        with open("output.txt", "r") as file2:

            data = file2.read()

        for line in data.splitlines():

            if "Monday" in line: 
                new_line = line.replace("Monday", "Tuesday")
                final_data.append(new_line)

            elif "Tuesday" in line: 
                new_line = line.replace("Tuesday", "Wednesday")
                final_data.append(new_line)


            elif "Wednesday" in line: 
                new_line = line.replace("Wednesday", "Thursday")
                final_data.append(new_line)


            elif "Thursday" in line:
                new_line = line.replace("Thursday", "Friday")
                final_data.append(new_line)


            elif "Friday" in line: 
                new_line = line.replace("Friday", "Monday")
                final_data.append(new_line)

        file.truncate()

        for new_item in final_data:

            file.write(str(new_item) + "\n")

    formatted = []

    for x in range(32, 57):

        formatted.append(final_data[x - 1])

    return format_table(formatted).replace(";", ":")

    # GET LINES 32 - 56
