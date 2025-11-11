import pygame
import random

# 초기화
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("초코비 먹고 싶은 짱구")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# 이미지 불러오기
# cleaner.png: 짱구 캐릭터 이미지 (투명 배경)
# trash.png: 쓰레기 이미지
original_img = pygame.image.load("images\cleaner.png").convert_alpha()
cleaner_img = pygame.transform.scale(original_img, (70, 70))  # 짱구 크기 조절
trash_img = pygame.image.load("images\\trash.png").convert_alpha()
trash_img = pygame.transform.scale(trash_img, (65, 65))       # 쓰레기 크기 조절

pygame.mouse.set_visible(False)  # 기본 커서 숨기기

# 쓰레기 위치 생성
trash_list = []
for _ in range(10):
    x = random.randint(0, WIDTH - 50)
    y = random.randint(0, HEIGHT - 50)
    trash_list.append(pygame.Rect(x, y, 50, 50))

score = 0
running = True
while running:
    screen.fill((255, 255, 255))

    # 쓰레기 이미지 그리기
    for trash in trash_list:
        screen.blit(trash_img, (trash.x, trash.y))

    # 점수 표시
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # 짱구 이미지 마우스 위치에 그리기
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


pygame.quit()
