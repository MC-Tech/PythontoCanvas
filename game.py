from tkinter import *
import random
root = Tk()
canvas = Canvas(root, width=1900, height=500, background = 'black')
canvas.pack()
i = 0
shot = False
lost = False
lost_ = False
enemy_x = 2000
enemy_y = random.randint(40, 460)
ship_x = 50
ship_y = 25
orig_y = 0
up = False
down = False
left = False
right = False
ship = canvas.create_rectangle(50, ship_y, 100, ship_y + 50, fill="red")
enemy = canvas.create_rectangle(enemy_x, enemy_y, enemy_x + 25, enemy_y + 25, fill="white")
laser = canvas.create_rectangle(-100, -100, -100, -100, fill = "green")
speed = 2
e_speed = 1
i = 0
score = 0
score_ = canvas.create_text(ship_x + 20, ship_y - 10, anchor=W, fill = "GREEN", font="Purisa", text=score)
kill = False
def down():
    global down, left, right, up
    left = False
    right = False
    up =  False
    down = True
def up():
    global down, left, right, up
    left = False
    right = False
    up =  True
    down = False
def left():
    global down, left, right, up
    left = True
    right = False
    up =  False
    down = False
def right():
    global down, left, right, up
    left = False
    right = True
    up =  False
    down = False
def update():
    global score_, enemy_x, ship_y, ship_x
    if ship_y < 465:
        if down == True:
            canvas.move(ship, 0, speed)
            ship_y += speed
    if ship_y > 10:
        if up == True:
            canvas.move(ship, 0, -speed)
            ship_y -= speed
    if ship_x < 1300:
        if right == True:
            canvas.move(ship, speed, 0)
            ship_x += speed
    if ship_x > 0:
        if left == True:
            canvas.move(ship, -speed, 0)
            ship_x -= speed
    if lost == False:
        canvas.coords(score_, ship_x + 20, ship_y - 10)
    canvas.move(enemy, -e_speed, 0)
    enemy_x -= e_speed
    canvas.after(5, update)
def test():
    global score_, score, lost_, lost, mouse, enemy, enemy_x, enemy_y, kill, e_speed, left, right, up, down
    if enemy_x < ship_x + 75:
        if enemy_x > ship_x - 25:
             if ship_y - 25 < enemy_y:
                if ship_y + 75 > enemy_y:
                        lost = True
    if enemy_x < 0:
        lost = True
    
    if kill == True:
        e_speed += 0.20
        enemy_x = 1910
        enemy_y = random.randint(40, 460)
        canvas.itemconfig(enemy, fill = "gray")
        enemy = canvas.create_rectangle(enemy_x, enemy_y, enemy_x + 25, enemy_y + 25, fill="white")
        kill = False
        score += 1
        canvas.itemconfig(score_, text = score)
    if score == 5:
        if lost == False:
            canvas.itemconfig(score_, fill = "CYAN")
    if score == 8:
        if lost == False:
            canvas.itemconfig(score_, fill = "MAGENTA")
            canvas.itemconfig(ship, fill = "BLUE")
    if lost == True:
        if lost_ == False:
            root.destroy()
            lost_ = True
            print("Your score was " + str(score))
    
    canvas.after(1, test)
def velo_u():
    global speed
    speed += 0.5
def velo_d():
    global speed
    if speed > 0.5:
        speed -= 0.5
def draw():
    global laser    
    canvas.coords(laser, ship_x + 50 + i, orig_y + 15, ship_x + 100 + i, orig_y + 35)
    canvas.after(1, shoot_)
def shoot_():
    global kill, i, shot
    if orig_y - 10 < enemy_y:
        if orig_y + 40 > enemy_y:
            if ship_x + 105 + i > enemy_x:
                    if ship_x < enemy_x:
                        kill = True
    if i > 1900:
        shot = False
    if i < 1900:
        shot = True

    if shot == True:
        canvas.after(1, draw)
    i += 100
    

def shoot():
    global orig_y, i
    if shot == False:
        orig_y = ship_y
        i = 0
        shoot_()
def key_test(event):
    global left, right, up, down, speed
    if event.char == 'w':
        left = False
        right = False
        up =  True
        down = False
    if event.char == 's':
        left = False
        right = False
        up =  False
        down = True
    if event.char == 'a':
        left = True
        right = False
        up =  False
        down = False
    if event.char == 'd':
        left = False
        right = True
        up =  False
        down = False
    if event.char == 'q':
        if speed > 0.5:
            speed -= 0.5
    if event.char == 'e':
        speed += 0.5
def space_press(event=None):
    global orig_y, i
    if shot == False:
        orig_y = ship_y
        i = 0
        shoot_()
test()
update()
canvas.bind_all('<Key>', key_test)
canvas.bind_all("<space>", space_press)
button_u = Button(root, text='LEFT(a)',command=left)
button_u.pack()
button_d = Button(root,text='RIGHT(d)',command=right)
button_d.pack()
button_u = Button(root, text='UP(w)',command=up)
button_u.pack()
button_d = Button(root,text='DOWN(s)',command=down)
button_d.pack()
velo_u = Button(root,text='+speed(e)',command=velo_u)
velo_u.pack()
velo_d = Button(root,text='-speed(q)',command=velo_d)
velo_d.pack()
shoot = Button(root,text='FIRE DA LASERZ!!!(space)',command=shoot)
shoot.pack()
root.mainloop()
