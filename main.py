# import required module
import os
import PyPDF2
# assign directory
directory = 'resumes'
requirements = []

with open('requirements.txt') as file:
    for line in file:
        line = line.strip()
        requirements.append(line)  # The comma to suppress the extra new line char
print("Our requirements")
print(requirements)


# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        reader = PyPDF2.PdfReader(f)
        for page_number in range(0, len(reader.pages)):
            page = reader.pages[page_number]
            page_content = page.extract_text()
            page_lower = page_content.lower()
            print(page_number)
            if any(substring in page_lower for substring in requirements):
                os.chdir("output_resumes")
                for page_number2 in range(0, len(reader.pages)):
                    fp = open(filename + ".txt", 'w')
                    page = reader.pages[page_number]
                    page_content = page.extract_text()
                    fp.write(page_content) 
                    fp.close()

        