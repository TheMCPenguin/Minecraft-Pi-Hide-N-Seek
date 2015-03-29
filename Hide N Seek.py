#Multiplayer Hide and Seek By TheMCPenguin.
#See README.txt before use. INSTRUCTIONS.txt contains... well... instructions.
import sys, random
sys.path.append("./mcpi/api/python/mcpi")
import minecraft
mc = minecraft.Minecraft.create()
mc.setting("world_immutable", True)
mc.setting("nametags_visible", False)
question = raw_input("How many players? ")

if question == ("1"):
    entityIds = mc.getPlayerEntityIds()
    entity1 = entityIds[0]
    mc.entity.setPos(entity1, 8.5, 3.5, -27.5)

if question == ("2"):
    entityIds = mc.getPlayerEntityIds()
    entity1 = entityIds[0]
    entity2 = entityIds[1]
    mc.entity.setPos(entity1, 8.5, 3.5, -27.5)
    mc.entity.setPos(entity2, 8.5, 3.5, 8.7)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos1 = mc.entity.getPos(entity1)
            if hitPos == pos1:
                mc.entity.setPos(entity1, 22.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos2 = mc.entity.getPos(entity2)
            if hitPos == pos2:
                mc.entity.setPos(entity2, 18.5, 32, -9)

if question == ("3"):
    entityIds = mc.getPlayerEntityIds()
    entity1 = entityIds[0]
    entity2 = entityIds[1]
    entity3 = entityIds[2]
    mc.entity.setPos(entity1, 8.5, 3.5, -27.5)
    mc.entity.setPos(entity2, 8.5, 3.5, 8.7)
    mc.entity.setPos(entity3, -9.5, 3.5, -9.5)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos1 = mc.entity.getPos(entity1)
            if hitPos == pos1:
                mc.entity.setPos(entity1, 22.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos2 = mc.entity.getPos(entity2)
            if hitPos == pos2:
                mc.entity.setPos(entity2, 18.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos3 = mc.entity.getPos(entity3)
            if hitPos == pos3:
                mc.entity.setPos(entity3, 14.5, 32, -9)

if question == ("4"):
    entityIds = mc.getPlayerEntityIds()
    entity1 = entityIds[0]
    entity2 = entityIds[1]
    entity3 = entityIds[2]
    entity4 = entityIds[3]
    mc.entity.setPos(entity1, 8.5, 3.5, -27.5)
    mc.entity.setPos(entity2, 8.5, 3.5, 8.7)
    mc.entity.setPos(entity3, -9.5, 3.5, -9.5)
    mc.entity.setPos(entity4, 26.5, 3.5, -9.5)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos1 = mc.entity.getPos(entity1)
            if hitPos == pos1:
                mc.entity.setPos(entity1, 22.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos2 = mc.entity.getPos(entity2)
            if hitPos == pos2:
                mc.entity.setPos(entity2, 18.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos3 = mc.entity.getPos(entity3)
            if hitPos == pos3:
                mc.entity.setPos(entity3, 14.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos4 = mc.entity.getPos(entity4)
            if hitPos == pos4:
                mc.entity.setPos(entity4, 6.5, 32, -9)

if question == ("5"):
    entityIds = mc.getPlayerEntityIds()
    entity1 = entityIds[0]
    entity2 = entityIds[1]
    entity3 = entityIds[2]
    entity4 = entityIds[3]
    entity5 = entityIds[4]
    mc.entity.setPos(entity1, 8.5, 3.5, -27.5)
    mc.entity.setPos(entity2, 8.5, 3.5, 8.7)
    mc.entity.setPos(entity3, -9.5, 3.5, -9.5)
    mc.entity.setPos(entity4, 26.5, 3.5, -9.5)
    mc.entity.setPos(entity5, 21.5, 3.5, 3.5)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos1 = mc.entity.getPos(entity1)
            if hitPos == pos1:
                mc.entity.setPos(entity1, 22.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos2 = mc.entity.getPos(entity2)
            if hitPos == pos2:
                mc.entity.setPos(entity2, 18.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos3 = mc.entity.getPos(entity3)
            if hitPos == pos3:
                mc.entity.setPos(entity3, 14.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos4 = mc.entity.getPos(entity4)
            if hitPos == pos4:
                mc.entity.setPos(entity4, 6.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos5 = mc.entity.getPos(entity5)
            if hitPos == pos5:
                mc.entity.setPos(entity5, 6.5, 32, -9)

if question == ("6"):
    entityIds = mc.getPlayerEntityIds()
    entity1 = entityIds[0]
    entity2 = entityIds[1]
    entity3 = entityIds[2]
    entity4 = entityIds[3]
    entity5 = entityIds[4]
    entity6 = entityIds[5]
    mc.entity.setPos(entity1, 8.5, 3.5, -27.5)
    mc.entity.setPos(entity2, 8.5, 3.5, 8.7)
    mc.entity.setPos(entity3, -9.5, 3.5, -9.5)
    mc.entity.setPos(entity4, 26.5, 3.5, -9.5)
    mc.entity.setPos(entity5, 21.5, 3.5, 3.5)
    mc.entity.setPos(entity6, -4.5, 3.5, 22.6)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos1 = mc.entity.getPos(entity1)
            if hitPos == pos1:
                mc.entity.setPos(entity1, 22.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos2 = mc.entity.getPos(entity2)
            if hitPos == pos2:
                mc.entity.setPos(entity2, 18.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos3 = mc.entity.getPos(entity3)
            if hitPos == pos3:
                mc.entity.setPos(entity3, 14.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos4 = mc.entity.getPos(entity4)
            if hitPos == pos4:
                mc.entity.setPos(entity4, 6.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos5 = mc.entity.getPos(entity5)
            if hitPos == pos5:
                mc.entity.setPos(entity5, 6.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos6 = mc.entity.getPos(entity6)
            if hitPos == pos6:
                mc.entity.setPos(entity6, 2.5, 32, -9)

if question == ("7"):
    entityIds = mc.getPlayerEntityIds()
    entity1 = entityIds[0]
    entity2 = entityIds[1]
    entity3 = entityIds[2]
    entity4 = entityIds[3]
    entity5 = entityIds[4]
    entity6 = entityIds[5]
    entity7 = entityIds[6]
    mc.entity.setPos(entity1, 8.5, 3.5, -27.5)
    mc.entity.setPos(entity2, 8.5, 3.5, 8.7)
    mc.entity.setPos(entity3, -9.5, 3.5, -9.5)
    mc.entity.setPos(entity4, 26.5, 3.5, -9.5)
    mc.entity.setPos(entity5, 21.5, 3.5, 3.5)
    mc.entity.setPos(entity6, -4.5, 3.5, 22.6)
    mc.entity.setPos(entity7, -4.5, 3.5, 3.5)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos1 = mc.entity.getPos(entity1)
            if hitPos == pos1:
                mc.entity.setPos(entity1, 22.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos2 = mc.entity.getPos(entity2)
            if hitPos == pos2:
                mc.entity.setPos(entity2, 18.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos3 = mc.entity.getPos(entity3)
            if hitPos == pos3:
                mc.entity.setPos(entity3, 14.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos4 = mc.entity.getPos(entity4)
            if hitPos == pos4:
                mc.entity.setPos(entity4, 6.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos5 = mc.entity.getPos(entity5)
            if hitPos == pos5:
                mc.entity.setPos(entity5, 6.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos6 = mc.entity.getPos(entity6)
            if hitPos == pos6:
                mc.entity.setPos(entity6, 2.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos7 = mc.entity.getPos(entity7)
            if hitPos == pos7:
                mc.entity.setPos(entity7, -1.5, 32, -9)


if question == ("8"):
    entityIds = mc.getPlayerEntityIds()
    entity1 = entityIds[0]
    entity2 = entityIds[1]
    entity3 = entityIds[2]
    entity4 = entityIds[3]
    entity5 = entityIds[4]
    entity6 = entityIds[5]
    entity7 = entityIds[6]
    entity8 = entityIds[7]
    mc.entity.setPos(entity1, 8.5, 3.5, -27.5)
    mc.entity.setPos(entity2, 8.5, 3.5, 8.7)
    mc.entity.setPos(entity3, -9.5, 3.5, -9.5)
    mc.entity.setPos(entity4, 26.5, 3.5, -9.5)
    mc.entity.setPos(entity5, 21.5, 3.5, 3.5)
    mc.entity.setPos(entity6, -4.5, 3.5, 22.6)
    mc.entity.setPos(entity7, -4.5, 3.5, 3.5)
    mc.entity.setPos(entity8, 21.5, 3.5, 22.5)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos1 = mc.entity.getPos(entity1)
            if hitPos == pos1:
                mc.entity.setPos(entity1, 22.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos2 = mc.entity.getPos(entity2)
            if hitPos == pos2:
                mc.entity.setPos(entity2, 18.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos3 = mc.entity.getPos(entity3)
            if hitPos == pos3:
                mc.entity.setPos(entity3, 4.5, 34, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos4 = mc.entity.getPos(entity4)
            if hitPos == pos4:
                mc.entity.setPos(entity4, 10.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos5 = mc.entity.getPos(entity5)
            if hitPos == pos5:
                mc.entity.setPos(entity5, 6.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos6 = mc.entity.getPos(entity6)
            if hitPos == pos6:
                mc.entity.setPos(entity6, 2.7, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos7 = mc.entity.getPos(entity7)
            if hitPos == pos7:
                mc.entity.setPos(entity7, -1.5, 32, -9)
    while True:
        hits = mc.events.pollBlockHits()
        for hit in hits:
            x = hit.pos.x
            y = hit.pos.y
            z = hit.pos.z
            hitPos = (x, y, z)
            pos8 = mc.entity.getPos(entity8)
            if hitPos == pos8:
                mc.entity.setPos(entity8, -5.5, 32, -9)
