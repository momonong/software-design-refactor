package com.adaptionsoft.games.uglytrivia;

public class Player {
    private String name;
    private int position = 0;
    private int coins = 0;
    private boolean inPenaltyBox = false;

    public Player(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public int getPosition() {
        return position;
    }

    public void move(int roll, int mapSize) {
        this.position = ((this.position)+roll) % mapSize;
    }

    public int getCoins() {
        return coins;
    }

    public void incrementCoins() {
        this.coins++;
    }

    public boolean isInPenaltyBox() {
        return inPenaltyBox;
    }

    public void sendToPenaltyBox() {
        this.inPenaltyBox = true;
    }

    public void leavePenaltyBox() {
        this.inPenaltyBox = false;
    }
}