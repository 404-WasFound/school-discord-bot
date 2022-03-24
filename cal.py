from datetime import datetime as dt

with open("20126-KNS5JXHSN1VBJM7DZLF4PVBQ.ics", "r") as file:

    data = file.read().splitlines()

all_data = []
final_data = []

# DTSTART;TZID=Pacific/Auckland:20220209T113500
# DTEND;TZID=Pacific/Auckland:20220209T123000

def chunks(lst, n):

    """Yield successive n-sized chunks from lst."""

    for i in range(0, len(lst), n):

        yield lst[i:i + n]


count = 0

for item in data:

    if "SUMMARY" in item:

        all_data.append(item.split(" ")[0])

        count += 1

    if "LOCATION" in item:

        all_data.append(item)

    if "DESCRIPTION" in item:

        all_data.append(item)

    if "DTSTART" in item:

        #if count >= 11:

            # 20220209T123000
            # 2022/02/09 T=12:30.00

            tzid = item.split(":")[1]

            time = list(chunks(tzid.split("T")[1], 2))
            time_str = f"{time[0]}:{time[1]}"
            # 12, 30, 00

            date = list(chunks(tzid.split("T")[0], 2))
            date_obj = dt(int(f"{date[0]}{date[1]}"), int(date[2]), int(date[3]), int(time[0]), int(time[1]), int(time[2]))
            date_str = str(date_obj.strftime("%A"))
            # 20, 22, 02, 09

            all_data.append(f"{date_str} ({time_str})")

        #else: 

        #    all_data.append("N/A")

    if "DTEND" in item:

        #if count >= 11:

            tzid = item.split(":")[1]

            time = list(chunks(tzid.split("T")[1], 2))
            time_str = f"{time[0]}:{time[1]}"

            date = list(chunks(tzid.split("T")[0], 2))
            date_obj = dt(int(f"{date[0]}{date[1]}"), int(date[2]), int(date[3]), int(time[0]), int(time[1]), int(time[2]))
            date_str = str(date_obj.strftime("%A"))

            all_data.append(f"{date_str} ({time_str})")

        #else: 

        #    all_data.append("N/A")



from pprint import pprint

print("\n\n STARTS HERE \n\n")

pprint(list(chunks(all_data, 5)))

with open("output.txt", "w") as file:

    file.truncate()

    for item in list(chunks(all_data, 5)):

        file.write(str(item) + "\n")
