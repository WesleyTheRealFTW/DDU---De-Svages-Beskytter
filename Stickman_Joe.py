import pygame
import sys


class Button:
    def __init__(self, surface, image_path, x, y, width, height, text=''):
        self.surface = surface
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.active = True

    def draw(self):
        if self.active:
            self.surface.blit(self.image, (self.x, self.y))
            if self.text != '':
                font = pygame.font.SysFont(None, 30)
                text_surface = font.render(self.text, True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
                self.surface.blit(text_surface, text_rect)

    def is_over(self, pos):
        if self.active:
            if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
                return True
        return False
    def set_inactive(self):
        self.active = False

class Key:
    def __init__(self, surface, image_path, x, y, width=50, height=50):
        self.surface = surface
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw_key(self):
        if not self.clicked:
            self.surface.blit(self.image, self.rect)

    def is_clicked(self, pos):
        if not self.clicked and self.rect.collidepoint(pos):
            self.clicked = True
            return True
        return False

    def scale_image(self, width, height):
        self.image = pygame.image.load(self.image_path)  # Reload original image
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

class Textbox:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 200, 30)
        self.text = ""
        self.active = False
        self.color = (230, 0, 0)
        self.visible = True

    def handle_event(self, event):
        if self.visible:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                self.color = (255, 0, 0) if self.active else (100, 150, 0)

            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.color, self.rect, 2)
            font = pygame.font.Font(None, 36)
            text_surface = font.render(self.text, True, (0, 0, 0))
            screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def get_text(self):
        return self.text


