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
bg_img = pygame.image.load("images\배경.png").convert()
original_img = pygame.image.load("images\짱구.png").convert_alpha()
cleaner_img = pygame.transform.scale(original_img, (60, 60))
trash_img = pygame.image.load("images\초코비.png").convert_alpha()
trash_img = pygame.transform.scale(trash_img, (50, 50))

pygame.mouse.set_visible(False)

# 쓰레기 위치 생성
trash_list = []
for _ in range(20):
    x = random.randint(0, WIDTH - 50)
    y = random.randint(0, HEIGHT - 50)
    trash_list.append(pygame.Rect(x, y, 50, 50))

# 제한 시간 설정 (초)
time_limit = 20
start_ticks = pygame.time.get_ticks()

score = 0
running = True
while running:
    screen.blit(bg_img, (0, 0))  # 배경 이미지 그리기

    # 남은 시간 계산
    seconds = time_limit - (pygame.time.get_ticks() - start_ticks) // 1000
    if score >= 20:
        end_reason = "clear"
        running = False
    elif seconds <= 0:
        end_reason = "timeout"
        running = False


    # 쓰레기 그리기
    for trash in trash_list:
        screen.blit(trash_img, (trash.x, trash.y))

    # 점수 및 시간 표시
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    time_text = font.render(f"Time: {seconds}", True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))

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

# 게임 종료 화면
screen.fill((255, 255, 255))
if end_reason == "clear":
    end_text = font.render(f"Chocobi collected! : {score}", True, (0, 150, 0))
else:
    end_text = font.render(f"Time's over! score: {score}", True, (150, 0, 0))


text_rect = end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(end_text, text_rect)
pygame.display.update()
pygame.time.wait(3000)

pygame.quit()
