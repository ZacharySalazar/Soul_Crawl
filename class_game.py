import pygame
import time
import random
import sys
import os
import webbrowser
from pynput.keyboard import Key, Controller
import pygame.mixer
from pygame.mixer import Sound
from pygame.mixer import music
from fractions import Fraction
pygame.init()
win = pygame.display.set_mode((1200,800))
surfaceCreation = pygame.font.SysFont('Comic Sans MS',50)
pygame.display.set_caption("classGame")


#menu images
noSelectMenu = pygame.image.load('noSelectMenu.png')
noSelectMenu = pygame.transform.scale(noSelectMenu,(1200,800))
playSelectMenu = pygame.image.load('playSelectMenu.png')
playSelectMenu = pygame.transform.scale(playSelectMenu,(1200,800))
aboutSelectMenu = pygame.image.load('aboutSelectMenu.png')
aboutSelectMenu = pygame.transform.scale(aboutSelectMenu,(1200,800))

#Info Panels
valkenSoulAttained = pygame.image.load('valkenSoulAttained.png')
valkenSoulAttained = pygame.transform.scale(valkenSoulAttained,(1200,800))

#Ability Pages
valkenAbilityPage = pygame.image.load('valkenAbilityPage.png')
valkenAbilityPage = pygame.transform.scale(valkenAbilityPage,(1200,800))
valkenAbilityPageFight = pygame.image.load('valkenAbilityPageFight.png')
valkenAbilityPageFight = pygame.transform.scale(valkenAbilityPageFight,(1200,800))

#bossMap images
bMNoSelectT1 = pygame.image.load('bMNoSelectT1.png')
bMNoSelectT1 = pygame.transform.scale(bMNoSelectT1,(1200,800))
bMNoSelectT2 = pygame.image.load('bMNoSelectT2.png')
bMNoSelectT2 = pygame.transform.scale(bMNoSelectT2,(1200,800))
bMSelectValkenT1 = pygame.image.load('bMSelectValkenT1.png')
bMSelectValkenT1 = pygame.transform.scale(bMSelectValkenT1,(1200,800))
bMSelectMarvT2 = pygame.image.load('bMSelectMarvT2.png')
bMSelectMarvT2 = pygame.transform.scale(bMSelectMarvT2,(1200,800))
marvAbilityPage = pygame.image.load('marvAbilityPage.png')
marvAbilityPage = pygame.transform.scale(marvAbilityPage,(1200,800))
marvAbilityPageFight = pygame.image.load('marvAbilityPageFight.png')
marvAbilityPageFight = pygame.transform.scale(marvAbilityPageFight,(1200,800))


#Text
rockWellSmall = pygame.font.SysFont('rockwell',15)
rockWell = pygame.font.SysFont('rockwell',20)
rockWellLarge = pygame.font.SysFont('rockwell',30)

#images
targetDummy = pygame.image.load('targetDummy.jpg')
targetDummy = pygame.transform.scale(targetDummy,(200,200))
brute = pygame.image.load('brute.jpg')
brute = pygame.transform.scale(brute,(300,800))
classChoice = pygame.image.load('classChoice.png')
classChoice = pygame.transform.scale(classChoice,(1200,800))
classChoiceBrute = pygame.image.load('classChoiceBrute.png')
classChoiceBrute = pygame.transform.scale(classChoiceBrute,(1200,800))
classChoiceMage = pygame.image.load('classChoiceMage.png')
classChoiceMage = pygame.transform.scale(classChoiceMage,(1200,800))
classChoiceAssassin = pygame.image.load('classChoiceAssassin.png')
classChoiceAssassin = pygame.transform.scale(classChoiceAssassin,(1200,800))



#SettingImages
battleTemplate = pygame.image.load('battleTemplate.jpg')
battleTemplate = pygame.transform.scale(battleTemplate,(1200,800))
battleTemplate2 = pygame.image.load('battleTemplate2.jpg')
battleTemplate2 = pygame.transform.scale(battleTemplate2,(1200,800))
blackScreen = pygame.image.load('blackScreen.jpg')
blackScreen = pygame.transform.scale(blackScreen,(1200,800)) 

#ValkenImages
valkenOne = pygame.image.load('valkenOne.png')
valkenOne = pygame.transform.scale(valkenOne,(250,250))
valkenOne1 = pygame.image.load('valkenOne1.png')
valkenOne1 = pygame.transform.scale(valkenOne1,(250,250))
valkenTwo = pygame.image.load('valkenTwo.png')
valkenTwo = pygame.transform.scale(valkenTwo,(200,200))
valkenTwoFace = pygame.image.load('valkenTwoFace.png')
valkenTwoFace = pygame.transform.scale(valkenTwoFace,(200,200))
valkenTakingDamage = pygame.image.load('valkenTakingDamage.png')
valkenTakingDamage = pygame.transform.scale(valkenTakingDamage,(250,250))
valkenTakingDamage2 = pygame.image.load('valkenTakingDamage2.png')
valkenTakingDamage2 = pygame.transform.scale(valkenTakingDamage2,(200,200))
valkenTakingDamage2Face = pygame.image.load('valkenTakingDamage2Face.png')
valkenTakingDamage2Face = pygame.transform.scale(valkenTakingDamage2Face,(200,200))

valkenFade1 = pygame.image.load('valkenFade1.png')
valkenFade1 = pygame.transform.scale(valkenFade1,(250,250))
valkenFade2 = pygame.image.load('valkenFade2.png')
valkenFade2 = pygame.transform.scale(valkenFade2,(250,250))
valkenHead = pygame.image.load('valkenHead.png')
valkenHead = pygame.transform.scale(valkenHead,(200,200))
valkenFadeHead = pygame.image.load('valkenFadeHead.png')
valkenFadeHead = pygame.transform.scale(valkenFadeHead,(200,200))


immuneShield = pygame.image.load('immuneShield.png')
immuneShield = pygame.transform.scale(immuneShield,(310,340))
valkenSpeak1 = pygame.image.load('valkenSpeak1.png')
valkenSpeak1 = pygame.transform.scale(valkenSpeak1,(250,250))
valkenSpeak2 = pygame.image.load('valkenSpeak2.png')
valkenSpeak2 = pygame.transform.scale(valkenSpeak2,(250,250))

valkenRSpeak1 = pygame.image.load('valkenRSpeak1.png')
valkenRSpeak1 = pygame.transform.scale(valkenRSpeak1,(250,250))
valkenRSpeak2 = pygame.image.load('valkenRSpeak2.png')
valkenRSpeak2 = pygame.transform.scale(valkenRSpeak2,(250,250))


valkenR1 = pygame.image.load('valkenR1.png')
valkenR1 = pygame.transform.scale(valkenR1,(500,180))
valkenR1Vuln = pygame.image.load('valkenR1Vuln.png')
valkenR1Vuln = pygame.transform.scale(valkenR1Vuln,(500,180))

valkenR2 = pygame.image.load('valkenR2.png')
valkenR2 = pygame.transform.scale(valkenR2,(600,250))
valkenR2Vuln = pygame.image.load('valkenR2Vuln.png')
valkenR2Vuln = pygame.transform.scale(valkenR2Vuln,(600,250))

valkenR3 = pygame.image.load('valkenR3.png')
valkenR3 = pygame.transform.scale(valkenR3,(220,220))
valkenR3Vuln = pygame.image.load('valkenR3Vuln.png')
valkenR3Vuln = pygame.transform.scale(valkenR3Vuln,(180,180))

valkenR4 = pygame.image.load('valkenR4.png')
valkenR4 = pygame.transform.scale(valkenR4,(200,200))
valkenR4Vuln = pygame.image.load('valkenR4Vuln.png')
valkenR4Vuln = pygame.transform.scale(valkenR4Vuln,(180,180))

valkenR5 = pygame.image.load('valkenR5.png')
valkenR5 = pygame.transform.scale(valkenR5,(80,80))
valkenR5Vuln = pygame.image.load('valkenR5Vuln.png')
valkenR5Vuln = pygame.transform.scale(valkenR5Vuln,(80,60))

valkenR6 = pygame.image.load('valkenR6.png')
valkenR6 = pygame.transform.scale(valkenR6,(80,70))
valkenR6Vuln = pygame.image.load('valkenR6Vuln.png')
valkenR6Vuln = pygame.transform.scale(valkenR6Vuln,(80,60))

valkenR7 = pygame.image.load('valkenR7.png')
valkenR7 = pygame.transform.scale(valkenR7,(140,70))
valkenR7Vuln = pygame.image.load('valkenR7Vuln.png')
valkenR7Vuln = pygame.transform.scale(valkenR7Vuln,(140,70))

valkenLaugh1 = pygame.image.load('valkenLaugh1.png')
valkenLaugh1 = pygame.transform.scale(valkenLaugh1,(300,300))
valkenLaugh2 = pygame.image.load('valkenLaugh2.png')
valkenLaugh2 = pygame.transform.scale(valkenLaugh2,(300,300))
valkenLaugh3 = pygame.image.load('valkenLaugh3.png')
valkenLaugh3 = pygame.transform.scale(valkenLaugh3,(300,300))

valkenPuke0 = pygame.image.load('valkenPuke0.png')
valkenPuke0 = pygame.transform.scale(valkenPuke0,(250,250))
valkenPuke1 = pygame.image.load('valkenPuke1.png')
valkenPuke1 = pygame.transform.scale(valkenPuke1,(250,250))
valkenPuke2 = pygame.image.load('valkenPuke2.png')
valkenPuke2 = pygame.transform.scale(valkenPuke2,(250,250))
valkenPuke3 = pygame.image.load('valkenPuke3.png')
valkenPuke3 = pygame.transform.scale(valkenPuke3,(250,250))
valkenPuke4 = pygame.image.load('valkenPuke4.png')
valkenPuke4 = pygame.transform.scale(valkenPuke4,(250,250))
valkenVomitDamage = pygame.image.load('valkenVomitDamage.png')
valkenVomitDamage = pygame.transform.scale(valkenVomitDamage,(250,250))

valkenVoiceImage = pygame.image.load('valkenVoiceImage.png')
valkenVoiceImage = pygame.transform.scale(valkenVoiceImage,(200,200))

valkenImmune = pygame.image.load('valkenImmune.png')
valkenImmune = pygame.transform.scale(valkenImmune,(200,300))

        #ValkenSpellImages
vortexOne1 = pygame.image.load('vortexImages/vortexOne1.png')
vortexOne1 = pygame.transform.scale(vortexOne1,(200,200))
vortexOne2 = pygame.image.load('vortexImages/vortexOne2.png')
vortexOne2 = pygame.transform.scale(vortexOne2,(200,200))
vortexOne3 = pygame.image.load('vortexImages/vortexOne3.png')
vortexOne3 = pygame.transform.scale(vortexOne3,(200,200))
vortexOne4 = pygame.image.load('vortexImages/vortexOne4.png')
vortexOne4 = pygame.transform.scale(vortexOne4,(200,200))
vortexTwo1 = pygame.image.load('vortexImages/vortexTwo1.png')
vortexTwo1 = pygame.transform.scale(vortexTwo1,(200,200))
vortexTwo2 = pygame.image.load('vortexImages/vortexTwo2.png')
vortexTwo2 = pygame.transform.scale(vortexTwo2,(200,200))
vortexTwo3 = pygame.image.load('vortexImages/vortexTwo3.png')
vortexTwo3 = pygame.transform.scale(vortexTwo3,(200,200))
vortexTwo4 = pygame.image.load('vortexImages/vortexTwo4.png')
vortexTwo4 = pygame.transform.scale(vortexTwo4,(200,200))
vortexThree1 = pygame.image.load('vortexImages/vortexThree1.png')
vortexThree1 = pygame.transform.scale(vortexThree1,(200,200))
vortexThree2 = pygame.image.load('vortexImages/vortexThree2.png')
vortexThree2 = pygame.transform.scale(vortexThree2,(200,200))
vortexThree3 = pygame.image.load('vortexImages/vortexThree3.png')
vortexThree3 = pygame.transform.scale(vortexThree3,(200,200))
vortexThree4 = pygame.image.load('vortexImages/vortexThree4.png')
vortexThree4 = pygame.transform.scale(vortexThree4,(200,200))

#p1 Valken Images
starP1 = pygame.image.load('starImages/starP1.png')
starP1 = pygame.transform.scale(starP1,(200,200))
starP2 = pygame.image.load('starImages/starP2.png')
starP2 = pygame.transform.scale(starP2,(200,200))
starP3 = pygame.image.load('starImages/starP3.png')
starP3 = pygame.transform.scale(starP3,(200,200))
starP4 = pygame.image.load('starImages/starP4.png')
starP4 = pygame.transform.scale(starP4,(200,200))
starP5 = pygame.image.load('starImages/starP5.png')
starP5 = pygame.transform.scale(starP5,(200,200))

starY1 = pygame.image.load('starImages/starY1.png')
starY1 = pygame.transform.scale(starY1,(200,200))
starY2 = pygame.image.load('starImages/starY2.png')
starY2 = pygame.transform.scale(starY2,(200,200))
starY3 = pygame.image.load('starImages/starY3.png')
starY3 = pygame.transform.scale(starY3,(200,200))
starY4 = pygame.image.load('starImages/starY4.png')
starY4 = pygame.transform.scale(starY4,(200,200))
starY5 = pygame.image.load('starImages/starY5.png')
starY5 = pygame.transform.scale(starY5,(200,200))

valkenPotrait = pygame.image.load('valkenPotrait.png')
valkenPotrait = pygame.transform.scale(valkenPotrait,(120,120))
valkenPotrait2 = pygame.image.load('valkenPotrait2.png')
valkenPotrait2 = pygame.transform.scale(valkenPotrait2,(120,120))
valkenPotraitP = pygame.image.load('valkenPotraitP.png')
valkenPotraitP = pygame.transform.scale(valkenPotraitP,(120,120))
valkenPotraitP2 = pygame.image.load('valkenPotraitP2.png')
valkenPotraitP2 = pygame.transform.scale(valkenPotraitP2,(120,120))
punishPotrait = pygame.image.load('punishPotrait.png')
punishPotrait = pygame.transform.scale(punishPotrait,(120,120))

simon1 = pygame.image.load('simon1.png')
simon1 = pygame.transform.scale(simon1,(300,300))
simon2 = pygame.image.load('simon2.png')
simon2 = pygame.transform.scale(simon2,(300,300))
simon3 = pygame.image.load('simon3.png')
simon3 = pygame.transform.scale(simon3,(400,300))
simonHand = pygame.image.load('simonHand.png')
simonHand = pygame.transform.scale(simonHand,(200,200))
handDead1 = pygame.image.load('handDead1.png')
handDead1 = pygame.transform.scale(handDead1,(200,200))
handDead2 = pygame.image.load('handDead2.png')
handDead2 = pygame.transform.scale(handDead2,(200,200))
handDead3 = pygame.image.load('handDead3.png')
handDead3 = pygame.transform.scale(handDead3,(200,200))
handDead4 = pygame.image.load('handDead4.png')
handDead4 = pygame.transform.scale(handDead4,(200,200))
handDead5 = pygame.image.load('handDead5.png')
handDead5 = pygame.transform.scale(handDead5,(200,200))
faceDead1 = pygame.image.load('faceDead1.png')
faceDead1 = pygame.transform.scale(faceDead1,(400,300))
faceDead2 = pygame.image.load('faceDead2.png')
faceDead2 = pygame.transform.scale(faceDead2,(400,300))
faceDead3 = pygame.image.load('faceDead3.png')
faceDead3 = pygame.transform.scale(faceDead3,(400,300))



simonHandTakeDamage = pygame.image.load('simonHandTakeDamage.png')
simonHandTakeDamage = pygame.transform.scale(simonHandTakeDamage,(200,200))

skW1 = pygame.image.load('cutSkeles/skW1.png')
skW1 = pygame.transform.scale(skW1,(75,75))
skW2 = pygame.image.load('cutSkeles/skW2.png')
skW2 = pygame.transform.scale(skW2,(75,75))
skW3 = pygame.image.load('cutSkeles/skW3.png')
skW3 = pygame.transform.scale(skW3,(75,75))
skW4 = pygame.image.load('cutSkeles/skW4.png')
skW4 = pygame.transform.scale(skW4,(75,75))
skW5 = pygame.image.load('cutSkeles/skW5.png')
skW5 = pygame.transform.scale(skW5,(75,75))
skW6 = pygame.image.load('cutSkeles/skW6.png')
skW6 = pygame.transform.scale(skW6,(75,75))
skW7 = pygame.image.load('cutSkeles/skW7.png')
skW7 = pygame.transform.scale(skW7,(75,75))
skW8 = pygame.image.load('cutSkeles/skW8.png')
skW8 = pygame.transform.scale(skW8,(75,75))
skW9 = pygame.image.load('cutSkeles/skW9.png')
skW9 = pygame.transform.scale(skW9,(75,75))
skW10 = pygame.image.load('cutSkeles/skW10.png')
skW10 = pygame.transform.scale(skW10,(75,75))
skW11 = pygame.image.load('cutSkeles/skW11.png')
skW11 = pygame.transform.scale(skW11,(75,75))
skW12 = pygame.image.load('cutSkeles/skW12.png')
skW12 = pygame.transform.scale(skW12,(75,75))
skW13 = pygame.image.load('cutSkeles/skW13.png')
skW13 = pygame.transform.scale(skW13,(75,75))

skA1 = pygame.image.load('cutSkeles/skA1.png')
skA1 = pygame.transform.scale(skA1,(75,75))
skA2 = pygame.image.load('cutSkeles/skA2.png')
skA2 = pygame.transform.scale(skA2,(75,75))
skA3 = pygame.image.load('cutSkeles/skA3.png')
skA3 = pygame.transform.scale(skA3,(75,75))
skA4 = pygame.image.load('cutSkeles/skA4.png')
skA4 = pygame.transform.scale(skA4,(75,75))
skA5 = pygame.image.load('cutSkeles/skA5.png')
skA5 = pygame.transform.scale(skA5,(75,75))
skA6 = pygame.image.load('cutSkeles/skA6.png')
skA6 = pygame.transform.scale(skA6,(75,75))
skA7 = pygame.image.load('cutSkeles/skA7.png')
skA7 = pygame.transform.scale(skA7,(75,75))
skA8 = pygame.image.load('cutSkeles/skA8.png')
skA8 = pygame.transform.scale(skA8,(75,75))
skA9 = pygame.image.load('cutSkeles/skA9.png')
skA9 = pygame.transform.scale(skA9,(75,75))
skA10 = pygame.image.load('cutSkeles/skA10.png')
skA10 = pygame.transform.scale(skA10,(75,75))
skA11 = pygame.image.load('cutSkeles/skA11.png')
skA11 = pygame.transform.scale(skA11,(75,75))
skA12 = pygame.image.load('cutSkeles/skA12.png')
skA12 = pygame.transform.scale(skA12,(75,75))
skA13 = pygame.image.load('cutSkeles/skA13.png')
skA13 = pygame.transform.scale(skA13,(75,75))
skA14 = pygame.image.load('cutSkeles/skA14.png')
skA14 = pygame.transform.scale(skA14,(75,75))
skA15 = pygame.image.load('cutSkeles/skA15.png')
skA15 = pygame.transform.scale(skA15,(75,75))
skA16 = pygame.image.load('cutSkeles/skA16.png')
skA16 = pygame.transform.scale(skA16,(75,75))
skA17 = pygame.image.load('cutSkeles/skA17.png')
skA17 = pygame.transform.scale(skA17,(75,75))
skA18 = pygame.image.load('cutSkeles/skA18.png')
skA18 = pygame.transform.scale(skA18,(75,75))

skD1 = pygame.image.load('cutSkeles/skD1.png')
skD1 = pygame.transform.scale(skD1,(75,75))
skD2 = pygame.image.load('cutSkeles/skD2.png')
skD2 = pygame.transform.scale(skD2,(75,75))
skD3 = pygame.image.load('cutSkeles/skD3.png')
skD3 = pygame.transform.scale(skD3,(75,75))
skD4 = pygame.image.load('cutSkeles/skD4.png')
skD4 = pygame.transform.scale(skD4,(75,75))
skD5 = pygame.image.load('cutSkeles/skD5.png')
skD5 = pygame.transform.scale(skD5,(75,75))
skD6 = pygame.image.load('cutSkeles/skD6.png')
skD6 = pygame.transform.scale(skD6,(75,75))
skD7 = pygame.image.load('cutSkeles/skD7.png')
skD7 = pygame.transform.scale(skD7,(75,75))
skD8 = pygame.image.load('cutSkeles/skD8.png')
skD8 = pygame.transform.scale(skD8,(75,75))
skD9 = pygame.image.load('cutSkeles/skD9.png')
skD9 = pygame.transform.scale(skD9,(75,75))
skD10 = pygame.image.load('cutSkeles/skD10.png')
skD10 = pygame.transform.scale(skD10,(75,75))
skD11 = pygame.image.load('cutSkeles/skD11.png')
skD11 = pygame.transform.scale(skD11,(75,75))
skD12 = pygame.image.load('cutSkeles/skD12.png')
skD12 = pygame.transform.scale(skD12,(75,75))
skD13 = pygame.image.load('cutSkeles/skD13.png')
skD13 = pygame.transform.scale(skD13,(75,75))
skD14 = pygame.image.load('cutSkeles/skD14.png')
skD14 = pygame.transform.scale(skD14,(75,75))
skD15 = pygame.image.load('cutSkeles/skD15.png')
skD15 = pygame.transform.scale(skD15,(75,75))

skZ1 = pygame.image.load('cutSkeles/skZ1.png')
skZ1 = pygame.transform.scale(skZ1,(75,75))
skZ2 = pygame.image.load('cutSkeles/skZ2.png')
skZ2 = pygame.transform.scale(skZ2,(75,75))
skZ3 = pygame.image.load('cutSkeles/skZ3.png')
skZ3 = pygame.transform.scale(skZ3,(75,75))
skZ4 = pygame.image.load('cutSkeles/skZ4.png')
skZ4 = pygame.transform.scale(skZ4,(75,75))
skZ5 = pygame.image.load('cutSkeles/skZ5.png')
skZ5 = pygame.transform.scale(skZ5,(75,75))
skZ6 = pygame.image.load('cutSkeles/skZ6.png')
skZ6 = pygame.transform.scale(skZ6,(75,75))
skZ7 = pygame.image.load('cutSkeles/skZ7.png')
skZ7 = pygame.transform.scale(skZ7,(75,75))
skZ8 = pygame.image.load('cutSkeles/skZ8.png')
skZ8 = pygame.transform.scale(skZ8,(75,75))

tWalk1 = pygame.image.load('tWalk1.png')
tWalk1 = pygame.transform.scale(tWalk1,(100,100))
tWalk2 = pygame.image.load('tWalk2.png')
tWalk2 = pygame.transform.scale(tWalk2,(100,100))
tWalk3 = pygame.image.load('tWalk3.png')
tWalk3 = pygame.transform.scale(tWalk3,(100,100))
tWalk4 = pygame.image.load('tWalk4.png')
tWalk4 = pygame.transform.scale(tWalk4,(100,100))


skeletonImage = pygame.image.load('skeletonImage.png')
skeletonImage = pygame.transform.scale(skeletonImage,(100,100))


staticPortal = pygame.image.load('staticPortal.png')
staticPortal = pygame.transform.scale(staticPortal,(200,200))
staticPortal2 = pygame.image.load('staticPortal2.png')
staticPortal2 = pygame.transform.scale(staticPortal2,(200,200))
exitPortalOne = pygame.image.load('exitPortalOne.png')
exitPortalOne = pygame.transform.scale(exitPortalOne,(350,235))
exitPortalTwo = pygame.image.load('exitPortalTwo.png')
exitPortalTwo = pygame.transform.scale(exitPortalTwo,(350,235))
exitPortalThree = pygame.image.load('exitPortalThree.png')
exitPortalThree = pygame.transform.scale(exitPortalThree,(350,235))
takePortalText = pygame.image.load('takePortalText.png')
takePortalText = pygame.transform.scale(takePortalText,(140,70))

portalDamageImage = pygame.image.load('portalDamageImage.png')
portalDamageImage = pygame.transform.scale(portalDamageImage,(200,200))
portalOff = pygame.image.load('portalOff.png')
portalOff = pygame.transform.scale(portalOff,(200,200))

fireSeq = pygame.image.load('fireSeq.png')
fireSeq2 = pygame.image.load('fireSeq2.png')
fireSeq3 = pygame.image.load('fireSeq3.png')
fireSeq4 = pygame.image.load('fireSeq4.png')

f1 = pygame.image.load('f1.png')
f1 = pygame.transform.scale(f1,(350,500))
f2 = pygame.image.load('f2.png')
f2 = pygame.transform.scale(f2,(350,500))
f3 = pygame.image.load('f3.png')
f3 = pygame.transform.scale(f3,(350,500))
f4 = pygame.image.load('f4.png')
f4 = pygame.transform.scale(f4,(350,500))
f5 = pygame.image.load('f5.png')
f5 = pygame.transform.scale(f5,(350,500))


blueSkull = pygame.image.load('blueSkull.jpg')
blueSkull = pygame.transform.scale(blueSkull,(100,100))
greenSkull = pygame.image.load('greenSkull.jpg')
greenSkull = pygame.transform.scale(greenSkull,(100,100))
yellowSkull = pygame.image.load('yellowSkull.png')
yellowSkull = pygame.transform.scale(yellowSkull,(100,100))
skullDamageTakenImage = pygame.image.load('skullDamageTakenImage.jpg')
skullDamageTakenImage = pygame.transform.scale(skullDamageTakenImage,(100,100))

