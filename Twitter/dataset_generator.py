import csv
import random
def main():
    lines=[]
    for i in range(0,10000):
        a=random.randint(1,11)
        b=random.randint(1,11)
        c=((random.randint(1,100))%2)*10
        d=random.randint(1,11)
        e=((random.randint(1,100))%2)*10
        FAL=0
        if(e!=10):
            FAL=a*0.15+b*0.25+c*0.3+d*0.3
        type=0
        if(FAL>=4 and FAL<=5):
            type=1
        if(FAL>5 and FAL<=10):
            type=2

        lines.append([a,b,c,d,e,FAL,type])

    with open('dataset_gen.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    writeFile.close()

main()
