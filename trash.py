import pygame
import random
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("청소 게임")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
original_img = pygame.image.load("images\짱구-Photoroom.png").convert_alpha()
cleaner_img = pygame.transform.scale(original_img, (70, 70))  # 원하는 크기로 조절
pygame.mouse.set_visible(False)
trash_img = pygame.image.load("images\초코비누끼-Photoroom.png").convert_alpha()
trash_img = pygame.transform.scale(trash_img, (50, 50)) 

# 쓰레기 리스트
trash_list = []
for _ in range(10):
    x = random.randint(0, 450)
    y = random.randint(0, 450)
    trash_list.append(pygame.Rect(x, y, 50, 50))
score = 0
running = True
while running:
    screen.fill((255, 255, 255))
    # 쓰레기 그리기
    for trash in trash_list:
        screen.blit(trash_img, (trash.x, trash.y))
    # 점수 표시
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(cleaner_img, (mouse_x - cleaner_img.get_width() // 2,
                              mouse_y - cleaner_img.get_height() // 2))
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for trash in trash_list[:]:
                if trash.collidepoint(event.pos):
                    trash_list.remove(trash)
                    score += 1
    pygame.display.update()
    clock.tick(60)
#
#  루프 종료 후 게임 종료
pygame.quit()