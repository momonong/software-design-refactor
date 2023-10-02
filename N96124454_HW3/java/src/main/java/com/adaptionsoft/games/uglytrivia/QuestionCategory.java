package com.adaptionsoft.games.uglytrivia;

import java.util.LinkedList;

public class QuestionCategory {
    private String name;
    private LinkedList<String> questions = new LinkedList<String>();

    public QuestionCategory(String name, int numQuestions) {
        this.name = name;
        initializeQuestions(numQuestions);
    }

    public String getName() {
        return name;
    }

    public String getNextQuestion() {
        if (questions.isEmpty()) {
            initializeQuestions(50); 
        }
        return questions.removeFirst();
    }

    private void initializeQuestions(int numQuestions) {
        for (int i = 0; i < numQuestions; i++) {
            questions.addLast(name + " Question " + i);
        }
    }
}