lazerFlyImage = pygame.image.load('lazerFlyImage.png')
lazerFlyImage = pygame.transform.scale(lazerFlyImage,(75,75))
lazerFlyDamageImage = pygame.image.load('lazerFlyDamageImage.png')
lazerFlyDamageImage = pygame.transform.scale(lazerFlyDamageImage,(75,75))
lazerFlyImage2 = pygame.image.load('lazerFlyImage2.png')
lazerFlyImage2 = pygame.transform.scale(lazerFlyImage2,(75,75))
lazerFly2DamageImage = pygame.image.load('lazerFly2DamageImage.png')
lazerFly2DamageImage = pygame.transform.scale(lazerFly2DamageImage,(75,75))
lazerFlyImage3 = pygame.image.load('lazerFlyImage3.png')
lazerFlyImage3 = pygame.transform.scale(lazerFlyImage3,(125,125))
lazerFly3DamageImage = pygame.image.load('lazerFly3DamageImage.png')
lazerFly3DamageImage = pygame.transform.scale(lazerFly3DamageImage,(75,75))

blueOrb1 = pygame.image.load('orbImages/blueOrb1.png')
blueOrb1 = pygame.transform.scale(blueOrb1,(20,20))
blueOrb2 = pygame.image.load('orbImages/blueOrb2.png')
blueOrb2 = pygame.transform.scale(blueOrb2,(25,25))
blueOrb3 = pygame.image.load('orbImages/blueOrb3.png')
blueOrb3 = pygame.transform.scale(blueOrb3,(30,30))
blueOrb4 = pygame.image.load('orbImages/blueOrb4.png')
blueOrb4 = pygame.transform.scale(blueOrb4,(35,35))
blueOrb5 = pygame.image.load('orbImages/blueOrb5.png')
blueOrb5 = pygame.transform.scale(blueOrb5,(35,35))
blueOrb6 = pygame.image.load('orbImages/blueOrb6.png')
blueOrb6 = pygame.transform.scale(blueOrb6,(35,35))
blueOrb7 = pygame.image.load('orbImages/blueOrb7.png')
blueOrb7 = pygame.transform.scale(blueOrb7,(35,35))

redOrb1 = pygame.image.load('orbImages/redOrb1.png')
redOrb1 = pygame.transform.scale(redOrb1,(35,35))
redOrb2 = pygame.image.load('orbImages/redOrb2.png')
redOrb2 = pygame.transform.scale(redOrb2,(25,25))
redOrb3 = pygame.image.load('orbImages/redOrb3.png')
redOrb3 = pygame.transform.scale(redOrb3,(30,30))
redOrb4 = pygame.image.load('orbImages/redOrb4.png')
redOrb4 = pygame.transform.scale(redOrb4,(35,35))
redOrb5 = pygame.image.load('orbImages/redOrb5.png')
redOrb5 = pygame.transform.scale(redOrb5,(35,35))
redOrb6 = pygame.image.load('orbImages/redOrb6.png')
redOrb6 = pygame.transform.scale(redOrb6,(35,35))
redOrb7 = pygame.image.load('orbImages/redOrb7.png')
redOrb7 = pygame.transform.scale(redOrb7,(35,35))

gargOrbF1 = pygame.image.load('orbImages/gargOrbF1.png')
gargOrbF1 = pygame.transform.scale(gargOrbF1,(50,50))
gargOrbF2 = pygame.image.load('orbImages/gargOrbF2.png')
gargOrbF2 = pygame.transform.scale(gargOrbF2,(50,50))
gargOrbF3 = pygame.image.load('orbImages/gargOrbF3.png')
gargOrbF3 = pygame.transform.scale(gargOrbF3,(50,50))
gargOrbF4 = pygame.image.load('orbImages/gargOrbF4.png')
gargOrbF4 = pygame.transform.scale(gargOrbF4,(50,50))
gargOrbF5 = pygame.image.load('orbImages/gargOrbF5.png')
gargOrbF5 = pygame.transform.scale(gargOrbF5,(50,50))
gargOrbF6 = pygame.image.load('orbImages/gargOrbF6.png')
gargOrbF6 = pygame.transform.scale(gargOrbF6,(50,50))

shrinkE1 = pygame.image.load('orbImages/shrinkE1.png')
shrinkE1 = pygame.transform.scale(shrinkE1,(200,200))
shrinkE2 = pygame.image.load('orbImages/shrinkE2.png')
shrinkE2 = pygame.transform.scale(shrinkE2,(200,200))
shrinkE3 = pygame.image.load('orbImages/shrinkE3.png')
shrinkE3 = pygame.transform.scale(shrinkE3,(200,200))
shrinkE4 = pygame.image.load('orbImages/shrinkE4.png')
shrinkE4 = pygame.transform.scale(shrinkE4,(200,200))
shrinkE5 = pygame.image.load('orbImages/shrinkE5.png')
shrinkE5 = pygame.transform.scale(shrinkE5,(200,200))
shrinkE6 = pygame.image.load('orbImages/shrinkE6.png')
shrinkE6 = pygame.transform.scale(shrinkE6,(200,200))
shrinkE7 = pygame.image.load('orbImages/shrinkE7.png')
shrinkE7 = pygame.transform.scale(shrinkE7,(200,200))

flyE1 = pygame.image.load('orbImages/flyE1.png')
flyE1 = pygame.transform.scale(flyE1,(75,75))
flyE2 = pygame.image.load('orbImages/flyE2.png')
flyE2 = pygame.transform.scale(flyE2,(75,75))
flyE3 = pygame.image.load('orbImages/flyE3.png')
flyE3 = pygame.transform.scale(flyE3,(75,75))
flyE4 = pygame.image.load('orbImages/flyE4.png')
flyE4 = pygame.transform.scale(flyE4,(75,75))
flyE5 = pygame.image.load('orbImages/flyE5.png')
flyE5 = pygame.transform.scale(flyE5,(75,75))
flyE6 = pygame.image.load('orbImages/flyE6.png')
flyE6 = pygame.transform.scale(flyE6,(75,75))
flyE7 = pygame.image.load('orbImages/flyE7.png')
flyE7 = pygame.transform.scale(flyE7,(75,75))


airlock1Image = pygame.image.load('airlock1Image.png')
airlock1Image = pygame.transform.scale(airlock1Image,(275,275))
airlock1ImageBroken = pygame.image.load('airlock1ImageBroken.png')
airlock1ImageBroken = pygame.transform.scale(airlock1ImageBroken,(275,275))
airlock2Image = pygame.image.load('airlock2Image.png')
airlock2Image = pygame.transform.scale(airlock2Image,(275,275))
airlock2ImageBroken = pygame.image.load('airlock2ImageBroken.png')
airlock2ImageBroken = pygame.transform.scale(airlock2ImageBroken,(275,275))

airlockLockC1 = pygame.image.load('airlockLockC1.png')
airlockLockC1 = pygame.transform.scale(airlockLockC1,(90,90))
airlockLockC2 = pygame.image.load('airlockLockC2.png')
airlockLockC2 = pygame.transform.scale(airlockLockC2,(90,90))
airlockLockC3 = pygame.image.load('airlockLockC3.png')
airlockLockC3 = pygame.transform.scale(airlockLockC3,(90,90))
airlockLockC4 = pygame.image.load('airlockLockC4.png')
airlockLockC4 = pygame.transform.scale(airlockLockC4,(90,90))
airlockLockTakeDamage = pygame.image.load('airlockLockTakeDamage.png')
airlockLockTakeDamage = pygame.transform.scale(airlockLockTakeDamage,(90,90))

reflectorImage = pygame.image.load('reflectorImage.png')
reflectorImage = pygame.transform.scale(reflectorImage,(250,250))
reflectorTakeDamage = pygame.image.load('reflectorTakeDamage.png')
reflectorTakeDamage = pygame.transform.scale(reflectorTakeDamage,(250,250))

reflectModImage = pygame.image.load('reflectModImage.png')
reflectModImage = pygame.transform.scale(reflectModImage,(100,100))



eC1 = pygame.image.load('eC1.png')
eC1 = pygame.transform.scale(eC1,(250,250))
eC2 = pygame.image.load('eC2.png')
eC2 = pygame.transform.scale(eC2,(250,250)) 
eC3 = pygame.image.load('eC3.png')
eC3 = pygame.transform.scale(eC3,(250,250))
eC4 = pygame.image.load('eC4.png')
eC4 = pygame.transform.scale(eC4,(250,250))


#shrinker starting and rotation images
startingTurrent = pygame.image.load('startingTurrent.png')
startingTurrent = pygame.transform.scale(startingTurrent,(200,200))
r1Image = pygame.image.load('r1Image.png')
r1Image = pygame.transform.scale(r1Image,(200,200))
r2Image = pygame.image.load('r2Image.png')
r2Image = pygame.transform.scale(r2Image,(200,200))
r3Image = pygame.image.load('r3Image.png')
r3Image = pygame.transform.scale(r3Image,(200,200))
r4Image = pygame.image.load('r4Image.png')
r4Image = pygame.transform.scale(r4Image,(200,200))
r5Image = pygame.image.load('r5Image.png')
r5Image = pygame.transform.scale(r5Image,(200,200))
r6Image = pygame.image.load('r6Image.png')
r6Image = pygame.transform.scale(r6Image,(200,200))
r7Image = pygame.image.load('r7Image.png')
r7Image = pygame.transform.scale(r7Image,(200,200))
r8Image = pygame.image.load('r8Image.png')
r8Image = pygame.transform.scale(r8Image,(200,200))

r1Dimage = pygame.image.load('r1Dimage.png')
r1Dimage = pygame.transform.scale(r1Dimage,(200,200))
r2Dimage = pygame.image.load('r2Dimage.png')
r2Dimage = pygame.transform.scale(r2Dimage,(200,200))
r3Dimage = pygame.image.load('r3Dimage.png')
r3Dimage = pygame.transform.scale(r3Dimage,(200,200))
r4Dimage = pygame.image.load('r4Dimage.png')
r4Dimage = pygame.transform.scale(r4Dimage,(200,200))
r5Dimage = pygame.image.load('r5Dimage.png')
r5Dimage = pygame.transform.scale(r5Dimage,(200,200))
r6Dimage = pygame.image.load('r6Dimage.png')
r6Dimage = pygame.transform.scale(r6Dimage,(200,200))
r7Dimage = pygame.image.load('r7Dimage.png')
r7Dimage = pygame.transform.scale(r7Dimage,(200,200))
r8Dimage = pygame.image.load('r8Dimage.png')
r8Dimage = pygame.transform.scale(r8Dimage,(200,200))

#moon
uSoundWave = pygame.image.load('uSoundWave.png')
dSoundWave = pygame.image.load('dSoundWave.png')
lSoundWave = pygame.image.load('lSoundWave.png')
rSoundWave = pygame.image.load('rSoundWave.png')
ulSoundWave = pygame.image.load('ulSoundWave.png')
ulSoundWave = pygame.transform.scale(ulSoundWave,(300,300))
urSoundWave = pygame.image.load('urSoundWave.png')
urSoundWave = pygame.transform.scale(urSoundWave,(300,300))
dlSoundWave = pygame.image.load('dlSoundWave.png')
dlSoundWave = pygame.transform.scale(dlSoundWave,(300,300))
drSoundWave = pygame.image.load('drSoundWave.png')
drSoundWave = pygame.transform.scale(drSoundWave,(300,300))

moonImage = pygame.image.load('moonImage.png')
moonImage = pygame.transform.scale(moonImage,(400,400))
moonTakingDamage = pygame.image.load('moonTakingDamage.png')
moonTakingDamage = pygame.transform.scale(moonTakingDamage,(400,400))
moonStoppedImage = pygame.image.load('moonStoppedImage.png')
moonStoppedIMage = pygame.transform.scale(moonStoppedImage,(400,400))
fire1 = pygame.image.load('fire1.png')
fire1 = pygame.transform.scale(fire1,(1000,700))
fire2 = pygame.image.load('fire2.png')
fire2 = pygame.transform.scale(fire2,(1000,700))
fire3 = pygame.image.load('fire3.png')
fire3 = pygame.transform.scale(fire3,(1000,700))


#player Sounds
playerTakeDamage1 = pygame.mixer.Sound("playerTakeDamage1.wav")
playerTakeDamage2 = pygame.mixer.Sound("playerTakeDamage2.wav")
playerTakeDamage3 = pygame.mixer.Sound("playerTakeDamage3.wav")

#valken Souinds
valkenTakingDamageSound = pygame.mixer.Sound("valkenTakingDamageSound.wav")
valkenP2TakingDamageSound = pygame.mixer.Sound("valkenP2TakingDamageSound.wav")
pukeSound = pygame.mixer.Sound("pukeSound.wav")
immunityDamageTakenSound = pygame.mixer.Sound("immunityDamageTakenSound.wav")

flamesCracklingSE = pygame.mixer.Sound("flamesCracklingSE.wav")
fireCracklingSE = pygame.mixer.Sound("fireCracklingSE.wav")
valkenBreathingSE = pygame.mixer.Sound("valkenBreathingSE.wav")
valkenDyingSE = pygame.mixer.Sound('valkenDyingSE.wav')

soulSound = pygame.mixer.Sound('soulSound.wav')


         #valken quotes p1
imagodSound = pygame.mixer.Sound("imagodSound.wav")
innocenceSound = pygame.mixer.Sound("innocenceSound.wav")
naiveSound = pygame.mixer.Sound("naiveSound.wav")
noEscapeSound = pygame.mixer.Sound("noEscapeSound.wav")
thisIsTheEndSE = pygame.mixer.Sound("thisIsTheEndSE.wav")
whatAreYouDoingSE = pygame.mixer.Sound("whatAreYouDoingSE.wav")
whatAreYouDoingSE.set_volume(0.05)


#P1 ObjectSounds
valkenOrbSound = pygame.mixer.Sound("valkenOrbSound.wav")
valkenFlashSound = pygame.mixer.Sound("flashSound.wav")
valkenLazerSound = pygame.mixer.Sound('valkenLazerSound.wav')
valkenVanishSound = pygame.mixer.Sound("vanishSound.wav")
valkenOrbSound.set_volume(0.1)
valkenFlashSound.set_volume(0.1)
valkenLazerSound.set_volume(0.03)
valkenVanishSound.set_volume(0.1)

simonSound = pygame.mixer.Sound("simonSound.wav")
simonSound2 = pygame.mixer.Sound("simonSound2.wav")
simonDeadSound = pygame.mixer.Sound("simonDeadSound.wav")
simonSound2.set_volume(0.3)
simonDeadSound.set_volume(0.05)
gruntSound = pygame.mixer.Sound("gruntSound.wav")
gruntSound2 = pygame.mixer.Sound("gruntSound2.wav")
gruntDeadSound = pygame.mixer.Sound("gruntDeadSound.wav")

gSound1 = pygame.mixer.Sound("gSound1.wav")
gSound2 = pygame.mixer.Sound("gSound2.wav")
gSound3 = pygame.mixer.Sound("gSound3.wav")
gSound4 = pygame.mixer.Sound("gSound4.wav")
gSound1.set_volume(0.3)
gSound2.set_volume(0.3)
gSound3.set_volume(0.3)
gSound4.set_volume(0.3)


takePortalSound = pygame.mixer.Sound("takePortalSound.wav")
takePortalSound.set_volume(0.3)

       #P2 ObjectSounds
valkenP2Laugh = pygame.mixer.Sound("valkenP2Laugh.wav")
flyExSound = pygame.mixer.Sound("flyExSound.wav")
flyEx2Sound = pygame.mixer.Sound("flyEx2Sound.wav")
sparkSound = pygame.mixer.Sound("sparkSound.wav")
reflectedSound = pygame.mixer.Sound("reflectedSound.wav")
reflectorsExplodeSound = pygame.mixer.Sound("reflectorsExplodeSound.wav") 
shrinkRaySound = pygame.mixer.Sound("shrinkRaySound.wav")
shrinkExplodeSound = pygame.mixer.Sound("shrinkExplodeSound.wav")
airlockBrokeSound = pygame.mixer.Sound("airlockBrokeSound.wav")
callMoonSound = pygame.mixer.Sound("callMoonSound.wav")


skullTakeDamageSound = pygame.mixer.Sound("skullTakeDamageSound.wav")
skullTakeDamageTwoSound = pygame.mixer.Sound("skullTakeDamageTwoSound.wav")

#BruteImages
bruteIntro = pygame.image.load('bruteIntro.jpg')
bruteIntro = pygame.transform.scale(bruteIntro,(1200,800))
bruteFormOne = pygame.image.load('bruteFormOne.jpg')
bruteFormOne = pygame.transform.scale(bruteFormOne,(300,300))
bruteFormTwo = pygame.image.load('bruteFormTwo.jpg')
bruteFormTwo = pygame.transform.scale(bruteFormTwo,(300,300))
bruteFormThree = pygame.image.load('bruteFormThree.jpg')
bruteFormThree = pygame.transform.scale(bruteFormThree,(300,300))
bruteDamageTaken1 = pygame.image.load('bruteDamageTaken1.jpg')
bruteDamageTaken1 = pygame.transform.scale(bruteDamageTaken1,(300,300))
bruteDamageTaken2 = pygame.image.load('bruteDamageTaken2.jpg')
bruteDamageTaken2 = pygame.transform.scale(bruteDamageTaken2,(300,300))
bruteDamageTaken3 = pygame.image.load('bruteDamageTaken3.jpg')
bruteDamageTaken3 = pygame.transform.scale(bruteDamageTaken3,(300,300))
bruteFormOnePois = pygame.image.load('bruteFormOnePois.jpg')
bruteFormOnePois = pygame.transform.scale(bruteFormOnePois,(300,300))
bruteFormTwoPois = pygame.image.load('bruteFormTwoPois.jpg')
bruteFormTwoPois = pygame.transform.scale(bruteFormTwoPois,(300,300))
bruteFormThreePois = pygame.image.load('bruteFormThreePois.jpg')
bruteFormThreePois = pygame.transform.scale(bruteFormThreePois,(300,300))



sword1 = pygame.image.load('weaponImages/sword1.png')
sword1 = pygame.transform.scale(sword1,(150,150))
sword2 = pygame.image.load('weaponImages/sword2.png')
sword2 = pygame.transform.scale(sword2,(150,150))
sword3 = pygame.image.load('weaponImages/sword3.png')
sword3 = pygame.transform.scale(sword3,(150,150))
axe1 = pygame.image.load('weaponImages/axe1.png')
axe1 = pygame.transform.scale(axe1,(150,150))
axe2 = pygame.image.load('weaponImages/axe2.png')
axe2 = pygame.transform.scale(axe2,(150,150))
axe3 = pygame.image.load('weaponImages/axe3.png')
axe3 = pygame.transform.scale(axe3,(150,150))
mace1 = pygame.image.load('weaponImages/mace1.png')
mace1 = pygame.transform.scale(mace1,(150,150))
mace2 = pygame.image.load('weaponImages/mace2.png')
mace2 = pygame.transform.scale(mace2,(150,150))
mace3 = pygame.image.load('weaponImages/mace3.png')
mace3 = pygame.transform.scale(mace3,(150,150))
warHammer1 = pygame.image.load('weaponImages/warHammer1.png')
warHammer1 = pygame.transform.scale(warHammer1,(150,150))
warHammer2 = pygame.image.load('weaponImages/warHammer2.png')
warHammer2 = pygame.transform.scale(warHammer2,(150,150))
warHammer3 = pygame.image.load('weaponImages/warHammer3.png')
warHammer3 = pygame.transform.scale(warHammer3,(150,150))

        #brute Sounds
shout1Sound = pygame.mixer.Sound("shout1Sound.wav")
shout2Sound = pygame.mixer.Sound("shout2Sound.wav")
shout3Sound = pygame.mixer.Sound("shout3Sound.wav")
furySound = pygame.mixer.Sound("furySound.wav")

#axe1 = pygame.image.load('axe1.jpg')
#axe1 = pygame.transform.scale(axe1,(150,150))

#mace1 = pygame.image.load('mace1.jpg')
#mace1 = pygame.transform.scale(mace1,(150,150))

#warHammer1 = pygame.image.load('warHammer1.jpg')
#warHammer1 = pygame.transform.scale(warHammer1,(150,150))

dStanceIcon = pygame.image.load('dStanceIcon.jpg')
dStanceIcon = pygame.transform.scale(dStanceIcon,(50,50))

oStanceIcon = pygame.image.load('oStanceIcon.jpg')
oStanceIcon = pygame.transform.scale(oStanceIcon,(50,50))

bruteQ = pygame.image.load('bruteQ.jpg')
bruteQ = pygame.transform.scale(bruteQ,(165,400))

furyAnimation = pygame.image.load('furyAnimation.jpg')
furyAnimation = pygame.transform.scale(furyAnimation,(1200,800))

#sound Effects
bruteSelect = pygame.mixer.Sound("bruteSelect.wav")
mageSelect = pygame.mixer.Sound("mageSelect.wav")
assassinSelect = pygame.mixer.Sound("assassinSelect.wav")

#colors
green = (0,255,0)
yellow = (255,255,0)
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
grey = (192,192,192)
purple = (255,0,255)

#effects
flashScreenOne = pygame.image.load('flashScreenOne.jpg')
flashScreenOne = pygame.transform.scale(flashScreenOne,(1200,800))
flashScreenTwo = pygame.image.load('flashScreenTwo.jpg')
flashScreenTwo = pygame.transform.scale(flashScreenTwo,(1200,800))

#globals

currentSpell = False
# = False

resetSpell = False


poisoned = False

flashEffect = False


def valkenCast(ability,playerHealth,spellPower,playerInput,valkenObjects):
        global resetSpell
        #global Brute.defensiveStance
        global poisoned
        global flashEffect
        
        
        
        def drawLazers(num_of_lazers):
                def drawSingleLazer(specificLazer):
                        if specificLazer == 1:
                                pygame.draw.line(win,red,(975,110),(200,680),1)
                                lazer1LetterText = rockWell.render(valkenObjects[0].letter,3,blue)
                                win.blit(lazer1LetterText,valkenObjects[0].location)
                                
                        if specificLazer == 2:
                                pygame.draw.line(win,red,(975,130),(200,700),1)
                                lazer2LetterText = rockWell.render(valkenObjects[1].letter,3,blue)
                                win.blit(lazer2LetterText,valkenObjects[1].location)
                                
                        if specificLazer == 3:
                                pygame.draw.line(win,red,(975,90),(200,660),1)
                                lazer3LetterText = rockWell.render(valkenObjects[2].letter,3,blue)
                                win.blit(lazer3LetterText, valkenObjects[2].location)
                                
                                
                if num_of_lazers == 1 and valkenObjects[0].letter not in playerInput:
                        drawSingleLazer(1)
                       
                elif num_of_lazers == 2 and valkenObjects[0].letter not in playerInput or num_of_lazers == 2 and valkenObjects[1].letter not in playerInput:
                        if valkenObjects[0].letter not in playerInput:
                                drawSingleLazer(1)
                                
                        if valkenObjects[1].letter not in playerInput:
                                drawSingleLazer(2)
                        
                elif num_of_lazers == 3 and valkenObjects[0].letter not in playerInput or num_of_lazers == 3 and valkenObjects[1].letter not in playerInput or num_of_lazers == 3 and valkenObjects[2].letter not in playerInput:
                        if valkenObjects[0].letter not in playerInput:
                                drawSingleLazer(1)
                                
                        if valkenObjects[1].letter not in playerInput:
                                drawSingleLazer(2)

                        if valkenObjects[2].letter not in playerInput:
                                drawSingleLazer(3)
                       
                else:
                        
                        global resetSpell
                        resetSpell = True
                        
        def summonVortex(type_of_vortex,vortexPhase,vortexX,vortexY,playerHealth):
                global resetSpell
                global poisoned
                #vortexDone = False
                
                #damage vortex
                if type_of_vortex == 1 and vortexPhase == 1:
                        win.blit(vortexOne1,(vortexX,vortexY))
                elif type_of_vortex == 1 and vortexPhase == 2:
                        win.blit(vortexOne2,(vortexX,vortexY))
                elif type_of_vortex == 1 and vortexPhase == 3:
                        win.blit(vortexOne3,(vortexX,vortexY))
                elif type_of_vortex == 1 and vortexPhase == 4:
                        win.blit(vortexOne4,(vortexX,vortexY))
            
                #poison vortex        
                if type_of_vortex == 2 and vortexPhase == 1:
                        win.blit(vortexTwo1,(vortexX,vortexY))
                if type_of_vortex == 2 and vortexPhase == 2:
                        win.blit(vortexTwo2,(vortexX,vortexY))
                if type_of_vortex == 2 and vortexPhase == 3:
                        win.blit(vortexTwo3,(vortexX,vortexY))
                if type_of_vortex == 2 and vortexPhase == 4:
                        win.blit(vortexTwo4,(vortexX,vortexY))
              
                #flashEffect vortex        
                if type_of_vortex == 3 and vortexPhase == 1:
                        win.blit(vortexThree1,(vortexX,vortexY))
                if type_of_vortex == 3 and vortexPhase == 2:
                         win.blit(vortexThree2,(vortexX,vortexY))
                if type_of_vortex == 3 and vortexPhase == 3:
                         win.blit(vortexThree3,(vortexX,vortexY))
                if type_of_vortex == 3 and vortexPhase == 4:
                         win.blit(vortexThree4,(vortexX,vortexY))
          
                        #damage vortex
                        #55.520
                        
                if type_of_vortex == 1 and valkenObjects[0] <= 55 and valkenObjects[1] >= 250:
                        if valkenObjects[0] > 53 and valkenObjects[1] >= 250:
                                return type_of_vortex
                               # playerHealth -= 10
                                #return playerHealth
                               # vortexDone = True
                
                        
                elif type_of_vortex == 2 and valkenObjects[0] <= 55 and valkenObjects[1] >= 250:
                        if valkenObjects[0] > 53 and valkenObjects[1] >= 250:
                                return type_of_vortex
                                #playerHealth -= 10
                                #return playerHealth
                                #global poisoned
                                #poisoned = True
                                #vortexDone = True
                        
                        
                         
                elif type_of_vortex == 3 and valkenObjects[0] <= 55 and valkenObjects[1] >= 250:
                        if valkenObjects[0] > 53 and valkenObjects[1] >= 250:
                                return type_of_vortex
                                #return playerHealth
                                #vortexDone = True
                        
                else:
                        
                        type_of_vortex = 0
                        return type_of_vortex
                        
       
                #if vortexDone:
                        #print('wtf how are you escaping?',playerHealth)
                        #playerHealth = playerHealth
                        #return playerHealth
                        #global resetSpell
                        #resetSpell = True         
       
                        
        if ability[0] == 'l':
                drawLazers(spellPower)
                if Brute.defensiveStance:
                        playerHealth -= .05 * spellPower
                else:
                        playerHealth -= .1 * spellPower
                        
                return playerHealth
        
        if ability[0] == 'v':
                vortexID = summonVortex(spellPower,valkenObjects[2],valkenObjects[0],valkenObjects[1],playerHealth)
                if vortexID == 0:
                        #print('hitting')
                        return playerHealth
                elif vortexID == 1:
                        if Brute.defensiveStance == True:
                                playerHealth -= 40
                                resetSpell = True
                        else:
                                playerHealth -= 80
                                resetSpell = True
                        return playerHealth
                elif vortexID == 2:
                        poisoned = True
                        resetSpell = True
                        return playerHealth
                elif vortexID == 3:
                        flashEffect = True
                        resetSpell = True
                        return playerHealth
                        
                        
                        
                
               
                
                
