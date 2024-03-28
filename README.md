# file-organizer

## Overview:
The goal of this project was to explore Python features associated with directory and file management, including paths and the os module. 
This project has a great deal of practical utility, as it automates the process of organizing files by extension code. 

### Description:
I planned on organizing my files into 4 categories: PDFs, Documents, Presentations, and Images. I initiated this process by defining how different file extensions 
should be categorized : for example, any file ending with '.png', '.jpeg', or '.jpg' should be classified as an 'Image'.

I created a function(**organize_dir**)that took in the name of a source directory as an argument. For my source dir, I created a directory named **'data'** that contained all of the 
files I wanted to organize. Because the source directory is passed in as a string object, I needed to define the path of my 'data' folder: I identified the current 
working directory (cwd) and joined it with the source. 

I then used a neat function in the 'os' module, 'os.walk'. This allows you to recursively navigate through the directory tree to ensure that you are accessing every item in your directory-- so if my source directory has subdirectories, I can organize the files contained in those folders as well! 

I iterated through each file in my source and created a path for them to identify their current location. 
I also assigned a 'target' directory for each file based on its extension. The 'target' would be one of the four aforementioned categories.
After joining the source path to the target directory name to identify the **target path**, I passed the target path into my '**create_dir()**' function. 
**create_dir()**:
If the target_path passed in did not already exist(meaning the current file is the first file to belong to a particular category), a new directory 
with the appropriate target name and path would be created. 
However, if the target_path passed in already exists(meaning another file was already assigned to the same target as the current file), no new target directory is created. 

As a final step, I used the '**shutil.move()**' method to move each file from its current location to the appropriate target directory. I highly recommend this method to anyone working with file and directory management, because the item in question is conveniently relocated to the target destination, rather than having another copy of the item placed in the target location and then deleting the first item copy from the original location. 

In my 'data' folder, you should be able to see the proper result after running this program:
four subdirectories representing the four target categories, each containing correctly organized file(s). 


