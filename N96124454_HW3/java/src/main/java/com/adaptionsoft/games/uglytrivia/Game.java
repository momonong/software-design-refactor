package com.adaptionsoft.games.uglytrivia;

import java.util.ArrayList;

public class Game {
    private ArrayList<Player> players = new ArrayList<Player>();
    private static final int MIN_PLAYERS = 2;
    private static final int MAX_PLAYERS = 6;
    
    private QuestionBank questionBank = new QuestionBank();
    
    int currentPlayer = 0;
    boolean isGettingOutOfPenaltyBox;
    
    public Game() {
        questionBank.initializeQuestions();
    }
    
    public boolean isPlayable() {
        return (players.size() >= MIN_PLAYERS && players.size() <= MAX_PLAYERS);
    }

    public boolean add(String playerName) {
        if (players.size() < MAX_PLAYERS) {
            players.add(new Player(playerName));
            System.out.println(playerName + " was added");
            System.out.println("They are player number " + players.size());
            return true;
        }
		System.out.println("Failed to add " + playerName + ". The game has reached its limit of " + MAX_PLAYERS + " players.");
        return false;
    }

    public void roll(int roll) {
        Player player = players.get(currentPlayer);
        System.out.println(player.getName() + " is the current player");
        System.out.println("They have rolled a " + roll);
        
        if (player.isInPenaltyBox()) {
            if (roll % 2 != 0) {
                isGettingOutOfPenaltyBox = true;
				player.getOutOfPenaltyBox();
                System.out.println(player.getName() + " is getting out of the penalty box");
                player.move(roll);
				displayPlayerPosition(player);
            } else {
                System.out.println(player.getName() + " is not getting out of the penalty box");
                isGettingOutOfPenaltyBox = false;
            }
        } else {
            player.move(roll);
			displayPlayerPosition(player);
        }
    }

    public boolean wasCorrectlyAnswered() {
        Player player = players.get(currentPlayer);
        if (player.isInPenaltyBox() && !isGettingOutOfPenaltyBox) {
            currentPlayer = (currentPlayer + 1) % players.size();
            return true;
        }
        
        System.out.println("Answer was correct!!!!");
        player.incrementCoins();
        System.out.println(player.getName() + " now has " + player.getCoins() + " Gold Coins.");
        
        boolean winner = didPlayerWin();
        currentPlayer = (currentPlayer + 1) % players.size();
        return winner;
    }
    
    public boolean wrongAnswer() {
        Player player = players.get(currentPlayer);
        System.out.println("Question was incorrectly answered");
        System.out.println(player.getName() + " was sent to the penalty box");
        player.sendToPenaltyBox();
        
        currentPlayer = (currentPlayer + 1) % players.size();
        return true;
    }

    private boolean didPlayerWin() {
        return players.get(currentPlayer).getCoins() != 6;
    }

	private void displayPlayerPosition(Player player) {
		System.out.println(player.getName() + "'s new location is " + player.getPosition());
        System.out.println("The category is " + questionBank.currentCategory(player.getPosition()));
        questionBank.askQuestion(player.getPosition());
	}

}
