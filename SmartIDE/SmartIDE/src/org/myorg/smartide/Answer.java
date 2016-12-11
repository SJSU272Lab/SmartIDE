/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package org.myorg.smartide;

/**
 *
 * @author Janis
 */
public class Answer {
    private String question;
    private String answer;
    private String link;
    // Luckman
    private String id;
    private int vote;
        
    public void setQuestion(String q)
    {
        question = q;
    }
    public String getQuestion()
    {
        return question;
    }
    
    public void setAnswer(String a)
    {
        answer = a;
    }
    public String getAnswer()
    {
        return answer;
    }
    
    public void setLink(String l)
    {
        link = l;
    }
    public String getLink()
    {
        return link;
    }
    
    // Luckman
    public void setId(String s)
    {
        id = s;
    }
    // Luckman
    public String getId()
    {
        return id;
    }
    
    public void setVote(int v)
    {
        vote = v;
    }
    public int getVote()
    {
        return vote;
    }
    
}
