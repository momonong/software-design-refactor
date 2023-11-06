package com.liftsimulation;

public class Lift {

    private int currentFloor;
    private boolean doorOpen;
    private Direction currentDirection;

    public Lift() {
        // 初始化電梯在一樓，門是關的
        // 先將方向預設為向上
        this.currentFloor = 1;
        this.doorOpen = false;
        this.currentDirection = Direction.UP; 
    }

    public void call(int floor, Direction direction) {
        // 直接移動到按鈕的樓層
        this.currentFloor = floor;
        this.currentDirection = direction;
        // 電梯到達後自己開門關門
        openDoor();
        closeDoor();
    }

    public int getCurrentFloor() {
        return currentFloor;
    }

    public int getCurrentFloorDisplay() {
        // 實作 current floor monitor
        return currentFloor;
    }

    public Direction getCurrentDirection() {
        return currentDirection;
    }

    public void moveToFloor(int floor) {
        // 移動到指定樓層然後打開門
        this.currentFloor = floor;
        this.doorOpen = true;
    }

    public void openDoor() {
        this.doorOpen = true;
    }

    public void closeDoor() {
        this.doorOpen = false;
    }

    public boolean isDoorOpen() {
        return doorOpen;
    }

    public boolean checkDingSound() {
        // 電梯到達樓層會「DING!」
        return true;
    }

    public enum Direction {
        UP, DOWN
    }
}
