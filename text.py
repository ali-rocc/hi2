# Function to create and write to a text file
def create_txt_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Define filenames and content
file1_name = 'file1.txt'
file1_content = 'This is the content of the first text file.'

file2_name = 'file2.txt'
file2_content = 'This is the content of the second text file.'

# Create the two text files
create_txt_file(file1_name, file1_content)
print(f"Contents of {file1_name}:\n{file1_content}\n")

create_txt_file(file2_name, file2_content)
print(f"Contents of {file2_name}:\n{file2_content}\n")

print(f"Created {file1_name} and {file2_name} successfully!")
