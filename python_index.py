from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import tempfile
import csv, re, glob, sys, os, shutil
import pandas as pd
import numpy as np
from pandas.io.parsers import read_csv
from flask import Flask, render_template, request
from pathlib import Path
from datetime import datetime
from os import listdir
from os.path import isfile, join
from flask import request
from urllib.request import Request, urlopen
import requests
import urllib.request
from urllib.request import urlretrieve


app = Flask(__name__)

@app.route('/')
def index():
    os.system("clear")
    print("Index.html")
    return render_template('index.html')
    

@app.route('/remove_string_from_other_txtfile', methods=['GET'])#✅
def remove_string_from_other_txtfile():
    A=np.loadtxt("QA.txt",dtype="str")
    AA=list(A)
    print(len(AA))

    B=np.loadtxt("output.txt",dtype="str")
    BB=list(B)
    print(len(BB))

    print("start")
    value = len(AA)
    counter=1

    for i in AA:
        if i in BB:
            BB.remove(i)
            counter += 1
            procent = counter/value*100
            print("C : "+str(counter)+" --- "+str(procent)+"%" )
            
    print(str(BB))

    with open("Resultxxx.txt", "a") as file_object:
        file_object.write(str(BB))

    file = Path('Resultxxx.txt')
    file.write_text(file.read_text().replace("', '", ' -e '))
    file.write_text(file.read_text().replace("['", ''))
    file.write_text(file.read_text().replace("']", ''))
    file.write_text(file.read_text().replace(" -e -E -e ", ' -E '))
    file.write_text(file.read_text().replace(" -e > -e ", ' > '))
    file.write_text(file.read_text().replace(" -e -r -e ", ' -r '))
    file.write_text(file.read_text().replace("sudo -e tsh", 'sudo tsh'))
    file.write_text(file.read_text().replace(" -e -T -e ", ' -T '))
    file.write_text(file.read_text().replace(" -e -e -e ", ' -e '))
    file.write_text(file.read_text().replace("  ", ' '))
    file.write_text(file.read_text().replace("-e -e -e", '-e'))
    file.write_text(file.read_text().replace("-e -e -e -e -e", '-e'))
    file.write_text(file.read_text().replace("-e -e -e -e -e -e -e", '-e'))
    file.write_text(file.read_text().replace("-e -e -e -e -e -e -e -e", '-e'))
    file.write_text(file.read_text().replace("-e -e -e -e -e -e -e -e -e", '-e'))
    file.write_text(file.read_text().replace("-e -e -e -e -e -e", '-e'))
    file.write_text(file.read_text().replace("-e -e -e -e", '-e'))
    file.write_text(file.read_text().replace("-e -e", '-e'))
    file.write_text(file.read_text().replace(" -e -e ", ' -e '))





    print("End")



    return "success"

@app.route('/devide_big_txtfile', methods=['GET'])#✅
def devide_big_txtfile():
    splitLen = 10000         # x lines per file
    outputBase = 'output' # output.1.txt, output.2.txt, etc.

    input = open('Result.txt', 'r').read().split('*^*')

    at = 1
    for lines in range(0, len(input), splitLen):
        outputData = input[lines:lines+splitLen]
        output = open(outputBase + str(at) + '.txt', 'w')
        output.write('\n'.join(outputData))
        output.close()
        at += 1

    return "success"

@app.route('/replace_text', methods=['GET'])#✅
def replace_text():
    file = Path('Result.txt')
    file.write_text(file.read_text().replace(' -e ', ' *^* -e '))
    
    return "succes"

@app.route('/protocol_gathering_wireshark', methods=['GET'])#✅
def protocol_gathering_wireshark():
    chrome_path = 'chromedriver'
    driver = webdriver.Chrome(chrome_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    
    driver.set_window_size(800,400)
    driver.get("https://www.wireshark.org/docs/dfref/")
    # sudo tshark -r network_traffic.pcap -T fields xxxx
    # -E header=y -E separator=, -E quote=d -E occurrence=f > test2.csv
    protocol_counter = 1
    
    while protocol_counter < 1000:
        
        len_field = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div/div/div['+str(protocol_counter)+']').text
        time.sleep(2)
        
        if len(len_field) == 1:
            protocol_counter += 1
            print("str = "+ str(len_field))
            len_field = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div/div/div['+str(protocol_counter)+']').text
        else:
            print("len str = "+str(len(len_field)))
            print("Name = "+ str(len_field))
        
        print("Information : "+str(len_field))

        my_list = len_field.split(",")
        my_list.pop(0)
        my_list2 = my_list[0].split(" ")
        
        fields_numb = my_list2[1]
        print("Number : "+str(fields_numb))

        driver.find_element(By.XPATH, '//*[@id="DFRef"]/div/div/div/div/div['+str(protocol_counter)+']/a').click()
        time.sleep(2)

        field_number = int(fields_numb)
        array_index = ['x'] * int(field_number)
        
        for index, item in enumerate(array_index):
            print(str(index)+" 😊")
            index = index+1
            find_field = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div/div/div/table/tbody/tr['+str(index+1)+']/td[1]').text
            print(str(find_field))
            with open("txt.txt", "a+") as textFile:
                textFile.write("-e ")
                for my_field in find_field:
                    textFile.write(my_field)
                textFile.write(" ")
        
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="filter_page_background"]/div/div/div/div/p[3]/a').click()
        time.sleep(2)
        
        protocol_counter += 1
        print("protocol_counter = "+str(protocol_counter))

    return str("Success")

