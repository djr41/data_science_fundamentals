:: batch file to create folders with conditional logic
@echo off
if exist new_folder mkdir if_folder
if exist if_folder (mkdir hyperionDev) else (mkdir new-projects)