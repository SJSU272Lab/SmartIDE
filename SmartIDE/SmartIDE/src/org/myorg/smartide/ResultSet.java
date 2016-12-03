/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package org.myorg.smartide;

import java.util.ArrayList;

/**
 *
 * @author Janis
 */
public class ResultSet {
    private String question;
    private ArrayList<Answer> result = new ArrayList<>();
    
    public void setQuestion(String q)
    {
        question = q;
    }
    public String getQuestion()
    {
        return question;
    }
    
    public void setResultSet(ArrayList<Answer> r)
    {
        result = r;
    }
    public ArrayList<Answer> getResultSet()
    {
        return result;
    }
    
}