class SkærmTæller:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("musik.mp3")
        pygame.mixer.music.play(-1)
        self.sound = pygame.mixer.Sound("Ny stickman joe mp3/Goe siger tak.mp3")
        self.sound_1 = pygame.mixer.Sound("Ny stickman joe mp3/Joe stol.mp3")
        self.sound_2 = pygame.mixer.Sound("Ny stickman joe mp3/Joes cement.mp3")
        self.sound_3 = pygame.mixer.Sound("Ny stickman joe mp3/Joes gren.mp3")
        self.sound_4 = pygame.mixer.Sound("Ny stickman joe mp3/Joes sten.mp3")
        self.sound_5 = pygame.mixer.Sound("Ny stickman joe mp3/Joe æg.mp3")
        self.sound_6 = pygame.mixer.Sound("Ny stickman joe mp3/Joe mælk.mp3")
        self.sound_7 = pygame.mixer.Sound("Ny stickman joe mp3/Joe æble.mp3")
        self.sound_8 = pygame.mixer.Sound("Ny stickman joe mp3/Joes banan.mp3")
        self.sound_9 = pygame.mixer.Sound("Ny stickman joe mp3/Joe forklarer tekstboks minigame.mp3")
        self.sound_10 = pygame.mixer.Sound("Ny stickman joe mp3/Tryk på nøglen.mp3")
        self.sound_11 = pygame.mixer.Sound("Ny stickman joe mp3/Tutorial højre knap.mp3")
        self.sound_12 = pygame.mixer.Sound("Ny stickman joe mp3/Joe kan ikke finde sin nøgle.mp3")
        self.sound_13 = pygame.mixer.Sound("Ny stickman joe mp3/Joe siger tak og skal finde sin indkøbsliste.mp3")
        self.sound_14 = pygame.mixer.Sound("Ny stickman joe mp3/Indkøbsliste varer.mp3")
        self.sound_15 = pygame.mixer.Sound("Ny stickman joe mp3/Tryk på ord på liste.mp3")
        self.sound_played = False
        self.skaerm_bredde = 1300
        self.skaerm_hoejde = 800
        self.skaerm = pygame.display.set_mode((self.skaerm_bredde, self.skaerm_hoejde))
        pygame.display.set_caption("Skærmtæller")
        self.font = pygame.font.SysFont(None, 30)
        self.koerer = True
        self.nuvaerende_skaerm = 0
        self.skaerm_stack = []


        self.start_button = Button(self.skaerm, "start_knap.png", 400, 275, 250, 250, "Start")

        self.left_button = Button(self.skaerm, "Venstre_knap.png", 50, self.skaerm_hoejde/2-100, 50, 200)
        self.right_button = Button(self.skaerm, "Hjre_pil.png", 1200, self.skaerm_hoejde/2-100, 50, 200)


        self.key1 = Key(self.skaerm, "KEy_1.png", self.skaerm_bredde / 2, self.skaerm_hoejde / 2, 30, 30)
        self.key2 = Key(self.skaerm, "KEy_2.png", 450, 660, 30, 30)
        self.key3 = Key(self.skaerm, "papir.png", 580, 460)

        self.key1_clicked = False
        self.key2_clicked = False
        self.key3_clicked = False

        self.screen_4_button = Button(self.skaerm, "Hjre_pil.png", 255, 440, 50, 35, "Æg")
        self.screen_5_button = Button(self.skaerm, "Hjre_pil.png", 250, 350, 75, 40, "Æble")
        self.screen_6_button = Button(self.skaerm, "Hjre_pil.png", 250, 280, 75, 49, "Mælk")
        self.screen_9_button = Button(self.skaerm, "Hjre_pil.png", 250, 390, 90, 40, "Banan")
        self.screen_10_button = Button(self.skaerm, "Hjre_pil.png", 250, 480, 75, 40, "Sten")
        self.screen_11_button = Button(self.skaerm, "Hjre_pil.png", 250, 525, 75, 40, "Gren")
        self.screen_12_button = Button(self.skaerm, "Hjre_pil.png", 250, 310, 75, 40, "Stol")
        self.screen_13_button = Button(self.skaerm, "Hjre_pil.png", 250, 570, 115, 40, "Cement")

        self.buttons_clicked = {self.screen_4_button: False,
                                self.screen_5_button: False,
                                self.screen_6_button: False,
                                self.screen_9_button: False}

        self.screen_14_button = Button(self.skaerm, "box_til_ord.png", 1000, 400, 50, 50, "Bold")
        self.screen_15_button = Button(self.skaerm, "box_til_ord.png", 450, 400, 50, 50, "Hold")
        self.screen_16_button = Button(self.skaerm, "box_til_ord.png", 820, 400, 50, 50, "Hop")
        self.screen_17_button = Button(self.skaerm, "box_til_ord.png", 450, 265, 50, 50, "Op")
        self.screen_18_button = Button(self.skaerm, "box_til_ord.png", 920, 475, 50, 50, "Skål")
        self.screen_19_button = Button(self.skaerm, "box_til_ord.png", 450, 320, 50, 50, "Mål")
        self.screen_20_button = Button(self.skaerm, "box_til_ord.png", 820, 475, 79, 50, "Trommer")
        self.screen_21_button = Button(self.skaerm, "box_til_ord.png", 450, 475, 79, 50, "Sommer")
        self.screen_22_button = Button(self.skaerm, "box_til_ord.png", 920, 300, 50, 50, "Kat")
        self.screen_23_button = Button(self.skaerm, "box_til_ord.png", 450, 190, 50, 50, "At")
        self.screen_24_button = Button(self.skaerm, "box_til_ord.png", 1000, 200, 50, 50, "Granit")
        self.screen_25_button = Button(self.skaerm, "box_til_ord.png", 920, 200, 50, 50, "Kamel")
        self.screen_26_button = Button(self.skaerm, "box_til_ord.png", 820, 300, 50, 50, "Fedt")
        self.screen_27_button = Button(self.skaerm, "box_til_ord.png", 920, 400, 50, 50, "Kanin")
        self.screen_28_button = Button(self.skaerm, "box_til_ord.png", 820, 200, 50, 50, "Måne")

        self.screen_29_button = Button(self.skaerm, "box_til_ord.png", 1150, 200, 50, 50, "Fandt")
        self.screen_30_button = Button(self.skaerm, "box_til_ord.png", 140, 250, 50, 50, "Blandt")
        self.screen_31_button = Button(self.skaerm, "box_til_ord.png", 1000, 400, 50, 50, "Hund")
        self.screen_32_button = Button(self.skaerm, "box_til_ord.png", 220, 300, 50, 50, "Stund")
        self.screen_33_button = Button(self.skaerm, "box_til_ord.png", 1000, 300, 50, 50, "Stråle")
        self.screen_34_button = Button(self.skaerm, "box_til_ord.png", 200, 100, 50, 50, "Åle")
        self.screen_35_button = Button(self.skaerm, "box_til_ord.png", 910, 200, 80, 50, "Ballade")
        self.screen_36_button = Button(self.skaerm, "box_til_ord.png", 150, 400, 110, 50, "Marmelade")
        self.screen_37_button = Button(self.skaerm, "box_til_ord.png", 1000, 100, 50, 50, "Hest")
        self.screen_38_button = Button(self.skaerm, "box_til_ord.png", 220, 200, 50, 50, "Bedst")
        self.screen_39_button = Button(self.skaerm, "box_til_ord.png", 1150, 300, 50, 50, "Østers")
        self.screen_40_button = Button(self.skaerm, "box_til_ord.png", 1150, 100, 50, 50, "Bavian")
        self.screen_41_button = Button(self.skaerm, "box_til_ord.png", 900, 300, 50, 50, "Mand")
        self.screen_42_button = Button(self.skaerm, "box_til_ord.png", 1150, 400, 50, 50, "Joe")
        self.screen_43_button = Button(self.skaerm, "box_til_ord.png", 1060, 200, 50, 50, "Bord")

        self.textbox = Textbox(800, 580)
        self.textbox1 = Textbox(370, 330)
        self.textbox2 = Textbox(800, 330)
        self.textbox3 = Textbox(370, 580)



        self.right_button_active = False

        button_names = [
            "button_14_clicked",
            "button_15_clicked",
            "button_16_clicked",
            "button_17_clicked",
            "button_18_clicked",
            "button_19_clicked",
            "button_20_clicked",
            "button_21_clicked",
            "button_22_clicked",
            "button_23_clicked",
            "button_29_clicked",
            "button_30_clicked",
            "button_31_clicked",
            "button_32_clicked",
            "button_33_clicked",
            "button_34_clicked",
            "button_35_clicked",
            "button_36_clicked",
            "button_37_clicked",
            "button_38_clicked"
        ]

        for button_name in button_names:
            setattr(self, button_name, False)

        self.message_printed = False
        self.message2_printed = False
        self.message3_printed = False
        self.message4_printed = False
        self.message5_printed = False
        self.message6_printed = False
        self.message7_printed = False
        self.message8_printed = False
        self.message9_printed = False
        self.message10_printed = False

        self.point_6 = 0
        self.point_9 = 0
        self.correct_count = 0
        self.right_button_active = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.koerer = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if len(self.skaerm_stack) > 0:
                        self.nuvaerende_skaerm = self.skaerm_stack.pop()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.nuvaerende_skaerm == 0:
                    if event.button == pygame.BUTTON_LEFT and self.start_button.is_over(event.pos):
                        self.nuvaerende_skaerm = 1
                elif self.nuvaerende_skaerm >= 1:
                    if event.button == pygame.BUTTON_LEFT and self.right_button.is_over(event.pos):
                        self.nuvaerende_skaerm += 1
                        self.skaerm_stack.append(self.nuvaerende_skaerm - 1)
                        if self.nuvaerende_skaerm == 2:
                            self.key1_clicked = False

                        elif self.nuvaerende_skaerm == 3:
                            self.key2_clicked = False

                        elif self.nuvaerende_skaerm == 4:
                            self.key3_clicked = False

                            for button in self.buttons_clicked:
                                self.buttons_clicked[button] = False
                        elif self.nuvaerende_skaerm == 6:
                            self.right_button_active = False
                    elif event.button == pygame.BUTTON_LEFT and self.left_button.is_over(event.pos):
                        if self.nuvaerende_skaerm != 1:
                            self.nuvaerende_skaerm -= 1
                    elif event.button == pygame.BUTTON_LEFT and self.key1.is_clicked(event.pos):
                        self.key1_clicked = True
                        print("The first key has been clicked")
                        if self.sound_11:
                            self.sound_11.play()
                            self.sound_11 = False

                    elif event.button == pygame.BUTTON_LEFT and self.key2.is_clicked(event.pos):
                        self.key2_clicked = True
                        print("The second key has been clicked")
                        if self.sound_13:
                            self.sound_13.play()
                            self.sound_13 = False

                    elif event.button == pygame.BUTTON_LEFT and self.key3.is_clicked(event.pos):
                        self.key3_clicked = True
                        print("The third key has been clicked")
                        if self.sound_14:
                            self.sound_14.play()
                            self.sound_14 = False


                    elif self.nuvaerende_skaerm == 6:
                        button_map = {
                            "button_14_clicked": self.screen_14_button,
                            "button_15_clicked": self.screen_15_button,
                            "button_16_clicked": self.screen_16_button,
                            "button_17_clicked": self.screen_17_button,
                            "button_18_clicked": self.screen_18_button,
                            "button_19_clicked": self.screen_19_button,
                            "button_20_clicked": self.screen_20_button,
                            "button_21_clicked": self.screen_21_button,
                            "button_22_clicked": self.screen_22_button,
                            "button_23_clicked": self.screen_23_button
                        }

                        for button_name, screen_button in button_map.items():
                            if screen_button.is_over(event.pos):
                                setattr(self, button_name, True)

                        if self.button_14_clicked and self.button_15_clicked and not self.message_printed:
                            print("Bold og hold")
                            self.message_printed = True
                            self.point_6 += 1
                            self.screen_14_button.set_inactive()
                            self.screen_15_button.set_inactive()
                        if self.button_16_clicked and self.button_17_clicked and not self.message2_printed:
                            print("Hop og op")
                            self.message2_printed = True
                            self.point_6 += 1
                            self.screen_16_button.set_inactive()
                            self.screen_17_button.set_inactive()
                        if self.button_18_clicked and self.button_19_clicked and not self.message3_printed:
                            print("Skål og mål")
                            self.message3_printed = True
                            self.point_6 += 1
                            self.screen_18_button.set_inactive()
                            self.screen_19_button.set_inactive()
                        if self.button_20_clicked and self.button_21_clicked and not self.message4_printed:
                            print("Trommer og sommer")
                            self.message4_printed = True
                            self.point_6 += 1
                            self.screen_20_button.set_inactive()
                            self.screen_21_button.set_inactive()
                        if self.button_22_clicked and self.button_23_clicked and not self.message5_printed:
                            print("Kat og at")
                            self.message5_printed = True
                            self.point_6 += 1
                            self.screen_22_button.set_inactive()
                            self.screen_23_button.set_inactive()

                    elif self.nuvaerende_skaerm == 9:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.screen_29_button.is_over(event.pos):
                                self.button_29_clicked = True
                            if self.screen_30_button.is_over(event.pos):
                                self.button_30_clicked = True
                            if self.screen_31_button.is_over(event.pos):
                                self.button_31_clicked = True
                            if self.screen_32_button.is_over(event.pos):
                                self.button_32_clicked = True
                            if self.screen_33_button.is_over(event.pos):
                                self.button_33_clicked = True
                            if self.screen_34_button.is_over(event.pos):
                                self.button_34_clicked = True
                            if self.screen_35_button.is_over(event.pos):
                                self.button_35_clicked = True
                            if self.screen_36_button.is_over(event.pos):
                                self.button_36_clicked = True
                            if self.screen_37_button.is_over(event.pos):
                                self.button_37_clicked = True
                            if self.screen_38_button.is_over(event.pos):
                                self.button_38_clicked = True

                        if self.button_29_clicked and self.button_30_clicked and not self.message6_printed:
                            print("Fandt og blandt")
                            self.message6_printed = True
                            self.point_9 += 1
                            self.screen_29_button.set_inactive()
                            self.screen_30_button.set_inactive()
                        if self.button_31_clicked and self.button_32_clicked and not self.message7_printed:
                            print("Hund og stund")
                            self.message7_printed = True
                            self.point_9 += 1
                            self.screen_31_button.set_inactive()
                            self.screen_32_button.set_inactive()
                        if self.button_33_clicked and self.button_34_clicked and not self.message8_printed:
                            print("Stråle og åle")
                            self.message8_printed = True
                            self.point_9 += 1
                            self.screen_33_button.set_inactive()
                            self.screen_34_button.set_inactive()
                        if self.button_35_clicked and self.button_36_clicked and not self.message9_printed:
                            print("Ballade og marmelade")
                            self.message9_printed = True
                            self.point_9 += 1
                            self.screen_35_button.set_inactive()
                            self.screen_36_button.set_inactive()
                        if self.button_37_clicked and self.button_38_clicked and not self.message10_printed:
                            print("Hest og bedst")
                            self.message10_printed = True
                            self.point_9 += 1
                            self.screen_37_button.set_inactive()
                            self.screen_38_button.set_inactive()

            # Handle textbox inputs
            self.textbox.handle_event(event)
            self.textbox1.handle_event(event)
            self.textbox2.handle_event(event)
            self.textbox3.handle_event(event)

            if self.textbox2.get_text().lower() == "æble":
                print("Korrekt! Du indtastede 'Æble'. Yderligere input deaktiveret.")
                self.textbox2.visible = False
                self.textbox2.text = ""
                self.correct_count += 1
            if self.textbox.get_text().lower() == "banan":
                print("Korrekt! Du indtastede 'Banan'. Yderligere input deaktiveret.")
                self.textbox.visible = False
                self.textbox.text = ""
                self.correct_count += 1

            if self.textbox1.get_text().lower() == "mælk":
                print("Korrekt! Du indtastede 'Mælk'. Yderligere input deaktiveret.")
                self.textbox1.visible = False
                self.textbox1.text = ""
                self.correct_count += 1

            if self.textbox3.get_text().lower() == "æg":
                print("Korrekt! Du indtastede 'Æg'. Yderligere input deaktiveret.")
                self.textbox3.visible = False
                self.textbox3.text = ""
                self.correct_count += 1

            elif self.nuvaerende_skaerm == 9:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.screen_29_button.is_over(event.pos):
                        self.button_29_clicked = True
                    if self.screen_30_button.is_over(event.pos):
                        self.button_30_clicked = True
                    if self.screen_31_button.is_over(event.pos):
                        self.button_31_clicked = True
                    if self.screen_32_button.is_over(event.pos):
                        self.button_32_clicked = True
                    if self.screen_33_button.is_over(event.pos):
                        self.button_33_clicked = True
                    if self.screen_34_button.is_over(event.pos):
                        self.button_34_clicked = True
                    if self.screen_35_button.is_over(event.pos):
                        self.button_35_clicked = True
                    if self.screen_36_button.is_over(event.pos):
                        self.button_36_clicked = True
                    if self.screen_37_button.is_over(event.pos):
                        self.button_37_clicked = True
                    if self.screen_38_button.is_over(event.pos):
                        self.button_38_clicked = True






    def draw_screen(self):
        if self.nuvaerende_skaerm == 0:
            background_img = pygame.image.load("Startskrm_eksamensprojekt.png")
            background_img = pygame.transform.scale(background_img, (self.skaerm_bredde, self.skaerm_hoejde))
            self.skaerm.blit(background_img, (0, 0))
            self.start_button.active = True
            self.start_button.draw()

        elif self.nuvaerende_skaerm >= 1 and self.nuvaerende_skaerm < 4:
            if self.nuvaerende_skaerm == 1:
                background_img_3 = pygame.image.load("Grafisk baggrund/Level_select.png")
                background_img_3 = pygame.transform.scale(background_img_3, (self.skaerm_bredde, self.skaerm_hoejde))
                self.skaerm.blit(background_img_3, (0, 0))
                if not self.key1_clicked:
                    self.key1.draw_key()
                if self.sound_10:
                    self.sound_10.play()
                    self.sound_10 = False


            elif self.nuvaerende_skaerm == 2:
                self.skaerm.fill((255, 0, 0))
                background_img_2 = pygame.image.load("Grafisk baggrund/inden_i_Joes_house_ny.png")
                background_img_2 = pygame.transform.scale(background_img_2, (self.skaerm_bredde, self.skaerm_hoejde))
                self.skaerm.blit(background_img_2, (0, 0))
                if not self.key2_clicked:
                    self.key2.draw_key()
                if self.sound_12:
                    self.sound_12.play()
                    self.sound_12 = False

            elif self.nuvaerende_skaerm == 3:
                self.skaerm.fill((0, 255, 0))
                background_img_4 = pygame.image.load("Grafisk baggrund/inden_i_Joes_house_ny.png")
                background_img_4 = pygame.transform.scale(background_img_4, (self.skaerm_bredde, self.skaerm_hoejde))
                self.skaerm.blit(background_img_4, (0, 0))
                if not self.key3_clicked:
                    self.key3.draw_key()

            if self.nuvaerende_skaerm != 1:
                self.left_button.active = True
                self.left_button.color = (0, 0, 0)
                self.left_button.draw()

            if self.nuvaerende_skaerm == 1 and self.key1.clicked:
                self.right_button.active = True
                self.right_button.draw()
            elif self.nuvaerende_skaerm == 2 and self.key2.clicked:
                self.right_button.active = True
                self.right_button.draw()
            elif self.nuvaerende_skaerm == 3 and self.key3.clicked:
                self.right_button.active = True
                self.right_button.draw()
            else:
                self.right_button.active = False


        elif self.nuvaerende_skaerm == 4:
            self.skaerm.fill((0, 0, 255))
            self.left_button.color = (0, 0, 0)
            self.left_button.draw()
            self.screen_4_button.draw()
            self.screen_5_button.draw()
            self.screen_6_button.draw()
            self.screen_9_button.draw()
            self.screen_10_button.draw()
            self.screen_11_button.draw()
            self.screen_12_button.draw()
            self.screen_13_button.draw()
            background_img_5 = pygame.image.load("Grafisk baggrund/Indkbsliste.png")
            background_img_5 = pygame.transform.scale(background_img_5, (self.skaerm_bredde, self.skaerm_hoejde))
            self.skaerm.blit(background_img_5, (0, 0))
            if self.sound_15:
                self.sound_15.play()
                self.sound_15 = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.screen_10_button.is_over(event.pos):
                        print("Click Sten")
                        self.sound_4.play()
                    elif self.screen_11_button.is_over(event.pos):
                        print("Click Gren")
                        self.sound_3.play()
                    elif self.screen_12_button.is_over(event.pos):
                        print("Click Stol")
                        self.sound_1.play()
                    elif self.screen_13_button.is_over(event.pos):
                        print("Click Cement")
                        self.sound_2.play()
                    elif self.screen_4_button.is_over(event.pos):
                        print("Click Æg")
                        self.sound_5.play()
                        self.buttons_clicked[self.screen_4_button] = True
                    elif self.screen_5_button.is_over(event.pos):
                        print("Click Æble")
                        self.sound_7.play()
                        self.buttons_clicked[self.screen_5_button] = True
                    elif self.screen_6_button.is_over(event.pos):
                        print("Click Mælk")
                        self.sound_6.play()
                        self.buttons_clicked[self.screen_6_button] = True
                    elif self.screen_9_button.is_over(event.pos):
                        print("Click Banan")
                        self.sound_8.play()
                        self.buttons_clicked[self.screen_9_button] = True
                    # Check if all required buttons have been clicked
                    if all(self.buttons_clicked.values()):
                        print("All buttons on screen 4 have been clicked")
                        self.right_button_active = True
                    else:
                        self.right_button_active = False
                if self.right_button_active and event.type == pygame.MOUSEBUTTONDOWN:
                    if self.right_button.is_over(event.pos):
                        self.nuvaerende_skaerm += 1
            if self.right_button_active:
                self.right_button.active = True
                self.right_button.color = (0, 0, 0)
            else:
                self.right_button.active = False
                self.right_button.color = (100, 100, 100)
            self.right_button.draw()



        elif self.nuvaerende_skaerm == 5:
            self.skaerm.fill((255, 255, 0))
            skaermtal_tekst = self.font.render(f"Skærm {self.nuvaerende_skaerm}", True, (0, 0, 0))
            self.skaerm.blit(skaermtal_tekst, (self.skaerm_bredde // 2 - skaermtal_tekst.get_width() // 2, 20))
            background_img_4 = pygame.image.load("Grafisk baggrund/cykel_scene_ny.png")
            background_img_4 = pygame.transform.scale(background_img_4, (self.skaerm_bredde, self.skaerm_hoejde))
            self.skaerm.blit(background_img_4, (0, 0))
            self.left_button.active = True
            self.left_button.color = (0, 0, 0)
            self.left_button.draw()
            self.right_button.active = True
            self.right_button.color = (0, 0, 0)
            self.right_button.draw()

        elif self.nuvaerende_skaerm == 6:
            background_img_4 = pygame.image.load("Grafisk baggrund/Park_rap_battle_park_ny.png")
            background_img_4 = pygame.transform.scale(background_img_4, (self.skaerm_bredde, self.skaerm_hoejde))
            self.skaerm.blit(background_img_4, (0, 0))
            self.screen_14_button.draw()
            self.screen_15_button.draw()
            self.screen_16_button.draw()
            self.screen_17_button.draw()
            self.screen_18_button.draw()
            self.screen_19_button.draw()
            self.screen_20_button.draw()
            self.screen_21_button.draw()
            self.screen_22_button.draw()
            self.screen_23_button.draw()
            self.screen_24_button.draw()
            self.screen_25_button.draw()
            self.screen_26_button.draw()
            self.screen_27_button.draw()
            self.screen_28_button.draw()

            skaermtal_tekst = self.font.render(f"Skærm {self.nuvaerende_skaerm}", True, (0, 0, 0))
            self.skaerm.blit(skaermtal_tekst, (self.skaerm_bredde // 2 - skaermtal_tekst.get_width() // 2, 20))

            self.left_button.active = True
            self.left_button.color = (0, 0, 0)
            self.left_button.draw()

            if self.point_6 == 5:
                self.right_button.active = True
                self.right_button.color = (0, 0, 0)
                self.right_button.draw()
            else:
                self.right_button.active = False


        elif self.nuvaerende_skaerm == 7:
            self.skaerm.fill((0, 255, 255))
            skaermtal_tekst = self.font.render(f"Skærm {self.nuvaerende_skaerm}", True, (0, 0, 0))
            self.skaerm.blit(skaermtal_tekst, (self.skaerm_bredde // 2 - skaermtal_tekst.get_width() // 2, 20))
            background_img_4 = pygame.image.load("Grafisk baggrund/Otten_front_ny.png")
            background_img_4 = pygame.transform.scale(background_img_4, (self.skaerm_bredde, self.skaerm_hoejde))
            self.skaerm.blit(background_img_4, (0, 0))
            self.left_button.active = True
            self.left_button.color = (0, 0, 0)
            self.left_button.draw()
            self.right_button.active = True
            self.right_button.color = (0, 0, 0)
            self.right_button.draw()

        elif self.nuvaerende_skaerm == 8:
            if self.sound_9:
                self.sound_9.play()
                self.sound_9 = False
            self.skaerm.fill((0, 255, 255))
            background_img_4 = pygame.image.load("Grafisk baggrund/Inden_i_butikken_nye_figuer.png")
            background_img_4 = pygame.transform.scale(background_img_4, (self.skaerm_bredde, self.skaerm_hoejde))
            self.skaerm.blit(background_img_4, (0, 0))
            self.textbox.draw(self.skaerm)
            self.textbox1.draw(self.skaerm)
            self.textbox2.draw(self.skaerm)
            self.textbox3.draw(self.skaerm)
            skaermtal_tekst = self.font.render(f"Skærm {self.nuvaerende_skaerm}", True, (0, 0, 0))
            self.skaerm.blit(skaermtal_tekst, (self.skaerm_bredde // 2 - skaermtal_tekst.get_width() // 2, 20))
            self.left_button.active = True
            self.left_button.color = (0, 0, 0)
            self.left_button.draw()

            if self.correct_count == 4:
                self.right_button.active = True
                self.right_button.color = (0, 0, 0)
                self.right_button.draw()
            else:
                self.right_button.active = False

        elif self.nuvaerende_skaerm == 9:
            self.skaerm.fill((0, 255, 79))
            background_img_4 = pygame.image.load("Grafisk baggrund/Kasse_damen_rim_boks_rykket.png")
            background_img_4 = pygame.transform.scale(background_img_4, (self.skaerm_bredde, self.skaerm_hoejde))
            self.skaerm.blit(background_img_4, (0, 0))
            self.screen_29_button.draw()
            self.screen_30_button.draw()
            self.screen_31_button.draw()
            self.screen_32_button.draw()
            self.screen_33_button.draw()
            self.screen_34_button.draw()
            self.screen_35_button.draw()
            self.screen_36_button.draw()
            self.screen_37_button.draw()
            self.screen_38_button.draw()
            self.screen_39_button.draw()
            self.screen_40_button.draw()
            self.screen_41_button.draw()
            self.screen_42_button.draw()
            self.screen_43_button.draw()

            skaermtal_tekst = self.font.render(f"Skærm {self.nuvaerende_skaerm}", True, (0, 0, 0))
            self.skaerm.blit(skaermtal_tekst, (self.skaerm_bredde // 2 - skaermtal_tekst.get_width() // 2, 20))


            self.left_button.active = True
            self.left_button.color = (0, 0, 0)
            self.left_button.draw()

            if self.point_9 == 5:
                self.right_button.active = True
                self.right_button.color = (0, 0, 0)
                self.right_button.draw()
                if self.sound:
                    self.sound.play()
                    self.sound = False
            else:
                self.right_button.active = False

        if self.nuvaerende_skaerm == 10:
            self.skaerm.fill((0, 0, 0))
            self.left_button.active = False

        pygame.display.flip()

    def run(self):
        while self.koerer:
            self.handle_events()
            self.draw_screen()
            pygame.display.flip()

if __name__ == "__main__":
    app = SkærmTæller()
    app.run()
    spil = SkærmTæller()