import turtle

tela = turtle.Screen()

tela.bgcolor('white')

cursor = turtle.Turtle()
cursor.color("black")

def eu():
    
    #LETRA "E" A SEGUIR
    
    cursor.penup()
    cursor.goto(-310, 475)
    cursor.pendown()
    
    cursor.forward(45)         
    cursor.right(90)
    cursor.forward(22.5)
    cursor.right(90)
    cursor.forward(45)
    cursor.left(90)
    cursor.forward(22.5)
    cursor.left(90)
    cursor.forward(45)
    cursor.right(90)
    cursor.forward(22.5)
    cursor.right(90)
    cursor.forward(45)
    cursor.left(90)
    cursor.forward(22.5)
    cursor.left(90)
    cursor.forward(45)
    cursor.right(90)
    cursor.forward(22.5)
    cursor.right(90)
    cursor.forward(65)
    cursor.right(90)
    cursor.forward(112.5)
    cursor.right(90)
    cursor.forward(22.5)
    
 #AQUI EMBAIXO: ↓ É A LETRA "U"
    
    cursor.penup()
    cursor.goto(-245, 475)
    cursor.pendown()
    cursor.forward(22.5)
    cursor.right(90)
    cursor.forward(60)
    cursor.circle(30, 180)
    cursor.forward(60)
    cursor.right(90)
    cursor.forward(22.5)
    cursor.right(90)
    cursor.forward(112.5)
    cursor.right(90)
    cursor.forward(105)
    cursor.right(90)
    cursor.forward(112.5)
    
  
def te():
    
    #LETRA "T" AQUI!!
    
    cursor.penup()
    cursor.goto(-310, 225)
    cursor.pendown()
    cursor.forward(90)
    cursor.left(90)
    cursor.forward(45)
    cursor.right(90)
    cursor.forward(22.5)
    cursor.right(90)
    cursor.forward(120)
    cursor.right(90)
    cursor.forward(22.5)
    cursor.right(90)
    cursor.forward(45)
    cursor.left(90)
    cursor.forward(90)
    cursor.right(90)
    cursor.forward(30)
    
    #LETRA "E" A SEGUIR DE NOVO?!
    
    cursor.penup()
    cursor.goto(-190, 337.5)
    cursor.pendown()
    
    cursor.forward(-45)         
    cursor.right(90)
    cursor.forward(-22.5)
    cursor.right(90)
    cursor.forward(-45)
    cursor.left(90)
    cursor.forward(-22.5)
    cursor.left(90)
    cursor.forward(-45)
    cursor.right(90)
    cursor.forward(-22.5)
    cursor.right(90)
    cursor.forward(-45)
    cursor.left(90)
    cursor.forward(-22.5)
    cursor.left(90)
    cursor.forward(-45)
    cursor.right(90)
    cursor.forward(-22.5)
    cursor.right(90)
    cursor.forward(-65)
    cursor.right(90)
    cursor.forward(-112.5)
    cursor.right(90)
    cursor.forward(-22.5)
    
def pontos():
    cursor.penup()
    cursor.goto(-125, 220)
    
    
    
    
eu()
te()
pontos()


turtle.exitonclick()