def drawTakeDamage(objects,currentPhase):
        image = objects.image
        damageImage = objects.damageImage
        switchID = objects.drawID
        timer = objects.damageTimer
        if currentPhase == 2 and objects.name == 'Valken':
                if objects.currentX == objects.harborX and objects.currentY == objects.harborY:
                        objects.faceNumber = 1
                else:
                        if objects.reflect or objects.puking:
                                objects.faceNumber = 1
                        else:
                                objects.faceShift()
                            
                if objects.faceNumber == 1:
                        if objects.puking:
                                image = pygame.transform.scale(objects.get_Puking_Image(),(objects.sizeX,objects.sizeY))
                                objects.damageImage = pygame.transform.scale(valkenVomitDamage,(objects.sizeX,objects.sizeY))
                                damageImage = objects.damageImage
                                
                        elif not objects.puking and objects.laughing:
                                image = pygame.transform.scale(objects.get_Laughing_Image(),(objects.sizeX,objects.sizeY))
                                objects.damageImage = pygame.transform.scale(valkenTakingDamage2,(objects.sizeX,objects.sizeY))
                                damageImage = objects.damageImage
                                
                        else:        
                                image = pygame.transform.scale(valkenTwo,(objects.sizeX,objects.sizeY))
                                objects.damageImage = pygame.transform.scale(valkenTakingDamage2,(objects.sizeX,objects.sizeY))
                                damageImage = objects.damageImage
                else:
                        image = pygame.transform.scale(valkenTwoFace,(objects.sizeX,objects.sizeY))
                        objects.damageImage = pygame.transform.scale(valkenTakingDamage2Face,(objects.sizeX,objects.sizeY))
                        damageImage = objects.damageImage
                    
        elif currentPhase == 1 and objects.name == 'Valken':
                #objects.currentX = 900
                #objects.currentY = 0
                damageImage = valkenTakingDamage
                #if objects.speaking:
                        #if objects.speakNumber <= 5 and objects.currentX < 600:
                                #image = valkenSpeak1
                        #elif objects.speakNumber > 5 and objects.currentX < 600:
                                #image = valkenSpeak2
                        #elif objects.speakNumber <= 5 and objects.currentY >= 600:
                                #image = valkenRSpeak1
                        #elif objects.speakNumber > 5 and objects.currentY >= 600:
                                #image = valkenRSpeak2
            #elif image == yellowSkulls.image:
                    #damageImage = 
            
        if timer > 5:
                if switchID == 1:
                        #if not phase2 and not phase3:
                        win.blit(damageImage,(objects.currentX,objects.currentY))
                        #need to create a valken coordinates for drawing adjustments for next phases                
                        switchID = 2
                        objects.drawID = switchID
                        timer -= 2
                        objects.damageTimer = timer
                        
                        #return switchID, timer
                            
                        
                elif switchID == 2:
                        #if not phase2 and not phase3:
                        win.blit(damageImage,(objects.currentX - 10,objects.currentY))
                        #need to create a valken coordinates for drawing adjustments for next phases        
                        switchID = 3
                        objects.drawID = switchID
                        timer -= 2
                        objects.damageTimer = timer
                        
                        #return switchID, timer

                elif switchID == 3:
                        win.blit(damageImage,(objects.currentX - 10,objects.currentY))
                        switchID = 1
                        objects.drawID = switchID
                        timer -= 2
                        objects.damageTimer = timer
                                
        else:
                    
                timer = 2
                win.blit(image,(objects.currentX,objects.currentY))
                #return switchID, timer
             
def determineImage(objImageList,timer,iteration,increments,cycled):
        timer += 1
        print(timer)
        if timer >= increments:
                iteration += 1
                timer = 0
        
        maxIteration = len(objImageList) - 1
        if iteration > maxIteration:
                cycled = True
                iteration = 1

        #print('the iteration is: ',iteration)
        image = objImageList[iteration]
        return image,timer,iteration,increments,cycled

def findSlope(y2,y1,x2,x1):
        slope = (y2 - y1) / (x2 - x1)
        return slope

def slopeTarget(destY,userY,destX,userX,currentSlope):
        if userY not in range(destY - 10,destY + 10):
            if userY < destY and userX > destX:     #because the denominator is converting the top to negative and the pygame uses inverted y increases
                    userY -= Fraction(currentSlope).limit_denominator().numerator
            elif userY < destY and userX < destX: 
                    userY += Fraction(currentSlope).limit_denominator().numerator
            elif userY > destY and userX < destX:
                    userY += Fraction(currentSlope).limit_denominator().numerator
            elif userY > destY and userX > destX:
                    userY -= Fraction(currentSlope).limit_denominator().numerator
        else:
                userY = userY
        
        if userX not in range(destX - 10, destX + 10):
                if userX > destX:
                        userX -= Fraction(currentSlope).limit_denominator().denominator
                else:
                        userX += Fraction(currentSlope).limit_denominator().denominator
        else:
                userX = userX
        return userY,userX
              
def findTarget(userX,destX,userY,destY,speed):
                if userX < destX:
                        userX += speed
                elif userX > destX:
                        userX -= speed
                if userY < destY:
                        userY += speed
                elif userY > destY:
                        userY -= speed
                if userX in range(destX - 15,destX + 15):
                        userX = destX
                if userY in range(destY - 15,destY + 15):
                        userY = destY
                        
                return userX,userY
        

def rangeCheckTarget(userX,destX,userY,destY):
        if userX in range(destX - 10,destX + 10):
                userX = destX
        if userY in range(destY - 10,destY + 10):
                userY = destY

        if userX == destX and userY == destY:
                return True
        else:
                return False
        
                
#Classes

class Class:
        def __init__(self,name,health,resource,abilityList,imageList,experience):
            self.name = name
            self.health = health
            self.resource = resource
            self.abilityList = abilityList
            self.imageList = imageList
            self.experience = experience


class Brute:
        defensiveStance = False
        qActive = False
        furyOn = False
        currentX = 0
        currentY = 650
        sizeX = 300
        sizeY = 300


        inputList = set()
        def __init__(self,name,health,resource,imageList,experience):
                self.name = name
                self.health = health
                self.resource = resource
                self.imageList = imageList
                self.experience = experience
                
player = Brute('default',0,0,0,0)
                
class airlock:
        name = 'Airlock'
        health = 300
        image = airlockLockC1
        sizeX = 90
        sizeY = 90
        damageImage = airlockLockTakeDamage
        damageTimer = 2
        drawID = 1
        reflect = False
        #airlockSpinDict = {1:airlockLockC1, 2:airlockLockC2, 3:airlockLockC3, 4:airlockLockC4}
        spinCounter = 120

        SoundOnce = False
        
        def __init__(self,imageI,imageBroken,imageX,imageY,currentX,currentY):
                self.imageI = imageI
                self.imageBroken = imageBroken
                self.imageX = imageX
                self.imageY = imageY
                self.harborX = imageX
                self.harborY = imageY
                self.currentX = currentX
                self.currentY = currentY
                
                
                
                
        def airlockSpin(self):
                self.spinCounter -= 1
                if self.spinCounter >= 90:
                        self.image = airlockLockC1
                elif self.spinCounter >= 60:
                        self.image = airlockLockC2
                elif self.spinCounter >= 30:
                        self.image = airlockLockC3
                elif self.spinCounter >= 0:
                        self.image = airlockLockC4
                else:
                        self.spinCounter = 120
                        
        def reset(self):
                self.health = 300
                self.damageTimer = 2
                self.SoundOnce = False
                
                
airlock1 = airlock(airlock1Image,airlock1ImageBroken,320,125,410,280) #310  125
airlock2 = airlock(airlock2Image,airlock2ImageBroken,600,125,675,280) #590 125

class shrinker():
        name = 'ShrinkMachine'
        health = 200
        currentX = 900
        currentY = -200
        harborX = 900
        harborY = 0
        sizeX = 200
        sizeY = 200
        shrinkX = 20
        shrinkY = 20
        image = startingTurrent
        imageID = 1
        damageImage = startingTurrent
        reflect = False
        


        animationTimer = 1
        animationCounter = 0
        shrinkerExplosionList = [shrinkE1,shrinkE2,shrinkE3,shrinkE4,shrinkE5,shrinkE6,shrinkE7]
        
        drawID = 1
        damageTimer = 2

        shrinkRaySoundOnce = False
        shrinkExplodeSoundOnce = False
        

        #imagePointDict = {
        #lazerPointDict = 
        damageImageDict = {1: r1Dimage, 2: r2Dimage, 3: r3Dimage, 4: r4Dimage, 5: r5Dimage, 6: r6Dimage, 7: r7Dimage, 8: r8Dimage}
        lazerPointDict = {1: [915,188], 2: [928,171], 3: [938,178], 4: [928,194], 5: [951,181], 6: [975,189], 7: [987,191], 8: [1013,197]}
        #harborSound = 
        #damageSound =
        #shrinkSound = 
        active = False 

        currentTarget = 0
        lazerPoint = [1,2]

        def reset(self):
                self.health = 200
                self.currentX = 900
                self.currentY = - 200
                self.active = False
                self.damageTimer = 2
                
                
        def updateLazerPoint(self):
                self.lazerPoint = self.lazerPointDict[self.imageID]

        def updateDamageImage(self):
                self.damageImage = self.damageImageDict[self.imageID]
                
        def updateImage(self,target):
                if target.currentX in range(0,800) and target.currentY < 300:
                        self.imageID = 2
                        self.image = r2Image
                        
                elif target.currentX in range(0,600):
                        self.imageID = 1
                        self.image = r1Image
                
                elif target.currentX in range(600,700):
                        self.imageID = 3
                        self.image = r3Image
                elif target.currentX in range(700,800):
                        self.imageID = 4
                        self.image = r4Image
                elif target.currentX in range(800,900):
                        self.imageID = 5
                        self.image = r5Image
                elif target.currentX in range(900,1000):
                        self.imageID = 6
                        self.image = r6Image
                elif target.currentX in range(1000,1100):
                        self.imageID = 7
                        self.image = r7Image
                elif target.currentX in range(1100,1200):
                        self.imageID = 8
                        self.image = r8Image

                        
        def animateExplosion(self):        
                self.animationTimer += 1
                self.image = self.shrinkerExplosionList[self.animationCounter]
                win.blit(self.image,(self.currentX,self.currentY))
                if self.animationTimer >= 7:
                        animationCounter += 1
                        self.animationTimer = 1

                
                
        def trackRay(self):
                #self.currentTarget.speed = 8
                if self.health > 0:
                        self.updateImage(self.currentTarget)
                        self.updateDamageImage()
                        self.updateLazerPoint()
                        drawTakeDamage(self,self.currentTarget.phase)
                        pygame.draw.line(win,green,(self.lazerPoint[0],self.lazerPoint[1]),(self.currentTarget.currentX + self.currentTarget.sizeX / 2,self.currentTarget.currentY + self.currentTarget.sizeY / 2),2)


                
        def startShrink(self):
                if not self.shrinkRaySoundOnce:
                        shrinkRaySound.play()
                        self.shrinkRaySoundOnce = True
                        
                if self.currentTarget.sizeX == self.shrinkX and self.currentTarget.sizeY == self.shrinkY and not self.active:
                        self.active = True
                        #self.currentTarget.speed = 6
                
                        
                if self.active:
                        
                        #self.currentTarget.speed = 6
                        self.trackRay()
                        
                else:
                        self.image = r2Image
                        self.updateLazerPoint()
                        self.updateDamageImage()
                        drawTakeDamage(self,self.currentTarget.phase)
                        pygame.draw.line(win,green,(self.lazerPoint[0],self.lazerPoint[1]),(self.currentTarget.currentX + self.currentTarget.sizeX / 2, self.currentTarget.currentY + self.currentTarget.sizeY / 2),2)
                        if self.currentTarget.sizeX > self.shrinkX:
                                self.currentTarget.sizeX -= 10
                        if self.currentTarget.sizeY > self.shrinkY:
                                self.currentTarget.sizeY -= 10
                        
                        

                        
        def loadShrinker(self,target):
                self.currentTarget = target
                if self.currentY == self.harborY:
                        self.startShrink()
                else:        
                        if self.currentY < self.harborY:
                                self.currentY += 10
                        self.image = startingTurrent
                        win.blit(self.image,(self.currentX,self.currentY))
              
               
shrinkMachine = shrinker()

starList = [None,starP1,starP2,starP3,starP4,starP5]
flashList = [None,starY1,starY2,starY3,starY4,starY5]

class Orb:
        name = 'Orb'
        currentX = 0
        currentY = 0
        image = blueOrb1
        sender = 0
        target = 0
        active = True
        damage = 10
        speed = 4
        orbList = []
        blueOrbImagesList = [blueOrb1, blueOrb2, blueOrb3, blueOrb4, blueOrb5, blueOrb6, blueOrb7]
        redOrbImagesList = [redOrb1, redOrb2, redOrb3, redOrb4, redOrb5, redOrb6, redOrb7]
        gOrbImageList = [gargOrbF1,gargOrbF2,gargOrbF3,gargOrbF4,gargOrbF5,gargOrbF6]
        animationTimer = 0
        animationCounter = 1
        animateActive = False

        gOrbTimer = 1
        gOrbCounter = 0

        
        def __init__(self,sender,target,upgradeLevel):
                self.sender = sender
                self.target = target
                self.upgradeLevel = upgradeLevel
                self.currentX = self.sender.currentX + self.sender.sizeX / 2
                self.currentY = self.sender.currentY + self.sender.sizeY / 2
                self.randomShotX = self.target.currentX + random.randint(0,200)
                self.randomShotY = self.target.currentY + random.randint(0,125)
                
                if upgradeLevel == 4:
                        self.name = 'Skeleton'
                        self.health = 25
                        self.damage = 5
                        self.speed = 2
                        self.currentX = self.sender.currentX + 225
                        self.currentY = self.sender.harborFaceY + 200
                        self.sizeX = 75
                        self.sizeY = 75
                        self.skeleWalkTimer = 140
                        self.skeleAttackTimer = 180
                        self.skeleDeathTimer = 160
                        self.damageTimer = 2
                        self.damageImage = skZ4
                        self.damageTimer = 2
                        self.drawID = 1

                        self.dead = False
                        self.reflect = False
                
                #make titanSkeles using the determineImage and the determineimage requirements
                if upgradeLevel == 44:
                        self.name = 'Skeleton'
                        self.health = 25
                        self.damage = 5
                        self.speed = 2
                        self.currentX = self.sender.currentX + 225
                        self.currentY = self.sender.harborFaceY + 200
                        self.sizeX = 75
                        self.sizeY = 75
                        self.damageTimer = 2
                        self.damageImage = skZ4
                        self.damageTimer = 2
                        self.drawID = 1

                        self.dead = False
                        self.reflect = False

                        self.imageTimer = 0
                        self.iterationNumber = 1
                        self.increment = 5
                        self.cycled = False
                        
                if upgradeLevel == 7 or upgradeLevel == 8:
                        self.randomShotY = self.target.currentY - 20
                        self.imageTimer = 0
                        self.iterationNumber = 1
                        self.increment = 5
                        self.cycled = False
                        if upgradeLevel == 7:
                                self.speed = 8
                                self.damage = 15
                        else:
                                self.damage = 0
                                self.speed = 4
                                
        def getSkeleDeath(self):
                self.skeleDeathTimer -= 10

                if self.skeleDeathTimer >= 150:
                        image = skD1
                        dead = False
                elif self.skeleDeathTimer >= 140:
                        image = skD2
                        dead = False
                elif self.skeleDeathTimer >= 130:
                        image = skD3
                        dead = False
                elif self.skeleDeathTimer >= 120:
                        image = skD4
                        dead = False
                elif self.skeleDeathTimer >= 110:
                        image = skD5
                        dead = False
                elif self.skeleDeathTimer >= 100:
                        image = skD6
                        dead = False
                elif self.skeleDeathTimer >= 90:
                        image = skD7
                        dead = False
                elif self.skeleDeathTimer >= 80:
                        image = skD8
                        dead = False
                elif self.skeleDeathTimer >= 70:
                        image = skD9
                        dead = False
                elif self.skeleDeathTimer >= 60:
                        image = skD10
                        dead = False
                elif self.skeleDeathTimer >= 50:
                        image = skD11
                        dead = False
                elif self.skeleDeathTimer >= 40:
                        image = skD12
                        dead = False
                elif self.skeleDeathTimer >= 30:
                        image = skD13
                        dead = False
                elif self.skeleDeathTimer >= 20:
                        image = skD14
                        dead = False
                elif self.skeleDeathTimer >= 10:
                        image = skD15
                        dead = False
                else:
                        image = skD15
                        dead = True
                        
                return image,dead
        
        
        def animateExplosion(self):
                if self.upgradeLevel == 4:
                        self.image,self.dead = self.getSkeleDeath()
                        win.blit(self.image,(self.currentX,self.currentY))
                        if self.dead:
                                self.active = False
                                
                elif self.upgradeLevel == 7 or self.upgradeLevel == 8:
                        self.active = False
                else:
                        self.animationTimer += 1
                        if self.upgradeLevel == 1:
                                self.image = self.blueOrbImagesList[self.animationCounter]
                                
                        elif self.upgradeLevel == 2:
                                self.image = self.redOrbImagesList[self.animationCounter]
                                
                        if self.upgradeLevel == 3 or self.upgradeLevel == 'Potrait':
                                self.active = False

                        win.blit(self.image,(self.currentX,self.currentY))
                        if self.animationTimer > 30:
                                if self.image == self.redOrbImagesList[6] or self.image == self.blueOrbImagesList[6]:   #and self.animationTimer >= 30
                                        self.active = False
                                        
                                else:
                                        self.image = self.blueOrbImagesList[self.animationCounter]
                                        self.animationCounter += 1
                                        self.animateTimer = 0
                        
                        
        def orbExplode(self):
                global flashEffect
                if not self.animateActive and self.name != 'Skeleton':
                        #skele doesnt deal damage on death/explosion but is an orb moving object
                        if self.upgradeLevel == 8:
                                flashEffect = True
                        self.target.health -= self.damage
                        self.animateActive = True
                else:
                        #continue animation at end make active false and end the orb
                        self.animateExplosion()
                
                #self.animateExplosion()
                
        def checkExplosion(self):
                #checking player center - ranged location
                #if self.sender.name == 'Simon':
                       # if health <= 0:
                                #print('im dead')
                               
                if self.currentX < 220 and self.currentY > 600:
                        self.orbExplode()
                '''        
                if self.currentX in range(self.randomShotX - 10, self.randomShotX + 10):
                        self.currentX = self.randomShotX
                if self.currentY in range(self.randomShotY - 10, self.randomShotY + 10):
                        self.currentY = self.randomShotY
                '''
        def getSkeleDeadth(self):
                self.skeleDeathTimer -= 10

                if self.skeleDeathTimer >= 150:
                        image = skD1
                elif self.skeleDeathTimer >= 140:
                        image = skD2
                elif self.skeleDeathTimer >= 130:
                        image = skD3
                elif self.skeleDeathTimer >= 120:
                        image = skD4
                elif self.skeleDeathTimer >= 110:
                        image = skD5
                elif self.skeleDeathTimer >= 100:
                        image = skD6
                elif self.skeleDeathTimer >= 90:
                        image = skD7
                elif self.skeleDeathTimer >= 80:
                        image = skD8
                elif self.skeleDeathTimer >= 70:
                        image = skD9
                elif self.skeleDeathTimer >= 60:
                        image = skD10
                elif self.skeleDeathTimer >= 50:
                        image = skD11
                elif self.skeleDeathTimer >= 40:
                        image = skD12
                elif self.skeleDeathTimer >= 30:
                        image = skD13
                elif self.skeleDeathTimer >= 20:
                        image = skD14
                elif self.skeleDeathTimer >= 10:
                        image = skD15
                else:
                        image = skD1
                        self.skeleDeathTimer = 160
                        
                return image

        
        def getSkeleWalk(self):
                self.skeleWalkTimer -= 10
                
                if self.skeleWalkTimer >= 130:
                        image = skW1
                elif self.skeleWalkTimer >= 120:
                        image = skW2
                elif self.skeleWalkTimer >= 110:
                        image = skW3
                elif self.skeleWalkTimer >= 100:
                        image = skW4
                elif self.skeleWalkTimer >= 90:
                        image = skW5
                elif self.skeleWalkTimer >= 80:
                        image = skW6
                elif self.skeleWalkTimer >= 70:
                        image = skW7
                elif self.skeleWalkTimer >= 60:
                        image = skW8
                elif self.skeleWalkTimer >= 50:
                        image = skW9
                elif self.skeleWalkTimer >= 40:
                        image = skW10
                elif self.skeleWalkTimer >= 30:
                        image = skW11
                elif self.skeleWalkTimer >= 20:
                        image = skW12
                elif self.skeleWalkTimer >= 10:
                        image = skW13
                else:
                        image = skW1
                        self.skeleWalkTimer = 140
                        
                return image
        
        def getSkeleStrike(self):
                self.skeleAttackTimer -= 10
                
                if self.skeleAttackTimer >= 170:
                        image = skA1
                elif self.skeleAttackTimer >= 160:
                        image = skA2
                elif self.skeleAttackTimer >= 150:
                        image = skA3
                elif self.skeleAttackTimer >= 140:
                        image = skA4
                elif self.skeleAttackTimer >= 130:
                        image = skA5
                elif self.skeleAttackTimer >= 120:
                        image = skA6
                elif self.skeleAttackTimer >= 110:
                        image = skA7
                elif self.skeleAttackTimer >= 100:
                        image = skA8
                elif self.skeleAttackTimer >= 90:
                        image = skA9
                elif self.skeleAttackTimer >= 80:
                        image = skA10
                elif self.skeleAttackTimer >= 70:
                        image = skA11
                elif self.skeleAttackTimer >= 60:
                        image = skA12
                elif self.skeleAttackTimer >= 50:
                        image = skA13
                elif self.skeleAttackTimer >= 40:
                        image = skA14
                elif self.skeleAttackTimer >= 30:
                        image = skA15
                elif self.skeleAttackTimer >= 20:
                        image = skA16
                elif self.skeleAttackTimer >= 10:
                        image = skA17
                elif self.skeleAttackTimer >= 0:
                        image = skA18
                else:
                        image = skA1
                        self.skeleAttackTimer = 180
                        
                return image
                
                


        def orbMove(self):
                                
                if self.upgradeLevel == 1:
                        self.image = blueOrb1
                        self.speed = 10
                elif self.upgradeLevel == 2:
                        self.image = redOrb1
                        self.damage = 30
                elif self.upgradeLevel == 3:
                        self.gOrbTimer += 1
                        if self.image == self.gOrbImageList[5] and self.gOrbTimer >=6:
                                self.gOrbCounter = 0
                        if self.gOrbTimer > 8:
                                self.gOrbCounter += 1
                                self.gOrbTimer = 1
                        self.image = self.gOrbImageList[self.gOrbCounter]
                        self.damage = 50
                        
                elif self.upgradeLevel == 'Potrait':
                        self.image = punishPotrait
                        self.speed = 8
                        self.damage = 50
                        
                elif self.upgradeLevel == 4:
                        self.image = skeletonImage
                        self.speed = 2
                        self.damage = 4

                        
                elif self.upgradeLevel == 7 or self.upgradeLevel == 8:
                        if self.upgradeLevel == 7:
                                self.image,self.imageTimer,self.iterationNumber,self.increment,self.cycled = determineImage(starList,self.imageTimer,self.iterationNumber,self.increment,self.cycled)
                        elif self.upgradeLevel == 8:
                                self.image,self.imageTimer,self.iterationNumber,self.increment,self.cycled = determineImage(flashList,self.imageTimer,self.iterationNumber,self.increment,self.cycled)
                        
                        
                if not self.animateActive:
                        if self.sender == p4: 
                                self.currentY += 4
                                self.currentX -= 8
                                win.blit(self.image,(self.currentX,self.currentY))
                                self.checkExplosion()
                                
                        elif self.sender == p5:
                                self.currentY += 3
                                self.currentX -= 8.5
                                win.blit(self.image,(self.currentX,self.currentY))
                                self.checkExplosion()
                                
                        elif self.sender == p6:
                                self.currentY += 2
                                self.currentX -= 9
                                win.blit(self.image,(self.currentX,self.currentY))
                                self.checkExplosion()
                                
                        elif self.sender.name == 'Simon':
                                                
                                if self.currentX > 250 and self.health > 0:
                                        if self.upgradeLevel == 4:
                                                self.currentX -= self.speed
                                                self.image = self.getSkeleWalk()
                                                drawTakeDamage(self,1)
                                                
                                       #elif self.upgradeLevel == 44:
                                        
                                elif self.currentX <= 250 and self.health > 0:
                                        if self.upgradeLevel == 4:
                                                self.image = self.getSkeleStrike()
                                                if self.skeleAttackTimer == 100:
                                                        self.target.health -= self.damage
                                                drawTakeDamage(self,1)

                                       #elif self.upgradeLevel == 44:
                                                
                                        
                                else:
                                        self.orbExplode()
                        else:
                                #print(self.sender.name)
                                print(self.randomShotY)
                                self.currentX,self.currentY = findTarget(self.currentX,self.randomShotX,self.currentY,self.randomShotY,self.speed)      #functions of ORBS in list and ^^^^^
                                win.blit(self.image,(self.currentX,self.currentY))
                                #print('orbsX: ',self.currentX,' orbsY: ', self.currentY)
                                self.checkExplosion()
                else:
                        self.orbExplode()
                
        #def createOrb(self):                                                            #DONE BY OTHER OBJECTS INTO A LIST
                #self.currentX = self.sender.currentX + self.sender.sizeX / 2
                #self.currentY = self.sender.currentY + self.sender.sizeY / 2
                #self.orbList.append(self)
                
                
                        
                
                
        
                     
