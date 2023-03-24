# IMPORTS
import pyxel
import random
import constantes
from plataforma import Plataforma
from mario import Mario
from donkeykong import DonkeyKong
from pauline import Pauline
from barril import Barril
from escaleras import Escaleras
from marcador import Marcador

class Tablero:
    def __init__(self):
        # Creo las plataformas agrupándolas en una lista
        self.listaplataformas = [Plataforma(0, 243, 144), Plataforma(144, 242, 23), Plataforma(167, 241, 23),
                                 Plataforma(190, 240, 23), Plataforma(213, 239, 23), Plataforma(236, 238, 19),
                                 Plataforma(0, 199, 23), Plataforma(23, 201, 23), Plataforma(46, 202, 23),
                                 Plataforma(69, 203, 23), Plataforma(92, 204, 23), Plataforma(115, 205, 23),
                                 Plataforma(138, 206, 23), Plataforma(161, 207, 23), Plataforma(184, 208, 23),
                                 Plataforma(207, 209, 23), Plataforma(16, 171, 19), Plataforma(35, 170, 23),
                                 Plataforma(58, 169, 23), Plataforma(81, 168, 23), Plataforma(104, 167, 23),
                                 Plataforma(127, 166, 17), Plataforma(144, 165, 23), Plataforma(167, 164, 23),
                                 Plataforma(190, 163, 23), Plataforma(213, 162, 23), Plataforma(236, 161, 19),
                                 Plataforma(0, 128, 23), Plataforma(23, 129, 23), Plataforma(46, 130, 23),
                                 Plataforma(69, 131, 23), Plataforma(92, 132, 23), Plataforma(115, 133, 23),
                                 Plataforma(138, 134, 23), Plataforma(161, 135, 23), Plataforma(184, 135, 23),
                                 Plataforma(207, 135, 23), Plataforma(12, 101, 23), Plataforma(35, 100, 23),
                                 Plataforma(58, 99, 23), Plataforma(81, 98, 23), Plataforma(104, 97, 23),
                                 Plataforma(127, 96, 17), Plataforma(144, 95, 23), Plataforma(167, 94, 23),
                                 Plataforma(190, 93, 23),Plataforma(213, 92, 23), Plataforma(236, 91, 19),
                                 Plataforma(0, 60, 144), Plataforma(144, 61, 23), Plataforma(167, 62, 23),
                                 Plataforma(190, 63, 23), Plataforma(213, 64, 23), Plataforma(104, 31, 37)]

        # Creo los objetos
        self.mario = Mario(15, 227)
        self.donkeykong = DonkeyKong(20, 27)
        self.pauline = Pauline(113, 8)
        self.barril1 = Barril(5, 43, 0)
        self.barril2 = Barril(5, 26, 0)
        self.escalera1 = Escaleras(215, 209, 31)
        self.escalera2 = Escaleras(25, 171, 30)
        self.escalera3 = Escaleras(205, 135, 27)
        self.escalera4 = Escaleras(37, 100, 29)
        self.escalera5 = Escaleras(215, 64, 30)
        self.escalera6 = Escaleras(93, 168, 36)
        self.escalera7 = Escaleras(121, 133, 34)
        self.escalera8 = Escaleras(83, 7, 52)
        self.escalera9 = Escaleras(93, 7, 52)
        self.escalera10 = Escaleras(101, 60, 11)
        self.escalera11 = Escaleras(101, 83, 15)
        self.escalera12 = Escaleras(161, 95, 21)
        self.escalera13 = Escaleras(161, 129, 6)
        self.escalera14 = Escaleras(57, 202, 11)
        self.escalera15 = Escaleras(57, 228, 15)
        self.marcador = Marcador(0, 3)

        # Creo la lista que almacenará los barriles
        self.listabarriles = []

        # Creo la lista que almacenará las escaleras que no están rotas
        self.listaescaleras = [self.escalera1, self.escalera2, self.escalera3, self.escalera4, self.escalera5,
                               self.escalera6, self.escalera7, self.escalera8, self.escalera9, self.escalera10,
                               self.escalera11, self.escalera12, self.escalera13, self.escalera14, self.escalera15,]

        # Creo la tupla que almacenará el resto de objetos para poder dibujarlos
        self.tuplaobjetos = [self.donkeykong, self.pauline, self.barril1, self.barril2, self.mario]

        # Variable auxiliar para animación Pauline
        self.auxhelp = False

        # Variables auxiliares para detectar derrota y victoria
        self.auxderrota = False
        self.auxvictoria = False

        # Inicio la pantalla y los métodos update y draw.
        pyxel.init(constantes.WIDTH, constantes.HEIGHT, caption=constantes.CAPTION, fps=constantes.FPS)
        pyxel.run(self.update, self.draw)


    def update(self):
        '''Esta función se ejecuta cada frame'''

        # Condicional que comprueba si se presiona la tecla Q y detiene el programa.
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # Movimiento horizontal de Mario
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1) or pyxel.btnp(pyxel.KEY_D, 1, 1):
            self.mario.rightX(2)
            self.mario.estadosubiendo = False
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1) or pyxel.btnp(pyxel.KEY_A, 1, 1):
            self.mario.leftX(2)
            self.mario.estadosubiendo = False

        # Movimiento vertical de Mario (en escaleras)
        for escalera in self.listaescaleras:
            if self.mario.posX+8 in range(escalera.posX, escalera.posX+7) and self.mario.posY in range(escalera.posY-18, escalera.posY+escalera.sprite[4]-15):
                if pyxel.btnp(pyxel.KEY_UP, 1, 1) or pyxel.btnp(pyxel.KEY_W, 1, 1):
                    self.mario.estadosubiendo = True
                    if pyxel.frame_count % 5 == 0:
                        self.mario.sprite = (0, 80, 16, 16, 16)
                    else:
                        self.mario.sprite = (0, 96, 16, 16, 16)
                    self.mario.upY(1)
                if pyxel.btnp(pyxel.KEY_DOWN, 1, 1) or pyxel.btnp(pyxel.KEY_S, 1, 1):
                    self.mario.estadosubiendo = True
                    if pyxel.frame_count % 5 == 0:
                        self.mario.sprite = (0, 80, 16, 16, 16)
                    else:
                        self.mario.sprite = (0, 96, 16, 16, 16)
                    self.mario.downY(1)

        # Salto de Mario
        if self.mario.estadosalto == False and pyxel.btnp(pyxel.KEY_SPACE) and self.mario.estadosubiendo == False:
            self.mario.posInicialY = self.mario.posY
            self.mario.velocidadsalto = -constantes.CTESALTOMARIO
            self.mario.estadosalto = True

        if self.mario.estadosalto == True:
            if (pyxel.frame_count % constantes.TIEMPOSALTOMARIO) == 0:
                self.mario.velocidadsalto += 1
                self.mario.posY += self.mario.velocidadsalto
                if self.mario.posY >= self.mario.posInicialY:
                    self.mario.posY = self.mario.posInicialY
                    self.mario.estadosalto = False

        # Gravedad y limitador de posición de Mario
        for plataforma in self.listaplataformas:
            if self.mario.estadosubiendo == False and self.mario.estadosalto == False:
                self.mario.gravedad(plataforma.posX, plataforma.posY, plataforma.width)

        # Evitar que Mario entre en el área de Donkey Kong
        if self.mario.posY in range(0, 50) and self.mario.posX < 73:
            self.mario.posX = 73

        # Lanzar barriles cada x frames (Máximo diez en pantalla)
        if (pyxel.frame_count % 75 == 0) and random.randrange(1, 2) == 1:
            barril = Barril(constantes.POSXBARRIL, constantes.POSYBARRIL, 1)
            if len(self.listabarriles) < 10:
                self.listabarriles.append(barril)

        # Movimiento de barriles
        for barril in self.listabarriles:
            barril.movimientoBarril()

        # Gravedad de barriles
        for barril in self.listabarriles:
            barril.sobreplataforma = False
            for plataforma in self.listaplataformas:
                if barril.posX+6 in range(plataforma.posX, plataforma.posX+plataforma.sprite[3]) and barril.posY in range(plataforma.posY-16, plataforma.posY-13) and barril.bajaescaleras == False:
                    barril.posY = plataforma.posY-14
                    barril.sobreplataforma = True

        # Caída de barriles por las escaleras
        for barril in self.listabarriles:
            for escalera in self.listaescaleras:
                if random.randrange(1, 5) == 1 and barril.posY == escalera.posY-14 and barril.posX+7 == escalera.posX:
                    if barril.posY in range(escalera.posY-18, escalera.posY+escalera.sprite[4]):
                        barril.bajaescaleras = True
                if barril.posY == escalera.posY-13:
                    barril.bajaescaleras = False

        # Colision barriles con Mario
        for barril in self.listabarriles:
            if (barril.posX < self.mario.posX + 8 < barril.posX + barril.sprite[3]) and (
                    barril.posY < self.mario.posY + 8 < barril.posY + barril.sprite[4]):
                pyxel.play(0, 0)
                self.marcador.perdervidas()
                self.marcador.puntos = 0
                self.mario.posX = 15
                self.mario.posY = 227
                self.listabarriles = []

        # Salto de barriles
        for barril in self.listabarriles:
            if self.mario.estadosalto == True and self.mario.posX+8 == barril.posX + 7 and self.mario.posY + 16 in range(
                    barril.posY - 60, barril.posY):
                self.marcador.puntossalto()

        # Eliminar barriles cuando llegan al final
        for barril in self.listabarriles:
            if barril.posX == 0 and barril.posY == 229:
                self.listabarriles.remove(barril)

        # Animación de los barriles
        for barril in self.listabarriles:
            if barril.sobreplataforma:
                if pyxel.frame_count % 30 < 15:
                    barril.sprite = (1, 105, 241, 14, 14)
                else:
                    barril.sprite = (1, 57, 241, 14, 14)

        # Animación de Pauline
        if pyxel.frame_count % 100 < 50:
            self.pauline.sprite = (0, 0, 0, 16, 23)
        else:
            self.pauline.sprite = (0, 0, 32, 16, 23)

        if pyxel.frame_count % 175 < 50:
            self.auxhelp = True
        else:
            self.auxhelp = False

        # Animación de Donkey Kong
        if pyxel.frame_count % 125 < 30:
            self.donkeykong.sprite = (0, 26, 48, 47, 32)
        else:
            self.donkeykong.sprite = (0, 26, 0, 47, 32)

        # Derrota - Game Over
        if self.marcador.vidas == 0:
            self.auxderrota = True

        # Victoria - Colisión con Pauline
        if (self.pauline.posX < self.mario.posX + 8 < self.pauline.posX + self.pauline.sprite[3]) and (
                self.pauline.posY < self.mario.posY + 8 < self.pauline.posY + self.pauline.sprite[4]) and (
                self.mario.estadosalto == False):
            self.auxvictoria = True



    def draw(self):
        '''Esta función dibuja las cosas en la pantalla'''

        # Creo la pantalla estableciendo un color de fondo 0-16. 0 es negro
        pyxel.cls(0)

        # Cargo el banco
        pyxel.load("assets/sprites.pyxres")

        # Colocamos las plataformas
        for plataforma in self.listaplataformas:
            pyxel.blt(plataforma.posX, plataforma.posY, plataforma.sprite[0], plataforma.sprite[1],
                      plataforma.sprite[2], plataforma.sprite[3], plataforma.sprite[4], colkey=0)

        # Colocamos las escaleras
        for escalera in self.listaescaleras:
            pyxel.blt(escalera.posX, escalera.posY, escalera.sprite[0], escalera.sprite[1], escalera.sprite[2],
                      escalera.sprite[3], escalera.sprite[4], colkey=0)

        # Dibujamos todos los objetos menos los barriles y el marcador
        for objeto in self.tuplaobjetos:
            pyxel.blt(objeto.posX, objeto.posY, objeto.sprite[0], objeto.sprite[1],
                      objeto.sprite[2], objeto.sprite[3], objeto.sprite[4], colkey=0)

        # Colocamos los barriles
        for barril in self.listabarriles:
            pyxel.blt(barril.posX, barril.posY, barril.sprite[0], barril.sprite[1],
                      barril.sprite[2], barril.sprite[3], barril.sprite[4], colkey=0)

        # Colocamos el marcador de puntos
        pyxel.text(5, 5, "Puntuacion: {}".format(str(self.marcador)), 7)
        # Colocamos el marcador de vidas
        pyxel.text(5, 12, "Vidas: {}".format(str(self.marcador.vidas)), 7)

        # Onomatopeya Help!
        if self.auxhelp:
            pyxel.blt(132, 8, 0, 80, 48, 22, 7, colkey=0)

        # Pantalla de Game Over
        if self.auxderrota:
            pyxel.rect(0, 0, 255, 255, 0)
            pyxel.text(110, 110, "Game Over!", 8)
            pyxel.text(90, 120, "Presiona Q para salir", 7)

        # Pantalla de Victoria
        if self.auxvictoria:
            pyxel.rect(0, 0, 255, 255, 7)
            pyxel.text(85, 110, "Enhorabuena, has ganado!", 12)
            pyxel.text(65, 120, "Tu puntuacion final ha sido: {}".format(str(self.marcador)), 0)

# Inicio el juego
Tablero()

