#подключаем библиотеку PyGame (заранее ее нужно установить)
import pygame
#используем метод init() для иницилизации  библиотеки в начале программы ( иначе будет выдавать ошибу и не запускать программу)
pygame.init()
#подключаем библиотеки time и random (эти библиотеку уже установленны и предварительной установки не требуют)
import time
import random
#подключаем музыку для игры
pygame.mixer.music.load("Kirara.mp3") #в скобках пишем название нашей музыки, которую хотим запустить. Файл с музыкой и программой должны находиться в одном месте, иначе будет вылетать ошибка
#запускаем нашу музыку
####pygame.mixer.music.play()
#что бы музыка не заканчивалась после моментка когда закончилась музыкальная дорожка, нам нужно ее зациклить
pygame.mixer.music.play(-1)


#цвета для игры, сохраняем в переменную их код по RGB
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
#сохраняем в переменные размер окна
dis_width = 500 #ширина
dis_height = 500 #высота
#устанавливаем размер игрового окна
dis = pygame.display.set_mode((dis_width, dis_height))
#придумываем название окну с игрой
pygame.display.set_caption('Змейка')
#считывает сколько времени прошло с начала запуска игры
clock = pygame.time.Clock()
#устанавливаем размер змейки и яблока
snake_block = 10

#snake_speed = 10
font_style = pygame.font.SysFont("bahnschrift", 25)#указываем шрифт и размер для окна с проигрешем
score_font = pygame.font.SysFont("comicsansms", 35)#указзываем название шрифта иразмер дял подписи очков
#создаем функцию для вывода на экран количества очков, передаем ей в аргументы переменную в которой хранится число очков(длина змейки - 1)
def Your_score(score):
   #создаем переменую в которую будем сохранять надпись, отображаться ей или нет и цвет
   value = score_font.render("Ваш счёт: " + str(score), True, yellow)
   #визиализируем надпись на экране, в квадратных скобках указываем где она будет располагаться
   dis.blit(value, [0, 0])
#функция которая отображает нашу змейку на экане, в аргументах мы передаем лист ее длиной и размер ее блока 
def our_snake(snake_block, snake_list):
   for x in snake_list:
       pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
#функция, которая виализирует текст в игровом окне
def message(msg, msg1, color):#передаем две переменных с текстом и переменную, которая отвечает за цвет
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width /5, dis_height / 3])#делим ширину и высоту экрана что бы расположить надписи по центру
   mesg = font_style.render(msg1, True, color)
   dis.blit(mesg, [dis_width /5, dis_height / 2])
#функция с игровой логикой
def gameLoop():
   #устанавливаем скорость 
   snake_speed = 10
   #создаем 2 переменных bool типа для запуска игрового цикла
   game_over = False
   game_close = False
   #создаем две перемнных в которые сохраним начальные координаты змейки
   x1 = dis_width / 2
   y1 = dis_height / 2
   #Создаём переменную, которой в цикле while будутприсваиваться значения изменения положения змейки по оси х.
   x1_change = 0
   #Создаём переменную, которой в цикле while будутприсваиваться значения изменения положения змейки по оси y.
   y1_change = 0
   #создадим лист в котором будем сохранять действительную величену змейки
   snake_List = []
   #изначальная длинна змейки
   Length_of_snake = 1
   #создаем две переменные в которые сохраняем где будет находиться еда для змейки
   foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
   foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
   #запускаем игровой цикл
   while not game_over:
       #создаем цмкл while, который будет запускаться когда мы вышли за границы карты или врезались в себя 
       while game_close == True:
           #меняем цвет консоли
           dis.fill(black)
           #обращаемся к функции, которая выводит сообщения на экран
           message(proposal,proposal1, red)
           #ввыводим надпись о том сколько у нас очков
           Your_score(Length_of_snake - 1)
           #обновляем наш экран
           pygame.display.update()
           #подклбчаем проверку сообытий
           for event in pygame.event.get():
               #дальше смотрим какое событие происходит от пользователями и проверяем если это событие кнопка нажата
               if event.type == pygame.KEYDOWN:
                   #если это клавиша Q, то останавливаем игровой цикл и выходим из игры
                   if event.key == pygame.K_q:
                       game_over = True
                       game_close = False
                    # если это клавиша C, то мы заново запускаем игру
                   if event.key == pygame.K_c:
                       gameLoop()
        #подклбчаем проверку сообытий
       for event in pygame.event.get():
           # Отслеживание события: "закрыть окно"
           if event.type == pygame.QUIT:
               game_over = True
            #дальше смотрим какое событие происходит от пользователями и проверяем если это событие кнопка нажата
            #настраиваем движение змейки, где шаг изменения = 10 пикселям
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                   x1_change = -snake_block
                   y1_change = 0
               elif event.key == pygame.K_RIGHT:
                   x1_change = snake_block
                   y1_change = 0
               elif event.key == pygame.K_UP:
                   y1_change = -snake_block
                   x1_change = 0
               elif event.key == pygame.K_DOWN:
                   y1_change = snake_block
                   x1_change = 0
        #проверяем что бы змейка не выходила за границы игрового поля, если вышла, то мы выводим сообщение о проигрыше
       if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
           game_close = True
           proposal ="Вы проиграли! Нажмите:"
           proposal1 ='Q - выход / C - повтор'
        #перезаписываем координаты змейки
       x1 += x1_change
       y1 += y1_change
       #какого цвета будет дисплей
       dis.fill(black)
       #отображаем прямоугольк отвечающий за наше яблоко
       pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
       #Создаём список, в котором будет храниться показатель длины змейки при движениях.
       snake_Head = []
       #Добавляем значения в список при изменении по оси х.
       snake_Head.append(x1)
       #Добавляем значения в список при изменении по оси y.
       snake_Head.append(y1)
       #добавляем в лист с действительной величиной длины змейки, список с даныыми длины змейки при движении
       snake_List.append(snake_Head)
       if len(snake_List) > Length_of_snake:
        #Удаляем первый элемент в списке длины змейки, чтобы она не увеличивалась сама по себе при движениях
           del snake_List[0]
        #проверяем не врезалась ли змейка в саму себя
       for x in snake_List[:-1]:
           if x == snake_Head:
               game_close = True
               proposal='Вы врезались в себя!'
               proposal1 ='Q - выход / C - повтор'
        #обращаемся к функции, которая отображает нашу змейку на экрвне
       our_snake(snake_block, snake_List)
       #обращаемся к функции, которая отображает количество очков
       Your_score(Length_of_snake - 1)
       #обновляем экран
       pygame.display.update()
       #проверяем не совпала ли голова змейки с едой
       if x1 == foodx and y1 == foody:
           #увеличиваем скорость змейки на 1
           snake_speed+=1
           #меняем координаты для яблока
           foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
           foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
           #увеличиваем лину змейки
           Length_of_snake += 1
        #просит pygame определить, сколько занимает цикл, а затем сделать паузу, чтобы цикл (целый кадр) длился нужно время.
       clock.tick(snake_speed)
    #выход из игры
   pygame.quit()
#обращаемся к ыункции в которой написана вся игровая логика 
gameLoop()
