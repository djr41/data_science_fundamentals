:: Batch file for manipulating folders
@echo off
mkdir folder_1
mkdir folder_2
mkdir folder_3
cd folder_1
mkdir sub_folder_1
mkdir sub_folder_2
mkdir sub_folder_3
:: Go back to initial directory and delete two of the folders
cd ..
rmdir folder_2
rmdir folder_3