@app.route('/analyze_create_csv', methods=['POST', 'GET'])#✅
def analyze_create_csv():


    
    if request.method == 'POST':
        #Get file
        f = request.files['file']
        f.save(secure_filename(f.filename))
        file_name = str(f.filename)
        
        #Obj'er
        cwd = os.getcwd()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        while_counter = 1
        irra_counter = 1
        parameter_count = 24 # min 2 -- max 24
        
        #Find directory and rename .pcap/.pcapng file
        print("\n")
        print("current = "+str(cwd))
        print("dir_path = "+str(dir_path))
        print("\n")
        file_name_len = list(listdir(dir_path))
        print("Dir = "+str(file_name_len))
        print("\n")
        matches = [match for match in file_name_len if ".pcap" in match]
        print("number of .pcap/.pcapng files : "+str(len(matches)))
        print("\n")
        pcap_files_num = len(matches)
        print("Pcap.files count = "+str(pcap_files_num))

       # while irra_counter < len(matches)+1: # 2 = 1
        pcap_file = str(matches[irra_counter-1])
        new_pcap_file = pcap_file.strip("['',]")
        orginal_pcap_fileName = str(new_pcap_file)
           # print("pcap file : "+new_pcap_file)
           # print("pcap file renamed to network_traffic.pcap")
        os.rename(str(orginal_pcap_fileName), 'network_traffic.pcap')

            #Create A_*.csv from /textFiles
        while while_counter < parameter_count:
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            analyze_x = Path(str(dir_path)+'/textFiles/'+str(while_counter)+'.txt').read_text()
            os.system("cd {} && {}".format(dir_path, analyze_x))
            print("Round 1 - Creating File: "+"A_"+str(while_counter)+" - "+str(time))
            while_counter += 1
        

            #Delete empty columns & convert to filter_csv.csv
        while_counter = 1
        while while_counter < parameter_count:
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data = read_csv('A_'+str(while_counter)+'.csv', low_memory=False)
            filtered_data = data.dropna(axis='columns', how='all')
            filtered_data.to_csv('filter_csv'+str(while_counter)+'.csv', index=False)
            print("Round 2 - Converting File: "+"filter_csv"+str(while_counter)+" - "+str(time))
                #Remove A_* files
            os.remove('A_'+str(while_counter)+'.csv')
            while_counter += 1
        
        #Delete empty rows & convert to Analyse_filter*.csv
        import csv
        while_counter = 1
        while while_counter < parameter_count:
            print("Round 3 - Filtering File: "+"Analyse_filter"+str(while_counter)+" - "+str(time))
            with open('filter_csv'+str(while_counter)+'.csv') as input, open('Analyse_filter'+str(while_counter)+'.csv', 'w', newline='') as output:
                writer = csv.writer(output)
                for row in csv.reader(input):
                    if any(field.strip() for field in row):
                        writer.writerow(row)
            while_counter += 1

            #Remove filter_csv* files
        while_counter = 1
        while while_counter < parameter_count:
            os.remove('filter_csv'+str(while_counter)+'.csv')
            while_counter += 1
    
            #Delete empty Analyse_filter.csv files
        empty_csv_files = ['x'] * int(parameter_count)
        while_counter = 1
        while while_counter < parameter_count:
            with open('Analyse_filter'+str(while_counter)+'.csv', 'r') as csv:
                first_line = csv.readline()
                leng = len(first_line)
                if leng < 5:
                    os.remove('Analyse_filter'+str(while_counter)+'.csv')
                    empty_csv_files.insert(while_counter-1, while_counter)
            while_counter += 1

        #Join Analyse_filter*.csv files into FULL_Analyse.csv
        print("Round 4 - Joining Files --> FULL_Analyse.csv")
        df = pd.concat(map(pd.read_csv, glob.glob(os.path.join(str(dir_path), 'Analyse_filter*.csv'))), ignore_index= True)
        df.to_csv("FULL_Analyse"+str(orginal_pcap_fileName)+".csv")
        print(df)
    
            #Delete all Analyse_filter*.csv files
        while_counter = 1
        while while_counter < parameter_count:
            if empty_csv_files[while_counter-1] == while_counter:
                print("Analyse_filter"+str(while_counter)+"is null")
            elif empty_csv_files[while_counter-1] != while_counter:
                os.remove('Analyse_filter'+str(while_counter)+'.csv')
            while_counter += 1
                
        #Result
        print("end")
        os.rename('network_traffic.pcap', str(orginal_pcap_fileName)+str(irra_counter)+'_analyzed'+'.pcap')
        shutil.move(str(dir_path)+"/"+str(orginal_pcap_fileName)+str(irra_counter)+'_analyzed'+'.pcap', str(dir_path)+"/Analyzed_pcaps")
        irra_counter += 1

    print("success mon ami!")
    return render_template('index.html', fileName=file_name)

# Activate function
#analyze_create_csv()

if __name__ == '__main__':
    app.run(debug=True)
