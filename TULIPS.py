import turtle as tu
import re
import docx

source = "tulips"
data = docx.Document("{}.docx".format(source))
coordinates = []
border_color = "yellow"  # Color del borde
background_color = "light blue"  # Color de fondo celeste pastel

for i in data.paragraphs:
    try:
        coord_stg_tup = re.findall(r'\([-+]?\d*\.\d*(?:[eE][-+]?\d+)? ?\, ?[-+]?\d*\.\d*(?:[eE][-+]?\d+)?\)', i.text)
        coord_num_tup = []

        for j in coord_stg_tup:
            coord_pos = re.findall(r'[-+]?\d*\.\d*', j)
            coord_num_lst = [float(k) for k in coord_pos]
            coord_num_tup.append(tuple(coord_num_lst))

        coordinates.append(coord_num_tup)
    except:
        pass

pen = tu.Turtle()
screen = tu.Screen()

# Establecer el color de fondo en celeste pastel
screen.bgcolor(background_color)

# Desactivar el trazado de Turtle
tu.tracer(2)

pen.speed(0)
screen.getcanvas().winfo_toplevel().attributes("-fullscreen", True)

for i in range(len(coordinates)):
    draw = 1
    path = coordinates[i]
    pen.pencolor(border_color)  # Establecer el color del borde en amarillo
    pen.pensize(2)  # Establecer el ancho de la pluma a 2 (ajusta según tu preferencia)
    pen.fillcolor(background_color)  # Establecer el color de relleno igual al fondo
    pen.begin_fill()
    for order_pair in path:
        x, y = order_pair
        y = -1 * y
        if draw:
            pen.up()
            pen.goto(x, y)
            pen.down()
            draw = 0
        else:
            pen.goto(x, y)
    pen.end_fill()
    pen.hideturtle()

# Actualizar la pantalla después de dibujar todas las formas
tu.update()

screen.mainloop()
