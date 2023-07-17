import face_recognition
import pygame
import time

#Base image initializations
base_image_path="face_recognition/1.jpg"
Baseimage = pygame.image.load(base_image_path)
Baseimage = pygame.transform.scale(Baseimage, (100, 100))
subject_photo = face_recognition.load_image_file(base_image_path)
subject_face_encoding = face_recognition.face_encodings(subject_photo)[0]

#pygame window init and configurations
pygame.init()
run = True
SCREEN_WIDTH=600
SCREEN_HIGHT=400

green = (124,252,0)
red = (255, 0, 0)
black = (0, 0, 0)
i = 1
pictures_of_me = 0
false_positive = 0
false_negative = 0

main_font = pygame.font.SysFont("Ariel",30)
sec_font = pygame.font.SysFont("Ariel",17)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT))
pygame.display.set_caption('Face recognition task')



#basic function to diaply text on the screen
def creatText(text,font,color,x,y):
    img = font.render(text,True,color)
    screen.blit(img,(x,y))

#program loop
while(run and i<=100):

    #i put some delay between each image so you will be able to see it proparly - it can be removed for better preformance
    time.sleep(0.25)
    screen.fill((255, 255, 255))

    #getting curr image
    curr_image_path ="face_recognition/{fname}.jpg".format(fname = i)
    image = pygame.image.load(curr_image_path)

    #scaling the image
    image = pygame.transform.scale(image, (300, 300))
    screen.blit(image, (150, 20))

    #getting image details
    unknown_image = face_recognition.load_image_file(curr_image_path)
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

    #result
    currResults = face_recognition.compare_faces([subject_face_encoding], unknown_face_encoding)

    if currResults[0] == True:
        creatText("Match!", main_font, green, 250, 350)
        pictures_of_me = pictures_of_me + 1
        if (i != 1 and i != 6 and i != 8):
            false_positive = false_positive + 1

    else:
        creatText("Unmatch!", main_font, red, 250, 350)
        if (i == 1 or i == 6 or i == 8):
            false_negative = false_negative + 1

    curr_precentage = "Matches/total scanned images: {d:.2f}%".format(d=((pictures_of_me/i) *100))
    curr_false_positive = "false positive: {r} , {d:.2f}% (of all images)".format(r=false_positive,d=(false_positive / i) * 100)
    curr_false_negative = "false negative: {r} , {d:.2f}% (of all images)".format(r=false_negative, d=(false_negative / i) * 100)

    creatText(curr_precentage, sec_font, black, 10, 330)
    creatText(curr_false_positive, sec_font, black, 10, 350)
    creatText(curr_false_negative, sec_font, black, 10, 370)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # displaying base image for reference
    creatText("Base", main_font, black, 50, 30)
    screen.blit(Baseimage, (25, 50))

    #screen refreshing
    pygame.display.flip()
    i = i + 1




pygame.QUIT


#console prints of the results
print("Total matches = {d} (should be 3)".format(d=pictures_of_me))
print("Total false positive ={d}".format(d=false_positive))
print("Total false negative ={d}".format(d=false_negative))





