import pygame
import sys
import os

pygame.init()

#Image Library
_image_library = {}
def get_image(path):
        global _image_library
        global v
        v = 0.75
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                image = pygame.transform.rotozoom(image, 0, v)
                _image_library[path] = image
        return image


screen = pygame.display.set_mode((900, 750), pygame.RESIZABLE)
img = pygame.image.load('ImageCalibrator1.png').convert()
done = False
Quit = False
ReSizeHold = False
Strawberry = True
Blueberry = True
Pineapple = True
Banana = True
DragStrawberry = False
DragBlueberry = False
DragPineapple = False
DragBanana = False
Restart = False
clock = pygame.time.Clock()
pressed = pygame.key.get_pressed()
StrawberryDrag_x = 0
StrawberryDrag_y = 0
StrawberryDragPoint_x = 0
StrawberryDragPoint_y = 0
BlueberryDrag_x = 0
BlueberryDrag_y = 0
BlueberryDragPoint_x = 0
BlueberryDragPoint_y = 0
PineappleDrag_x = 0
PineappleDrag_y = 0
PineappleDragPoint_x = 0
PineappleDragPoint_y = 0
BananaDrag_x = 0
BananaDrag_y = 0
BananaDragPoint_x = 0
BananaDragPoint_y = 0
show = 'Blender'
MouseDrag = 'None'
Blender1 = 'None'
Blender2 = 'None'
Blender3 = 'None'
Blender4 = 'None'
Smuuuuuuthie = []