class lazerFly:
        name = 'fly'
        health = 1
        currentPower = 1
        image = lazerFlyImage
        damageImage = lazerFlyDamageImage
        direction = 1
        directionCounter = 0
        sizeX = 75
        sizeY = 75

        markY = 0
        
        drawID = 1
        damageTimer = 2

        attackTimer = 100

        flyExplosionList = [flyE1,flyE2,flyE3,flyE3,flyE4,flyE5,flyE6,flyE7]
        explosionSoundList = [flyExSound,flyEx2Sound]
        explodeSoundOnce = False
        active = True
        reflect = False


        assignedX = None
        assignedY = None
        assignedLocation = False
        locationReached = False
        
        animationTimer = 1
        animationCounter = 0
        

        def __init__(self,currentX,currentY):
                self.currentX = currentX
                self.currentY = currentY
                self.harborX = currentX
                self.harborY = currentY
                self.markY = self.currentY
                self.turnY = self.markY + 30
                
                #self.turnY = currentY + 5


        def upgrade(self):
                if self.currentPower < 3:
                        self.currentPower += 1
                if self.currentPower == 2:
                        self.image = lazerFlyImage2
                        self.damageImage = lazerFly2DamageImage
                        self.health = 30
                if self.currentPower == 3:
                        self.image = lazerFlyImage3
                        self.damageImage = lazerFly3DamageImage
                        self.health = 60
                else:
                        pass
                        
                        
                        
        def animateExplosion(self):
                if not self.explodeSoundOnce:
                        flyExplosionSound = random.choice(self.explosionSoundList)
                        flyExplosionSound.play()
                        self.explodeSoundOnce = True
                self.animationTimer += 1
                self.image = self.flyExplosionList[self.animationCounter]
                win.blit(self.image,(self.currentX,self.currentY))
                if self.animationTimer > 4:
                        if self.image == self.flyExplosionList[6] and self.animationTimer >= 4:
                                self.active = False
                        else:
                                self.animationTimer = 1
                                self.animationCounter += 1
                        
                
        def flyAttack(self,upgradeNumber):
                #if upgradeNumber == 1:
                Orb.orbList.append(Orb(self,self.target,self.currentPower))
                #elif upgradeNumber == 2:
                       
                #elif upgradeNumber == 3:
                        
                        

                        
                #for somewhere ahead
                #for i in flyList:
                        #i.flyMove()
                        #drawTakeDamage(i.image,valken.phase)
                        
                        

        def flyMove(self,target):
                self.target = target
                self.attackTimer -= 1
                
                if self.health > 0:
                        drawTakeDamage(self,2)
                        if self.attackTimer == 0 and self.currentPower == 1:
                                #self.image = level 1 fly
                                self.attackTimer = 100
                                self.flyAttack(self.currentPower)
                                
                        elif self.attackTimer == 0 and self.currentPower == 2:
                                #self.image = level 2 fly
                                self.attackTimer = 125
                                self.flyAttack(self.currentPower)
                                
                        elif self.attackTimer == 0 and self.currentPower == 3:
                                #self.image = level 3 fly
                                self.attackTimer = 150
                                self.flyAttack(self.currentPower)

                         
                        #win.blit(self.image,(self.currentX,self.currentY))
                        
                        
                        if self.direction == 1:
                                if self.currentY < self.turnY:
                                        self.directionCounter += 1
                                        
                                        self.currentX -= 2
                                        self.currentY += 1

                                else:
                                        self.markY = self.currentY
                                        self.turnY = self.markY + 30
                                        self.direction = 2 # directionCounter at 30
                                        
                        #print(self.direction)                
                        elif self.direction == 2:

                                if self.currentY < self.turnY:         # will need 10 cycles then will =
                                        self.currentX += 2
                                        self.currentY += 1
                                else:
                                        self.markY = self.currentY
                                        self.turnY = self.markY - 30
                                        self.direction = 3
                        
                        #print(self.direction)
                        elif self.direction == 3:
                              
                                if self.currentY > self.turnY:       #will go through another 10 cycles and =
                                        self.currentX += 2
                                        self.currentY -= 1
                                else:
                                        self.markY = self.currentY
                                        self.turnY = self.markY - 30
                                        self.direction = 4

                        elif self.direction == 4:
                                if self.currentY > self.turnY:
                                        self.currentX -= 2
                                        self.currentY -= 1

                                else:
                                        self.markY = self.currentY
                                        self.turnY = self.markY + 30
                                        self.direction = 1

                else:
                        self.animateExplosion()
                        
lazerFlyList = []
                #print(self.direction)                
                #elif self.direction == 4:
                        
                        #findTarget(self.currentX,self.harborX,self.currentY,self.harborY,1)
                        #restartReady = rangeCheckTarget(self.currentX,self.harborX,self.currentY,self.harborY)
                        #if restartReady:
                                #print('hitting restart')
                                #self.directionCounter = 0
                                #self.direction = 1
                                
                        #if self.directionCounter > 0:      #directionCounter starts at 30 and goes down to 0 ready for direction 1 again
                                #self.currentX -= .2
                                #self.currentY -= 1
                                #self.directionCounter -= 1
                                #if self.directionCounter == 0:
                                        #self.direction = 1

                                        
        

                
                        
                        

#testFly = lazerFly(900,500)
class reflector:
        name = 'Reflector'
        health = 200
        currentX = -200
        currentY = 200
        harborX = -50
        harborY = 200
        sizeX = 250
        sizeY = 250
        speed = 4
        shrinkX = 20
        shrinkY = 20
        image = reflectorImage
        sparkImageID = 1
        damageImage = reflectorTakeDamage
        reflectModImages = reflectModImage
        reflectModText = rockWellSmall.render('REFLECTING',3,purple)
        drawingReflections = False
        reflect = False
        reflectedPlayer = False
        engageTimer = 0

        animationTimer = 1
        animationCounter = 0
        
        animateReflected = 0
        


        animationTimer = 1
        animationCounter = 0
        sparkDict = {1: eC1,2: eC2,3: eC3,4: eC4}
        
        drawID = 1
        damageTimer = 2

        sparkSoundOnce = False
        explodeSoundOnce = False
       
        def reset(self):
                self.engageTimer = 0
                self.drawingReflections = False
                self.currentX = - 200
                self.damageTimer = 2
                
                for i in lazerFlyList:
                        i.reflect = False
                shrinkMachine.reflect = False



        def animateExplosion(self):
                if not self.explodeSoundOnce:
                        reflectorsExplodeSound.play()
                        self.explodeSoundOnce = True
                self.animationTimer += 1
                if self.animationCounter < 7:
                        self.image = shrinkMachine.shrinkerExplosionList[self.animationCounter]
                        win.blit(self.image,(self.currentX,self.currentY))
                        if self.animationTimer >= 7:
                                self.animationCounter += 1
                                self.animationTimer = 1
                                
        def spark(self):
                if self.sparkImageID == 1:
                        self.sparkImage = eC1
                        self.sparkImageID = 2
                        
                elif self.sparkImageID == 2:
                        self.sparkImage = eC2
                        self.sparkImageID = 3
                        
                elif self.sparkImageID == 3:
                        self.sparkImage = eC3
                        self.sparkImageID = 4
                        
                elif self.sparkImageID == 4:
                        self.sparkImage = eC4
                        self.sparkImageID = 1


                        
        def drawTargetReflect(self,target):
                sX = target.sizeX
                sY = target.sizeY
                self.reflectModImages = pygame.transform.scale(reflectModImage,(sX + 50,sY))
                win.blit(self.reflectModText,(target.currentX + 60,target.currentY))
                win.blit(self.reflectModImages,(target.currentX,target.currentY))
                
                
        def drawReflections(self):
                
                for i in lazerFlyList:
                        if i.reflect:
                                sX = i.sizeX
                                sY = i.sizeY
                                self.reflectModImages = pygame.transform.scale(reflectModImage,(sX + 15,sY))
                                win.blit(self.reflectModText,(i.currentX,i.currentY - 10))
                                win.blit(self.reflectModImages,(i.currentX,i.currentY))

                if shrinkMachine.health > 0 and shrinkMachine.active:
                                reflectors.drawTargetReflect(shrinkMachine)
                        
                                        
        def reflectorEngage(self):
                drawTakeDamage(self,(2))
                self.engageTimer += 2
                if self.engageTimer == 200:
                        for i in lazerFlyList:
                                i.reflect = True
                                
                        if shrinkMachine.health > 0 and shrinkMachine.active:
                                shrinkMachine.reflect = True
                                
                                        
                if self.engageTimer > 200 and self.engageTimer <= 300:
                        self.spark()
                        if not self.sparkSoundOnce:
                                sparkSound.play()
                                self.sparkSoundOnce = True
                        win.blit(self.sparkImage,(self.currentX + self.sizeX - 165,self.currentY - 20))
                        self.drawingReflections = True
                        
                        
                        
                if self.engageTimer > 300:
                        
                        for i in lazerFlyList:
                                i.reflect = False
                                
                        shrinkMachine.reflect = False
                        self.drawingReflections = False
                        self.engageTimer = 0
                        self.sparkSoundOnce = False

                if self.drawingReflections:
                        reflectors.drawReflections()

                
                        
                        #if shrinkMachine.health > 0 and shrinkMachine.active:
                                #reflectors.drawTargetReflect(shrinkMachine)

        def loadHarborX(self):
                self.currentX,self.currentY = findTarget(self.currentX,self.harborX,self.currentY,self.harborY,self.speed)
                drawTakeDamage(self,(2))
                if self.currentX == self.harborX:
                        self.reflectorEngage()


        def checkPlayerReflects(self):
                if self.animateReflected > 0:
                        self.animateReflected -= 5
                        self.spark()
                        self.sparkImage = pygame.transform.scale(self.sparkImage,(300,300))
                        win.blit(self.sparkImage,(0,550))

reflectors = reflector()


class Moon():
        name = 'Moon'
        health = 100
        currentX = 1500
        currentY = -1000
        sizeX = 400
        sizeY = 400
        destX = -1000
        destY = 1200
        speed = 2.4
        image = moonImage
        damageImage = moonTakingDamage
        stoppedImage = moonStoppedImage
        moonFireCounter = 0
        moonFireDict = {1: fire1, 2: fire2, 3: fire3}
        summoned = False
        recovered = True
        reflect = False

        drawID = 1
        damageTimer = 2


        def moonFire(self):
                self.moonFireCounter += 1
                win.blit(self.moonFireDict[self.moonFireCounter],(self.currentX - 160,self.currentY - 150))
                if self.moonFireCounter == 3:
                        
                        self.moonFireCounter = 0

        def startFall(self):
                self.currentX, self.currentY = findTarget(self.currentX,self.destX,self.currentY,self.destY,self.speed)
                drawTakeDamage(self,2)
                self.moonFire()

        def moonFall(self):
                if self.health >= 100:
                        self.recovered = True
                        
                if self.health <= 0:
                        self.health = 0
                        self.recovered = False
                
                if not self.recovered:
                        win.blit(self.stoppedImage,(self.currentX,self.currentY))
                        self.health += .5
                        self.damageTimer = 2
                        
                if self.health > 0 and self.recovered == True:
                        self.startFall()


        
moon = Moon()

class Portal:
        name = 'Portal'
        active = True
        health = 100
        harborX = -500
        harborY = 0
        sizeX = 200
        sizeY = 200
        reflect = False
        
        image = staticPortal
        damageImage = portalDamageImage
        damageTimer = 2
        drawID = 1
        
        animateStaticTimer = 20
        exitPortalTimer = 20

        pStartXY = [-200,0]
        #p1Coordinate = (50,100)         ############################################## do i still need this?
        #p2Coordinate = (50,220)
        #p3Coordinate = (50,340)
        
        #p4Coordinate = (1000,100)
        #p5Coordinate = (1000,220)
        #p6Coordinate = (1000,340)


        possessed = False
        animateRiftTimer = 5

        harborRiftX = -250
        
        def __init__(self,currentX,currentY):
                self.goX = currentX    #make currentX go to this when active
                self.goY = currentY
                self.currentX = self.harborX   #start currentX at this harbor when made, but stored unique go to in the goX self
                self.currentY = self.harborY
                

                
        def animatePortal(self,ID):
                if ID == 1:
                        self.exitPortalTimer -= 1
                        if self.exitPortalTimer >= 10:
                                self.image = exitPortalOne
                        elif self.exitPortalTimer >= 0:
                                self.image = exitPortalTwo
                        else:
                                self.exitPortalTimer = 20
                                self.image = exitPortalOne
                else:                
                        self.animateStaticTimer -= 1
                        if self.animateStaticTimer >= 10:
                                self.image = staticPortal
                        elif self.animateStaticTimer >= 0:
                                self.image = staticPortal2
                        else:
                                self.animateStaticTimer = 20
                                self.image = staticPortal
                        
                
        def convertToPotrait(self,rightFace,ID):
                self.name = 'Potrait'
                self.health = 1
                self.active = False
                self.punished = False
                self.currentX = -200
                self.ID = ID
                self.sizeX = 120
                self.sizeY = 120 
                self.rightFace = rightFace
                if self.rightFace:
                        self.image = valkenPotrait2
                else:
                        self.image = valkenPotrait
                        
        def convertToRiftPiece(self,ID):
                self.name = 'RiftPiece'
                self.health = 1
                self.currentX = -600
                self.destructionDamage = False
                self.destroyed = False
                if ID == 1:
                        self.image = valkenR1Vuln
                        #self.currentX = 200
                        #self.currentY = 100
                        self.sizeX = 500
                        self.sizeY = 180
                elif ID == 2:
                        self.image = valkenR2Vuln
                        #self.currentX = 200
                        #self.currentY = 300
                        self.sizeX = 600
                        self.sizeY = 250
                elif ID == 3:
                        self.image = valkenR3Vuln
                        #self.currentX = 630
                        #self.currentY = 135
                        self.sizeX = 180
                        self.sizeY = 180
                elif ID == 4:
                        self.image = valkenR4Vuln
                        #self.currentX = 790
                        #self.currentY = 240
                        self.sizeX = 180
                        self.sizeY = 180
                elif ID == 5:
                        self.image = valkenR5Vuln
                        #self.currentX = 740
                        #self.currentY = 360
                        self.sizeX = 80
                        self.sizeY = 60
                elif ID == 6:
                        self.image = valkenR6Vuln
                        #self.currentX = 780
                        #self.currentY = 420
                        self.sizeX = 80
                        self.sizeY = 60
                elif ID == 7:
                        self.image = valkenR7Vuln
                        #self.currentX = 790
                        #self.currentY = 490
                        self.sizeX = 140
                        self.sizeY = 70
                        
        #def rootObject(self):
                #self.currentX = self.harborRiftX
                        
                
        def castPunish(self,addedTarget):
                self.target = addedTarget
                Orb.orbList.append(Orb(self,self.target,self.name))
                self.punished = True

        def checkPossession(self):
                if self.possessed and self.rightFace:
                        image = valkenPotraitP2
                elif self.possessed and not self.rightFace:
                        image = valkenPotraitP
                elif not self.possessed and self.rightFace:
                        image = valkenPotrait2
                elif not self.possessed and not self.rightFace:
                        image = valkenPotrait
                        
                return image
                
        def paint(self):
                if self.health <= 0:
                        self.currentX = -200
                else:
                        if self.ID == 1:
                                self.currentX = 50
                                self.currentY = 180
                                self.image = self.checkPossession()
                                win.blit(self.image,(self.currentX,self.currentY))
                        elif self.ID == 2:
                                self.currentX = 50
                                self.currentY = 290
                                self.image = self.checkPossession()
                                win.blit(self.image,(self.currentX,self.currentY))                 #drawTakeDamage(self,1)
                        elif self.ID == 3:
                                self.currentX = 50
                                self.currentY = 400
                                self.image = self.checkPossession()
                                win.blit(self.image,(self.currentX,self.currentY))
                        elif self.ID == 4:
                                self.currentX = 1000
                                self.currentY = 180
                                self.image = self.checkPossession()
                                win.blit(self.image,(self.currentX,self.currentY))
                        elif self.ID == 5:
                                self.currentX = 1000
                                self.currentY = 290
                                self.image = self.checkPossession()
                                win.blit(self.image,(self.currentX,self.currentY))
                        elif self.ID == 6:
                                self.currentX = 1000
                                self.currentY = 400
                                self.image = self.checkPossession()
                                win.blit(self.image,(self.currentX,self.currentY))

        def riftSpeak(self):
                rng = random.randint(1,4)
                if rng == 1:
                        gSound1.play()
                elif rng == 2:
                        gSound2.play()
                elif rng == 3:
                        gSound3.play()
                elif rng == 4:
                        gSound4.play()
                        
        def animateRiftDestruction(self):
                self.animateRiftTimer -= 1
                if self.animateRiftTimer >= 4:
                        self.riftSpeak()
                        #valkenVanishSound.play()
                        self.image = fireSeq
                        self.image = pygame.transform.scale(self.image,(self.sizeX,self.sizeY))
                        win.blit(self.image,(self.currentX - 10,self.currentY - 50))
                        
                if self.animateRiftTimer >= 3:
                        self.image = fireSeq2
                        self.image = pygame.transform.scale(self.image,(self.sizeX,self.sizeY))
                        win.blit(self.image,(self.currentX - 10,self.currentY - 50))
                        
                elif self.animateRiftTimer >= 2:
                        self.image = fireSeq3
                        self.image = pygame.transform.scale(self.image,(self.sizeX,self.sizeY))
                        win.blit(self.image,(self.currentX - 10,self.currentY - 50))
                        
                elif self.animateRiftTimer >= 1:
                        self.image = fireSeq4
                        self.image = pygame.transform.scale(self.image,(self.sizeX,self.sizeY))
                        win.blit(self.image,(self.currentX - 10,self.currentY - 50))
                else:
                        self.currentX = -300
                        self.destroyed = True
                                
     
                
                
portalOne = Portal(25,20)
portalTwo = Portal(950,20)
exitPortal = Portal(500,500)
exitPortal.sizeX = 250
exitPortal.sizeY = 220
#exitPortal.image = exitPortalOne
#short for potraits borrowing the portal class
#first 3 are on left the next 3 on right (they face each other)
p1 = Portal(0,0) 
p2 = Portal(0,0) 
p3 = Portal(0,0)
p1.convertToPotrait(True,1)
p2.convertToPotrait(True,2)
p3.convertToPotrait(True,3)

p4 = Portal(0,0) 
p5 = Portal(0,0) 
p6 = Portal(0,0) 
p4.convertToPotrait(False,4)
p5.convertToPotrait(False,5)
p6.convertToPotrait(False,6)

pList = [p1,p2,p3,p4,p5,p6]
#rift pieces borrowing portal class
rP1 = Portal(0,0) 
rP2 = Portal(0,0) 
rP3 = Portal(0,0) 
rP4 = Portal(0,0) 
rP5 = Portal(0,0) 
rP6 = Portal(0,0) 
rP7 = Portal(0,0)
rP1.convertToRiftPiece(1)
rP2.convertToRiftPiece(2)  
rP3.convertToRiftPiece(3)  
rP4.convertToRiftPiece(4)  
rP5.convertToRiftPiece(5)  
rP6.convertToRiftPiece(6)  
rP7.convertToRiftPiece(7)  
                

class Simon:
        'simon is a hand using currentX/Y not the face!'
        name = 'Simon'
        health = 100
        sizeX = 200
        sizeY = 200
        currentX = 1400
        currentY = 900
        harborX = 750
        harborY = 350
        faceX = 1500
        faceY = 900
        harborFaceX = 900  #900
        harborFaceY = 375
        image = simonHand
        faceImage = simon1
        target = player

        reflect = False
        damageImage = simonHandTakeDamage
        damageTimer = 2
        drawID = 1
        jawOpen = 0

        respawnRate = 5
        spitTimer = None
        spitStart = None
        
        dyingHandList = [None,handDead1,handDead2,handDead3,handDead4,handDead5]
        imageTimer = 0
        iterationNumber = 1
        increment = 10
        cycled = False
        simonCycleLevel = 1
        simonSoundPlayed = False
        climbTimer = 0
        summonTitanTimer = 0
        
        def closeMouth(self):
                self.jawOpen -= 1
                if self.jawOpen <= 30:
                        simonDeadSound.play()
                        self.faceImage = faceDead3
                elif self.jawOpen > 30 and self.jawOpen <= 60:
                        self.faceImage = faceDead2
                else:
                        self.faceImage = faceDead1
                        self.jawOpen = 0
                        
        def fallDown(self):
                if self.cycled:
                        self.currentX = 1400
                        self.currentY = 900
                        faceX = 1500
                        faceY = 900
                        self.jawOpen = 0
                else:
                        self.image,self.imageTimer,self.iterationNumber,self.increment,self.cycled = determineImage(self.dyingHandList,self.imageTimer,self.iterationNumber,self.increment,self.cycled)
                        win.blit(self.image,(self.currentX,self.currentY))
                        win.blit(self.faceImage,(self.faceX,self.faceY))
                        self.closeMouth()
        
                        
               
                        #self.faceX,self.faceY = findTarget(self.faceX,1500,self.faceY,900,3)
       # def summonTitan(self):
                #self.summonTitanTimer += 1
                #if self.summonTitanTimer >= 3:
                        #Orb.orblist.append(Orb(self,self.target,44))
                        
        def adjustMinionRespawn(self):
                print(self.simonCycleLevel)
                if self.simonCycleLevel == 1:
                        return 5
                elif self.simonCycleLevel == 2:
                        return 4
                else:
                        return 3
                    
        def openMouth(self):
                self.jawOpen += 1
                if self.jawOpen <= 30:
                        self.faceImage = simon1
                elif self.jawOpen > 30 and self.jawOpen <= 60:
                        self.faceImage = simon2
                else:
                        self.respawnRate = self.adjustMinionRespawn()
                        self.faceImage = simon3
                        self.jawOpen = 90
                        if self.spitTimer == None:
                                self.spitStart = pygame.time.get_ticks()
                        self.spitTimer = int((pygame.time.get_ticks() - self.spitStart) / 1000)
                        #print(self.spitTimer)
                        if self.spitTimer == self.respawnRate:
                                Orb.orbList.append(Orb(self,self.target,4))
                                self.spitTimer = None
                                #self.summonTitan()
                        
                
        def climb(self):
                if not self.simonSoundPlayed and self.simonCycleLevel == 1:
                        simonSound.play()
                        self.simonSoundPlayed = True
                elif not self.simonSoundPlayed and self.simonCycleLevel == 2:
                        simonSound2.play()
                        self.simonSoundPlayed = True
                elif not self.simonSoundPlayed and self.simonCycleLevel == 3:
                        simonSound2.play()
                        self.simonSoundPlayed = True
                        
                if self.health > 0:
                        self.currentX,self.currentY = findTarget(self.currentX,self.harborX,self.currentY,self.harborY,5)
                        self.faceX,self.faceY = findTarget(self.faceX,self.harborFaceX,self.faceY,self.harborFaceY,3)
                        drawTakeDamage(self,2)
                        win.blit(self.faceImage,(self.faceX,self.faceY))
                        if self.currentX == self.harborX and self.faceX == self.harborFaceX:       
                                self.openMouth()
                else:
                        self.fallDown()
                                
                        
                        

simon = Simon()
def skeleRngSound():
        randomNum = random.randint(1,2)
        if randomNum == 1:
                gruntSound.play()
        else:
                gruntSound2.play()
        


class Lazer:
        letter = None
        off = False
        foundLocation = True
        lazerLetterList = ['a','b','c','d','g','h','i','j','k','l','m','n','o','p','s','t','u','v','x','y','z']
        
        def __init__(self,lazerNum,currentX,currentY,name):
                self.lazerNum = lazerNum
                self.currentX = currentX
                self.currentY = currentY
                self.name = name
                if self.name == 'L1' or self.name == 'L4':
                        print('L1 and L4 made')
                        self.destinationX = random.randint(10,150)
                        if self.name == 'L1':
                                self.destinationY = random.randint(550,660)
                        elif self.name == 'L4':
                                self.destinationY = random.randint(670,780)
                elif self.name == 'L2' or self.name == 'L3':
                        print('L2 and L3 made')
                        self.destinationX = random.randint(150,280)
                        if self.name == 'L2':
                                self.destinationY = random.randint(560,650)
                        elif self.name == 'L3':
                                self.desinationY = random.randint(670,780)
                
        def shootLazer(self):
                #for i in lettterList:
                if self.on == True:
                        if not self.setup:
                                self.letter = random.choice(lazerLetterList)
                                self.setup = True
                        
L1 = Lazer(1,random.randint(10,150),random.randint(550,660),'L1')   #top left
L2 = Lazer(2,random.randint(155,280),random.randint(550,660),'L2') #top right
L3 = Lazer(3,random.randint(155,280),random.randint(670,780),'L3') #bottom right
L4 = Lazer(4,random.randint(10,150),random.randint(670,780),'L4')   #bottom left
#L4 = Lazer(4,random.randint(0,150),random.randint(           
lazerList1 = [L1,L2]
lazerList2 = [L1,L2,L3,L4]
lazerLists = [lazerList1,lazerList2]




                
                
                
        
