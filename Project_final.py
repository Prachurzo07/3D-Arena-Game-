from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time
import random

_window_created = False 
level=1

def start_level_1():

    # -------------------- CORE VARIABLES --------------------
    global sam_camera_pos, sam_fovY, sam_player_rotation, sam_game_score
    global sam_enemy_count, sam_player_life, sam_enemy_info
    global sam_bullets, sam_enemy_bullets, sam_bullet_counter, sam_enemy_bullet_counter
    global sam_bullet_velocity, sam_enemy_bullet_velocity, sam_bullets_missed
    global sam_enemy_velocity, sam_next_enemy, sam_game_state
    global sam_is_day, sam_sky_color_day, sam_sky_color_night
    global sam_cheat_mode, sam_cheat_start_time, sam_CHEAT_DURATION
    global sam_player_x, sam_player_y, sam_pov
    global sam_dragon, sam_dragon_fireballs, sam_dragon_fireball_counter
    global sam_dragon_speed, sam_dragon_height, sam_dragon_move_interval, sam_dragon_fire_interval
    global sam_dragon_fireball_speed, sam_dragon_gravity
    global sam_ARENA_HALF, sam_ARENA_OUT, sam_TILE_SIZE, sam_TILES_AMOUNT, sam_WALL_H
    global sam_blocks, sam_PLAYER_RADIUS, sam_ENEMY_RADIUS, sam_BULLET_RADIUS
    global sam_player_base_z, sam_player_z
    global sam_jump_active, sam_jump_t0, sam_jump_duration
    global sam_jump_start_x, sam_jump_start_y, sam_jump_start_z
    global sam_jump_target_x, sam_jump_target_y, sam_jump_target_z
    global sam_jump_peak_z, sam_jump_target_block, sam_player_on_block
    global sam_player_coins, sam_coins, sam_coin_counter, sam_coin_spawn_interval, sam_last_coin_spawn, sam_max_coins, sam_AMMO_COST
    global sam_ammo_count, sam_hearts, sam_heart_counter, sam_last_heart_spawn, sam_heart_spawn_interval, sam_max_hearts
    global sam_cars, sam_car_counter, sam_next_car_spawn_time, sam_CAR_SPEED
    global sam_damage_cooldown_active, sam_damage_last_time, sam_DAMAGE_COOLDOWN
    global sam_UI_W, sam_UI_H, sam_WIN_W, sam_WIN_H
    global sam_VEST_X1, sam_VEST_Y1, sam_VEST_X2, sam_VEST_Y2
    global sam_game_start_time
    global sam_flying_active, sam_flying_start_time, sam_FLY_DURATION, sam_FLY_Z_OFFSET
    global level  # for level switching (you already used this)

    sam_camera_pos = (0, 500, 500)
    sam_fovY = 120
    sam_player_rotation = 0
    sam_game_score = 0

    # MODERATE ENEMIES
    sam_enemy_count = 6
    sam_player_life = 40
    sam_enemy_info = {}

    sam_bullets = {}
    sam_enemy_bullets = {}
    sam_bullet_counter = 0
    sam_enemy_bullet_counter = 0

    sam_bullet_velocity = 8
    sam_enemy_bullet_velocity = 5
    sam_bullets_missed = 0

    sam_enemy_velocity = 0.3
    sam_next_enemy = 0
    sam_game_state = "play"

    # -------------------- DAY / NIGHT --------------------
    sam_is_day = True
    sam_sky_color_day = (0.53, 0.81, 0.92)
    sam_sky_color_night = (0.05, 0.05, 0.1)

    # -------------------- CHEAT MODE --------------------
    sam_cheat_mode = "off"
    sam_cheat_start_time = 0.0
    sam_CHEAT_DURATION = 15.0

    sam_player_x = 0
    sam_player_y = 0
    sam_pov = "tpp"

    # -------------------- DRAGON --------------------
    sam_dragon = {}
    sam_dragon_fireballs = {}
    sam_dragon_fireball_counter = 0
    sam_dragon_speed = 2.5
    sam_dragon_height = 600.0
    sam_dragon_move_interval = 3.0
    sam_dragon_fire_interval = 2.0
    sam_dragon_fireball_speed = 12.0
    sam_dragon_gravity = 0.15

    # -------------------- ARENA SIZE --------------------
    sam_ARENA_HALF = 1200.0
    sam_ARENA_OUT = sam_ARENA_HALF + 8.0
    sam_TILE_SIZE = 100.0
    sam_TILES_AMOUNT = 24
    sam_WALL_H = 220.0

    # -------------------- BLOCKS (TREES) --------------------
    sam_blocks = []
    sam_PLAYER_RADIUS = 45
    sam_ENEMY_RADIUS = 40
    sam_BULLET_RADIUS = 8

    # -------------------- PLAYER Z + JUMP --------------------
    sam_player_base_z = 75.0
    sam_player_z = 75.0

    sam_jump_active = False
    sam_jump_t0 = 0.0
    sam_jump_duration = 0.65
    sam_jump_start_x = sam_jump_start_y = sam_jump_start_z = 0.0
    sam_jump_target_x = sam_jump_target_y = sam_jump_target_z = 0.0
    sam_jump_peak_z = 0.0
    sam_jump_target_block = None
    sam_player_on_block = None

    # -------------------- COINS --------------------
    sam_player_coins = 0
    sam_coins = {}
    sam_coin_counter = 0
    sam_coin_spawn_interval = 2.0
    sam_last_coin_spawn = 0.0
    sam_max_coins = 15
    sam_AMMO_COST = 5

    # -------------------- AMMO & HEARTS --------------------
    sam_ammo_count = 20
    sam_hearts = {}
    sam_heart_counter = 0
    sam_last_heart_spawn = 0.0
    sam_heart_spawn_interval = 15.0
    sam_max_hearts = 2

    # -------------------- CARS --------------------
    sam_cars = {}
    sam_car_counter = 0
    sam_next_car_spawn_time = 0.0
    sam_CAR_SPEED = 5.0

    # -------------------- DAMAGE COOLDOWN --------------------
    sam_damage_cooldown_active = False
    sam_damage_last_time = 0.0
    sam_DAMAGE_COOLDOWN = 1.0

    # -------------------- UI --------------------
    sam_UI_W, sam_UI_H = 1000.0, 800.0
    sam_WIN_W, sam_WIN_H = 1200.0, 800.0

    sam_VEST_X1, sam_VEST_Y1 = 850.0, 720.0
    sam_VEST_X2, sam_VEST_Y2 = 990.0, 790.0

    sam_game_start_time = 0.0

    # -------------------- FLY MODE --------------------
    sam_flying_active = False
    sam_flying_start_time = 0.0
    sam_FLY_DURATION = 20.0
    sam_FLY_Z_OFFSET = 25.0

    # ==============================================================================
    # UTILS & HELPERS
    # ==============================================================================

    def flying_is_on():
        global sam_flying_active, sam_flying_start_time
        if not sam_flying_active:
            return False
        if time.time() - sam_flying_start_time > sam_FLY_DURATION:
            sam_flying_active = False
            return False
        return True

    def take_damage(sam_amount):
        global sam_player_life, sam_damage_cooldown_active, sam_damage_last_time
        if sam_damage_cooldown_active:
            if time.time() - sam_damage_last_time < sam_DAMAGE_COOLDOWN:
                return
            else:
                sam_damage_cooldown_active = False

        sam_player_life -= sam_amount
        sam_damage_cooldown_active = True
        sam_damage_last_time = time.time()

    # ==============================================================================
    # DRAWING HELPERS
    # ==============================================================================

    def draw_text(sam_x, sam_y, sam_text, sam_font=GLUT_BITMAP_HELVETICA_18):
        glColor3f(1, 1, 1)
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, sam_UI_W, 0, sam_UI_H)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glRasterPos2f(sam_x, sam_y)
        for sam_ch in sam_text:
            glutBitmapCharacter(sam_font, ord(sam_ch))
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

    def draw_ui_rect(sam_x1, sam_y1, sam_x2, sam_y2, sam_r, sam_g, sam_b):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, sam_UI_W, 0, sam_UI_H)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glColor3f(sam_r, sam_g, sam_b)
        glBegin(GL_QUADS)
        glVertex3f(sam_x1, sam_y1, 0)
        glVertex3f(sam_x2, sam_y1, 0)
        glVertex3f(sam_x2, sam_y2, 0)
        glVertex3f(sam_x1, sam_y2, 0)
        glEnd()
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

    def draw_vest_icon():
        sam_affordable = (sam_player_coins >= sam_AMMO_COST)
        draw_ui_rect(sam_VEST_X1, sam_VEST_Y1, sam_VEST_X2, sam_VEST_Y2, 0.2, 0.2, 0.2)
        if sam_affordable:
            glColor3f(1.0, 1.0, 0.0)
        else:
            glColor3f(0.5, 0.5, 0.5)
        draw_text(sam_VEST_X1 + 10, sam_VEST_Y1 + 40, "BUY BULLETS")
        draw_text(sam_VEST_X1 + 10, sam_VEST_Y1 + 15, f"Cost: {sam_AMMO_COST}")

    def draw_minimap():
        sam_MAP_SIZE = 150.0
        sam_MARGIN = 20.0
        sam_x1, sam_y1 = sam_MARGIN, sam_MARGIN
        sam_x2, sam_y2 = sam_MARGIN + sam_MAP_SIZE, sam_MARGIN + sam_MAP_SIZE

        draw_ui_rect(sam_x1, sam_y1, sam_x2, sam_y2, 0.0, 0.0, 0.0)

        glMatrixMode(GL_PROJECTION); glPushMatrix(); glLoadIdentity()
        gluOrtho2D(0, sam_UI_W, 0, sam_UI_H)
        glMatrixMode(GL_MODELVIEW); glPushMatrix(); glLoadIdentity()

        def world_to_map(sam_wx, sam_wy):
            sam_nx = (sam_wx + sam_ARENA_HALF) / (2 * sam_ARENA_HALF)
            sam_ny = (sam_wy + sam_ARENA_HALF) / (2 * sam_ARENA_HALF)
            sam_mx = sam_x1 + sam_nx * sam_MAP_SIZE
            sam_my = sam_y1 + sam_ny * sam_MAP_SIZE
            return sam_mx, sam_my

        glPointSize(4.0)
        glBegin(GL_POINTS)

        glColor3f(0.0, 1.0, 0.0)
        for sam_b in sam_blocks:
            sam_mx, sam_my = world_to_map(sam_b["x"], sam_b["y"])
            if sam_x1 <= sam_mx <= sam_x2 and sam_y1 <= sam_my <= sam_y2:
                glVertex3f(sam_mx, sam_my, 0)

        glColor3f(1.0, 1.0, 0.0)
        for sam_c in sam_coins.values():
            sam_mx, sam_my = world_to_map(sam_c[0], sam_c[1])
            if sam_x1 <= sam_mx <= sam_x2 and sam_y1 <= sam_my <= sam_y2:
                glVertex3f(sam_mx, sam_my, 0)

        glColor3f(1.0, 0.0, 0.0)
        for sam_h in sam_hearts.values():
            sam_mx, sam_my = world_to_map(sam_h[0], sam_h[1])
            if sam_x1 <= sam_mx <= sam_x2 and sam_y1 <= sam_my <= sam_y2:
                glVertex3f(sam_mx, sam_my, 0)

        glColor3f(1.0, 1.0, 1.0)
        sam_px, sam_py = world_to_map(sam_player_x, sam_player_y)
        glVertex3f(sam_px, sam_py, 0)

        glColor3f(1.0, 0.5, 0.0)
        for sam_c in sam_cars.values():
            sam_mx, sam_my = world_to_map(sam_c["x"], sam_c["y"])
            if sam_x1 <= sam_mx <= sam_x2 and sam_y1 <= sam_my <= sam_y2:
                glVertex3f(sam_mx, sam_my, 0)

        glEnd()
        glPointSize(1.0)

        glColor3f(1, 1, 1)
        sam_line_w = 2.0
        glBegin(GL_QUADS)
        glVertex3f(sam_x1, sam_y1, 0); glVertex3f(sam_x2, sam_y1, 0); glVertex3f(sam_x2, sam_y1 + sam_line_w, 0); glVertex3f(sam_x1, sam_y1 + sam_line_w, 0)
        glVertex3f(sam_x1, sam_y2, 0); glVertex3f(sam_x2, sam_y2, 0); glVertex3f(sam_x2, sam_y2 - sam_line_w, 0); glVertex3f(sam_x1, sam_y2 - sam_line_w, 0)
        glVertex3f(sam_x1, sam_y1, 0); glVertex3f(sam_x1 + sam_line_w, sam_y1, 0); glVertex3f(sam_x1 + sam_line_w, sam_y2, 0); glVertex3f(sam_x1, sam_y2, 0)
        glVertex3f(sam_x2, sam_y1, 0); glVertex3f(sam_x2 - sam_line_w, sam_y1, 0); glVertex3f(sam_x2 - sam_line_w, sam_y2, 0); glVertex3f(sam_x2, sam_y2, 0)
        glEnd()

        glPopMatrix(); glMatrixMode(GL_PROJECTION); glPopMatrix(); glMatrixMode(GL_MODELVIEW)

    def screen_to_ui(sam_mx, sam_my):
        sam_ux = (sam_mx / float(sam_WIN_W)) * sam_UI_W
        sam_uy = sam_UI_H - (sam_my / float(sam_WIN_H)) * sam_UI_H
        return sam_ux, sam_uy

    def game_board(sam_i, sam_j, sam_tiles_amount, sam_x1, sam_y1):
        if sam_i >= sam_tiles_amount:
            return
        if sam_j < sam_tiles_amount:
            if (sam_i + sam_j) % 2 == 0:
                glColor3f(0.20, 0.70, 0.20)
            else:
                glColor3f(0.10, 0.50, 0.10)
            sam_x2, sam_y2 = sam_x1 + sam_TILE_SIZE, sam_y1 + sam_TILE_SIZE
            glVertex3f(sam_x1, sam_y1, 0)
            glVertex3f(sam_x2, sam_y1, 0)
            glVertex3f(sam_x2, sam_y2, 0)
            glVertex3f(sam_x1, sam_y2, 0)
            game_board(sam_i, sam_j + 1, sam_tiles_amount, sam_x1 + sam_TILE_SIZE, sam_y1)
        else:
            game_board(sam_i + 1, 0, sam_tiles_amount, -sam_ARENA_HALF, sam_y1 + sam_TILE_SIZE)

    def draw_floor():
        glBegin(GL_QUADS)
        game_board(0, 0, sam_TILES_AMOUNT, -sam_ARENA_HALF, -sam_ARENA_HALF)
        glEnd()

    def draw_boundary():
        sam_dark = (0.65, 0.16, 0.18)
        sam_light = (0.88, 0.45, 0.46)
        sam_cell_w = 100.0
        sam_cell_h = 55.0
        sam_cols = int((sam_ARENA_HALF * 2) / sam_cell_w)
        sam_rows = max(1, int(sam_WALL_H / sam_cell_h))

        def wall_gen(sam_x_c, sam_y_c, sam_vertical):
            glBegin(GL_QUADS)
            for sam_i in range(sam_cols):
                sam_start = -sam_ARENA_HALF + sam_i * sam_cell_w
                for sam_j in range(sam_rows):
                    sam_z0 = sam_j * sam_cell_h
                    sam_z1 = min(sam_WALL_H, sam_z0 + sam_cell_h)
                    if (sam_i + sam_j) % 2 == 0:
                        glColor3f(*sam_dark)
                    else:
                        glColor3f(*sam_light)
                    if sam_vertical:
                        glVertex3f(sam_x_c, sam_start, sam_z0); glVertex3f(sam_x_c, sam_start + sam_cell_w, sam_z0)
                        glVertex3f(sam_x_c, sam_start + sam_cell_w, sam_z1); glVertex3f(sam_x_c, sam_start, sam_z1)
                    else:
                        glVertex3f(sam_start, sam_y_c, sam_z0); glVertex3f(sam_start + sam_cell_w, sam_y_c, sam_z0)
                        glVertex3f(sam_start + sam_cell_w, sam_y_c, sam_z1); glVertex3f(sam_start, sam_y_c, sam_z1)
            glEnd()

        wall_gen(0, -sam_ARENA_HALF, False)
        wall_gen(0, sam_ARENA_HALF, False)
        wall_gen(-sam_ARENA_HALF, 0, True)
        wall_gen(sam_ARENA_HALF, 0, True)

    def draw_backpack():
        glPushMatrix()
        glColor3f(0.2, 0.2, 0.2)
        glTranslatef(0, -12, 50)
        glScalef(1.2, 0.6, 1.5)
        glutSolidCube(20)
        glPopMatrix()

    def draw_humanoid(sam_body_color, sam_head_color, sam_is_enemy=False, sam_show_spark=False, sam_torso_scale_x=2.0):
        glPushMatrix()
        glScalef(sam_torso_scale_x, 1, 4)
        glColor3f(sam_body_color[0], sam_body_color[1], sam_body_color[2])
        glTranslatef(0, 0, 5)
        glutSolidCube(20)
        glPopMatrix()
        draw_backpack()

        for sam_s in [-1, 1]:
            glColor3f(0.1, 0.1, 0.4)
            glPushMatrix()
            glTranslatef(sam_s * 15, 0, 8)
            glRotatef(180, 1, 0, 0)
            gluCylinder(gluNewQuadric(), 12, 6, 80, 10, 10)
            glPopMatrix()

            glColor3f(1.0, 0.8, 0.7)
            glPushMatrix()
            glTranslatef(sam_s * 25, 0, 50)
            glRotatef(-90, 1, 0, 0)
            gluCylinder(gluNewQuadric(), 10, 5, 50, 10, 10)
            glPopMatrix()

        glPushMatrix()
        glColor3f(sam_head_color[0], sam_head_color[1], sam_head_color[2])
        glTranslatef(0, 0, 85)
        gluSphere(gluNewQuadric(), 20, 20, 20)
        if sam_is_enemy:
            glColor3f(0, 0, 0)
            for sam_s in [-1, 1]:
                glPushMatrix()
                glTranslatef(sam_s * 8, 18, 5)
                glScalef(5, 1, 1)
                glutSolidCube(1)
                glPopMatrix()
        glPopMatrix()

        glPushMatrix()
        glColor3f(0.3, 0.3, 0.3)
        glTranslatef(0, 0, 40)
        glRotatef(-90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 8, 4, 100, 10, 10)
        if sam_show_spark:
            glTranslatef(0, 0, 105)
            for _ in range(10):
                glPushMatrix()
                glRotatef(random.randint(0, 360), 0, 0, 1)
                glTranslatef(random.uniform(0, 10), 0, 0)
                glColor3f(1, random.choice([0, 0.5]), 0)
                gluSphere(gluNewQuadric(), 3, 8, 8)
                glPopMatrix()
        glPopMatrix()

    # --- INDIVIDUAL DRAW FUNCTIONS FOR SORTING ---
    def draw_player_immediate():
        global sam_player_x, sam_player_y, sam_player_rotation, sam_player_z
        glPushMatrix()
        glTranslatef(sam_player_x, sam_player_y, sam_player_z)
        glRotatef(sam_player_rotation, 0, 0, 1)
        draw_humanoid([0.4, 0.5, 0.0], [0.0, 0.0, 0.0], sam_torso_scale_x=2.0)
        glPopMatrix()

    def draw_enemy_immediate(sam_pos, sam_heading, sam_firing):
        glPushMatrix()
        glTranslatef(sam_pos[0], sam_pos[1], 0)
        glTranslatef(0, 0, 75)
        glRotatef(sam_heading, 0, 0, 1)
        draw_humanoid([0.0, 0.0, 0.5], [1.0, 0.8, 0.6], sam_is_enemy=True, sam_show_spark=sam_firing, sam_torso_scale_x=2.0)
        glPopMatrix()

    def draw_tree_immediate(sam_b):
        glPushMatrix()
        glTranslatef(sam_b["x"], sam_b["y"], 0)

        # Trunk
        glColor3f(0.55, 0.27, 0.07)
        glPushMatrix()
        gluCylinder(gluNewQuadric(), 35, 35, 140, 12, 10)
        glPopMatrix()

        # Leaves
        glTranslatef(0, 0, 140)
        glColor3f(0.0, 0.6, 0.0)
        gluCylinder(gluNewQuadric(), 140, 0, 250, 12, 10)

        glPopMatrix()

    def draw_car_immediate(sam_c):
        glPushMatrix()
        glTranslatef(sam_c["x"], sam_c["y"], 50)
        glRotatef(sam_c["heading"], 0, 0, 1)
        glColor3f(0.0, 0.0, 0.0)
        for sam_wx, sam_wy in [(-65, -60), (-65, 60), (65, -60), (65, 60)]:
            glPushMatrix()
            glTranslatef(sam_wx, sam_wy, -35)
            glutSolidCube(25)
            glPopMatrix()
        glColor3f(0.9, 0.1, 0.1)
        glScalef(4.0, 6.0, 3.5)
        glutSolidCube(30)
        glPopMatrix()

    def draw_cap_square(sam_radius, sam_thickness):
        glPushMatrix()
        glScalef(sam_radius * 2.0, sam_radius * 2.0, sam_thickness)
        glutSolidCube(1)
        glPopMatrix()

    def draw_ring_cubes(sam_inner_r, sam_outer_r, sam_thickness, sam_segments=24):
        sam_mid_r = (sam_inner_r + sam_outer_r) * 0.5
        sam_radial = max(0.5, (sam_outer_r - sam_inner_r))
        for sam_i in range(sam_segments):
            sam_ang = (360.0 / sam_segments) * sam_i
            glPushMatrix()
            glRotatef(sam_ang, 0, 0, 1)
            glTranslatef(sam_mid_r, 0, 0)
            glScalef(sam_radial, sam_radial, sam_thickness)
            glutSolidCube(1)
            glPopMatrix()

    # ==============================================================================
    # MATH & LOGIC
    # ==============================================================================

    def manual(sam_y, sam_x):
        if sam_x == 0 and sam_y == 0:
            return 0.0
        return math.atan2(sam_y, sam_x)

    def clamp(sam_v, sam_lo, sam_hi):
        return max(sam_lo, min(sam_v, sam_hi))

    def rect_bounds(sam_b, sam_margin=0.0):
        sam_hw, sam_hl = sam_b["w"] * 0.5, sam_b["l"] * 0.5
        return sam_b["x"] - sam_hw - sam_margin, sam_b["x"] + sam_hw + sam_margin, sam_b["y"] - sam_hl - sam_margin, sam_b["y"] + sam_hl + sam_margin

    def point_in_rect(sam_px, sam_py, sam_minx, sam_maxx, sam_miny, sam_maxy):
        return (sam_minx <= sam_px <= sam_maxx) and (sam_miny <= sam_py <= sam_maxy)

    def point_in_block(sam_px, sam_py, sam_b, sam_margin=0.0):
        sam_minx, sam_maxx, sam_miny, sam_maxy = rect_bounds(sam_b, sam_margin)
        return point_in_rect(sam_px, sam_py, sam_minx, sam_maxx, sam_miny, sam_maxy)

    def segment_intersects_aabb_2d(sam_x0, sam_y0, sam_x1, sam_y1, sam_minx, sam_maxx, sam_miny, sam_maxy):
        sam_dx, sam_dy = sam_x1 - sam_x0, sam_y1 - sam_y0
        sam_p = [-sam_dx, sam_dx, -sam_dy, sam_dy]
        sam_q = [sam_x0 - sam_minx, sam_maxx - sam_x0, sam_y0 - sam_miny, sam_maxy - sam_y0]
        sam_t0, sam_t1 = 0.0, 1.0
        for sam_i in range(4):
            if sam_p[sam_i] == 0:
                if sam_q[sam_i] < 0:
                    return False
            else:
                sam_t = sam_q[sam_i] / sam_p[sam_i]
                if sam_p[sam_i] < 0:
                    if sam_t > sam_t1:
                        return False
                    sam_t0 = max(sam_t0, sam_t)
                else:
                    if sam_t < sam_t0:
                        return False
                    sam_t1 = min(sam_t1, sam_t)
        return sam_t0 <= sam_t1

    def has_clear_shot(sam_ex, sam_ey, sam_px, sam_py):
        for sam_i, sam_b in enumerate(sam_blocks):
            if sam_player_on_block is not None and sam_i == sam_player_on_block:
                continue
            sam_minx, sam_maxx, sam_miny, sam_maxy = rect_bounds(sam_b, sam_margin=10.0)
            if segment_intersects_aabb_2d(sam_ex, sam_ey, sam_px, sam_py, sam_minx, sam_maxx, sam_miny, sam_maxy):
                return False
        return True

    def bullet_hits_block(sam_bx, sam_by, sam_bz):
        for sam_b in sam_blocks:
            if point_in_block(sam_bx, sam_by, sam_b, sam_margin=sam_BULLET_RADIUS):
                if sam_bz <= sam_b["h"] + 5.0:
                    return True
        return False

    def push_player_out_of_blocks():
        global sam_player_x, sam_player_y
        if sam_player_on_block is not None or sam_jump_active:
            return
        for _ in range(6):
            sam_fixed = False
            for sam_b in sam_blocks:
                sam_minx, sam_maxx, sam_miny, sam_maxy = rect_bounds(sam_b, sam_margin=sam_PLAYER_RADIUS)
                if point_in_rect(sam_player_x, sam_player_y, sam_minx, sam_maxx, sam_miny, sam_maxy):
                    sam_d = [
                        abs(sam_player_x - sam_minx),
                        abs(sam_maxx - sam_player_x),
                        abs(sam_player_y - sam_miny),
                        abs(sam_maxy - sam_player_y)
                    ]
                    sam_m = min(sam_d)
                    if sam_m == sam_d[0]:
                        sam_player_x = sam_minx - 1
                    elif sam_m == sam_d[1]:
                        sam_player_x = sam_maxx + 1
                    elif sam_m == sam_d[2]:
                        sam_player_y = sam_miny - 1
                    else:
                        sam_player_y = sam_maxy + 1
                    sam_player_x = clamp(sam_player_x, -sam_ARENA_HALF, sam_ARENA_HALF)
                    sam_player_y = clamp(sam_player_y, -sam_ARENA_HALF, sam_ARENA_HALF)
                    sam_fixed = True
            if not sam_fixed:
                break

    def random_free_spot(sam_margin=60.0, sam_tries=200):
        sam_lim = sam_ARENA_HALF - sam_margin
        for _ in range(sam_tries):
            sam_x, sam_y = random.uniform(-sam_lim, sam_lim), random.uniform(-sam_lim, sam_lim)
            if not any(point_in_block(sam_x, sam_y, sam_b, sam_margin=sam_margin) for sam_b in sam_blocks):
                return sam_x, sam_y
        return 0.0, 0.0

    def init_blocks():
        global sam_blocks
        sam_blocks = []
        sam_limit = int(sam_ARENA_HALF - 150)
        for _ in range(5):
            sam_tries = 0
            while sam_tries < 100:
                sam_tx = random.randint(-sam_limit, sam_limit)
                sam_ty = random.randint(-sam_limit, sam_limit)
                if math.sqrt(sam_tx * sam_tx + sam_ty * sam_ty) < 250:
                    sam_tries += 1
                    continue
                sam_too_close = False
                for sam_b in sam_blocks:
                    sam_dist = math.sqrt((sam_tx - sam_b["x"]) ** 2 + (sam_ty - sam_b["y"]) ** 2)
                    if sam_dist < 500:
                        sam_too_close = True
                        break
                if not sam_too_close:
                    sam_blocks.append({"x": sam_tx, "y": sam_ty, "w": 80, "l": 80, "h": 400})
                    break
                sam_tries += 1

    def start_jump_to(sam_block_id, sam_land_x, sam_land_y, sam_land_z):
        global sam_jump_active, sam_jump_t0, sam_jump_start_x, sam_jump_start_y, sam_jump_start_z
        global sam_jump_target_x, sam_jump_target_y, sam_jump_target_z, sam_jump_peak_z
        sam_jump_active = True
        sam_jump_t0 = time.time()
        sam_jump_start_x, sam_jump_start_y, sam_jump_start_z = sam_player_x, sam_player_y, sam_player_z
        sam_jump_target_x, sam_jump_target_y, sam_jump_target_z = sam_land_x, sam_land_y, sam_land_z
        sam_jump_peak_z = max(sam_jump_start_z, sam_jump_target_z) + 250.0

    def bezier_z(sam_a, sam_b, sam_c, sam_t):
        sam_u = 1.0 - sam_t
        return (sam_u * sam_u * sam_a) + (2 * sam_u * sam_t * sam_b) + (sam_t * sam_t * sam_c)

    def update_jump():
        global sam_jump_active, sam_player_x, sam_player_y, sam_player_z
        if not sam_jump_active:
            return
        sam_t = (time.time() - sam_jump_t0) / sam_jump_duration
        if sam_t >= 1.0:
            sam_player_x, sam_player_y, sam_player_z = sam_jump_target_x, sam_jump_target_y, sam_jump_target_z
            sam_jump_active = False
            if sam_player_on_block is None:
                push_player_out_of_blocks()
            return
        sam_player_x = (1.0 - sam_t) * sam_jump_start_x + sam_t * sam_jump_target_x
        sam_player_y = (1.0 - sam_t) * sam_jump_start_y + sam_t * sam_jump_target_y
        sam_player_z = bezier_z(sam_jump_start_z, sam_jump_peak_z, sam_jump_target_z, sam_t)

    # -------------------- CARS --------------------
    def spawn_car():
        global sam_car_counter, sam_player_x, sam_player_y, sam_next_car_spawn_time
        if len(sam_cars) >= 1:
            return

        sam_side = random.randint(0, 3)
        sam_margin = 50.0
        if sam_side == 0:
            sam_x, sam_y = -sam_ARENA_HALF + sam_margin, random.uniform(-sam_ARENA_HALF, sam_ARENA_HALF)
        elif sam_side == 1:
            sam_x, sam_y = sam_ARENA_HALF - sam_margin, random.uniform(-sam_ARENA_HALF, sam_ARENA_HALF)
        elif sam_side == 2:
            sam_x, sam_y = random.uniform(-sam_ARENA_HALF, sam_ARENA_HALF), -sam_ARENA_HALF + sam_margin
        else:
            sam_x, sam_y = random.uniform(-sam_ARENA_HALF, sam_ARENA_HALF), sam_ARENA_HALF - sam_margin

        sam_dx, sam_dy = sam_player_x - sam_x, sam_player_y - sam_y
        sam_dist = (sam_dx * sam_dx + sam_dy * sam_dy) ** 0.5
        if sam_dist == 0:
            sam_dist = 1
        sam_vx, sam_vy = (sam_dx / sam_dist) * sam_CAR_SPEED, (sam_dy / sam_dist) * sam_CAR_SPEED
        sam_heading = -math.degrees(math.atan2(sam_dx, sam_dy))
        sam_car_counter += 1
        sam_cars[sam_car_counter] = {"x": sam_x, "y": sam_y, "vx": sam_vx, "vy": sam_vy, "heading": sam_heading}

    def update_cars():
        global sam_player_coins, sam_next_car_spawn_time

        if len(sam_cars) < 1:
            if sam_next_car_spawn_time == 0.0:
                sam_next_car_spawn_time = time.time() + 2.0
            if time.time() > sam_next_car_spawn_time:
                spawn_car()

        sam_rem = []
        for sam_k, sam_c in sam_cars.items():
            sam_hit_wall = False
            for sam_b in sam_blocks:
                if point_in_block(sam_c["x"], sam_c["y"], sam_b, sam_margin=50.0):
                    sam_hit_wall = True
                    break
            if sam_hit_wall:
                sam_rem.append(sam_k)
                sam_next_car_spawn_time = time.time() + random.uniform(3.0, 6.0)
                continue

            sam_c["x"] += sam_c["vx"]
            sam_c["y"] += sam_c["vy"]
            if abs(sam_c["x"]) > sam_ARENA_OUT or abs(sam_c["y"]) > sam_ARENA_OUT:
                sam_player_coins += 1
                sam_next_car_spawn_time = time.time() + random.uniform(3.0, 6.0)
                sam_rem.append(sam_k)
                continue

            if abs(sam_player_x - sam_c["x"]) < 100 and abs(sam_player_y - sam_c["y"]) < 100:
                if sam_player_z < 90.0:
                    # ONLY IMMUNITY IN CHEAT MODE: car won't damage player
                    if sam_cheat_mode == "off":
                        take_damage(2)
                        sam_next_car_spawn_time = time.time() + random.uniform(3.0, 6.0)
                        sam_rem.append(sam_k)
                    else:
                        pass

        for sam_k in sam_rem:
            if sam_k in sam_cars:
                del sam_cars[sam_k]

    # -------------------- COINS + HEARTS --------------------
    def draw_coins():
        sam_spin = (time.time() * 160.0) % 360.0
        sam_bob = math.sin(time.time() * 2.2) * 3.5
        glColor3f(1.0, 0.85, 0.10)
        for sam_c in sam_coins.values():
            glPushMatrix()
            glTranslatef(sam_c[0], sam_c[1], 40.0 + sam_bob)
            glRotatef(sam_spin, 0, 0, 1)
            glRotatef(90, 1, 0, 0)
            draw_ring_cubes(10.0, 18.0, 2.5)
            glPopMatrix()

    def draw_hearts():
        sam_spin = (time.time() * 100.0) % 360.0
        sam_bob = math.sin(time.time() * 3.0) * 3.0
        glColor3f(1.0, 0.0, 0.0)
        for sam_h in sam_hearts.values():
            glPushMatrix()
            glTranslatef(sam_h[0], sam_h[1], 40.0 + sam_bob)
            glRotatef(sam_spin, 0, 0, 1)
            glScalef(15, 15, 15)
            glRotatef(45, 0, 1, 0)
            glRotatef(45, 1, 0, 0)
            glutSolidCube(1)
            glPopMatrix()

    def spawn_coin():
        global sam_coin_counter
        sam_x, sam_y = random_free_spot(sam_margin=70.0)
        sam_coin_counter += 1
        sam_coins[sam_coin_counter] = [sam_x, sam_y]

    def spawn_heart():
        global sam_heart_counter
        sam_x, sam_y = random_free_spot(sam_margin=70.0)
        sam_heart_counter += 1
        sam_hearts[sam_heart_counter] = [sam_x, sam_y]

    def collect_pickups():
        global sam_player_coins, sam_player_life
        if (sam_player_z > sam_player_base_z + 10.0) and (not flying_is_on()):
            return
        sam_rem = []
        for sam_k, sam_c in sam_coins.items():
            if (sam_player_x - sam_c[0]) ** 2 + (sam_player_y - sam_c[1]) ** 2 <= 55 ** 2:
                sam_player_coins += 1
                sam_rem.append(sam_k)
        for sam_k in sam_rem:
            del sam_coins[sam_k]

        sam_rem2 = []
        for sam_k, sam_h in sam_hearts.items():
            if (sam_player_x - sam_h[0]) ** 2 + (sam_player_y - sam_h[1]) ** 2 <= 55 ** 2:
                sam_player_life += 2
                sam_rem2.append(sam_k)
        for sam_k in sam_rem2:
            del sam_hearts[sam_k]

    # ==============================================================================
    # GAME STATE CONTROL
    # ==============================================================================

    def restart_game():
        global sam_pov, sam_player_x, sam_player_y, sam_camera_pos, sam_player_rotation, sam_game_score, sam_player_life
        global sam_enemy_info, sam_bullets, sam_enemy_bullets, sam_bullet_counter, sam_enemy_bullet_counter, sam_bullets_missed
        global sam_game_state, sam_cheat_mode, sam_cheat_start_time, sam_player_base_z, sam_player_z, sam_next_enemy
        global sam_dragon, sam_dragon_fireballs, sam_dragon_fireball_counter
        global sam_jump_active, sam_player_on_block, sam_jump_target_block
        global sam_player_coins, sam_coins, sam_coin_counter, sam_last_coin_spawn
        global sam_ammo_count, sam_damage_cooldown_active
        global sam_cars, sam_car_counter, sam_next_car_spawn_time
        global sam_hearts, sam_heart_counter, sam_last_heart_spawn
        global sam_game_start_time, sam_flying_active
        global sam_is_day

        sam_camera_pos = (0, 500, 500)
        sam_player_rotation = 0
        sam_game_score = 0
        sam_player_life = 40
        sam_enemy_info = {}
        sam_bullets = {}
        sam_enemy_bullets = {}
        sam_bullet_counter = 0
        sam_enemy_bullet_counter = 0
        sam_bullets_missed = 0
        sam_next_enemy = 0
        sam_game_state = "play"
        sam_cheat_mode = "off"
        sam_cheat_start_time = 0.0
        sam_player_x = 0
        sam_player_y = 0
        sam_pov = "tpp"
        sam_player_base_z = 75.0
        sam_player_z = 75.0
        sam_jump_active = False
        sam_player_on_block = None
        sam_jump_target_block = None
        sam_player_coins = 0
        sam_coins = {}
        sam_coin_counter = 0
        sam_ammo_count = 20
        sam_cars = {}
        sam_car_counter = 0
        sam_next_car_spawn_time = time.time() + 7.0
        sam_hearts = {}
        sam_heart_counter = 0
        sam_damage_cooldown_active = False
        sam_last_coin_spawn = time.time()
        sam_last_heart_spawn = time.time()
        sam_game_start_time = time.time()
        sam_flying_active = False
        sam_is_day = True
        init_blocks()
        init_dragon()

    def try_buy_ammo():
        global sam_player_coins, sam_ammo_count
        if sam_player_coins >= sam_AMMO_COST:
            sam_player_coins -= sam_AMMO_COST
            sam_ammo_count += 5
            print("BOUGHT BULLETS!")
        else:
            print("NOT ENOUGH COINS!")

    # -------------------- INPUT --------------------
    def specialKeyListener_1(sam_key, sam_x, sam_y):
        global sam_camera_pos
        sam_cx, sam_cy, sam_cz = sam_camera_pos
        if sam_key == GLUT_KEY_UP:
            sam_cz += 5
        if sam_key == GLUT_KEY_DOWN:
            sam_cz -= 5

        sam_res = (sam_cx ** 2 + sam_cy ** 2) ** 0.5
        sam_ang = manual(sam_cy, sam_cx)

        if sam_key == GLUT_KEY_LEFT:
            sam_ang -= 0.05
        if sam_key == GLUT_KEY_RIGHT:
            sam_ang += 0.05

        sam_camera_pos = (sam_res * math.cos(sam_ang), sam_res * math.sin(sam_ang), sam_cz)
        glutPostRedisplay()

    def keyboardListener_1(sam_key, sam_x, sam_y):
        global sam_player_x, sam_player_y, sam_player_rotation, sam_cheat_mode, sam_cheat_start_time, sam_game_state
        global sam_jump_active, sam_player_on_block, sam_flying_active, sam_flying_start_time
        global sam_is_day, level

        if sam_key == b'n' and level == 1:
            # IMPORTANT: you already use this. Keep your own start_level2() outside.
            start_level_2()

        if sam_game_state == "play":
            sam_speed = 12
            if sam_cheat_mode == "on":
                sam_speed = 6
            if sam_jump_active:
                glutPostRedisplay()
                return

            if sam_key == b'm':
                sam_is_day = not sam_is_day
                glutPostRedisplay()
                return

            if sam_key == b'f':
                sam_flying_active = True
                sam_flying_start_time = time.time()
                sam_player_on_block = None
                glutPostRedisplay()
                return

            if sam_key == b'j':
                start_jump_to(None, sam_player_x, sam_player_y, sam_player_base_z)
                glutPostRedisplay()
                return

            sam_old_x, sam_old_y = sam_player_x, sam_player_y
            if sam_key == b'w':
                sam_player_x += sam_speed * math.sin(math.radians(-sam_player_rotation))
                sam_player_y += sam_speed * math.cos(math.radians(-sam_player_rotation))
            if sam_key == b's':
                sam_player_x -= sam_speed * math.sin(math.radians(-sam_player_rotation))
                sam_player_y -= sam_speed * math.cos(math.radians(-sam_player_rotation))

            sam_player_x = clamp(sam_player_x, -sam_ARENA_HALF, sam_ARENA_HALF)
            sam_player_y = clamp(sam_player_y, -sam_ARENA_HALF, sam_ARENA_HALF)

            if sam_player_on_block is None:
                sam_collided = False
                for sam_b in sam_blocks:
                    if point_in_block(sam_player_x, sam_player_y, sam_b, sam_margin=sam_PLAYER_RADIUS):
                        sam_collided = True
                        break
                if sam_collided:
                    sam_player_x, sam_player_y = sam_old_x, sam_old_y
                push_player_out_of_blocks()

            if sam_key == b'd':
                sam_player_rotation -= 8
            if sam_key == b'a':
                sam_player_rotation += 8

            if sam_key == b'c':
                if sam_cheat_mode == "off":
                    sam_cheat_mode = "on"
                    sam_cheat_start_time = time.time()
                    # keep your existing behavior
                    sam_bullets.clear()
                    sam_enemy_bullets.clear()
                else:
                    sam_cheat_mode = "off"

        if sam_key == b'r' and (sam_game_state == "over" or sam_game_state == "win"):
            restart_game()

        glutPostRedisplay()

    def mouseListener_1(sam_button, sam_state, sam_x, sam_y):
        global sam_pov, sam_bullets, sam_bullet_counter, sam_player_rotation
        global sam_player_z, sam_ammo_count, sam_game_state, sam_camera_pos

        if sam_state != GLUT_DOWN:
            return

        sam_ux, sam_uy = screen_to_ui(sam_x, sam_y)

        if sam_button == GLUT_LEFT_BUTTON and sam_game_state == "play":
            if (sam_VEST_X1 <= sam_ux <= sam_VEST_X2) and (sam_VEST_Y1 <= sam_uy <= sam_VEST_Y2):
                try_buy_ammo()
                glutPostRedisplay()
                return

    
        if sam_button == GLUT_LEFT_BUTTON and sam_game_state == "play":
            if sam_ammo_count > 0:
                sam_ammo_count -= 1
                sam_bullet_counter += 1
                sam_rad = math.radians(-sam_player_rotation)
                sam_bullets[sam_bullet_counter] = [
                    sam_player_x, sam_player_y, sam_player_z + 35.0,
                    sam_bullet_velocity * math.sin(sam_rad), sam_bullet_velocity * math.cos(sam_rad)
                ]

        if sam_button == GLUT_RIGHT_BUTTON and sam_game_state == "play":
            sam_pov = "fpp" if sam_pov == "tpp" else "tpp"
            if sam_pov == "tpp":
                sam_camera_pos = (0, 500, 500)

        glutPostRedisplay()

    # -------------------- CAMERA --------------------
    def setupCamera():
        global sam_player_x, sam_player_y, sam_player_rotation, sam_camera_pos, sam_pov, sam_player_z
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(sam_fovY, 1.25, 0.1, 4000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        if sam_pov == "tpp":
            sam_x, sam_y, sam_z = sam_camera_pos
            gluLookAt(sam_x, sam_y, sam_z, 0, 0, 0, 0, 0, 1)
        else:
            sam_rad = math.radians(-sam_player_rotation)
            sam_eye_x = sam_player_x
            sam_eye_y = sam_player_y
            sam_eye_z = sam_player_z + 125.0
            sam_target_x = sam_eye_x + math.sin(sam_rad) * 120.0
            sam_target_y = sam_eye_y + math.cos(sam_rad) * 120.0
            sam_target_z = sam_eye_z - 40.0
            gluLookAt(sam_eye_x, sam_eye_y, sam_eye_z, sam_target_x, sam_target_y, sam_target_z, 0, 0, 1)

    # -------------------- BULLETS --------------------
    def draw_bullet():
        glPushMatrix()

        def draw_cyl(sam_x, sam_y, sam_z, sam_vx, sam_vy, sam_radius, sam_length):
            sam_ang = math.degrees(math.atan2(sam_vx, sam_vy))
            glPushMatrix()
            glTranslatef(sam_x, sam_y, sam_z)
            glRotatef(sam_ang, 0, 0, 1)
            glRotatef(90, 1, 0, 0)
            sam_q = gluNewQuadric()
            gluCylinder(sam_q, sam_radius, sam_radius, sam_length, 12, 2)
            glColor3f(0.75, 0.75, 0.80)
            draw_cap_square(sam_radius, 0.8)
            glTranslatef(0, 0, sam_length)
            draw_cap_square(sam_radius, 0.8)
            glPopMatrix()

        glColor3f(0.80, 0.80, 0.86)
        for sam_b in sam_bullets.values():
            draw_cyl(sam_b[0], sam_b[1], sam_b[2], sam_b[3], sam_b[4], 5.0, 22.0)

        glColor3f(0.65, 0.65, 0.70)
        for sam_eb in sam_enemy_bullets.values():
            draw_cyl(sam_eb[0], sam_eb[1], sam_eb[2], sam_eb[3], sam_eb[4], 4.5, 20.0)

        glPopMatrix()

    def player_enemy_interaction():
        global sam_enemy_info, sam_enemy_bullets, sam_enemy_bullet_counter
        sam_curr = time.time()
        for sam_k, sam_v in sam_enemy_info.items():
            sam_ex, sam_ey, sam_ez = sam_v["pos"]
            sam_v["is_firing"] = False

            sam_rad_move = math.radians(sam_v["heading"])
            sam_nx = sam_ex + sam_enemy_velocity * math.sin(sam_rad_move)
            sam_ny = sam_ey + sam_enemy_velocity * math.cos(sam_rad_move)

            if abs(sam_nx) > sam_ARENA_HALF or abs(sam_ny) > sam_ARENA_HALF:
                sam_v["heading"] = random.uniform(0, 360)
                continue

            sam_blocked = False
            for sam_b in sam_blocks:
                if point_in_block(sam_nx, sam_ny, sam_b, sam_margin=sam_ENEMY_RADIUS):
                    sam_blocked = True
                    break
            if sam_blocked:
                sam_v["heading"] = random.uniform(0, 360)
                continue

            sam_v["pos"] = (sam_nx, sam_ny, sam_ez)


            sam_dist = math.sqrt((sam_nx - sam_player_x) ** 2 + (sam_ny - sam_player_y) ** 2)
            if sam_dist < 450 and has_clear_shot(sam_nx, sam_ny, sam_player_x, sam_player_y):
                sam_v["heading"] = -math.degrees(math.atan2(sam_player_x - sam_nx, sam_player_y - sam_ny))
                if sam_curr - sam_v["last_fire"] > 1.2:
                    sam_v["is_firing"] = True
                    sam_enemy_bullet_counter += 1
                    sam_rad_fire = math.radians(-sam_v["heading"])
                    sam_enemy_bullets[sam_enemy_bullet_counter] = [
                        sam_nx, sam_ny, 110.0, 6 * math.sin(sam_rad_fire), 6 * math.cos(sam_rad_fire)
                    ]
                    sam_v["last_fire"] = sam_curr

    def render_bullet():
        global sam_bullets, sam_enemy_bullets, sam_bullets_missed, sam_enemy_info, sam_game_score

        sam_rem_b = []
        for sam_k, sam_v in sam_bullets.items():
            sam_v[0] += sam_v[3]
            sam_v[1] += sam_v[4]
            if abs(sam_v[0]) > sam_ARENA_HALF or abs(sam_v[1]) > sam_ARENA_HALF:
                sam_rem_b.append(sam_k)
                sam_bullets_missed += 1
                continue
            if bullet_hits_block(sam_v[0], sam_v[1], sam_v[2]):
                sam_rem_b.append(sam_k)
                continue
            for sam_ek, sam_ev in list(sam_enemy_info.items()):
                if ((sam_v[0] - sam_ev["pos"][0]) ** 2 + (sam_v[1] - sam_ev["pos"][1]) ** 2) <= 50 ** 2:
                    sam_game_score += 1
                    sam_rem_b.append(sam_k)
                    del sam_enemy_info[sam_ek]
                    break

        for sam_k in sam_rem_b:
            if sam_k in sam_bullets:
                del sam_bullets[sam_k]

        sam_rem_eb = []
        for sam_k, sam_v in sam_enemy_bullets.items():
            sam_v[0] += sam_v[3]
            sam_v[1] += sam_v[4]
            if abs(sam_v[0]) > sam_ARENA_HALF or abs(sam_v[1]) > sam_ARENA_HALF:
                sam_rem_eb.append(sam_k)
                continue
            if bullet_hits_block(sam_v[0], sam_v[1], sam_v[2]):
                sam_rem_eb.append(sam_k)
                continue
            if ((sam_v[0] - sam_player_x) ** 2 + (sam_v[1] - sam_player_y) ** 2) <= 45 ** 2:
                if sam_player_z <= sam_v[2] <= (sam_player_z + 150.0):
                    take_damage(1)
                    sam_rem_eb.append(sam_k)

        for sam_k in sam_rem_eb:
            if sam_k in sam_enemy_bullets:
                del sam_enemy_bullets[sam_k]

    def render_enemy_spawn():
        global sam_enemy_info, sam_next_enemy
        sam_spawn_lim = int(sam_ARENA_HALF - 50)
        while len(sam_enemy_info) < sam_enemy_count:
            sam_tx = random.randint(-sam_spawn_lim, sam_spawn_lim)
            sam_ty = random.randint(-sam_spawn_lim, sam_spawn_lim)
            if math.sqrt((sam_tx - sam_player_x) ** 2 + (sam_ty - sam_player_y) ** 2) <= 300:
                continue
            sam_bad = False
            for sam_b in sam_blocks:
                if point_in_block(sam_tx, sam_ty, sam_b, sam_margin=sam_ENEMY_RADIUS + 15):
                    sam_bad = True
                    break
            if sam_bad:
                continue
            sam_enemy_info[sam_next_enemy] = {
                "pos": (sam_tx, sam_ty, 0),
                "heading": random.uniform(0, 360),
                "last_fire": 0,
                "is_firing": False
            }
            sam_next_enemy += 1

    # -------------------- DRAGON --------------------
    def init_dragon():
        global sam_dragon, sam_dragon_fireballs, sam_dragon_fireball_counter
        sam_dragon_fireballs = {}
        sam_dragon_fireball_counter = 0
        sam_lim = int(sam_ARENA_HALF - 50)
        sam_x = random.randint(-sam_lim, sam_lim)
        sam_y = random.randint(-sam_lim, sam_lim)
        sam_z = sam_dragon_height
        sam_dragon = {
            "pos": [float(sam_x), float(sam_y), float(sam_z)],
            "target": [float(random.randint(-sam_lim, sam_lim)), float(random.randint(-sam_lim, sam_lim)), float(sam_z)],
            "last_move": time.time(),
            "last_fire": time.time()
        }

    def update_dragon():
        if not sam_dragon:
            init_dragon()
            return
        sam_now = time.time()
        sam_lim = int(sam_ARENA_HALF - 50)
        if sam_now - sam_dragon["last_move"] > sam_dragon_move_interval:
            sam_dragon["target"] = [float(random.randint(-sam_lim, sam_lim)), float(random.randint(-sam_lim, sam_lim)), sam_dragon_height]
            sam_dragon["last_move"] = sam_now

        sam_px, sam_py, sam_pz = sam_dragon["pos"]
        sam_tx, sam_ty, sam_tz = sam_dragon["target"]
        sam_dx, sam_dy = sam_tx - sam_px, sam_ty - sam_py
        sam_dist = (sam_dx * sam_dx + sam_dy * sam_dy) ** 0.5
        if sam_dist > 0.001:
            sam_step = min(sam_dragon_speed, sam_dist)
            sam_dragon["pos"][0] = sam_px + (sam_dx / sam_dist) * sam_step
            sam_dragon["pos"][1] = sam_py + (sam_dy / sam_dist) * sam_step

    def spawn_dragon_fireball():
        global sam_dragon_fireball_counter
        sam_dragon_fireball_counter += 1
        sam_sx, sam_sy, sam_sz = sam_dragon["pos"]
        sam_tx = sam_player_x + random.uniform(-80, 80)
        sam_ty = sam_player_y + random.uniform(-80, 80)
        sam_dx, sam_dy, sam_dz = sam_tx - sam_sx, sam_ty - sam_sy, 90.0 - sam_sz
        sam_dist = (sam_dx * sam_dx + sam_dy * sam_dy + sam_dz * sam_dz) ** 0.5
        if sam_dist == 0:
            sam_dist = 1
        sam_dragon_fireballs[sam_dragon_fireball_counter] = [
            sam_sx, sam_sy, sam_sz,
            (sam_dx / sam_dist) * sam_dragon_fireball_speed,
            (sam_dy / sam_dist) * sam_dragon_fireball_speed,
            (sam_dz / sam_dist) * sam_dragon_fireball_speed
        ]

    def update_dragon_fireballs():
        global sam_dragon_fireballs
        if not sam_dragon:
            return
        sam_now = time.time()
        if sam_now - sam_dragon["last_fire"] > sam_dragon_fire_interval:
            spawn_dragon_fireball()
            sam_dragon["last_fire"] = sam_now

        sam_to_rem = []
        for sam_k, sam_fb in sam_dragon_fireballs.items():
            sam_fb[5] -= sam_dragon_gravity
            sam_fb[0] += sam_fb[3]
            sam_fb[1] += sam_fb[4]
            sam_fb[2] += sam_fb[5]
            if abs(sam_fb[0]) > sam_ARENA_OUT or abs(sam_fb[1]) > sam_ARENA_OUT or sam_fb[2] <= 0:
                sam_to_rem.append(sam_k)
                continue
            if ((sam_fb[0] - sam_player_x) ** 2 + (sam_fb[1] - sam_player_y) ** 2) <= 45 ** 2 and sam_fb[2] <= 170:
                take_damage(1)
                sam_to_rem.append(sam_k)
        for sam_k in sam_to_rem:
            del sam_dragon_fireballs[sam_k]

    def draw_dragon():
        if not sam_dragon:
            return
        sam_x, sam_y, sam_z = sam_dragon["pos"]
        glPushMatrix()
        glTranslatef(sam_x, sam_y, sam_z)
        glColor3f(1.0, 0.45, 0.0)
        gluSphere(gluNewQuadric(), 28, 18, 18)
        glPushMatrix()
        glTranslatef(0, 35, 10)
        glColor3f(1.0, 0.55, 0.0)
        gluSphere(gluNewQuadric(), 16, 14, 14)
        glPopMatrix()
        glColor3f(0.95, 0.35, 0.0)
        glPushMatrix()
        glTranslatef(-55, 0, 0)
        glScalef(110, 2, 35)
        glutSolidCube(1)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(55, 0, 0)
        glScalef(110, 2, 35)
        glutSolidCube(1)
        glPopMatrix()
        glPopMatrix()

    def draw_dragon_fireballs():
        glColor3f(1.0, 0.45, 0.0)
        for sam_fb in sam_dragon_fireballs.values():
            glPushMatrix()
            glTranslatef(sam_fb[0], sam_fb[1], sam_fb[2])
            gluSphere(gluNewQuadric(), 10, 10, 10)
            glPopMatrix()

    # -------------------- LOOP --------------------
    def idle_1():
        global sam_game_state, sam_player_life, sam_bullets_missed, sam_cheat_mode, sam_cheat_start_time
        global sam_last_coin_spawn, sam_last_heart_spawn, sam_player_z

        if sam_player_life <= 0 or sam_bullets_missed >= 50:
            sam_game_state = "over"
        if sam_game_score >= 10:
            sam_game_state = "win"

        if sam_game_state == "play":
            if sam_cheat_mode == "on" and (time.time() - sam_cheat_start_time > sam_CHEAT_DURATION):
                sam_cheat_mode = "off"

            update_jump()

            if (not sam_jump_active) and flying_is_on():
                sam_player_z = sam_player_base_z + sam_FLY_Z_OFFSET
            elif (not sam_jump_active) and (sam_player_on_block is None):
                sam_player_z = sam_player_base_z

            if (not sam_jump_active) and (sam_player_on_block is not None):
                sam_b = sam_blocks[sam_player_on_block]
                sam_minx, sam_maxx, sam_miny, sam_maxy = rect_bounds(sam_b, sam_margin=-10.0)
                if not point_in_rect(sam_player_x, sam_player_y, sam_minx, sam_maxx, sam_miny, sam_maxy):
                    start_jump_to(None, sam_player_x, sam_player_y, sam_player_base_z)

            render_bullet()
            render_enemy_spawn()
            player_enemy_interaction()
            update_dragon()
            update_dragon_fireballs()
            push_player_out_of_blocks()

            sam_now = time.time()
            if (sam_now - sam_last_coin_spawn) > sam_coin_spawn_interval and len(sam_coins) < sam_max_coins:
                spawn_coin()
                sam_last_coin_spawn = sam_now

            update_cars()

            if (sam_now - sam_last_heart_spawn) > sam_heart_spawn_interval and len(sam_hearts) < sam_max_hearts:
                spawn_heart()
                sam_last_heart_spawn = sam_now

            collect_pickups()

        glutPostRedisplay()

    def draw_sky():
        if sam_is_day:
            sam_c = sam_sky_color_day
        else:
            sam_c = sam_sky_color_night
        glPushMatrix()
        if sam_pov == "tpp":
            glTranslatef(sam_camera_pos[0], sam_camera_pos[1], sam_camera_pos[2])
        else:
            glTranslatef(sam_player_x, sam_player_y, sam_player_z)
        glColor3f(sam_c[0], sam_c[1], sam_c[2])
        gluSphere(gluNewQuadric(), 3500, 12, 12)
        glPopMatrix()

    # -------------------- RENDER --------------------
    def showScreen_1():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glViewport(0, 0, int(sam_WIN_W), int(sam_WIN_H))
        setupCamera()

        draw_sky()
        draw_floor()
        draw_boundary()

        if sam_game_state == "play":
            draw_coins()
            draw_hearts()
            draw_bullet()
            draw_dragon()
            draw_dragon_fireballs()

            if sam_pov == "tpp":
                sam_cx, sam_cy, sam_cz = sam_camera_pos
            else:
                sam_cx, sam_cy, sam_cz = sam_player_x, sam_player_y, sam_player_z

            sam_render_list = []
            for sam_b in sam_blocks:
                sam_dist = (sam_b["x"] - sam_cx) ** 2 + (sam_b["y"] - sam_cy) ** 2
                sam_render_list.append((sam_dist, draw_tree_immediate, (sam_b,)))

            for sam_v in sam_enemy_info.values():
                sam_pos = sam_v["pos"]
                sam_dist = (sam_pos[0] - sam_cx) ** 2 + (sam_pos[1] - sam_cy) ** 2
                sam_render_list.append((sam_dist, draw_enemy_immediate, (sam_pos, sam_v["heading"], sam_v["is_firing"])))

            for sam_c in sam_cars.values():
                sam_dist = (sam_c["x"] - sam_cx) ** 2 + (sam_c["y"] - sam_cy) ** 2
                sam_render_list.append((sam_dist, draw_car_immediate, (sam_c,)))

            sam_p_dist = (sam_player_x - sam_cx) ** 2 + (sam_player_y - sam_cy) ** 2
            sam_render_list.append((sam_p_dist, draw_player_immediate, ()))

            sam_render_list.sort(key=lambda x: x[0], reverse=True)
            for sam_item in sam_render_list:
                sam_item[1](*sam_item[2])

            draw_text(10, 770, f"HP: {sam_player_life}   Kills: {sam_game_score}/10   Coins: {sam_player_coins}   Bullets: {sam_ammo_count}")
            draw_vest_icon()
            draw_minimap()

            if sam_cheat_mode == "on":
                sam_rem = int(max(0, sam_CHEAT_DURATION - (time.time() - sam_cheat_start_time)))
                draw_text(380, 745, f"CHEAT MODE ({sam_rem}s)")

            if flying_is_on():
                sam_rem = int(max(0, sam_FLY_DURATION - (time.time() - sam_flying_start_time)))
                draw_text(380, 725, f"FLY MODE ({sam_rem}s)")

            sam_mode = "DAY" if sam_is_day else "NIGHT"
            draw_text(850, 680, f"TIME: {sam_mode} (Press M)")

        elif sam_game_state == "win":
            draw_text(420, 420, "LEVEL 1 COMPLETED!")
            draw_text(400, 380, f"Final Score: {sam_game_score} |Press N to go to Level 2 , Press R to Restart")
        else:
            draw_text(470, 420, "GAME OVER")
            draw_text(400, 380, f"Score: {sam_game_score} | Press R to Restart")

        glutSwapBuffers()

    init_blocks()    # Generates the trees
    init_dragon()    # Generates the dragon
    sam_last_coin_spawn = time.time()  # Ensures coins spawn correctly

    glutDisplayFunc(showScreen_1)
    glutKeyboardFunc(keyboardListener_1)
    glutSpecialFunc(specialKeyListener_1)
    glutMouseFunc(mouseListener_1)
    glutIdleFunc(idle_1)
    glutPostRedisplay()





from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time
import random


def start_level_2():

    global Prachurzo_camera_pos, Prachurzo_fovY, Prachurzo_player_rotation, Prachurzo_game_score
    global Prachurzo_enemy_count, Prachurzo_player_life, Prachurzo_enemy_info
    global Prachurzo_bullets, Prachurzo_enemy_bullets, Prachurzo_bullet_counter, Prachurzo_enemy_bullet_counter
    global Prachurzo_bullet_velocity, Prachurzo_enemy_bullet_velocity, Prachurzo_bullets_missed
    global Prachurzo_enemy_velocity, Prachurzo_next_enemy, Prachurzo_game_state
    global Prachurzo_cheat_mode, Prachurzo_cheat_start_time, Prachurzo_CHEAT_DURATION
    global Prachurzo_player_x, Prachurzo_player_y, Prachurzo_pov
    global Prachurzo_dragon, Prachurzo_dragon_fireballs, Prachurzo_dragon_fireball_counter
    global Prachurzo_dragon_speed, Prachurzo_dragon_height, Prachurzo_dragon_move_interval, Prachurzo_dragon_fire_interval
    global Prachurzo_dragon_fireball_speed, Prachurzo_dragon_gravity
    global Prachurzo_ARENA_HALF, Prachurzo_ARENA_OUT, Prachurzo_TILE_SIZE, Prachurzo_TILES_AMOUNT, Prachurzo_WALL_H
    global Prachurzo_blocks, Prachurzo_PLAYER_RADIUS, Prachurzo_ENEMY_RADIUS, Prachurzo_BULLET_RADIUS
    global Prachurzo_player_base_z, Prachurzo_player_z
    global Prachurzo_jump_active, Prachurzo_jump_t0, Prachurzo_jump_duration
    global Prachurzo_jump_start_x, Prachurzo_jump_start_y, Prachurzo_jump_start_z
    global Prachurzo_jump_target_x, Prachurzo_jump_target_y, Prachurzo_jump_target_z
    global Prachurzo_jump_peak_z, Prachurzo_jump_target_block, Prachurzo_player_on_block
    global Prachurzo_player_coins, Prachurzo_coins, Prachurzo_coin_counter
    global Prachurzo_coin_spawn_interval, Prachurzo_last_coin_spawn, Prachurzo_max_coins
    global Prachurzo_ammo_count, Prachurzo_bullet_pickups, Prachurzo_bullet_pickup_counter
    global Prachurzo_bullet_pickup_spawn_interval, Prachurzo_last_bullet_pickup_spawn
    global Prachurzo_max_bullet_pickups, Prachurzo_bullet_pickup_amount
    global Prachurzo_vest_active, Prachurzo_vest_start_time, Prachurzo_vest_duration, Prachurzo_VEST_COST
    global Prachurzo_UI_W, Prachurzo_UI_H, Prachurzo_WIN_W, Prachurzo_WIN_H
    global Prachurzo_VEST_X1, Prachurzo_VEST_Y1, Prachurzo_VEST_X2, Prachurzo_VEST_Y2
    global Prachurzo_black_tiles, Prachurzo_blocked_tiles, Prachurzo_last_black_spawn
    global Prachurzo_black_spawn_interval, Prachurzo_black_start_delay, Prachurzo_max_black_tiles
    global Prachurzo_last_black_damage, Prachurzo_black_damage_cooldown
    global Prachurzo_game_start_time
    global Prachurzo_flying_active, Prachurzo_flying_start_time, Prachurzo_FLY_DURATION, Prachurzo_FLY_Z_OFFSET
    global Prachurzo_CLEAR_RGB

    Prachurzo_camera_pos = (0, 500, 500)
    Prachurzo_fovY = 120
    Prachurzo_player_rotation = 0
    Prachurzo_game_score = 0
    Prachurzo_enemy_count = 5
    Prachurzo_player_life = 40
    Prachurzo_enemy_info = {}

    Prachurzo_bullets = {}
    Prachurzo_enemy_bullets = {}
    Prachurzo_bullet_counter = 0
    Prachurzo_enemy_bullet_counter = 0

    Prachurzo_bullet_velocity = 8
    Prachurzo_enemy_bullet_velocity = 5
    Prachurzo_bullets_missed = 0

    Prachurzo_enemy_velocity = 0.3
    Prachurzo_next_enemy = 0
    Prachurzo_game_state = "play"

    Prachurzo_cheat_mode = "off"
    Prachurzo_cheat_start_time = 0.0
    Prachurzo_CHEAT_DURATION = 15.0

    Prachurzo_player_x = 0
    Prachurzo_player_y = 0
    Prachurzo_pov = "tpp"

    Prachurzo_dragon = {}
    Prachurzo_dragon_fireballs = {}
    Prachurzo_dragon_fireball_counter = 0
    Prachurzo_dragon_speed = 2.0
    Prachurzo_dragon_height = 520.0
    Prachurzo_dragon_move_interval = 3.5
    Prachurzo_dragon_fire_interval = 1.0
    Prachurzo_dragon_fireball_speed = 10.0
    Prachurzo_dragon_gravity = 0.12

    Prachurzo_ARENA_HALF = 1200.0
    Prachurzo_ARENA_OUT = Prachurzo_ARENA_HALF + 8.0
    Prachurzo_TILE_SIZE = 100.0
    Prachurzo_TILES_AMOUNT = 24
    Prachurzo_WALL_H = 220.0

    Prachurzo_blocks = []
    Prachurzo_PLAYER_RADIUS = 45
    Prachurzo_ENEMY_RADIUS = 40
    Prachurzo_BULLET_RADIUS = 8

    Prachurzo_player_base_z = 75.0
    Prachurzo_player_z = 75.0

    Prachurzo_jump_active = False
    Prachurzo_jump_t0 = 0.0
    Prachurzo_jump_duration = 0.55
    Prachurzo_jump_start_x = Prachurzo_jump_start_y = Prachurzo_jump_start_z = 0.0
    Prachurzo_jump_target_x = Prachurzo_jump_target_y = Prachurzo_jump_target_z = 0.0
    Prachurzo_jump_peak_z = 0.0
    Prachurzo_jump_target_block = None
    Prachurzo_player_on_block = None

    Prachurzo_player_coins = 0
    Prachurzo_coins = {}
    Prachurzo_coin_counter = 0
    Prachurzo_coin_spawn_interval = 2.5
    Prachurzo_last_coin_spawn = 0.0
    Prachurzo_max_coins = 12

    Prachurzo_ammo_count = 40
    Prachurzo_bullet_pickups = {}
    Prachurzo_bullet_pickup_counter = 0
    Prachurzo_bullet_pickup_spawn_interval = 8.0
    Prachurzo_last_bullet_pickup_spawn = 0.0
    Prachurzo_max_bullet_pickups = 3
    Prachurzo_bullet_pickup_amount = 1

    Prachurzo_vest_active = False
    Prachurzo_vest_start_time = 0.0
    Prachurzo_vest_duration = 120.0
    Prachurzo_VEST_COST = 15

    Prachurzo_UI_W, Prachurzo_UI_H = 1000.0, 800.0
    Prachurzo_WIN_W, Prachurzo_WIN_H = 1200.0, 800.0

    Prachurzo_VEST_X1, Prachurzo_VEST_Y1 = 915.0, 720.0
    Prachurzo_VEST_X2, Prachurzo_VEST_Y2 = 990.0, 790.0

    Prachurzo_black_tiles = set()
    Prachurzo_blocked_tiles = set()
    Prachurzo_last_black_spawn = 0.0
    Prachurzo_black_spawn_interval = 4.0
    Prachurzo_black_start_delay = 10.0
    Prachurzo_max_black_tiles = 80

    Prachurzo_last_black_damage = 0.0
    Prachurzo_black_damage_cooldown = 0.6

    Prachurzo_game_start_time = 0.0

    Prachurzo_flying_active = False
    Prachurzo_flying_start_time = 0.0
    Prachurzo_FLY_DURATION = 120.0
    Prachurzo_FLY_Z_OFFSET = 25.0

    # -----------------------------
    # Replacement for glClearColor()
    # -----------------------------
    Prachurzo_CLEAR_RGB = (0.53, 0.81, 0.92)  # default sky color

    def set_fake_clear_color(r, g, b):
        global Prachurzo_CLEAR_RGB
        Prachurzo_CLEAR_RGB = (r, g, b)

    def draw_fake_clear_background():
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, Prachurzo_UI_W, 0, Prachurzo_UI_H)

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        glColor3f(Prachurzo_CLEAR_RGB[0], Prachurzo_CLEAR_RGB[1], Prachurzo_CLEAR_RGB[2])
        glBegin(GL_QUADS)
        glVertex3f(0, 0, 0)
        glVertex3f(Prachurzo_UI_W, 0, 0)
        glVertex3f(Prachurzo_UI_W, Prachurzo_UI_H, 0)
        glVertex3f(0, Prachurzo_UI_H, 0)
        glEnd()

        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)


    def get_camera_eye():
        global Prachurzo_pov, Prachurzo_camera_pos, Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_rotation, Prachurzo_player_z
        if Prachurzo_pov == "tpp":
            return Prachurzo_camera_pos

        rad = math.radians(-Prachurzo_player_rotation)
        fwd_x = math.sin(rad)
        fwd_y = math.cos(rad)

        eye_x = Prachurzo_player_x
        eye_y = Prachurzo_player_y
        eye_z = Prachurzo_player_z + 125.0

        return (eye_x, eye_y, eye_z)

    def dist2_to_camera(x, y, z):
        cx, cy, cz = get_camera_eye()
        dx = x - cx
        dy = y - cy
        dz = z - cz
        return dx * dx + dy * dy + dz * dz

    def vest_is_on():
        global Prachurzo_vest_active, Prachurzo_vest_start_time
        if not Prachurzo_vest_active:
            return False
        if time.time() - Prachurzo_vest_start_time > Prachurzo_vest_duration:
            Prachurzo_vest_active = False
            return False
        return True

    def flying_is_on():
        global Prachurzo_flying_active, Prachurzo_flying_start_time
        if not Prachurzo_flying_active:
            return False
        if time.time() - Prachurzo_flying_start_time > Prachurzo_FLY_DURATION:
            Prachurzo_flying_active = False
            return False
        return True

    def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
        glColor3f(1, 1, 1)

        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, Prachurzo_UI_W, 0, Prachurzo_UI_H)

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        glRasterPos2f(x, y)
        for ch in text:
            glutBitmapCharacter(font, ord(ch))

        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

    def draw_ui_rect(x1, y1, x2, y2, r, g, b):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, Prachurzo_UI_W, 0, Prachurzo_UI_H)

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        glColor3f(r, g, b)
        glBegin(GL_QUADS)
        glVertex3f(x1, y1, 0)
        glVertex3f(x2, y1, 0)
        glVertex3f(x2, y2, 0)
        glVertex3f(x1, y2, 0)
        glEnd()

        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

    def draw_vest_icon():
        affordable = (Prachurzo_player_coins >= Prachurzo_VEST_COST)
        active = vest_is_on()

        if active:
            draw_ui_rect(Prachurzo_VEST_X1, Prachurzo_VEST_Y1, Prachurzo_VEST_X2, Prachurzo_VEST_Y2, 0.5, 0.0, 0.1)
            draw_text(Prachurzo_VEST_X1 + 12, Prachurzo_VEST_Y1 + 30, "VEST", GLUT_BITMAP_HELVETICA_18)
            rem = int(max(0, Prachurzo_vest_duration - (time.time() - Prachurzo_vest_start_time)))
            draw_text(Prachurzo_VEST_X1 + 10, Prachurzo_VEST_Y1 + 10, f"{rem}s", GLUT_BITMAP_HELVETICA_18)
        else:
            if affordable:
                draw_ui_rect(Prachurzo_VEST_X1, Prachurzo_VEST_Y1, Prachurzo_VEST_X2, Prachurzo_VEST_Y2, 0.5, 0.0, 0.1)
            else:
                draw_ui_rect(Prachurzo_VEST_X1, Prachurzo_VEST_Y1, Prachurzo_VEST_X2, Prachurzo_VEST_Y2, 0.25, 0.05, 0.08)
            draw_text(Prachurzo_VEST_X1 + 10, Prachurzo_VEST_Y1 + 30, "VEST", GLUT_BITMAP_HELVETICA_18)
            draw_text(Prachurzo_VEST_X1 + 8, Prachurzo_VEST_Y1 + 10, f"{Prachurzo_VEST_COST} COINS", GLUT_BITMAP_HELVETICA_18)

    def screen_to_ui(mx, my):
        ux = (mx / float(Prachurzo_WIN_W)) * Prachurzo_UI_W
        uy = Prachurzo_UI_H - (my / float(Prachurzo_WIN_H)) * Prachurzo_UI_H
        return ux, uy

    def game_board(i, j, tiles_amount, x1, y1):
        if i >= tiles_amount:
            return
        if j < tiles_amount:

            if (i, j) in Prachurzo_black_tiles and (i, j) not in Prachurzo_blocked_tiles:
                glColor3f(0.0, 0.0, 0.0)
            else:
                if (i + j) % 2 == 0:
                    glColor3f(0.20, 0.70, 0.20)
                else:
                    glColor3f(0.10, 0.50, 0.10)

            x2, y2 = x1 + Prachurzo_TILE_SIZE, y1 + Prachurzo_TILE_SIZE
            glVertex3f(x1, y1, 0)
            glVertex3f(x2, y1, 0)
            glVertex3f(x2, y2, 0)
            glVertex3f(x1, y2, 0)

            game_board(i, j + 1, tiles_amount, x1 + Prachurzo_TILE_SIZE, y1)
        else:
            game_board(i + 1, 0, tiles_amount, -Prachurzo_ARENA_HALF, y1 + Prachurzo_TILE_SIZE)

    def draw_floor():
        glBegin(GL_QUADS)
        game_board(0, 0, Prachurzo_TILES_AMOUNT, -Prachurzo_ARENA_HALF, -Prachurzo_ARENA_HALF)
        glEnd()

    def draw_boundary():
        dark = (0.65, 0.16, 0.18)
        light = (0.88, 0.45, 0.46)

        cell_w = 100.0
        cell_h = 55.0
        cols = int((Prachurzo_ARENA_HALF * 2) / cell_w)
        rows = max(1, int(Prachurzo_WALL_H / cell_h))

        def wall_along_x(y_const):
            glBegin(GL_QUADS)
            for i in range(cols):
                x0 = -Prachurzo_ARENA_HALF + i * cell_w
                x1 = x0 + cell_w
                for j in range(rows):
                    z0 = j * cell_h
                    z1 = min(Prachurzo_WALL_H, z0 + cell_h)
                    if (i + j) % 2 == 0:
                        glColor3f(*dark)
                    else:
                        glColor3f(*light)
                    glVertex3f(x0, y_const, z0)
                    glVertex3f(x1, y_const, z0)
                    glVertex3f(x1, y_const, z1)
                    glVertex3f(x0, y_const, z1)
            glEnd()

        def wall_along_y(x_const):
            glBegin(GL_QUADS)
            for i in range(cols):
                y0 = -Prachurzo_ARENA_HALF + i * cell_w
                y1 = y0 + cell_w
                for j in range(rows):
                    z0 = j * cell_h
                    z1 = min(Prachurzo_WALL_H, z0 + cell_h)
                    if (i + j) % 2 == 0:
                        glColor3f(*dark)
                    else:
                        glColor3f(*light)
                    glVertex3f(x_const, y0, z0)
                    glVertex3f(x_const, y1, z0)
                    glVertex3f(x_const, y1, z1)
                    glVertex3f(x_const, y0, z1)
            glEnd()

        wall_along_x(-Prachurzo_ARENA_HALF)
        wall_along_x(Prachurzo_ARENA_HALF)
        wall_along_y(-Prachurzo_ARENA_HALF)
        wall_along_y(Prachurzo_ARENA_HALF)

    def draw_backpack():
        glPushMatrix()
        glColor3f(0.2, 0.2, 0.2)
        glTranslatef(0, -12, 50)
        glScalef(1.2, 0.6, 1.5)
        glutSolidCube(20)
        glPopMatrix()

    def draw_humanoid(body_color, head_color, is_enemy=False, show_spark=False, torso_scale_x=2.0):
        glPushMatrix()
        glScalef(torso_scale_x, 1, 4)
        glColor3f(body_color[0], body_color[1], body_color[2])
        glTranslatef(0, 0, 5)
        glutSolidCube(20)
        glPopMatrix()

        draw_backpack()

        glColor3f(0.1, 0.1, 0.4)
        glPushMatrix()
        glTranslatef(-15, 0, 8)
        glRotatef(180, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 12, 6, 80, 10, 10)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(15, 0, 8)
        glRotatef(180, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 12, 6, 80, 10, 10)
        glPopMatrix()

        glColor3f(1.0, 0.8, 0.7)
        glPushMatrix()
        glTranslatef(-25, 0, 50)
        glRotatef(-90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 10, 5, 50, 10, 10)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(25, 0, 50)
        glRotatef(-90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 10, 5, 50, 10, 10)
        glPopMatrix()

        glPushMatrix()
        glColor3f(head_color[0], head_color[1], head_color[2])
        glTranslatef(0, 0, 85)
        gluSphere(gluNewQuadric(), 20, 20, 20)

        if is_enemy:
            glColor3f(0, 0, 0)
            glPushMatrix()
            glTranslatef(-8, 18, 5)
            glScalef(5, 1, 1)
            glutSolidCube(1)
            glPopMatrix()
            glPushMatrix()
            glTranslatef(8, 18, 5)
            glScalef(5, 1, 1)
            glutSolidCube(1)
            glPopMatrix()
        glPopMatrix()

        glPushMatrix()
        glColor3f(0.3, 0.3, 0.3)
        glTranslatef(0, 0, 40)
        glRotatef(-90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), 8, 4, 100, 10, 10)

        if show_spark:
            glTranslatef(0, 0, 105)
            for _ in range(10):
                glPushMatrix()
                spark_color = random.choice([[1.0, 0.0, 0.0], [1.0, 0.5, 0.0]])
                glColor3f(spark_color[0], spark_color[1], spark_color[2])
                glRotatef(random.randint(0, 360), 0, 0, 1)
                glTranslatef(random.uniform(0, 10), 0, 0)
                gluSphere(gluNewQuadric(), 3, 8, 8)
                glPopMatrix()
        glPopMatrix()

    def draw_player():
        global Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_rotation, Prachurzo_player_z
        glPushMatrix()
        glTranslatef(Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_z)
        glRotatef(Prachurzo_player_rotation, 0, 0, 1)

        if vest_is_on():
            draw_humanoid([0.55, 0.0, 0.12], [0.0, 0.0, 0.0], torso_scale_x=2.0)
        else:
            draw_humanoid([0.4, 0.5, 0.0], [0.0, 0.0, 0.0], torso_scale_x=2.0)

        glPopMatrix()

    def draw_enemy(heading, firing):
        glPushMatrix()
        glTranslatef(0, 0, 75)
        glRotatef(heading, 0, 0, 1)
        draw_humanoid([0.0, 0.0, 0.5], [1.0, 0.8, 0.6], is_enemy=True, show_spark=firing, torso_scale_x=2.0)
        glPopMatrix()

    def draw_cap_square(radius, thickness):
        glPushMatrix()
        glScalef(radius * 2.0, radius * 2.0, thickness)
        glutSolidCube(1)
        glPopMatrix()

    def draw_ring_cubes(inner_r, outer_r, thickness, segments=24):
        mid_r = (inner_r + outer_r) * 0.5
        radial = max(0.5, (outer_r - inner_r))
        arc = (2.0 * math.pi * mid_r) / float(segments)
        tangential = max(0.5, arc * 0.85)

        for i in range(segments):
            ang = (360.0 / segments) * i
            glPushMatrix()
            glRotatef(ang, 0, 0, 1)
            glTranslatef(mid_r, 0, 0)
            glScalef(radial, tangential, thickness)
            glutSolidCube(1)
            glPopMatrix()

    def manual(y, x):
        if x == 0 and y == 0:
            return 0.0
        return math.atan2(y, x)

    def clamp(v, lo, hi):
        if v < lo:
            return lo
        if v > hi:
            return hi
        return v

    def rect_bounds(b, margin=0.0):
        half_w = b["w"] * 0.5
        half_l = b["l"] * 0.5
        minx = b["x"] - half_w - margin
        maxx = b["x"] + half_w + margin
        miny = b["y"] - half_l - margin
        maxy = b["y"] + half_l + margin
        return minx, maxx, miny, maxy

    def point_in_rect(px, py, minx, maxx, miny, maxy):
        return (minx <= px <= maxx) and (miny <= py <= maxy)

    def point_in_block(px, py, b, margin=0.0):
        minx, maxx, miny, maxy = rect_bounds(b, margin)
        return point_in_rect(px, py, minx, maxx, miny, maxy)

    def distance_point_to_rect(px, py, minx, maxx, miny, maxy):
        dx = 0.0
        if px < minx:
            dx = minx - px
        elif px > maxx:
            dx = px - maxx
        dy = 0.0
        if py < miny:
            dy = miny - py
        elif py > maxy:
            dy = py - maxy
        return (dx * dx + dy * dy) ** 0.5

    def segment_intersects_aabb_2d(x0, y0, x1, y1, minx, maxx, miny, maxy):
        dx = x1 - x0
        dy = y1 - y0
        t0, t1 = 0.0, 1.0

        def clip(p, q, t0_, t1_):
            if p == 0:
                if q < 0:
                    return False, t0_, t1_
                return True, t0_, t1_
            r = q / p
            if p < 0:
                if r > t1_:
                    return False, t0_, t1_
                if r > t0_:
                    t0_ = r
            else:
                if r < t0_:
                    return False, t0_, t1_
                if r < t1_:
                    t1_ = r
            return True, t0_, t1_

        ok, t0, t1 = clip(-dx, x0 - minx, t0, t1)
        if not ok:
            return False
        ok, t0, t1 = clip(dx, maxx - x0, t0, t1)
        if not ok:
            return False
        ok, t0, t1 = clip(-dy, y0 - miny, t0, t1)
        if not ok:
            return False
        ok, t0, t1 = clip(dy, maxy - y0, t0, t1)
        if not ok:
            return False
        return True

    def has_clear_shot(ex, ey, px, py):
        for i, b in enumerate(Prachurzo_blocks):
            if Prachurzo_player_on_block is not None and i == Prachurzo_player_on_block:
                continue
            minx, maxx, miny, maxy = rect_bounds(b, margin=10.0)
            if segment_intersects_aabb_2d(ex, ey, px, py, minx, maxx, miny, maxy):
                return False
        return True

    def bullet_hits_block(bx, by, bz):
        for b in Prachurzo_blocks:
            if point_in_block(bx, by, b, margin=Prachurzo_BULLET_RADIUS):
                if bz <= b["h"] + 5.0:
                    return True
        return False

    def push_player_out_of_blocks():
        global Prachurzo_player_x, Prachurzo_player_y

        if Prachurzo_player_on_block is not None or Prachurzo_jump_active:
            return

        for _ in range(6):
            fixed = False
            for b in Prachurzo_blocks:
                minx, maxx, miny, maxy = rect_bounds(b, margin=Prachurzo_PLAYER_RADIUS)
                if point_in_rect(Prachurzo_player_x, Prachurzo_player_y, minx, maxx, miny, maxy):
                    dl = abs(Prachurzo_player_x - minx)
                    dr = abs(maxx - Prachurzo_player_x)
                    db = abs(Prachurzo_player_y - miny)
                    dt = abs(maxy - Prachurzo_player_y)

                    m = min(dl, dr, db, dt)
                    eps = 1.0
                    if m == dl:
                        Prachurzo_player_x = minx - eps
                    elif m == dr:
                        Prachurzo_player_x = maxx + eps
                    elif m == db:
                        Prachurzo_player_y = miny - eps
                    else:
                        Prachurzo_player_y = maxy + eps

                    Prachurzo_player_x = clamp(Prachurzo_player_x, -Prachurzo_ARENA_HALF, Prachurzo_ARENA_HALF)
                    Prachurzo_player_y = clamp(Prachurzo_player_y, -Prachurzo_ARENA_HALF, Prachurzo_ARENA_HALF)
                    fixed = True
            if not fixed:
                break

    def random_free_spot(margin=60.0, tries=200):
        lim = Prachurzo_ARENA_HALF - margin
        for _ in range(tries):
            x = random.uniform(-lim, lim)
            y = random.uniform(-lim, lim)
            ok = True
            for b in Prachurzo_blocks:
                if point_in_block(x, y, b, margin=margin):
                    ok = False
                    break
            if ok:
                return x, y
        return 0.0, 0.0

    def tile_index_from_pos(x, y):
        col = int((x + Prachurzo_ARENA_HALF) / Prachurzo_TILE_SIZE)
        row = int((y + Prachurzo_ARENA_HALF) / Prachurzo_TILE_SIZE)

        row = max(0, min(Prachurzo_TILES_AMOUNT - 1, row))
        col = max(0, min(Prachurzo_TILES_AMOUNT - 1, col))
        return row, col

    def rebuild_blocked_tiles():
        Prachurzo_blocked_tiles.clear()
        for b in Prachurzo_blocks:
            minx, maxx, miny, maxy = rect_bounds(b, margin=0.0)

            col0 = int((minx + Prachurzo_ARENA_HALF) / Prachurzo_TILE_SIZE)
            col1 = int((maxx + Prachurzo_ARENA_HALF) / Prachurzo_TILE_SIZE)
            row0 = int((miny + Prachurzo_ARENA_HALF) / Prachurzo_TILE_SIZE)
            row1 = int((maxy + Prachurzo_ARENA_HALF) / Prachurzo_TILE_SIZE)

            col0 = max(0, min(Prachurzo_TILES_AMOUNT - 1, col0))
            col1 = max(0, min(Prachurzo_TILES_AMOUNT - 1, col1))
            row0 = max(0, min(Prachurzo_TILES_AMOUNT - 1, row0))
            row1 = max(0, min(Prachurzo_TILES_AMOUNT - 1, row1))

            for r in range(row0, row1 + 1):
                for c in range(col0, col1 + 1):
                    Prachurzo_blocked_tiles.add((r, c))

    def spawn_black_tiles():
        if len(Prachurzo_black_tiles) >= Prachurzo_max_black_tiles:
            return

        tries = 200
        added = 0
        while tries > 0 and added < 6 and len(Prachurzo_black_tiles) < Prachurzo_max_black_tiles:
            tries -= 1
            ii = random.randint(0, Prachurzo_TILES_AMOUNT - 1)
            jj = random.randint(0, Prachurzo_TILES_AMOUNT - 1)
            if (ii, jj) in Prachurzo_blocked_tiles:
                continue
            Prachurzo_black_tiles.add((ii, jj))
            added += 1

    def apply_black_tile_damage():
        global Prachurzo_player_life, Prachurzo_last_black_damage

        if flying_is_on():
            return
        if Prachurzo_jump_active or Prachurzo_player_on_block is not None:
            return

        now = time.time()
        if now - Prachurzo_last_black_damage < Prachurzo_black_damage_cooldown:
            return

        ii, jj = tile_index_from_pos(Prachurzo_player_x, Prachurzo_player_y)
        if (ii, jj) in Prachurzo_black_tiles and (ii, jj) not in Prachurzo_blocked_tiles:
            Prachurzo_player_life -= 1
            Prachurzo_last_black_damage = now

    def init_blocks():
        global Prachurzo_blocks
        Prachurzo_blocks = [
            {"x": -520.0, "y": 120.0, "w": 260.0, "l": 260.0, "h": 220.0},
            {"x": 520.0, "y": 220.0, "w": 280.0, "l": 220.0, "h": 200.0},
            {"x": 120.0, "y": -560.0, "w": 320.0, "l": 200.0, "h": 180.0},
            {"x": -260.0, "y": 520.0, "w": 240.0, "l": 240.0, "h": 240.0},
        ]
        rebuild_blocked_tiles()

    def find_jump_block(px, py, near_dist=60.0):
        for i, b in enumerate(Prachurzo_blocks):
            minx, maxx, miny, maxy = rect_bounds(b, margin=0.0)
            d = distance_point_to_rect(px, py, minx, maxx, miny, maxy)
            inside = point_in_rect(px, py, minx, maxx, miny, maxy)
            if (not inside) and d <= near_dist:
                lx = clamp(px, minx + 25.0, maxx - 25.0)
                ly = clamp(py, miny + 25.0, maxy - 25.0)
                return i, lx, ly
        return None, None, None

    def compute_drop_point(block_id, px, py):
        b = Prachurzo_blocks[block_id]
        minx, maxx, miny, maxy = rect_bounds(b, margin=0.0)

        dl = abs(px - minx)
        dr = abs(maxx - px)
        db = abs(py - miny)
        dt = abs(maxy - py)

        push = Prachurzo_PLAYER_RADIUS + 25.0
        m = min(dl, dr, db, dt)

        if m == dl:
            x = minx - push
            y = clamp(py, miny, maxy)
        elif m == dr:
            x = maxx + push
            y = clamp(py, miny, maxy)
        elif m == db:
            x = clamp(px, minx, maxx)
            y = miny - push
        else:
            x = clamp(px, minx, maxx)
            y = maxy + push

        x = clamp(x, -Prachurzo_ARENA_HALF, Prachurzo_ARENA_HALF)
        y = clamp(y, -Prachurzo_ARENA_HALF, Prachurzo_ARENA_HALF)

        for _ in range(25):
            bad = False
            for bb in Prachurzo_blocks:
                if point_in_block(x, y, bb, margin=Prachurzo_PLAYER_RADIUS):
                    bad = True
                    break
            if not bad:
                return x, y
            x += random.choice([-1, 1]) * 35.0
            y += random.choice([-1, 1]) * 35.0
            x = clamp(x, -Prachurzo_ARENA_HALF, Prachurzo_ARENA_HALF)
            y = clamp(y, -Prachurzo_ARENA_HALF, Prachurzo_ARENA_HALF)

        return x, y

    def start_jump_to(block_id, land_x, land_y, land_z):
        global Prachurzo_jump_active, Prachurzo_jump_t0, Prachurzo_jump_start_x, Prachurzo_jump_start_y, Prachurzo_jump_start_z
        global Prachurzo_jump_target_x, Prachurzo_jump_target_y, Prachurzo_jump_target_z, Prachurzo_jump_peak_z, Prachurzo_jump_target_block

        Prachurzo_jump_active = True
        Prachurzo_jump_t0 = time.time()

        Prachurzo_jump_start_x, Prachurzo_jump_start_y, Prachurzo_jump_start_z = Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_z
        Prachurzo_jump_target_x, Prachurzo_jump_target_y, Prachurzo_jump_target_z = land_x, land_y, land_z

        Prachurzo_jump_peak_z = max(Prachurzo_jump_start_z, Prachurzo_jump_target_z) + 120.0
        Prachurzo_jump_target_block = block_id

    def bezier_z(a, b, c, t):
        u = 1.0 - t
        return (u * u * a) + (2 * u * t * b) + (t * t * c)

    def update_jump():
        global Prachurzo_jump_active, Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_z, Prachurzo_player_on_block, Prachurzo_jump_target_block
        if not Prachurzo_jump_active:
            return

        t = (time.time() - Prachurzo_jump_t0) / Prachurzo_jump_duration
        if t >= 1.0:
            Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_z = Prachurzo_jump_target_x, Prachurzo_jump_target_y, Prachurzo_jump_target_z
            Prachurzo_jump_active = False
            Prachurzo_player_on_block = Prachurzo_jump_target_block
            if Prachurzo_player_on_block is None:
                push_player_out_of_blocks()
            return

        Prachurzo_player_x = (1.0 - t) * Prachurzo_jump_start_x + t * Prachurzo_jump_target_x
        Prachurzo_player_y = (1.0 - t) * Prachurzo_jump_start_y + t * Prachurzo_jump_target_y
        Prachurzo_player_z = bezier_z(Prachurzo_jump_start_z, Prachurzo_jump_peak_z, Prachurzo_jump_target_z, t)

    def draw_single_block(b):
        glPushMatrix()
        glTranslatef(b["x"], b["y"], b["h"] * 0.5)
        glColor3f(0.55, 0.27, 0.07)
        glScalef(b["w"], b["l"], b["h"])
        glutSolidCube(1)
        glPopMatrix()

    def spawn_coin():
        global Prachurzo_coin_counter
        x, y = random_free_spot(margin=70.0)
        Prachurzo_coin_counter += 1
        Prachurzo_coins[Prachurzo_coin_counter] = [x, y]

    def spawn_bullet_pickup():
        global Prachurzo_bullet_pickup_counter
        x, y = random_free_spot(margin=80.0)
        Prachurzo_bullet_pickup_counter += 1
        Prachurzo_bullet_pickups[Prachurzo_bullet_pickup_counter] = [x, y]

    def collect_pickups():
        global Prachurzo_player_coins, Prachurzo_ammo_count

        if (Prachurzo_player_z > Prachurzo_player_base_z + 10.0) and (not flying_is_on()):
            return

        rem = []
        for k, c in Prachurzo_coins.items():
            if (Prachurzo_player_x - c[0]) ** 2 + (Prachurzo_player_y - c[1]) ** 2 <= (55.0 ** 2):
                Prachurzo_player_coins += 1
                rem.append(k)
        for k in rem:
            if k in Prachurzo_coins:
                del Prachurzo_coins[k]

        rem2 = []
        for k, p in Prachurzo_bullet_pickups.items():
            if (Prachurzo_player_x - p[0]) ** 2 + (Prachurzo_player_y - p[1]) ** 2 <= (55.0 ** 2):
                Prachurzo_ammo_count += Prachurzo_bullet_pickup_amount
                rem2.append(k)
        for k in rem2:
            if k in Prachurzo_bullet_pickups:
                del Prachurzo_bullet_pickups[k]

    def restart_game():

        global Prachurzo_pov, Prachurzo_player_x, Prachurzo_player_y, Prachurzo_camera_pos, Prachurzo_player_rotation, Prachurzo_game_score, Prachurzo_player_life
        global Prachurzo_enemy_info, Prachurzo_bullets, Prachurzo_enemy_bullets, Prachurzo_bullet_counter, Prachurzo_enemy_bullet_counter, Prachurzo_bullets_missed
        global Prachurzo_game_state, Prachurzo_cheat_mode, Prachurzo_cheat_start_time, Prachurzo_player_base_z, Prachurzo_player_z, Prachurzo_next_enemy
        global Prachurzo_dragon, Prachurzo_dragon_fireballs, Prachurzo_dragon_fireball_counter
        global Prachurzo_jump_active, Prachurzo_player_on_block, Prachurzo_jump_target_block
        global Prachurzo_player_coins, Prachurzo_coins, Prachurzo_coin_counter, Prachurzo_last_coin_spawn
        global Prachurzo_ammo_count, Prachurzo_bullet_pickups, Prachurzo_bullet_pickup_counter, Prachurzo_last_bullet_pickup_spawn
        global Prachurzo_vest_active, Prachurzo_vest_start_time
        global Prachurzo_black_tiles, Prachurzo_last_black_spawn, Prachurzo_last_black_damage, Prachurzo_game_start_time
        global Prachurzo_flying_active, Prachurzo_flying_start_time

        Prachurzo_camera_pos = (0, 500, 500)
        Prachurzo_player_rotation = 0
        Prachurzo_game_score = 0
        Prachurzo_player_life = 40
        Prachurzo_enemy_info = {}

        Prachurzo_bullets = {}
        Prachurzo_enemy_bullets = {}
        Prachurzo_bullet_counter = 0
        Prachurzo_enemy_bullet_counter = 0
        Prachurzo_bullets_missed = 0

        Prachurzo_next_enemy = 0
        Prachurzo_game_state = "play"
        Prachurzo_cheat_mode = "off"
        Prachurzo_cheat_start_time = 0.0

        Prachurzo_player_x = 0
        Prachurzo_player_y = 0
        Prachurzo_pov = "tpp"

        Prachurzo_player_base_z = 75.0
        Prachurzo_player_z = 75.0

        Prachurzo_jump_active = False
        Prachurzo_player_on_block = None
        Prachurzo_jump_target_block = None

        Prachurzo_player_coins = 0
        Prachurzo_coins = {}
        Prachurzo_coin_counter = 0
        Prachurzo_last_coin_spawn = time.time()

        Prachurzo_ammo_count = 40
        Prachurzo_bullet_pickups = {}
        Prachurzo_bullet_pickup_counter = 0
        Prachurzo_last_bullet_pickup_spawn = time.time()

        Prachurzo_vest_active = False
        Prachurzo_vest_start_time = 0.0

        Prachurzo_black_tiles = set()
        Prachurzo_last_black_spawn = time.time()
        Prachurzo_last_black_damage = 0.0
        Prachurzo_game_start_time = time.time()

        Prachurzo_flying_active = False
        Prachurzo_flying_start_time = 0.0

        init_blocks()
        init_dragon()

    def handlecamera_2(key, x, y):
        global Prachurzo_camera_pos
        cx, cy, cz = Prachurzo_camera_pos
        if key == GLUT_KEY_UP:
            cz += 5
        if key == GLUT_KEY_DOWN:
            cz -= 5
        res = (cx ** 2 + cy ** 2) ** 0.5
        ang = manual(cy, cx)
        if key == GLUT_KEY_LEFT:
            ang -= 0.01
        if key == GLUT_KEY_RIGHT:
            ang += 0.01
        Prachurzo_camera_pos = (res * math.cos(ang), res * math.sin(ang), cz)
        glutPostRedisplay()

    def keyboardListener_2(key, x, y):
        global Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_rotation, Prachurzo_cheat_mode, Prachurzo_cheat_start_time, Prachurzo_game_state
        global Prachurzo_jump_active, Prachurzo_player_on_block
        global Prachurzo_flying_active, Prachurzo_flying_start_time

        # ----------- NEW: level complete input handling -----------
        if Prachurzo_game_state == "completed":
            if key == b'r':
                restart_game()

            glutPostRedisplay()
            return
        # ---------------------------------------------------------

        if Prachurzo_game_state == "play":
            speed = 12
            if Prachurzo_cheat_mode == "on":
                speed = 6

            if Prachurzo_jump_active:
                glutPostRedisplay()
                return

            if key == b'f':
                Prachurzo_flying_active = True
                Prachurzo_flying_start_time = time.time()
                Prachurzo_player_on_block = None
                glutPostRedisplay()
                return

            if key == b'j':
                if Prachurzo_player_on_block is None:
                    bid, lx, ly = find_jump_block(Prachurzo_player_x, Prachurzo_player_y, near_dist=60.0)
                    if bid is not None:
                        top_z = Prachurzo_player_base_z + Prachurzo_blocks[bid]["h"]
                        start_jump_to(bid, lx, ly, top_z)
                    glutPostRedisplay()
                    return
                else:
                    dx, dy = compute_drop_point(Prachurzo_player_on_block, Prachurzo_player_x, Prachurzo_player_y)
                    start_jump_to(None, dx, dy, Prachurzo_player_base_z)
                    glutPostRedisplay()
                    return

            old_x, old_y = Prachurzo_player_x, Prachurzo_player_y

            if key == b'w':
                Prachurzo_player_x += speed * math.sin(math.radians(-Prachurzo_player_rotation))
                Prachurzo_player_y += speed * math.cos(math.radians(-Prachurzo_player_rotation))

            if key == b's':
                Prachurzo_player_x -= speed * math.sin(math.radians(-Prachurzo_player_rotation))
                Prachurzo_player_y -= speed * math.cos(math.radians(-Prachurzo_player_rotation))

            Prachurzo_player_x = clamp(Prachurzo_player_x, -Prachurzo_ARENA_HALF, Prachurzo_ARENA_HALF)
            Prachurzo_player_y = clamp(Prachurzo_player_y, -Prachurzo_ARENA_HALF, Prachurzo_ARENA_HALF)

            if Prachurzo_player_on_block is None:
                collided = False
                for b in Prachurzo_blocks:
                    if point_in_block(Prachurzo_player_x, Prachurzo_player_y, b, margin=Prachurzo_PLAYER_RADIUS):
                        collided = True
                        break
                if collided:
                    Prachurzo_player_x, Prachurzo_player_y = old_x, old_y

                push_player_out_of_blocks()


            if key == b'd':
                    Prachurzo_player_rotation -= 8
            if key == b'a':
                    Prachurzo_player_rotation += 8

            if key == b'c':
                if Prachurzo_cheat_mode == "off":
                    Prachurzo_cheat_mode = "on"
                    Prachurzo_cheat_start_time = time.time()
                    Prachurzo_bullets.clear()
                    Prachurzo_enemy_bullets.clear()
                else:
                    Prachurzo_cheat_mode = "off"

        if key == b'r' and Prachurzo_game_state == "over":
            restart_game()

        glutPostRedisplay()

    def try_buy_vest():
        global Prachurzo_player_coins, Prachurzo_vest_active, Prachurzo_vest_start_time
        if vest_is_on():
            return
        if Prachurzo_player_coins >= Prachurzo_VEST_COST:
            Prachurzo_player_coins -= Prachurzo_VEST_COST
            Prachurzo_vest_active = True
            Prachurzo_vest_start_time = time.time()

    def mouseListener_2(button, state, x, y):
        global Prachurzo_pov, Prachurzo_bullets, Prachurzo_bullet_counter, Prachurzo_bullet_velocity, Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_rotation, Prachurzo_cheat_mode, Prachurzo_camera_pos
        global Prachurzo_player_z, Prachurzo_ammo_count, Prachurzo_game_state

        if state != GLUT_DOWN:
            return

        ux, uy = screen_to_ui(x, y)
        if button == GLUT_LEFT_BUTTON and Prachurzo_game_state == "play":
            if (Prachurzo_VEST_X1 <= ux <= Prachurzo_VEST_X2) and (Prachurzo_VEST_Y1 <= uy <= Prachurzo_VEST_Y2):
                try_buy_vest()
                glutPostRedisplay()
                return

        if button == GLUT_LEFT_BUTTON and Prachurzo_cheat_mode == "off" and Prachurzo_game_state == "play":
            if Prachurzo_ammo_count > 0:
                Prachurzo_ammo_count -= 1
                Prachurzo_bullet_counter += 1
                rad = math.radians(-Prachurzo_player_rotation)
                Prachurzo_bullets[Prachurzo_bullet_counter] = [
                    Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_z + 35.0,
                    Prachurzo_bullet_velocity * math.sin(rad), Prachurzo_bullet_velocity * math.cos(rad)
                ]

        if button == GLUT_RIGHT_BUTTON and Prachurzo_game_state == "play":
            Prachurzo_pov = "fpp" if Prachurzo_pov == "tpp" else "tpp"
            if Prachurzo_pov == "tpp":
                Prachurzo_camera_pos = (0, 500, 500)

        glutPostRedisplay()

    def setup_camera():
        global Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_rotation, Prachurzo_camera_pos, Prachurzo_pov, Prachurzo_player_z

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(Prachurzo_fovY, 1.25, 0.1, 4000)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        if Prachurzo_pov == "tpp":
            x, y, z = Prachurzo_camera_pos
            gluLookAt(x, y, z, 0, 0, 0, 0, 0, 1)
        else:
            rad = math.radians(-Prachurzo_player_rotation)
            fwd_x = math.sin(rad)
            fwd_y = math.cos(rad)

            eye_x = Prachurzo_player_x
            eye_y = Prachurzo_player_y
            eye_z = Prachurzo_player_z + 125.0

            target_x = eye_x + fwd_x * 120.0
            target_y = eye_y + fwd_y * 120.0
            target_z = eye_z - 40.0

            gluLookAt(eye_x, eye_y, eye_z, target_x, target_y, target_z, 0, 0, 1)

    def draw_cyl(x, y, z, vx, vy, radius, length, body_rgb, cap_rgb):
        ang = math.degrees(math.atan2(vx, vy))

        glPushMatrix()
        glTranslatef(x, y, z)
        glRotatef(ang, 0, 0, 1)
        glRotatef(90, 1, 0, 0)

        glColor3f(body_rgb[0], body_rgb[1], body_rgb[2])
        q = gluNewQuadric()
        gluCylinder(q, radius, radius, length, 12, 2)

        glColor3f(cap_rgb[0], cap_rgb[1], cap_rgb[2])
        draw_cap_square(radius, 0.8)
        glPushMatrix()
        glTranslatef(0, 0, length)
        draw_cap_square(radius, 0.8)
        glPopMatrix()

        glPopMatrix()

    def draw_single_coin(cx, cy, spin, bob):
        glColor3f(1.0, 0.85, 0.10)
        glPushMatrix()
        glTranslatef(cx, cy, 40.0 + bob)
        glRotatef(spin, 0, 0, 1)
        glRotatef(90, 1, 0, 0)
        draw_ring_cubes(inner_r=10.0, outer_r=18.0, thickness=2.5, segments=24)
        glPopMatrix()

    def draw_single_bullet_pickup(px, py, spin, bob):
        glPushMatrix()
        glTranslatef(px, py, 18.0 + bob)
        glRotatef(spin, 0, 0, 1)
        glRotatef(90, 0, 1, 0)

        glColor3f(0.80, 0.80, 0.86)
        radius = 6.5
        length = 30.0
        q = gluNewQuadric()
        gluCylinder(q, radius, radius, length, 14, 2)

        glColor3f(0.75, 0.75, 0.80)
        draw_cap_square(radius, 0.9)
        glPushMatrix()
        glTranslatef(0, 0, length)
        draw_cap_square(radius, 0.9)
        glPopMatrix()

        glPopMatrix()

    def draw_enemy_at(v):
        glPushMatrix()
        glTranslatef(v["pos"][0], v["pos"][1], 0)
        draw_enemy(v["heading"], v["is_firing"])
        glPopMatrix()

    def player_enemy_interaction():
        global Prachurzo_enemy_info, Prachurzo_player_x, Prachurzo_player_y, Prachurzo_cheat_mode, Prachurzo_enemy_bullets, Prachurzo_enemy_bullet_counter
        curr = time.time()

        for k, v in Prachurzo_enemy_info.items():
            ex, ey, ez = v["pos"]
            v["is_firing"] = False

            rad_move = math.radians(v["heading"])
            nx = ex + Prachurzo_enemy_velocity * math.sin(rad_move)
            ny = ey + Prachurzo_enemy_velocity * math.cos(rad_move)

            if abs(nx) > Prachurzo_ARENA_HALF or abs(ny) > Prachurzo_ARENA_HALF:
                v["heading"] = random.uniform(0, 360)
                continue

            blocked = False
            for b in Prachurzo_blocks:
                if point_in_block(nx, ny, b, margin=Prachurzo_ENEMY_RADIUS):
                    blocked = True
                    break
            if blocked:
                v["heading"] = random.uniform(0, 360)
                continue

            v["pos"] = (nx, ny, ez)

            if Prachurzo_cheat_mode == "off":
                dist = math.sqrt((nx - Prachurzo_player_x) ** 2 + (ny - Prachurzo_player_y) ** 2)
                if dist < 450 and has_clear_shot(nx, ny, Prachurzo_player_x, Prachurzo_player_y):
                    v["heading"] = -math.degrees(math.atan2(Prachurzo_player_x - nx, Prachurzo_player_y - ny))
                    if curr - v["last_fire"] > 1.2:
                        v["is_firing"] = True
                        Prachurzo_enemy_bullet_counter += 1
                        rad_fire = math.radians(-v["heading"])
                        Prachurzo_enemy_bullets[Prachurzo_enemy_bullet_counter] = [
                            nx, ny, 110.0,
                            6 * math.sin(rad_fire), 6 * math.cos(rad_fire)
                        ]
                        v["last_fire"] = curr

    def render_bullet():
        global Prachurzo_bullets, Prachurzo_enemy_bullets, Prachurzo_bullets_missed, Prachurzo_enemy_info, Prachurzo_game_score, Prachurzo_player_life, Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_z

        rem_b = []
        for k, v in Prachurzo_bullets.items():
            v[0] += v[3]
            v[1] += v[4]

            if abs(v[0]) > Prachurzo_ARENA_HALF or abs(v[1]) > Prachurzo_ARENA_HALF:
                rem_b.append(k)
                Prachurzo_bullets_missed += 1
                continue

            if bullet_hits_block(v[0], v[1], v[2]):
                rem_b.append(k)
                continue

            for ek, ev in list(Prachurzo_enemy_info.items()):
                if ((v[0] - ev["pos"][0]) ** 2 + (v[1] - ev["pos"][1]) ** 2) <= 50 ** 2:
                    Prachurzo_game_score += 1
                    rem_b.append(k)
                    del Prachurzo_enemy_info[ek]
                    break

        for k in rem_b:
            if k in Prachurzo_bullets:
                del Prachurzo_bullets[k]

        rem_eb = []
        for k, v in Prachurzo_enemy_bullets.items():
            v[0] += v[3]
            v[1] += v[4]

            if abs(v[0]) > Prachurzo_ARENA_HALF or abs(v[1]) > Prachurzo_ARENA_HALF:
                rem_eb.append(k)
                continue

            if bullet_hits_block(v[0], v[1], v[2]):
                rem_eb.append(k)
                continue

            if ((v[0] - Prachurzo_player_x) ** 2 + (v[1] - Prachurzo_player_y) ** 2) <= 45 ** 2:
                if Prachurzo_player_z <= v[2] <= (Prachurzo_player_z + 150.0):
                    if not vest_is_on():
                        Prachurzo_player_life -= 1
                    rem_eb.append(k)

        for k in rem_eb:
            if k in Prachurzo_enemy_bullets:
                del Prachurzo_enemy_bullets[k]

    def render_enemy_spawn():
        global Prachurzo_enemy_info, Prachurzo_next_enemy, Prachurzo_enemy_count, Prachurzo_player_x, Prachurzo_player_y
        spawn_lim = int(Prachurzo_ARENA_HALF - 50)

        while len(Prachurzo_enemy_info) < Prachurzo_enemy_count:
            tx, ty = random.randint(-spawn_lim, spawn_lim), random.randint(-spawn_lim, spawn_lim)

            if math.sqrt((tx - Prachurzo_player_x) ** 2 + (ty - Prachurzo_player_y) ** 2) <= 300:
                continue

            bad = False
            for b in Prachurzo_blocks:
                if point_in_block(tx, ty, b, margin=Prachurzo_ENEMY_RADIUS + 15):
                    bad = True
                    break
            if bad:
                continue

            Prachurzo_enemy_info[Prachurzo_next_enemy] = {
                "pos": (tx, ty, 0),
                "heading": random.uniform(0, 360),
                "last_fire": 0,
                "is_firing": False
            }
            Prachurzo_next_enemy += 1

    def init_dragon():
        global Prachurzo_dragon, Prachurzo_dragon_fireballs, Prachurzo_dragon_fireball_counter
        Prachurzo_dragon_fireballs = {}
        Prachurzo_dragon_fireball_counter = 0

        lim = int(Prachurzo_ARENA_HALF - 50)
        x = random.randint(-lim, lim)
        y = random.randint(-lim, lim)
        z = Prachurzo_dragon_height

        Prachurzo_dragon = {
            "pos": [float(x), float(y), float(float(z))],
            "target": [float(random.randint(-lim, lim)), float(random.randint(-lim, lim)), float(float(z))],
            "last_move": time.time(),
            "last_fire": time.time()
        }

    def update_dragon():
        global Prachurzo_dragon
        if not Prachurzo_dragon:
            init_dragon()
            return

        now = time.time()
        lim = int(Prachurzo_ARENA_HALF - 50)

        if now - Prachurzo_dragon["last_move"] > Prachurzo_dragon_move_interval:
            Prachurzo_dragon["target"][0] = float(random.randint(-lim, lim))
            Prachurzo_dragon["target"][1] = float(random.randint(-lim, lim))
            Prachurzo_dragon["last_move"] = now

        px, py, pz = Prachurzo_dragon["pos"]
        tx, ty, tz = Prachurzo_dragon["target"]
        dx, dy = (tx - px), (ty - py)
        dist = (dx * dx + dy * dy) ** 0.5

        if dist > 0.001:
            step = min(Prachurzo_dragon_speed, dist)
            Prachurzo_dragon["pos"][0] = px + (dx / dist) * step
            Prachurzo_dragon["pos"][1] = py + (dy / dist) * step
            Prachurzo_dragon["pos"][2] = pz

    def spawn_dragon_fireball():
        global Prachurzo_dragon_fireballs, Prachurzo_dragon_fireball_counter, Prachurzo_dragon, Prachurzo_player_x, Prachurzo_player_y
        if not Prachurzo_dragon:
            return

        Prachurzo_dragon_fireball_counter += 1
        sx, sy, sz = Prachurzo_dragon["pos"]

        target_x = Prachurzo_player_x + random.uniform(-80, 80)
        target_y = Prachurzo_player_y + random.uniform(-80, 80)
        target_z = 90.0

        dx = target_x - sx
        dy = target_y - sy
        dz = target_z - sz

        dist = (dx * dx + dy * dy + dz * dz) ** 0.5
        if dist == 0:
            dist = 1.0

        vx = (dx / dist) * Prachurzo_dragon_fireball_speed
        vy = (dy / dist) * Prachurzo_dragon_fireball_speed
        vz = (dz / dist) * Prachurzo_dragon_fireball_speed

        Prachurzo_dragon_fireballs[Prachurzo_dragon_fireball_counter] = [sx, sy, sz, vx, vy, vz]

    def update_dragon_fireballs():
        global Prachurzo_dragon_fireballs, Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_life, Prachurzo_dragon
        if not Prachurzo_dragon:
            return

        now = time.time()

        if now - Prachurzo_dragon["last_fire"] > Prachurzo_dragon_fire_interval:
            spawn_dragon_fireball()
            Prachurzo_dragon["last_fire"] = now

        to_remove = []
        out_lim = Prachurzo_ARENA_HALF + 120.0

        for k, fb in Prachurzo_dragon_fireballs.items():
            x, y, z, vx, vy, vz = fb

            vz -= Prachurzo_dragon_gravity
            x += vx
            y += vy
            z += vz

            Prachurzo_dragon_fireballs[k] = [x, y, z, vx, vy, vz]

            if abs(x) > out_lim or abs(y) > out_lim or z <= 0:
                to_remove.append(k)
                continue

            if ((x - Prachurzo_player_x) ** 2 + (y - Prachurzo_player_y) ** 2) <= (45 ** 2) and z <= 170:
                if not vest_is_on():
                    Prachurzo_player_life -= 1
                to_remove.append(k)

        for k in to_remove:
            if k in Prachurzo_dragon_fireballs:
                del Prachurzo_dragon_fireballs[k]

    def draw_dragon():
        if not Prachurzo_dragon:
            return

        x, y, z = Prachurzo_dragon["pos"]

        glPushMatrix()
        glTranslatef(x, y, z)

        glColor3f(1.0, 0.45, 0.0)
        gluSphere(gluNewQuadric(), 28, 18, 18)

        glPushMatrix()
        glTranslatef(0, 35, 10)
        glColor3f(1.0, 0.55, 0.0)
        gluSphere(gluNewQuadric(), 16, 14, 14)
        glPopMatrix()

        glColor3f(0.95, 0.35, 0.0)
        glPushMatrix()
        glTranslatef(-55, 0, 0)
        glScalef(110, 2, 35)
        glutSolidCube(1)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(55, 0, 0)
        glScalef(110, 2, 35)
        glutSolidCube(1)
        glPopMatrix()

        glPopMatrix()

    def draw_single_dragon_fireball(fb):
        glColor3f(1.0, 0.45, 0.0)
        glPushMatrix()
        glTranslatef(fb[0], fb[1], fb[2])
        gluSphere(gluNewQuadric(), 10, 10, 10)
        glPopMatrix()

    def animate_2():
        global Prachurzo_game_state, Prachurzo_player_life, Prachurzo_bullets_missed, Prachurzo_cheat_mode, Prachurzo_cheat_start_time
        global Prachurzo_last_coin_spawn, Prachurzo_last_bullet_pickup_spawn
        global Prachurzo_last_black_spawn


        if Prachurzo_game_state == "play" and Prachurzo_game_score >= 20:
            Prachurzo_game_state = "completed"
        # ----------------------------------------------------

        if Prachurzo_player_life <= 0 or Prachurzo_bullets_missed >= 25:
            Prachurzo_game_state = "over"

        if Prachurzo_game_state == "play":

            if Prachurzo_cheat_mode == "on" and (time.time() - Prachurzo_cheat_start_time > Prachurzo_CHEAT_DURATION):
                Prachurzo_cheat_mode = "off"

            update_jump()

            global Prachurzo_player_z
            if (not Prachurzo_jump_active) and flying_is_on():
                Prachurzo_player_z = Prachurzo_player_base_z + Prachurzo_FLY_Z_OFFSET
            elif (not Prachurzo_jump_active) and (Prachurzo_player_on_block is None):
                Prachurzo_player_z = Prachurzo_player_base_z

            if (not Prachurzo_jump_active) and (Prachurzo_player_on_block is not None):
                b = Prachurzo_blocks[Prachurzo_player_on_block]
                minx, maxx, miny, maxy = rect_bounds(b, margin=-10.0)
                if not point_in_rect(Prachurzo_player_x, Prachurzo_player_y, minx, maxx, miny, maxy):
                    start_jump_to(None, Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_base_z)

            render_bullet()
            render_enemy_spawn()
            player_enemy_interaction()

            update_dragon()
            update_dragon_fireballs()

            push_player_out_of_blocks()

            now = time.time()
            if (now - Prachurzo_last_coin_spawn) > Prachurzo_coin_spawn_interval and len(Prachurzo_coins) < Prachurzo_max_coins:
                spawn_coin()
                Prachurzo_last_coin_spawn = now

            if (now - Prachurzo_last_bullet_pickup_spawn) > Prachurzo_bullet_pickup_spawn_interval and len(Prachurzo_bullet_pickups) < Prachurzo_max_bullet_pickups:
                spawn_bullet_pickup()
                Prachurzo_last_bullet_pickup_spawn = now

            if (now - Prachurzo_game_start_time) > Prachurzo_black_start_delay:
                if (now - Prachurzo_last_black_spawn) > Prachurzo_black_spawn_interval:
                    spawn_black_tiles()
                    Prachurzo_last_black_spawn = now

            apply_black_tile_damage()
            collect_pickups()

        glutPostRedisplay()

    def display_2():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_fake_clear_background()
        setup_camera()

        draw_floor()
        draw_boundary()

        if Prachurzo_game_state == "play":
            items = []

            for b in Prachurzo_blocks:
                items.append((dist2_to_camera(b["x"], b["y"], b["h"] * 0.5), (lambda bb=b: draw_single_block(bb))))

            spin_coin = (time.time() * 160.0) % 360.0
            bob_coin = math.sin(time.time() * 2.2) * 3.5
            for c in Prachurzo_coins.values():
                cx, cy = c[0], c[1]
                items.append((dist2_to_camera(cx, cy, 40.0 + bob_coin), (lambda x=cx, y=cy: draw_single_coin(x, y, spin_coin, bob_coin))))

            spin_pick = (time.time() * 140.0) % 360.0
            bob_pick = math.sin(time.time() * 2.0) * 2.0
            for p in Prachurzo_bullet_pickups.values():
                px, py = p[0], p[1]
                items.append((dist2_to_camera(px, py, 18.0 + bob_pick), (lambda x=px, y=py: draw_single_bullet_pickup(x, y, spin_pick, bob_pick))))

            items.append((dist2_to_camera(Prachurzo_player_x, Prachurzo_player_y, Prachurzo_player_z + 75.0), draw_player))

            for v in Prachurzo_enemy_info.values():
                ex, ey, _ = v["pos"]
                items.append((dist2_to_camera(ex, ey, 75.0), (lambda vv=v: draw_enemy_at(vv))))

            for b in Prachurzo_bullets.values():
                items.append((
                    dist2_to_camera(b[0], b[1], b[2]),
                    (lambda bb=b: draw_cyl(bb[0], bb[1], bb[2], bb[3], bb[4], 5.0, 22.0, (0.80, 0.80, 0.86), (0.75, 0.75, 0.80)))
                ))

            for eb in Prachurzo_enemy_bullets.values():
                items.append((
                    dist2_to_camera(eb[0], eb[1], eb[2]),
                    (lambda bb=eb: draw_cyl(bb[0], bb[1], bb[2], bb[3], bb[4], 4.5, 20.0, (0.65, 0.65, 0.70), (0.75, 0.75, 0.80)))
                ))

            if Prachurzo_dragon:
                dx, dy, dz = Prachurzo_dragon["pos"]
                items.append((dist2_to_camera(dx, dy, dz), draw_dragon))

            for fb in Prachurzo_dragon_fireballs.values():
                items.append((dist2_to_camera(fb[0], fb[1], fb[2]), (lambda f=fb: draw_single_dragon_fireball(f))))

            items.sort(key=lambda it: it[0], reverse=True)
            for _, fn in items:
                fn()

            draw_text(10, 770, f"Life: {Prachurzo_player_life}  |  Kills: {Prachurzo_game_score}  |  Coins: {Prachurzo_player_coins}  |  Ammo: {Prachurzo_ammo_count}")
            draw_vest_icon()

            if Prachurzo_cheat_mode == "on":
                rem = int(max(0, Prachurzo_CHEAT_DURATION - (time.time() - Prachurzo_cheat_start_time)))
                draw_text(380, 745, f"CHEAT MODE ON ({rem}s)")

            if flying_is_on():
                rem = int(max(0, Prachurzo_FLY_DURATION - (time.time() - Prachurzo_flying_start_time)))
                draw_text(380, 725, f"FLY MODE ON ({rem}s)")

        # ----------- NEW: completed screen -----------
        elif Prachurzo_game_state == "completed":
            draw_text(310, 450, "Congratulations, level-2 completed", GLUT_BITMAP_TIMES_ROMAN_24)
            draw_text(330, 410, "Press n for starting level-3", GLUT_BITMAP_HELVETICA_18)
            draw_text(340, 380, "Press r for restarting level-2", GLUT_BITMAP_HELVETICA_18)
        # --------------------------------------------

        else:
            draw_text(470, 420, "GAME OVER", GLUT_BITMAP_TIMES_ROMAN_24)
            draw_text(400, 380, f"Score: {Prachurzo_game_score} | Press R to Restart", GLUT_BITMAP_HELVETICA_18)

        glutSwapBuffers()

    init_blocks()
    init_dragon()
    Prachurzo_last_coin_spawn = time.time()
    Prachurzo_last_bullet_pickup_spawn = time.time()
    Prachurzo_last_black_spawn = time.time()
    Prachurzo_game_start_time = time.time()

    glutDisplayFunc(display_2)
    glutIdleFunc(animate_2)
    glutKeyboardFunc(keyboardListener_2)
    glutSpecialFunc(handlecamera_2)
    glutMouseFunc(mouseListener_2)

    glutMainLoop()


 










def main():
        global _window_created
        if not _window_created:
            glutInit()
            glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
            glutInitWindowSize(1200, 800)
            glutInitWindowPosition(0, 0)
            glutCreateWindow(b"Chaos Arena (Level Switch with N)")
            _window_created = True

            start_level_1()
            glutMainLoop()

if __name__ == "__main__":
    main()


