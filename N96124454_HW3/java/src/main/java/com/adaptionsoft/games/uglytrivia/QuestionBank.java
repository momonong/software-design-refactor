package com.adaptionsoft.games.uglytrivia;

import java.util.ArrayList;
import java.util.List;

public class QuestionBank {
    private List<QuestionCategory> categories = new ArrayList<QuestionCategory>();


    public String currentCategory(int position) {
        int index = position % categories.size();
        return categories.get(index).getName();
    }

    public void askQuestion(int position) {
        int index = position % categories.size();
        System.out.println(categories.get(index).getNextQuestion());
    }

    public void addCategory(String name, int numQuestions) {
        categories.add(new QuestionCategory(name, numQuestions));
    }

    public void initializeQuestions() {
        categories.add(new QuestionCategory("Pop", 50));
        categories.add(new QuestionCategory("Science", 50));
        categories.add(new QuestionCategory("Sports", 50));
        categories.add(new QuestionCategory("Rock", 50));
    }
}
