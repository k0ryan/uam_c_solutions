import subprocess

if __name__ == "__main__":
    for sem_num in range(1, 15):
        cunt = True
        ej_num = 0
        while cunt and ej_num < 20:
            ej_num = ej_num + 1
            subprocess.call("wget https://uamx.uam.es/assets/courseware/a61188e6fea1ff94be6d0d5eec38090b/asset-v1:UAMx+ProgC02+2017+type@asset+block/"+str(sem_num)+"_"+str(ej_num)+".c", shell=True)

        cunt = True
        ej_num = 0
        while cunt and ej_num < 10:
            ej_num = ej_num + 1
            subprocess.call("wget https://uamx.uam.es/assets/courseware/a61188e6fea1ff94be6d0d5eec38090b/asset-v1:UAMx+ProgC02+2017+type@asset+block/"+str(sem_num)+"_p"+str(ej_num)+".c", shell=True)
