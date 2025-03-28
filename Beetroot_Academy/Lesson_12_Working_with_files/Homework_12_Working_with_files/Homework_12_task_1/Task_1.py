#
# Files
#
# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
# Then write another script that opens myfile.txt, and reads and prints its contents.
# Run your two scripts from the system command line.
#
# Does the new file show up in the directory where you ran your scripts?
#
# What if you add a different directory path to the filename passed to open?
#
# Note: file write methods do not add newline characters to your strings;
# add an explicit "\n" at the end of the string if you want to fully terminate the line in the file.

print(
    '_____Task 1_____\n'
)

with open("myfile.txt", "w") as file:
    file.write("Hello file world!\n")

with open("myfile.txt", "r") as file:
    content = file.read()
    print(content)