class SC:
        flames = False
        breathing = False
        thisEnd = False
        death = False

class valkenClass:
        name = 'Valken'
        alive = True
        harborX = 470
        currentX = 900
        harborY = 190
        currentY = 30
        destinationX = 0
        destinationY = 0
        destinationReady = True
        startImmunity = False
        immuneActive = False

        ogSizeX = 200
        ogSizeY = 200
        sizeX = 250  #was 300 before p1 changes
        sizeY = 250  #was 300 before p1 changes
        shrunk = False

        faceNumber = 0
        faceTimer = 50
        
        speed = 2
        charge = 0
        chargeRate = .2
        reflect = False
        level = 1
        health = 1200
        fullHealth = 1200
        image = valkenOne
        damageImage = valkenTakingDamage2
        phase = 1
        laughing = False
        valkenLaughID = 4
        laughingTimer = 100
        puking = False
        pukingAnimation = False
        pukeSoundOnce = False
        pukeTimer = 230
        pukeAFlyTimer = 0
        pukeFlysCounter = 0
        pukedFlysList = []
        flysToPuke = 10
        flysPuked = 0
        valkenPukeList = [valkenPuke0,valkenPuke1,valkenPuke2,valkenPuke3,valkenPuke4]
        
        returningPhase = False
        
        resetBoss = False  #change to true
        
        drawID = 1
        damageTimer = 2
        takingDamageSound = valkenTakingDamageSound
        lSoundWave = lSoundWave
        rSoundWave = rSoundWave
        uSoundWave = uSoundWave
        dSoundWave = dSoundWave
        ulSoundWave = ulSoundWave
        urSoundWave = urSoundWave
        dlSoundWave = dlSoundWave
        drSoundWave = drSoundWave
        generateFly = 0

        callMoonSoundOnce = False
        summoningMoon = False
        moonCounter = 0
        shakeFace = 1
        voiceShake = 80

        valkenLaughID = 90
        sX = 200
        bX = 300

        #for p1 valken
        portalMasterLevel = 1
        potraitsList = [p1,p2,p3,p4,p5,p6]
        possessedList = []
        possessionTimer = 0
        possessedPotrait = None
        lastPossession = None
        madePotraitsList = False
        
        destroyedRiftsList = []
        riftsList = [rP1, rP2, rP3, rP4, rP5, rP6, rP7]
        speakList = [naiveSound,noEscapeSound,innocenceSound]
        
        lazersActive = False
        lazerPower = None
        lazerListLength = None
        lazersOffList = []
        #lazerOne = False
        #lazerTwo = False
        #lazerThree = False
        #lazerOneLetter = None
        #lazerTwoLetter = None
        #lazerThreeLetter = None
        
        spellReady = None
        spellStartTimer = None
        castTimer = 5
        
        
        simonActive = False
        playerPortalTaken = False
        exitPortalActive = False

        speakTimerReady = None
        speakTimerMarker = None
        speakCast = None
        speakNumber = 0
        animateSpeaking = False

        sayLength = 50
        said = False
        waydSaid = False
        
        inRift = False

        deathTimers = 1500
        
        #dyingValkenList = []
        #imageTimer =
        #iterationNumber =
        #increment =
        #cycled = False

        
        #def drawUsingPortal(self):
                #self.portalSpinID -= 1
                #if self.portalSpinID == 4:
                        #self.portalSpinImage = 1
                #elif self.portalSpinID == 3:
                        #self.portalSpinImage = 1
                #elif self.portalSpinID == 2:
                        #self.portalSpinImage = 1
                #elif self.portalSpinID == 1:
                        #self.portalSpinImage = 1

        def setupBossTwo(self):
                self.phase = 2
                self.health = self.fullHealth
                self.image = valkenTwo
                self.takingDamageSound = valkenP2TakingDamageSound
                self.currentX = self.harborX
                self.currentY = self.harborY
                self.damageTimer = 2
                
                self.sizeX = 300
                self.sizeY = 300
                self.resetBoss = True
                    
        def deathTransition(self):
                
                if self.alive:
                        if not SC.flames:
                                flamesCracklingSE.play()
                                SC.flames = True
                        
                        flames.changeImage()
                        win.blit(flames.image,(450,100))
                        self.damageTimer = 2
                        self.takingDamageSound.stop()
                        self.deathTimers -= 2
                        self.health = 0
                        if self.deathTimers < 1500 and self.deathTimers >= 1200:
                                self.image = valkenFade1
                                if not SC.breathing:
                                        valkenBreathingSE.play()
                                        SC.breathing = True
                                
                        elif self.deathTimers < 1200 and self.deathTimers >= 800:
                                self.image = valkenFade2
                                
                                
                        else:
                                if self.currentY < 300:
                                        print(self.currentY, 'this is the Y')
                                        self.currentY += .15
                                        if self.deathTimers < 800 and self.deathTimers >= 400:
                                                self.image = valkenHead
                                                if not SC.thisEnd:
                                                        thisIsTheEndSE.play()
                                                        SC.thisEnd = True
                                        else:
                                                self.image = valkenFadeHead
                                                if not SC.death:
                                                        valkenDyingSE.play()
                                                        SC.death = True
                                else:
                                                self.alive = False
               
                        
                        
                                

                        
                #self.image,self.imageTimer,self.iterationNumber,self.increment,self.cycled = determineImage(self.dyingValkenList,self.imageTimer,iterationNumber,self.increment,self.cycled)
                
                
        def checkPortals(self):
                if portalOne.health > 0 and self.currentX >= 600:
                        portalOne.animatePortal(0)
                        drawTakeDamage(portalOne,self.phase)
                        
                elif portalOne.health <= 0:
                        #implement an upgrading unit iteration
                        self.simonActive = True
                        win.blit(portalOff,(portalOne.currentX,portalOne.currentY))
                        portalOne.active = False
                        
                        
                if portalTwo.health > 0 and self.currentX < 600:
                        portalTwo.animatePortal(0)
                        drawTakeDamage(portalTwo,self.phase)
                        
                if portalTwo.health <= 0:
                        #implement an upgrading unit iteration
                        self.simonActive = True
                        win.blit(portalOff,(portalTwo.currentX,portalTwo.currentY))
                        portalTwo.active = False
                        
                        
        def useTeleport(self):
                if self.currentX >= 600:
                        self.image = valkenOne1
                        self.currentX = 0
                        self.currentY = 0
                        portalTwo.damageTimer = 2
                elif self.currentX < 600:
                        self.image = valkenOne
                        self.currentX = 950
                        self.currentY = 0
                        portalOne.damageTimer = 2
                        
        def portalPhase(self,playerMouseX,playerMouseY):
                self.checkPortals()
                if self.currentX >= 600:
                        if playerMouseX in range(self.currentX - 2,self.currentX + self.sizeX + 2) and playerMouseY in range(self.currentY - 2,self.currentY + self.sizeY + 2):
                                self.useTeleport()
                                
                elif self.currentX < 600:
                        if playerMouseX in range(self.currentX - 2,self.currentX + self.sizeX + 2) and playerMouseY in range(self.currentY - 2,self.currentY + self.sizeY + 2):
                                self.useTeleport()

     
        def makeTimeX(self):
                if self.portalMasterLevel == 1:
                        timeX = 150
                elif self.portalMasterLevel == 2:
                        if len(self.potraitsList) > 3:
                                timeX = 100
                        else:
                                timeX = 80
                elif self.portalMasterLevel == 3:
                        if len(self.potraitsList) > 4:
                                timeX = 100
                        else:
                                timeX = 70
                else:
                        self.portalMasterLevel = 4
                        timeX = 100
                return timeX
                    
        def possess(self):
                #print(self.potraitsList)
                for i in self.potraitsList:
                        if i.health < 0:
                                 del self.potraitsList[self.potraitsList.index(i)]
                                 #print(self.potraitsList)
                                
                                
                if len(self.possessedList) <= 0 and len(self.potraitsList) > 1:   # requires no possessed potrait AND at least 2 potraits health above 0
                        self.possessedPotrait = random.choice(self.potraitsList)  #if random.choice in self.possessedList  reroll
                        while self.possessedPotrait == self.lastPossession:
                                self.possessedPotrait = random.choice(self.potraitsList)
                                
                        self.possessedPotrait.possessed = True
                        #self.potraitsList.remove(self.possessedPotrait)
                        self.possessedList.append(self.possessedPotrait)
                        self.lastPossession = self.possessedPotrait


                self.possessionTimer += 1
                timeX = self.makeTimeX()        
                if self.possessionTimer >= timeX and len(self.potraitsList) > 1:
                        self.possessedPotrait.possessed = False
                        #self.potraitsList.append(self.possessedPotrait)
                        self.possessedList.remove(self.possessedPotrait)
                        self.possessionTimer = 0

                elif len(self.potraitsList) <= 1:
                        self.potraitsList[0].possessed = True
                        #for i in self.potraitsList:
                                #i.possessed = False
                        self.lastPossession = None
                                
        def castPotraits(self):
                #possesPotrait()
                if self.portalMasterLevel == 1:
                        if not self.madePotraitsList:
                                self.potraitsList = [p1,p4]
                                self.madePotraitsList = True
                                
                        p1.paint()
                        p4.paint()
                        if p1.health > 0 or p4.health > 0:
                                self.possess()
                                return True
                        
                        else:
                                #p1.currentX = p1.harborX
                                #p4.currentX = p4.harborX
                                self.potraitsList = [p1,p2,p4,p5]
                                for i in self.potraitsList:
                                        i.possessed = False
                                return False
                       
                elif self.portalMasterLevel == 2:
                        p1.paint()
                        p2.paint()
                        p4.paint()
                        p5.paint()
                        if p1.health > 0 or p4.health > 0 or p2.health > 0 or p5.health > 0:
                                self.possess()
                                return True
                        else:
                                self.potraitsList = [p1,p2,p3,p4,p5,p6]
                                for i in self.potraitsList:
                                        i.possessed = False
                                return False
                        
                elif self.portalMasterLevel == 3:
                        p1.paint()
                        p2.paint()
                        p3.paint()
                        p4.paint()
                        p5.paint()
                        p6.paint()
                        if p1.health > 0 or p2.health > 0 or p3.health > 0 or p4.health > 0 or p5.health > 0 or p6.health > 0:
                                self.possess()
                                return True
                        else:
                                self.potraitsList = [p1,p2,p3,p4,p5,p6]
                                for i in self.potraitsList:
                                        i.possessed = False
                                return False

        def resetPortals_Simon_Potraits_Rifts(self):
                portalOne.health = 100
                portalOne.active = True
                portalOne.damageTimer = 2
                portalTwo.health = 100
                portalTwo.active = True
                portalTwo.damageTimer = 2
                
                p1.health = 1
                p2.health = 1
                p3.health = 1
                p4.health = 1
                p5.health = 1
                p6.health = 1

                simon.image = simonHand
                simon.faceImage = simon1
                simon.faceX = 1500
                simon.faceY = 900
                simon.jawOpen = 0
                simon.spitTimer = None
                simon.cycled = False
                simon.simonSoundPlayed = False
                
                rP1.currentX = -600
                rP2.currentX = -600
                rP3.currentX = -600
                rP4.currentX = -600
                rP5.currentX = -600
                rP6.currentX = -600
                rP7.currentX = -600


                if self.portalMasterLevel == 1:
                        rP3.health = 1
                        rP4.health = 1
                elif self.portalMasterLevel == 2:
                        rP1.health = 1
                        rP2.health = 1
                        
                self.playerPortalTaken = False
                self.exitPortalActive = False
                
        def nextCycle(self):
                
                self.health -= 100
                self.startImmunity = False
                simon.health = 100
                simon.simonActive = False
                simon.climbTimer = 0
                self.image = valkenOne
                self.spellReady = None
                self.currentX = 900
                self.currentY = 30
                self.resetPortals_Simon_Potraits_Rifts()
                self.portalMasterLevel += 1
                self.inRift = False
                self.speakTimerReady = None
                simon.simonCycleLevel = self.portalMasterLevel
                self.animateSpeaking = True
                self.sayLength = 100
                imagodSound.play()
                print('moving on')
                
                
        #def setupPotraits():
                #if self.portalMasterLevel == 1:
                       # self.portraitsList = [not p1.active,not p2.active]
                       
               
        def createRifts(self):
                if self.portalMasterLevel == 1:
                        
                        rP1.currentX = 200
                        rP1.currentY = 100

                        rP2.currentX = 200
                        rP2.currentY = 300

                        rP3.currentX = 630
                        rP3.currentY = 135

                        rP4.currentX = 800
                        rP4.currentY = 240

                        rP5.currentX = 740
                        rP5.currentY = 360

                        rP6.currentX = 780
                        rP6.currentY = 430

                        rP7.currentX = 790
                        rP7.currentY = 490
                        
                elif self.portalMasterLevel == 2:
                        
                        rP1.currentX = 200
                        rP1.currentY = 100
                        
                        rP2.currentX = 200
                        rP2.currentY = 300
                        
                        rP3.currentX = 630
                        rP3.currentY = 135
                        
                        rP4.currentX = 800
                        rP4.currentY = 240

                elif self.portalMasterLevel == 3:
                        
                        rP1.currentX = 200
                        rP1.currentY = 100

                        rP2.currentX = 200
                        rP2.currentY = 300
                        

        def checkRiftDamage(self,riftPiece):
                if riftPiece.destroyed and not riftPiece.destructionDamage:
                        if riftPiece == rP2 or riftPiece == rP1:
                                self.health -= 180
                                riftPiece.destructionDamage = True
                        else:
                                self.health -= 180
                                riftPiece.destructionDamage = True

        def awaitDeath(self):
                
                if not self.waydSaid:
                        whatAreYouDoingSE.play()
                        self.waydSaid = True
                        self.health = 100
                self.speak('whatAreYouDoing')
                print(self.animateSpeaking)
                print(self.speakNumber)
                print(self.said)
                #self.image = valkenOne
                self.currentX = 500
                self.currentY = 250
                self.startImmunity = False
                self.immuneActive = False
                if self.health < 0:
                        self.deathTransition()
                
        def rift(self):
                if self.portalMasterLevel == 1:
                        self.createRifts()
                        win.blit(rP1.image,(rP1.currentX,rP1.currentY))
                        win.blit(rP2.image,(rP2.currentX,rP2.currentY))
                        win.blit(rP3.image,(rP3.currentX,rP3.currentY))
                        win.blit(rP4.image,(rP4.currentX,rP4.currentY))
                        
                        if rP5.health > 0:
                                win.blit(valkenR5,(rP5.currentX,rP5.currentY))
                        else:
                                self.checkRiftDamage(rP5)
                                rP5.animateRiftDestruction()
                                #rP5.destroyed = True
                                
                        if rP6.health > 0:        
                                win.blit(valkenR6,(rP6.currentX,rP6.currentY))
                        else:
                                self.checkRiftDamage(rP6)
                                rP6.animateRiftDestruction()
                                #rP6.destroyed = True
                                
                        if rP7.health > 0:        
                                win.blit(valkenR7,(rP7.currentX,rP7.currentY))
                        else:
                                self.checkRiftDamage(rP7)
                                rP7.animateRiftDestruction()
                                #rP7.destroyed = True

                        self.destroyedRiftsList = [rP5.destroyed,rP6.destroyed,rP7.destroyed]        
                        if all(self.destroyedRiftsList):
                                self.nextCycle()

                elif self.portalMasterLevel == 2:
                        #setup healths for pieces
                        self.createRifts()
                        win.blit(rP1.image,(rP1.currentX,rP1.currentY))
                        win.blit(rP2.image,(rP2.currentX,rP2.currentY))
                        
                        if rP3.health > 0:
                                win.blit(valkenR3,(rP3.currentX,rP3.currentY))
                        else:
                                self.checkRiftDamage(rP3)
                                rP3.animateRiftDestruction()
                                
                        if rP4.health > 0:
                                win.blit(valkenR4,(rP4.currentX,rP4.currentY))
                        else:
                                self.checkRiftDamage(rP4)
                                rP4.animateRiftDestruction()

                        self.destroyedRiftsList = [rP3.destroyed,rP4.destroyed]
                        if all(self.destroyedRiftsList):
                                rP1.health = 1
                                rP2.health = 1
                                self.nextCycle()

                elif self.portalMasterLevel == 3:
                        self.createRifts()
                        if rP1.health > 0:
                                win.blit(valkenR1,(rP1.currentX,rP1.currentY))
                        else:
                                self.checkRiftDamage(rP1)
                                rP1.animateRiftDestruction()
                                
                        if rP2.health > 0:
                                win.blit(valkenR2,(rP2.currentX,rP2.currentY))
                        else:
                                self.checkRiftDamage(rP2)
                                rP2.animateRiftDestruction()

                        self.destroyedRiftsList = [rP1.destroyed,rP2.destroyed]
                        if all(self.destroyedRiftsList):
                                self.awaitDeath()
                                
                                
                                
                
                        
        #def shatter(self):
        
                        
        def goPortals(self):
                portalOne.currentX = portalOne.goX
                portalOne.currentY = portalOne.goY
                portalTwo.currentX = portalTwo.goX
                portalTwo.currentY = portalTwo.goY
                
        def fallPortals(self):
                portalOne.currentX = portalOne.harborX
                portalOne.currentY = portalOne.harborY
                portalTwo.currentX = portalTwo.harborX
                portalTwo.currentY = portalTwo.harborY

        def checkNewDestination(self,phase):
                if self.destinationReady:
                        if phase == 1:
                                self.destinationX = random.randint(290,890) #(100,1100)
                                self.destinationY = random.randint(100,101)  #(125,600)  # used to be  150 440
                        else:
                                self.destinationX = random.randint(50,1000)
                                self.destinationY = random.randint(140,400)
                        self.destinationReady = False

        def checkNewDestination(self,phase):
                if self.destinationReady:
                        if phase == 1:
                                self.destinationX = random.randint(290,890) #(100,1100)
                                self.destinationY = random.randint(100,101)  #(125,600)  # used to be  150 440
                        else:
                                self.destinationX = random.randint(50,1000)
                                self.destinationY = random.randint(140,400)
                        self.destinationReady = False
                        
        def castRandomSpell(self):
                
                def castVortex():
                        valkenOrbSound.play()
                        print('casted vortex')
                        Orb.orbList.append(Orb(self,player,7))
                        self.castTimer = 6
                        
                def castFlash():
                        valkenOrbSound.play()
                        print('casted flash')
                        Orb.orbList.append(Orb(self,player,8))
                        self.castTimer = 9
                 
                def castLazers():     
                        if not self.lazersActive:
                                #player.inputList = set()
                                self.lazerPower = random.choice(lazerLists)
                                self.lazerListLength = len(self.lazerPower)
                                for i in self.lazerPower:
                                        i.off = False
                                        i.letter = random.choice(i.lazerLetterList)
                                        #print(i.off)
                                self.lazersActive = True
                                
                                        
                        else:
                                valkenLazerSound.play()
                                print('casting lazers')
                                for i in self.lazerPower:
                                        if i.foundLocation:
                                                
                                                if i == L1 or i == L4:
                                                        i.destinationX = random.randint(10,150)
                                                        i.destinationY = random.randint(550,670)
                                                        
                                                elif i == L2 or i == L3:
                                                        i.destinationX = random.randint(150,280)
                                                        i.destinationY = random.randint(670,780)
                                                i.foundLocation = False
                                        else:
                                                #print('running lazers')
                                                if i.letter in player.inputList:
                                                        i.off = True
                                                        if self.lazerListLength == 2:
                                                                if all([L1.off,L2.off]):
                                                                        self.lazersActive = False
                                                                        player.inputList.clear()
                                        
                                                        elif self.lazerListLength == 4:
                                                                if all([L1.off,L2.off,L3.off,L4.off]):
                                                                        self.lazersActive = False
                                                                        player.inputList.clear()
                                                                        
                                                        #checkLazersOff(self.lazerPower)
                                                        
                                                if not i.off:
                                                        pygame.draw.line(win,red,(self.currentX + self.sizeX / 2, self.currentY + self.sizeY / 2),(i.currentX,i.currentY),2)
                                                        pygame.draw.circle(win,red,(i.currentX,i.currentY),6,6)
                                                        lazerLetterText = rockWell.render(str(i.letter),3,white)
                                                        win.blit(lazerLetterText,(i.currentX,i.currentY))
                                                        i.currentX,i.currentY = findTarget(i.currentX,i.destinationX,i.currentY,i.destinationY,1)
                                                        i.foundLocation = rangeCheckTarget(i.currentX,i.destinationX,i.currentY,i.destinationY)

                                                        #CAST DAMAGE HERE THIS IS WHERE LAZERS ARE DRAWN INDIVIDUALLY AND TICK DAMAGE
                                                        
                                                #pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)
                        #pygame.draw.circle(win,red,(
                                #if self.health < 1100:
                                        #self.lazersActive = False
                                
                if self.currentX > -50:     #lets us know valken is on screen
                        
                        if not self.lazersActive:
                                valkenLazerSound.stop()
                                randomCastList = [castVortex,castLazers] #castVortex,castFlash, put back to list
                        else:
                                castLazers()
                                randomCastList = [castVortex]
                                
                        if self.spellReady == None:
                                self.spellStartTimer = pygame.time.get_ticks()
                        self.spellReady = int((pygame.time.get_ticks() - self.spellStartTimer) / 1000)
                        
                        if self.spellReady == self.castTimer:
                                random.choice(randomCastList)()
                                self.spellReady = None

                #turning off all lazers                
                else:
                        #L1.off = L2.off = L3.off = L4.off = True
                        self.lazersActive = False
                        player.inputList.clear()
                #rngV = random.randint(1,3)
                #if rngV == 1:
                       # Orb.orbList.append(vortex1)
                #elif rngV == 2:
                        #Orb.orbList.append(vortex2)
        def findSpeakLength(self,rngNumber):
                if rngNumber == 0:
                        self.sayLength = 40
                        
                elif rngNumber == 1:
                        self.sayLength = 50
                        
                elif rngNumber == 2:
                        self.sayLength = 85
                
                
        def speak(self,specify):
                if self.animateSpeaking:
                        self.speakNumber += 1
                        if self.currentX < 600 and specify != 'whatAreYouDoing':
                                if self.speakNumber % 2 == 0:
                                        self.image = valkenRSpeak1
                                else:
                                        self.image = valkenRSpeak2
                        else:
                                if self.speakNumber % 2 == 0:
                                        self.image = valkenSpeak1
                                else:
                                        self.image = valkenSpeak2
                                        
                        if self.speakNumber >= self.sayLength and specify != 'whatAreYouDoing':       
                                self.animateSpeaking = False
                                self.speakNumber = 0
                else:
                        if self.currentX < 600 and specify != 'whatAreYouDoing':
                                self.image = valkenOne1
                        elif self.currentX >= 600:
                                self.image = valkenOne
                                
                print('this is timer: ',self.speakTimerReady,' this is cast: ',self.speakCast)
                if specify == 'whatAreYouDoing':
                        if self.speakNumber < 80 and not self.said:
                                self.animateSpeaking = True
                        else:
                                self.said = True
                                self.animateSpeaking = False
                else:
                        
                        if self.speakTimerReady == None:
                                self.speakTimerMarker = pygame.time.get_ticks()
                                self.speakCast = random.randint(6,11)
                                
                        self.speakTimerReady = int((pygame.time.get_ticks() - self.speakTimerMarker) / 1000)
                        
                        
                        if self.speakTimerReady >= self.speakCast:
                                self.animateSpeaking = True
                                rng = random.randint(0,2)
                                self.findSpeakLength(rng)
                                chosenSaying = self.speakList[rng]
                                chosenSaying.play()
                                #chosenSaying = random.choice(self.speakList)()
                                self.speakTimerReady = None
                        
        def cyclePortalMaster(self,playerMouseX,playerMouseY):
                
                if self.health > 0:
                        self.castRandomSpell()
                        if not self.inRift:
                                self.speak(None)
                        #print(playerMouseX,playerMouseY)
                        if self.simonActive:
                                simon.climbTimer += .5
                                if simon.climbTimer >= self.sayLength:
                                        simon.climb()
                                        
                        if portalOne.active or portalTwo.active:
                                self.goPortals()
                                #simon.climb()
                                self.portalPhase(playerMouseX,playerMouseY)
                        else:
                                self.fallPortals()
                                if self.castPotraits() or simon.health > 0:
                                        self.possess()
                                        #self.image = valkenOne
                                        self.startImmunity = True
                                        self.checkNewDestination(1)
                                        self.currentX,self.currentY = findTarget(self.currentX,self.destinationX,self.currentY,self.destinationY,self.speed)
                                        self.destinationReady = rangeCheckTarget(self.currentX,self.destinationX,self.currentY,self.destinationY)
                                        
                                else:
                                        self.currentX = -400
                                        if not self.playerPortalTaken:
                                                print(self.playerPortalTaken,self.exitPortalActive)
                                                self.exitPortalActive = True
                                                self.inRift = True
                                                valkenLazerSound.stop()
                                                exitPortal.animatePortal(1)
                                                if playerMouseX in range(exitPortal.currentX,exitPortal.currentX + exitPortal.sizeX) and playerMouseY in range(exitPortal.currentY,exitPortal.currentY + exitPortal.sizeY):
                                                        win.blit(takePortalText,(exitPortal.currentX + 80,exitPortal.currentY - 50))
                                                        exitPortal.image = exitPortalThree
                                                exitPortal.currentX = 900
                                                exitPortal.currentY = 450
                                                win.blit(exitPortal.image,(exitPortal.currentX,exitPortal.currentY))
                                                
                                        else:
                                                self.rift()
                else:
                        self.deathTransition()
                                
                       
                
        

                                        
                        
        ############################################## phase2 abilities
        def get_Laughing_Image(self):
                
                self.valkenLaughID -= 1
                if self.valkenLaughID >= 3:
                        image = valkenLaugh1

                elif self.valkenLaughID >= 2:
                        image = valkenLaugh2
                        
                elif self.valkenLaughID >= 1:
                        image = valkenLaugh3
                        
                else:
                        self.valkenLaughID = 4
                        image = valkenLaugh1

                return image
                        


                
        def voice(self):

                self.voiceShake -= 5
                if self.voiceShake > 70:
                        self.lSoundWave = pygame.transform.scale(lSoundWave,(self.sX,self.sX))
                        self.rSoundWave = pygame.transform.scale(rSoundWave,(self.sX,self.sX))
                        win.blit(self.lSoundWave,(self.currentX - 190,self.currentY))
                        win.blit(self.rSoundWave,(self.currentX + 170,self.currentY))
                        
                elif self.voiceShake > 60:
                        win.blit(self.ulSoundWave,(self.currentX - 200,self.currentY - 200))
                        win.blit(self.drSoundWave,(self.currentX + 200,self.currentY + 200))
                                 
                elif self.voiceShake > 50:
                        self.uSoundWave = pygame.transform.scale(uSoundWave,(self.bX,self.bX))
                        self.dSoundWave = pygame.transform.scale(dSoundWave,(self.bX,self.bX))
                        win.blit(self.uSoundWave,(self.currentX,self.currentY - 200)) 
                        win.blit(self.dSoundWave,(self.currentX,self.currentY + 200))

                elif self.voiceShake > 40:
                        win.blit(self.urSoundWave,(self.currentX + 170,self.currentY - 170))
                        win.blit(self.dlSoundWave,(self.currentX - 200,self.currentY + 200))
                        
                elif self.voiceShake > 30:
                        self.lSoundWave = pygame.transform.scale(lSoundWave,(self.bX,self.bX))
                        self.rSoundWave = pygame.transform.scale(rSoundWave,(self.bX,self.bX))
                        win.blit(self.lSoundWave,(self.currentX - 190,self.currentY))
                        win.blit(self.rSoundWave,(self.currentX + 170,self.currentY))

                elif self.voiceShake > 20:
                        self.uSoundWave = pygame.transform.scale(uSoundWave,(self.sX,self.sX))
                        self.dSoundWave = pygame.transform.scale(dSoundWave,(self.sX,self.sX))
                        win.blit(self.uSoundWave,(self.currentX,self.currentY - 200))
                        win.blit(self.dSoundWave,(self.currentX,self.currentY + 200))
                                 

                if self.voiceShake < 20:
                                 self.voiceShake = 80

        def activateMoon(self):
                moon.moonFall()
                
        def summonMoon(self):
                if moon.summoned == False:
                        self.summoningMoon = True
                        while self.summoningMoon:
                                if not self.callMoonSoundOnce:
                                        callMoonSound.play()
                                        self.callMoonSoundOnce = True
                                self.moonCounter += 1
                                self.damageTimer = 60
                                win.blit(blackScreen,(0,0))
                                self.voice()
                                
                                if self.shakeFace == 1:
                                        win.blit(valkenVoiceImage,(self.currentX,self.currentY))
                                        self.shakeFace = 2
                                else:
                                        win.blit(valkenVoiceImage,(self.currentX - 5,self.currentY))
                                        self.shakeFace = 1
                                        
                                pygame.display.update()

                                if self.moonCounter > 200:
                                        self.damageTimer = 2
                                        moon.summoned = True
                                        self.summoningMoon = False
                                        
                else:
                        self.activateMoon()
                                

        def activateShrinkers(self):
                if self.sizeX != shrinker.shrinkX or self.sizeY != shrinker.shrinkY:
                                shrinkMachine.loadShrinker(self)
                                
                else:
                        if shrinkMachine.health > 0:
                                self.speed = 8
                                shrinkMachine.loadShrinker(self)
                                #self.shrunk = True

                        else:
                                if not shrinkMachine.shrinkExplodeSoundOnce:
                                        shrinkRaySound.stop()
                                        shrinkExplodeSound.play()
                                        shrinkMachine.shrinkExplodeSoundOnce = True
                                        
                                if shrinkMachine.image != shrinkMachine.shrinkerExplosionList and shrinkMachine.animationTimer <= 30:
                                        shrinkMachine.animateExplosion()
                                else:
                                        pass
                                
                                self.sizeX = self.ogSizeX
                                self.sizeY = self.ogSizeY
                                self.speed = 0
                
        def activateReflectors(self):
                if reflectors.health > 0:
                        reflectors.loadHarborX()
                        
                else:
                        if reflectors.image != shrinkMachine.shrinkerExplosionList and reflectors.animationTimer <= 30:
                                reflectors.animateExplosion()
                        else:
                        
                                reflectors.reset()
                        

                        
        def chargeFlys(self,flysInList):
                for i in flysInList:
                        i.upgrade()
                        
        def callFly(self):
                self.generateFly = random.randint(0,200)
                if self.generateFly == 50:
                        randomFlyX = random.randint(50,1000)
                        randomFlyY = random.randint(150,450)
                        lazerFlyList.append(lazerFly(randomFlyX,randomFlyY))
                                
                
                        
        #def pukeFlys(self):
                #if len(self.pukedFlysList) < 10:
                        #self.pukeFlysCounter += 2
                        #if self.pukeFlysCounter == 20:
                                #spawnX = self.currentX
                                #spawnY = self.currentY
                                #self.pukedFlysList.append(lazerFly,spawnX,spawnY))
                                
                        #for i in self.pukedFlysList:
                                #if not assignedLocation:
                                       # i.assignedX = random.randint(50,1100)
                                        #i.assignedY = random.randint(150,450)
                               # if not i.locationReached:
                                        #findTarget(i.currentX,i.assignedX,i.currentY,i.assignedY,8)
                                        #drawTakeDamage(i,self.phase)
                                        #if i.currentX == i.assignedX and i.currentY == i.assignedY:
                                          #      i.locationReached = True
                               # elif i.locationReached and len(selfFlyList) > 0 and all(self.pukedFlysList):
                                        #combine puked and lazer lists
                                #else:
                                        #i.locationReached = True
                                        #drawTakeDamage(i,self.phase)
                                                      
                                
                        

        def get_Puking_Image(self):
                
                self.pukeTimer -= 1
                if self.pukeTimer >= 200:
                        image = self.valkenPukeList[0]
                        
                elif self.pukeTimer >= 170:
                        image = self.valkenPukeList[1]
                       
                elif self.pukeTimer >= 140:
                        image = self.valkenPukeList[2]
                        
                elif self.pukeTimer >= 110 or self.pukeTimer < 110:
                        vomitRng = random.randint(1,2)
                        self.pukingAnimation = True
                        if vomitRng == 1:
                                image = self.valkenPukeList[3]
                        else:
                                image = self.valkenPukeList[4]
                        
                return image
        
        def puke(self):
                self.puking = True
                if self.flysToPuke > self.flysPuked and self.pukingAnimation:
                        if not self.pukeSoundOnce:
                                pukeSound.play()
                                self.pukeSoundOnce = True
                                
                        self.speed = 14
                        self.pukeAFlyTimer += 1
                        if self.pukeAFlyTimer > 20:
                                self.pukeAFlyTimer = 0
                                self.flysPuked += 1
                                lazerFlyList.append(lazerFly(self.currentX + self.sizeX / 2,self.currentY + self.sizeY / 2))
                                
                else:    
                        
                        if self.flysToPuke == self.flysPuked:
                                self.puking = False
                                self.speed = 5
                                
                        
                        #self.puking = False
                        #reset flystoPuke
                        #reset flysPuked
                                
                                
                #print(len(self.pukedFlysList))
                #if pukedlist != 
                #if len(self.pukedFlysList) < self.flysToPuke and self.pukeAFlyTimer > 50:# and     not all(#use function to get list info on reachedLocations
                        #self.pukeAFlyTimer = 0
                        #self.pukedFlysList.append(lazerFly(self.currentX,self.currentY))
                #else:
                        #self.pukeAFlyTimer += 1
                        
                #if len(self.pukedFlysList) >= 1:
                       # for i in self.pukedFlysList:
                               # if i.health <= 0:
                                       # i.animateExplosion()
                                     #   
                        #for i in self.pukedFlysList:
                                #if i.active == False:
                                        #self.pukedFlysList.remove(i)
                                       # self.flysToPuke -= 1
                                        
                               # if not i.assignedLocation:
                                     #   i.assignedX = random.randint(50,1100)
                                       # i.assignedY = random.randint(150,450)
                                     #   
                              #  if not i.locationReached:
                                      #  i.currentX,i.currentY = findTarget(i.currentX,i.assignedX,i.currentY,i.assignedY,4)
                                       # drawTakeDamage(i,self.phase)
                                      #  print('drawing flys')
                                      #  if i.currentX == i.assignedX and i.currentY == i.assignedY:
                                       #         i.locationReached = True
                                                
                                #elif i.locationReached and len(selfFlyList) > 0 and all(self.pukedFlysList):
                                        #combine puked and lazer lists  #where puking is false?
                              #  else:
                                       # i.locationReached = True
                                        #drawTakeDamage(i,self.phase)
                                
                               
                #else:
                        #self.puking = False
                        
        def preparePhase2(self):
                self.health = 1200
                self.image = valkenTwo
                self.currentX = self.harborX
                self.currentY = self.harborY
                if self.phase == 1:
                        self.phase == 2
                elif self.phase == 2:
                        self.phase == 3

        def checkNewDestination(self,phase):
                if self.destinationReady:
                        if phase == 1:
                                self.destinationX = random.randint(290,890) #(100,1100)
                                self.destinationY = random.randint(100,101)  #(125,600)  # used to be  150 440
                        else:
                                self.destinationX = random.randint(50,1000)
                                self.destinationY = random.randint(140,400)
                        self.destinationReady = False

        def faceShift(self):
                if self.faceTimer < 100:
                        self.faceNumber = 1
                        self.faceTimer += 1
                elif self.faceTimer < 200:
                        self.faceNumber = 2
                        self.faceTimer += 1
                if self.faceTimer >= 200:
                        self.faceNumber = 1
                        self.faceTimer = 0
                
        
        def returning(self):
                self.returningPhase = True
                self.speed = 5
                self.currentX,self.currentY = findTarget(self.currentX,self.harborX,self.currentY,self.harborY,self.speed)
                if self.currentX in range(self.harborX - 6,self.harborX + 6):
                        self.currentX = self.harborX
                        
                if self.currentY in range(self.harborY - 6, self.harborY + 6):
                        self.currentY = self.harborY

                if airlock1.imageX != airlock1.harborX:        
                        airlock1.imageX,airlock1.imageY = findTarget(airlock1.imageX,airlock1.harborX,airlock1.imageY,airlock1.harborY,10)
                if airlock2.imageX != airlock2.harborX:        
                        airlock2.imageX,airlock2.imageY = findTarget(airlock2.imageX,airlock2.harborX,airlock2.imageY,airlock2.harborY,10)
                
                if airlock1.imageX in range(airlock1.harborX - 11,airlock1.harborX + 11) and airlock1.imageY in range(airlock1.harborY - 11, airlock1.harborY + 10):
                        airlock1.imageX = airlock1.harborX
                        airlock1.imageY = airlock1.harborY
                
                if airlock2.imageX in range(airlock2.harborX - 11,airlock2.harborX + 11) and airlock2.imageY in range(airlock2.harborY - 11, airlock2.harborY + 10):
                        airlock2.imageX = airlock2.harborX
                        airlock2.imageY = airlock2.harborY
                        
                         
                if self.currentX == self.harborX and self.currentY == self.harborY and airlock1.imageX == airlock1.harborX and airlock2.imageX == airlock2.harborX:
                        
                        airlock1.reset()
                        airlock2.reset()
                        shrinkMachine.reset()
                        self.returningPhase = False
                        self.flysToPuke = 10
                        self.flysPuked = 0
                        self.pukeTimer = 230
                        self.pukingAnimation = False
                        self.pukeSoundOnce = False
                        shrinkMachine.shrinkRaySoundOnce = False
                        shrinkMachine.shrinkExplodeSoundOnce = False
                        reflectors.explodeSoundOnce = False
                        reflectors.health = 200
                        reflectors.image = reflectorImage
                        reflectors.animationTimer = 1
                        reflectors.animationCounter = 0

                        self.level += 1
                        self.cycle()
                        
                        
        def airlocked(self):
                self.sizeX = 200
                self.sizeY = 200
                self.image = valkenOne
                self.charge += self.chargeRate
                self.callFly()
                if self.charge > 100:
                        self.chargeFlys(lazerFlyList)
                        self.charge = 0

                pygame.draw.rect(win,purple,(455,160,self.charge * 3,30))
            

        def floatSpace(self):
                #self.callFly()
                self.checkNewDestination(2)
                
                if self.health >= self.fullHealth * .80 and self.level == 1:
                        self.reflect = False
                        self.puke()
                        self.currentX,self.currentY = findTarget(self.currentX,self.destinationX,self.currentY,self.destinationY,self.speed)
                        self.destinationReady = rangeCheckTarget(self.currentX,self.destinationX,self.currentY,self.destinationY)
                        
                                
                elif self.health >= self.fullHealth * .60 and self.level == 2:
                        self.reflect = False
                        self.puke()
                        self.activateShrinkers()
                        
                        self.currentX,self.currentY = findTarget(self.currentX,self.destinationX,self.currentY,self.destinationY,self.speed)
                        self.destinationReady = rangeCheckTarget(self.currentX,self.destinationX,self.currentY,self.destinationY)

                elif self.health >= self.fullHealth * .40 and self.level == 3:
                        self.reflect = False
                        self.puke()
                        self.activateShrinkers()
                        self.activateReflectors()

                        self.currentX,self.currentY = findTarget(self.currentX,self.destinationX,self.currentY,self.destinationY,self.speed)
                        self.destinationReady = rangeCheckTarget(self.currentX,self.destinationX,self.currentY,self.destinationY)
                
                        
                elif self.health > self.fullHealth * 0 and self.level == 4:
                        self.reflect = False
                        self.puke()
                        self.activateShrinkers()
                        self.activateReflectors()
                        self.summonMoon()

                        self.currentX,self.currentY = findTarget(self.currentX,self.destinationX,self.currentY,self.destinationY,self.speed)
                        self.destinationReady = rangeCheckTarget(self.currentX,self.destinationX,self.currentY,self.destinationY)
                        
                        #self.activateMoon()
                        
                        
                        
                        #if self.currentX in range(self.destinationX - 10,self.destinationX + 10) and self.currentY in range(self.destinationY - 10,self.destinationY + 10):
                                #self.currentX = self.destinationX
                                #self.currentY = self.destinationY
                                #if self.currentX == self.destinationX and self.currentY == self.destinationY:
                                        #self.destinationReady = True
                                

                else:
                        
                        #self.speed = 3
                        self.reflect = True
                        reflectors.drawTargetReflect(self)
                        self.returning()
            
        def cycle(self):
                self.callFly()
                #if lazerFly.singularity == False:
                        #lazerFlyList.append(testFly)
                        #lazerFly.singularity = True
                #self.callFly()
                rngLaugh = random.randint(1,200)
                if rngLaugh == 100 and not self.laughing:
                        valkenP2Laugh.play()
                        self.laughing = True
                if self.laughing:
                        self.laughingTimer -= 2
                        if self.laughingTimer <= 0:
                                self.laughingTimer = 100
                                self.laughing = False
                                        
                airlock1HealthText = rockWell.render(str(airlock1.health),3,white)
                airlock2HealthText = rockWell.render(str(airlock2.health),3,white)
                airlock1.airlockSpin()
                airlock2.airlockSpin()
                reflectors.checkPlayerReflects()
                
                if airlock1.health <= 0 and airlock2.health <= 0:
                        if not airlock1.SoundOnce or not airlock2.SoundOnce:
                                airlockBrokeSound.play()
                                airlock1.SoundOnce = True
                                airlock2.SoundOnce = True
                                
                        if not self.returningPhase:
                                if airlock1.imageX > -275:
                                        airlock1.imageX,airlock1.imageY = findTarget(airlock1.imageX,-275,airlock1.imageY,airlock1.imageY,3)
                                if airlock2.imageX < 1300:
                                        airlock2.imageX, airlock2.imageY = findTarget(airlock2.imageX,1300,airlock2.imageY,airlock2.imageY,3)
                        win.blit(airlock1.imageBroken,(airlock1.imageX,airlock1.imageY))
                        win.blit(airlock2.imageBroken,(airlock2.imageX,airlock2.imageY))
                        self.floatSpace()
                
                elif airlock1.health <= 0:
                        if not airlock1.SoundOnce:
                                airlockBrokeSound.play()
                                airlock1.SoundOnce = True
                                
                        airlock1.imageX,airlock1.imageY = findTarget(airlock1.imageX,-275,airlock1.imageY,airlock1.imageY,1)
                        win.blit(airlock1.imageBroken,(airlock1.imageX,airlock1.imageY))
                        win.blit(airlock2.imageI,(airlock2.imageX,airlock2.imageY))
                        drawTakeDamage(airlock2,self.phase)
                        win.blit(airlock2HealthText,(airlock2.currentX + airlock2.sizeX / 2 - 15,airlock2.currentY + airlock2.sizeY - 20))
                        self.airlocked()
                        
                elif airlock2.health <= 0:
                        if not airlock2.SoundOnce:
                                airlockBrokeSound.play()
                                airlock2.SoundOnce = True
                                
                        airlock2.imageX,airlock2.imageY = findTarget(airlock2.imageX,1300,airlock2.imageY,airlock2.imageY,1)
                        win.blit(airlock2.imageBroken,(airlock2.imageX,airlock2.imageY))
                        win.blit(airlock1.imageI,(airlock1.imageX,airlock1.imageY))
                        drawTakeDamage(airlock1,self.phase)
                        win.blit(airlock1HealthText,(airlock1.currentX + airlock1.sizeX / 2 - 15,airlock1.currentY + airlock1.sizeY - 20))
                        self.airlocked()
                else:
                        win.blit(airlock1.imageI,(airlock1.imageX,airlock1.imageY))
                        win.blit(airlock2.imageI,(airlock2.imageX,airlock2.imageY))
                        drawTakeDamage(airlock1,self.phase)
                        drawTakeDamage(airlock2,self.phase)
                        win.blit(airlock1HealthText,(airlock1.currentX + airlock1.sizeX / 2 - 15,airlock1.currentY + airlock1.sizeY - 20))
                        win.blit(airlock2HealthText,(airlock2.currentX + airlock2.sizeX / 2 - 15,airlock2.currentY + airlock2.sizeY - 20))
                        self.airlocked()
                        

