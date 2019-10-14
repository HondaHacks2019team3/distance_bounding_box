import os

def main():
	file_list=[]
	for file in os.listdir("output"):
		if file.endswith(".txt"):
			file_list.append("output/"+file)
	# print(file_list)

	for i in file_list:
		print("File name is ",i)
		box_coords=[]
		count =1
		file=open(i,"r")
		if file.mode=="r":
			for contents in file.read().split(" "):
				if count%6==0 or contents=='\n':
					count=count+1
					continue
				count=count+1

				box_coords.append(int(contents))

		bounding_box(box_coords)

def bounding_box(lista):
	listb=[]
	for i in range(len(lista)):
		if (i%5==0 and lista[i]==2):
			xmin=lista[i+1]
			xmax=lista[i+3]
			ymin=lista[i+2]
			ymax=lista[i+4]
			print ('bounding_box coordinates are',xmin,xmax,ymin,ymax)
			listb.append([xmin,xmax,ymin,ymax])
	
	listb.sort(key=lambda x:x[0])
	print (listb)
	check_distance(listb)
		
def check_distance(listc):
	# pixel_to_feet=0.049564379
	pixel_to_meter=0.0091159136
	for i in range(len(listc)-1):
		check_distance=(listc[i+1][0]-listc[i][1])*pixel_to_meter
		print ("Distance between vehicle {} and {} in pixels is {}".format(i,i+1,check_distance))

if __name__=="__main__":
	main()