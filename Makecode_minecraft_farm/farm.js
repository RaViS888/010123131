let setpos: Position = null
let linemove = 0

player.onItemInteracted(CLOCK, function () {
    gameplay.setWeather(CLEAR)
    gameplay.timeSet(gameplay.time(DAY))
})
player.onItemInteracted(WOODEN_SHOVEL, function () {
    blocks.fill(
    AIR,
    pos(-10, 0, 0),
    pos(10, 0, 10),
    FillOperation.Replace
    )
    blocks.fill(
    GRASS,
    pos(-10, -1, 0),
    pos(10, -1, 10),
    FillOperation.Replace
    )
})
player.onItemInteracted(CARROT, function () {
    agent.setItem(CARROTS, 64, 1)
    agent.teleportToPlayer()
    agent.move(FORWARD, 1)
    setpos = agent.getPosition()
    linemove = 1
    for (let index = 0; index < 5; index++) {
        for (let index = 0; index < 5; index++) {
            agent.till(FORWARD)
            agent.move(FORWARD, 1)
            agent.setSlot(1)
            agent.place(DOWN)
        }
        agent.teleportToPlayer()
        agent.turn(LEFT_TURN)
        agent.move(FORWARD, linemove)
        linemove += 1
        agent.turn(RIGHT_TURN)
        agent.move(FORWARD, 1)
    }
    agent.teleportToPlayer()
    agent.turn(LEFT_TURN)
    agent.move(FORWARD, 2)
    agent.turn(RIGHT_TURN)
    agent.move(FORWARD, 4)
    agent.destroy(DOWN)
    agent.move(DOWN, 1)
    blocks.place(WATER, agent.getPosition())
    agent.setItem(LOG_OAK, 64, 27)
    agent.setItem(OAK_FENCE, 64, 26)
    agent.collectAll()
    agent.teleportToPlayer()
    agent.turn(RIGHT_TURN)
    agent.move(FORWARD, 1)
    agent.turn(LEFT_TURN)
    agent.move(FORWARD, 1)
    agent.destroy(DOWN)
    agent.setSlot(27)
    agent.place(DOWN)
    for (let index = 0; index < 3; index++) {
        for (let index = 0; index < 6; index++) {
            agent.move(FORWARD, 1)
            agent.destroy(DOWN)
            agent.collectAll()
            agent.setSlot(27)
            agent.place(DOWN)
            agent.setSlot(26)
            agent.place(BACK)
        }
        agent.turn(LEFT_TURN)
    }
    agent.move(FORWARD, 1)
    agent.place(BACK)
    agent.teleportToPlayer()
})
player.onChat("come", function () {
    agent.teleportToPlayer()
})
player.onItemInteracted(SEEDS, function () {
    agent.setItem(CARROTS, 64, 1)
    agent.teleportToPlayer()
    linemove = 1
    for (let index = 0; index < 5; index++) {
        for (let index = 0; index < 5; index++) {
            agent.move(FORWARD, 1)
            agent.setSlot(1)
            agent.place(FORWARD)
        }
        agent.teleportToPlayer()
        agent.turn(LEFT_TURN)
        agent.move(FORWARD, linemove)
        linemove += 1
        agent.turn(RIGHT_TURN)
    }
    agent.teleportToPlayer()
})
player.onChat("clr", function () {
    gameplay.setWeather(CLEAR)
    gameplay.timeSet(gameplay.time(DAY))
})
player.onItemInteracted(STONE_HOE, function () {
    agent.teleportToPlayer()
    setpos = agent.getPosition()
    linemove = 1
    agent.turn(LEFT_TURN)
    for (let index = 0; index < 5; index++) {
        for (let index = 0; index < 5; index++) {
            agent.move(FORWARD, 1)
            agent.destroy(FORWARD)
            agent.collect(CARROT)
            agent.collect(POTATO)
        }
        agent.teleportToPlayer()
        agent.turn(LEFT_TURN)
        agent.move(FORWARD, linemove)
        linemove += 1
        agent.turn(RIGHT_TURN)
    }
    agent.teleportToPlayer()
})
