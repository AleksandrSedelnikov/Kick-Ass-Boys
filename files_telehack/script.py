import check
import subprocess

global check_l
trace_data = []
lines = []

def nothing():
    pass

def file_size(file):
    return len(open(file).readlines())

def trace(link):
    output = subprocess.check_output(['tracert', link])
    trace_data.append(output.decode('cp866'))

def save_data(src_file): #принимает на вход путь исходного файла
    f = open(src_file)
    size = file_size(src_file)
    outf = open('results.txt', 'w')
    for i in range (size):
        line = f.readline()
        link = line.rstrip('\n')
        outf.write('%-23s' % (link + trace_data[i] + '\n'))
        if(i != size -1):
            outf.write('/----------------------------------------------------------/' + '\n')

def main_script(src_file):
    size = file_size(src_file)
    f = open(src_file)

    for i in range (size):
        line = f.readline()
        lines.append(line.rstrip('\n'))
    f.close()

    access_data = check.connection_possibility(lines, size)
    
    for j in range (size):
        trace(access_data[1][j])

    for i2 in range(0, len(trace_data)):
        access_data[2].append(trace_data[i2])
    
    return access_data
