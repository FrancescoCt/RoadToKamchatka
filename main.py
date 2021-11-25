import pygame

def collisione(missilex, missiley, carro, carro0x, carro0y):
    tolleranza = 2
    carro_lato_dx = carro0x+carro.get_width()-tolleranza
    carro_lato_sx = carro0x + tolleranza
    missile_lato_dx = missilex + missile.get_width()
    missile_lato_sx = missilex
    carro_lato_su = carro0y+tolleranza
    #carro_lato_giu = 290+carro.get_height()-tolleranza
    missile_lato_su = missiley + 50#costante in base al carro
    #missile_lato_giu = self.y+tolleranza+1

    if carro_lato_dx > missile_lato_sx and carro_lato_sx < missile_lato_dx:
        if carro_lato_su < missile_lato_su:
            print("Game over - Score: {}".format(score))
            hai_perso()

#Inizializzo pygame
pygame.init()
pygame.display.set_caption('Road to Kamchatka Lv 1')

#Carico le immagini
sfondo = pygame.image.load('sfondoPix1.jpg')
base = pygame.image.load('basePix.jpg')
carro = pygame.image.load('carro2.png')

elicottero = pygame.image.load('elicottero.png')
missile = pygame.image.load('missile.png')
missile1 = pygame.image.load('missile.png')

pygame.display.set_icon(carro)
gameover = pygame.image.load('gameOver.png')

#Costanti globali
SCHERMO = pygame.display.set_mode((412, 430))
FPS = 50
VEL_AVANZ = 3
FONT = pygame.font.SysFont('Comic Sans Ms', 24, bold = True )

def hai_perso():
    SCHERMO.blit(gameover, (50, 160))
    aggiorna()
    ricominciamo = False
    while not ricominciamo:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE):
                inizializza()
                ricominciamo = True
            if event.type == pygame.QUIT:
                pygame.quit()
def inizializza():
    global carrox, carroy, carro_velx
    global basex, sfondox
    global elicotterox, missilex, missiley, missile1x, missile1y
    global flag, flag1
    global  score
    carrox, carroy = 60, 283
    carro_velx = 0
    basex, sfondox = 0, 0
    elicotterox = 0
    missilex, missiley = 0, 80
    missile1x, missile1y = 0, 80
    flag, flag1 = False, False
    score = 0
def disegna_oggetti():
    #SCHERMO.blit(sfondo, (0, 0)) #sfondo fisso
    #disegno sfondo e personaggio
    SCHERMO.blit(sfondo, (sfondox, 0))
    SCHERMO.blit(carro, (carrox, carroy))
    SCHERMO.blit(base, (basex, 322))
    #dinamica nemici
    SCHERMO.blit(elicottero, (elicotterox, 20))
    if flag == True: SCHERMO.blit(missile, (missilex, missiley))
    if flag1 == True: SCHERMO.blit(missile1, (missile1x, missile1y))
    #segno punteggio
    score_render = FONT.render("Score: "+str(int(score)), 1, (255, 255, 255))
    SCHERMO.blit(score_render, (0, 0))


def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
inizializza()
#Ciclo principale
while True:
    score+=0.005
    basex -= VEL_AVANZ
    sfondox -= VEL_AVANZ*0.5
    if basex < -50: basex = 5
    if sfondox < -500: sfondox = 0

    #Movimento in avanti automatico
    #carro_velx += 0.05
    carrox += carro_velx

    #Movimento elicottero e missili
    elicotterox += 1
    if (elicotterox == 512):
        elicotterox = 0
    elif (elicotterox == 100):
        #512 ):
        missilex = elicotterox
        flag = True
    elif (elicotterox == 200):
        #512 ):
        missile1x = elicotterox
        flag1 = True

    if flag == True:
        missiley += 1
        if missiley == 290:
            missiley = 80
            flag = False
    if flag1 == True:
        missile1y += 1
        if missile1y == 290:
            missile1y = 80
            flag1 = False
    #Gestione collisione
    collisione(missilex, missiley, carro, carrox, carroy)
    collisione(missile1x, missile1y, carro, carrox, carroy)
    #Input da tastiera
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN
            and event.key == pygame.K_UP ):
            carro_velx = +1

        if (event.type == pygame.KEYDOWN
                and event.key == pygame.K_DOWN):
            carro_velx = -1

        #if (event.type == pygame.KEYDOWN
         #       and event.key == pygame.K_SPACE):
          #  carro_velx = -0

        if event.type == pygame.QUIT:
            pygame.quit()
    #Aggiornamento schermo
    disegna_oggetti()
    aggiorna()