/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package org.myorg.smartide;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JTextArea;
import javax.swing.text.JTextComponent;
import org.netbeans.api.editor.EditorRegistry;
import org.openide.cookies.EditorCookie;
import org.openide.awt.ActionID;
import org.openide.awt.ActionReference;
import org.openide.awt.ActionReferences;
import org.openide.awt.ActionRegistration;
import org.openide.util.NbBundle.Messages;
import org.openide.windows.WindowManager;

@ActionID(
        category = "Debug",
        id = "org.myorg.smartide.SmartFix"
)
@ActionRegistration(
        iconBase = "org/myorg/smartide/wand16.png",
        displayName = "#CTL_SmartFix"
)
@ActionReferences({
    @ActionReference(path = "Menu/Window", position = 1050, separatorBefore = 1025, separatorAfter = 1075)
    ,
  @ActionReference(path = "Editors/text/x-java/Popup", position = 1455, separatorBefore = 1442, separatorAfter = 1467)
})
@Messages("CTL_SmartFix=Smart Fix")
public final class SmartFix implements ActionListener {

    private final EditorCookie context;

    public SmartFix(EditorCookie context) {
        this.context = context;
    }

    @Override
    public void actionPerformed(ActionEvent ev) {
        JTextComponent editor = EditorRegistry.lastFocusedComponent();
        String selection = editor.getSelectedText();
                
        SmartFixTopComponent smartFix = (SmartFixTopComponent) WindowManager.getDefault().findTopComponent("SmartFixTopComponent");
        
        if(!smartFix.isOpened())
            smartFix.open();
        smartFix.requestFocus();
        smartFix.requestActive();
        
        JTextArea text = smartFix.getTextArea();
        text.setText(selection);
        
        // BELOW CODE LAUNCHES BROWSER WITH SEARCH TERMS
        /*
        if(selection != null)
        try {
            String searchText = URLEncoder.encode(selection, "UTF-8");
            HtmlBrowser.URLDisplayer.getDefault().showURL(new URL("http://www.google.com/search?hl=en&q=" + searchText));
        } catch (Exception eee) {
            return;
        }*/
    }
}
