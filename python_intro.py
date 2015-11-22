print("Hello, Django girls!")
if 3>2:
	print("5 is indeed greater than 2")
else:
	print("5 is not greater thane 2")

name="Sonja"
if name=="Ola":
	print("Hey Ola!")
elif name=="Sonja":
	print("Hey Sonja")

else:
	print("Hey anonymus!")
volume=57
if volume<20:
	print("kisebb, mint 70")
elif 20<= volume<40:
	print("20 és 40 között")
elif 40<=volume<60:
	print("40 és 60 között")
elif 60<= volume<80:
	print("60 és 80 között")
elif 80<=volume<100:
	print("jajj, már 100")

def hi():
	print("Hi there")
	print("How are you")
hi()

def hi(name):
	if name== "Ola":
		print("Hi ola")
	elif name== "Sonja":
		print("Hi Sonja")
	else:
		print("Hi anonymus")
hi("Béla")
hi("Bözsi")

def hi(name):
	print("Hi "+ name +" !")
hi("Kálmán")

girls = ["Réka", "Móni", "Jani", "Peti"]
for name in girls:
	hi(name)
	print("Next girl")

for i in range(1,6):
	print(i)