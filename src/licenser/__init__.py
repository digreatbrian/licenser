'''Easily  Add license string to a file. '''
__author__='Brian Musakwa'
def add_license(filename,license):
	data=license
	dt=data.split('\n')
	dr=[]
	for x in dt:
		dr.append('\n')
		dr.append('#')
		dr.append(x)
	dr_str=""
	for x in dr:
		dr_str+=x
	
	fd=open(str(filename),'r')
	filedata=fd.read()
	fd.close()
	
	with open(filename,"w") as fd:
		data=dr_str+'\n'+filedata
		fd.write(data)
		fd.close()
