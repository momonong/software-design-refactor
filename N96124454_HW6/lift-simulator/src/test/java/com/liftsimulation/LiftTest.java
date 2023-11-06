package com.liftsimulation;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class LiftTest {

    private Lift lift;

    @Before
    public void setUp() {
        lift = new Lift();
    }

    @Test
    public void testInitialFloor() {
        assertEquals("Lift should start at floor 1", 1, lift.getCurrentFloor());
    }

    @Test
    public void testDoorInitiallyClosed() {
        assertFalse("Door should be initially closed", lift.isDoorOpen());
    }

    @Test
    public void testCallLift() {
        lift.call(5, Lift.Direction.UP);
        assertEquals("Lift should move to floor 5 when called", 5, lift.getCurrentFloor());
        assertFalse("Door should be closed after calling lift", lift.isDoorOpen());
    }

    @Test
    public void testOpenDoor() {
        lift.openDoor();
        assertTrue("Door should be open", lift.isDoorOpen());
    }

    @Test
    public void testCloseDoor() {
        lift.openDoor(); // 先開門
        lift.closeDoor(); // 然後關門
        assertFalse("Door should be closed", lift.isDoorOpen());
    }

    @Test
    public void testDingSound() {
        lift.call(3, Lift.Direction.UP); // 電梯到達發出「DING!」
        assertTrue("Ding sound should be made when lift arrives", lift.checkDingSound());
    }

    @Test
    public void testCurrentFloorDisplay() {
        lift.call(6, Lift.Direction.UP);
        assertEquals("Lift display should show current floor", 6, lift.getCurrentFloorDisplay());
    }
}
