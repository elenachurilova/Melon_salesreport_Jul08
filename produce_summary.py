# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


def melon_delivery_report():
    """Printing sales report from 3 files"""

    #varibales to reference file names
    day_1_file = open("um-deliveries-20140519.txt")
    day_2_file = open("um-deliveries-20140520.txt")
    day_3_file = open("um-deliveries-20140521.txt")

    #creating a list with file varibales to iterate over
    files = [day_1_file, day_2_file, day_3_file]

    #variable to count the number of a day (day 1, day 2...)
    day_number = 1

    #for every file from the list of files
    for file in files:

        #need this to use the loop below
        current_file = file
        
        #print what day sales report data refers  to
        print("DATA FOR DAY {}".format(day_number))  
        day_number += 1  #day counter

        #for every line in the each file 
        for line in current_file:

            #remove blank space from the right hand side
            line = line.rstrip()
            #split the line of text into list items, look for | sign to know where to split
            words = line.split('|')

            #assign new list's indices for the new variables
            melon = words[0]
            count = words[1]
            amount = words[2]

            #print message using format method
            print("Delivered {} {}s for total of ${}".format(
                count, melon, amount))

        #close the file at the end
        current_file.close()

melon_delivery_report()



