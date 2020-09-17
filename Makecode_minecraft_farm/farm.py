setpos: Position = None
linemove = 0

def item_interacted_clock():
    gameplay.set_weather(CLEAR)
    gameplay.time_set(gameplay.time(DAY))
player.on_item_interacted(CLOCK, item_interacted_clock)

def item_interacted_wooden_shovel():
    blocks.fill(AIR, pos(-10, 0, 0), pos(10, 0, 10), FillOperation.REPLACE)
    blocks.fill(GRASS,
        pos(-10, -1, 0),
        pos(10, -1, 10),
        FillOperation.REPLACE)
player.on_item_interacted(WOODEN_SHOVEL, item_interacted_wooden_shovel)

def item_interacted_carrot():
    agent.set_item(CARROTS, 64, 1)
    agent.teleport_to_player()
    agent.move(FORWARD, 1)
    setpos = agent.get_position()
    linemove = 1
    for index in range(5):
        for index2 in range(5):
            agent.till(FORWARD)
            agent.move(FORWARD, 1)
            agent.set_slot(1)
            agent.place(DOWN)
        agent.teleport_to_player()
        agent.turn(LEFT_TURN)
        agent.move(FORWARD, linemove)
        linemove += 1
        agent.turn(RIGHT_TURN)
        agent.move(FORWARD, 1)
    agent.teleport_to_player()
    agent.turn(LEFT_TURN)
    agent.move(FORWARD, 2)
    agent.turn(RIGHT_TURN)
    agent.move(FORWARD, 4)
    agent.destroy(DOWN)
    agent.move(DOWN, 1)
    blocks.place(WATER, agent.get_position())
    agent.set_item(LOG_OAK, 64, 27)
    agent.set_item(OAK_FENCE, 64, 26)
    agent.collect_all()
    agent.teleport_to_player()
    agent.turn(RIGHT_TURN)
    agent.move(FORWARD, 1)
    agent.turn(LEFT_TURN)
    agent.move(FORWARD, 1)
    agent.destroy(DOWN)
    agent.set_slot(27)
    agent.place(DOWN)
    for index3 in range(3):
        for index4 in range(6):
            agent.move(FORWARD, 1)
            agent.destroy(DOWN)
            agent.collect_all()
            agent.set_slot(27)
            agent.place(DOWN)
            agent.set_slot(26)
            agent.place(BACK)
        agent.turn(LEFT_TURN)
    agent.move(FORWARD, 1)
    agent.place(BACK)
    agent.teleport_to_player()
player.on_item_interacted(CARROT, item_interacted_carrot)

def on_chat():
    agent.teleport_to_player()
player.on_chat("come", on_chat)

def item_interacted_seeds():
    agent.set_item(CARROTS, 64, 1)
    agent.teleport_to_player()
    linemove = 1
    for index5 in range(5):
        for index6 in range(5):
            agent.move(FORWARD, 1)
            agent.set_slot(1)
            agent.place(FORWARD)
        agent.teleport_to_player()
        agent.turn(LEFT_TURN)
        agent.move(FORWARD, linemove)
        linemove += 1
        agent.turn(RIGHT_TURN)
    agent.teleport_to_player()
player.on_item_interacted(SEEDS, item_interacted_seeds)

def on_chat2():
    gameplay.set_weather(CLEAR)
    gameplay.time_set(gameplay.time(DAY))
player.on_chat("clr", on_chat2)

def item_interacted_stone_hoe():
    agent.teleport_to_player()
    setpos = agent.get_position()
    linemove = 1
    agent.turn(LEFT_TURN)
    for index7 in range(5):
        for index8 in range(5):
            agent.move(FORWARD, 1)
            agent.destroy(FORWARD)
            agent.collect(CARROT)
            agent.collect(POTATO)
        agent.teleport_to_player()
        agent.turn(LEFT_TURN)
        agent.move(FORWARD, linemove)
        linemove += 1
        agent.turn(RIGHT_TURN)
    agent.teleport_to_player()
player.on_item_interacted(STONE_HOE, item_interacted_stone_hoe)