while not done:
    #Mouse Coordinates
    Mouse_x, Mouse_y = pygame.mouse.get_pos()

    #Size of Window
    SWidth, SHeight = pygame.display.get_surface().get_size()

    screen.fill((255, 255, 255))

    if show == 'Blender' or show == 'Blend':

        screen.blit(get_image('Blender.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))

        if Blender1 == 'Strawberry':
            screen.blit(get_image('BlenderStrawberry1.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif Blender1 == 'Blueberry':
            screen.blit(get_image('BlenderBlueberry1.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif Blender1 == 'Pineapple':
            screen.blit(get_image('BlenderPineapple1.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif Blender1 == 'Banana':
            screen.blit(get_image('BlenderBanana1.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))

        if Blender2 == 'Strawberry':
            screen.blit(get_image('BlenderStrawberry2.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif Blender2 == 'Blueberry':
            screen.blit(get_image('BlenderBlueberry2.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif Blender2 == 'Pineapple':
            screen.blit(get_image('BlenderPineapple2.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif Blender2 == 'Banana':
            screen.blit(get_image('BlenderBanana2.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))

        if Blender3 == 'Strawberry':
            screen.blit(get_image('BlenderStrawberry3.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif Blender3 == 'Blueberry':
            screen.blit(get_image('BlenderBlueberry3.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif Blender3 == 'Pineapple':
            screen.blit(get_image('BlenderPineapple3.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif Blender3 == 'Banana':
            screen.blit(get_image('BlenderBanana3.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))

        if Blender4 == 'Strawberry':
            screen.blit(get_image('BlenderStrawberry4.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif Blender4 == 'Blueberry':
            screen.blit(get_image('BlenderBlueberry4.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif Blender4 == 'Pineapple':
            screen.blit(get_image('BlenderPineapple4.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif Blender4 == 'Banana':
            screen.blit(get_image('BlenderBanana4.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))

        screen.blit(get_image('BlenderOverlay.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        screen.blit(get_image('Title.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))


        if Banana:
            screen.blit(get_image('Banana.png'), ((SWidth/2) + (v * img.get_width())/5 + BananaDrag_x, (SHeight/3) - (v * img.get_height())/75 + BananaDrag_y))

        if Pineapple:
            screen.blit(get_image('Pineapple.png'), ((SWidth/2) - (v * img.get_width())/6 + PineappleDrag_x, (SHeight/3) - (v * img.get_height())/75 + PineappleDrag_y))

        if Blueberry:
            screen.blit(get_image('Blueberry.png'), ((SWidth/2) - (v * img.get_width())/0.9 + BlueberryDrag_x, (SHeight/3) - (v * img.get_height())/75 + BlueberryDrag_y))

        if Strawberry:
            screen.blit(get_image('Strawberry.png'), ((SWidth/2) - (v * img.get_width())/1.25 + StrawberryDrag_x, (SHeight/3) - (v * img.get_height())/75 + StrawberryDrag_y))

        pygame.display.flip()

        if Mouse_x >= (SWidth/2) - (v * img.get_width())/10.5 and Mouse_y >= (SHeight/3) + (v * img.get_height())/2.6 and Mouse_x <= ((SWidth/2) - (v * img.get_width())/10.5) + (v * img.get_width())/5.5 and Mouse_y <= ((SHeight/3) + (v * img.get_height())/2.6) + (v * img.get_height())/13.5:
            show = 'Blend'
        elif Mouse_x >= (SWidth/2) - (v * img.get_width())/2.325 + StrawberryDrag_x and Mouse_y >= (SHeight/3) + (v * img.get_height())/3.12 + StrawberryDrag_y and Mouse_x <= ((SWidth/2) - (v * img.get_width())/2.325) + (v * img.get_width())/3.7 + StrawberryDrag_x and Mouse_y <= ((SHeight/3) + (v * img.get_height())/3.12) + (v * img.get_height())/3 + StrawberryDrag_y and Strawberry:
            MouseDrag = 'MouseStrawberry'
        elif Mouse_x >= (SWidth/2) - (v * img.get_width())/1.305 + BlueberryDrag_x and Mouse_y >= (SHeight/3) + (v * img.get_height())/3 + BlueberryDrag_y and Mouse_x <= ((SWidth/2) - (v * img.get_width())/1.305) + (v * img.get_width())/3.2 + BlueberryDrag_x and Mouse_y <= ((SHeight/3) + (v * img.get_height())/3) + (v * img.get_height())/3.25 + BlueberryDrag_y and Blueberry:
            MouseDrag = 'MouseBlueberry'
        elif Mouse_x >= (SWidth/2) + (v * img.get_width())/8.5 + PineappleDrag_x and Mouse_y >= (SHeight/3) + (v * img.get_height())/2.8 + PineappleDrag_y and Mouse_x <= ((SWidth/2) + (v * img.get_width())/8.5) + (v * img.get_width())/3.2 + PineappleDrag_x and Mouse_y <= ((SHeight/3) + (v * img.get_height())/2.8) + (v * img.get_height())/3.5 + PineappleDrag_y and Pineapple:
            MouseDrag = 'MousePineapple'
        elif Mouse_x >= (SWidth/2) + (v * img.get_width())/1.75 + BananaDrag_x and Mouse_y >= (SHeight/3) + (v * img.get_height())/3.85 + BananaDrag_y and Mouse_x <= ((SWidth/2) + (v * img.get_width())/1.75) + (v * img.get_width())/4 + BananaDrag_x and Mouse_y <= ((SHeight/3) + (v * img.get_width())/3.85) + (v * img.get_height())/2.2 + BananaDrag_y and Banana:
            MouseDrag = 'MouseBanana'
        else:
            show = 'Blender'
            MouseDrag = 'None'

    elif show == 'Smuuuuuuthie!!!':
        screen.fill((255, 255, 255))

        if Blender1 == 'Strawberry' or Blender2 == 'Strawberry' or Blender3 == 'Strawberry' or Blender4 == 'Strawberry':
            Smuuuuuuthie.append('Strawberry')

        if Blender1 == 'Blueberry' or Blender2 == 'Blueberry' or Blender3 == 'Blueberry' or Blender4 == 'Blueberry':
            Smuuuuuuthie.append('Blueberry')

        if Blender1 == 'Pineapple' or Blender2 == 'Pineapple' or Blender3 == 'Pineapple' or Blender4 == 'Pineapple':
            Smuuuuuuthie.append('Pineapple')

        if Blender1 == 'Banana' or Blender2 == 'Banana' or Blender3 == 'Banana' or Blender4 == 'Banana':
            Smuuuuuuthie.append('Banana')



        if 'Strawberry' in Smuuuuuuthie and 'Blueberry' not in Smuuuuuuthie and 'Pineapple' not in Smuuuuuuthie and 'Banana' not in Smuuuuuuthie:
            screen.blit(get_image('StrawberrySmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' in Smuuuuuuthie and 'Blueberry' in Smuuuuuuthie and 'Pineapple' not in Smuuuuuuthie and 'Banana' not in Smuuuuuuthie:
            screen.blit(get_image('StrawberryBlueberrySmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' in Smuuuuuuthie and 'Blueberry' not in Smuuuuuuthie and 'Pineapple' in Smuuuuuuthie and 'Banana' not in Smuuuuuuthie:
            screen.blit(get_image('StrawberryPineappleSmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' in Smuuuuuuthie and 'Blueberry' not in Smuuuuuuthie and 'Pineapple' not in Smuuuuuuthie and 'Banana' in Smuuuuuuthie:
            screen.blit(get_image('StrawberryBananaSmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' in Smuuuuuuthie and 'Blueberry' in Smuuuuuuthie and 'Pineapple' in Smuuuuuuthie and 'Banana' not in Smuuuuuuthie:
            screen.blit(get_image('StrawberryBlueberryPineappleSmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' in Smuuuuuuthie and 'Blueberry' in Smuuuuuuthie and 'Pineapple' not in Smuuuuuuthie and 'Banana' in Smuuuuuuthie:
            screen.blit(get_image('StrawberryBlueberryBananaSmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' in Smuuuuuuthie and 'Blueberry' not in Smuuuuuuthie and 'Pineapple' in Smuuuuuuthie and 'Banana' in Smuuuuuuthie:
            screen.blit(get_image('StrawberryPineappleBananaSmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' in Smuuuuuuthie and 'Blueberry' in Smuuuuuuthie and 'Pineapple' in Smuuuuuuthie and 'Banana' in Smuuuuuuthie:
            screen.blit(get_image('StrawberryBlueberryPineappleBananaSmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' not in Smuuuuuuthie and 'Blueberry' in Smuuuuuuthie and 'Pineapple' not in Smuuuuuuthie and 'Banana' not in Smuuuuuuthie:
            screen.blit(get_image('BlueberrySmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' not in Smuuuuuuthie and 'Blueberry' in Smuuuuuuthie and 'Pineapple' in Smuuuuuuthie and 'Banana' not in Smuuuuuuthie:
            screen.blit(get_image('BlueberryPineappleSmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' not in Smuuuuuuthie and 'Blueberry' in Smuuuuuuthie and 'Pineapple' not in Smuuuuuuthie and 'Banana' in Smuuuuuuthie:
            screen.blit(get_image('BlueberryBananaSmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' not in Smuuuuuuthie and 'Blueberry' in Smuuuuuuthie and 'Pineapple' in Smuuuuuuthie and 'Banana' in Smuuuuuuthie:
            screen.blit(get_image('BlueberryPineappleBananaSmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' not in Smuuuuuuthie and 'Blueberry' not in Smuuuuuuthie and 'Pineapple' in Smuuuuuuthie and 'Banana' not in Smuuuuuuthie:
            screen.blit(get_image('PineappleSmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' not in Smuuuuuuthie and 'Blueberry' not in Smuuuuuuthie and 'Pineapple' in Smuuuuuuthie and 'Banana' in Smuuuuuuthie:
            screen.blit(get_image('PineappleBananaSmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
        elif 'Strawberry' not in Smuuuuuuthie and 'Blueberry' not in Smuuuuuuthie and 'Pineapple' not in Smuuuuuuthie and 'Banana' in Smuuuuuuthie:
            screen.blit(get_image('BananaSmth.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))

        Restart = True
        pygame.display.flip()

    for event in pygame.event.get():

        if MouseDrag == 'MouseStrawberry' and event.type == pygame.MOUSEBUTTONDOWN:
            DragStrawberry = True

            if StrawberryDragPoint_x == 0 and StrawberryDragPoint_y == 0:
                StrawberryDragPoint_x = Mouse_x
                StrawberryDragPoint_y = Mouse_y
            else:
                StrawberryDragPoint_x += Mouse_x - StrawberryDragCheck_x
                StrawberryDragPoint_y += Mouse_y - StrawberryDragCheck_y

        if DragStrawberry and pygame.mouse.get_pressed()[0]:
            StrawberryDrag_x = Mouse_x - StrawberryDragPoint_x
            StrawberryDrag_y = Mouse_y - StrawberryDragPoint_y
        elif DragStrawberry and not pygame.mouse.get_pressed()[0]:
            DragStrawberry = False
            StrawberryDragCheck_x = Mouse_x
            StrawberryDragCheck_y = Mouse_y

            if Mouse_x >= (SWidth/2) - (v * img.get_width())/6.5 and Mouse_y >= (SHeight/3) - (v * img.get_height())/3 and Mouse_x <= ((SWidth/2) - (v * img.get_width())/6.5) + (v * img.get_width())/3.2 and Mouse_y <= ((SHeight/3) - (v * img.get_height())/3) + (v * img.get_height())/1.9:
                Strawberry = False

                if Blender1 != 'Blueberry' and Blender1 != 'Pineapple' and Blender1 != 'Banana':
                    Blender1 = 'Strawberry'

                elif Blender2 != 'Blueberry' and Blender2 != 'Pineapple' and Blender2 != 'Banana':
                    Blender2 = 'Strawberry'

                elif Blender3 != 'Blueberry' and Blender3 != 'Pineapple' and Blender3 != 'Banana':
                    Blender3 = 'Strawberry'

                else:
                    Blender4 = 'Strawberry'

        if MouseDrag == 'MouseBlueberry' and event.type == pygame.MOUSEBUTTONDOWN:
            DragBlueberry = True

            if BlueberryDragPoint_x == 0 and BlueberryDragPoint_y == 0:
                BlueberryDragPoint_x = Mouse_x
                BlueberryDragPoint_y = Mouse_y
            else:
                BlueberryDragPoint_x += Mouse_x - BlueberryDragCheck_x
                BlueberryDragPoint_y += Mouse_y - BlueberryDragCheck_y

        if DragBlueberry and pygame.mouse.get_pressed()[0]:
            BlueberryDrag_x = Mouse_x - BlueberryDragPoint_x
            BlueberryDrag_y = Mouse_y - BlueberryDragPoint_y
        elif DragBlueberry and not pygame.mouse.get_pressed()[0]:
            DragBlueberry = False
            BlueberryDragCheck_x = Mouse_x
            BlueberryDragCheck_y = Mouse_y

            if Mouse_x >= (SWidth/2) - (v * img.get_width())/6.5 and Mouse_y >= (SHeight/3) - (v * img.get_height())/3 and Mouse_x <= ((SWidth/2) - (v * img.get_width())/6.5) + (v * img.get_width())/3.2 and Mouse_y <= ((SHeight/3) - (v * img.get_height())/3) + (v * img.get_height())/1.9:
                Blueberry = False

                if Blender1 != 'Strawberry' and Blender1 != 'Pineapple' and Blender1 != 'Banana':
                    Blender1 = 'Blueberry'

                elif Blender2 != 'Strawberry' and Blender2 != 'Pineapple' and Blender2 != 'Banana':
                    Blender2 = 'Blueberry'

                elif Blender3 != 'Strawberry' and Blender3 != 'Pineapple' and Blender3 != 'Banana':
                    Blender3 = 'Blueberry'

                else:
                    Blender4 = 'Blueberry'

        if MouseDrag == 'MousePineapple' and event.type == pygame.MOUSEBUTTONDOWN:
            DragPineapple = True

            if PineappleDragPoint_x == 0 and PineappleDragPoint_y == 0:
                PineappleDragPoint_x = Mouse_x
                PineappleDragPoint_y = Mouse_y
            else:
                PineappleDragPoint_x += Mouse_x - PineappleDragCheck_x
                PineappleDragPoint_y += Mouse_y - PineappleDragCheck_y

        if DragPineapple and pygame.mouse.get_pressed()[0]:
            PineappleDrag_x = Mouse_x - PineappleDragPoint_x
            PineappleDrag_y = Mouse_y - PineappleDragPoint_y
        elif DragPineapple and not pygame.mouse.get_pressed()[0]:
            DragPineapple = False
            PineappleDragCheck_x = Mouse_x
            PineappleDragCheck_y = Mouse_y

            if Mouse_x >= (SWidth/2) - (v * img.get_width())/6.5 and Mouse_y >= (SHeight/3) - (v * img.get_height())/3 and Mouse_x <= ((SWidth/2) - (v * img.get_width())/6.5) + (v * img.get_width())/3.2 and Mouse_y <= ((SHeight/3) - (v * img.get_height())/3) + (v * img.get_height())/1.9:
                Pineapple = False

                if Blender1 != 'Blueberry' and Blender1 != 'Strawberry' and Blender1 != 'Banana':
                    Blender1 = 'Pineapple'

                elif Blender2 != 'Blueberry' and Blender2 != 'Strawberry' and Blender2 != 'Banana':
                    Blender2 = 'Pineapple'

                elif Blender3 != 'Blueberry' and Blender3 != 'Strawberry' and Blender3 != 'Banana':
                    Blender3 = 'Pineapple'

                else:
                    Blender4 = 'Pineapple'

        if MouseDrag == 'MouseBanana' and event.type == pygame.MOUSEBUTTONDOWN:
            DragBanana = True

            if BananaDragPoint_x == 0 and BananaDragPoint_y == 0:
                BananaDragPoint_x = Mouse_x
                BananaDragPoint_y = Mouse_y
            else:
                BananaDragPoint_x += Mouse_x - BananaDragCheck_x
                BananaDragPoint_y += Mouse_y - BananaDragCheck_y

        if DragBanana and pygame.mouse.get_pressed()[0]:
            BananaDrag_x = Mouse_x - BananaDragPoint_x
            BananaDrag_y = Mouse_y - BananaDragPoint_y
        elif DragBanana and not pygame.mouse.get_pressed()[0]:
            DragBanana = False
            BananaDragCheck_x = Mouse_x
            BananaDragCheck_y = Mouse_y

            if Mouse_x >= (SWidth/2) - (v * img.get_width())/6.5 and Mouse_y >= (SHeight/3) - (v * img.get_height())/3 and Mouse_x <= ((SWidth/2) - (v * img.get_width())/6.5) + (v * img.get_width())/3.2 and Mouse_y <= ((SHeight/3) - (v * img.get_height())/3) + (v * img.get_height())/1.9:
                Banana = False

                if Blender1 != 'Blueberry' and Blender1 != 'Pineapple' and Blender1 != 'Strawberry':
                    Blender1 = 'Banana'

                elif Blender2 != 'Blueberry' and Blender2 != 'Pineapple' and Blender2 != 'Strawberry':
                    Blender2 = 'Banana'

                elif Blender3 != 'Blueberry' and Blender3 != 'Pineapple' and Blender3 != 'Strawberry':
                    Blender3 = 'Banana'

                else:
                    Blender4 = 'Banana'

        if show == 'Blend' and MouseDrag == 'None' and event.type == pygame.MOUSEBUTTONDOWN:
            cv = 5
            clock.tick(1)
            screen.fill((255, 255, 255))
            pygame.display.flip()

            clock.tick(cv)
            screen.blit(get_image('BlendingFrame1.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
            pygame.display.flip()

            clock.tick(cv)
            screen.blit(get_image('BlendingFrame2.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
            pygame.display.flip()

            clock.tick(cv)
            screen.blit(get_image('BlendingFrame3.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
            pygame.display.flip()

            clock.tick(cv)
            screen.blit(get_image('BlendingFrame4.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
            pygame.display.flip()

            clock.tick(cv)
            screen.blit(get_image('BlendingFrame5.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
            pygame.display.flip()

            clock.tick(cv)
            screen.blit(get_image('BlendingFrame6.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
            pygame.display.flip()

            clock.tick(cv)
            screen.blit(get_image('BlendingFrame7.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
            pygame.display.flip()

            clock.tick(cv)
            screen.blit(get_image('BlendingFrame8.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
            pygame.display.flip()

            clock.tick(cv)
            screen.blit(get_image('BlendingFrame9.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
            pygame.display.flip()

            clock.tick(cv)
            screen.blit(get_image('BlendingFrame10.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
            pygame.display.flip()

            clock.tick(cv)
            screen.blit(get_image('BlendingFrame11.png'), ((SWidth - (v * img.get_width()))/2, (SHeight - (v * img.get_height()))/3))
            pygame.display.flip()

            show = 'Smuuuuuuthie!!!'

        if Restart and event.type == pygame.MOUSEBUTTONDOWN:

            show = 'Blender'

            Blender1 = 'None'
            Blender2 = 'None'
            Blender3 = 'None'
            Blender4 = 'None'

            while len(Smuuuuuuthie) > 0:
                Smuuuuuuthie.pop()

            Strawberry = True
            Blueberry = True
            Pineapple = True
            Banana = True

            StrawberryDrag_x = 0
            StrawberryDrag_y = 0
            StrawberryDragPoint_x = 0
            StrawberryDragPoint_y = 0
            BlueberryDrag_x = 0
            BlueberryDrag_y = 0
            BlueberryDragPoint_x = 0
            BlueberryDragPoint_y = 0
            PineappleDrag_x = 0
            PineappleDrag_y = 0
            PineappleDragPoint_x = 0
            PineappleDragPoint_y = 0
            BananaDrag_x = 0
            BananaDrag_y = 0
            BananaDragPoint_x = 0
            BananaDragPoint_y = 0

            Restart = False

        if Mouse_x >= (SWidth/2) - (v * img.get_width())/1.4 and Mouse_y >= (SHeight/3) - (v * img.get_height())/3 and Mouse_x <= ((SWidth/2) - (v * img.get_width())/1.4) + (v * img.get_width())/1.75 and Mouse_y <= ((SHeight/3) - (v * img.get_height())/3) + (v * img.get_height())/4 and event.type == pygame.MOUSEBUTTONDOWN and MouseDrag == 'None':
            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('Title.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame1.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame2.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame3.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame4.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame5.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame6.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame1.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame2.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame3.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame4.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame5.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame6.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame1.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame2.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame3.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame4.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame5.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])

            clock.tick(6)
            screen.fill((255, 255, 255))
            screen.blit(get_image('TitleFrame6.png'), ((SWidth/2) - (v * img.get_width())/1.075, (SHeight - (v * img.get_height()))/3))
            pygame.display.update([(SWidth/2) - (v * img.get_width())/1.4, (SHeight/3) - (v * img.get_height())/3, (v * img.get_width())/1.75, (v * img.get_height())/4])


        if event.type == pygame.QUIT or Quit == True:
            done = True
            pygame.quit()
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            ReSizeHold = False
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)