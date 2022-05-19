width = float(input("Digite a largura da parede em metros: "))
height = float(input("Digite a altura da parede em metros: "))

total_area = width * height
total_paint = total_area/2

print("Uma parede com {}m de largura e {}m de altura, tem uma área total de {}m² e são necessários {} litros de tinta para a sua pintura.".format(width, height, total_area, total_paint))