valken = valkenClass()
                        
'''                       
        #def __init__(self,harborX,harborY,speed,level,sizeX,sizeY):
                
                #self.harborX = harborX
                #self.currentX = harborX
                #self.harborY = harborY
                #self.currentY = harborY

                #self.sizeX = sizeX
                #self.sizeY = sizeY
                
                #self.speed = speed
                #self.level = level
 '''               

class animations:
        
        def __init__(self,image,imageList,imageTimer,iterationNumber,increments,cycled):
                self.image = image 
                self.imageList = imageList
                self.imageTimer = imageTimer
                self.iterationNumber = iterationNumber
                self.increments = increments
                self.cycled = cycled

        def changeImage(self):
                
                self.imageTimer += 1
                print(self.imageTimer)
                if self.imageTimer >= self.increments:
                        self.iterationNumber += 1
                        self.timer = 0
                
                maxIteration = len(self.imageList) - 1
                if self.iterationNumber > maxIteration:
                        self.cycled = True
                        self.iterationNumber = 1

                #print('the iteration is: ',iteration)
                self.image = self.imageList[self.iterationNumber]

flames = animations(f1,[None,f1,f2,f3,f4,f5],0,1,10,False)

class combatText:
        def __init__(self,leftDirection,randomX,randomY,inString):
                self.leftDirection = leftDirection
                self.randomX = randomX
                self.startX = randomX
                self.randomY = randomY
                self.startY = randomY
                self.inString = inString

        def addCombatText(objects,combatList,damageDone):
                if objects.name == 'Moon':
                        pass
                else:
                        combatList.append(combatText(random.randint(1,2),random.randint(objects.currentX + int((objects.sizeX * .10)),objects.currentX + int((objects.sizeX - objects.sizeX *.10)))\
                                                                               ,random.randint(objects.currentY + int((objects.sizeY - objects.sizeY * .15)),objects.currentY + objects.sizeY),int(damageDone)))
        def move(self):
                if self.leftDirection == 1:
                        if self.randomY <= self.startY + 25:
                                self.randomX = self.randomX + 1
                                self.randomY += 1
                        elif self.randomY >= self.startY + 25:
                                self.randomX = self.randomX -1
                                self.randomY += 1
                        
                        
                elif self.leftDirection == 2:
                        if self.randomY <= self.startY + 25:
                                self.randomX = self.randomX -1
                                self.randomY += 1
                        elif self.randomY >= self.startY + 25:
                                self.randomX = self.randomX + 1
                                self.randomY += 1
                                
        def combatTextDraw(self,combatList,currentWeapon,startImmunityOn):
                #for i in combatList:
                if self.randomY > self.startY + 50:
                        del combatList[combatList.index(self)]
                        if combatList == None:
                                combatList = []
                                        
                if combatList != []:
                        #for i in combatList:
                        if self.inString > 0:
                                damageTextColor = red
                        else:
                                damageTextColor = white

                        if startImmunityOn:
                                infoDamage = 'IMMUNE'
                        elif currentWeapon == 'WarHammer' and self.inString == 0:
                                infoDamage = 'missed'
                                damageTextColor = blue
                                
                        else:
                                infoDamage = 'dmg'
                                
                        tempText = rockWell.render(str(self.inString) + ' ' + infoDamage,3,damageTextColor)
                        win.blit(tempText,(self.randomX,self.randomY))
                        self.move()

               
class Timer:
        def __init__(self,time):
                self.time = time
                
class Weapon:
    def __init__(self,name,damage,swapNumber,image):
        self.name = name
        self.damage = damage
        self.swapNumber = swapNumber
        self.image = image
        
    def getName(self):
            return self.name
        
    def swingWeapon(self,targetHealth,activeAbility,stance,immunity,target):
            def determineEffect():
                    if self.name == 'Sword':
                            doubleStrike = random.randint(1,5)
                            if doubleStrike == 1:
                                    effectDamage = self.damage * 2
                                    print('sword doubleStriked', effectDamage)
                                    return effectDamage
                            else:
                                    effectDamage = self.damage
                                    print('no double hit', effectDamage)
                                    return effectDamage
                                
                    elif self.name == 'Axe':
                            extraDamage = random.randint(1,3)
                            if extraDamage == 1:
                                    effectDamage = self.damage + 5
                                    print('axe hit extra 5', effectDamage)
                                    return effectDamage
                            else:
                                    effectDamage = self.damage
                                    print('no extra damage', effectDamage)
                                    return effectDamage
                                
                    elif self.name == 'Mace':
                            effectDamage = self.damage
                            return effectDamage
                    elif self.name == 'WarHammer':
                            hugeHit = random.randint(1,2)
                            if hugeHit == 1:
                                    print('warHammer hit!')
                                    return self.damage
                            else:
                
                                    print('warHammer missed!')
                                    return 0
                                
            def finalDamage(activeAbilitys,stances,effectDamage):
                    if activeAbilitys and not stances:
                            #print('activeQ and offensive stance')
                            effectDamage = effectDamage + 20
                            effectDamage = effectDamage + effectDamage * .20
                            return effectDamage
                    elif activeAbilitys and stances:
                            #print('Brute.qActive, in defensive stance')
                            effectDamage = effectDamage + 20
                            return effectDamage
                    elif not activeAbilitys and not stances:
                            #print('no Brute.qActive, in offensive Stance')
                            effectDamage = effectDamage + effectDamage * .20
                            return effectDamage
                            
                    else:
                            #print('no Brute.qActive, not in offensive Stance')
                            effectDamage = effectDamage
                            return effectDamage
                    
                                        
                   
            if target == 'interface':
                    interfaceDamage = finalDamage(activeAbility,stance,self.damage)
                    return interfaceDamage
                    
                        
            elif immunity and target == 'Valken':
                    print('target is immune')
                    return targetHealth
                
            else:
                    
                    effectDamage = determineEffect()
                    damage = finalDamage(activeAbility,stance,effectDamage)
                    #damage = effectDamage
                    print(damage)
                    targetHealth -= damage
                    return targetHealth

            



#lazers come on#
           #we determine lists used based off lazer level
           #send a setup function through the list that makes each object unique (letter,destination)

class Line:
        def __init__(self,x,y,x2,y2):
                self.x = x 
                self.y = y
                self.x2 = x2 
                self.y2 = y2
class Skull:
        damageSoundList = [skullTakeDamageSound,skullTakeDamageTwoSound]
        damageImage = skullDamageTakenImage
        damageTimer = 2
        drawID = 1
        skullNameList = ['yellow','green','blue']
           
        def __init__(self,damage,currentX,currentY,speed,health,image,switch,active,name,originalHealth,timer,timerOn,sizeX,sizeY):
                self.damage = damage
                self.currentX = currentX
                self.currentY = currentY
                self.speed = speed
                self.health = health
                self.image = image
                self.switch = switch
                self.name = name
                self.originalHealth = originalHealth
                self.timer = timer
                self.timerOn = timerOn
                self.sizeX = sizeX
                self.sizeY = sizeY
                
                
                
class turrentSetup():
        image = r1Image

        def nextImage(self):
                if self.image == r1Image:
                        self.image = r2Image
                elif self.image == r2Image:
                        self.image = r3Image
                elif self.image == r3Image:
                        self.image = r4Image
                elif self.image == r4Image:
                        self.image = r5Image
                elif self.image == r5Image:
                        self.image = r6Image
                elif self.image == r6Image:
                        self.image = r7Image
                elif self.image == r7Image:
                        self.image = r8Image
                elif self.image == r8Image:
                        self.image = r1Image

