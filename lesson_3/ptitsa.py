from turtle import *
x=Turtle()
x.screen.setup(800,800)
# def risuem_kvadrat(z,y):
#      for i in range(4):
#       x.left(45) поворот
#       x.fd(z)вперед
#       x.circle(radius,360) 
#       x.bk() nazad
#       x.left(45)
#       x.fd(y)
# risuem_kvadrat(100,100)
# x.screen.exitonclick()
# x.screen.mainloop()
def risuem_ptitsu():
    #x.left(10)
    x.fd(100)
    x.circle(40,180)
    x.left(38.5)
    x.fd(128)
    x.left(170)
    x.up()
    x.fd(145)
    x.down()
    x.circle(30,292)
    x.left(80)
    x.up()
    x.fd(58)
    x.right(60)
    x.down()
    x.fd(20)
    x.right(130)
    x.fd(17)
    x.right(85)
    x.up()
    x.fd(20)
    x.down()
    x.circle(4,360) #glaz
    x.left(120)
    x.up()
    x.fd(120)
    x.down()
    x.left(25)
    x.fd(30)    #noga
    x.left(70)
    x.fd(10)
    x.bk(10)
    x.left(30)
    x.fd(10)
    x.up()
    x.left(130)
    x.fd(40)
    x.down()
    x.left(130)
    x.fd(28)    #noga
    x.left(70)
    x.fd(10)
    x.bk(10)
    x.left(30)
    x.fd(10)

    x.up()
    x.fd(110)

risuem_ptitsu()
x.screen.exitonclick()
x.screen.mainloop()   
