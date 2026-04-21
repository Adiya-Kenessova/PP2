import pygame
from player import MusicPlayer 

pygame.init()
pygame.mixer.init()
#scr
scr = pygame.display.set_mode((400,400))
icon = pygame.image.load('spotify.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Music by Adiya")
clock = pygame.time.Clock()

player=MusicPlayer()

#font
font = pygame.font.SysFont("Arial", 24)
font2 = pygame.font.SysFont("Arial", 24, italic=True)
controls = font.render("P Play | S Stop | N Next | B Back | Q Quit", True, (255,255,255))

cover_img = None
rect = None
current_index = -1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next()

            elif event.key == pygame.K_b:
                player.previous()

            elif event.key == pygame.K_q:
                running = False

    scr.fill((0,186,186))

    #status
    status = "Playing" if player.is_playing else "Stopped"
    if status == "Playing":
        status_text = font.render(f"Status: {status}", True, (0,180,0))
    elif status == "Stopped":
        status_text = font.render(f"Status: {status}", True, (200,100,120))

    #image
    cover_path = player.get_cover()
    cover_img = pygame.image.load(cover_path)
    cover_img = pygame.transform.smoothscale(cover_img, (200, 200))
    rect = cover_img.get_rect()
    rect.center = (200, 200)

    #song
    song_path = player.playlist[player.index]
    song_name = song_path.split("/")[-1].replace(".mp3", "")
    song_text = font2.render(f"{song_name}", True, (255,255,255))

    #progress
    pos = pygame.mixer.music.get_pos()
    current = max(0, pos // 1000)

    minutes = current // 60 
    seconds = current % 60

    time_text_str = f"{minutes:02}:{seconds:02}"

    time_text = font.render(time_text_str, True, (255, 255, 255))
    scr.blit(time_text, (170, 340))

    #blit
    scr.blit(song_text, (110,300))
    scr.blit(controls, (20, 3))
    scr.blit(status_text, (20, 50))
    if cover_img:
        scr.blit(cover_img, rect)

    pygame.draw.line(scr, (225,225,225), (0,40), (400,40), 3) 
    pygame.display.update()
    clock.tick(60)

pygame.quit()