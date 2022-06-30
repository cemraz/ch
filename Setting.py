
class Setting():
    '''Настройки всей игры'''
    def __init__(self):
        #Размеры окна
        self.screen_w = 1600
        self.screen_h = 1000

        self.bg_color = (230, 255, 230)#Цвет фона

        self.beaver_limit = 3#Разрешено смертей бобров

        # Параметры пули
        self.bullet_speed = 50
        self.bullet_w = 3
        self.bullet_h = 15
        self.bullet_color = (15,15,15)
        self.bullets_allowed = 5

        #Параметры белок
        self.fleet_drop_speed = 50
        #Направление движения: self.fleet_direction = 1 -вправо/// = -1 - влево
        self.fleet_direction = 1