setupT = turrentSetup()                        
def setHealthBar(currentHealth):
        if currentHealth > 350:
            setColor = green
        elif currentHealth > 200:
            setColor = yellow
        else:
            setColor = red
        
        return setColor
                

def skullHealthBar(currentHealth):
        if currentHealth >70:
                setColor = green
        elif currentHealth > 40:
                setColor = yellow
        else:
                currentHealth > 0
                setColor = red
                
        return setColor

def battleStart(classChosen,boss):
    clock = pygame.time.Clock()    
    global currentSpell
    global resetSpell
    global summonSkulls
        
    
    summonSkulls = False
    
    player = classChosen
    playerName = surfaceCreation.render(player.name,3,(255,0,0))
    letterList = ['a','b','c','d','g','h','i','j','k','l','m','n','o','p','s','t','u','v','x','y','z'] #no user inputs for abilities
    playerInput = set()
    originalPlayerHealth = player.health
    playerDamageTaken = False
    animatePlayerDamage = False
    playerDamagedTimer = 0
    playerDamagedSwitch = 1
    playerTakeDamageSoundList = [playerTakeDamage1,playerTakeDamage2,playerTakeDamage3]    
    bruteDamagedList = [bruteDamageTaken1,bruteDamageTaken2,bruteDamageTaken3]
  
    #def playerTakeDamage(previousHealth,currentHealth,heroImage,heroImageList):
            #if previous != currentHealth:
                    
    valkenImages = []
    skullSoundList = [skullTakeDamageSound,skullTakeDamageTwoSound]
    if summonSkulls == False:
            
            valkenAbilities = ['summonskull','immunity','lazerchain','vortex'] #'immunity','lazerchain','vortex' put back in!
    else:
            valkenAbilities = ['immunity','lazerchain','vortex']

    valken = valkenClass()
    valken.target = player
    valkenName = surfaceCreation.render(valken.name,3,(255,0,0))
    
 
    valkenObjects = []
    spellCounter = 1
    startVortex = 1
    vortexX = 700
    vortexY = 90

    combatDamageTextList = []
    
    #damageDone = 0
    
    if player.name == 'Brute':
        #create the brute weapons
        #global Brute.defensiveStance
        global furyActive
        global warriorUpgrade1
        global warriorUpgrade2
        global experienceMax
        furyActive = False
        furyTimer = 0
        animateFury = False
        weaponUse = True
        warriorUpgrade1 = False
        warriorUpgrade2 = False
        experienceMax = False
        rage = 0
        swordImageList = [sword1,sword2,sword3]
        axeImageList = [axe1,axe2,axe3]
        maceImageList = [mace1,mace2,mace3]
        warHammerImageList = [warHammer1,warHammer2,warHammer3]
        weaponEffectText = 'Chance: hit Twice!'
        sword = Weapon('Sword',3,1,swordImageList[0])
        axe = Weapon('Axe',35,2,axeImageList[0]) #5 starting damage
        mace = Weapon('Mace',4,3,maceImageList[0])
        warHammer = Weapon('WarHammer',11,4,warHammerImageList[0])
        currentWeapon = sword
        
        shoutSoundList = [shout1Sound,shout2Sound,shout3Sound]
        shoutLineOne1 = Line(100,100,250,100)
        shoutLineOne2 = Line(125,160,225,160)
        shoutLineOne3 = Line(150,220,200,220)

        shoutLineTwo1 = Line(300,400,450,550)
        shoutLineTwo2 = Line(300,450,385,530)
        shoutLineTwo3 = Line(300,500,330,530)

        shoutLineThree1 = Line(460,600,460,750)
        shoutLineThree2 = Line(400,625,400,725)
        shoutLineThree3 = Line(340,650,340,700)
                                    
    
    battleStarted = True
    startTime = pygame.time.get_ticks()
    valkenStartTime = pygame.time.get_ticks()
    valkenCastTimer = random.choice([4,5,6])

    #ability variables
    #Brute.qActive = False
    qCoolDownStart = 0
    wPressed = False
    wStart = False
    wSeconds = 9
    wCoolDownStart = 0
    ePressed = False
    
    #def interfaceUpdates(playerClassName):
            #if playerClassName == 'Brute':
                    #win.blit
    def qwerAbility(playerClass, key):
            #global Brute.Brute.defensiveStance
            global warriorUpgrade1
            global warriorUpgrade2
            global experienceMax
            if playerClass == 'Brute':
                    if key == 'f':
                            if Brute.defensiveStance == True:
                                    return False
                            elif Brute.defensiveStance == False:
                                    return True
                    if key == 'r':
                            if player.experience > 500 and warriorUpgrade1 == True:
                                    sword.damage += 10
                                    axe.damage += 15
                                    mace.damage += 1
                                    warHammer.damage += 20
                                    warriorUpgrade1 = False
                                    sword.image = swordImageList[2]
                                    axe.image = axeImageList[2]
                                    mace.image = maceImageList[2]
                                    warHammer.image = warHammerImageList[2]
                                    warriorUpgrade2 = True
                                    player.experience = 0
                                    experienceMax = True
                                    print('sword damage: ', sword.damage,'\naxe damage: ', axe.damage,'\nmace damage: ',mace.damage,'\nwarHammer damage: ', warHammer.damage)
                                    
                            elif player.experience > 500 and not experienceMax:
                                    sword.damage += 10
                                    axe.damage += 15
                                    mace.damage += 1
                                    warHammer.damage += 20
                                    sword.image = swordImageList[1]
                                    axe.image = axeImageList[1] 
                                    mace.image = maceImageList[1]
                                    warHammer.image = warHammerImageList[1]
                                    player.experience = 0
                                    warriorUpgrade1 = True
                                    print('sword damage: ', sword.damage,'\naxe damage: ', axe.damage,'\nmace damage: ',mace.damage,'\nwarHammer damage: ', warHammer.damage)
                                    
                    #elif key == 'r':
                            
                    
                            
                    #elif key == 'r':
                            
    def drawShoutLines():
            pygame.draw.line(win,red,(shoutLineOne1.x,shoutLineOne1.y),(shoutLineOne1.x2,shoutLineOne1.y2),2)
            pygame.draw.line(win,red,(shoutLineOne2.x,shoutLineOne2.y),(shoutLineOne2.x2,shoutLineOne2.y2),2)
            pygame.draw.line(win,red,(shoutLineOne3.x,shoutLineOne3.y),(shoutLineOne3.x2,shoutLineOne3.y2),2)
            
            pygame.draw.line(win,red,(shoutLineTwo1.x,shoutLineTwo1.y),(shoutLineTwo1.x2,shoutLineTwo1.y2),2)
            pygame.draw.line(win,red,(shoutLineTwo2.x,shoutLineTwo2.y),(shoutLineTwo2.x2,shoutLineTwo2.y2),2)
            pygame.draw.line(win,red,(shoutLineTwo3.x,shoutLineTwo3.y),(shoutLineTwo3.x2,shoutLineTwo3.y2),2)

            pygame.draw.line(win,red,(shoutLineThree1.x,shoutLineThree1.y),(shoutLineThree1.x2,shoutLineThree1.y2),2)
            pygame.draw.line(win,red,(shoutLineThree2.x,shoutLineThree2.y),(shoutLineThree2.x2,shoutLineThree2.y2),2)
            pygame.draw.line(win,red,(shoutLineThree3.x,shoutLineThree3.y),(shoutLineThree3.x2,shoutLineThree3.y2),2)
            
            shoutLineOne1.y -= .2
            shoutLineOne1.y2 -= .2
            shoutLineOne2.y -= .2
            shoutLineOne2.y2 -= .2
            shoutLineOne3.y -= .2
            shoutLineOne3.y2 -= .2

            shoutLineThree1.x += .2
            shoutLineThree1.x2 += .2
            shoutLineThree2.x += .2
            shoutLineThree2.x2 += .2
            shoutLineThree3.x += .2
            shoutLineThree3.x2 += .2
            
    def resetShoutLines():
            shoutLineOne1.y = 400
            shoutLineOne1.y2 = 400
            shoutLineOne2.y = 460
            shoutLineOne2.y2 = 460
            shoutLineOne3.y = 520
            shoutLineOne3.y2 = 520

            shoutLineThree1.x = 460
            shoutLineThree1.x2 = 460
            shoutLineThree2.x = 400
            shoutLineThree2.x2 = 400
            shoutLineThree3.x = 340
            shoutLineThree3.x2 = 340
            #shoutLineOne1.y
            
    immuneCounter = 0    
    
    def immuneCast(time_of_immunity):
            if time_of_immunity == 1:
                    print('300 immunity')
                    return 300
                    
            elif time_of_immunity == 2:
                    print('400 immunity')
                    return 400
                
            elif time_of_immunity == 3:
                    print('500 immunity')
                    return 500

                
    yellowSkulls = Skull(50,1300,450,1,100,yellowSkull,False,True,'yellow',100,50,False,100,100)
    greenSkulls = Skull(50,1300,450,1,100,greenSkull,False,True,'green',100,50,False,100,100)
    blueSkulls = Skull(50,1300,450,1,100,blueSkull,False,True,'blue',100,50,False,100,100)
    skullAlignmentTimer = Timer(1000)
    
    def skullTakeDamage(skullType):
            if skullType.name == 'yellow':
                    yellowSkulls.image = skullDamageTakenImage
                    yellowSkulls.currentX -= 2
                     
    def clickedSkulls(mouseCoordinates):
                    skullDamagedSound = random.choice(skullSoundList)
                    if mouseCoordinates[0] in range(yellowSkulls.currentX, yellowSkulls.currentX + 100):
                            if mouseCoordinates[1] in range(yellowSkulls.currentY, yellowSkulls.currentY + 100):
                                    skullDamagedSound.play()
                                    yellowSkulls.health = currentWeapon.swingWeapon(yellowSkulls.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,'skull')
                                    print('hit yellow')
                                    
                    elif mouseCoordinates[0] in range(greenSkulls.currentX, greenSkulls.currentX + 100):
                            if mouseCoordinates[1] in range(greenSkulls.currentY, greenSkulls.currentY + 100):
                                    skullDamagedSound.play()
                                    greenSkulls.health = currentWeapon.swingWeapon(greenSkulls.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,'skull')
                                    print('hit green')
                                    
                    elif mouseCoordinates[0] in range(blueSkulls.currentX, blueSkulls.currentX + 100):
                            if mouseCoordinates[1] in range(blueSkulls.currentY, blueSkulls.currentY + 100):
                                    skullDamagedSound.play()
                                    blueSkulls.health = currentWeapon.swingWeapon(blueSkulls.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,'skull')
                                    print('hit blue')
                                      
    def summonSkull():
            #global Brute.defensiveStance
            global summonSkulls
            def resetSkulls():
                    yellowSkulls.currentX = 1300
                    yellowSkulls.health = 100
                    greenSkulls.currentX = 1300
                    greenSkulls.health = 100
                    blueSkulls.currentX = 1300
                    blueSkulls.health = 100
                    skullAlignmentTimer.time = 1000
                    yellowSkulls.originalHealth = 100
                    greenSkulls.originalHealth = 100
                    blueSkulls.originalHealth = 100
                    
                                   
            def skullHealthBar(currentHealth):
                    if currentHealth >70:
                            setColor = green
                    elif currentHealth > 40:
                            setColor = yellow
                    else:
                            currentHealth > 0
                            setColor = red
                
                    return setColor

            skullYellowBar = skullHealthBar(yellowSkulls.health)
            skullGreenBar = skullHealthBar(greenSkulls.health)
            skullBlueBar = skullHealthBar(blueSkulls.health)
            yellowSkullText = rockWellSmall.render(str(int(yellowSkulls.health)),3,white)
            greenSkullText = rockWellSmall.render(str(int(greenSkulls.health)),3,white)
            blueSkullText = rockWellSmall.render(str(int(blueSkulls.health)),3,white)

            
            
            def drawSkulls(skullName,healthText,healthBar):
                    #if skullName.health < skullName.originalHealth:
                            #skullName.image = skullDamageTakenImage
                            #skullName.originalHealth = skullName.health
                            #skullName.timerOn = True
                    #if skullName.timerOn:
                            
                            #skullName.timer -= 2
                            #print(skullName.timer)
                    #if skullName.timer < 0:
                            #if skullName.name == 'yellow':
                                    #skullName.image = yellowSkull
                            #elif skullName.name == 'green':
                                    #skullName.image = greenSkull
                            #elif skullName.name == 'blue':
                                    #skullName.image = blueSkull
                            #skullName.timer = 50
                            #skullName.timerOn = False
                    #objects,image,switchID,timer,currentPhase
                    
                    drawTakeDamage(skullName,valken.phase)
                    healthNumber = rockWellSmall.render(str(skullName.health),3,white)
                    pygame.draw.rect(win,healthBar,(skullName.currentX,skullName.currentY - 10, skullName.health, 10))
                    win.blit(healthText,(skullName.currentX + 40, skullName.currentY - 30))
                    
                    skullAlignmentTimer.time -= 1
                    skullName.currentX -= skullName.speed
                    
                    if skullName.currentY == 350:
                            skullName.switch = True
                            
                    if skullName.switch:
                            skullName.currentY += skullName.speed
                            
                    if skullName.currentY == 450:
                            skullName.switch = False
                            
                    if not skullName.switch:
                            skullName.currentY -= skullName.speed
                    

                    #if event.type == pygame.MOUSEBUTTONDOWN:
                            #yellowSkulls.health -= 2
                    #yellowSkulls.currentX -= yellowSkulls.speed
                    #if yellowSkulls.currentY == 450:
                            #yellowSkulls.switch = True
                            #print('ya')
                    #if yellowSkulls.switch:
                            #yellowSkulls.currentY += yellowSkulls.speed
                            
                    #if yellowSkulls.currentY == 550:
                            #yellowSkulls.switch = False
                            
                    #if not yellowSkulls.switch:
                            #yellowSkulls.currentY -= yellowSkulls.speed



            if yellowSkulls.health <= 0 and greenSkulls.health <= 0 and blueSkulls.health <= 0:
                    resetSkulls()
                    print('resetting Skulls')
                    summonSkulls = False
                    
                    
                    
            else:
                    #print(yellowSkulls.health,greenSkulls.health,blueSkulls.health)
                    if yellowSkulls.health > 0:
                            drawSkulls(yellowSkulls,yellowSkullText,skullYellowBar)
                    else:
                            yellowSkulls.currentX = 1300
                                    
                    if skullAlignmentTimer.time < 900 and greenSkulls.health > 0:
                            drawSkulls(greenSkulls,greenSkullText,skullGreenBar)
                    else:
                            greenSkulls.currentX = 1300
                         
                    if skullAlignmentTimer.time < 700 and blueSkulls.health > 0:
                            drawSkulls(blueSkulls,blueSkullText,skullBlueBar)
                    else:
                            blueSkulls.currentX = 1300
        
                    if yellowSkulls.currentX == 220:
                            if Brute.defensiveStance:
                                    player.health -= yellowSkulls.damage / 2
                                    
                            else:
                                    player.health -= yellowSkulls.damage
                            yellowSkulls.currentX = 1300
                            yellowSkulls.health = 0
                            
                    if greenSkulls.currentX == 220:
                            if Brute.defensiveStance:
                                    player.health -= greenSkulls.damage / 2
                                    
                            else:
                                    player.health -= greenSkulls.damage
                            greenSkulls.currentX = 1300
                            greenSkulls.health = 0
                    if blueSkulls.currentX == 220:
                            if Brute.defensiveStance:
                                    player.health -= blueSkulls.damage / 2
                                    
                            else:
                                    player.health -= blueSkulls.damage
                            blueSkulls.currentX = 1300
                            blueSkulls.health = 0
                            
            

                    #mouseCoordinates[1] in range(yellowSkulls.currentY, yellowSkulls.currentY - 100):
                    #yellowSkulls.health -= 2
            #win.blit(yellowSkulls.image,(yellowSkulls.currentX,yellowSkulls.currentY))
            #yellowHealthText = rockWellSmall.render(str(yellowSkulls.health),3,white)
            #pygame.draw.rect(win,skullYellowBar,(yellowSkulls.currentX,yellowSkulls.currentY - 10, yellowSkulls.health, 10))
            #win.blit(yellowHealthText,(yellowSkulls.currentX + 40, yellowSkulls.currentY - 30))
    
    #valken.damageTimer = (pygame.time.get_ticks() - valkenDamageNow) / 1000
    
    #takingDamage = False
   
                    
    def checkPlayerDamageTaken(currentHealth,originalHealth):
            if currentHealth < originalHealth:
                    originalHealth = currentHealth
                    return originalHealth,True
            else:
                    originalHealth = originalHealth
                    return originalHealth,False
                
    def checkPhase(phase):
            if phase == 1:
                    phase = 2
                    valken.health = 1200
                    return phase
                
            elif phase == 2:
                    phase = 3
                    valken.health = 1200
                    return phase
            
    def drawTemplate(playerModifier,currentPhase,upgrade1,upgrade2):
            if playerModifier:
                    battleground = furyAnimation
                    win.blit(battleground,(0,0))
            else:
                    if currentPhase == 2:
                            battleground =  battleTemplate2
                    else:
                            battleground = battleTemplate
                    win.blit(battleground,(0,0))
                    
            if upgrade2:
                    currentHero = player.imageList[2]
            elif upgrade1:
                    currentHero = player.imageList[1]
            else:
                    currentHero = player.imageList[0]
                    
            return currentHero        

    def locateDamage(mouseX,mouseY):
            def checkObjects(objects,mouseX,mouseY):
                    objectTarget = objects
                    #print(objectTarget.name)
                    #if objectTarget.name == 'Moon':
                            #if mouseX >= objects.currentX and mouseX <= objects.currentX + objects.sizeX - 1000 and mouseY >= objects.currentY and mouseY <= objects.currentY + objects.sizeY - 1000:
                    if mouseX >= objects.currentX and mouseX <= objects.currentX + objects.sizeX and mouseY >= objects.currentY and mouseY <= objects.currentY + objects.sizeY:
                                    
                            #playObjectSound(objectTarget,'damage')  #takes target and type of sound

                                    
                                    #if objectTarget.name in Skull.skullNameList:
                                            #selectSkullSound = random.choice(objectTarget.damageSoundList)
                                            #selectSkullSound.play()

                            #elif valken.phase == 2:
                                    #if objectTarget.name == 'fly':
                                            #flyDeath.play()
                        

                                    
                            
                #identify class damage to identified target
                            if player.name == 'Brute' and player.resource >= 50:
                                    if valken.phase == 2 and objectTarget.reflect:
                                            objectTarget = player
                                            reflectedSound.play()
                                            reflectors.animateReflected = 200
                                            
                                    if objectTarget.name == 'Potrait' and not objectTarget.possessed:
                                            objectTarget.castPunish(player)
                                            
                                            if Brute.furyOn:
                                                            pass
                                            else:
                                                    player.resource -= 50
                                    else:
                                            
                                            
                                            if Brute.qActive:
                                                    beforeDamageHealth = objectTarget.health
                                                    objectTarget.health = currentWeapon.swingWeapon(objectTarget.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,objectTarget.name)
                                                    damageDone = int(beforeDamageHealth - objectTarget.health)
                                                    combatText.addCombatText(objectTarget,combatDamageTextList,damageDone)
                                                    objectTarget.damageTimer = 30
                                            
                                                    Brute.qActive = False
                                                    qCoolDownStart = pygame.time.get_ticks()
                                            else:
                                                    beforeDamageHealth = objectTarget.health
                                                    objectTarget.health = currentWeapon.swingWeapon(objectTarget.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,objectTarget.name)
                                                    damageDone = int(beforeDamageHealth - objectTarget.health)
                                                    combatText.addCombatText(objectTarget,combatDamageTextList,damageDone)
                                                    objectTarget.damageTimer = 30

                                            if Brute.furyOn:
                                                    pass
                                            else:
                                                    player.resource -= 50
                                                    

                #sounds for objects on click
                            if valken.phase == 1 and objectTarget.name == 'Skeleton' and objectTarget.health > 0:
                                    skeleRngSound()
                            elif valken.phase == 1 and objectTarget.name == 'Skeleton' and objectTarget.health <= 0:
                                    gruntDeadSound.play()
                            
            #if valken.phase == 1:
            if mouseX >= valken.currentX and mouseX <= valken.currentX + valken.sizeX and mouseY >= valken.currentY and mouseY <= valken.currentY + valken.sizeY:
                    if player.name == 'Brute' and player.resource >= 50:
                            
                            if valken.startImmunity:
                                    immunityDamageTakenSound.play()
                                    pass
                            else:
                                    valken.damageTimer = 50   
                                    valken.takingDamageSound.play()
                                
                            if currentWeapon.name == 'Mace' and player.health + currentWeapon.damage / 2 <= 500 and not valken.startImmunity:
                                    player.health += currentWeapon.damage / 2
                                    player.experience += currentWeapon.damage / 10
                                
                            if Brute.qActive:
                                    if valken.reflect:
                                            player.health = currentWeapon.swingWeapon(player.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,valken.name)
                                    else:
                                            valken.health = currentWeapon.swingWeapon(valken.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,valken.name)
                                    player.experience += currentWeapon.damage / 10
                                
                                    Brute.qActive = False
                                    qCoolDownStart = pygame.time.get_ticks()
                            else:
                                    beforeDamageHealth = valken.health
                                    if valken.reflect:
                                            player.health = currentWeapon.swingWeapon(player.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,valken.name)
                                    else:
                                            valken.health = currentWeapon.swingWeapon(valken.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,valken.name)
                                    damageDone = int(beforeDamageHealth - valken.health)
                                    #combatDamageTextList.append(combatText(random.randint(1,2),random.randint(valken.currentX + int((valken.sizeX * .10)),valken.currentX + int((valken.sizeX - valken.sizeX *.10)))\
                                                                       #,random.randint(valken.currentY + int((valken.sizeY - valken.sizeY * .15)),valken.currentY + valken.sizeY),int(damageDone)))#250,290
                                    combatText.addCombatText(valken,combatDamageTextList,damageDone)
                                    player.experience += currentWeapon.damage / 10
                        
                            if Brute.furyOn: 
                                    pass
                            else:
                                    player.resource -= 50
                                
                            if valken.phase == 2:
                                    airlock1.health = 0
                                    airlock2.health = 0

                                                                           ####else:
            if valken.phase == 1:
                    #check first for non killable objects such as actives(portals,levers) etc.
                    if mouseX in range(exitPortal.currentX,exitPortal.currentX + exitPortal.sizeX) and mouseY in range(exitPortal.currentY,exitPortal.currentY + exitPortal.sizeY) and valken.exitPortalActive:
                            valken.playerPortalTaken = True
                            valken.exitPortalActive = False
                            takePortalSound.play()
                        
                    for i in phase1ObjectsList:
                            checkObjects(i,mouseX,mouseY)
                    for i in Orb.orbList:
                            if i.name == 'Skeleton':
                                    checkObjects(i,mouseX,mouseY)
                
                            
            elif valken.phase == 2:
                    for i in phase2ObjectsList:
                            if i.name == 'Moon' and not i.recovered:
                                    pass
                                
                            else:
                                    checkObjects(i,mouseX,mouseY)
                                    
                    for i in lazerFlyList:
                            checkObjects(i,mouseX,mouseY)
                                    
                            
    '''                                   
                        
            elif mouseX >= yellowSkulls.currentX and mouseX <= yellowSkulls.currentX + yellowSkulls.sizeX and mouseY >= yellowSkulls.currentY and mouseY <= yellowSkulls.currentY + yellowSkulls.sizeY:
                    print('hitting yellow plzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
                    objectTarget = yellowSkulls
                    objectTarget.damageTimer = 50
                    selectSkullSound = random.choice(objectTarget.damageSoundList)
                    selectSkullSound.play()
                    

                    beforeDamageHealth = yellowSkulls.health
                    yellowSkulls.health = currentWeapon.swingWeapon(yellowSkulls.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,yellowSkulls.name)
                    damageDone = int(beforeDamageHealth - yellowSkulls.health)
                    combatText.addCombatText(yellowSkulls,combatDamageTextList,damageDone)
                    
            elif mouseX >= greenSkulls.currentX and mouseX <= greenSkulls.currentX + greenSkulls.sizeX and mouseY >= greenSkulls.currentY and mouseY <= greenSkulls.currentY + greenSkulls.sizeY:
                    objectTarget = greenSkulls
                    objectTarget.damageTimer = 50
                    selectSkullSound = random.choice(objectTarget.damageSoundList)
                    selectSkullSound.play()
                    
                    beforeDamageHealth = greenSkulls.health
                    greenSkulls.health = currentWeapon.swingWeapon(greenSkulls.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,greenSkulls.name)
                    damageDone = int(beforeDamageHealth - greenSkulls.health)    
                    combatText.addCombatText(greenSkulls,combatDamageTextList,damageDone)    
                    
            elif mouseX >= blueSkulls.currentX and mouseX <= blueSkulls.currentX + blueSkulls.sizeX and mouseY >= blueSkulls.currentY and mouseY <= blueSkulls.currentY + blueSkulls.sizeY:
                    objectTarget = blueSkulls
                    objectTarget.damageTimer = 50
                    selectSkullSound = random.choice(objectTarget.damageSoundList)
                    selectSkullSound.play()

                    beforeDamageHealth = blueSkulls.health
                    blueSkulls.health = currentWeapon.swingWeapon(blueSkulls.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,blueSkulls.name)
                    damageDone = int(beforeDamageHealth - blueSkulls.health)
                    combatText.addCombatText(blueSkulls,combatDamageTextList,damageDone)
                    
    '''
                    
    #effects
    global poisoned
    poisonImageList = [bruteFormOnePois,bruteFormTwoPois,bruteFormThreePois]
    poisonTally = 0
    poisonText = rockWell.render('POISONED',3,green)

    global flashEffect
    flashEffectList = [flashScreenOne,flashScreenTwo]
    flashTally = 0

    phase1ObjectsList = [portalOne,portalTwo,p1,p2,p3,p4,p5,p6,rP1,rP2,rP3,rP4,rP5,rP6,rP7,simon]
    phase2ObjectsList = [airlock1,airlock2,shrinkMachine,reflectors,moon]
    
    #######################################################
    #(self,name,health,resource,abilityList,imageList,experience)    
    #valken = Class('Valken',1200,5000,valkenAbilities,valkenImages,0)
    ##############################################
    
    #valken.phase = 2
    #valken.currentX = valken.harborX
    #valken.currentY = valken.harborY
    #valken.takingDamageSound = valkenP2TakingDamageSound
    #valken.phase = checkPhase(valken.phase)
    #valken.damageTimer = 2
    #valken.image = valkenTwo
    #resetSpell = True
    #summonSkulls = False
    
    while battleStarted:
        #print('currentX and currentY: ',valken.currentX,' ',valken.currentY,'\n destination x and y: ',valken.destinationX,valken.destinationY)
        #if valken.health <= 0 and phase == 2:
        #print(valken.faceNumber)
        #print(Brute.qActive)
        #valken.phase = 1
        
        #valken.currentX = 900
        #valken.currentY = 30
        #valken.takingDamageSound = valkenP2TakingDamageSound
        
        #if valken.health <= 0:

                #if valken.deathTimers <= -600:
                
                        #valken.phase = 2
                        #resetSpell = True
                        #summonSkulls = False
                        #valken.health = valken.fullHealth
                        #valken.image = valkenTwo
                        #valken.takingDamageSound = valkenP2TakingDamageSound
                        #valken.currentX = valken.harborX
                        #valken.currentY = valken.harborY
                        #valken.damageTimer = 2

                        
                        #valken.sizeX = 300
                        #valken.sizeY = 300
                
        
        event = pygame.event.poll()
        mousePosition = pygame.mouse.get_pos()
        seconds = (pygame.time.get_ticks()-startTime) / 1000
        clock.tick(60) #was at 70 before moon lag
        
        #battle template /playerDrawing / AND Poison Effect
        if player.name == 'Brute':
                currentHero = drawTemplate(animateFury,valken.phase,warriorUpgrade1,warriorUpgrade2)
                        
        if poisoned:
                poisonNumber = player.imageList.index(currentHero)
                if playerDamagedSwitch == 1:
                        win.blit(poisonImageList[poisonNumber],(0,550))
                elif playerDamagedSwitch == 2:
                        win.blit(poisonImageList[poisonNumber],(5,550))
                poisonTally += 1
                win.blit(poisonText,(120,520))
                if Brute.defensiveStance:
                        if poisonTally <= 150:
                                player.health -= .05
                        else:
                                poisonTally = 0
                                poisoned = False        
                else:
                        
                        if poisonTally <= 300:
                                player.health -= .1
                        else:
                                poisonTally = 0
                                poisoned = False
    
        #player damage check animation
        originalPlayerHealth, playerDamageTaken = checkPlayerDamageTaken(player.health,originalPlayerHealth)
        if playerDamageTaken:
                animatePlayerDamage = True
        if not poisoned and animatePlayerDamage:
               currentHeroNumber = player.imageList.index(currentHero)
               playerDamagedSound = random.choice(playerTakeDamageSoundList)
               if player.name == 'Brute':
                       if playerDamagedTimer < 50:
                               playerDamagedTimer += 1
                               if playerDamagedTimer == 1 or playerDamagedTimer == 35:
                                       print('play damage taken sound here')
                                       playerDamagedSound.play()
                               if playerDamagedSwitch == 1:
                                       win.blit(bruteDamagedList[currentHeroNumber],(0,550))
                                       playerDamagedSwitch = 2
                               elif playerDamagedSwitch == 2:
                                       win.blit(bruteDamagedList[currentHeroNumber],(5,550))
                                       playerDamagedSwitch = 1         
                       elif playerDamagedTimer >= 50:
                               playerDamagedTimer = 0
                               animatePlayerDamage = False
                               
        elif poisoned:
                pass
        else:
                win.blit(currentHero,(0,550))
                
       
                
                
        #win.blit(currentHero,(0,550))
        win.blit(playerName,(80,720))
        playerHealthBarColor = setHealthBar(player.health)
        valkenHealthBarColor = setHealthBar(valken.health)
        pygame.draw.rect(win,playerHealthBarColor,(600,680, player.health, 50))
        pygame.draw.rect(win,blue,(600,730,player.resource,50))
        if not experienceMax:
                pygame.draw.rect(win,grey,(600,780,player.experience,20))
        #pygame.draw.rect(win,blue,(600,760,stamina,30))
       
                
        #logic for class Type
        if weaponUse:
                if Brute.defensiveStance:
                        pygame.draw.rect(win,blue,(5,490, 50, 55))
                        win.blit(dStanceIcon,(5,500,))
                        win.blit(oStanceIcon,(70,500))
                
                else:
                        pygame.draw.rect(win,red,(70,490, 50, 55))
                        win.blit(dStanceIcon,(5,500,))
                        win.blit(oStanceIcon,(70,500))
                        
                #weapon interface
                currentWeaponName = rockWell.render(currentWeapon.name,3,blue)
                currentWeaponBaseDamage = rockWell.render('Base Dmg: ' + str(currentWeapon.damage),3,white)
                damageInterface = rockWell.render('Total Strike Damage:',3,white)
                interfaceDamage = currentWeapon.swingWeapon(valken.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,'interface')
        
                if Brute.qActive:
                        interfaceDamage = rockWell.render(str(interfaceDamage),3,red)
                else:        
                        interfaceDamage = rockWell.render(str(interfaceDamage),3,white)
                win.blit(damageInterface,(600,650))
                win.blit(interfaceDamage,(800,650))
                
                
                
                if player.resource < 300:
                        player.resource += .5
                else:
                        player.resource = 300

                if player.resource < 500 and not warriorUpgrade2:
                        player.experience += 4
                        
                        
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                        currentWeapon = sword
                        weaponEffectText = 'Chance: Hit Twice!'
                        print(currentWeapon.name, " was equipped!")
                        
                        
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                        currentWeapon = axe
                        weaponEffectText = 'Chance: Extra Dmg!'
                        print(currentWeapon.name, " was equipped!")
                        
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                        currentWeapon = mace
                        weaponEffectText = 'Chance: To Stun'
                        print(currentWeapon.name, " was equipped!")
                        
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                        currentWeapon = warHammer
                        weaponEffectText = 'Chance: To Miss!'
                        print(currentWeapon.name, " was equipped!")
                        
                weaponEffectAlert = rockWell.render(weaponEffectText,3,white)
                if Brute.qActive:
                        win.blit(bruteQ,(300,625))
                win.blit(weaponEffectAlert,(300,600))
                win.blit(currentWeapon.image,(300,650))
                win.blit(currentWeaponName,(330,780))
                win.blit(currentWeaponBaseDamage,(300,630))
        
        #abilities for classes
                
        qSeconds = (pygame.time.get_ticks() - qCoolDownStart) / 1000
        if wStart:
                wSeconds = (pygame.time.get_ticks() - wCoolDownStart) / 1000
                
        #print(wSeconds)
        if event.type == pygame.KEYDOWN: 
                keyGiven = event.unicode
                print(keyGiven)
                if keyGiven == 'q':
                        if qSeconds >= 5:
                                if Brute.qActive:
                                        pass
                                else:
                                        
                                        Brute.qActive = True
                                        #playSound
                                        print('q activated')
                                
                        else:
                                print('on cd!')
                                
                elif keyGiven == 'w':
                        print('hello')
                        
                        if wSeconds >= 8:
                                
                                wPressed = False
                                
                        if wPressed == False:
                                wStart = True
                                randomShout = random.choice(shoutSoundList)
                                randomShout.play()
                                wCoolDownStart = pygame.time.get_ticks()
                                print('added 25 rage')
                                if player.resource + 25 > 300:
                                        player.resource = 300
                                else:
                                        
                                        player.resource += 50
                                        
                                wPressed = True
                                
                        else:
                                
                                print('on cd')

                elif keyGiven == 'e':
                        if ePressed == False:
                                ePressed = True
                                furyActive = True
                                furySound.play()

                        else:
                                print('on cd')
                                
                elif keyGiven == 'f':
                        
                        Brute.defensiveStance = qwerAbility(player.name,keyGiven)
                        print(Brute.defensiveStance)
                        
                elif keyGiven == 'r':
                        qwerAbility(player.name,keyGiven)
                        
                elif keyGiven == 'b':
                        if furyTimer > 300:
                                furyTimer = 0
                                ePressed = False
                        furyActive = True
                        #ePressed == False
                        
                #if player.name == 'Brute':
                        #if event.key == pygame.K_f:
                                #Brute.defensiveStance = qwerAbility(player.name,'f',Brute.defensiveStance)
                                #print(Brute.defensiveStance)
                        #elif event.key == pygame.K_q:
                                #print('hello')
                                
        if event.type == pygame.KEYDOWN and event.key != pygame.K_1:
                 if event.type == pygame.KEYDOWN and event.key != pygame.K_2:
                          if event.type == pygame.KEYDOWN and event.key != pygame.K_3:
                                   if event.type == pygame.KEYDOWN and event.key != pygame.K_4:
                                        #print(event.unicode)
                                        #playerInput.add(event.unicode)
                                        player.inputList.add(event.unicode)
                                        print(player.inputList)
                                        
                                        #print(playerInput)
                                        
        #enemyDrawing
        #drawTakeDamage(valken,valken.phase)
        if not valken.alive and boss == 1:
                SoulAttained('valken')
        elif not valken.alive and boss == 2:
                SoulAttained('marv')
                
                
        if boss == 1:
                valken.cyclePortalMaster(mousePosition[0],mousePosition[1])

        drawTakeDamage(valken,valken.phase)

        if valken.startImmunity:
                win.blit(immuneShield,(valken.currentX - 40,valken.currentY - 50))
        if boss == 2:
                #resetSpell = True
                #summonSkulls = False
                if not valken.resetBoss:
                        valken.setupBossTwo()
                valken.cycle()
        
        #drawTakeDamage(valken,valken.phase)                                
        #win.blit(valkenOne,(900,0))
        #win.blit(valkenName,(1000,220))
        pygame.draw.rect(win,valkenHealthBarColor,(280,40, valken.health / 2, 50))
        valkenSeconds = (pygame.time.get_ticks()-valkenStartTime) / 1000
        #print(valkenSeconds)
        
        if resetSpell:
                print('resetting spells')
                spellCast = ''
                resetValkenStartTime = pygame.time.get_ticks()
                valkenStartTime = resetValkenStartTime
                valkenSeconds = (pygame.time.get_ticks()-valkenStartTime) / 1000
                valkenObjects = []
                player.health = player.health
                playerInput = set()
                vortexX = 700
                vortexY = 90
                spellCounter = 1
                currentSpell = False
                resetSpell = False
                
        if valkenSeconds > valkenCastTimer and currentSpell == False and valken.phase != 1 and valken.phase != 2:
                
                
                spellCast = random.choice(valkenAbilities)
                spellPower = random.randint(1,3)
                
                if spellCast == 'lazerchain': #is L
                        lazer1 = Lazer(1,random.choice(letterList),(600,380))
                        lazer2 = Lazer(2,random.choice(letterList),(600,400))
                        lazer3 = Lazer(3,random.choice(letterList),(600,360))
                        valkenObjects.append(lazer1) #valkenObjects[0]
                        valkenObjects.append(lazer2) #valkenObjects[1]
                        valkenObjects.append(lazer3) #valkenObjects[2]
                        
                #damage,positionX,positionY,speed,health,healthBarLength,image        
                elif spellCast == 'summonskull':
                        summonSkulls = True
                        resetSpell = True
                        
                currentSpell = True
                
                
        if currentSpell == True:
                #print(spellCounter)
                if spellCast == 'vortex':
                        startVortex += 1
                        if startVortex > 100:
                                
                                valkenObjects = [1,2,3]
                                vortexX -= 3
                                vortexY += 2
                                valkenObjects[0] = vortexX
                                valkenObjects[1] = vortexY
                                if spellCounter == 5:
                                        spellCounter = 1
                                else:
                                        spellCounter += 1
                                        
                                valkenObjects[2] = spellCounter
                        else:
                                valkenObjects = [1,2,3]
                                valkenObjects[0] = vortexX
                                valkenObjects[1] = vortexY
                                if spellCounter == 5:
                                        spellCounter = 1
                                else:
                                        spellCounter += 1
                                        
                                valkenObjects[2] = spellCounter
                                
                                
                                
                #print(valkenObjects)
                if spellCast == 'vortex' or spellCast == 'lazerchain':
                        player.health = valkenCast(spellCast,player.health,spellPower,playerInput,valkenObjects)
                elif spellCast == 'immunity':
                        if valken.startImmunity:
                                immuneTimer += 300
                                print(immuneTimer,' 200 was added to this immunity')
                                print(immuneCounter,' is the counter')
                                resetSpell = True
                        else:
                                print(immuneCounter,' counter is at <<<')
                                immuneTimer = immuneCast(spellPower)
                                valken.startImmunity = True
                                resetSpell = True
                        
                
       # for event in pygame.event.get():
                
               # if event.type == pygame.KEYDOWN and event.key != pygame.K_1 or event.type == pygame.KEYDOWN and event.key != pygame.K_2 or event.type == pygame.KEYDOWN and event.key != pygame.K_3 or event.type == pygame.KEYDOWN and event.key != pygame.K_4:
                       # print(event.unicode)
                       # playerInput.add(event.unicode)
               # print(playerInput)
        if summonSkulls:
                summonSkull()
        #if valken.startImmunity:
                #if immuneCounter < immuneTimer:
                        #immuneCounter += 1
                        #win.blit(valkenImmune,(900,0))
                        #immuneText = rockWellLarge.render('IMMUNE',3,white)
                        #win.blit(immuneText,(500,0))
                        #pygame.draw.rect(win,white,(200,40, valken.health / 2, 50))
                #else:
                        #immuneCounter = 0
                        #immuneTimer = 0
                        #valken.startImmunity = False
                        
        #shout ability animation                
        if wSeconds >= 0 and wSeconds <= 5:
                drawShoutLines()
                player.resource += .5
                
        else:
                resetShoutLines()
                
        #fury animation and usage
        #print(eSeconds)       
        #print(furyTimer)
        
        if furyActive:
                if furyTimer < 300:
                        Brute.furyOn = True
                        furyTimer += 2
                        player.resource = 300
                        animateFury = True
                        #play fury sound
                        #draw fury background
                elif furyTimer >= 300 and furyTimer < 1000:
                        furyTimer += 2
                        animateFury = False
                        Brute.furyOn = False
                        #downTime
                elif furyTimer >= 1000:
                        furyTimer = 0
                        ePressed = False
                        furyActive  = False
                #if eSeconds < 4:
                        #draw animations
                        #print('drawing E')
                        #pass
                #else:
                        #furyActive = False
                        
        #damage for brute and assassins
        if event.type == pygame.MOUSEBUTTONDOWN:
                locateDamage(mousePosition[0],mousePosition[1])
                setupT.nextImage()

                '''
                        if valken.startImmunity:
                                immunityDamageTakenSound.play()
                                pass
                        else:
                                valken.damageTimer = 50   
                                valken.takingDamageSound.play()
                                
                        if currentWeapon.name == 'Mace' and player.health + currentWeapon.damage / 2 <= 500 and not valken.startImmunity:
                                player.health += currentWeapon.damage / 2
                                player.experience += currentWeapon.damage / 10
                                
                        if Brute.qActive:
                                valken.health = currentWeapon.swingWeapon(valken.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,'valken')
                                player.experience += currentWeapon.damage / 10
                                
                                Brute.qActive = False
                                qCoolDownStart = pygame.time.get_ticks()
                        else:
                                beforeDamageHealth = valken.health
                                valken.health = currentWeapon.swingWeapon(valken.health,Brute.qActive,Brute.defensiveStance,valken.startImmunity,'valken')
                                damageDone = int(beforeDamageHealth - valken.health)
                                combatDamageTextList.append(combatText(random.randint(1,2),random.randint(valken.currentX + int((valken.sizeX * .10)),valken.currentX + int((valken.sizeX - valken.sizeX *.10)))\
                                                                       ,random.randint(valken.currentY + int((valken.sizeY - valken.sizeY * .15)),valken.currentY + valken.sizeY),int(damageDone)))#250,290
                                player.experience += currentWeapon.damage / 10
                        
                        if Brute.furyOn: 
                                pass
                        else:
                                player.resource -= 50
                                
                        if valken.phase == 2:
                                airlock1.health = 0
                                airlock2.health = 0
                        

        
        if event.type == pygame.MOUSEBUTTONDOWN and mousePosition[1] > 300 and valken.phase == 1:
                takingDamage = False
                if player.name == 'Brute' and player.resource >= 50:
                        if Brute.furyOn:
                                pass
                        else:
                                player.resource -= 50
                                
                        if Brute.qActive:
                                clickedSkulls(mousePosition)
                                Brute.qActive = False
                                qCoolDownStart = pygame.time.get_ticks()
                                
                        else:
                                clickedSkulls(mousePosition)

'''     
        for i in Orb.orbList:
                if i.target != player:  #and i.name == 'Skeleton'
                        i.target = player
                        
                if i.active:
                        
                        i.orbMove()
                        
                        #win.blit(i.image,(i.currentX,i.currentY))
                else:
                        Orb.orbList.remove(i)
                         
        for i in lazerFlyList:
                if i.active:
                        i.flyMove(player)
                else:
                        lazerFlyList.remove(i)

        
                
        for i in combatDamageTextList:
                i.combatTextDraw(combatDamageTextList,currentWeapon.name,valken.startImmunity)                        

        if flashEffect:
                if flashTally < 50:
                        flashTally += 1
                        win.blit(random.choice(flashEffectList),(0,0))
                else:
                        flashTally = 0
                        flashEffect = False
        #player.inputList = set()
        pygame.display.update()
        
        #else:
                #if rng number is = 1 in randint(1,2)
                #play not enough stamina alert

        
        
    #print(playerClassName,playerHealth,playerRage,playerAbilities)
    


