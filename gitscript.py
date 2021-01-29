#!/usr/bin/python3

# Built by jod35
import os
import subprocess


BASE_DIR=os.path.dirname(os.path.realpath(__file__))




print("Welcome to the GitScript v1.0!")


while True:
    print("Enter Action\n \
            1.Create local repository\n \
            2.Commit Changes \n \
            3.Show recent commits \n \
            4.Create a branch \n \
            5.Switch to branch \n \
            6.Show All branches \n \
            6.Pull remote changes \n \
            7.Delete local Git Repository \n \
            0.Exit\n \
            ")

    option=int(input(">>>> "))


    if option ==1:
        subprocess.run(["git", "init"])
        print(f"Created repository in {BASE_DIR} \n")

    elif option == 2:
        subprocess.run(["git","add","--all"])
        for file in os.listdir(BASE_DIR):
            print(f"Adding {file} ...")
        print("Done....")
        
        _commit_message=input("Enter your commit message: ")

        subprocess.run(["git","commit","-m",_commit_message])

        print("==============================")


    elif option == 3:
        subprocess.run(["git","log"])
        print("\n")
        print("===============================")


    elif option ==4:
        
        print("Enter the name of the branch to create: ")
        _branch_name =input("")

        subprocess.run(["git","checkout","-b",_branch_name])

        print("==============================")


    elif option==5:
        print("Enter the name of the branch to switch to: ")
        
        _branch_name =input("")

        subprocess.run(["git","checkout",_branch_name])


        print("==============================")




    elif option ==7:
        subprocess.run(["rm","-rf",".git"])
        print(f"Deleted git repository from {BASE_DIR} \n")

        print("==============================")


    elif option ==0:
        print("Thank You for using the GitScript")
        break