def introTutorial(classChosen):
    tutorialScreen = True
    #pygame.key.get_pressed()
    #pressed = pygame.key.get_pressed()
    #tutorialOver = pygame.time.get_ticks()
    #fontInfo = pygame.font.get_fonts()
    #print(fontInfo)
    while tutorialScreen:
        event = pygame.event.poll()
        #secondsTutorial = (pygame.time.get_ticks() - tutorialOver)/1000
        
            
        if classChosen.name == 'Brute':
            win.blit(bruteIntro,(0,0))
            pygame.display.update()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print('next')
                tutorialScreen = False
                Brute.classStorage = classChosen
                BossMap(1)
                #battleStart(classChosen)
                
                
                
    
    
    
def classCreation(classChosen):
    bruteImages = [bruteFormOne,bruteFormTwo,bruteFormThree]
    mageImages = []
    assassinImages = []
    bruteAbilities = ['Shout']
    mageAbilities = ['shield','slow','fireball','arcaneBarrage']
    assassinAbilities = ['shroud']
   
    bruteClass = Brute('Brute',500,300,bruteImages,0)
    battleMageClass = Class('Battle Mage',200,400,mageAbilities,mageImages,0) 
    assassinClass = Class('Assassin',200,100,assassinAbilities,assassinImages,0)
    
    if classChosen == 'brute':
        
        #All weapons start damage is /4 from max damage at full upgrades
        
        introTutorial(bruteClass)
    elif classChosen == 'battleMage':
        introTutorial(battleMageClass)
    elif classChosen == 'assassin':
        introTutorial(assassinClass)


def AbilityPage(boss):
        abilityPage = True
        xStart = yStart = 0
        filler = None
        while abilityPage:
                event = pygame.event.poll()
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                        x, y = event.pos
                        print(x,y)
                        
                if boss == 'valken':
                        win.blit(valkenAbilityPage,(0,0))
                        abilityPage,xStart,yStart = checkBox('valkenPage',xStart,yStart)

                elif boss == 'marv':
                        win.blit(marvAbilityPage,(0,0))
                        abilityPage,xStart,yStart = checkBox('marvPage',xStart,yStart)
                        
                        
                pygame.display.update()

        
def checkBox(ID,x,y):
        #event = pygame.event.poll()
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                print(x,y)

                
        if ID == 1:
                #this is bossMap coordinates for valken rune
                if x in range(908,939) and y in range(337,384):
                        print('in range')
                        win.blit(bMSelectValkenT1,(0,0))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                AbilityPage('valken')
                                print('hit')
                                return False, x, y
                        else:
                                return True, x, y
                else:
                        return True, x, y
                
        elif ID == 'valkenPage':
                #this is valken ability page coordinates
                if x in range(821,1113) and y in range(404,514):
                        win.blit(valkenAbilityPageFight,(0,0))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                battleStart(Brute.classStorage,1)
                                return False, x, y
                        else:
                                return True, x, y
                else:
                        return True, x, y

        elif ID == 'valkenSoul':
                #this is valken Soul Attained Page
                win.blit(valkenSoulAttained,(0,0))
                soulSound.play()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        BossMap(2)
                        return False, x, y
                else:
                        return True, x, y

        elif ID == 2:
                #this is bossMap coordinates for Marv rune
                if x in range(761,797) and y in range(434,484):
                        win.blit(bMSelectMarvT2,(0,0))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                AbilityPage('marv')
                                return False, x, y
                        else:
                                return True, x, y
                else:
                        win.blit(bMNoSelectT2,(0,0))
                        return True, x, y
                #if event.type == pygame.MOUSEBUTTONDOWN:

        elif ID == 'marvPage':
                if x in range(720,1013) and y in range(662,775):
                        win.blit(marvAbilityPageFight,(0,0))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                valken.alive = True
                                valken.resetBoss = False
                                battleStart(Brute.classStorage,2)
                                return False, x, y
                        else:
                                return True, x, y
                else:
                        return True, x, y
                
        
        elif ID == 'clickToContinue':
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                        BossMap('2')
                        return False, x, y
                else:
                        return True, x, y
                
        else:
                return True,x,y
                        
        

def SoulAttained(soul):
        print('made it to soul')
        screen = True
        xStart = yStart = 0
        
        if soul == 'valken':
                while screen:
                        screen,xStart,yStart = checkBox('valkenSoul',xStart,yStart)
                       
                        #screen,xStart,yStart = checkBox('clickToContinue',xStart,yStart)
                        
                        
                        pygame.display.update()
                        
def BossMap(currentBossNumber):
        bossMap = True
        xStart = yStart = 0
        
        while bossMap:        
                win.blit(bMNoSelectT1,(0,0))
                bossMap, xStart, yStart = checkBox(currentBossNumber,xStart,yStart)
                
                        #if xStart in range(908,939) and yStart in range(337,384):
                                #win.blit(bMSelectValkenT1,(0,0))
                                #if event.type == pygame.MOUSEBUTTONDOWN:
                                        #bossMap = False
                                        #valkenClicked = True
        #else:
                #eventPoller()
                #if valkenClicked:
                        #win.blit(valkenAbilityPage,(0,0))
                        #checkBox(
                pygame.display.update()
        
def gameStart():
    gameOn = True
    noSelect = True
    xStart = yStart = 0
    pressed1 = False
    bruteC = False
    mageC = False
    assassinC = False
    while gameOn:
        event = pygame.event.poll()
        if noSelect == True:
            win.blit(classChoice,(0,0))
        pygame.display.update()
        
        dummyHealth = 200

        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEMOTION:
                xStart, yStart = event.pos
                print(xStart,yStart)

        if xStart < 385 and xStart > 0 and event.type == pygame.MOUSEBUTTONDOWN:
            noSelect = False
            bruteC = True
            mageC = assassinC = False
            print(mageC,assassinC)
            win.blit(classChoiceBrute,(0,0))
            pygame.mixer.stop()
            bruteSelect.play()
        elif xStart > 385 and xStart < 808 and event.type == pygame.MOUSEBUTTONDOWN:
            noSelect = False
            mageC = True
            bruteC = assassinC = False
            win.blit(classChoiceMage,(0,0))
            pygame.mixer.stop()
            mageSelect.play()
        elif xStart > 808 and event.type == pygame.MOUSEBUTTONDOWN:
            noSelect = False
            assassinC = True
            bruteC = mageC = False
            win.blit(classChoiceAssassin,(0,0))
            pygame.mixer.stop()
            assassinSelect.play()
        pressed = pygame.key.get_pressed()
        if bruteC == True and pressed[pygame.K_RETURN] and pressed1 == False:
                gameOn = False
                classCreation('brute')
                #BossMap(1)
                
                
            #classCreation('brute')
            #pressed1 = True
        if mageC == True and pressed[pygame.K_RETURN] and pressed1 == False:
            print('You have not yet Unlocked That Class!')
        if assassinC == True and pressed[pygame.K_RETURN] and pressed1 == False:
            print('You have not yet Unlocked That Class!')
                    
                    
                    
                    
                    
                
def MainMenu():
        menu = True
        xStart = yStart = 0
        selected = None
        while menu:
             
                
                event = pygame.event.poll()
                
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                        xStart, yStart = event.pos
                        print(xStart,yStart)


                if xStart >= 790 and xStart <= 1065 and yStart >= 460 and yStart <= 550:
                        win.blit(playSelectMenu,(0,0))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                menu = False
                                gameStart()

                elif xStart >= 788 and xStart <= 1065 and yStart >= 568 and yStart <= 655:
                        selected = win.blit(aboutSelectMenu, (0,0))
                else:
                        selected = win.blit(noSelectMenu,(0,0))

                #if event.type == pygame.MOUSEBUTTONDOWN:
                       # if selected == win.blit(playSelectMenu,(0,0)):
                               # gameStart()
                
                                        
                                        
                        
        
                pygame.display.update()
                
MainMenu()








                
#gameStart()
